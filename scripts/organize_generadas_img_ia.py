"""
Copia PNG desde la carpeta de assets de Cursor hacia
`corpus/generadas-img-ia/<categoria>/` con el nombre correcto.

Formatos reconocidos:
  dict-img-001-arracacha-alimentos.png  -> generadas-img-ia/alimentos/arracacha.png
  alimentos_arveja.png                  -> generadas-img-ia/alimentos/arveja.png
  ambientales_agua.png                  -> generadas-img-ia/ambientales/agua.png

Uso (ajusta ASSETS si tu ruta de proyecto Cursor difiere):
  python scripts/organize_generadas_img_ia.py
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEST = REPO / "corpus" / "generadas-img-ia"

# Subcarpetas validas (mismo criterio que IMAGENES_LEXICO_DESCARGA.md)
KNOWN_CATS = frozenset(
    {
        "alimentos",
        "ambientales",
        "animales",
        "astros",
        "colores",
        "cuerpo_humano",
        "diccionario_general",
        "frutas_verduras",
        "herramientas",
        "muebles_inmuebles",
        "nombres_propios",
        "numeros",
        "parentescos",
        "plantas_medicinales",
        "saludos",
        "utiles_hogar",
        "vocabulario_general",
    }
)

# Carpeta donde Cursor suele guardar imagenes generadas en el chat
ASSETS = Path(
    r"C:\Users\Juliana\.cursor\projects\c-Users-Juliana-OneDrive-Desktop-GRADO-ING\assets"
)

RE_DICT_IMG = re.compile(r"^dict-img-\d+-(.+)-([a-z0-9_]+)\.png$", re.I)

_CATS_BY_LEN = sorted(KNOWN_CATS, key=len, reverse=True)


def split_cat_word_filename(name: str) -> tuple[str, str] | None:
    if not name.lower().endswith(".png"):
        return None
    base = name.rsplit(".", 1)[0].lower()
    for cat in _CATS_BY_LEN:
        prefix = f"{cat}_"
        if base.startswith(prefix):
            return cat, base[len(prefix) :]
    return None


def main() -> None:
    if not ASSETS.is_dir():
        print(f"No existe assets: {ASSETS}")
        return

    n = 0
    for f in sorted(ASSETS.iterdir()):
        if not f.is_file() or f.suffix.lower() != ".png":
            continue
        name = f.name
        dest: Path | None = None

        m = RE_DICT_IMG.match(name)
        if m:
            stem, cat = m.group(1), m.group(2)
            if cat not in KNOWN_CATS:
                print(f"Omitido (categoria desconocida): {name}")
                continue
            dest = DEST / cat / f"{stem}.png"
        else:
            m2 = split_cat_word_filename(name)
            if m2:
                cat, stem = m2
                dest = DEST / cat / f"{stem}.png"

        if dest is None:
            continue

        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dest)
        print(f"{name} -> {dest.relative_to(REPO)}")
        n += 1

    print(f"Listo: {n} archivos copiados bajo {DEST}")


if __name__ == "__main__":
    main()
