#!/usr/bin/env python3
"""Sube PNG a Hugging Face dataset en lotes pequenos (reanudable, sin URLs expiradas)."""
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
IMG_ROOT = REPO_ROOT / "corpus" / "generadas-img-ia-solo"
DEFAULT_REPO = os.environ.get("HF_DATASET_REPO", "Juliana08/yuwe-dict-images")
DEFAULT_BATCH = int(os.environ.get("HF_UPLOAD_BATCH", "35"))


def list_pngs() -> list[tuple[Path, str]]:
    return [
        (path, path.relative_to(IMG_ROOT).as_posix())
        for path in sorted(IMG_ROOT.rglob("*.png"))
        if path.is_file()
    ]


def list_remote_pngs(api, repo: str, token: str) -> set[str]:
    print("Listando archivos ya en Hugging Face...", flush=True)
    files = api.list_repo_files(repo_id=repo, repo_type="dataset", token=token)
    remote = {f for f in files if f.lower().endswith(".png")}
    print(f"En el Hub: {len(remote)} PNG", flush=True)
    return remote


def upload_batch(api, repo: str, batch: list[tuple[Path, str]], token: str, attempt: int) -> None:
    from huggingface_hub import CommitOperationAdd

    ops = [CommitOperationAdd(path_in_repo=rel, path_or_fileobj=str(local)) for local, rel in batch]
    api.create_commit(
        repo_id=repo,
        repo_type="dataset",
        operations=ops,
        commit_message=f"corpus-img {batch[0][1]} +{len(batch)} (try {attempt})",
        token=token,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH)
    args = parser.parse_args()

    token = (os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN") or "").strip()
    if not token:
        try:
            from huggingface_hub.utils import get_token

            token = (get_token() or "").strip()
        except Exception:
            token = ""
    if not token:
        print("Falta HF_TOKEN (env o huggingface-cli login)", file=sys.stderr)
        return 1

    os.environ.setdefault("HF_HUB_DISABLE_XET", "1")

    from huggingface_hub import HfApi, create_repo

    pngs = list_pngs()
    print(f"Local: {len(pngs)} PNG -> {args.repo} (lotes {args.batch_size})", flush=True)

    api = HfApi(token=token)
    create_repo(args.repo, repo_type="dataset", exist_ok=True, token=token)

    try:
        remote = list_remote_pngs(api, args.repo, token)
    except Exception as exc:
        print(f"Aviso listado remoto: {exc}; subiendo todo", flush=True)
        remote = set()

    pending = [(local, rel) for local, rel in pngs if rel not in remote]
    print(f"Pendientes: {len(pending)}", flush=True)

    uploaded = 0
    errors = 0
    total_batches = (len(pending) + args.batch_size - 1) // args.batch_size

    for bi, start in enumerate(range(0, len(pending), args.batch_size), start=1):
        batch = pending[start : start + args.batch_size]
        for attempt in range(1, 6):
            try:
                upload_batch(api, args.repo, batch, token, attempt)
                uploaded += len(batch)
                print(
                    f"[{bi}/{total_batches}] OK +{len(batch)} | total {uploaded}/{len(pending)} | {batch[0][1]}",
                    flush=True,
                )
                break
            except Exception as exc:
                print(f"[{bi}] intento {attempt}/5: {exc}", file=sys.stderr, flush=True)
                if attempt >= 5:
                    errors += len(batch)
                else:
                    time.sleep(min(45, 4 * attempt))
        if bi % 15 == 0:
            time.sleep(3)

    base = f"https://huggingface.co/datasets/{args.repo}/resolve/main"
    print(f"\nFIN. subidos={uploaded} errores={errors} pendientes_inicial={len(pending)}")
    print(f"SOLO_IMG_CDN_BASE={base}")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
