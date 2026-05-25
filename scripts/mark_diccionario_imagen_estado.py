"""
Marca filas en DICCIONARIO-PALABRAS-COMPLETO.md por id:
  - [~] en curso
  - [x] listo (si existe PNG)
  - [ ] falta

Uso:
  python scripts/mark_diccionario_imagen_estado.py LEXR-02901 --estado curso
  python scripts/mark_diccionario_imagen_estado.py LEXR-02901 LEXR-01016 --estado listo
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DIC_PATH = REPO / "corpus" / "data" / "DICCIONARIO-PALABRAS-COMPLETO.md"
JSONL_PATH = REPO / "corpus" / "generadas-img-ia-solo" / "prompts_solo_full.jsonl"
IMG_ROOT = REPO / "corpus" / "generadas-img-ia-solo"

ROW_RE = re.compile(
    r"^(\|\s*\d+\s*\|\s*`(?P<rid>[^`]+)`\s*\|\s*(?P<es>[^|]*?)\s*\|\s*(?P<cat>[^|]*?)\s*\|)(?P<cell>[^|]*?)(\|\s*)$",
    re.MULTILINE,
)


def load_id_to_dest() -> dict[str, str]:
    out: dict[str, str] = {}
    for line in JSONL_PATH.read_text(encoding="utf-8").splitlines():
        if line.strip():
            o = json.loads(line)
            out[o["id"]] = o["dest_rel"]
    return out


def cell_for(estado: str, dest: str | None) -> str:
    if estado == "curso":
        return " - [~] en curso |"
    if estado == "listo" and dest:
        p = IMG_ROOT / dest
        if p.is_file():
            return f" - [x] `{dest}` |"
        return f" - [~] en curso (PNG pendiente sync) |"
    return " - [ ] falta |"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="+", help="LEX-... o LEXR-...")
    ap.add_argument("--estado", choices=["curso", "listo", "falta"], default="listo")
    args = ap.parse_args()

    id_to_dest = load_id_to_dest()
    text = DIC_PATH.read_text(encoding="utf-8")
    changed = 0

    for rid in args.ids:
        dest = id_to_dest.get(rid)
        new_cell = cell_for(args.estado, dest)

        def repl(m: re.Match[str]) -> str:
            if m.group("rid") != rid:
                return m.group(0)
            return f"{m.group(1)}{new_cell}"

        new_text, n = ROW_RE.subn(repl, text)
        if n:
            text = new_text
            changed += 1
        else:
            print(f"No encontrado en tabla pares: {rid}")

    if changed:
        DIC_PATH.write_text(text, encoding="utf-8")
    print(f"Actualizadas {changed} filas -> {args.estado}")


if __name__ == "__main__":
    main()
