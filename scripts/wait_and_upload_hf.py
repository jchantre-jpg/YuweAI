"""Espera token HF y sube solo-img-ia.tar.gz al Hub."""
from __future__ import annotations

import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TAR = REPO / "solo-img-ia.tar.gz"
REPO_ID = "jchantre-jpg/yuwe-solo-img-tarball"
LOG = REPO / "upload-hf.log"


def log(msg: str) -> None:
    line = f"{time.strftime('%H:%M:%S')} {msg}"
    print(line, flush=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def has_token() -> bool:
    try:
        from huggingface_hub import get_token

        return bool(get_token())
    except Exception:
        return False


def main() -> int:
    if not TAR.is_file():
        log(f"ERROR: no existe {TAR}")
        return 2

    log("Esperando login en Hugging Face (ventana abierta)...")
    for i in range(600):  # ~50 min max
        if has_token():
            break
        if i % 12 == 0:
            log(f"  ... aun sin token ({i * 5}s)")
        time.sleep(5)
    else:
        log("TIMEOUT: no se detecto token HF")
        return 2

    log("Token detectado. Subiendo tarball (~5 GB)...")
    from huggingface_hub import HfApi

    api = HfApi()
    api.create_repo(repo_id=REPO_ID, repo_type="model", private=False, exist_ok=True)
    api.upload_file(
        path_or_fileobj=str(TAR),
        path_in_repo=TAR.name,
        repo_id=REPO_ID,
        repo_type="model",
        commit_message="solo-img-ia.tar.gz 3720 PNG diccionario YuweAI",
    )
    url = f"https://huggingface.co/{REPO_ID}/resolve/main/{TAR.name}"
    log(f"LISTO: {url}")
    log("Pega esa URL en Render -> SOLO_IMG_TARBALL_URL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
