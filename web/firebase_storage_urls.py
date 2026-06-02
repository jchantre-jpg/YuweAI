"""URLs publicas de Firebase Storage para ilustraciones del diccionario."""
from __future__ import annotations

import os
from urllib.parse import quote

_BUCKET = os.environ.get("FIREBASE_STORAGE_BUCKET", "").strip()
_PREFIX = (os.environ.get("FIREBASE_STORAGE_PREFIX", "corpus-img") or "corpus-img").strip("/")


def firebase_storage_enabled() -> bool:
    return bool(_BUCKET)


def firebase_corpus_image_url(rel: str) -> str | None:
    """URL HTTPS de un PNG en Firebase Storage (lectura publica via rules)."""
    if not _BUCKET:
        return None
    rel = str(rel or "").strip().replace("\\", "/").lstrip("/")
    if not rel or ".." in rel or not rel.lower().endswith(".png"):
        return None
    path = f"{_PREFIX}/{rel}" if _PREFIX else rel
    encoded = quote(path, safe="")
    return f"https://firebasestorage.googleapis.com/v0/b/{_BUCKET}/o/{encoded}?alt=media"
