"""Divide solo-img-ia.tar.gz en partes < 2 GB para GitHub Releases."""
from __future__ import annotations

import sys
from pathlib import Path

CHUNK = 1_900_000_000  # GitHub limit 2147483648


def main() -> int:
    src = Path(__file__).resolve().parents[1] / "solo-img-ia.tar.gz"
    if not src.is_file():
        print(f"No existe: {src}", file=sys.stderr)
        return 2
    out_dir = src.parent / "solo-img-ia-parts"
    out_dir.mkdir(exist_ok=True)
    for old in out_dir.glob("solo-img-ia.tar.gz.part*"):
        old.unlink()

    size = src.stat().st_size
    part = 0
    with src.open("rb") as f:
        while True:
            chunk = f.read(CHUNK)
            if not chunk:
                break
            part += 1
            out = out_dir / f"solo-img-ia.tar.gz.part{part:03d}"
            out.write_bytes(chunk)
            print(f"Escrito {out.name} ({len(chunk) / 1e9:.2f} GB)")

    print(f"\nTotal: {size / 1e9:.2f} GB en {part} partes -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
