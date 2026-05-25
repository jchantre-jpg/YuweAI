"""Pruebas amplias del chat AVI: chips, temas y preguntas libres."""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location("avi_server", ROOT / "server.py")
server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)

ENGINE = server.ENGINE


def _ans(data: dict) -> str:
    return (data.get("answer") or "").lower()


def _has_ny(data: dict) -> bool:
    return bool(data.get("contexts"))


def _not_empty_fail(data: dict) -> bool:
    a = _ans(data)
    return "todavia no tengo" not in a and "no tengo una coincidencia" not in a


def _not_meta_gloss(data: dict) -> bool:
    a = _ans(data)
    return "ma'w? — como" not in a and "como se dice" not in a or "escribe" in a


# (consulta, validador)
QUERIES: list[tuple[str, object]] = [
    # Chips y temas frecuentes
    ("Como saludo?", lambda d: "saludar" in _ans(d) or "saludo" in _ans(d)),
    ("Como me despido?", lambda d: "desped" in _ans(d) and "como," not in _ans(d)),
    ("como me despido", lambda d: "desped" in _ans(d)),
    ("Despedidas", lambda d: "desped" in _ans(d)),
    ("Quiero hablar de mi familia", lambda d: "familia" in _ans(d)),
    ("Como digo gracias?", lambda d: "agradec" in _ans(d) and "de nada" not in _ans(d)),
    ("gracias", lambda d: "de nada" in _ans(d)),
    ("hola", lambda d: "hola" in _ans(d) or _has_ny(d)),
    ("quiero aprender numeros", lambda d: any(x in _ans(d) for x in ("numer", "uno", "tee", "trabajar"))),
    ("como presentarme", lambda d: "salud" in _ans(d) or "present" in _ans(d)),
    ("Traduce esta frase", lambda d: "escribe" in _ans(d)),
    ("Como se dice…?", lambda d: "palabra" in _ans(d)),
    ("Explicame esta palabra", lambda d: "palabra" in _ans(d) or "cual" in _ans(d)),
    ("Dame un ejemplo", lambda d: "ejemplo" in _ans(d) or "modelo" in _ans(d)),
    ("Como se dice perro en nasa yuwe", lambda d: _has_ny(d) and "de nada" not in _ans(d) and "perro" in _ans(d)),
    ("buenos dias", lambda d: "salud" in _ans(d) or "ma'g" in _ans(d) or "fxi" in _ans(d)),
    ("ayudame con animales", lambda d: "animal" in _ans(d)),
    # Preguntas libres — palabra suelta
    ("agua", lambda d: _not_empty_fail(d) and ("yu'" in _ans(d) or "agua" in _ans(d))),
    ("perro", lambda d: _not_empty_fail(d) and ("alcu" in _ans(d) or "perro" in _ans(d))),
    ("gato", lambda d: _not_empty_fail(d) and ("gato" in _ans(d) or "•" in (d.get("answer") or ""))),
    ("sol", lambda d: _not_empty_fail(d) and ("sek" in _ans(d) or "sol" in _ans(d))),
    ("rojo", lambda d: _not_empty_fail(d) and ("rojo" in _ans(d) or "bej" in _ans(d))),
    ("mama", lambda d: _not_empty_fail(d) and ("mama" in _ans(d) or "abuel" in _ans(d))),
    ("casa", lambda d: _not_empty_fail(d) and _not_meta_gloss(d)),
    ("arbol", lambda d: _not_empty_fail(d) and ("arbol" in _ans(d) or "kwet" in _ans(d))),
    # Variantes de pregunta
    ("como se dice agua", lambda d: "escribe" not in _ans(d) and _not_empty_fail(d) and ("agua" in _ans(d) or "yu'" in _ans(d))),
    ("que significa agua", lambda d: _not_empty_fail(d) and "agua" in _ans(d)),
    ("que es perro", lambda d: _not_empty_fail(d) and "perro" in _ans(d)),
    ("significado de casa", lambda d: _not_empty_fail(d) and "casa" in _ans(d)),
    ("traduce hola a nasa yuwe", lambda d: _not_empty_fail(d) and ("hola" in _ans(d) or "ewcha" in _ans(d) or "ma'g" in _ans(d))),
    ("explicame la palabra agua", lambda d: _not_empty_fail(d) and "agua" in _ans(d)),
    # Typo / sin tilde
    ("montana", lambda d: _not_empty_fail(d) and ("monta" in _ans(d) or "vits" in _ans(d))),
    ("numeros", lambda d: _not_empty_fail(d) and ("numer" in _ans(d) or "uno" in _ans(d) or "tee" in _ans(d))),
    ("colores", lambda d: _not_empty_fail(d) and "color" in _ans(d)),
    # Frases cortas del usuario
    ("me llamo ana", lambda d: _not_empty_fail(d)),
    ("quiero practicar saludos", lambda d: "salud" in _ans(d)),
    ("cuantos colores hay", lambda d: "color" in _ans(d)),
    # No debe confundir gracias con lección de agradecer
    ("muchas gracias avi", lambda d: "de nada" in _ans(d)),
    ("como digo gracias en clase", lambda d: "agradec" in _ans(d)),
]


def main():
    failed = 0
    for q, check in QUERIES:
        data = ENGINE.ask(q, top_k=5)
        ok = check(data)
        status = "OK" if ok else "FAIL"
        if not ok:
            failed += 1
        ans = (data.get("answer") or "")[:140].replace("\n", " ")
        print(f"[{status}] {q}")
        print(f"  ans: {ans}...")
    total = len(QUERIES)
    print(f"\n{total - failed}/{total} passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
