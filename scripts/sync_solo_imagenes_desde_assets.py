"""
Copia PNG desde assets de Cursor hacia corpus/generadas-img-ia-solo/

Espera nombres: solo__<categoria>__<stem>.png
  -> corpus/generadas-img-ia-solo/<categoria>/<stem>.png

Uso (desde YuweAI):
  python scripts/sync_solo_imagenes_desde_assets.py
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEST = REPO / "corpus" / "generadas-img-ia-solo"
ASSETS = Path(
    r"C:\Users\Juliana\.cursor\projects\c-Users-Juliana-OneDrive-Desktop-GRADO-ING\assets"
)

RE_SOLO = re.compile(r"^solo__(.+?)__(.+)\.png$", re.I)


def main() -> None:
    if not ASSETS.is_dir():
        print(f"No existe carpeta assets: {ASSETS}")
        return

    copied = 0
    for f in sorted(ASSETS.iterdir()):
        if not f.is_file() or f.suffix.lower() != ".png":
            continue
        m = RE_SOLO.match(f.name)
        if not m:
            continue
        cat, stem = m.group(1).lower(), m.group(2).lower()
        out = DEST / cat / f"{stem}.png"
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, out)
        print(f"{f.name} -> {out.relative_to(REPO)}")
        copied += 1

    print(f"\nCopiadas: {copied}")


if __name__ == "__main__":
    main()
