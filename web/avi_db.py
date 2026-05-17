"""
Capa mínima SQLite / PostgreSQL para YuweAI.
Si DATABASE_URL está definida (p. ej. Supabase), se usa psycopg; si no, sqlite3.
"""
from __future__ import annotations

import ipaddress
import json
import os
import re
import socket
import ssl
import urllib.parse
import urllib.request
from typing import Any

DATABASE_URL = (os.environ.get("DATABASE_URL") or "").strip()
USE_POSTGRES = bool(DATABASE_URL)


def _host_is_literal_ip(hostname: str) -> bool:
    try:
        ipaddress.ip_address(hostname.split("%")[0])
    except ValueError:
        return False
    return True


def _ipv4_socket_lookup(hostname: str, port: int) -> str | None:
    """Primero solo IPv4; si el SO no devuelve A, prueba AF_UNSPEC y elige la primera IPv4."""
    try:
        infos = socket.getaddrinfo(hostname, port, socket.AF_INET, socket.SOCK_STREAM)
    except OSError:
        infos = []
    if infos:
        return infos[0][4][0]
    try:
        infos = socket.getaddrinfo(hostname, port, type=socket.SOCK_STREAM)
    except OSError:
        return None
    for fam, *_rest, sa in infos:
        if fam == socket.AF_INET:
            return sa[0]
    return None


def _ipv4_gethostbyname(hostname: str) -> str | None:
    """API legacy; a veces devuelve A cuando getaddrinfo(AF_INET) no."""
    try:
        ip = socket.gethostbyname(hostname)
    except OSError:
        return None
    if ":" in ip:
        return None
    return ip


def _a_record_from_dns_json(payload: dict) -> str | None:
    for item in payload.get("Answer", []):
        if item.get("type") != 1 or not item.get("data"):
            continue
        data = str(item["data"]).strip().strip('"')
        if ":" in data:
            continue
        return data
    return None


def _dns_resolve_a_record(hostname: str) -> str | None:
    """DoH (Cloudflare / Google) sin proxy HTTP; respaldo sin verificar TLS solo para leer DNS público."""
    q = urllib.parse.quote(hostname, safe="")
    urls = (
        f"https://1.1.1.1/dns-query?name={q}&type=A",
        f"https://dns.google/resolve?name={q}&type=A",
    )
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    headers = {"Accept": "application/dns-json", "User-Agent": "YuweAI-avi/1"}
    for ctx in (ssl.create_default_context(), ssl._create_unverified_context()):
        for url in urls:
            req = urllib.request.Request(url, headers=headers)
            try:
                with opener.open(req, timeout=8, context=ctx) as resp:
                    payload = json.loads(resp.read().decode())
            except Exception:
                continue
            addr = _a_record_from_dns_json(payload)
            if addr:
                return addr
    return None


def _resolve_ipv4_for_postgres_host(hostname: str, port: int) -> str | None:
    return (
        _ipv4_socket_lookup(hostname, port)
        or _ipv4_gethostbyname(hostname)
        or _dns_resolve_a_record(hostname)
    )


def _postgres_connect_conninfo() -> str:
    """Cadena conninfo para libpq. En Render→Supabase a menudo IPv6 no es alcanzable; fijamos hostaddr (IPv4)."""
    import psycopg.conninfo as conninfo

    params = dict(conninfo.conninfo_to_dict(DATABASE_URL))
    prefer_ipv4 = os.environ.get("AVI_PG_PREFER_IPV4", "1").strip().lower() in ("1", "true", "yes")
    host = (params.get("host") or "").strip()
    manual = (os.environ.get("AVI_PG_HOSTADDR") or "").strip()

    # Supabase "Direct" (db.*.supabase.co) es IPv6-only; Render no lo alcanza.
    if (
        prefer_ipv4
        and host.startswith("db.")
        and ".supabase.co" in host
        and "pooler" not in host
        and not (params.get("hostaddr") or "").strip()
        and not manual
    ):
        raise RuntimeError(
            "DATABASE_URL en Render sigue apuntando al host DIRECTO %r (solo IPv6). "
            "El HOST de la URI debe contener pooler.supabase.com (Session pooler de Supabase → Connect), "
            "no db.… Pasos: Supabase Connect → Session → copiar URI; Render → servicio web "
            "yuweai-avi-api → Environment → clave exacta DATABASE_URL → pegar → Save → Manual Deploy. "
            "Si solo editaste el Blueprint, abre el servicio hijo y comprueba que DATABASE_URL se actualizó allí."
            % (host,)
        )

    if prefer_ipv4 and host and not host.startswith("/") and not _host_is_literal_ip(host):
        if not (params.get("hostaddr") or "").strip():
            try:
                port = int(params.get("port") or 5432)
            except ValueError:
                port = 5432
            addr = manual or _resolve_ipv4_for_postgres_host(host, port)
            if addr:
                params["hostaddr"] = addr
            else:
                if ".supabase.co" in host and host.startswith("db."):
                    hint = (
                        "Supabase: la conexion DIRECTA (host db.xxx.supabase.co) es solo IPv6 por defecto; "
                        "Render no tiene IPv6 hacia esa ruta. En el dashboard Supabase pulsa Connect y elige "
                        "Session mode (Supavisor): URI con host aws-0-REGION.pooler.supabase.com y puerto 5432, "
                        "usuario postgres.TU_PROJECT_REF. Sustituye DATABASE_URL en Render por esa cadena (con sslmode=require)."
                    )
                else:
                    hint = (
                        "Define AVI_PG_HOSTADDR en Render con una IPv4 alcanzable, o usa la URI Session pooler "
                        "de Supabase (host …pooler.supabase.com). Documentacion: "
                        "https://supabase.com/docs/guides/database/connecting-to-postgres"
                    )
                raise RuntimeError(
                    "YuweAI Postgres: no hay IPv4 resuelto para el host %r. %s" % (host, hint)
                )

    clean = {k: v for k, v in params.items() if v is not None and v != ""}
    return conninfo.make_conninfo(**clean)


