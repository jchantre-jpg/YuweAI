#!/usr/bin/env python3
"""
Copia corpus_bilingue_v5.csv desde la carpeta corpus del monorepo (../corpus/data/)
hacia YuweAI/corpus/data/, para que Docker/Render empaqueten el corpus completo.

Uso (desde la raíz del repo YuweAI):
  python scripts/sync_corpus_from_project.py
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT.parent / "corpus" / "data" / "corpus_bilingue_v5.csv"
DST = ROOT / "corpus" / "data" / "corpus_bilingue_v5.csv"


def main() -> int:
    if not SRC.is_file():
        print(f"No se encontro origen: {SRC}", file=sys.stderr)
        return 1
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SRC, DST)
    n = sum(1 for _ in DST.open(encoding="utf-8")) - 1
    print(f"OK: {SRC} -> {DST} ({n} filas de datos)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
