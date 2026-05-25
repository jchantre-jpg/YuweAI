#!/usr/bin/env python3
"""
Sube solo-img-ia.tar.gz a un repositorio *model* publico en Hugging Face y muestra la URL HTTPS
para pegar en Render como SOLO_IMG_TARBALL_URL.

Requisitos:
  pip install huggingface_hub

Autenticacion (una de):
  export HF_TOKEN=hf_...     # o HUGGING_FACE_HUB_TOKEN

Uso (desde la raiz YuweAI):
  python scripts/upload_solo_tarball_to_hf.py --repo-id TU_USUARIO/yuwe-solo-img-tarball
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Sube solo-img-ia.tar.gz al Hub para Render.")
    parser.add_argument(
        "--repo-id",
        default=os.environ.get("HF_SOLO_TARBALL_REPO", "").strip(),
        help="Repo Hub tipo 'usuario/nombre' (model). Ej: miuser/yuwe-solo-img-tarball",
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "solo-img-ia.tar.gz",
        help="Ruta al .tar.gz (por defecto: raiz del repo / solo-img-ia.tar.gz)",
    )
    args = parser.parse_args()

    repo_id = (args.repo_id or "").strip()
    if not repo_id:
        print(
            "Indica el repo Hub: --repo-id USUARIO/nombre\n"
            "Ejemplo: python scripts/upload_solo_tarball_to_hf.py --repo-id jchantre/yuwe-solo-img-tarball",
            file=sys.stderr,
        )
        return 2

    path = args.file.resolve()
    if not path.is_file():
        print(f"No existe el archivo: {path}", file=sys.stderr)
        return 2

    try:
        from huggingface_hub import HfApi
    except ImportError:
        print("Instala: pip install huggingface_hub", file=sys.stderr)
        return 2

    token = (os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN") or "").strip()
    if not token:
        print(
            "Define HF_TOKEN o HUGGING_FACE_HUB_TOKEN (token de https://huggingface.co/settings/tokens)",
            file=sys.stderr,
        )
        return 2

    api = HfApi(token=token)
    api.create_repo(repo_id=repo_id, repo_type="model", private=False, exist_ok=True)

    dest_name = path.name
    print(f"Subiendo {path} ({path.stat().st_size / 1e9:.2f} GB aprox.) a {repo_id} ...")
    api.upload_file(
        path_or_fileobj=str(path),
        path_in_repo=dest_name,
        repo_id=repo_id,
        repo_type="model",
        commit_message="solo-img-ia.tar.gz para Render SOLO_IMG_TARBALL_URL",
    )

    url = f"https://huggingface.co/{repo_id}/resolve/main/{dest_name}"
    print("")
    print("Listo. En Render -> Environment -> SOLO_IMG_TARBALL_URL pega:")
    print(url)
    print("")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
