"""Descarga corpus/generadas-img-ia-solo en runtime si faltan PNG (Render build sin 5 GB)."""
from __future__ import annotations

import os
import shutil
import subprocess
import tarfile
import threading
import tempfile
from pathlib import Path

_MIN_PNG = int(os.environ.get("SOLO_IMG_MIN_PNG", "100"))
_TARGET_PNG = int(os.environ.get("SOLO_IMG_TARGET_PNG", "3600"))
_lock = threading.Lock()
_started = False


def png_count(img_dir: Path) -> int:
    if not img_dir.is_dir():
        return 0
    return sum(1 for _ in img_dir.rglob("*.png"))


def is_corpus_complete(img_dir: Path) -> bool:
    return png_count(img_dir) >= _TARGET_PNG


def _merge_tree(src: Path, dest: Path) -> None:
    """Copia archivos sin borrar categorias ya presentes (reanuda extracciones parciales)."""
    dest.mkdir(parents=True, exist_ok=True)
    for item in src.rglob("*"):
        if not item.is_file():
            continue
        rel = item.relative_to(src)
        out = dest / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, out)


def _extract_tarball(tar_path: Path, dest: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="solo_ex_") as tmp:
        root = Path(tmp)
        with tarfile.open(tar_path, "r:gz") as tf:
            tf.extractall(root)
        nested = root / "generadas-img-ia-solo"
        src = nested if nested.is_dir() else root
        _merge_tree(src, dest)


def _curl_download(url: str, out: Path) -> None:
    subprocess.run(
        ["curl", "-fSL", url, "-o", str(out)],
        check=True,
        timeout=7200,
    )


def fetch_if_needed(img_dir: Path) -> int:
    """Descarga tarball si faltan PNG. Devuelve conteo final."""
    n = png_count(img_dir)
    if is_corpus_complete(img_dir):
        print(f"[solo bootstrap] Corpus completo: {n} PNG en {img_dir}", flush=True)
        return n
    if n >= _MIN_PNG:
        print(f"[solo bootstrap] Parcial ({n}/{_TARGET_PNG}); reanudando descarga...", flush=True)

    parts_raw = (os.environ.get("SOLO_IMG_TARBALL_PARTS") or "").strip()
    url = (os.environ.get("SOLO_IMG_TARBALL_URL") or "").strip()
    if not parts_raw and not url:
        print(f"[solo bootstrap] Sin URL; solo {n} PNG en disco", flush=True)
        return n

    img_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="solo_dl_") as tmp:
        tar_path = Path(tmp) / "solo-img-ia.tar.gz"
        if parts_raw:
            print("[solo bootstrap] Descargando SOLO_IMG_TARBALL_PARTS ...", flush=True)
            part_files: list[Path] = []
            for i, part_url in enumerate(
                (p.strip() for p in parts_raw.split(",") if p.strip()), start=1
            ):
                part_path = Path(tmp) / f"part{i:03d}"
                print(f"[solo bootstrap] Parte {i}: {part_url[:80]}...", flush=True)
                _curl_download(part_url, part_path)
                part_files.append(part_path)
            with tar_path.open("wb") as out:
                for pf in part_files:
                    out.write(pf.read_bytes())
        else:
            print(f"[solo bootstrap] Descargando SOLO_IMG_TARBALL_URL ...", flush=True)
            _curl_download(url, tar_path)

        print(f"[solo bootstrap] Extrayendo {tar_path.stat().st_size / 1e9:.2f} GB ...", flush=True)
        _extract_tarball(tar_path, img_dir)

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
        try:
            fetch_if_needed(img_dir)
        except Exception as exc:
            print(f"[solo bootstrap] ERROR: {exc}", flush=True)

    threading.Thread(target=_run, daemon=True, name="solo-img-bootstrap").start()
