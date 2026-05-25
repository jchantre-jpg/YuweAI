"""
Genera corpus/IMAGENES_LEXICO_DESCARGA.md con la lista de archivos sugeridos
por categoria (lexico) a partir de corpus_bilingue_v5.csv.
Ejecutar desde la raiz del repo YuweAI: python scripts/gen_imagenes_lexico_md.py
"""
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CSV_PATH = REPO / "corpus" / "data" / "corpus_bilingue_v5.csv"
OUT_PATH = REPO / "corpus" / "IMAGENES_LEXICO_DESCARGA.md"

INVALID_WIN = '<>:"/\\|?*'


def safe_filename_stem(s: str) -> str:
    t = (s or "").strip().lower()
    for ch in INVALID_WIN:
        t = t.replace(ch, "_")
    t = re.sub(r"\s+", "_", t)
    t = re.sub(r"_+", "_", t).strip("_")
    return t or "item"


def load_lexico_by_category() -> dict[str, list[dict]]:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("record_type") != "lexico":
                continue
            cat = (row.get("categoria") or "").strip()
            es = (row.get("espanol") or "").strip()
            en = (row.get("espanol_norm") or "").strip()
            if not es and not en:
                continue
            by_cat[cat].append(
                {
                    "id": (row.get("id") or "").strip(),
                    "espanol": es,
                    "espanol_norm": en or es,
                    "nasa_yuwe": (row.get("nasa_yuwe") or "").strip(),
                }
            )
    # dedupe por (categoria, espanol_norm) conservando la primera fila
    for cat in list(by_cat.keys()):
        seen: set[str] = set()
        uniq: list[dict] = []
        for row in sorted(by_cat[cat], key=lambda x: x["espanol_norm"].lower()):
            k = row["espanol_norm"].lower()
            if k in seen:
                continue
            seen.add(k)
            uniq.append(row)
        by_cat[cat] = uniq
    return dict(sorted(by_cat.items()))


def main() -> None:
    by_cat = load_lexico_by_category()
    lines: list[str] = []
    lines.append("# Imagenes lexico: nombres de archivo sugeridos\n\n")
    lines.append(
        "Este documento lista **cada entrada de lexico** del corpus `corpus_bilingue_v5.csv` "
        "con el **nombre de archivo** recomendado para que puedas descargar o dibujar la imagen "
        "y asociarla de forma estable (sin depender de Wikimedia Commons).\n\n"
    )
    lines.append("## Convencion\n\n")
    lines.append(
        "- Carpeta raiz sugerida: `corpus/imagenes_lexico/` (puedes versionarla en Git LFS si pesan mucho).\n"
        "- Subcarpeta **una por categoria** del CSV (mismo texto que la columna `categoria`).\n"
        "- Archivo: **`{espanol_norm}`** en minusculas, espacios como `_`, sin caracteres prohibidos en Windows, extension **`.jpg`** o **`.webp`** (elige una y usala en todo el proyecto).\n"
        "- La columna **Archivo sugerido** usa `espanol_norm` del corpus; si en tu Excel el lema difiere, prioriza `espanol_norm` para que coincida con el indice del sistema.\n"
        "- Columna **ID**: identificador unico del CSV por si necesitas distinguir homonimos (no suele haber en la misma categoria).\n"
        "- Para **regenerar** esta lista tras editar el CSV: `python scripts/gen_imagenes_lexico_md.py` (desde la carpeta `YuweAI`).\n"
        "- **Siguiente paso en el codigo** (aun no hecho): que el backend o el front resuelva la URL como "
        "`/static/imagenes_lexico/{categoria}/{archivo}` o una columna nueva en el CSV; hoy el diccionario sigue usando `/api/image` (Commons).\n\n"
    )
    lines.append("## Resumen por categoria\n\n")
    lines.append("| Categoria | Entradas (unicas por `espanol_norm`) |\n")
    lines.append("|-----------|----------------------------------------|\n")
    for cat, rows in by_cat.items():
        lines.append(f"| `{cat}` | {len(rows)} |\n")
    lines.append("\n---\n\n")

    for cat, rows in by_cat.items():
        lines.append(f"## `{cat}` ({len(rows)} archivos)\n\n")
        lines.append("| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |\n")
        lines.append("|-------------------|---------------------|-----------|----|\n")
        used_stems: dict[str, int] = {}
        for row in rows:
            stem = safe_filename_stem(row["espanol_norm"])
            n = used_stems.get(stem, 0)
            used_stems[stem] = n + 1
            if n:
                fname = f"{stem}__{n + 1}.jpg"
            else:
                fname = f"{stem}.jpg"
            es_esc = (row["espanol"] or row["espanol_norm"]).replace("|", "\\|").replace("\n", " ")
            ny = (row["nasa_yuwe"] or "—").replace("|", "\\|").replace("\n", " ")
            rid = row["id"] or "—"
            lines.append(f"| `{cat}/{fname}` | {es_esc} | {ny} | `{rid}` |\n")

    OUT_PATH.write_text("".join(lines), encoding="utf-8")
    print(f"Escrito {OUT_PATH} ({OUT_PATH.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
