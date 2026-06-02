"""URLs CDN para ilustraciones del diccionario (Hugging Face, Firebase, etc.)."""
from __future__ import annotations

import os
from urllib.parse import quote

# Opcion 1: Hugging Face dataset o cualquier CDN (SIN tarjeta).
# Ej: https://huggingface.co/datasets/Juliana08/yuwe-dict-images/resolve/main
_CDN_BASE = os.environ.get("SOLO_IMG_CDN_BASE", "").strip().rstrip("/")

# Opcion 2: Firebase Storage (requiere plan Blaze + tarjeta, aunque el uso dentro del free tier no cobra).
_BUCKET = os.environ.get("FIREBASE_STORAGE_BUCKET", "").strip()
_PREFIX = (os.environ.get("FIREBASE_STORAGE_PREFIX", "corpus-img") or "corpus-img").strip("/")


def remote_images_enabled() -> bool:
    return bool(_CDN_BASE or _BUCKET)


def firebase_storage_enabled() -> bool:
    return bool(_BUCKET)


def cdn_base() -> str:
    return _CDN_BASE


def remote_corpus_image_url(rel: str) -> str | None:
    rel = str(rel or "").strip().replace("\\", "/").lstrip("/")
    if not rel or ".." in rel or not rel.lower().endswith(".png"):
        return None
    if _CDN_BASE:
        return f"{_CDN_BASE}/{rel}"
    if _BUCKET:
        path = f"{_PREFIX}/{rel}" if _PREFIX else rel
        encoded = quote(path, safe="")
        return f"https://firebasestorage.googleapis.com/v0/b/{_BUCKET}/o/{encoded}?alt=media"
    return None


# Compat nombre anterior
def firebase_corpus_image_url(rel: str) -> str | None:
    return remote_corpus_image_url(rel)
