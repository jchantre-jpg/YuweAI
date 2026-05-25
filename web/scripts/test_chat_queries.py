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
    return "ma'w? — como" not in a and ("como se dice" not in a or "escribe" in a)


def _no_generic_summary(data: dict) -> bool:
    return "te resumo de forma directa" not in _ans(data)


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
    ("buenas noches", lambda d: "salud" in _ans(d) or "ma'g" in _ans(d) or "fxi" in _ans(d)),
    ("ayudame con animales", lambda d: "animal" in _ans(d)),
    # Preguntas libres — palabra suelta
    ("agua", lambda d: _not_empty_fail(d) and ("yu'" in _ans(d) or "agua" in _ans(d))),
    ("perro", lambda d: _not_empty_fail(d) and ("alcu" in _ans(d) or "perro" in _ans(d))),
    ("gato", lambda d: _not_empty_fail(d) and ("gato" in _ans(d) or "mish" in _ans(d))),
    ("sol", lambda d: _not_empty_fail(d) and "sek" in _ans(d)),
    ("luna", lambda d: _not_empty_fail(d) and ("a'te" in _ans(d) or "ate" in _ans(d) or "luna" in _ans(d))),
    ("fuego", lambda d: _not_empty_fail(d) and ("ipx" in _ans(d) or "fuego" in _ans(d))),
    ("rojo", lambda d: _not_empty_fail(d) and ("rojo" in _ans(d) or "beh" in _ans(d))),
    ("mama", lambda d: _not_empty_fail(d) and ("mama" in _ans(d) or "uma" in _ans(d))),
    ("casa", lambda d: _not_empty_fail(d) and _not_meta_gloss(d)),
    ("arbol", lambda d: _not_empty_fail(d) and ("arbol" in _ans(d) or "kwet" in _ans(d))),
    ("hermano", lambda d: _not_empty_fail(d) and "hermano" in _ans(d)),
    ("abuela", lambda d: _not_empty_fail(d) and "abuel" in _ans(d)),
    ("padre", lambda d: _not_empty_fail(d) and "padre" in _ans(d)),
    # Variantes de pregunta
    ("como se dice agua", lambda d: "escribe" not in _ans(d) and _not_empty_fail(d) and ("agua" in _ans(d) or "yu'" in _ans(d))),
    ("que significa agua", lambda d: _not_empty_fail(d) and "agua" in _ans(d)),
    ("que significa sol", lambda d: _not_empty_fail(d) and "sek" in _ans(d) and _ans(d).find("sek") < 200),
    ("que es perro", lambda d: _not_empty_fail(d) and "perro" in _ans(d)),
    ("significado de casa", lambda d: _not_empty_fail(d) and "casa" in _ans(d)),
    ("traduce hola a nasa yuwe", lambda d: _not_empty_fail(d) and ("hola" in _ans(d) or "ewcha" in _ans(d) or "ma'g" in _ans(d))),
    ("traduce gracias", lambda d: _not_empty_fail(d) and ("agradec" in _ans(d) or "wecha" in _ans(d) or "gracias" in _ans(d))),
    ("explicame la palabra agua", lambda d: _not_empty_fail(d) and "agua" in _ans(d)),
    ("como se dice mi mama", lambda d: _not_empty_fail(d) and ("mama" in _ans(d) or "uma" in _ans(d))),
    ("palabra agua", lambda d: _not_empty_fail(d) and "agua" in _ans(d)),
    # Typo / sin tilde
    ("montana", lambda d: _not_empty_fail(d) and ("monta" in _ans(d) or "vits" in _ans(d))),
    ("numeros", lambda d: _not_empty_fail(d) and ("numer" in _ans(d) or "uno" in _ans(d) or "tee" in _ans(d))),
    ("colores", lambda d: _not_empty_fail(d) and "color" in _ans(d)),
    ("tres", lambda d: _not_empty_fail(d) and ("tres" in _ans(d) or "tekh" in _ans(d))),
    ("diez", lambda d: _not_empty_fail(d) and ("diez" in _ans(d) or "kseba" in _ans(d))),
    ("azul", lambda d: _not_empty_fail(d) and ("azul" in _ans(d) or "çem" in _ans(d) or "cem" in _ans(d))),
    ("pajaro", lambda d: _not_empty_fail(d) and ("pajaro" in _ans(d) or "pájaro" in (d.get("answer") or "").lower())),
    # Frases cortas / conversacion
    ("me llamo ana", lambda d: _not_empty_fail(d)),
    ("quiero practicar saludos", lambda d: "salud" in _ans(d)),
    ("cuantos colores hay", lambda d: "color" in _ans(d)),
    ("adios", lambda d: "desped" in _ans(d) or "wecha" in _ans(d)),
    ("nos vemos", lambda d: "desped" in _ans(d) or "gusto" in _ans(d)),
    ("muchas gracias avi", lambda d: "de nada" in _ans(d)),
    ("como digo gracias en clase", lambda d: "agradec" in _ans(d)),
    # Ayuda y errores
    ("ayuda", lambda d: "puedes escribirme" in _ans(d) or "palabra" in _ans(d)),
    ("no entiendo", lambda d: "paso a paso" in _ans(d) or "ejemplos" in _ans(d)),
    ("quien eres", lambda d: "avi" in _ans(d) and "nasa yuwe" in _ans(d)),
    ("xyzabc", lambda d: "no encontré" in _ans(d) and "cuarenta" not in _ans(d)),
    ("ayudame", lambda d: _no_generic_summary(d) and ("ayudo" in _ans(d) or "palabra" in _ans(d))),
    # Comida / naturaleza
    ("maiz", lambda d: _not_empty_fail(d) and "maiz" in _ans(d)),
    ("cuy", lambda d: _not_empty_fail(d) and "cuy" in _ans(d)),
    ("frio", lambda d: _not_empty_fail(d) and ("frio" in _ans(d) or "frío" in (d.get("answer") or "").lower())),
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
