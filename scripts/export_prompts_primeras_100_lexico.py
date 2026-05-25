"""
Lee corpus/IMAGENES_LEXICO_DESCARGA.md y exporta las primeras N filas de tabla
con prompts listos para IA (estilo mascota / logo Nasa Yuwe).

Uso (desde carpeta YuweAI):
  python scripts/export_prompts_primeras_100_lexico.py
  python scripts/export_prompts_primeras_100_lexico.py --limit 100
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MD_PATH = REPO / "corpus" / "IMAGENES_LEXICO_DESCARGA.md"
OUT_DIR = REPO / "corpus" / "generadas-img-ia"

ROW_RE = re.compile(
    r"^\|\s*`([^`]+\.(?:jpg|webp))`\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*`([^`]+)`\s*\|\s*$"
)

# Rotacion de personajes: **pueblo Nasa / lengua Nasa Yuwe — Cauca, Colombia**
# (Nasa = nacion indigena; NO la agencia espacial estadounidense NASA / cohetes / astronautas)
ARCHETYPES = [
    "a young Nasa Yuwe girl from Colombia's Cauca region (indigenous Nasa nation, Nasa Yuwe language community — not NASA aerospace), warm smile, traditional woven straw hat vu'ts paju style, black aksu ruana with red green yellow black rhombus geometry, small gold hoop earrings, dignified and friendly like an educational app mascot",
    "a young Nasa Yuwe boy from Colombia Cauca (indigenous Nasa people, Nasa Yuwe — not space agency NASA), warm smile, straw hat, black woven garment with Nasa textile trim red green yellow, dignified educational mascot style",
    "an adult Nasa Yuwe woman from Colombia Cauca (Nasa indigenous nation), gentle expression, straw hat with woven band, black woven dress with Nasa geometric patterns and modest jewelry, respectful cultural dress",
    "an adult Nasa Yuwe man from Colombia Cauca (Nasa indigenous nation), calm friendly expression, straw hat, black woven poncho with red green yellow Nasa borders, respectful educational illustration",
    "an elderly Nasa Yuwe woman from Colombia Cauca (Nasa indigenous nation), kind face, straw hat, woven shawl with Nasa rhombus motifs green red black gold, wise grandmother energy, respectful",
    "an elderly Nasa Yuwe man from Colombia Cauca (Nasa indigenous nation), wise gentle smile, straw hat, dark woven mantle with traditional Nasa geometry, respectful elder character",
]

STYLE_BLOCK = (
    "Stylized high-quality 3D illustration matching the SAME art direction as the Yuwe / Nasa Yuwe educational app mascot (Colombia): "
    "smooth 3D surfaces, soft cinematic lighting, warm brown skin tones, large expressive eyes, polished Pixar-like cartoon 3D, NOT photorealistic stock photo, NOT generic 'native American' stereotypes. "
    "**Disambiguation:** 'Nasa' here means the **indigenous Nasa people and Nasa Yuwe language of Cauca, Colombia** — **NOT** the U.S. **NASA** space agency: **no** astronauts, spacesuits, rockets, shuttles, satellites, planets as space-tech, moon landing, NASA logos. "
    "Cultural anchor: **Nasa indigenous nation (Nasa Yuwe) of Cauca, Colombia** — handmade **aksu** textiles with **green, red, yellow, black** rhombus and step patterns, **vu'ts / paju** woven straw hat textures, dark woven ruana or tunic. "
    "Avoid: feather headdresses, tipis, Amazon jungle clichés, Mexican sombrero stereotypes, face paint war bonnets, Inca temples unless clearly incidental; keep Andean Cauca dignity and school-safe tone. "
    "Composition: MAIN FOCUS is an oversized educational subject in foreground (clear readable silhouette), Nasa character smaller beside it, hands naturally presenting the subject, poster-like scale. "
    "Background: fully transparent alpha OR solid flat pure black for later matting — no landscape scene, no floor, no horizon, no sky unless subject requires a tiny hint (prefer none). "
    "No text, no letters, no watermark, centered, clean edges, ultra detailed, 4K friendly."
)


def subject_clause(espanol: str, categoria: str, rel_path: str) -> str:
    es = espanol.strip()
    cat = categoria.strip()
    folder = rel_path.split("/")[0] if "/" in rel_path else ""
    return (
        f"The educational subject is: {es} (lexical theme: {cat}; category folder: {folder}). "
        f"Render {es} large, appealing, botanically or contextually accurate for teaching, vivid colors, appetitive or clear shapes."
    )


def build_prompt(archetype: str, subject: str) -> str:
    return (
        f"Create a {STYLE_BLOCK} "
        f"{subject} "
        f"Character: {archetype}. "
        "Avoid gore; avoid stereotypes outside respectful Nasa Yuwe dress; family-friendly; celebrate Nasa identity with accuracy and dignity."
    )


def parse_md_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    text = MD_PATH.read_text(encoding="utf-8")
    for line in text.splitlines():
        m = ROW_RE.match(line.strip())
        if not m:
            continue
        rel, es_label, nasa, rid = m.groups()
        rel = rel.strip()
        cat = rel.split("/")[0] if "/" in rel else "general"
        rows.append(
            {
                "archivo_sugerido": rel,
                "archivo_png": rel.rsplit(".", 1)[0] + ".png",
                "espanol": es_label.strip(),
                "nasa_yuwe": nasa.strip(),
                "id": rid.strip(),
                "categoria": cat,
            }
        )
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=100)
    args = ap.parse_args()

    all_rows = parse_md_rows()
    if not all_rows:
        raise SystemExit(f"No se encontraron filas de tabla en {MD_PATH}")

    chunk = all_rows[: max(1, args.limit)]
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    manifest: list[dict[str, object]] = []

    for i, r in enumerate(chunk):
        arch = ARCHETYPES[i % len(ARCHETYPES)]
        subj = subject_clause(r["espanol"], r["categoria"], r["archivo_sugerido"])
        prompt = build_prompt(arch, subj)
        manifest.append(
            {
                "idx": i + 1,
                **r,
                "arquetipo": arch,
                "prompt_en": prompt,
            }
        )

    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    with (OUT_DIR / "primeras_100.csv").open("w", encoding="utf-8", newline="") as cf:
        w = csv.writer(cf)
        w.writerow(
            ["idx", "archivo_png", "id", "espanol", "categoria", "nasa_yuwe", "arquetipo"]
        )
        for i, m in enumerate(manifest):
            r = chunk[i]
            w.writerow(
                [
                    i + 1,
                    r["archivo_png"],
                    r["id"],
                    r["espanol"],
                    r["categoria"],
                    r["nasa_yuwe"],
                    ARCHETYPES[i % len(ARCHETYPES)],
                ]
            )
    (OUT_DIR / "prompts_one_per_line.txt").write_text(
        "\n\n---PROMPT_SEPARATOR---\n\n".join(m["prompt_en"] for m in manifest),
        encoding="utf-8",
    )

    readme = f"""# Imagenes generadas con IA (lote primeras {len(chunk)})

