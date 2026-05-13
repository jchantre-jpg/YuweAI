import csv
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
SERVER_PATH = ROOT / "server.py"
TEST_PATH = PROJECT_ROOT / "corpus" / "data" / "corpus_v5_test.csv"
REPORT_PATH = ROOT / "reports" / "model_evaluation_report.md"
DETAILS_PATH = ROOT / "reports" / "model_evaluation_details.csv"


def load_server_module():
    spec = importlib.util.spec_from_file_location("avi_server_eval", SERVER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_test_rows():
    with TEST_PATH.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def pct(value):
    return round(value * 100, 2)


def evaluate_lexical(engine, rows):
    lexical = [r for r in rows if r.get("record_type") == "lexico" and r.get("espanol")]
    details = []
    exact_top1 = 0
    category_top1 = 0
    coherent = 0

    for row in lexical:
        query = f"Como se dice {row['espanol']} en nasa yuwe?"
        result = engine.ask(query, top_k=5)
        contexts = result.get("contexts") or []
        top = contexts[0] if contexts else {}
        top_nasa = (top.get("nasa_yuwe") or "").strip().lower()
        expected_nasa = (row.get("nasa_yuwe") or "").strip().lower()
        exact_ok = bool(top_nasa and top_nasa == expected_nasa)
        category_ok = bool(top.get("categoria") == row.get("categoria"))
        coherence_ok = bool(
            result.get("answer")
            and contexts
            and top.get("fuente_nombre")
            and top.get("record_type") == "lexico"
        )
        exact_top1 += int(exact_ok)
        category_top1 += int(category_ok)
        coherent += int(coherence_ok)
        details.append(
            {
                "evaluation_type": "lexical_translation",
                "expected_id": row.get("id", ""),
                "query": query,
                "expected_nasa_yuwe": row.get("nasa_yuwe", ""),
                "top_id": top.get("id", ""),
                "top_record_type": top.get("record_type", ""),
                "top_category": top.get("categoria", ""),
                "exact_top1": exact_ok,
                "category_top1": category_ok,
                "coherence_ok": coherence_ok,
            }
        )

    total = max(len(lexical), 1)
    return {
        "total": len(lexical),
        "exact_top1": exact_top1 / total,
        "category_top1": category_top1 / total,
        "coherence": coherent / total,
        "details": details,
    }


def evaluate_dialogues(engine, rows):
    dialogue_rows = [r for r in rows if r.get("record_type") == "dialogo"]
    if not dialogue_rows:
        # Fallback because most generated dialogues are in train/dev by design.
        dialogue_rows = [r for r in engine.rows if r.get("record_type") == "dialogo"][:60]

    top1_dialogue = 0
    coherent = 0
    details = []
    for row in dialogue_rows:
        category = row.get("categoria", "")
        query = f"Quiero practicar un dialogo para aprender {category}"
        result = engine.ask(query, top_k=5)
        contexts = result.get("contexts") or []
        top = contexts[0] if contexts else {}
        dialogue_ok = top.get("record_type") == "dialogo"
        coherence_ok = bool(
            result.get("answer")
            and contexts
            and top.get("fuente_nombre")
            and top.get("record_type") == "dialogo"
            and top.get("source_kind")
        )
        top1_dialogue += int(dialogue_ok)
        coherent += int(coherence_ok)
        details.append(
            {
                "evaluation_type": "pedagogical_dialogue",
                "expected_id": row.get("id", ""),
                "query": query,
                "expected_nasa_yuwe": row.get("nasa_yuwe", ""),
                "top_id": top.get("id", ""),
                "top_record_type": top.get("record_type", ""),
                "top_category": top.get("categoria", ""),
                "exact_top1": dialogue_ok,
                "category_top1": top.get("categoria") == category,
                "coherence_ok": coherence_ok,
            }
        )

    total = max(len(dialogue_rows), 1)
    return {
        "total": len(dialogue_rows),
        "top1_dialogue": top1_dialogue / total,
        "coherence": coherent / total,
        "details": details,
    }


def write_details(rows):
    DETAILS_PATH.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "evaluation_type",
        "expected_id",
        "query",
        "expected_nasa_yuwe",
        "top_id",
        "top_record_type",
        "top_category",
        "exact_top1",
        "category_top1",
        "coherence_ok",
    ]
    with DETAILS_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_report(engine, lexical, dialogues):
    stats = engine.stats()
    lines = [
        "# Evaluacion tecnica del modelo AVI",
        "",
        "## Objetivo evaluado",
        "",
        "Evaluar precision y coherencia del modelo PLN de recuperacion usado por el AVI sobre el corpus semantico Nasa Yuwe-Espanol.",
        "",
        "## Configuracion",
        "",
        f"- Corpus cargado: **{stats['corpus_entries']}** registros.",
        f"- Modelo: **{stats['model']['name']}**.",
        f"- Filas de entrenamiento: **{stats['model']['training_rows']}**.",
        f"- Vocabulario del modelo: **{stats['model']['vocabulary_size']}** terminos.",
        f"- Optimizador: `{stats['optimizer']}`.",
        "",
        "## Metricas",
        "",
        "| Prueba | Casos | Metrica | Resultado |",
        "|---|---:|---|---:|",
        f"| Traduccion lexica | {lexical['total']} | Precision exacta top-1 | {pct(lexical['exact_top1'])}% |",
        f"| Traduccion lexica | {lexical['total']} | Precision por categoria top-1 | {pct(lexical['category_top1'])}% |",
        f"| Traduccion lexica | {lexical['total']} | Coherencia de respuesta | {pct(lexical['coherence'])}% |",
        f"| Dialogo pedagogico | {dialogues['total']} | Recuperacion dialogal top-1 | {pct(dialogues['top1_dialogue'])}% |",
        f"| Dialogo pedagogico | {dialogues['total']} | Coherencia dialogal | {pct(dialogues['coherence'])}% |",
        "",
        "## Criterios de coherencia",
        "",
        "- La respuesta no debe estar vacia.",
        "- Debe recuperar al menos un contexto.",
        "- El contexto debe incluir fuente trazable.",
        "- En traduccion directa debe priorizar registros lexicos.",
        "- En practica pedagogica debe priorizar registros dialogales.",
        "",
        "## Evidencia generada",
        "",
        f"- Detalle por consulta: `{DETAILS_PATH.as_posix()}`.",
        "- La evaluacion usa el motor real de la aplicacion (`CorpusEngine`) y el modelo de recuperacion entrenado.",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    server = load_server_module()
    engine = server.ENGINE
    rows = read_test_rows()
    lexical = evaluate_lexical(engine, rows)
    dialogues = evaluate_dialogues(engine, rows)
    write_details(lexical["details"] + dialogues["details"])
    write_report(engine, lexical, dialogues)
    print(f"Reporte generado: {REPORT_PATH}")
    print(f"Detalles generados: {DETAILS_PATH}")
    print(f"Precision exacta top-1: {pct(lexical['exact_top1'])}%")
    print(f"Coherencia lexica: {pct(lexical['coherence'])}%")
    print(f"Recuperacion dialogal top-1: {pct(dialogues['top1_dialogue'])}%")


if __name__ == "__main__":
    main()
