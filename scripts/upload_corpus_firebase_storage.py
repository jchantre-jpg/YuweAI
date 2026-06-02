#!/usr/bin/env python3
"""
Sube corpus/generadas-img-ia-solo/*.png a Firebase Storage (proyecto yuwe-ai).

Requisitos (una vez):
  pip install google-cloud-storage
  Firebase Console -> Configuracion -> Cuentas de servicio -> Generar clave JSON
  set GOOGLE_APPLICATION_CREDENTIALS=C:\\ruta\\yuwe-ai-firebase-adminsdk.json

Uso:
  python scripts/upload_corpus_firebase_storage.py
  python scripts/upload_corpus_firebase_storage.py --dry-run
  python scripts/upload_corpus_firebase_storage.py --workers 12

Despues:
  firebase deploy --only storage   (reglas lectura publica corpus-img/)
  Render: FIREBASE_STORAGE_BUCKET=yuwe-ai.firebasestorage.app
"""
from __future__ import annotations

import argparse
import os
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
IMG_ROOT = REPO / "corpus" / "generadas-img-ia-solo"
PREFIX = os.environ.get("FIREBASE_STORAGE_PREFIX", "corpus-img").strip("/")
DEFAULT_BUCKET = os.environ.get("FIREBASE_STORAGE_BUCKET", "yuwe-ai.firebasestorage.app").strip()

_counter_lock = threading.Lock()
_stats = {"uploaded": 0, "skipped": 0, "errors": 0, "done": 0}


def _inc(key: str, n: int = 1) -> None:
    with _counter_lock:
        _stats[key] += n
        _stats["done"] += n


def list_pngs() -> list[tuple[Path, str]]:
    out: list[tuple[Path, str]] = []
    for path in IMG_ROOT.rglob("*.png"):
        if not path.is_file():
            continue
        rel = path.relative_to(IMG_ROOT).as_posix()
        out.append((path, rel))
    return sorted(out, key=lambda x: x[1])


def upload_one(bucket, local: Path, rel: str, dry_run: bool) -> None:
    blob_name = f"{PREFIX}/{rel}" if PREFIX else rel
    if dry_run:
        print(f"[dry-run] {blob_name}")
        _inc("skipped")
        return
    blob = bucket.blob(blob_name)
    if blob.exists():
        _inc("skipped")
        return
    try:
        blob.upload_from_filename(str(local), content_type="image/png")
        blob.cache_control = "public, max-age=604800, immutable"
        blob.patch()
        _inc("uploaded")
    except Exception as exc:
        print(f"ERROR {rel}: {exc}", file=sys.stderr)
        _inc("errors")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sube PNG del diccionario a Firebase Storage")
    parser.add_argument("--bucket", default=DEFAULT_BUCKET, help="Bucket Firebase Storage")
    parser.add_argument("--workers", type=int, default=8, help="Subidas paralelas")
    parser.add_argument("--dry-run", action="store_true", help="Solo listar, no subir")
    parser.add_argument("--limit", type=int, default=0, help="Max archivos (prueba)")
    args = parser.parse_args()

    if not IMG_ROOT.is_dir():
        print(f"No existe {IMG_ROOT}", file=sys.stderr)
        return 1

    pngs = list_pngs()
    if args.limit > 0:
        pngs = pngs[: args.limit]
    total = len(pngs)
    print(f"PNG locales: {total} en {IMG_ROOT}")
    print(f"Destino: gs://{args.bucket}/{PREFIX}/")

    if args.dry_run:
        for local, rel in pngs[:20]:
            upload_one(None, local, rel, True)
        if total > 20:
            print(f"... y {total - 20} mas")
        return 0

    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        print(
            "Falta GOOGLE_APPLICATION_CREDENTIALS (JSON de cuenta de servicio Firebase).\n"
            "Firebase Console -> yuwe-ai -> Configuracion -> Cuentas de servicio -> Generar clave.",
            file=sys.stderr,
        )
        return 1

    try:
        from google.cloud import storage
    except ImportError:
        print("pip install google-cloud-storage", file=sys.stderr)
        return 1

    client = storage.Client()
    bucket = client.bucket(args.bucket)

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = [pool.submit(upload_one, bucket, local, rel, False) for local, rel in pngs]
        for i, fut in enumerate(as_completed(futures), start=1):
            fut.result()
            if i % 200 == 0 or i == total:
                with _counter_lock:
                    s = dict(_stats)
                print(
                    f"Progreso {i}/{total} | subidos={s['uploaded']} "
                    f"omitidos={s['skipped']} errores={s['errors']}",
                    flush=True,
                )

    print(
        f"Listo. subidos={_stats['uploaded']} omitidos={_stats['skipped']} errores={_stats['errors']}"
    )
    print(
        f"\nSiguiente:\n"
        f"  cd web/frontend && firebase deploy --only storage\n"
        f"  Render -> FIREBASE_STORAGE_BUCKET={args.bucket}\n"
        f"  Probar: https://firebasestorage.googleapis.com/v0/b/{args.bucket}/o/"
        f"{PREFIX.replace('/', '%2F')}%2Falimentos%2Farveja.png?alt=media"
    )
    return 0 if _stats["errors"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