Este directorio guarda **PNG** (transparente o fondo negro para recortar) alineados al **diccionario** (`IMAGENES_LEXICO_DESCARGA.md`).

## Estilo: **Nasa Yuwe (Cauca, Colombia) — no NASA espacial**

- **Nasa Yuwe** = **pueblo Nasa** y **lengua Nasa Yuwe** del **Cauca** (Colombia): tejidos **aksu**, sombrero **vu'ts / paju**, mascota educativa de la app.
- **NASA** (EE.UU.) = agencia **aeroespacial**: **no** cohetes, astronautas ni iconos de espacio en estas imagenes.

Guia y frase lista para prompts: **`ESTILO_NASA_YUWE_IA.md`**.

## Archivos generados por script

- `ESTILO_NASA_YUWE_IA.md` — recordatorio de estilo (editado a mano; no lo pisa este script).
- `manifest.json` — metadatos + **prompt_en** por entrada.
- `primeras_100.csv` — indice compacto.
- `prompts_one_per_line.txt` — prompts separados por `---PROMPT_SEPARATOR---`.

## Copiar PNG a las subcarpetas correctas

Desde `YuweAI` (tras poner PNG en `imagenes app/` o en `assets` de Cursor como `animales_aguila.png`):

```bash
python scripts/sync_primeras_100_imagenes.py --limit 100
```

Solo assets Cursor (`dict-img-*`, `categoria_lemma.png`):

```bash
python scripts/organize_generadas_img_ia.py
```

## Convencion de nombres

Usa el campo **`archivo_png`** del manifest, p. ej. `alimentos/arveja.png`.

## Regenerar prompts

```bash
python scripts/export_prompts_primeras_100_lexico.py --limit 100
```

## Nota sobre Cursor

La generacion masiva de imagenes conviene hacerla en tu motor de IA; aqui quedan **prompts y rutas** coherentes con el corpus.
"""
    (OUT_DIR / "README.md").write_text(readme, encoding="utf-8")

    print(f"OK: {len(chunk)} entradas -> {OUT_DIR}")
    print("  manifest.json, primeras_100.csv, prompts_one_per_line.txt, README.md")


if __name__ == "__main__":
    main()
