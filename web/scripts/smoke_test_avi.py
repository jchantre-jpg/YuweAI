import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SERVER_PATH = ROOT / "server.py"


def load_server_module():
    spec = importlib.util.spec_from_file_location("avi_server", SERVER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_true(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    server = load_server_module()
    engine = server.ENGINE

    stats = engine.stats()
    assert_true(stats["corpus_entries"] >= 4593, "El corpus cargado no incluye la version reforzada.")
    assert_true(stats["record_types"].get("dialogo", 0) >= 360, "No se cargaron los dialogos pedagogicos.")
    assert_true(stats["model"]["training_rows"] > 0, "El modelo de recuperacion entrenado no fue cargado.")

    direct = engine.ask("Como se dice perro en nasa yuwe?", top_k=3)
    assert_true(direct["contexts"], "La consulta directa no recupero contextos.")
    assert_true(direct["contexts"][0]["record_type"] == "lexico", "La traduccion directa debe priorizar lexico real.")

    practice = engine.ask("Quiero practicar un dialogo para aprender animales", top_k=3)
    assert_true(practice["contexts"], "La consulta pedagogica no recupero contextos.")
    assert_true(practice["contexts"][0]["record_type"] == "dialogo", "La practica debe priorizar dialogos.")

    dialogues = engine.dialogues("animales", limit=3)
    assert_true(len(dialogues["dialogues"]) == 3, "El endpoint logico de dialogos no devuelve el limite esperado.")

    print("Smoke test AVI: OK")
    print(f"Entradas corpus: {stats['corpus_entries']}")
    print(f"Dialogos: {stats['record_types'].get('dialogo', 0)}")
    print(f"Modelo: {stats['model']['name']} ({stats['model']['training_rows']} filas train)")


if __name__ == "__main__":
    main()