def _adapt_sql_postgres(sql: str) -> str:
    s = sql
    if "INSERT OR REPLACE INTO password_resets" in s:
        s = s.replace(
            "INSERT OR REPLACE INTO password_resets (email, code, expires_at, created_at)\n                   VALUES (?, ?, ?, ?)",
            "INSERT INTO password_resets (email, code, expires_at, created_at) VALUES (%s, %s, %s, %s) "
            "ON CONFLICT (email) DO UPDATE SET code = EXCLUDED.code, expires_at = EXCLUDED.expires_at, "
            "created_at = EXCLUDED.created_at",
        )
    # SQLite INSERT OR IGNORE -> Postgres ON CONFLICT (PK es (group_id, student_user_id)).
    # Debe coincidir con cualquier espaciado (server.py usa una linea; otras variantes multilinea).
    if "INSERT OR IGNORE INTO group_members" in s:
        s = re.sub(
            r"INSERT\s+OR\s+IGNORE\s+INTO\s+group_members\s*\(\s*group_id\s*,\s*student_user_id\s*,\s*assigned_at\s*\)\s*VALUES\s*\(\s*\?\s*,\s*\?\s*,\s*\?\s*\)",
            "INSERT INTO group_members (group_id, student_user_id, assigned_at) VALUES (%s, %s, %s) "
            "ON CONFLICT (group_id, student_user_id) DO NOTHING",
            s,
            flags=re.IGNORECASE | re.DOTALL,
        )
    if "?" in s:
        s = re.sub(r"\?", "%s", s)
    s = re.sub(r"ON CONFLICT\s*\(", "ON CONFLICT (", s, flags=re.IGNORECASE)
    return s


def adapt_sql(sql: str) -> str:
    if not USE_POSTGRES:
        return sql
    return _adapt_sql_postgres(sql)


def scalar_from_row(row: Any) -> Any:
    if row is None:
        return None
    if isinstance(row, dict):
        return next(iter(row.values()))
    return row[0]


class _AuthConn:
    __slots__ = ("_raw",)

    def __init__(self, raw: Any) -> None:
        self._raw = raw

    def execute(self, sql: str, parameters: tuple | list = ()) -> Any:
        sql2 = adapt_sql(sql)
        params = tuple(parameters) if parameters is not None else ()
        if USE_POSTGRES:
            return self._raw.execute(sql2, params)
        return self._raw.execute(sql2, params)

    def commit(self) -> None:
        self._raw.commit()

    def close(self) -> None:
        self._raw.close()

    def executescript(self, script: str) -> None:
        if USE_POSTGRES:
            raise RuntimeError("executescript no soportado en Postgres; usa migraciones SQL en Supabase.")
        self._raw.executescript(script)


def connect_auth():
    if USE_POSTGRES:
        import psycopg
        from psycopg.rows import dict_row

        conn = psycopg.connect(_postgres_connect_conninfo(), row_factory=dict_row)
        return _AuthConn(conn)
    import sqlite3

    from pathlib import Path

    base = Path(__file__).resolve().parent
    db_path = base / "data" / "avi_auth.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    raw = sqlite3.connect(str(db_path), timeout=30)
    raw.row_factory = sqlite3.Row
    return _AuthConn(raw)


def insert_returning_id(conn: _AuthConn, insert_sql: str, params: tuple, id_column: str = "id") -> int:
    """Insert y devuelve PK; Postgres usa RETURNING, SQLite last_insert_rowid."""
    if USE_POSTGRES:
        sql = insert_sql.rstrip().rstrip(";")
        if "RETURNING" not in sql.upper():
            sql = f"{sql} RETURNING {id_column}"
        row = conn.execute(sql, params).fetchone()
        if not row:
            raise RuntimeError("INSERT sin fila RETURNING")
        if isinstance(row, dict):
            return int(row[id_column])
        return int(row[0])
    conn.execute(insert_sql, params)
    row = conn.execute("SELECT last_insert_rowid()", ()).fetchone()
    return int(scalar_from_row(row))
