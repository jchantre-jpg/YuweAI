"""
Coloca las imagenes de las primeras 100 entradas del manifest en
`corpus/generadas-img-ia/<categoria>/<archivo>.png` segun `archivo_png`.

Busca PNG en (por prioridad):
  1) Carpeta hermana `imagenes app/` (misma raiz que YuweAI, nombres sueltos tipo Arracacha.png)
  2) Assets de Cursor (`dict-img-*`, `categoria_palabra.png`)

Uso (desde YuweAI):
  python scripts/sync_primeras_100_imagenes.py
  python scripts/sync_primeras_100_imagenes.py --limit 100
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEST = REPO / "corpus" / "generadas-img-ia"
MANIFEST = DEST / "manifest.json"
# Carpeta tipica donde guardas exports sueltos (GRADO ING/imagenes app)
IMAGENES_APP = REPO.parent / "imagenes app"
ASSETS = Path(
    r"C:\Users\Juliana\.cursor\projects\c-Users-Juliana-OneDrive-Desktop-GRADO-ING\assets"
)

RE_DICT_IMG = re.compile(r"^dict-img-\d+-(.+)-([a-z0-9_]+)\.png$", re.I)

KNOWN = frozenset(
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

# Orden: categorias mas largas primero (p. ej. frutas_verduras antes que frutas)
_CATS_BY_LEN = sorted(KNOWN, key=len, reverse=True)


def split_cat_word_filename(name: str) -> tuple[str, str] | None:
    """ambientales_arbol_caucho.png -> (ambientales, arbol_caucho). None si no calza."""
    if not name.lower().endswith(".png"):
        return None
    base = name.rsplit(".", 1)[0].lower()
    for cat in _CATS_BY_LEN:
        prefix = f"{cat}_"
        if base.startswith(prefix):
            return cat, base[len(prefix) :]
    return None


def index_flat_dir(folder: Path, source_tag: str) -> dict[str, list[tuple[int, Path, str]]]:
    """stem_lower -> list of (priority, path, dict_cat or '')"""
    out: dict[str, list[tuple[int, Path, str]]] = defaultdict(list)
    if not folder.is_dir():
        return out
    for f in folder.iterdir():
        if not f.is_file() or f.suffix.lower() != ".png":
            continue
        name = f.name
        m = RE_DICT_IMG.match(name)
        if m:
            stem, cat = m.group(1).lower(), m.group(2).lower()
            if cat not in KNOWN:
                continue
            pr = 20 if source_tag == "assets" else 25
            out[stem].append((pr, f, cat))
            continue
        m2 = split_cat_word_filename(name)
        if m2:
            cat, stem = m2
            pr = 21 if source_tag == "assets" else 26
            out[stem].append((pr, f, cat))
            continue
        stem = f.stem.lower()
        pr = 10 if source_tag == "imagenes_app" else 15
        out[stem].append((pr, f, ""))
    return out


def merge_indexes(*idxs: dict[str, list[tuple[int, Path, str]]]) -> dict[str, list[tuple[int, Path, str]]]:
    merged: dict[str, list[tuple[int, Path, str]]] = defaultdict(list)
    for ix in idxs:
        for stem, lst in ix.items():
            merged[stem].extend(lst)
    return merged


def pick_best(stem: str, categoria: str, by_stem: dict[str, list[tuple[int, Path, str]]]) -> Path | None:
    cands = by_stem.get(stem)
    if not cands:
        return None
    cat_l = categoria.lower()

    def sort_key(t: tuple[int, Path, str]) -> tuple[int, int, str]:
        pr, p, dcat = t
        mismatch = 1 if (dcat and dcat != cat_l) else 0
        return (mismatch, pr, p.name)

    return sorted(cands, key=sort_key)[0][1]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=100)
    args = ap.parse_args()

    if not MANIFEST.is_file():
        raise SystemExit(f"No existe {MANIFEST}. Ejecuta antes export_prompts_primeras_100_lexico.py")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    chunk = manifest[: max(1, args.limit)]

    ix_app = index_flat_dir(IMAGENES_APP, "imagenes_app")
    ix_assets = index_flat_dir(ASSETS, "assets") if ASSETS.is_dir() else {}
    merged = merge_indexes(ix_app, ix_assets)

    copied = 0
    missing: list[str] = []
    for row in chunk:
        rel = row["archivo_png"]
        stem = Path(rel).stem.lower()
        cat = row.get("categoria") or rel.split("/")[0]
        dest = DEST / rel
        src = pick_best(stem, str(cat), merged)
        if src is None:
            missing.append(rel)
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        print(f"{src.name} -> {dest.relative_to(REPO)}")
        copied += 1

    print(f"\nCopiadas: {copied} / {len(chunk)}")
    if missing:
        print(f"Sin archivo fuente para {len(missing)} entradas (primeras faltas):")
        for m in missing[:40]:
            print(f"  - {m}")
        if len(missing) > 40:
            print(f"  ... y {len(missing) - 40} mas")


if __name__ == "__main__":
    main()
