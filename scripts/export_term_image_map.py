"""
Construye `corpus/generadas-img-ia-solo/term_image_routes.json` para el servidor:

- **by_id**: `LEX-…` / `LEXR-…` → ruta relativa PNG (desambigua gloss duplicados).
- **by_lex_key**: `normalize(espanol)|normalize(categoria)` → ruta (fallback sin `id`).

Criterio `normalize` alineado con `server.py` (`normalize_text`).

Fuente: `IMAGENES_LEXICO_DESCARGA.md` + `prompts_solo_full.jsonl` (mismo orden que
`export_prompts_solo_desde_lexico_md.py`).

Uso (desde YuweAI):
  python scripts/export_term_image_map.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MD_PATH = REPO / "corpus" / "IMAGENES_LEXICO_DESCARGA.md"
JSONL_PATH = REPO / "corpus" / "generadas-img-ia-solo" / "prompts_solo_full.jsonl"
OUT_PATH = REPO / "corpus" / "generadas-img-ia-solo" / "term_image_routes.json"

ROW_RE = re.compile(
    r"^\|\s*`([^`]+\.(?:jpg|webp))`\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*`([^`]+)`\s*\|\s*$"
)


def normalize_text(text: str) -> str:
    text = (text or "").lower().strip()
    text = text.replace("’", "'").replace("`", "'").replace("´", "'")
    text = re.sub(r"[^a-zA-Z0-9áéíóúüñçëïä'\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_md_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    text = MD_PATH.read_text(encoding="utf-8")
    for line in text.splitlines():
        m = ROW_RE.match(line.strip())
        if not m:
            continue
        rel, es_label, _nasa, rid = m.groups()
        rel = rel.strip()
        cat = rel.split("/")[0] if "/" in rel else "general"
        rows.append(
            {
                "espanol": es_label.strip(),
                "categoria": cat,
                "id_md": rid.strip(),
            }
        )
    return rows


def main() -> None:
    if not MD_PATH.is_file():
        raise SystemExit(f"No existe {MD_PATH}")
    if not JSONL_PATH.is_file():
        raise SystemExit(f"No existe {JSONL_PATH}")

    md_rows = parse_md_rows()
    jsonl_lines = [ln for ln in JSONL_PATH.read_text(encoding="utf-8").splitlines() if ln.strip()]
    if len(md_rows) != len(jsonl_lines):
        raise SystemExit(
            f"Conteo distinto: MD {len(md_rows)} filas vs JSONL {len(jsonl_lines)}. "
            "Vuelve a correr export_prompts_solo_desde_lexico_md.py o revisa archivos."
        )

    by_lex: dict[str, str] = {}
    by_id: dict[str, str] = {}
    for row, jline in zip(md_rows, jsonl_lines, strict=True):
        o = json.loads(jline)
        tid = str(o.get("id", "")).strip()
        dest = str(o.get("dest_rel", "")).strip().replace("\\", "/")
        if not dest:
            continue
        if tid:
            by_id[tid] = dest
        k = f"{normalize_text(row['espanol'])}|{normalize_text(row['categoria'])}"
        by_lex[k] = dest

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {"by_id": by_id, "by_lex_key": by_lex}
    OUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Escrito {OUT_PATH.relative_to(REPO)} — by_id={len(by_id)} by_lex_key={len(by_lex)}")


if __name__ == "__main__":
    main()
