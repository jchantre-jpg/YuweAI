"""Prueba respuestas del chat AVI para chips y ejemplos frecuentes."""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location("avi_server", ROOT / "server.py")
server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)

QUERIES = [
    ("Como saludo?", lambda d: "saludar" in (d.get("answer") or "").lower()),
    ("Como me despido?", lambda d: "desped" in (d.get("answer") or "").lower() and "como," not in (d.get("answer") or "").lower()),
    ("como me despido", lambda d: "desped" in (d.get("answer") or "").lower()),
    ("Despedidas", lambda d: "desped" in (d.get("answer") or "").lower()),
    ("Quiero hablar de mi familia", lambda d: "familia" in (d.get("answer") or "").lower()),
    ("Como digo gracias?", lambda d: "agradec" in (d.get("answer") or "").lower() and "de nada" not in (d.get("answer") or "").lower()),
    ("gracias", lambda d: "de nada" in (d.get("answer") or "").lower()),
    ("hola", lambda d: "hola" in (d.get("answer") or "").lower() or bool(d.get("contexts"))),
    ("Como me despido?", lambda d: "wecha" in (d.get("answer") or "").lower() or "ewcha" in (d.get("answer") or "").lower() or "ma'g" in (d.get("answer") or "").lower()),
    ("quiero aprender numeros", lambda d: "numer" in (d.get("answer") or "").lower() or "aprender" in (d.get("answer") or "").lower()),
    ("como presentarme", lambda d: "saludar" in (d.get("answer") or "").lower() or "present" in (d.get("answer") or "").lower()),
    ("Traduce esta frase", lambda d: "escribe" in (d.get("answer") or "").lower()),
    ("Como se dice…?", lambda d: "palabra" in (d.get("answer") or "").lower()),
    ("Explicame esta palabra", lambda d: "palabra" in (d.get("answer") or "").lower()),
    ("Dame un ejemplo", lambda d: "ejemplo" in (d.get("answer") or "").lower() or "modelo" in (d.get("answer") or "").lower()),
    ("Como se dice perro en nasa yuwe", lambda d: bool(d.get("contexts")) and "de nada" not in (d.get("answer") or "").lower()),
]


def main():
    engine = server.ENGINE
    failed = 0
    for q, check in QUERIES:
        data = engine.ask(q, top_k=5)
        ok = check(data)
        status = "OK" if ok else "FAIL"
        if not ok:
            failed += 1
        ans = (data.get("answer") or "")[:120].replace("\n", " ")
        print(f"[{status}] {q}")
        print(f"  ans: {ans}...")
    print(f"\n{len(QUERIES) - failed}/{len(QUERIES)} passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
