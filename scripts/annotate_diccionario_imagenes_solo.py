"""
Actualiza `corpus/data/DICCIONARIO-PALABRAS-COMPLETO.md`:
  - Inserta seccion **Estado PNG IA solo** (conteos y %).
  - Anade columna checklist a la tabla **Pares unicos (prioritario para imagenes)**:
    `- [x]` si existe `corpus/generadas-img-ia-solo/<dest_rel>` del JSONL por `id`,
    `- [~] en curso` si se esta generando,
    `- [ ]` si falta, `- [?]` si el id no esta en prompts_solo_full.jsonl.

Genera `corpus/data/DICCIONARIO-IMAGENES-SOLO-RESUMEN.md` con tabla por categoria y lista de PNG ya presentes.

Uso (desde raiz YuweAI):
  python scripts/annotate_diccionario_imagenes_solo.py
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DIC_PATH = REPO / "corpus" / "data" / "DICCIONARIO-PALABRAS-COMPLETO.md"
JSONL_PATH = REPO / "corpus" / "generadas-img-ia-solo" / "prompts_solo_full.jsonl"
IMG_ROOT = REPO / "corpus" / "generadas-img-ia-solo"
RESUMEN_PATH = REPO / "corpus" / "data" / "DICCIONARIO-IMAGENES-SOLO-RESUMEN.md"
# Una linea por `id` (LEX-...) o `dest_rel` (categoria/archivo.png); marca `- [~] en curso` en el MD.
EN_CURSO_PATH = REPO / "corpus" / "data" / "solo_generacion_en_curso.txt"

ANCHOR_PARES = "## Pares unicos (prioritario para imagenes)"
ANCHOR_TODAS = "## Todas las entradas (orden por id)"

ROW_RE = re.compile(
    r"^\|\s*(?P<num>\d+)\s*\|\s*`(?P<rid>[^`]+)`\s*\|\s*(?P<es>[^|]*?)\s*\|\s*(?P<cat>[^|]*?)(?:\s*\|\s*[^|]*)?\s*\|\s*$"
)

GLOSS_RE = re.compile(
    r"gloss to illustrate is: «([^»]+)»|"
    r"subject to render is: ([^(]+)|"
    r"term to depict visually is: «([^»]+)»|"
    r"kinship term to depict visually is: «([^»]+)»|"
    r"full first name to spell letter-by-letter in the image is: ([^(]+)"
)


def load_en_curso_ids_and_dests() -> set[str]:
    if not EN_CURSO_PATH.is_file():
        return set()
    out: set[str] = set()
    for line in EN_CURSO_PATH.read_text(encoding="utf-8").splitlines():
        t = line.strip()
        if not t or t.startswith("#"):
            continue
        out.add(t)
    return out


def load_id_to_dest() -> dict[str, str]:
    out: dict[str, str] = {}
    for line in JSONL_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        o = json.loads(line)
        out[o["id"]] = o["dest_rel"]
    return out


def load_pairs_from_jsonl() -> list[tuple[str, str, str, str]]:
    """Reconstruye filas (#, id, espanol, categoria) si la tabla del MD se perdio."""
    rows: list[tuple[str, str, str, str]] = []
    for i, line in enumerate(JSONL_PATH.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        o = json.loads(line)
        rid = o["id"]
        cat = o["dest_rel"].split("/")[0]
        m = GLOSS_RE.search(o.get("prompt_en", ""))
        es = ""
        if m:
            es = next(g for g in m.groups() if g).strip()
        if not es:
            es = Path(o["dest_rel"]).stem.replace("_", " ")
        rows.append((str(i), rid, es, cat))
    return rows


def build_estado_markdown(
    *,
    total_pairs: int,
    in_jsonl: int,
    with_png: int,
    missing_jsonl: int,
    en_curso: int,
    by_cat: list[tuple[str, int, int, int]],
) -> str:
    pct = (100.0 * with_png / total_pairs) if total_pairs else 0.0
    lines = [
        "## Estado PNG IA solo (`corpus/generadas-img-ia-solo`)",
        "",
        "Cada fila de *Pares unicos* se cruza con `prompts_solo_full.jsonl` por **`id`** y se comprueba si existe el archivo **`corpus/generadas-img-ia-solo/<ruta>.png`**.",
        "",
        f"- **Pares en esta tabla:** {total_pairs}",
        f"- **Ids resueltos en JSONL:** {in_jsonl}",
        f"- **PNG ya presentes en disco:** {with_png} ({pct:.1f} %)",
        f"- **Marcados en curso** (`solo_generacion_en_curso.txt`): {en_curso}",
        f"- **Ids sin fila en JSONL (revisar):** {missing_jsonl}",
        "",
        "Para generar nuevas imagenes: prompts en `corpus/generadas-img-ia-solo/prompts_solo_full.jsonl`; assets Cursor `solo__<categoria>__<stem>.png`; luego `python scripts/sync_solo_imagenes_desde_assets.py`.",
        "Mientras generas un lote, pon sus `id` o `dest_rel` en `corpus/data/solo_generacion_en_curso.txt` (una por linea) y vuelve a ejecutar este script para ver `- [~] en curso` en la tabla.",
        "",
        "Para **refrescar** esta columna y el resumen: `python scripts/annotate_diccionario_imagenes_solo.py`",
        "",
    ]
    lines.append("### Por categoria (pares unicos)")
    lines.append("")
    lines.append("| categoria | PNG listos | Faltan | Total pares |")
    lines.append("|-----------|------------|--------|-------------|")
    for cat, ok, miss, tot in sorted(by_cat, key=lambda x: x[0].lower()):
        lines.append(f"| `{cat}` | {ok} | {miss} | {tot} |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    if not DIC_PATH.is_file():
        raise SystemExit(f"No existe {DIC_PATH}")
    if not JSONL_PATH.is_file():
        raise SystemExit(f"No existe {JSONL_PATH}")

    id_to_dest = load_id_to_dest()
    en_curso_raw = load_en_curso_ids_and_dests()
    text = DIC_PATH.read_text(encoding="utf-8")
    i_pares = text.find(ANCHOR_PARES)
    i_todas = text.find(ANCHOR_TODAS)
    if i_pares < 0 or i_todas < 0 or i_todas <= i_pares:
        raise SystemExit("No se encontraron anclas del diccionario.")

    head = text[:i_pares].rstrip()
    # Mantener solo intro (sin bloques Estado previos)
    estado_anchor = "## Estado PNG IA solo"
    if estado_anchor in head:
        head = head[: head.find(estado_anchor)].rstrip()
    old_block = text[i_pares:i_todas]
    tail = text[i_todas:]

    old_lines = old_block.splitlines()
    table_body: list[tuple[str, str, str, str]] = []
    in_progress: dict[str, str] = {}  # rid -> celda previa si estaba en curso
    for ln in old_lines:
        m = ROW_RE.match(ln.strip())
        if not m:
            continue
        rid = m.group("rid")
        table_body.append((m.group("num"), rid, m.group("es").strip(), m.group("cat").strip()))
        if "[~]" in ln and "haciendo" in ln.lower():
            in_progress[rid] = "- [~] haciendo"

    if not table_body:
        table_body = load_pairs_from_jsonl()
        print(f"Tabla vacia: reconstruidas {len(table_body)} filas desde JSONL.")

    total_pairs = len(table_body)
    stats_cat: dict[str, list[int]] = defaultdict(lambda: [0, 0])  # ok, miss

    new_rows: list[str] = [
        ANCHOR_PARES,
        "",
        "| # | id (ejemplo) | espanol | categoria | PNG `generadas-img-ia-solo` |",
        "|---|----------------|---------|-----------|------------------------------|",
    ]

    in_jsonl = 0
    with_png = 0
    missing_jsonl = 0
    en_curso_marked = 0
    done_paths: list[str] = []

    for num, rid, es, cat in table_body:
        dest = id_to_dest.get(rid)
        if dest is None:
            cell = "- [?] sin JSONL"
            missing_jsonl += 1
            stats_cat[cat][1] += 1
        else:
            in_jsonl += 1
            p = IMG_ROOT / dest
            if p.is_file():
                cell = f"- [x] `{dest}`"
                with_png += 1
                stats_cat[cat][0] += 1
                done_paths.append(dest)
            elif rid in en_curso_raw or dest in en_curso_raw:
                cell = f"- [~] en curso · `{dest}`"
                en_curso_marked += 1
                stats_cat[cat][1] += 1
            else:
                cell = "- [ ] falta"
                stats_cat[cat][1] += 1
        new_rows.append(f"| {num} | `{rid}` | {es} | {cat} | {cell} |")

    new_rows.append("")

    by_cat_rows: list[tuple[str, int, int, int]] = []
    for cat, (ok, miss) in stats_cat.items():
        tot = ok + miss
        by_cat_rows.append((cat, ok, miss, tot))

    estado_md = build_estado_markdown(
        total_pairs=total_pairs,
        in_jsonl=in_jsonl,
        with_png=with_png,
        missing_jsonl=missing_jsonl,
        en_curso=en_curso_marked,
        by_cat=by_cat_rows,
    )

    out_text = head + "\n\n" + estado_md + "\n" + "\n".join(new_rows) + "\n" + tail.lstrip("\n")
    DIC_PATH.write_text(out_text, encoding="utf-8")

    # Resumen aparte: lista de listos + tabla
    res_lines = [
        "# Resumen: imagenes IA solo-tema (`generadas-img-ia-solo`)",
        "",
        f"- **PNG presentes:** {with_png} / {total_pairs} pares unicos ({(100.0*with_png/total_pairs) if total_pairs else 0:.1f} %)",
        f"- **Ids sin JSONL:** {missing_jsonl}",
        "",
        "Tabla por categoria:",
        "",
        "| categoria | listos | faltan | total |",
        "|-----------|--------|--------|-------|",
    ]
    for cat, ok, miss, tot in sorted(by_cat_rows, key=lambda x: x[0].lower()):
        res_lines.append(f"| `{cat}` | {ok} | {miss} | {tot} |")
    res_lines.extend(
        [
            "",
            "## Checklist PNG ya generados (ruta relativa al corpus)",
            "",
        ]
    )
    for d in sorted(done_paths, key=lambda x: (x.split("/")[0].lower(), x.lower())):
        res_lines.append(f"- [x] `{d}`")
    res_lines.append("")
    RESUMEN_PATH.write_text("\n".join(res_lines), encoding="utf-8")

    print(f"Actualizado {DIC_PATH.relative_to(REPO)}")
    print(f"Escrito {RESUMEN_PATH.relative_to(REPO)}")
    print(f"Pares: {total_pairs} | PNG ok: {with_png} | sin JSONL: {missing_jsonl}")


if __name__ == "__main__":
    main()
