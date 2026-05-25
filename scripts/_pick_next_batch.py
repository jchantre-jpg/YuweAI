"""Pick next missing visual entries from DICCIONARIO + jsonl."""
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
dest = REPO / "corpus" / "generadas-img-ia-solo"
existing = {p.relative_to(dest).as_posix() for p in dest.rglob("*.png")}
id_dest = {}
for line in (REPO / "corpus/generadas-img-ia-solo/prompts_solo_full.jsonl").read_text(
    encoding="utf-8"
).splitlines():
    o = json.loads(line)
    id_dest[o["id"]] = o

visual = re.compile(
    r"\b(abeja|hormiga|rana|sapo|jaguar|aguila|tucan|tomate|banano|mango|naranja|limon|"
    r"nadar|cantar|tocar|tambor|flauta|cuchara|sarten|machete|canasta|olla|luna|sol|nube|"
    r"lluvia|viento|piedra|madera|langosta|delfin|murci|armadillo|venado|conejo|cerdo|vaca|"
    r"burro|oveja|cabra|pato|mariposa|libelula|grillo|cucaracha|lavar|cocinar|abrazar|besar|"
    r"saludar|gritar|caminar|subir|bajar|trepar|plantar|sembrar|pescar|ladrar|mugir|sonreir|"
    r"llorar|saltar|volar|comer|beber|dormir|hornear|freir|hervir|hongo|breva|cedro|brea|"
    r"fuego|agua|pez|serpiente|culebra|araña|lobo|zorro|ardilla|oso|leon|tigre|gato|perro|"
    r"caballo|gallo|gallina|paloma|loro|mono|chivo|cuy|raton|luciernaga|escarabajo|mosca)\b",
    re.I,
)
skip = re.compile(r"pene|vagina|seno|^[0-9]|defecar|cagar", re.I)
row_re = re.compile(
    r"^\|\s*\d+\s*\|\s*`(LEX[^`]+)`\s*\|\s*([^|]+?)\s*\|\s*diccionario_general\s*\|\s*- \[ \] falta"
)

batch = []
for line in (REPO / "corpus/data/DICCIONARIO-PALABRAS-COMPLETO.md").read_text(
    encoding="utf-8"
).splitlines():
    m = row_re.search(line.strip())
    if not m:
        continue
    rid, es = m.group(1), m.group(2).strip()
    if skip.search(es):
        continue
    row = id_dest.get(rid)
    if not row or row["dest_rel"] in existing:
        continue
    if visual.search(es) and len(es) < 55 and "," not in es and ";" not in es:
        batch.append((rid, es, row["asset_filename"], row["dest_rel"]))
    if len(batch) >= 16:
        break

for rid, es, a, d in batch:
    print(f"{rid}\t{es}\t{a}")
print(f"TOTAL_DISK={len(existing)} BATCH={len(batch)}")
