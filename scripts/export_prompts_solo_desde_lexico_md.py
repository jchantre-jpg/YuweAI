"""
Lee corpus/IMAGENES_LEXICO_DESCARGA.md (todo el lexico) y exporta prompts **solo tema**
(fondo blanco solo en el telón; personajes y objetos siempre a color vivo y saturado) + nombres para assets: solo__<cat>__<stem>.png

Excepciones ya especializadas: `parentescos`, `nombres_propios`.

Criterio general: si el lema es una acción humana típica (p. ej. bailar, correr), deben verse
personajes realizando la acción, no solo objetos simbólicos sueltos. Animales y objetos: la entidad nombrada.

Salida: corpus/generadas-img-ia-solo/prompts_solo_full.jsonl

Uso (desde YuweAI):
  python scripts/export_prompts_solo_desde_lexico_md.py
  python scripts/export_prompts_solo_desde_lexico_md.py --limit 500
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MD_PATH = REPO / "corpus" / "IMAGENES_LEXICO_DESCARGA.md"
OUT_JSONL = REPO / "corpus" / "generadas-img-ia-solo" / "prompts_solo_full.jsonl"

ROW_RE = re.compile(
    r"^\|\s*`([^`]+\.(?:jpg|webp))`\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*`([^`]+)`\s*\|\s*$"
)

NO_TEXT_RULE = (
    "ABSOLUTELY ZERO TEXT IN THE IMAGE (critical): no letters, no words, no labels, no captions, "
    "no numbers printed as glyphs, no signs, no banners, no speech bubbles, no watermarks, "
    "no logos, no typography of any language anywhere in the frame — pure illustration only."
)

SOLO_COLOR_VS_WHITE_BG = (
    "COLOR vs BACKGROUND (mandatory): ONLY the flat studio backdrop is pure white #FFFFFF. "
    "All foreground content — people, animals, plants, food, tools, props, hair, skin, clothing — "
    "must be vivid, saturated MULTICOLOR (clear reds, greens, blues, yellows, earth tones as fits the subject). "
    "Do NOT output a mostly white, gray, or beige illustration; do NOT paint the main subject the same white as the background (no white-on-white). "
    "Strong contrast so the subject pops off the white screen."
)

SOLO_LEXICO_SEMANTIC = (
    "Stylized high-quality 3D dictionary illustration for the Yuwe / Nasa Yuwe educational app (Colombia): "
    "indigenous Nasa nation of Cauca and Nasa Yuwe language context — NOT the U.S. NASA space agency, "
    "no astronauts, rockets, or spacesuits. Smooth Pixar-like cartoon 3D, soft cinematic lighting, "
    "vivid colors, polished surfaces, NOT photorealistic stock photo. "
    "SEMANTIC ACCURACY (mandatory): show what a child must learn from the Spanish gloss — the REAL meaning, not misleading metonymy. "
    "If the gloss names an ACTION or ACTIVITY usually performed by people (dance, run, write, wash, draw, give, open arms, etc.), "
    "show clear stylized 3D cartoon PEOPLE performing that action with correct poses, outfits, and small props — "
    "for example for «bailar» / dance: TWO people dancing together in dance clothes, NOT only a disconnected dress and shoes without dancers. "
    "If it names an ANIMAL, PLANT, or FOOD, show THAT species or item clearly. "
    "If it names a TOOL, BODY PART, VEHICLE, or OBJECT, show THAT concrete thing in respectful educational style. "
    "If it names a QUALITY (shape, texture, temperature, mood), show an immediate visual that matches (e.g. wet surface, dirty hands, round ball). "
    "Background MUST be a solid flat pure WHITE (#FFFFFF) seamless studio backdrop ONLY — no horizon, landscape, floor tiles, checkerboard, "
    "no gray studio gradient. Centered composition. "
    f"{NO_TEXT_RULE} "
    "Optional subtle aksu rhombus motif on clothing or objects. Friendly faces; no gore; no sexualized content."
)

SOLO_WHITE_BG_TAIL = (
    "Background MUST be a solid flat pure WHITE (#FFFFFF) seamless backdrop: isolated subject only, "
    "NO transparency checkerboard, NO gray studio, NO black, NO floor tiles, NO horizon, NO sky gradient. "
    "NOT photorealistic stock photo. No watermark."
)

SOLO_PARENTESCOS_PREFIX = (
    "Stylized high-quality 3D dictionary illustration for the Yuwe / Nasa Yuwe educational app (Colombia): "
    "indigenous Nasa nation of Cauca and Nasa Yuwe language context — NOT the U.S. NASA space agency, "
    "no astronauts, rockets, or spacesuits. Smooth Pixar-like cartoon 3D, soft cinematic lighting, "
    "vivid colors, friendly school-dictionary character. "
    "THIS ENTRY IS KINSHIP: show ONE clear figure in human likeness (Pixar-style bust OR cute rounded vinyl art-toy collectible proportions) "
    "that obviously matches the Spanish kinship term (age, role). "
    "Waist-up or three-quarter view, centered, warm expression, modest everyday clothing; optional subtle aksu rhombus pattern on fabric. "
    f"{SOLO_WHITE_BG_TAIL} {SOLO_COLOR_VS_WHITE_BG} {NO_TEXT_RULE} "
    "No extra people in frame."
)

SOLO_NOMBRES_PREFIX = (
    "Stylized high-quality 3D dictionary illustration for the Yuwe / Nasa Yuwe educational app (Colombia): "
    "indigenous Nasa nation of Cauca and Nasa Yuwe language context — NOT the U.S. NASA space agency, "
    "no astronauts, rockets, or spacesuits. Smooth Pixar-like cartoon 3D, soft cinematic lighting, vivid colors. "
    "THIS ENTRY IS A GIVEN NAME: show ONE friendly stylized 3D cartoon person (child or adult as fits the name) as a portrait avatar — "
    "warm smile, modest clothing, optional subtle aksu rhombus on fabric. Do NOT spell the name with letters. "
    f"{SOLO_WHITE_BG_TAIL} {SOLO_COLOR_VS_WHITE_BG} {NO_TEXT_RULE} "
    "Centered composition."
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


def build_solo_prompt(espanol: str, categoria: str) -> str:
    es = espanol.strip()
    cat = categoria.strip().lower()

    if cat == "parentescos":
        return (
            f"{SOLO_PARENTESCOS_PREFIX} "
            f"The kinship term to depict visually is: «{es}». "
            f"Make the character read immediately as a typical {es} for a children's language app."
        )

    if cat == "nombres_propios":
        return (
            f"{SOLO_NOMBRES_PREFIX} "
            f"The given first name is: {es}. Depict a single likable character whose age and vibe fit a person named {es}; "
            f"no written name, no letters, no typography."
        )

    return (
        f"{SOLO_LEXICO_SEMANTIC} "
        f"The Spanish gloss to illustrate is: «{es}» (lexical category: {cat}). "
        f"Make the main idea large, readable, and unmistakable for a school dictionary card."
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="0 = todas las filas del MD")
    args = ap.parse_args()

    if not MD_PATH.is_file():
        raise SystemExit(f"No existe {MD_PATH}")

    all_rows = parse_md_rows()
    if not all_rows:
        raise SystemExit("No se encontraron filas de tabla en el MD")

    rows = all_rows if args.limit <= 0 else all_rows[: args.limit]

    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with OUT_JSONL.open("w", encoding="utf-8") as f:
        for i, row in enumerate(rows):
            rel = row["archivo_png"]
            if "/" not in rel:
                continue
            cat, fname = rel.split("/", 1)
            stem = Path(fname).stem  # conserva mayusculas del archivo; assets suelen en minuscula
            stem_key = stem.lower()
            asset_name = f"solo__{cat.lower()}__{stem_key}.png"
            prompt = build_solo_prompt(row["espanol"], str(row["categoria"]))
            f.write(
                json.dumps(
                    {
                        "idx": i + 1,
                        "id": row["id"],
                        "asset_filename": asset_name,
                        "dest_rel": f"{cat.lower()}/{stem_key}.png",
                        "prompt_en": prompt,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
            n += 1

    print(f"Escritas {n} lineas en {OUT_JSONL.relative_to(REPO)}")


if __name__ == "__main__":
    main()
