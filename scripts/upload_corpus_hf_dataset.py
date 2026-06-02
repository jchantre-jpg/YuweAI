#!/usr/bin/env python3
"""
Sube corpus/generadas-img-ia-solo/*.png a un dataset publico de Hugging Face.
GRATIS — no pide tarjeta (a diferencia de Firebase Storage).

Requisitos:
  pip install huggingface_hub
  set HF_TOKEN=hf_...   (cuenta Juliana08, permiso write)

Uso:
  python scripts/upload_corpus_hf_dataset.py
  python scripts/upload_corpus_hf_dataset.py --repo Juliana08/yuwe-dict-images
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
IMG_ROOT = REPO_ROOT / "corpus" / "generadas-img-ia-solo"
DEFAULT_REPO = os.environ.get("HF_DATASET_REPO", "Juliana08/yuwe-dict-images")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sube PNG del diccionario a Hugging Face Dataset")
    parser.add_argument("--repo", default=DEFAULT_REPO, help="ID dataset HF (usuario/nombre)")
    parser.add_argument("--batch-size", type=int, default=80, help="Archivos por commit")
    args = parser.parse_args()

    if not IMG_ROOT.is_dir():
        print(f"No existe {IMG_ROOT}", file=sys.stderr)
        return 1

    token = (os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN") or "").strip()
    if not token:
        print("Falta HF_TOKEN. Crea uno en https://huggingface.co/settings/tokens", file=sys.stderr)
        return 1

    try:
        from huggingface_hub import HfApi, create_repo
    except ImportError:
        print("pip install huggingface_hub", file=sys.stderr)
        return 1

    os.environ.setdefault("HF_HUB_DISABLE_XET", "1")

    pngs = sorted(IMG_ROOT.rglob("*.png"))
    print(f"Subiendo {len(pngs)} PNG -> dataset {args.repo}")

    api = HfApi(token=token)
    create_repo(args.repo, repo_type="dataset", exist_ok=True, token=token)

    # upload_folder en lotes por subcarpeta (commits mas pequenos, reanudable)
    categories = sorted({p.parent.relative_to(IMG_ROOT).as_posix() for p in pngs if p.parent != IMG_ROOT})
    if not categories:
        categories = ["."]

    uploaded = 0
    for cat in categories:
        folder = IMG_ROOT if cat == "." else IMG_ROOT / cat
        if not folder.is_dir():
            continue
        n = sum(1 for _ in folder.rglob("*.png"))
        if not n:
            continue
        path_in_repo = "" if cat == "." else cat
        print(f"  -> {cat} ({n} PNG)...", flush=True)
        api.upload_folder(
            folder_path=str(folder),
            path_in_repo=path_in_repo,
            repo_id=args.repo,
            repo_type="dataset",
            token=token,
            commit_message=f"corpus-img {cat or 'root'}",
        )
        uploaded += n
        print(f"     OK ({uploaded}/{len(pngs)})", flush=True)

    base = f"https://huggingface.co/datasets/{args.repo}/resolve/main"
    print(
        f"\nListo. {uploaded} PNG en {args.repo}\n"
        f"Render / .env:\n"
        f"  SOLO_IMG_CDN_BASE={base}\n"
        f"Prueba:\n"
        f"  {base}/alimentos/arveja.png"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
