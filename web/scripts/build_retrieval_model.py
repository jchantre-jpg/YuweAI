import csv
import json
import math
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
TRAIN_PATH = PROJECT_ROOT / "corpus" / "data" / "corpus_v5_train.csv"
OUT_PATH = ROOT / "models" / "retrieval_model_v1.json"


def normalize_text(text: str) -> str:
    text = (text or "").lower().strip()
    text = text.replace("’", "'").replace("`", "'").replace("´", "'")
    text = re.sub(r"[^a-zA-Z0-9áéíóúüñçëïä'\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str):
    return [t for t in normalize_text(text).split(" ") if t]


def main():
    rows = []
    with TRAIN_PATH.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    doc_freq = Counter()
    record_types = Counter()
    categories = Counter()
    source_kinds = Counter()
    for row in rows:
        text = " ".join(
            [
                row.get("nasa_yuwe", ""),
                row.get("espanol", ""),
                row.get("categoria", ""),
                row.get("record_type", ""),
                row.get("intencion", ""),
            ]
        )
        for token in set(tokenize(text)):
            doc_freq[token] += 1
        record_types[row.get("record_type", "")] += 1
        categories[row.get("categoria", "")] += 1
        source_kinds[row.get("source_kind", "")] += 1

    total_docs = max(len(rows), 1)
    idf = {
        token: round(math.log((1 + total_docs) / (1 + freq)) + 1.0, 8)
        for token, freq in sorted(doc_freq.items())
    }
    model = {
        "model_name": "AVI Retrieval Model v1",
        "model_type": "tfidf_idf_mmr_retrieval",
        "trained_on": str(TRAIN_PATH.as_posix()),
        "training_rows": len(rows),
        "vocabulary_size": len(idf),
        "optimizer": "idf_overlap + mmr + ttl_cache + lexical_priority + pedagogical_dialogue_boost",
        "record_types": dict(record_types),
        "categories": dict(categories),
        "source_kinds": dict(source_kinds),
        "idf": idf,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(model, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Modelo de recuperacion generado: {OUT_PATH}")
    print(f"Filas de entrenamiento: {len(rows)}")
    print(f"Vocabulario: {len(idf)}")


if __name__ == "__main__":
    main()
