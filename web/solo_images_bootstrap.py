"""Descarga corpus/generadas-img-ia-solo en runtime (Render: sin tarball en /tmp)."""
from __future__ import annotations

import os
import subprocess
import threading
import time
from pathlib import Path

_MIN_PNG = int(os.environ.get("SOLO_IMG_MIN_PNG", "100"))
_TARGET_PNG = int(os.environ.get("SOLO_IMG_TARGET_PNG", "3600"))
_DEFER_SECONDS = int(os.environ.get("SOLO_IMG_DEFER_SECONDS", "45"))
# En plan free: no reintentar 5 GB si ya hay corpus parcial (evita bucle OOM/eviction).
_SKIP_REDOWLOAD = os.environ.get("SOLO_IMG_SKIP_REDOWLOAD", "1") == "1"
_SKIP_IF_COUNT = int(os.environ.get("SOLO_IMG_SKIP_IF_COUNT", "2000"))
_lock = threading.Lock()
_started = False
_bootstrap_status = "idle"  # idle | waiting | downloading | done | error | skipped


def bootstrap_status() -> str:
    return _bootstrap_status


def png_count(img_dir: Path) -> int:
    if not img_dir.is_dir():
        return 0
    n = 0
    for _root, _dirs, files in os.walk(img_dir):
        n += sum(1 for f in files if f.lower().endswith(".png"))
    return n


def is_corpus_complete(img_dir: Path) -> bool:
    return png_count(img_dir) >= _TARGET_PNG


def _shell_stream_extract(urls: list[str], dest: Path) -> None:
    """
    curl | tar directo al destino (cero bytes en /tmp).
    --skip-old-files reanuda sin sobrescribir PNG ya extraidos.
    """
    dest.mkdir(parents=True, exist_ok=True)
    dest_s = str(dest).replace('"', '\\"')
    if len(urls) == 1:
        curl_part = f'curl -fSL "{urls[0]}"'
    else:
        inner = "; ".join(f'curl -fSL "{u}"' for u in urls)
        curl_part = f"( {inner} )"

    # --strip-components=1 quita generadas-img-ia-solo/ del path en el tar.
    script = (
        f"{curl_part} | "
        f'tar -xz --skip-old-files --no-same-owner --warning=no-timestamp '
        f'-C "{dest_s}" --strip-components=1'
    )
    print(f"[solo bootstrap] Stream extract -> {dest} ({len(urls)} URL(s))", flush=True)
    subprocess.run(
        ["sh", "-c", script],
        check=True,
        timeout=7200,
    )


def fetch_if_needed(img_dir: Path) -> int:
    """Descarga/extrae tarball si faltan PNG. Devuelve conteo final."""
    global _bootstrap_status

    n = png_count(img_dir)
    if is_corpus_complete(img_dir):
        _bootstrap_status = "done"
        print(f"[solo bootstrap] Corpus completo: {n} PNG en {img_dir}", flush=True)
        return n

    if _SKIP_REDOWLOAD and n >= _SKIP_IF_COUNT:
        _bootstrap_status = "skipped"
        print(
            f"[solo bootstrap] Parcial ({n} PNG) — omitiendo descarga 5 GB en plan free. "
            f"Sube a Starter+disco o SOLO_IMG_FORCE_REDOWLOAD=1.",
            flush=True,
        )
        return n

    if _SKIP_REDOWLOAD and n >= _MIN_PNG and os.environ.get("SOLO_IMG_FORCE_REDOWLOAD", "0") != "1":
        _bootstrap_status = "skipped"
        print(
            f"[solo bootstrap] Parcial ({n}/{_TARGET_PNG}); no se repite descarga "
            f"(SOLO_IMG_FORCE_REDOWLOAD=1 para forzar).",
            flush=True,
        )
        return n

    parts_raw = (os.environ.get("SOLO_IMG_TARBALL_PARTS") or "").strip()
    url = (os.environ.get("SOLO_IMG_TARBALL_URL") or "").strip()
    urls: list[str] = []
    if parts_raw:
        urls = [p.strip() for p in parts_raw.split(",") if p.strip()]
    elif url:
        urls = [url]

    if not urls:
        _bootstrap_status = "skipped"
        print(f"[solo bootstrap] Sin URL; solo {n} PNG en disco", flush=True)
        return n

    img_dir.mkdir(parents=True, exist_ok=True)
    _bootstrap_status = "downloading"
    try:
        _shell_stream_extract(urls, img_dir)
        _bootstrap_status = "done"
    except Exception as exc:
        _bootstrap_status = "error"
        print(f"[solo bootstrap] ERROR en stream: {exc}", flush=True)
        raise

    n = png_count(img_dir)
    print(f"[solo bootstrap] Listo: {n} PNG", flush=True)
    return n


def start_background_fetch(img_dir: Path) -> None:
    global _started
    with _lock:
        if _started:
            return
        _started = True

    def _run() -> None:
        global _bootstrap_status
        if _DEFER_SECONDS > 0:
            _bootstrap_status = "waiting"
            print(f"[solo bootstrap] Esperando {_DEFER_SECONDS}s (API arriba primero)...", flush=True)
            time.sleep(_DEFER_SECONDS)
        try:
            fetch_if_needed(img_dir)
        except Exception as exc:
            _bootstrap_status = "error"
            print(f"[solo bootstrap] ERROR: {exc}", flush=True)

    threading.Thread(target=_run, daemon=True, name="solo-img-bootstrap").start()
