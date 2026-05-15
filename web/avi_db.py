"""
Capa mínima SQLite / PostgreSQL para YuweAI.
Si DATABASE_URL está definida (p. ej. Supabase), se usa psycopg; si no, sqlite3.
"""
from __future__ import annotations

import os
import re
from typing import Any

DATABASE_URL = (os.environ.get("DATABASE_URL") or "").strip()
USE_POSTGRES = bool(DATABASE_URL)


def _adapt_sql_postgres(sql: str) -> str:
    s = sql
    if "INSERT OR REPLACE INTO password_resets" in s:
        s = s.replace(
            "INSERT OR REPLACE INTO password_resets (email, code, expires_at, created_at)\n                   VALUES (?, ?, ?, ?)",
            "INSERT INTO password_resets (email, code, expires_at, created_at) VALUES (%s, %s, %s, %s) "
            "ON CONFLICT (email) DO UPDATE SET code = EXCLUDED.code, expires_at = EXCLUDED.expires_at, "
            "created_at = EXCLUDED.created_at",
        )
    if "INSERT OR IGNORE INTO group_members" in s:
        s = s.replace(
            "INSERT OR IGNORE INTO group_members (group_id, student_user_id, assigned_at)\n                        VALUES (?, ?, ?)",
            "INSERT INTO group_members (group_id, student_user_id, assigned_at) VALUES (%s, %s, %s) "
            "ON CONFLICT (group_id, student_user_id) DO NOTHING",
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

        conn = psycopg.connect(DATABASE_URL, row_factory=dict_row)
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
