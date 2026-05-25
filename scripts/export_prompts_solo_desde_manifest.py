"""
Lee corpus/generadas-img-ia/manifest.json y exporta prompts **solo tema**
(fondo blanco; significado fiel al lema) + nombre de archivo para assets: solo__<cat>__<stem>.png

Excepciones: `parentescos` y `nombres_propios` (misma lógica que export_prompts_solo_desde_lexico_md.py).

Uso (desde YuweAI):
  python scripts/export_prompts_solo_desde_manifest.py
  python scripts/export_prompts_solo_desde_manifest.py --limit 100
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "corpus" / "generadas-img-ia" / "manifest.json"
OUT_JSONL = REPO / "corpus" / "generadas-img-ia-solo" / "prompts_solo.jsonl"

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
    f"{SOLO_COLOR_VS_WHITE_BG} "
    "No text, no watermark. "
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
    f"{SOLO_WHITE_BG_TAIL} {SOLO_COLOR_VS_WHITE_BG} "
    "No labels, no captions, no extra people in frame."
)

SOLO_NOMBRES_PREFIX = (
    "Stylized high-quality 3D dictionary illustration for the Yuwe / Nasa Yuwe educational app (Colombia): "
    "indigenous Nasa nation of Cauca and Nasa Yuwe language context — NOT the U.S. NASA space agency, "
    "no astronauts, rockets, or spacesuits. Smooth Pixar-like cartoon 3D, soft cinematic lighting, vivid colors. "
    "THIS ENTRY IS A GIVEN NAME: the main focus must be LARGE legible 3D display letters that spell the COMPLETE first name "
    "with every letter shown (full name spelling), NOT initials, NOT a monogram, NOT abbreviated. "
    "Each letter chunky glossy colorful kid-friendly font on a simple stand or ribbon; optional tiny aksu rhombus motif on the letter blocks only. "
    "No people required; if any tiny decorative mascot appears it must not replace the spelled-out letters. "
    f"{SOLO_WHITE_BG_TAIL} {SOLO_COLOR_VS_WHITE_BG} "
    "Centered composition."
)


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
            f"The exact full first name to spell letter-by-letter in the image is: {es} "
            f"(use those letters and accents as appropriate; all characters of the name visible)."
        )

    return (
        f"{SOLO_LEXICO_SEMANTIC} "
        f"The Spanish gloss to illustrate is: «{es}» (lexical category: {cat}). "
        f"Make the main idea large, readable, and unmistakable for a school dictionary card."
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="0 = todas las filas del manifest")
    args = ap.parse_args()

    if not MANIFEST.is_file():
        raise SystemExit(f"No existe {MANIFEST}")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rows = manifest if args.limit <= 0 else manifest[: args.limit]

    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with OUT_JSONL.open("w", encoding="utf-8") as f:
        for row in rows:
            rel = row.get("archivo_png") or ""
            if "/" not in rel:
                continue
            cat, fname = rel.split("/", 1)
            stem = Path(fname).stem.lower()
            asset_name = f"solo__{cat.lower()}__{stem}.png"
            prompt = build_solo_prompt(str(row.get("espanol", stem)), str(row.get("categoria", cat)))
            f.write(
                json.dumps(
                    {"asset_filename": asset_name, "dest_rel": f"{cat.lower()}/{stem}.png", "prompt_en": prompt},
                    ensure_ascii=False,
                )
                + "\n"
            )
            n += 1

    print(f"Escritas {n} lineas en {OUT_JSONL.relative_to(REPO)}")


if __name__ == "__main__":
    main()
