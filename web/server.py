import csv
import json
import math
import os
import random
import re
import secrets
from avi_db import USE_POSTGRES, connect_auth, insert_returning_id, scalar_from_row
import solo_images_bootstrap
import firebase_storage_urls
import threading
import time
import hashlib
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlparse


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
FRONTEND_DIST_DIR = BASE_DIR / "frontend" / "dist"
_CORPUS_UNDER_REPO = BASE_DIR.parent / "corpus" / "data" / "corpus_bilingue_v5.csv"
_CORPUS_SIBLING = BASE_DIR.parent.parent / "corpus" / "data" / "corpus_bilingue_v5.csv"
_CORPUS_ENV = os.environ.get("AVI_CORPUS_PATH", "").strip()
if _CORPUS_ENV:
    CORPUS_PATH = Path(_CORPUS_ENV)
else:
    CORPUS_PATH = _CORPUS_UNDER_REPO if _CORPUS_UNDER_REPO.exists() else _CORPUS_SIBLING
MODEL_PATH = BASE_DIR / "models" / "retrieval_model_v1.json"

_SOLO_IMG_UNDER_REPO = BASE_DIR.parent / "corpus" / "generadas-img-ia-solo"
_SOLO_IMG_ENV = os.environ.get("AVI_SOLO_IMG_DIR", "").strip()
SOLO_IMG_DIR = Path(_SOLO_IMG_ENV) if _SOLO_IMG_ENV else _SOLO_IMG_UNDER_REPO
TERM_IMAGE_ROUTES_PATH = SOLO_IMG_DIR / "term_image_routes.json"
_SOLO_IMAGE_INDEX_LOCK = threading.Lock()
_SOLO_IMAGE_INDEX: tuple[dict[str, str], dict[str, str]] | None = None


def _listen_port() -> int:
    raw = (os.environ.get("PORT") or "").strip()
    if not raw:
        return 8090
    try:
        return int(raw)
    except ValueError:
        return 8090


HOST = "0.0.0.0"
# Render / Fly / Railway inyectan PORT; localmente 8090 si no está definido.
PORT = _listen_port()
AUTH_DB_PATH = BASE_DIR / "data" / "avi_auth.db"
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "").strip()
SESSION_TTL_SEC = 60 * 60 * 24 * 14  # vida máxima de la sesión
SESSION_IDLE_SEC = 60 * 30  # renueva tiempo de vida con cada petición autorizada (inactividad)
REGISTER_ROLES = frozenset({"estudiante", "docente"})
AUTH_ROLES = frozenset({"estudiante", "docente", "administrador"})

# Demo: se crean en la DB al arrancar si no existen. Producción: AVI_SKIP_DEMO_USERS=1
DEMO_LOGIN_PASSWORD = "AviDemo2026!"
DEMO_ACCOUNTS = (
    ("estudiante.demo@nasayuwe.local", "María", "estudiante"),
    ("docente.demo@nasayuwe.local", "Docente Demo", "docente"),
    ("admin.demo@nasayuwe.local", "Administrador Demo", "administrador"),
)

# Tres docentes con datos de panel (grupos, alumnos, actividades, asignaciones). Misma contraseña fuerte.
DEMO_TEACHER_PANEL_PASSWORD = "YuweDocente2026!"
DEMO_TEACHER_PANEL_ACCOUNTS = (
    ("docente.ana@nasayuwe.local", "Ana López", "docente"),
    ("docente.carlos@nasayuwe.local", "Carlos Becerra", "docente"),
    ("docente.lucia@nasayuwe.local", "Lucía Tunque", "docente"),
)
# Alumnos dedicados (cada uno solo en un grupo); contraseña = DEMO_LOGIN_PASSWORD
DEMO_PANEL_STUDENTS = (
    ("alumno.panel01@nasayuwe.local", "Panel Alumno 01"),
    ("alumno.panel02@nasayuwe.local", "Panel Alumno 02"),
    ("alumno.panel03@nasayuwe.local", "Panel Alumno 03"),
    ("alumno.panel04@nasayuwe.local", "Panel Alumno 04"),
    ("alumno.panel05@nasayuwe.local", "Panel Alumno 05"),
    ("alumno.panel06@nasayuwe.local", "Panel Alumno 06"),
    ("alumno.panel07@nasayuwe.local", "Panel Alumno 07"),
    ("alumno.panel08@nasayuwe.local", "Panel Alumno 08"),
    ("alumno.panel09@nasayuwe.local", "Panel Alumno 09"),
    ("alumno.panel10@nasayuwe.local", "Panel Alumno 10"),
    ("alumno.panel11@nasayuwe.local", "Panel Alumno 11"),
    ("alumno.panel12@nasayuwe.local", "Panel Alumno 12"),
)

TEACHER_PANEL_SEED_DESC_MARKER = "Datos semilla AVI — panel docente relleno."

# CORS: AVI_CORS_ORIGINS=lista separada por comas (p. ej. http://127.0.0.1:5173). Vacío = "*" (solo desarrollo).
_CORS_RAW = os.environ.get("AVI_CORS_ORIGINS", "").strip()
CORS_ALLOWED_ORIGINS = frozenset(o.strip() for o in _CORS_RAW.split(",") if o.strip()) if _CORS_RAW else None
# Rate limit peticiones sensibles de auth por IP (login, registro, recuperación).
AUTH_RL_MAX = max(1, int(os.environ.get("AVI_AUTH_RATE_MAX", "50")))
AUTH_RL_WINDOW_SEC = max(60.0, float(os.environ.get("AVI_AUTH_RATE_WINDOW_SEC", "900")))
_AUTH_RL_LOCK = threading.Lock()
_AUTH_RL_BUCKETS: dict[str, list[float]] = {}

_AUTH_DB_LOCK = threading.Lock()
IMAGE_CACHE = {}
IMAGE_CACHE_TTL_SEC = int(os.environ.get("AVI_IMAGE_CACHE_TTL_SEC", "21600"))  # 6 h; evita imagenes incorrectas cacheadas para siempre


def _image_cache_get(key: str):
    ent = IMAGE_CACHE.get(key)
    if not ent:
        return None
    ts, payload = ent
    if time.time() - ts > IMAGE_CACHE_TTL_SEC:
        IMAGE_CACHE.pop(key, None)
        return None
    return payload


def _image_cache_set(key: str, payload: dict) -> None:
    IMAGE_CACHE[key] = (time.time(), payload)


IMAGE_STOPWORDS = {
    "de",
    "la",
    "el",
    "los",
    "las",
    "un",
    "una",
    "en",
    "y",
    "con",
    "para",
}


def normalize_text(text: str) -> str:
    text = (text or "").lower().strip()
    text = text.replace("’", "'").replace("`", "'").replace("´", "'")
    text = re.sub(r"[^a-zA-Z0-9áéíóúüñçëïä'\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str):
    return [t for t in normalize_text(text).split(" ") if t]


def _get_solo_image_index() -> tuple[dict[str, str], dict[str, str]]:
    """(by_id, by_lex_key) rutas relativas PNG bajo corpus/generadas-img-ia-solo."""
    global _SOLO_IMAGE_INDEX
    with _SOLO_IMAGE_INDEX_LOCK:
        if _SOLO_IMAGE_INDEX is not None:
            return _SOLO_IMAGE_INDEX
        by_id: dict[str, str] = {}
        by_lex: dict[str, str] = {}
        legacy = SOLO_IMG_DIR / "term_image_map.json"
        try:
            if TERM_IMAGE_ROUTES_PATH.is_file():
                raw = json.loads(TERM_IMAGE_ROUTES_PATH.read_text(encoding="utf-8"))
                if isinstance(raw, dict):
                    bid = raw.get("by_id")
                    blk = raw.get("by_lex_key")
                    if isinstance(bid, dict):
                        by_id = {str(k).strip(): str(v).strip().replace("\\", "/") for k, v in bid.items() if k and v}
                    if isinstance(blk, dict):
                        by_lex = {str(k).strip(): str(v).strip().replace("\\", "/") for k, v in blk.items() if k and v}
            elif legacy.is_file():
                raw = json.loads(legacy.read_text(encoding="utf-8"))
                if isinstance(raw, dict) and "by_id" not in raw:
                    by_lex = {str(k).strip(): str(v).strip().replace("\\", "/") for k, v in raw.items() if k and v}
        except (OSError, json.JSONDecodeError, TypeError):
            pass
        _SOLO_IMAGE_INDEX = (by_id, by_lex)
        return _SOLO_IMAGE_INDEX


def _local_solo_image_payload(query: str, category: str, term_id: str = "") -> dict | None:
    """Si existe PNG local para el termino, devuelve dict compatible con fetch_commons_image."""
    by_id, by_lex = _get_solo_image_index()
    rel = ""
    tid = (term_id or "").strip()
    if tid and tid in by_id:
        rel = by_id[tid]
    if not rel:
        k = f"{normalize_text(query or '')}|{normalize_text(category or '')}"
        rel = by_lex.get(k, "")
    if not rel:
        return None
    fb = firebase_storage_urls.firebase_corpus_image_url(rel)
    if fb:
        return {
            "ok": True,
            "query": normalize_text(query or ""),
            "image_url": fb,
            "thumb_url": fb,
            "source_url": "",
            "license": "ilustracion corpus YuweAI (generada)",
            "author": "corpus generadas-img-ia-solo",
            "source": "firebase_storage",
        }
    try:
        p = (SOLO_IMG_DIR / rel).resolve()
        root = SOLO_IMG_DIR.resolve()
    except OSError:
        return None
    if not str(p).startswith(str(root)) or not p.is_file():
        return None
    if p.suffix.lower() != ".png":
        return None
    url = f"/api/corpus-img/{rel}"
    return {
        "ok": True,
        "query": normalize_text(query or ""),
        "image_url": url,
        "thumb_url": url,
        "source_url": "",
        "license": "ilustracion corpus YuweAI (generada)",
        "author": "corpus generadas-img-ia-solo",
        "source": "corpus_solo",
    }


def _term_local_image_url(term_id: str = "", query: str = "", category: str = "") -> str | None:
    """URL relativa /api/corpus-img/... si el termino tiene PNG en generadas-img-ia-solo."""
    by_id, by_lex = _get_solo_image_index()
    rel = ""
    tid = (term_id or "").strip()
    if tid and tid in by_id:
        rel = by_id[tid]
    if not rel:
        k = f"{normalize_text(query or '')}|{normalize_text(category or '')}"
        rel = by_lex.get(k, "")
    if not rel:
        return None
    rel = str(rel).strip().replace("\\", "/").lstrip("/")
    if not firebase_storage_urls.is_safe_corpus_rel_path(rel):
        return None
    fb = firebase_storage_urls.firebase_corpus_image_url(rel)
    if fb:
        return fb
    try:
        p = (SOLO_IMG_DIR / rel).resolve()
        root = SOLO_IMG_DIR.resolve()
    except OSError:
        return None
    if not str(p).startswith(str(root)) or not p.is_file():
        return None
    return f"/api/corpus-img/{rel}"


def _attach_term_image(term: dict) -> dict:
    """Copia del termino con image_url cuando hay ilustracion local."""
    out = dict(term)
    url = _term_local_image_url(
        str(out.get("id") or ""),
        str(out.get("espanol") or ""),
        str(out.get("categoria") or ""),
    )
    if url:
        out["image_url"] = url
    return out


def _lexicon_ny_index(lex_rows: list) -> dict[str, dict]:
    """Indice normalize(nasa_yuwe) -> fila lexica (primera aparicion)."""
    idx: dict[str, dict] = {}
    for row in lex_rows:
        k = normalize_text((row.get("nasa_yuwe") or "").strip())
        if k and k not in idx:
            idx[k] = row
    return idx


def _option_images_for_nasa_options(
    options: list[str], ny_index: dict[str, dict], cat_norm: str
) -> dict[str, str]:
    """Mapa texto opcion (Nasa) -> /api/corpus-img/... solo ilustraciones locales."""
    out: dict[str, str] = {}
    for ny in options or []:
        s = (ny or "").strip()
        if not s:
            continue
        row = ny_index.get(normalize_text(s))
        if not row:
            continue
        url = _term_local_image_url(
            str(row.get("id") or ""),
            str(row.get("espanol") or ""),
            str(row.get("categoria") or cat_norm),
        )
        if url:
            out[s] = url
    return out


def _lev_distance(a: str, b: str) -> int:
    """Distancia Levenshtein (sugerencias sin dependencias)."""
    if len(a) < len(b):
        a, b = b, a
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a):
        cur = [i + 1]
        for j, cb in enumerate(b):
            ins, del_, sub = cur[j] + 1, prev[j + 1] + 1, prev[j] + (ca != cb)
            cur.append(min(ins, del_, sub))
        prev = cur
    return prev[-1]


# Combinan varias categorias del CSV bajo un slug de UI (mas terminos en pantalla).
# Claves y valores deben coincidir con normalize_text(categoria) usado en by_category.
VIRTUAL_CATEGORIES = {
    "comida": ("alimentos", normalize_text("frutas_verduras")),
}

# Palabras frecuentes en espanol (vocab por tema)
ESP_STOP_QUERY = {
    "el", "la", "los", "las", "un", "una", "unos", "unas", "de", "y", "del", "al", "a", "en", "lo", "o",
    "le", "les", "con", "por", "para", "se", "su", "sus", "al", "como", "más", "mas",
}

# Preguntas al chat AVI: quitar marcadores para quedarse con la palabra/frase buscada.
CHAT_QUERY_STOP = ESP_STOP_QUERY | {
    "que", "cual", "cuales", "digo", "dice", "decir", "significa", "significado", "es", "son",
    "esta", "este", "esto", "hay", "tiene", "explicame", "explica", "traduce", "traduccion",
    "busca", "buscar", "pregunta", "pregunto", "avi", "yuwe", "nasa", "quiero", "hablar",
    "sobre", "dame", "dime", "ayuda", "ayudame", "favor", "aprender", "aprendizaje",
    "practicar", "estudiar", "palabra", "frase", "me", "te", "mi", "tu", "nos", "les",
    "cuantos", "cuantas", "muchos", "muchas", "todo", "toda", "todos", "todas", "asi",
    "hoy", "ahora", "bien", "muy", "tan", "tambien", "llamo", "nombre", "cuenta", "cifra",
    "entiendo", "entender", "funciona", "puedo", "preguntar",
}

# Palabras funcionales -> terminos del corpus (glosa o forma).
_LEXICAL_ALIASES: dict[str, tuple[str, ...]] = {
    "gracias": ("agradecer", "agradecido", "wecha"),
    "adios": ("despedir", "despedida", "wecha"),
    "hola": ("saludo", "hola", "ewcha", "fxi'z"),
    "buenos dias": ("saludo", "buenos dias", "fxi'z"),
    "buenas tardes": ("saludo", "buenas tardes"),
    "buenas noches": ("saludo", "buenas noches"),
}

# Parentesco: priorizar lexico concreto (mama, hermano…) frente al tema familia generico.
_FAMILY_LEXICON_HINTS = re.compile(
    r"\b(mama|mamá|papa|papá|padre|madre|hermano|hermana|abuelo|abuela|hijo|hija|tio|tía|tia|primo|prima|esposo|esposa)\b"
)

NUMERO_EN_PALABRA = {
    "cero": "0", "uno": "1", "dos": "2", "tres": "3", "cuatro": "4", "cinco": "5", "seis": "6",
    "siete": "7", "ocho": "8", "nueve": "9", "diez": "10", "once": "11", "doce": "12",
    "veinte": "20", "cien": "100", "mil": "1000",
}

COLOR_ES_A_EN = {
    "rojo": "red", "azul": "blue", "verde": "green", "amarillo": "yellow", "blanco": "white",
    "negro": "black", "naranja": "orange", "violeta": "violet", "morado": "purple", "gris": "gray",
    "cafe": "brown", "café": "brown", "marron": "brown", "marrón": "brown", "rosa": "pink",
    "dorado": "gold", "plateado": "silver",
}

# Cielo / cuerpos celestes (evita homonimos tipo "Diana Luna" en deportes)
CELESTE_ES_A_EN = {
    "luna": "moon",
    "sol": "sun",
    "estrella": "star",
    "cielo": "sky",
    "nube": "cloud",
}

# Verbos / palabras muy ambiguas en Commons (toponimos, museos): busqueda en ingles concretada.
ES_LEX_IMAGE_SEARCH = {
    "correr": "running person athletics",
    "caminar": "walking people street",
    "saltar": "jumping person outdoors",
    "nadar": "swimming person pool",
    "bailar": "folk dance traditional",
    "cantar": "singer choir singing",
    "dormir": "sleeping child peaceful",
    "comer": "eating meal table family",
    "beber": "drinking water glass",
}
# Ayuda a Commons: titulos en ingles; la coincidencia con el token en espanol es debil
ALIMENTO_ES_A_EN = {
    "ajo": "garlic", "arroz": "rice", "leche": "milk", "agua": "water", "pan": "bread", "manzana": "apple",
    "platano": "banana", "plátano": "banana", "tomate": "tomato", "cebolla": "onion", "carne": "meat",
    "pescado": "fish", "huevo": "egg", "queso": "cheese", "cafe": "coffee", "café": "coffee", "miel": "honey",
    "sal": "salt", "azucar": "sugar", "azúcar": "sugar", "pollo": "chicken", "mantequilla": "butter",
    "frijol": "beans", "frijoles": "beans", "yuca": "yuca", "naranja": "orange", "frutas": "fruit",
    "limon": "lemon", "limón": "lemon", "uva": "grape", "sandia": "watermelon", "sandía": "watermelon", "pera": "pear",
    "aceite": "cooking oil", "maiz": "corn", "maíz": "corn", "cacao": "cocoa", "canela": "cinnamon", "cordero": "lamb", "chocolate": "chocolate",
    "mazorca": "corn", "arveja": "pea", "arvejas": "peas",
    "zapallo": "squash", "calabaza": "squash", "papa": "potato", "patata": "potato",
    "arracacha": "arracacha", "guama": "inga edulis guama fruit", "choclo": "corn on the cob", "chicha": "fermented corn drink",
    "quinua": "quinoa", "quinoa": "quinoa", "camote": "sweet potato", "batata": "sweet potato",
    "remolacha": "beet", "zanahoria": "carrot", "apio": "celery", "espinaca": "spinach",
    "coliflor": "cauliflower", "brocoli": "broccoli", "brócoli": "broccoli", "repollo": "cabbage",
    "aji": "chili pepper", "ají": "chili pepper",
}

ANIMAL_ES_A_EN = {
    "gato": "cat", "perro": "dog", "pez": "fish", "vaca": "cow", "caballo": "horse", "oso": "bear", "leon": "lion", "león": "lion",
    "pajaro": "bird", "pájaro": "bird", "oveja": "sheep", "cerdo": "pig", "rana": "frog", "serpiente": "snake", "pato": "duck",
    "gallina": "chicken", "gallo": "rooster", "tortuga": "turtle", "conejo": "rabbit", "cabra": "goat", "elefante": "elephant",
    "mariposa": "butterfly",
}


def _core_phrase_for_image(q: str) -> str:
    """Quita Articulos y deja 2–5 palabras con significado para buscar en Commons."""
    toks = [t for t in tokenize(q) if t not in ESP_STOP_QUERY]
    if not toks:
        toks = [t for t in tokenize(q) if t]
    return " ".join(toks[:5])


def _image_cat_hint_ui(cat: str) -> str:
    c = normalize_text(cat)
    if c == "comida" or c == normalize_text("frutas_verduras"):
        return "alimentos"
    if c in ("diccionario_general", "vocabulario_general"):
        return "general"
    return c or "general"


def _gloss_lookup(token: str):
    """Primer token normalizado -> (tipo, valor_en_o_digito)."""
    k = normalize_text(token)
    if k in NUMERO_EN_PALABRA:
        return "num", NUMERO_EN_PALABRA[k]
    if k in COLOR_ES_A_EN:
        return "color", COLOR_ES_A_EN[k]
    if k in CELESTE_ES_A_EN:
        return "celest", CELESTE_ES_A_EN[k]
    if k in ALIMENTO_ES_A_EN:
        return "food", ALIMENTO_ES_A_EN[k]
    if k in ANIMAL_ES_A_EN:
        return "animal", ANIMAL_ES_A_EN[k]
    return None, None


def fetch_commons_image(query: str, category: str = "", term_id: str = ""):
    """
    Imagen del termino: primero PNG local (`generadas-img-ia-solo` + term_image_routes.json),
    si no hay, Wikimedia Commons con busqueda guiada por tema.
    """
    core = _core_phrase_for_image(query or "")
    q = normalize_text(core) or normalize_text(query or "")
    cat = normalize_text(category)
    tid = (term_id or "").strip()
    cache_key = f"{q}|{cat}|{tid}"
    hit = _image_cache_get(cache_key)
    if hit is not None:
        return hit

    loc = _local_solo_image_payload(query or "", category or "", tid)
    if loc is not None:
        _image_cache_set(cache_key, loc)
        return loc

    if not q:
        r = {"ok": False, "message": "query vacia"}
        _image_cache_set(cache_key, r)
        return r

    cat_hint = _image_cat_hint_ui(category)
    toks = tokenize(q)
    first = normalize_text(toks[0]) if toks else ""

    gkind, gval = _gloss_lookup(first)
    if gkind == "num":
        search_q = f"{gval} number"
    elif gkind == "color":
        search_q = f"{gval} color"
    elif gkind == "celest":
        search_q = f"{gval} natural sky"
    elif gkind == "food":
        gv = str(gval)
        gvn = normalize_text(gv)
        if gvn in ("pea", "peas"):
            search_q = "pea pisum sativum vegetable plant"
        elif first == "arracacha":
            search_q = "arracacha xanthorrhiza"
        elif " " in gv or len(gv) > 14:
            search_q = gv
        else:
            search_q = f"{gv} food"
    elif gkind == "animal":
        search_q = f"{gval} animal"
    else:
        # Léxico del corpus sin entrada en glosarios: búsqueda por texto en español.
        search_q = (core or q).strip()
        if len(search_q) < 2:
            r = {"ok": False, "message": "sin texto para buscar imagen"}
            _image_cache_set(cache_key, r)
            return r
        if first in ES_LEX_IMAGE_SEARCH:
            search_q = f"{ES_LEX_IMAGE_SEARCH[first]} photo"
        else:
            search_q = f"{search_q} photo"

    api_url = (
        "https://commons.wikimedia.org/w/api.php"
        "?action=query"
        "&format=json"
        "&generator=search"
        "&gsrnamespace=6"
        f"&gsrsearch={quote(search_q)}"
        "&gsrlimit=40"
        "&prop=imageinfo"
        "&iiprop=url|extmetadata|size"
        "&iiurlwidth=640"
        "&origin=*"
    )
    req = urllib.request.Request(
        api_url,
        headers={"User-Agent": "AVI-NasaYuwe/1.0 (educational project; educational image search)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=7) as resp:
            raw = json.loads(resp.read().decode("utf-8", errors="ignore"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        result = {"ok": False, "message": "sin imagen externa disponible"}
        _image_cache_set(cache_key, result)
        return result

    pages = (raw.get("query") or {}).get("pages") or {}
    _lk, gloss_val = _gloss_lookup(first)
    gloss_en_first = str(gloss_val).split()[0] if gloss_val else ""

    q_tokens = [t for t in toks if t not in IMAGE_STOPWORDS and t not in ESP_STOP_QUERY]
    en_extra = set()
    for w in toks:
        wn = normalize_text(w)
        if wn in ALIMENTO_ES_A_EN:
            for p in str(ALIMENTO_ES_A_EN[wn]).split():
                en_extra.add(normalize_text(p))
        if wn in ANIMAL_ES_A_EN:
            for p in str(ANIMAL_ES_A_EN[wn]).split():
                en_extra.add(normalize_text(p))
        if wn in COLOR_ES_A_EN:
            en_extra.add(normalize_text(COLOR_ES_A_EN[wn]))
        if wn in CELESTE_ES_A_EN:
            en_extra.add(normalize_text(CELESTE_ES_A_EN[wn]))
    match_tokens = set(q_tokens) | en_extra
    if first in ES_LEX_IMAGE_SEARCH:
        for w in tokenize(normalize_text(ES_LEX_IMAGE_SEARCH[first])):
            if len(w) > 2 and w not in IMAGE_STOPWORDS and w not in ESP_STOP_QUERY:
                match_tokens.add(w)

    banned_title = {
        "logo", "icon", "symbol", "flag", "map", "escudo", "vector", "svg", "diagram", "chart",
        "coa", "coat", "arms", "fountain", "pennon", "route", "highway", "location", "crystal",
        "document", "manuscript", "parchment", "scroll", "letter", "facsimile", "monument",
        "newspaper", "journal", "gazette", "typeset", "typesetting", "pressroom", "factory",
        "workshop", "assembly", "congress", "parliament", "soldiers", "battlefield", "portrait",
        "yearbook", "classroom", "students", "crowd", "album", "bookcover", "scan",
    }
    harmful_title_sub = (
        "newspaper", "journal", "gazette", "typeset", "facsimile", "manuscript", "parchment",
        "pressroom", "factory", "workers", "workshop", "assembly line", "congress", "parliament",
        "soldiers", "battlefield", "portrait of", "team photo", "classroom", "students",
        "crowd at", "album cover", "book cover", "scan of", "typesetting", "canning", "jstor",
        "ambigram",
    )
    if gkind in ("food", "animal"):
        min_score_strict = 5
    elif gkind in ("color", "num", "celest"):
        min_score_strict = 4
    else:
        min_score_strict = 3

    def _gloss_needles_ok(loose: bool, title_norm: str, needles: set[str]) -> bool:
        if not needles:
            return True
        strict_ok = any(len(n) >= 2 and n in title_norm for n in needles)
        if strict_ok:
            return True
        if not loose:
            return False
        if first and first in title_norm:
            return True
        return any(len(n) >= 3 and n in title_norm for n in needles)

    def build_ranked(skip_harmful_substrings: bool, loose_gloss_needles: bool) -> list[tuple[int, dict]]:
        ranked_local: list[tuple[int, dict]] = []
        for page in pages.values():
            infos = page.get("imageinfo") or []
            if not infos:
                continue
            info = infos[0]
            title_raw = page.get("title", "")
            title = title_raw.replace("File:", "")
            if ".pdf" in title_raw.lower():
                continue
            tl = title_raw.lower()
            if tl.endswith(".gif") or tl.endswith(".svg"):
                continue
            title_norm = normalize_text(title)
            title_tokens = set(tokenize(title_norm))
            if title_tokens & banned_title:
                continue
            if not skip_harmful_substrings and any(h in title_norm for h in harmful_title_sub):
                continue
            if int(info.get("width", 0) or 0) < 200 or int(info.get("height", 0) or 0) < 200:
                continue

            if gkind == "food" and gval:
                needles = {first} | {normalize_text(x) for x in str(gval).split() if len(normalize_text(x)) >= 2}
                needles.discard("")
                if needles and not _gloss_needles_ok(loose_gloss_needles, title_norm, needles):
                    continue
            if gkind == "animal" and gval:
                needles = {first} | {normalize_text(x) for x in str(gval).split() if len(normalize_text(x)) >= 2}
                needles.discard("")
                if needles and not _gloss_needles_ok(loose_gloss_needles, title_norm, needles):
                    continue
            if gkind == "color" and gval:
                needles = {first} | {normalize_text(x) for x in str(gval).split() if len(normalize_text(x)) >= 2}
                needles.discard("")
                if needles and not _gloss_needles_ok(loose_gloss_needles, title_norm, needles):
                    continue
            if gkind == "celest" and gval:
                needles = {first} | {normalize_text(x) for x in str(gval).split() if len(normalize_text(x)) >= 2}
                needles.discard("")
                if needles and not _gloss_needles_ok(loose_gloss_needles, title_norm, needles):
                    continue

            overlap = len(match_tokens & title_tokens)
            en_overlap = 0
            for w in toks:
                wn = normalize_text(w)
                for enp in (
                    ALIMENTO_ES_A_EN.get(wn),
                    ANIMAL_ES_A_EN.get(wn),
                    COLOR_ES_A_EN.get(wn),
                    CELESTE_ES_A_EN.get(wn),
                ):
                    if enp and str(enp):
                        en_full = normalize_text(str(enp))
                        if en_full in title_norm:
                            en_overlap += 2
                        else:
                            for part in en_full.split():
                                if len(part) > 2 and part in title_norm:
                                    en_overlap += 1
                                    break
            exact_bonus = 0
            if first and first in title_tokens:
                exact_bonus = 4
            elif first and len(first) >= 5 and first in title_norm:
                exact_bonus = 2
            if gloss_en_first and len(gloss_en_first) > 2 and gloss_en_first in title_norm:
                exact_bonus = max(exact_bonus, 5)

            score = overlap * 2 + en_overlap + exact_bonus
            if cat_hint == "colores" and ("color" in title_tokens or "colour" in title_tokens):
                score += 1
            if (cat_hint == "animales" or first in ANIMAL_ES_A_EN) and "animal" in title_tokens:
                score += 1
            if (cat_hint == "alimentos" or first in ALIMENTO_ES_A_EN) and "food" in title_tokens:
                score += 1

            meta = info.get("extmetadata") or {}
            candidate = {
                "ok": True,
                "query": q,
                "title": title,
                "image_url": info.get("thumburl") or info.get("url"),
                "source_url": info.get("descriptionurl"),
                "license": (meta.get("LicenseShortName") or {}).get("value", "desconocida"),
                "author": (meta.get("Artist") or {}).get("value", "desconocido"),
            }
            if gkind is None:
                has_anchor = (
                    (first and len(first) >= 3 and first in title_tokens)
                    or overlap > 0
                    or en_overlap > 0
                    or exact_bonus >= 4
                )
                if not has_anchor:
                    continue
            if score < 1 and (q_tokens and overlap == 0 and en_overlap == 0) and gkind is not None:
                continue
            ranked_local.append((score, candidate))
        ranked_local.sort(key=lambda x: x[0], reverse=True)
        return ranked_local

    # Paso 1: estricto. Paso 2: sin subtitulos dañinos. Paso 3: solo gloss (comida/animal/color/cielo):
    # relaja agujas y umbral; no aplica a lexico general (evita "correr" -> Museo Correr).
    if gkind is None:
        passes = (
            (False, False, min_score_strict),
            (True, False, max(2, min_score_strict - 1)),
        )
    else:
        passes = (
            (False, False, min_score_strict),
            (True, False, max(3, min_score_strict - 2)),
            (True, True, 2),
        )
    for skip_harm, loose_needles, min_take in passes:
        ranked = build_ranked(skip_harm, loose_needles)
        if ranked and ranked[0][0] >= min_take:
            result = ranked[0][1]
            _image_cache_set(cache_key, result)
            return result

    result = {"ok": False, "message": "no se encontro imagen adecuada"}
    _image_cache_set(cache_key, result)
    return result


def _chat_pick_variant(query_norm: str, options: tuple[str, ...]) -> str:
    if not options:
        return ""
    i = sum(ord(c) for c in query_norm) % len(options)
    return options[i]


def _looks_like_meta_spanish_gloss(es: str) -> bool:
    """Preguntas tipo 'como se dice X' en la ficha espanola (no sirven como etiqueta al usuario)."""
    n = normalize_text(es or "")
    return "como se dice" in n or n.startswith("traduce ") or "traduccion" in n


def _is_asking_how(query_norm: str) -> bool:
    return bool(
        re.search(
            r"\bcomo\s+(digo|se\s+dice|saludo|pregunto|me\s+despido|presento|presentarme)\b",
            query_norm,
        )
        or re.search(r"\b(explicame|explica|que\s+significa)\b", query_norm)
        or "traduce" in query_norm
        or "traduccion" in query_norm
    )


def _is_thanking_avi(query_norm: str, q_tokens: list[str]) -> bool:
    """Gracias al AVI, no 'como digo gracias'."""
    if _is_asking_how(query_norm):
        return False
    ts = set(q_tokens)
    if "gracias" not in query_norm and "agradec" not in query_norm:
        return False
    if {"como", "digo", "dice", "decir", "traduce", "traduccion", "significa", "explicame", "explica"} & ts:
        return False
    return True


def _content_tokens_from_query(q_tokens: list[str]) -> list[str]:
    return [t for t in q_tokens if t not in CHAT_QUERY_STOP and len(t) >= 2]


def _clean_lexical_target(term: str) -> str:
    t = normalize_text(term or "")
    t = re.sub(r"^(mi|tu|su|mis|tus|sus|el|la|los|las)\s+", "", t).strip()
    t = re.sub(r"^(la|el)\s+palabra\s+", "", t).strip()
    return t


def _gloss_match_rank(prefer: str, es_norm: str) -> int:
    """0 = glosa exacta; valores mayores = coincidencia mas debil."""
    if not prefer:
        return 9
    if es_norm == prefer:
        return 0
    parts = es_norm.split()
    if parts and parts[0] == prefer and len(parts) == 1:
        return 1
    if parts and parts[0] == prefer:
        return 2
    if prefer in parts:
        return 3
    if prefer in es_norm and len(es_norm) <= len(prefer) + 12:
        return 4
    if prefer in es_norm:
        return 6
    return 9


def _dict_suggestion_acceptable(query_term: str, distance: int) -> bool:
    ql = normalize_text(query_term)
    if len(ql) < 3:
        return False
    max_d = 2 if len(ql) <= 5 else max(2, len(ql) // 3)
    return distance <= max_d


def _chat_help_guidance(query_norm: str, q_tokens: list[str]) -> str | None:
    ts = set(q_tokens)
    if query_norm in ("ayuda", "ayudame", "help", "auxilio") or (
        ts <= {"ayuda", "ayudame", "avi"} and ("ayuda" in ts or "ayudame" in ts)
    ):
        return (
            "Claro, te ayudo. Puedes escribirme de estas formas:\n\n"
            "• Una palabra en español: agua, luna, hermano, rojo…\n"
            "• «¿Cómo se dice … en Nasa Yuwe?» o «¿Qué significa …?»\n"
            "• Un tema: saludos, familia, números, colores, animales\n"
            "• Una frase corta: buenos días, me llamo Ana, gracias\n\n"
            "Prueba con la palabra que más te interese hoy."
        )
    if any(
        p in query_norm
        for p in (
            "no entiendo",
            "no comprendo",
            "no se que preguntar",
            "no sé que preguntar",
            "que puedo preguntar",
            "qué puedo preguntar",
            "como te uso",
            "cómo te uso",
        )
    ):
        return (
            "Vamos paso a paso. Elige una sola palabra o tema y yo te doy la forma en Nasa Yuwe.\n\n"
            "Ejemplos que funcionan muy bien: «agua», «Como saludo?», «perro», «quiero aprender numeros», "
            "«Como digo gracias?». Escríbeme una y seguimos desde ahí."
        )
    if query_norm in ("quien eres", "que eres", "qué eres", "que es avi", "qué es avi"):
        return (
            "Soy AVI, tu acompañante para practicar Nasa Yuwe con el material del curso. "
            "No invento palabras: te muestro formas del corpus y te guío para practicar en voz alta.\n\n"
            "Pregúntame una palabra o un tema y empezamos."
        )
    return None


def _token_looks_gibberish(word: str) -> bool:
    raw = re.sub(r"[^a-zA-Záéíóúüñ]", "", normalize_text(word))
    if len(raw) < 5:
        return False
    vowels = sum(1 for c in raw if c.lower() in "aeiouáéíóú")
    return vowels <= 1


def _query_looks_unsearchable(query_norm: str, q_tokens: list[str]) -> bool:
    content = _content_tokens_from_query(q_tokens)
    if len(content) == 1 and _token_looks_gibberish(content[0]):
        return True
    if content:
        return False
    raw = re.sub(r"[^a-zA-Záéíóúüñ]", "", query_norm)
    if len(raw) < 4:
        return False
    if raw in ("hola", "ey", "hey", "ei", "buenas"):
        return False
    # Cadenas largas sin vocales claras (xyzabc) o mezcla rara.
    vowels = sum(1 for c in raw if c.lower() in "aeiouáéíóú")
    if len(raw) >= 5 and vowels < max(2, len(raw) // 4):
        return True
    return len(raw) >= 7 and vowels == 0


def _lexico_doc_indices(rows: list[dict], term: str, *, limit: int = 14) -> list[int]:
    """Indices de filas lexico que coinciden con una glosa o forma (como dictionary_search)."""
    ql = normalize_text(term)
    if not ql or len(ql) < 2:
        return []
    matches: list[tuple[int, int]] = []
    for i, row in enumerate(rows):
        if row.get("record_type") != "lexico":
            continue
        es = row.get("espanol_norm") or ""
        ny = row.get("nasa_norm") or ""
        score = 0
        if ql == es or ql == ny:
            score = 100
        elif es == ql or ny == ql:
            score = 100
        elif ql in es or ql in ny:
            score = 80
        elif es.startswith(ql) or ny.startswith(ql):
            score = 70
        elif any(ql == part for part in es.split() if len(ql) >= 2):
            score = 65
        elif any(ql in part for part in es.split() if len(ql) >= 3):
            score = 55
        if score:
            rank = _gloss_match_rank(ql, es)
            matches.append((score, rank, len(es), i))
    matches.sort(key=lambda x: (x[1], -x[0], x[2]))
    out = [i for _, _, _, i in matches[:limit]]
    if not out and ql in _LEXICAL_ALIASES:
        seen: set[int] = set()
        for alias in _LEXICAL_ALIASES[ql]:
            for i in _lexico_doc_indices(rows, alias, limit=limit):
                if i not in seen:
                    seen.add(i)
                    out.append(i)
                if len(out) >= limit:
                    break
            if len(out) >= limit:
                break
    return out[:limit]


def _prioritize_chat_contexts(
    contexts: list[dict],
    *,
    direct_target: str = "",
    translation_intent: bool = False,
) -> list[dict]:
    if not contexts:
        return contexts
    dt = normalize_text(direct_target or "")

    def rank_key(ctx: dict) -> tuple[int, float]:
        rt = (ctx.get("record_type") or "").strip().lower()
        es = normalize_text(ctx.get("espanol") or "")
        ny = normalize_text(ctx.get("nasa_yuwe") or "")
        base = float(ctx.get("score") or 0)
        penalty = 0
        if rt == "qa":
            penalty += 80
        if _looks_like_meta_spanish_gloss(ctx.get("espanol") or ""):
            penalty += 60
        if rt == "dialogo" and (translation_intent or dt):
            penalty += 25
        if dt and rt == "lexico":
            gm = _gloss_match_rank(dt, es)
            penalty -= max(0, 280 - gm * 35)
            if ny == dt:
                penalty -= 40
        if translation_intent and rt == "lexico" and not _looks_like_meta_spanish_gloss(ctx.get("espanol") or ""):
            penalty -= 15
        return (penalty, -base)

    return sorted(contexts, key=rank_key)


def _extract_lexical_target(query_norm: str, q_tokens: list[str] | None = None) -> str | None:
    for pat in (
        r"(?:explicame|explica)\s+la\s+palabra\s+(.+?)(?:\?|$)",
        r"como\s+digo\s+(.+?)(?:\s+en\s+nasa|\?|$)",
        r"como\s+se\s+dice\s+(.+?)(?:\s+en\s+nasa|\?|$)",
        r"traduce\s+(.+?)(?:\s+a\s+nasa|\?|$)",
        r"traduccion\s+de\s+(.+?)(?:\?|$)",
        r"significado\s+de\s+(.+?)(?:\?|$)",
        r"que\s+significa\s+(.+?)(?:\?|$)",
        r"que\s+es\s+(.+?)(?:\s+en\s+nasa|\?|$)",
        r"(?:explicame|explica)\s+(?:esta\s+)?(?:palabra|frase)?\s*(.+?)(?:\?|$)",
        r"(?:busca|buscar)\s+(?:la\s+)?palabra\s+(.+?)(?:\?|$)",
    ):
        m = re.search(pat, query_norm)
        if m:
            t = _clean_lexical_target(m.group(1).strip(" ?."))
            if t and t not in ("esta frase", "esta palabra", "esta", "", "…", "..."):
                return t
    m_pal = re.search(r"^palabra\s+(.+?)\s*\??$", query_norm)
    if m_pal:
        t = _clean_lexical_target(m_pal.group(1))
        if t:
            return t
    if re.search(r"\bcomo\s+saludo\b", query_norm) or query_norm in ("saludo", "saludos"):
        return "saludo"
    if re.search(r"\bcomo\s+me\s+despido\b", query_norm) or query_norm in ("despedida", "despedidas"):
        return "despedida"
    tokens = q_tokens if q_tokens is not None else tokenize(query_norm)
    content = _content_tokens_from_query(tokens)
    if len(content) == 1:
        if content[0] in ("adios", "chao", "chau") and not _is_asking_how(query_norm):
            return None
        if content[0] == "gracias" and not _is_asking_how(query_norm):
            return None
        return content[0]
    if len(content) >= 2 and (
        _is_asking_how(query_norm)
        or "significa" in query_norm
        or "significado" in query_norm
        or query_norm.startswith("traduce ")
    ):
        joined = " ".join(content[-3:])
        return _clean_lexical_target(joined) or joined
    return None


_CHAT_TOPIC_REGEX: list[tuple[str, re.Pattern[str]]] = [
    (
        "familia",
        re.compile(
            r"\bfamilia\b|\bparentesco\b|\bcasa\b.*\bfamilia\b|"
            r"\bhablar\s+de\s+mi\s+familia\b"
        ),
    ),
    (
        "despedida",
        re.compile(
            r"\bdespid|\bdesped\b|\badios\b|\bhasta\s+luego\b|\bnos\s+vemos\b|"
            r"\bchao\b|\bchau\b|\bme\s+voy\b|\bcomo\s+me\s+despido\b|\bdespedidas?\b"
        ),
    ),
    ("gracias", re.compile(r"\bgracias\b|\bagradec")),
    (
        "saludos",
        re.compile(
            r"\bsaludo|\bcomo\s+saludo\b|\bpresentarme\b|\bpresentacion\b|"
            r"\bconocer\b|\bbuenos\s+dias\b|\bbuenas\s+tardes\b|\bbuenas\s+noches\b"
        ),
    ),
    ("numeros", re.compile(r"\bnumeros?\b|\bcontar\b|\bcuenta\b|\bcifra\b")),
    ("colores", re.compile(r"\bcolores?\b")),
    ("animales", re.compile(r"\banimales?\b|\bmascota\b|\bayudame\s+con\s+animales\b")),
    ("ejemplo", re.compile(r"\bdame\s+un\s+ejemplo\b|\bun\s+ejemplo\b|\bejemplo\s+de\b")),
    ("aprender", re.compile(r"\baprender\b|\baprendizaje\b|\bpracticar\b|\bestudiar\b")),
]

_CHAT_TOPIC_SEED_TOKENS: dict[str, tuple[str, ...]] = {
    "saludos": ("saludo", "hola", "ma'g", "fxi'z", "ewcha"),
    "familia": ("familia", "casa", "yaattewe"),
    "gracias": ("agradecer", "agradecido", "wecha"),
    "despedida": ("despedir", "saludar", "wecha", "hola"),
    "numeros": ("numero", "contar", "uno", "dos"),
    "colores": ("color", "rojo", "azul", "verde"),
    "animales": ("animal", "perro", "gato"),
    "ejemplo": ("ejemplo", "dialogo", "estudiante"),
    "aprender": ("aprender", "practicar", "dialogo"),
}

_TOPIC_CURATED_FALLBACK: dict[str, list[str]] = {
    "saludos": [
        "• Ma'g fxi'z — Saludo basico",
        "• Ma'w fxi'z — Saludo basico",
        "• ewcha — ¡Hola! (saludando a un hombre)",
        "• ewchacue — ¡Hola! (saludando a una mujer o a varias personas)",
    ],
    "gracias": [
        "• wecha- / wecháa- — 1. estar agradecido, agradecer; 2. saludar, despedir, besar",
    ],
    "despedida": [
        "• wecha- / wecháa- — 1. estar agradecido, agradecer; 2. saludar, despedir, besar",
        "• ewcha — ¡Hola! (saludando a un hombre)",
        "• Ma'g fxi'z — Saludo basico (también sirve para cerrar un encuentro con respeto)",
    ],
    "familia": [
        "• yaattewe'sh — familia, los de la casa",
    ],
}


def _detect_chat_topic(query_norm: str, q_tokens: list[str]) -> str | None:
    if _is_thanking_avi(query_norm, q_tokens):
        return None
    # Traduccion lexical directa (perro, agua…): no forzar tema animales/numeros/colores.
    if "en nasa yuwe" in query_norm or "a nasa yuwe" in query_norm:
        thematic_only = ("saludos", "despedida", "familia", "gracias")
    else:
        thematic_only = None
    for name, rx in _CHAT_TOPIC_REGEX:
        if thematic_only is not None and name not in thematic_only:
            continue
        if not rx.search(query_norm):
            continue
        if name == "gracias":
            if not _is_asking_how(query_norm):
                continue
            if not re.search(r"\b(como|digo|dice|decir|significa)\b", query_norm):
                continue
        if name == "familia" and _FAMILY_LEXICON_HINTS.search(query_norm):
            if not re.search(r"\bfamilia\b|\bparentesco\b", query_norm):
                continue
        if name == "saludos" and re.search(r"\bcomo\s+me\s+despido\b", query_norm):
            continue
        return name
    return None


def _vague_chat_guidance(query_norm: str) -> str | None:
    """Chips del inicio que necesitan que el estudiante complete la idea."""
    if query_norm in ("traduce esta frase", "traduce esta palabra"):
        return (
            "Claro. Escribe en español la frase completa que quieres pasar a Nasa Yuwe "
            "(por ejemplo: «buenos días», «me llamo Ana», «gracias por tu ayuda») y te doy la forma en Nasa Yuwe."
        )
    if query_norm in ("como se dice", "como se dice?"):
        return (
            "¿Qué palabra o frase quieres decir en Nasa Yuwe? Escríbela en español "
            "(por ejemplo: agua, gracias, mi mamá) y te respondo con la forma del corpus."
        )
    m_cs = re.search(r"^como\s+se\s+dice\s*(.+?)\s*\??$", query_norm)
    if m_cs:
        rest = normalize_text(m_cs.group(1).strip(" ?."))
        if not rest or rest in ("", "…", "..."):
            return (
                "¿Qué palabra o frase quieres decir en Nasa Yuwe? Escríbela en español "
                "(por ejemplo: agua, gracias, mi mamá) y te respondo con la forma del corpus."
            )
    if query_norm.startswith("explicame esta palabra") or query_norm.startswith("explica esta palabra"):
        return (
            "¿Cuál palabra quieres que te explique? Escríbela en español o en Nasa Yuwe "
            "y te doy significado, uso y un ejemplo corto."
        )
    return None


def _line_matches_topic(topic: str, nasa_yuwe: str, espanol: str) -> bool:
    blob = normalize_text(f"{nasa_yuwe} {espanol}")
    if not blob:
        return False
    if topic == "despedida":
        if any(b in blob for b in ("despedaz", "pedaz", "padrino", "sombra", "llamas", "como,")):
            return False
        return any(g in blob for g in ("despedir", "saludar", "besar", "hola", "wecha", "saludo"))
    if topic == "gracias":
        return "agradec" in blob or (normalize_text(nasa_yuwe).startswith("wecha") and "agradec" in blob)
    if topic == "saludos":
        if "despedaz" in blob or "padrino" in blob:
            return False
        return any(g in blob for g in ("saludo", "hola", "ma'g", "ma'w", "ewcha", "ikuus", "pe't"))
    if topic == "familia":
        return "familia" in blob or "casa" in blob
    if topic == "numeros":
        return any(g in blob for g in ("numero", "contar", "uno", "dos", "tres", "cuatro", "cinco"))
    if topic == "colores":
        return "color" in blob or any(c in blob for c in ("rojo", "azul", "verde", "amarillo", "negro", "blanco"))
    if topic == "animales":
        return "animal" in blob or any(
            a in blob for a in ("perro", "gato", "pajaro", "pez", "vaca", "caballo", "cuy")
        )
    return True


def _contexts_lexico_lines(
    contexts: list[dict],
    limit: int = 5,
    *,
    prefer_gloss: str = "",
    topic: str | None = None,
) -> list[str]:
    prefer = normalize_text(prefer_gloss) if prefer_gloss else ""
    ordered = list(contexts)
    if prefer:

        def rank(ctx: dict) -> tuple[int, int, str]:
            es = normalize_text(ctx.get("espanol") or "")
            return (_gloss_match_rank(prefer, es), len(es), es)

        ordered = sorted(ordered, key=rank)

    lines = []
    seen = set()
    for ctx in ordered:
        rt = (ctx.get("record_type") or "").strip().lower()
        ny = (ctx.get("nasa_yuwe") or "").strip()
        es = (ctx.get("espanol") or "").strip()
        if topic and rt == "lexico" and not _line_matches_topic(topic, ny, es):
            continue
        if rt not in ("lexico", "dialogo"):
            continue
        if topic in ("numeros", "colores", "animales", "gracias", "saludos", "despedida", "familia") and rt == "dialogo":
            continue
        if rt == "lexico" and (not ny or _looks_like_meta_spanish_gloss(es)):
            continue
        if rt == "dialogo":
            key = (ny[:80], es[:80])
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"• {es[:220]}")
            if len(lines) >= limit:
                break
            continue
        key = (ny, es)
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"• {ny} — {es}")
        if len(lines) >= limit:
            break
    return lines


def _topic_lines_or_fallback(contexts: list[dict], topic: str, *, prefer: str = "", limit: int = 5) -> list[str]:
    lines = _contexts_lexico_lines(contexts, limit, prefer_gloss=prefer, topic=topic)
    if lines:
        return lines
    return list(_TOPIC_CURATED_FALLBACK.get(topic, []))


def compose_avi_chat_answer(
    query_norm: str,
    q_tokens: list[str],
    contexts: list[dict],
    *,
    translation_intent: bool,
    direct_target: str = "",
) -> str:
    """
    Texto del tutor AVI para la vista 'Conversar': tono cercano, sin exponer metadatos tecnicos
    (fuente sintetica, tipo de registro, etc.) en el cuerpo del mensaje.
    """
    ts = set(q_tokens)
    contexts = _prioritize_chat_contexts(
        contexts,
        direct_target=direct_target,
        translation_intent=translation_intent,
    )
    best = contexts[0] if contexts else {}
    es = (best.get("espanol") or "").strip()
    ny = (best.get("nasa_yuwe") or "").strip()
    rt = (best.get("record_type") or "").strip().lower()

    def pair_block() -> str:
        if ny and es and _looks_like_meta_spanish_gloss(es):
            return f"Para saludar en Nasa Yuwe puedes usar: {ny}"
        parts = []
        if ny:
            parts.append(f"Nasa Yuwe: {ny}")
        if es and not _looks_like_meta_spanish_gloss(es):
            parts.append(f"Español (referencia): {es}")
        elif es and _looks_like_meta_spanish_gloss(es) and not ny:
            parts.append(f"Referencia: {es}")
        return (
            "\n".join(parts)
            if parts
            else "Te sugiero nombrar un tema concreto (familia, saludo, numeros, colores) o una sola palabra que quieras aprender."
        )

    topic = _detect_chat_topic(query_norm, q_tokens)
    dt = normalize_text(_clean_lexical_target(direct_target) or direct_target or "")

    if dt and not topic:
        lines = _contexts_lexico_lines(contexts, 4, prefer_gloss=dt)
        if lines:
            label = direct_target or dt
            return (
                f"Claro. Esto es lo que encontré para «{label}» en el corpus:\n\n"
                + "\n".join(lines)
                + "\n\n"
                "Practica la forma en Nasa Yuwe en voz alta tres veces; luego úsala en una frase corta. "
                "Si quieres otro matiz (formal, con niños, en clase), dímelo."
            )

    if topic == "saludos":
        lines = _topic_lines_or_fallback(contexts, "saludos", prefer="saludo basico", limit=6)
        return (
            "Para saludar o presentarte en Nasa Yuwe, estas formas aparecen en el material del curso:\n\n"
            + "\n".join(lines)
            + "\n\n"
            "Consejo: Ma'g suele usarse hacia una persona considerada hombre; Ma'w hacia mujer. "
            "Elige una sola frase, repítela en voz alta tres veces y luego úsala en una mini presentación."
        )

    if topic == "gracias":
        lines = _topic_lines_or_fallback(contexts, "gracias", prefer="agradec", limit=4)
        extra = ("\n\nOtras formas relacionadas:\n" + "\n".join(lines[1:])) if len(lines) > 1 else ""
        return (
            "Para agradecer o decir gracias, en el corpus aparece sobre todo el verbo de agradecimiento:\n\n"
            f"{lines[0]}{extra}\n\n"
            "Puedes usarlo en contexto formal con calma. Si me dices si es para un adulto, un par o en clase, "
            "te sugiero una frase corta completa."
        )

    if topic == "despedida":
        lines = _topic_lines_or_fallback(contexts, "despedida", prefer="despedir", limit=5)
        return (
            "Para despedirte en Nasa Yuwe, puedes apoyarte en estas formas del material del curso:\n\n"
            + "\n".join(lines)
            + "\n\n"
            "Practica una despedida corta: saludo + agradecimiento breve + deseo de buen día. "
            "Si escribes tu despedida en español, te ayudo a pasarla a Nasa Yuwe."
        )

    if topic == "familia":
        lines = _topic_lines_or_fallback(contexts, "familia", prefer="familia", limit=5)
        more = ("\n\nTambién relacionado:\n" + "\n".join(lines[1:])) if len(lines) > 1 else ""
        return (
            "Qué bonito tema. Para hablar de familia, una palabra central en el corpus es:\n\n"
            f"{lines[0]}{more}\n\n"
            "Puedes armar frases sencillas: mi familia, en mi casa, con mi mamá/papá… "
            "Dime quién quieres mencionar (mamá, papá, hermano, abuela) y buscamos la forma en Nasa Yuwe."
        )

    if topic == "numeros":
        lines = _topic_lines_or_fallback(contexts, "numeros", prefer="numero", limit=6)
        return (
            "Para trabajar números en Nasa Yuwe, esto es lo que encontré en el corpus:\n\n"
            + "\n".join(lines)
            + "\n\n"
            "Practica contando del 1 al 5 en voz alta. Si necesitas un número concreto, escríbelo en español."
        )

    if topic == "colores":
        lines = _topic_lines_or_fallback(contexts, "colores", prefer="color", limit=6)
        if not lines:
            lines = [
                "• Beh — Rojo",
                "• Çemçem — Azul",
                "• atate tsẽy — amarillo",
            ]
        return (
            "Estos colores y formas relacionadas aparecen en el material:\n\n"
            + "\n".join(lines)
            + "\n\n"
            "Nómbrame un color en español si quieres profundizar en uno solo."
        )

    if topic == "animales":
        lines = _topic_lines_or_fallback(contexts, "animales", prefer="animal", limit=6)
        return (
            "Sobre animales en Nasa Yuwe, el corpus tiene entradas como estas:\n\n"
            + "\n".join(lines)
            + "\n\n"
            "Dime un animal concreto (perro, gato, pájaro…) y te doy la forma exacta."
        )

    if topic == "ejemplo":
        lines = _contexts_lexico_lines(contexts, 3, topic="ejemplo")
        if not lines:
            lines = _topic_lines_or_fallback(contexts, "saludos", limit=2)
        return (
            "Te dejo un ejemplo tomado del material del curso para que lo uses como modelo:\n\n"
            + "\n".join(lines)
            + "\n\n"
            "Léelo en voz alta, luego cambia un solo detalle (nombre, lugar o persona) y vuelve a practicarlo."
        )

    if topic == "aprender":
        lines = _contexts_lexico_lines(contexts, 4, prefer_gloss="aprender", topic="aprender")
        if not lines:
            lines = _contexts_lexico_lines(contexts, 3, topic=None)
        body = "\n".join(lines) if lines else pair_block()
        return (
            "Buena actitud. Para aprender paso a paso, te sugiero empezar con vocabulario concreto:\n\n"
            f"{body}\n\n"
            "Elige un tema (saludos, familia, colores, animales) y practica tres palabras hoy. "
            "Yo te guío frase por frase."
        )

    wants_hi = (
        query_norm.strip() in ("hola", "buenas", "hey", "ei")
        or any(p in query_norm for p in ("buenos dias", "buenas tardes", "buenas noches", "buen dia", "buena tarde"))
        or ("hola" in ts and len(ts) <= 4)
    )
    wants_thanks = _is_thanking_avi(query_norm, q_tokens)
    wants_bye = any(
        p in query_norm for p in ("adios", "hasta luego", "nos vemos", "chao", "chau", "hasta pronto", "me voy")
    )

    if wants_bye:
        return _chat_pick_variant(
            query_norm,
            (
                "Ha sido un gusto acompañarte en esta sesión. Sigue practicando con calma; el idioma se abre poco a poco.\n\n"
                "Cuando quieras volver, aquí estaré.",
                "Nos leemos pronto. Recuerda: una frase corta al día suma muchísimo.\n\n"
                "Hasta la próxima.",
            ),
        )

    if wants_thanks:
        return (
            "De nada, con gusto.\n\n"
            f"Por si te sirve retenerlo, esto es lo que mejor encaja con lo que venías comentando:\n\n"
            f"{pair_block()}\n\n"
            "Si quieres profundizar, dime en qué situación real lo usarías (colegio, casa, saludo a un adulto…) y lo afinamos."
        )

    if rt == "dialogo":
        return (
            "Te dejo una idea clara, tomada del material del curso, para que la uses como modelo:\n\n"
            f"{pair_block()}\n\n"
            "Léela en voz alta una vez en español y otra vez fijándote en la parte en Nasa Yuwe. "
            "Luego inventa una variación mínima: cambia solo un detalle (quién habla, el lugar, el momento del día)."
        )

    if translation_intent or "como se dice" in query_norm or "traduce" in query_norm or "traduccion" in query_norm:
        return (
            "Claro. Así lo tienes en la ficha que mejor coincide con tu pregunta:\n\n"
            f"{pair_block()}\n\n"
            "Practica primero la forma en Nasa Yuwe sola, y cuando te salga fluida, métela en una frase de tres a siete palabras. "
            "Si me dices el contexto (formal o informal), te propongo una mini conversación."
        )

    if wants_hi:
        opener = _chat_pick_variant(
            query_norm,
            (
                "Hola, qué gusto que sigas aquí.",
                "Buen momento para practicar; vamos con calma.",
                "Hola. Me alegra leerte; seguimos paso a paso.",
            ),
        )
        return (
            f"{opener}\n\n"
            "Sobre lo que preguntas, esto es lo que mejor encaja con el material que tenemos a mano:\n\n"
            f"{pair_block()}\n\n"
            "Úsalo como saludo o presentación breve, y si quieres un tono más formal o más cercano, dímelo y lo ajustamos."
        )

    second = contexts[1] if len(contexts) > 1 else None
    extra = ""
    if second:
        s_es = (second.get("espanol") or "").strip()
        s_ny = (second.get("nasa_yuwe") or "").strip()
        if (s_es or s_ny) and (s_es != es or s_ny != ny):
            lines2 = [f"Nasa Yuwe: {s_ny or '—'}"]
            if s_es and not _looks_like_meta_spanish_gloss(s_es):
                lines2.append(f"Español: {s_es}")
            extra = "\n\nTambién podría relacionarse con esto:\n" + "\n".join(lines2)

    lines = _contexts_lexico_lines(contexts, 3, prefer_gloss=dt)
    if lines:
        return (
            "Esto es lo que mejor encaja con tu mensaje:\n\n"
            + "\n".join(lines)
            + "\n\n"
            "Si buscabas otra palabra, escríbela sola o en una frase corta (por ejemplo: «¿cómo se dice agua?»)."
            + extra
        )

    return (
        "Puedo ayudarte con palabras, saludos, familia, números, colores o animales.\n\n"
        f"{pair_block()}\n\n"
        "Prueba escribiendo una palabra en español o preguntando «¿cómo se dice … en Nasa Yuwe?»."
        + extra
    )


class CorpusEngine:
    """
    AVI engine with lightweight optimization:
    - inverted index retrieval
    - weighted overlap scoring
    - MMR diversification
    - answer cache with TTL
    """

    def __init__(self, corpus_path: Path):
        self.corpus_path = corpus_path
        self.rows = []
        self.inv_index = defaultdict(set)
        self.doc_tokens = {}
        self.doc_freq = Counter()
        self.cache = {}
        self.cache_ttl = 180  # seconds
        self.metrics = Counter()
        self.by_category = defaultdict(list)
        self.model = self._load_model()
        self._load()

    def _load_model(self):
        if not MODEL_PATH.exists():
            return {
                "model_name": "AVI Retrieval Model runtime",
                "model_type": "runtime_idf",
                "idf": {},
                "training_rows": 0,
                "vocabulary_size": 0,
            }
        with MODEL_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _load(self):
        if not self.corpus_path.exists():
            raise FileNotFoundError(f"No se encontro corpus en: {self.corpus_path}")

        with self.corpus_path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                rid = row["id"]
                nasa = row.get("nasa_yuwe", "")
                esp = row.get("espanol", "")
                cat_display = (row.get("categoria") or "general").strip() or "general"
                cat_key = normalize_text(cat_display) or "general"
                record_type = row.get("record_type", "lexico")
                source = row.get("fuente_nombre", "desconocida")

                text = f"{nasa} {esp} {cat_display} {record_type}"
                toks = set(tokenize(text))
                if not toks:
                    continue

                self.rows.append(
                    {
                        "idx": len(self.rows),
                        "id": rid,
                        "nasa_yuwe": nasa,
                        "espanol": esp,
                        "categoria": cat_display,
                        "record_type": record_type,
                        "fuente_nombre": source,
                        "fuente_url": row.get("fuente_url", ""),
                        "source_kind": row.get("source_kind", ""),
                        "nivel_confianza": row.get("nivel_confianza", ""),
                        "intencion": row.get("intencion", ""),
                        "espanol_norm": normalize_text(esp),
                        "nasa_norm": normalize_text(nasa),
                    }
                )
                self.doc_tokens[i] = toks
                for t in toks:
                    self.inv_index[t].add(i)
                for t in toks:
                    self.doc_freq[t] += 1
                self.by_category[cat_key].append(i)

        self.total_docs = max(len(self.rows), 1)

    def _doc_ids_for_category(self, cat_norm: str) -> list:
        if cat_norm in VIRTUAL_CATEGORIES:
            seen = set()
            ordered = []
            for sub in VIRTUAL_CATEGORIES[cat_norm]:
                for i in self.by_category.get(sub, []):
                    if i not in seen:
                        seen.add(i)
                        ordered.append(i)
            return ordered
        return list(self.by_category.get(cat_norm, []))

    def _has_category(self, cat_norm: str) -> bool:
        if cat_norm in VIRTUAL_CATEGORIES:
            return any(self.by_category.get(s) for s in VIRTUAL_CATEGORIES[cat_norm])
        return cat_norm in self.by_category

    def _idf(self, token: str) -> float:
        trained_idf = (self.model.get("idf") or {}).get(token)
        if trained_idf is not None:
            return float(trained_idf)
        return math.log((1 + self.total_docs) / (1 + self.doc_freq.get(token, 0))) + 1.0

    def _candidates(self, query_tokens):
        ids = set()
        for t in query_tokens:
            ids |= self.inv_index.get(t, set())
        return ids

    def _topic_doc_indices(self, topic: str) -> list[int]:
        """Refuerza recuperacion para chips frecuentes (saludo, familia, gracias, despedida)."""
        out: list[int] = []
        seen: set[int] = set()

        def add(i: int) -> None:
            if i not in seen:
                seen.add(i)
                out.append(i)

        if topic == "saludos":
            for i in self._doc_ids_for_category("saludos"):
                row = self.rows[i]
                if row.get("record_type") == "lexico" and not _looks_like_meta_spanish_gloss(row.get("espanol", "")):
                    add(i)
            for i, row in enumerate(self.rows):
                if row.get("record_type") == "lexico" and "hola" in (row.get("espanol_norm") or ""):
                    add(i)
        elif topic == "familia":
            for i, row in enumerate(self.rows):
                esn = row.get("espanol_norm") or ""
                if "familia" in esn and row.get("record_type") == "lexico":
                    add(i)
        elif topic == "gracias":
            for i, row in enumerate(self.rows):
                if row.get("record_type") != "lexico":
                    continue
                esn = row.get("espanol_norm") or ""
                ny = row.get("nasa_norm") or ""
                if "agradecer" in esn or (ny.startswith("wecha") and "agradec" in esn):
                    add(i)
        elif topic == "despedida":
            for i, row in enumerate(self.rows):
                row = self.rows[i]
                if row.get("record_type") != "lexico":
                    continue
                esn = row.get("espanol_norm") or ""
                ny = row.get("nasa_norm") or ""
                if "despedaz" in esn or "pedaz" in esn or "llamas" in esn or "padrino" in esn:
                    continue
                if "despedir" in esn or "despedida" in esn or (ny.startswith("wecha") and "saludar" in esn):
                    add(i)
            for i in self._doc_ids_for_category("saludos"):
                row = self.rows[i]
                if row.get("record_type") == "lexico" and not _looks_like_meta_spanish_gloss(row.get("espanol", "")):
                    add(i)
            for i, row in enumerate(self.rows):
                if row.get("record_type") == "lexico" and "hola" in (row.get("espanol_norm") or ""):
                    add(i)
        elif topic == "numeros":
            for cat in ("numeros", "vocabulario_general"):
                for i in self._doc_ids_for_category(cat):
                    if self.rows[i].get("record_type") == "lexico":
                        add(i)
            for i, row in enumerate(self.rows):
                esn = row.get("espanol_norm") or ""
                if row.get("record_type") == "lexico" and (
                    "numero" in esn or "contar" in esn or "uno" in esn or "dos" in esn
                ):
                    add(i)
        elif topic == "colores":
            for cat in ("colores", "vocabulario_general"):
                for i in self._doc_ids_for_category(cat):
                    if self.rows[i].get("record_type") == "lexico":
                        add(i)
            for i, row in enumerate(self.rows):
                esn = row.get("espanol_norm") or ""
                if row.get("record_type") == "lexico" and (
                    "color" in esn or "rojo" in esn or "azul" in esn or "verde" in esn
                ):
                    add(i)
        elif topic == "animales":
            for i in self._doc_ids_for_category("animales"):
                if self.rows[i].get("record_type") == "lexico":
                    add(i)
        elif topic in ("ejemplo", "aprender"):
            for i, row in enumerate(self.rows):
                if row.get("record_type") == "dialogo":
                    add(i)
            for i, row in enumerate(self.rows):
                esn = row.get("espanol_norm") or ""
                if row.get("record_type") == "lexico" and "aprender" in esn:
                    add(i)
        return out[:20]

    def _score(self, q_tokens, doc_id, pedagogical_intent=False):
        d_tokens = self.doc_tokens[doc_id]
        row = self.rows[doc_id]
        overlap = set(q_tokens) & d_tokens
        if not overlap:
            return 0.0
        weighted = sum(self._idf(t) for t in overlap)
        coverage = len(overlap) / max(1, len(set(q_tokens)))
        score = weighted * 0.7 + coverage * 0.3
        # prioritize lexical entries for translation intent
        if row.get("record_type") == "lexico":
            score *= 1.12
        if pedagogical_intent and row.get("record_type") == "dialogo":
            score *= 1.25
        return score

    def _similarity(self, d1, d2):
        s1 = self.doc_tokens[d1]
        s2 = self.doc_tokens[d2]
        inter = len(s1 & s2)
        union = len(s1 | s2) or 1
        return inter / union

    def _mmr(self, ranked_ids, top_k=5, lambda_param=0.75):
        selected = []
        candidates = ranked_ids[:]
        while candidates and len(selected) < top_k:
            best_id = None
            best_mmr = -1e9
            for cid in candidates:
                rel = cid[1]
                if not selected:
                    div_penalty = 0.0
                else:
                    div_penalty = max(self._similarity(cid[0], sid[0]) for sid in selected)
                mmr_score = lambda_param * rel - (1 - lambda_param) * div_penalty
                if mmr_score > best_mmr:
                    best_mmr = mmr_score
                    best_id = cid
            selected.append(best_id)
            candidates = [c for c in candidates if c[0] != best_id[0]]
        return selected

    def _cached(self, query: str):
        now = time.time()
        item = self.cache.get(query)
        if not item:
            return None
        if now - item["time"] > self.cache_ttl:
            del self.cache[query]
            return None
        return item["data"]

    def ask(self, query: str, top_k=5):
        query_norm = normalize_text(query)
        if not query_norm:
            return {"answer": "Escribe una pregunta o una palabra y te respondo en seguida.", "contexts": []}

        cached = self._cached(query_norm)
        if cached:
            cached["meta"]["cache_hit"] = True
            self.metrics["cache_hit"] += 1
            return cached

        vague = _vague_chat_guidance(query_norm)
        if vague:
            data = {
                "answer": vague,
                "contexts": [],
                "meta": {"cache_hit": False, "vague_prompt": True},
            }
            self.cache[query_norm] = {"time": time.time(), "data": data}
            return data

        q_tokens = tokenize(query_norm)
        help_msg = _chat_help_guidance(query_norm, q_tokens)
        if help_msg:
            data = {
                "answer": help_msg,
                "contexts": [],
                "meta": {"cache_hit": False, "help_prompt": True},
            }
            self.cache[query_norm] = {"time": time.time(), "data": data}
            return data
        if _query_looks_unsearchable(query_norm, q_tokens):
            data = {
                "answer": (
                    "No encontré esa palabra en el corpus tal como la escribiste. "
                    "Revisa la ortografía o prueba una palabra en español (agua, luna, mamá, rojo…).\n\n"
                    "También puedes pedir un tema: saludos, familia, números, colores o animales."
                ),
                "contexts": [],
                "meta": {"cache_hit": False, "unsearchable": True},
            }
            self.cache[query_norm] = {"time": time.time(), "data": data}
            return data
        if _is_thanking_avi(query_norm, q_tokens):
            data = {
                "answer": (
                    "De nada, con gusto.\n\n"
                    "Me alegra acompañarte. Cuando quieras, seguimos con otra palabra o tema "
                    "(saludos, familia, numeros, colores…)."
                ),
                "contexts": [],
                "meta": {"cache_hit": False, "thanks_only": True},
            }
            self.cache[query_norm] = {"time": time.time(), "data": data}
            return data
        asking_how = _is_asking_how(query_norm)
        chat_topic = _detect_chat_topic(query_norm, q_tokens)
        if chat_topic:
            q_tokens = list(set(q_tokens) | set(_CHAT_TOPIC_SEED_TOKENS.get(chat_topic, ())))
        translation_intent = asking_how or (
            ("dice" in q_tokens)
            or ("traduce" in q_tokens)
            or ("traduccion" in q_tokens)
            or ("como se dice" in query_norm)
        )
        pedagogical_intent = bool(
            {
                "practicar",
                "practica",
                "dialogo",
                "dialogos",
                "clase",
                "docente",
                "estudiante",
                "actividad",
                "aprender",
                "aprendizaje",
            }
            & set(q_tokens)
        )

        cand = self._candidates(q_tokens)
        if chat_topic:
            for i in self._topic_doc_indices(chat_topic):
                cand.add(i)

        direct_target = _clean_lexical_target(_extract_lexical_target(query_norm, q_tokens) or "")
        if not direct_target:
            m = re.search(r"dice (.+?) en nasa yuwe", query_norm)
            if m:
                direct_target = _clean_lexical_target(m.group(1))
        if not direct_target:
            m2 = re.search(r"traduce (.+?) a nasa yuwe", query_norm)
            if m2:
                direct_target = _clean_lexical_target(m2.group(1))
        if direct_target:
            for i in _lexico_doc_indices(self.rows, direct_target):
                cand.add(i)
            if not cand:
                content = _content_tokens_from_query(q_tokens)
                if content:
                    for i in _lexico_doc_indices(self.rows, content[0]):
                        cand.add(i)
        if not cand and chat_topic:
            for i in self._topic_doc_indices(chat_topic):
                cand.add(i)
        if not cand:
            lookup_q = direct_target or " ".join(_content_tokens_from_query(q_tokens)) or query_norm
            ds = self.dictionary_search(lookup_q)
            found = ds.get("found")
            if found:
                fid = found.get("id")
                for i, row in enumerate(self.rows):
                    if row.get("id") == fid:
                        cand.add(i)
                        if not direct_target:
                            direct_target = normalize_text(found.get("espanol") or lookup_q)
                        break
            elif ds.get("suggestions"):
                top = ds["suggestions"][0]
                es_top = normalize_text(top.get("espanol") or "")
                dist = _lev_distance(lookup_q, es_top)
                if _dict_suggestion_acceptable(lookup_q, dist):
                    for i, row in enumerate(self.rows):
                        if row.get("record_type") == "lexico" and (row.get("espanol_norm") or "") == es_top:
                            cand.add(i)
                            direct_target = es_top
                            break
        if not cand:
            if _is_thanking_avi(query_norm, q_tokens):
                data = {
                    "answer": (
                        "De nada, con gusto.\n\n"
                        "Me alegra acompañarte. Cuando quieras, seguimos con otra palabra o tema "
                        "(saludos, familia, numeros, colores…)."
                    ),
                    "contexts": [],
                    "meta": {"cache_hit": False, "candidates": 0, "thanks_only": True},
                }
                self.cache[query_norm] = {"time": time.time(), "data": data}
                return data
            data = {
                "answer": (
                    "Todavia no tengo una pista clara con las palabras que usaste. "
                    "Prueba con un tema concreto (por ejemplo: saludos, familia, numeros, colores) o con una sola palabra que quieras aprender."
                ),
                "contexts": [],
                "meta": {"cache_hit": False, "candidates": 0},
            }
            self.cache[query_norm] = {"time": time.time(), "data": data}
            self.metrics["empty_result"] += 1
            return data

        scored = []
        for doc_id in cand:
            row_doc = self.rows[doc_id]
            rt = row_doc.get("record_type", "").strip().lower()
            if (translation_intent or direct_target) and rt in {"qa", "dialogo"}:
                # avoid generated conversational records when user asks direct lexical translation
                continue
            if chat_topic == "saludos" and rt in {"qa", "dialogo"}:
                continue
            if chat_topic in {"gracias", "familia", "despedida", "numeros", "colores", "animales"} and rt == "qa":
                continue
            if chat_topic == "ejemplo" and rt == "qa":
                continue
            if direct_target and row_doc.get("record_type", "").strip().lower() == "lexico":
                esn = row_doc.get("espanol_norm") or ""
                nyn = row_doc.get("nasa_norm") or ""
                dt = normalize_text(direct_target)
                if esn == dt or nyn == dt:
                    scored.append((doc_id, 999.0))
                    continue
                if esn.startswith(dt + " ") or (esn.split()[:1] == [dt]):
                    scored.append((doc_id, 950.0))
                    continue
                if dt in esn.split():
                    scored.append((doc_id, 900.0))
                    continue
                if dt in esn or dt in nyn:
                    scored.append((doc_id, 850.0))
                    continue
            sc = self._score(q_tokens, doc_id, pedagogical_intent=pedagogical_intent)
            if chat_topic == "saludos" and rt == "lexico":
                sc *= 1.35
            if chat_topic == "familia" and "familia" in (row_doc.get("espanol_norm") or ""):
                sc *= 1.5
            if chat_topic == "gracias" and "agradec" in (row_doc.get("espanol_norm") or ""):
                sc *= 1.45
            if chat_topic == "despedida" and "despedir" in (row_doc.get("espanol_norm") or ""):
                sc *= 1.4
            if chat_topic == "numeros" and "numero" in (row_doc.get("espanol_norm") or ""):
                sc *= 1.35
            if chat_topic == "colores" and "color" in (row_doc.get("espanol_norm") or ""):
                sc *= 1.35
            if chat_topic == "animales" and row_doc.get("categoria", "").lower() == "animales":
                sc *= 1.4
            if chat_topic in ("ejemplo", "aprender") and rt == "dialogo":
                sc *= 1.3
            if sc > 0:
                scored.append((doc_id, sc))
        if not scored and chat_topic:
            for i in self._topic_doc_indices(chat_topic)[: max(top_k, 5)]:
                scored.append((i, 1.0))
        if not scored and direct_target:
            for i in _lexico_doc_indices(self.rows, direct_target)[: max(top_k, 5)]:
                scored.append((i, 1.0))
        scored.sort(key=lambda x: x[1], reverse=True)
        mmr_selected = self._mmr(scored, top_k=top_k, lambda_param=0.75)

        contexts = []
        for doc_id, score in mmr_selected:
            row = self.rows[doc_id]
            contexts.append(
                {
                    "id": row["id"],
                    "nasa_yuwe": row["nasa_yuwe"],
                    "espanol": row["espanol"],
                    "categoria": row["categoria"],
                    "record_type": row["record_type"],
                    "fuente_nombre": row["fuente_nombre"],
                    "fuente_url": row.get("fuente_url", ""),
                    "source_kind": row.get("source_kind", ""),
                    "nivel_confianza": row.get("nivel_confianza", ""),
                    "intencion": row.get("intencion", ""),
                    "score": round(float(score), 4),
                }
            )

        best = contexts[0] if contexts else None
        if best:
            contexts = _prioritize_chat_contexts(
                contexts,
                direct_target=direct_target,
                translation_intent=translation_intent,
            )
            answer = compose_avi_chat_answer(
                query_norm,
                q_tokens,
                contexts,
                translation_intent=translation_intent,
                direct_target=direct_target,
            )
        else:
            answer = (
                "No tengo una coincidencia segura con esa pregunta. "
                "Reformula con otra palabra o dime si buscas saludo, despedida, familia, numeros… y lo intentamos de nuevo."
            )

        data = {
            "answer": answer,
            "contexts": contexts,
            "meta": {
                "cache_hit": False,
                "candidates": len(cand),
                "retrieved": len(contexts),
                "optimizer": "idf_overlap + mmr + ttl_cache",
            },
        }
        self.cache[query_norm] = {"time": time.time(), "data": data}
        self.metrics["queries"] += 1
        return data

    def lesson(self, category: str, limit: int = 8):
        cat_norm = normalize_text(category)
        if not cat_norm or not self._has_category(cat_norm):
            options = sorted(self.by_category.keys())[:12]
            return {
                "category": cat_norm,
                "terms": [],
                "available_categories": options,
                "message": "Categoria no disponible, revisa las sugeridas.",
            }

        try:
            cap = int(limit)
        except (TypeError, ValueError):
            cap = 12
        want_all = cap <= 0
        if not want_all and cap < 1:
            cap = 12
        max_terms = 10**9 if want_all else cap

        doc_ids = self._doc_ids_for_category(cat_norm)
        if not want_all:
            doc_ids = doc_ids[: max(cap * 25, 600)]

        rows = []
        for doc_id in doc_ids:
            row = self.rows[doc_id]
            if row["record_type"] != "lexico":
                continue
            rows.append(
                _attach_term_image(
                    {
                        "id": row["id"],
                        "nasa_yuwe": row["nasa_yuwe"],
                        "espanol": row["espanol"],
                        "fuente_nombre": row["fuente_nombre"],
                        "categoria": row.get("categoria") or row.get("categoria_norm") or "",
                    }
                )
            )
            if not want_all and len(rows) >= max_terms:
                break
        self.metrics["lessons"] += 1
        return {
            "category": cat_norm,
            "terms": rows,
            "count": len(rows),
            "available_categories": sorted(self.by_category.keys()),
            "message": "Leccion generada con vocabulario del corpus real.",
        }

    def lexicon_terms_flat(self, limit: int = 8000) -> list[dict]:
        """Todos los registros lexicos (para diccionario estudiantil en una sola respuesta)."""
        try:
            cap = int(limit)
        except (TypeError, ValueError):
            cap = 8000
        cap = max(1, min(cap, 50_000))
        out: list[dict] = []
        for row in self.rows:
            if row.get("record_type") != "lexico":
                continue
            out.append(
                _attach_term_image(
                    {
                        "id": row["id"],
                        "nasa_yuwe": row["nasa_yuwe"],
                        "espanol": row["espanol"],
                        "fuente_nombre": row["fuente_nombre"],
                        "categoria": row.get("categoria") or "",
                    }
                )
            )
            if len(out) >= cap:
                break
        return out

    def dictionary_search(self, raw_q: str) -> dict:
        """Busqueda de palabra para diccionario estudiantil (traduccion + sugerencias)."""
        qraw = (raw_q or "").strip()
        ql = normalize_text(qraw)
        if not ql:
            return {
                "found": None,
                "suggestions": [],
                "alternatives": [],
                "message": "Ingresa una palabra para buscar.",
            }

        lex_matches = []
        for row in self.rows:
            if row.get("record_type") != "lexico":
                continue
            es = normalize_text(row.get("espanol", ""))
            ny = normalize_text(row.get("nasa_yuwe", ""))
            score = 0
            if ql == es or ql == ny:
                score = 100
            elif ql in es or ql in ny:
                score = 80
            elif es.startswith(ql) or ny.startswith(ql):
                score = 70
            elif any(ql in part for part in es.split() if len(ql) >= 3):
                score = 55
            if score:
                entry = _attach_term_image(
                    {
                        "id": row.get("id"),
                        "espanol": row.get("espanol", ""),
                        "nasa_yuwe": row.get("nasa_yuwe", ""),
                        "categoria": row.get("categoria", ""),
                        "fuente_nombre": row.get("fuente_nombre", ""),
                    }
                )
                lex_matches.append((score, entry))

        lex_matches.sort(key=lambda x: x[0], reverse=True)
        if lex_matches:
            best = lex_matches[0][1]
            alt = [x[1] for x in lex_matches[1:12]]
            return {"found": best, "alternatives": alt, "suggestions": [], "message": "Encontrado en el corpus."}

        # Sugerencias por similitud sobre lexico (espanol principal)
        sug = []
        for row in self.rows:
            if row.get("record_type") != "lexico":
                continue
            es = str(row.get("espanol", "") or "")
            if len(es) < 2:
                continue
            esn = normalize_text(es)
            ny = str(row.get("nasa_yuwe", "") or "")
            d = min(_lev_distance(ql, esn), _lev_distance(ql, normalize_text(ny)))
            if len(ql) <= 3 and d <= 2:
                sug.append({"label": es, "distance": d, "espanol": row.get("espanol", ""), "nasa_yuwe": row.get("nasa_yuwe", "")})
            elif len(ql) <= 6 and d <= 3:
                sug.append({"label": es, "distance": d, "espanol": row.get("espanol", ""), "nasa_yuwe": row.get("nasa_yuwe", "")})
            elif d <= 4 and len(esn) <= 12:
                sug.append({"label": es, "distance": d, "espanol": row.get("espanol", ""), "nasa_yuwe": row.get("nasa_yuwe", "")})

        sug.sort(key=lambda x: x["distance"])
        top = []
        seen = set()
        for s in sug:
            k = normalize_text(s["espanol"])
            if k in seen:
                continue
            seen.add(k)
            top.append({"espanol": s["espanol"], "nasa_yuwe": s["nasa_yuwe"]})
            if len(top) >= 8:
                break

        return {
            "found": None,
            "alternatives": [],
            "suggestions": top,
            "message": "La palabra no se encuentra.",
        }

    def activity(self, category: str, limit: int = 5, difficulty: str = "intermedio", mode: str = "quiz"):
        cat_norm = normalize_text(category)
        if not cat_norm or not self._has_category(cat_norm):
            return {
                "category": cat_norm,
                "questions": [],
                "message": "Categoria no disponible para actividad.",
                "mode": mode,
                "difficulty": difficulty,
            }

        diff = normalize_text(difficulty) or "intermedio"
        if diff not in ("facil", "intermedio", "avanzado"):
            diff = "intermedio"
        act_mode = normalize_text(mode).replace(" ", "_") or "quiz"
        if act_mode not in ("quiz", "completar", "imagen"):
            act_mode = "quiz"

        num_opts = 3 if diff == "facil" else 4
        n_distractors = max(1, num_opts - 1)

        lex_rows = []
        for doc_id in self._doc_ids_for_category(cat_norm):
            row = self.rows[doc_id]
            if row["record_type"] == "lexico":
                lex_rows.append(row)

        # Una fila por glosa Nasa (normalizada): evita opciones repetidas en el mismo quiz
        # y fallos en el cliente (keys duplicadas / misma etiqueta dos veces).
        _seen_ny: set[str] = set()
        _uniq_lex: list = []
        for row in lex_rows:
            ny_raw = (row.get("nasa_yuwe") or "").strip()
            if not ny_raw:
                continue
            nk = normalize_text(ny_raw)
            if nk in _seen_ny:
                continue
            _seen_ny.add(nk)
            _uniq_lex.append(row)
        lex_rows = _uniq_lex

        if len(lex_rows) < max(4, num_opts):
            return {
                "category": cat_norm,
                "questions": [],
                "message": "No hay suficientes terminos para actividad.",
                "mode": act_mode,
                "difficulty": diff,
            }

        ny_index = _lexicon_ny_index(lex_rows)
        random.shuffle(lex_rows)
        cap = max(limit, num_opts + 1)

        if act_mode == "imagen":
            lex_img_rows = [
                r
                for r in lex_rows
                if _term_local_image_url(
                    str(r.get("id") or ""),
                    str(r.get("espanol") or ""),
                    str(r.get("categoria") or cat_norm),
                )
            ]
            if len(lex_img_rows) < 2:
                return {
                    "category": cat_norm,
                    "questions": [],
                    "message": "No hay suficientes terminos con ilustracion en esta categoria.",
                    "mode": act_mode,
                    "difficulty": diff,
                }
            random.shuffle(lex_img_rows)
            base = lex_img_rows[: max(cap, 5)]
        elif act_mode == "quiz":
            lex_quiz_rows = [
                r
                for r in lex_rows
                if _term_local_image_url(
                    str(r.get("id") or ""),
                    str(r.get("espanol") or ""),
                    str(r.get("categoria") or cat_norm),
                )
            ]
            random.shuffle(lex_quiz_rows if len(lex_quiz_rows) >= 2 else lex_rows)
            base = (lex_quiz_rows if len(lex_quiz_rows) >= 2 else lex_rows)[: max(cap, 5)]
        else:
            base = lex_rows[: max(cap, 5)]

        all_answers = [(r.get("nasa_yuwe") or "").strip() for r in lex_rows if (r.get("nasa_yuwe") or "").strip()]
        questions = []
        qid = 1
        for row in base[:limit]:
            answer = (row.get("nasa_yuwe") or "").strip()
            es = (row.get("espanol", "") or "").strip()
            if not answer:
                continue
            ans_key = normalize_text(answer)
            distractors = [x for x in all_answers if x and normalize_text(x) != ans_key]
            random.shuffle(distractors)
            if diff == "avanzado" and len(answer) > 2:
                ln = len(answer)
                closer = [x for x in distractors if abs(len(x) - ln) <= 2]
                pool = closer if len(closer) >= n_distractors else distractors
            else:
                pool = distractors
            picks = pool[:n_distractors]
            # Opciones unicas: respuesta + distractores sin repetir (ni duplicar la correcta)
            opt_seen: set[str] = {ans_key}
            opt_out: list[str] = [answer]
            for o in picks:
                s = (o or "").strip()
                if not s:
                    continue
                k = normalize_text(s)
                if k in opt_seen:
                    continue
                opt_seen.add(k)
                opt_out.append(s)
                if len(opt_out) >= num_opts:
                    break
            if len(opt_out) < 2:
                continue
            options = list(opt_out)
            random.shuffle(options)
            opts_final = options[:num_opts]

            if act_mode == "quiz":
                img_url = _term_local_image_url(
                    str(row.get("id") or ""),
                    es,
                    str(row.get("categoria") or cat_norm),
                )
                if img_url:
                    prompt = f"¿Cuál palabra en Nasa Yuwe corresponde mejor a «{es}»?"
                else:
                    prompt = f"Selecciona la traducción en Nasa Yuwe para: «{es}»"
                q = {
                    "id": f"{cat_norm}-{qid}",
                    "type": "quiz",
                    "prompt": prompt,
                    "answer": answer,
                    "options": opts_final,
                    "options_style": "text_only",
                    "categoria": cat_norm,
                    "espanol": es,
                    "image_url": img_url,
                    "image_ok": bool(img_url),
                }
            elif act_mode == "completar":
                prompt = f"Completa: la expresión en Nasa Yuwe para «{es}» es _____"
                q = {
                    "id": f"{cat_norm}-c-{qid}",
                    "type": "completar",
                    "prompt": prompt,
                    "answer": answer,
                    "options": opts_final,
                    "options_style": "text_only",
                    "categoria": cat_norm,
                    "espanol": es,
                }
            else:
                img_url = _term_local_image_url(
                    str(row.get("id") or ""),
                    es,
                    str(row.get("categoria") or cat_norm),
                )
                if not img_url:
                    continue
                q = {
                    "id": f"{cat_norm}-i-{qid}",
                    "type": "imagen",
                    "prompt": "Une la imagen con la palabra correcta en Nasa Yuwe.",
                    "answer": answer,
                    "options": opts_final,
                    "options_style": "text_only",
                    "hide_espanol_cue": True,
                    "categoria": cat_norm,
                    "espanol": es,
                    "image_url": img_url,
                    "image_ok": True,
                    "image_source": "corpus_solo",
                }
            questions.append(q)
            qid += 1

        self.metrics["activities"] += 1
        return {
            "category": cat_norm,
            "questions": questions,
            "message": "Actividad generada correctamente.",
            "mode": act_mode,
            "difficulty": diff,
        }

    def dialogues(self, category: str = "", limit: int = 6):
        cat_norm = normalize_text(category)
        if cat_norm and not self._has_category(cat_norm):
            return {
                "category": cat_norm,
                "dialogues": [],
                "message": "Categoria no disponible para dialogos.",
            }
        if not cat_norm:
            source_ids = range(len(self.rows))
        else:
            source_ids = self._doc_ids_for_category(cat_norm)
        items = []
        for doc_id in source_ids:
            row = self.rows[doc_id]
            if row["record_type"] != "dialogo":
                continue
            items.append(
                {
                    "id": row["id"],
                    "nasa_yuwe": row["nasa_yuwe"],
                    "espanol": row["espanol"],
                    "categoria": row["categoria"],
                    "fuente_nombre": row["fuente_nombre"],
                    "source_kind": row.get("source_kind", ""),
                    "nivel_confianza": row.get("nivel_confianza", ""),
                }
            )
            if len(items) >= limit:
                break
        self.metrics["dialogues"] += 1
        return {
            "category": cat_norm,
            "dialogues": items,
            "message": "Dialogos pedagogicos generados desde el corpus trazable.",
        }

    def stats(self):
        cat_dist = {k: len(v) for k, v in self.by_category.items()}
        record_types = Counter(r["record_type"] for r in self.rows)
        source_kinds = Counter(r.get("source_kind", "") for r in self.rows)
        return {
            "corpus_entries": len(self.rows),
            "categories": len(self.by_category.keys()),
            "category_distribution": cat_dist,
            "record_types": dict(record_types),
            "source_kinds": dict(source_kinds),
            "metrics": dict(self.metrics),
            "optimizer": "idf_overlap + mmr + ttl_cache + lexical_priority + pedagogical_dialogue_boost",
            "model": {
                "name": self.model.get("model_name", "runtime"),
                "type": self.model.get("model_type", "runtime_idf"),
                "training_rows": self.model.get("training_rows", 0),
                "vocabulary_size": self.model.get("vocabulary_size", 0),
            },
        }


# --- Autenticacion (SQLite + sesiones + Google ID token) ---------------------------------


def normalize_email(value) -> str:
    return (value or "").strip().lower()


def init_auth_db() -> None:
    if USE_POSTGRES:
        auth_migrate_tables()
        auth_seed_demo_users()
        print("[AVI] Base de datos: PostgreSQL (DATABASE_URL / Supabase).")
        return
    AUTH_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = connect_auth()
    try:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL COLLATE NOCASE UNIQUE,
                password_hash TEXT,
                google_sub TEXT UNIQUE,
                display_name TEXT NOT NULL,
                role TEXT NOT NULL,
                created_at REAL NOT NULL,
                active INTEGER NOT NULL DEFAULT 1,
                email_verified INTEGER NOT NULL DEFAULT 1
            );
            CREATE TABLE IF NOT EXISTS sessions (
                token TEXT PRIMARY KEY,
                user_id INTEGER NOT NULL,
                created_at REAL NOT NULL,
                expires_at REAL NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            );
            CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id);
            CREATE INDEX IF NOT EXISTS idx_sessions_exp ON sessions(expires_at);
            """
        )
        conn.commit()
    finally:
        conn.close()
    auth_migrate_tables()
    auth_seed_demo_users()


def auth_migrate_tables() -> None:
    """Tablas nuevas y columnas sobre DB existente (SQLite). En Postgres el esquema viene de supabase/migrations/."""
    if USE_POSTGRES:
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                conn.execute("SELECT 1")
                conn.commit()
            finally:
                conn.close()
        return
    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS password_resets (
                    email TEXT PRIMARY KEY COLLATE NOCASE,
                    code TEXT NOT NULL,
                    expires_at REAL NOT NULL,
                    created_at REAL NOT NULL
                );
                CREATE TABLE IF NOT EXISTS teacher_groups (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    teacher_user_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    education_level TEXT,
                    grade TEXT,
                    difficulty_default TEXT,
                    created_at REAL NOT NULL,
                    FOREIGN KEY (teacher_user_id) REFERENCES users(id)
                );
                CREATE TABLE IF NOT EXISTS group_members (
                    group_id INTEGER NOT NULL,
                    student_user_id INTEGER NOT NULL,
                    assigned_at REAL NOT NULL,
                    PRIMARY KEY (group_id, student_user_id),
                    FOREIGN KEY (group_id) REFERENCES teacher_groups(id),
                    FOREIGN KEY (student_user_id) REFERENCES users(id)
                );
                CREATE TABLE IF NOT EXISTS cms_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    kind TEXT NOT NULL,
                    title TEXT NOT NULL,
                    body TEXT NOT NULL,
                    updated_at REAL NOT NULL,
                    status TEXT NOT NULL DEFAULT 'published'
                );
                CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    level TEXT NOT NULL DEFAULT 'General',
                    active INTEGER NOT NULL DEFAULT 1,
                    created_at REAL NOT NULL
                );
                CREATE TABLE IF NOT EXISTS student_grades (
                    student_user_id INTEGER PRIMARY KEY,
                    grade_id INTEGER NOT NULL,
                    assigned_at REAL NOT NULL,
                    FOREIGN KEY (student_user_id) REFERENCES users(id),
                    FOREIGN KEY (grade_id) REFERENCES grades(id)
                );
                CREATE TABLE IF NOT EXISTS student_settings (
                    student_user_id INTEGER PRIMARY KEY,
                    language TEXT NOT NULL DEFAULT 'Espanol',
                    theme TEXT NOT NULL DEFAULT 'Claro Nasa',
                    level TEXT NOT NULL DEFAULT 'Intermedio',
                    goal TEXT NOT NULL DEFAULT 'Conversacion fluida',
                    reminders INTEGER NOT NULL DEFAULT 1,
                    notif_daily INTEGER NOT NULL DEFAULT 1,
                    notif_content INTEGER NOT NULL DEFAULT 1,
                    notif_streak INTEGER NOT NULL DEFAULT 1,
                    notif_tips INTEGER NOT NULL DEFAULT 0,
                    consent_given INTEGER NOT NULL DEFAULT 1,
                    updated_at REAL NOT NULL DEFAULT 0,
                    vocab_diary_json TEXT NOT NULL DEFAULT '{}',
                    dictionary_categories_json TEXT NOT NULL DEFAULT '[]',
                    streak_current INTEGER NOT NULL DEFAULT 0,
                    streak_last_active_ymd TEXT,
                    avi_chat_json TEXT NOT NULL DEFAULT '[]',
                    FOREIGN KEY (student_user_id) REFERENCES users(id)
                );
                CREATE TABLE IF NOT EXISTS learning_activities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    category TEXT NOT NULL,
                    difficulty TEXT NOT NULL,
                    mode TEXT NOT NULL,
                    creator_user_id INTEGER NOT NULL,
                    creator_role TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'active',
                    created_at REAL NOT NULL,
                    updated_at REAL NOT NULL,
                    FOREIGN KEY (creator_user_id) REFERENCES users(id)
                );
                CREATE TABLE IF NOT EXISTS activity_assignments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    activity_id INTEGER NOT NULL,
                    grade_id INTEGER,
                    group_id INTEGER,
                    student_user_id INTEGER,
                    assigned_by_user_id INTEGER NOT NULL,
                    assigned_at REAL NOT NULL,
                    FOREIGN KEY (activity_id) REFERENCES learning_activities(id),
                    FOREIGN KEY (grade_id) REFERENCES grades(id),
                    FOREIGN KEY (group_id) REFERENCES teacher_groups(id),
                    FOREIGN KEY (student_user_id) REFERENCES users(id)
                );
                CREATE TABLE IF NOT EXISTS content_submissions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    teacher_user_id INTEGER NOT NULL,
                    kind TEXT NOT NULL,
                    title TEXT NOT NULL,
                    espanol TEXT,
                    nasa_yuwe TEXT,
                    translation TEXT,
                    image_url TEXT,
                    audio_url TEXT,
                    notes TEXT,
                    status TEXT NOT NULL DEFAULT 'pending',
                    review_notes TEXT,
                    reviewed_by_user_id INTEGER,
                    created_at REAL NOT NULL,
                    reviewed_at REAL,
                    FOREIGN KEY (teacher_user_id) REFERENCES users(id),
                    FOREIGN KEY (reviewed_by_user_id) REFERENCES users(id)
                );
                CREATE TABLE IF NOT EXISTS admin_audit_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at REAL NOT NULL,
                    actor_user_id INTEGER,
                    actor_name TEXT NOT NULL,
                    action TEXT NOT NULL,
                    detail TEXT NOT NULL DEFAULT ''
                );
                CREATE TABLE IF NOT EXISTS admin_mail_messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at REAL NOT NULL,
                    subject TEXT NOT NULL,
                    body TEXT NOT NULL DEFAULT '',
                    audience TEXT NOT NULL DEFAULT 'all',
                    state TEXT NOT NULL DEFAULT 'Entregado'
                );
                CREATE TABLE IF NOT EXISTS admin_support_tickets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at REAL NOT NULL,
                    topic TEXT NOT NULL,
                    requester_name TEXT NOT NULL DEFAULT '',
                    requester_email TEXT,
                    priority TEXT NOT NULL DEFAULT 'Media',
                    state TEXT NOT NULL DEFAULT 'Abierto',
                    created_by_user_id INTEGER
                );
                CREATE TABLE IF NOT EXISTS user_app_state (
                    user_id INTEGER NOT NULL,
                    namespace TEXT NOT NULL,
                    payload TEXT NOT NULL DEFAULT '{}',
                    updated_at REAL NOT NULL,
                    PRIMARY KEY (user_id, namespace),
                    FOREIGN KEY (user_id) REFERENCES users(id)
                );
                CREATE INDEX IF NOT EXISTS idx_audit_created ON admin_audit_log(created_at);
                CREATE INDEX IF NOT EXISTS idx_groups_teacher ON teacher_groups(teacher_user_id);
                CREATE INDEX IF NOT EXISTS idx_members_student ON group_members(student_user_id);
                CREATE INDEX IF NOT EXISTS idx_student_grades_grade ON student_grades(grade_id);
                CREATE INDEX IF NOT EXISTS idx_activities_creator ON learning_activities(creator_user_id);
                CREATE INDEX IF NOT EXISTS idx_activity_assignments_activity ON activity_assignments(activity_id);
                CREATE INDEX IF NOT EXISTS idx_activity_assignments_grade ON activity_assignments(grade_id);
                CREATE INDEX IF NOT EXISTS idx_activity_assignments_group ON activity_assignments(group_id);
                CREATE INDEX IF NOT EXISTS idx_content_submissions_status ON content_submissions(status);
                """
            )
            cols = {r[1] for r in conn.execute("PRAGMA table_info(users)").fetchall()}
            if "active" not in cols:
                conn.execute("ALTER TABLE users ADD COLUMN active INTEGER NOT NULL DEFAULT 1")
            if "email_verified" not in cols:
                conn.execute("ALTER TABLE users ADD COLUMN email_verified INTEGER NOT NULL DEFAULT 1")
            gcols = {r[1] for r in conn.execute("PRAGMA table_info(teacher_groups)").fetchall()}
            if "grade_id" not in gcols:
                conn.execute("ALTER TABLE teacher_groups ADD COLUMN grade_id INTEGER")
            cms_cols = {r[1] for r in conn.execute("PRAGMA table_info(cms_items)").fetchall()}
            if "status" not in cms_cols:
                conn.execute("ALTER TABLE cms_items ADD COLUMN status TEXT NOT NULL DEFAULT 'published'")
            scols = {r[1] for r in conn.execute("PRAGMA table_info(student_settings)").fetchall()}
            for col, decl in (
                ("vocab_diary_json", "TEXT NOT NULL DEFAULT '{}'"),
                ("dictionary_categories_json", "TEXT NOT NULL DEFAULT '[]'"),
                ("streak_current", "INTEGER NOT NULL DEFAULT 0"),
                ("streak_last_active_ymd", "TEXT"),
                ("avi_chat_json", "TEXT NOT NULL DEFAULT '[]'"),
            ):
                if col not in scols:
                    conn.execute(f"ALTER TABLE student_settings ADD COLUMN {col} {decl}")
            conn.commit()
        finally:
            conn.close()


def auth_write_demo_credentials_file() -> None:
    """Referencias en texto plano junto al proyecto (contraseña demo fija)."""
    path = AUTH_DB_PATH.parent / "CUENTAS_PRUEBA.txt"
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "NASA Yuwe / AVI — cuentas de prueba para entrar directo\n\n",
            "SI VES \"Error 501\" al iniciar sesion:\n",
            "  No uses Live Server, ni abrir solo frontend/dist/index.html,\n",
            "  ni python -m http.server (no aceptan POST /api).\n",
            "  Desde la carpeta avi_webapp ejecuta:  python server.py\n",
            "  y abre en el navegador:  http://127.0.0.1:8090/\n\n",
            f"Contraseña para las cuentas base (estudiante / docente / admin): {DEMO_LOGIN_PASSWORD}\n\n",
        ]
        for email, _dn, role in DEMO_ACCOUNTS:
            lines.append(f"  {email}  ({role})\n")
        lines.append(
            "\nSe crean solas la primera vez que inicias server.py "
            "(excepto si AVI_SKIP_DEMO_USERS=1).\n",
        )
        lines.append("\n--- Docentes con panel lleno (grupos, alumnos, actividades) ---\n")
        lines.append(f"Contraseña (las 3 cuentas docente): {DEMO_TEACHER_PANEL_PASSWORD}\n")
        for email, dn, role in DEMO_TEACHER_PANEL_ACCOUNTS:
            lines.append(f"  {email}  ({dn}, {role})\n")
        lines.append(
            f"\nAlumnos solo para esos grupos (contraseña {DEMO_LOGIN_PASSWORD}, "
            "misma que estudiante.demo):\n",
        )
        for email, dn in DEMO_PANEL_STUDENTS:
            lines.append(f"  {email}  ({dn})\n")
        lines.append(
            "\nLos datos de grupos/actividades se insertan al arrancar el servidor "
            "(una vez por docente, si aún no tenían actividades semilla).\n",
        )
        path.write_text("".join(lines), encoding="utf-8")
    except OSError:
        pass


def _ensure_seed_grade(conn, now: float) -> int:
    row = conn.execute("SELECT id FROM grades WHERE active = 1 ORDER BY id LIMIT 1").fetchone()
    if row:
        return int(row["id"])
    return insert_returning_id(
        conn,
        "INSERT INTO grades (name, level, active, created_at) VALUES (?, ?, 1, ?)",
        ("Grado institucional (semilla AVI)", "General", now),
    )


def auth_seed_teacher_panel_demo_data(conn, now: float) -> int:
    """Grupos, alumnos panel, actividades y asignaciones para DEMO_TEACHER_PANEL_ACCOUNTS."""
    seeded_teachers = 0
    panel_ids: list[int] = []
    for em, _ in DEMO_PANEL_STUDENTS:
        norm = normalize_email(em)
        r = conn.execute("SELECT id FROM users WHERE email = ?", (norm,)).fetchone()
        if r:
            panel_ids.append(int(r["id"]))
    available = [
        sid
        for sid in panel_ids
        if not conn.execute("SELECT 1 FROM group_members WHERE student_user_id = ?", (sid,)).fetchone()
    ]
    next_free = 0

    def take_students(n: int) -> list[int]:
        nonlocal next_free
        out: list[int] = []
        while len(out) < n and next_free < len(available):
            sid = available[next_free]
            next_free += 1
            out.append(sid)
        return out

    grade_id = _ensure_seed_grade(conn, now)
    grow = conn.execute("SELECT name FROM grades WHERE id = ?", (grade_id,)).fetchone()
    grade_label = (grow["name"] if grow else None) or "General"

    for em, display_name, _role in DEMO_TEACHER_PANEL_ACCOUNTS:
        norm = normalize_email(em)
        ur = conn.execute("SELECT id FROM users WHERE email = ?", (norm,)).fetchone()
        if not ur:
            continue
        tid = int(ur["id"])
        if conn.execute(
            "SELECT 1 FROM learning_activities WHERE creator_user_id = ? AND description LIKE ?",
            (tid, "Datos semilla AVI%"),
        ).fetchone():
            continue

        tag = (display_name.split()[0] if display_name else "Docente").strip() or "Docente"
        g1 = insert_returning_id(
            conn,
            """
            INSERT INTO teacher_groups (
                teacher_user_id, name, education_level, grade, grade_id, difficulty_default, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                tid,
                f"Intercultural A — {tag} (semilla AVI)",
                "Primaria",
                grade_label,
                grade_id,
                "intermedio",
                now - 86400 * 40,
            ),
        )
        g2 = insert_returning_id(
            conn,
            """
            INSERT INTO teacher_groups (
                teacher_user_id, name, education_level, grade, grade_id, difficulty_default, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                tid,
                f"Lengua viva B — {tag} (semilla AVI)",
                "Primaria",
                grade_label,
                grade_id,
                "intermedio",
                now - 86400 * 34,
            ),
        )

        for sid in take_students(2):
            conn.execute(
                "INSERT OR IGNORE INTO group_members (group_id, student_user_id, assigned_at) VALUES (?, ?, ?)",
                (g1, sid, now - 86400 * 30),
            )
        for sid in take_students(2):
            conn.execute(
                "INSERT OR IGNORE INTO group_members (group_id, student_user_id, assigned_at) VALUES (?, ?, ?)",
                (g2, sid, now - 86400 * 28),
            )

        def insert_activity(
            title: str,
            category: str,
            mode: str,
            status: str,
            days_ago_created: float,
            group_assignments: list[tuple[int, float]],
        ) -> None:
            c_at = now - 86400 * days_ago_created
            desc = f"{TEACHER_PANEL_SEED_DESC_MARKER} Actividad: {title}."
            aid = insert_returning_id(
                conn,
                """
                INSERT INTO learning_activities (
                    title, description, category, difficulty, mode, creator_user_id, creator_role, status, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, 'docente', ?, ?, ?)
                """,
                (title, desc, category, "intermedio", mode, tid, status, c_at, c_at),
            )
            for gid, days_a in group_assignments:
                conn.execute(
                    """
                    INSERT INTO activity_assignments (
                        activity_id, grade_id, group_id, student_user_id, assigned_by_user_id, assigned_at
                    ) VALUES (?, NULL, ?, NULL, ?, ?)
                    """,
                    (aid, gid, tid, now - 86400 * days_a),
                )

        insert_activity("Saludos en contexto escolar", "saludos", "quiz", "active", 6.0, [(g1, 4.0)])
        insert_activity("Familia y parentesco", "familia", "completar", "active", 9.0, [(g1, 7.0)])
        insert_activity("Numeros del 1 al 20", "numeros", "quiz", "draft", 14.0, [])
        insert_activity("Frutas de nuestra tierra", "comida", "imagen", "active", 4.0, [(g2, 3.0)])
        insert_activity("Expresiones de cortesia", "expresiones", "leccion", "scheduled", 11.0, [(g2, 10.0)])
        insert_activity("Animales del entorno", "animales", "quiz", "active", 2.0, [(g1, 1.0), (g2, 1.0)])

        if not conn.execute(
            "SELECT 1 FROM content_submissions WHERE teacher_user_id = ? AND notes LIKE ?",
            (tid, "%semilla AVI propuesta%"),
        ).fetchone():
            conn.execute(
                """
                INSERT INTO content_submissions (
                    teacher_user_id, kind, title, espanol, nasa_yuwe, translation,
                    image_url, audio_url, notes, status, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, '', '', ?, 'pending', ?)
                """,
                (
                    tid,
                    "termino",
                    f"Semilla AVI: kimus (color) — {tag}",
                    "color",
                    "kimus",
                    "",
                    "Propuesta generada en semilla AVI propuesta (demo)",
                    now - 3600,
                ),
            )

        seeded_teachers += 1
    return seeded_teachers


def auth_seed_demo_users() -> None:
    if os.environ.get("AVI_SKIP_DEMO_USERS", "").strip().lower() in ("1", "true", "yes"):
        return
    auth_write_demo_credentials_file()
    now = time.time()
    created: list[str] = []
    panel_seeded = 0
    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            for email, display_name, role in DEMO_ACCOUNTS:
                norm = normalize_email(email)
                if conn.execute("SELECT 1 FROM users WHERE email = ?", (norm,)).fetchone():
                    continue
                ph = auth_hash_password(DEMO_LOGIN_PASSWORD)
                conn.execute(
                    """
                    INSERT INTO users (
                        email, password_hash, google_sub, display_name, role, created_at, active, email_verified
                    ) VALUES (?, ?, NULL, ?, ?, ?, 1, 1)
                    """,
                    (norm, ph, display_name, role, now),
                )
                created.append(norm)
            ph_stu = auth_hash_password(DEMO_LOGIN_PASSWORD)
            for email, display_name in DEMO_PANEL_STUDENTS:
                norm = normalize_email(email)
                if conn.execute("SELECT 1 FROM users WHERE email = ?", (norm,)).fetchone():
                    continue
                conn.execute(
                    """
                    INSERT INTO users (
                        email, password_hash, google_sub, display_name, role, created_at, active, email_verified
                    ) VALUES (?, ?, NULL, ?, 'estudiante', ?, 1, 1)
                    """,
                    (norm, ph_stu, display_name, now),
                )
                created.append(norm)
            ph_doc_panel = auth_hash_password(DEMO_TEACHER_PANEL_PASSWORD)
            for email, display_name, role in DEMO_TEACHER_PANEL_ACCOUNTS:
                norm = normalize_email(email)
                if conn.execute("SELECT 1 FROM users WHERE email = ?", (norm,)).fetchone():
                    continue
                conn.execute(
                    """
                    INSERT INTO users (
                        email, password_hash, google_sub, display_name, role, created_at, active, email_verified
                    ) VALUES (?, ?, NULL, ?, ?, ?, 1, 1)
                    """,
                    (norm, ph_doc_panel, display_name, role, now),
                )
                created.append(norm)
            panel_seeded = auth_seed_teacher_panel_demo_data(conn, now)
            conn.commit()
        finally:
            conn.close()
    if created:
        print(
            f"[AVI] Creadas o actualizadas cuentas de prueba ({len(created)} altas nuevas). "
            f"Cuentas base: {DEMO_LOGIN_PASSWORD} — docentes panel: {DEMO_TEACHER_PANEL_PASSWORD} — "
            f"ver {AUTH_DB_PATH.parent / 'CUENTAS_PRUEBA.txt'}",
        )
    if panel_seeded:
        print(f"[AVI] Semilla panel docente aplicada a {panel_seeded} docente(s) con grupos y actividades.")


def auth_connect():
    return connect_auth()


def auth_hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    dk = hashlib.scrypt(password.encode("utf-8"), salt=salt.encode("ascii"), n=2**14, r=8, p=1, dklen=32)
    return f"scrypt|{salt}|{dk.hex()}"


def auth_verify_password(password: str, stored: str) -> bool:
    try:
        parts = (stored or "").split("|")
        if len(parts) != 3 or parts[0] != "scrypt":
            return False
        salt, hexdigest = parts[1], parts[2]
        dk = hashlib.scrypt(password.encode("utf-8"), salt=salt.encode("ascii"), n=2**14, r=8, p=1, dklen=32)
        return dk.hex() == hexdigest
    except Exception:
        return False


def auth_password_policy_violation(pw: str) -> str | None:
    """None si cumple la política; mensaje corto si no."""
    if not isinstance(pw, str) or len(pw) < 10:
        return "La contrasena debe tener al menos 10 caracteres."
    if len(pw) > 256:
        return "La contrasena es demasiado larga."
    if not any(c.islower() for c in pw):
        return "Incluye al menos una letra minuscula."
    if not any(c.isupper() for c in pw):
        return "Incluye al menos una letra mayuscula."
    if not any(c.isdigit() for c in pw):
        return "Incluye al menos un numero."
    _spec = set("!@#$%^&*()_+-=[]{};:\\'\",.<>?/\\|`~")
    if not any(c in _spec for c in pw):
        return "Incluye al menos un simbolo (por ejemplo ! @ # ...)."
    return None


def auth_row_to_user(row):
    if not row:
        return None
    d = {k: row[k] for k in row.keys()}
    return {
        "id": d["id"],
        "email": d["email"],
        "display_name": d["display_name"],
        "role": d["role"],
        "active": bool(int(d.get("active", 1) or 1)),
        "email_verified": bool(int(d.get("email_verified", 1) or 1)),
    }


def auth_prune_expired_sessions(conn):
    conn.execute("DELETE FROM sessions WHERE expires_at <= ?", (time.time(),))


def auth_create_session(conn, user_id: int) -> str:
    auth_prune_expired_sessions(conn)
    token = secrets.token_urlsafe(32)
    now = time.time()
    conn.execute(
        "INSERT INTO sessions (token, user_id, created_at, expires_at) VALUES (?, ?, ?, ?)",
        (token, user_id, now, now + SESSION_TTL_SEC),
    )
    conn.commit()
    return token


def auth_get_session_token(handler):
    auth = handler.headers.get("Authorization") or ""
    if auth.lower().startswith("bearer "):
        return auth[7:].strip() or None
    return None


def auth_resolve_user(handler, touch: bool = True):
    tok = auth_get_session_token(handler)
    if not tok:
        return None, None
    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            auth_prune_expired_sessions(conn)
            now = time.time()
            row = conn.execute(
                """
                SELECT u.id, u.email, u.display_name, u.role,
                       COALESCE(u.active, 1) AS active,
                       COALESCE(u.email_verified, 1) AS email_verified
                FROM sessions s
                JOIN users u ON u.id = s.user_id
                WHERE s.token = ? AND s.expires_at > ?
                """,
                (tok, now),
            ).fetchone()
            if not row:
                return tok, None
            user = auth_row_to_user(row)
            if user and not user.get("active"):
                conn.execute("DELETE FROM sessions WHERE token = ?", (tok,))
                conn.commit()
                return tok, None
            if touch:
                sr = conn.execute("SELECT created_at FROM sessions WHERE token = ?", (tok,)).fetchone()
                if sr:
                    cap = sr["created_at"] + SESSION_TTL_SEC
                    new_exp = min(now + SESSION_IDLE_SEC, cap)
                    conn.execute(
                        "UPDATE sessions SET expires_at = ? WHERE token = ?",
                        (new_exp, tok),
                    )
                    conn.commit()
            return tok, user
        finally:
            conn.close()


def auth_verify_google_token(credential: str) -> dict:
    if not GOOGLE_CLIENT_ID:
        raise ValueError("Falta GOOGLE_CLIENT_ID en el servidor.")
    try:
        from google.oauth2 import id_token
        from google.auth.transport import requests as grequests
    except ImportError as exc:
        raise ValueError("Instala google-auth en el servidor: pip install google-auth") from exc
    info = id_token.verify_oauth2_token(credential, grequests.Request(), GOOGLE_CLIENT_ID)
    iss = info.get("iss")
    if iss not in ("accounts.google.com", "https://accounts.google.com"):
        raise ValueError("Emisor del token no valido.")
    return info


def auth_json_body(handler) -> dict:
    length = int(handler.headers.get("Content-Length", "0") or "0")
    raw = handler.rfile.read(length) if length > 0 else b"{}"
    try:
        return json.loads(raw.decode("utf-8"))
    except json.JSONDecodeError:
        return {}


api_read_json = auth_json_body


def admin_audit_fmt_when(ts: float) -> str:
    """Formato español corto para el panel web."""
    try:
        return datetime.fromtimestamp(ts).strftime("%d/%m/%Y %H:%M")
    except (OSError, OverflowError, ValueError):
        return "—"


def admin_audit_insert(conn, actor: dict, action: str, detail: str) -> None:
    if actor is None:
        actor = {}
    now = time.time()
    name = ((actor.get("display_name") or actor.get("email") or "") or "Admin").strip()
    aid = actor.get("id")
    conn.execute(
        """INSERT INTO admin_audit_log (created_at, actor_user_id, actor_name, action, detail)
           VALUES (?, ?, ?, ?, ?)""",
        (now, aid, name, (action or "EVENT")[:200], (detail or "")[:2500]),
    )


_MAIL_AUDIENCE_KEYS = frozenset({"all", "teachers", "students"})


def _mail_audience_label(key: str) -> str:
    return {
        "all": "Toda la comunidad",
        "teachers": "Solo docentes",
        "students": "Solo estudiantes",
    }.get(key, key or "Destinatarios")


def _cors_allow_origin(handler) -> str | None:
    """Valor para Access-Control-Allow-Origin. None = origen no permitido (lista AVI_CORS_ORIGINS)."""
    if not CORS_ALLOWED_ORIGINS:
        return "*"
    origin = (handler.headers.get("Origin") or "").strip()
    if not origin:
        return "*"
    if origin in CORS_ALLOWED_ORIGINS:
        return origin
    return None


def auth_rate_allow(handler) -> tuple[bool, str | None]:
    """Limita intentos de auth por IP (ventana deslizante)."""
    ip = handler.client_address[0]
    now = time.time()
    with _AUTH_RL_LOCK:
        bucket = _AUTH_RL_BUCKETS.setdefault(ip, [])
        cutoff = now - AUTH_RL_WINDOW_SEC
        while bucket and bucket[0] < cutoff:
            bucket.pop(0)
        if len(bucket) >= AUTH_RL_MAX:
            return False, "Demasiados intentos desde esta red. Espera unos minutos e intentalo de nuevo."
        bucket.append(now)
    return True, None


def auth_handle_register(handler, data: dict):
    email = normalize_email(data.get("email"))
    password = data.get("password") or ""
    password_confirm = data.get("password_confirm") or ""
    display_name = (data.get("display_name") or "").strip()
    role = (data.get("role") or "").strip().lower()

    dn = display_name.replace("\u00a0", " ").strip()
    if not dn or not email or not password or not password_confirm:
        return {"error": "Los campos están vacíos, por favor ingresar los datos correspondientes."}, 400

    if "@" not in email:
        return {"error": "Correo invalido."}, 400
    if len(password) > 256:
        return {"error": "La contraseña es demasiado larga."}, 400
    if len(password_confirm) > 256:
        return {"error": "La contraseña es demasiado larga."}, 400
    if not secrets.compare_digest(password, password_confirm):
        return {"error": "Las contraseña no coincide"}, 400
    pol = auth_password_policy_violation(password)
    if pol:
        return {"error": pol}, 400
    if len(dn) < 2:
        return {"error": "Nombre minimo 2 caracteres."}, 400
    if role not in REGISTER_ROLES:
        return {"error": "En el registro solo se permiten los roles estudiante y docente."}, 400

    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            if conn.execute("SELECT 1 FROM users WHERE email = ?", (email,)).fetchone():
                return {"error": "Ya existe una cuenta con este correo."}, 409
            ph = auth_hash_password(password)
            now = time.time()
            _ = insert_returning_id(
                conn,
                """
                INSERT INTO users (
                    email, password_hash, google_sub, display_name, role, created_at, active, email_verified
                ) VALUES (?, ?, NULL, ?, ?, ?, 1, 1)
                """,
                (email, ph, dn, role, now),
            )
            conn.commit()
        finally:
            conn.close()
    return (
        {
            "message": "Cuenta creada. Inicia sesion con tu correo y contrasena.",
            "email": email,
        },
        201,
    )


def auth_handle_login(handler, data: dict):
    email = normalize_email(data.get("email"))
    password = data.get("password") or ""

    if len(password) > 256:
        return {"error": "La contraseña es demasiado larga."}, 400

    if not email or not password:
        return {"error": "Los campos están vacíos, por favor ingresar los datos correspondientes."}, 400

    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            auth_prune_expired_sessions(conn)
            row = conn.execute(
                """
                SELECT id, email, password_hash, display_name, role,
                       COALESCE(active,1) AS active,
                       COALESCE(email_verified,1) AS email_verified
                FROM users WHERE email = ?
                """,
                (email,),
            ).fetchone()
            if not row:
                return {"error": "El correo electrónico no se encuentra registrado."}, 401
            if not row["active"]:
                return {"error": "Cuenta inactiva. Contacta al administrador."}, 403
            if not row["password_hash"]:
                return {"error": "Esta cuenta usa solo Google. Usa Continuar con Google."}, 401
            if not auth_verify_password(password, row["password_hash"]):
                return {"error": "La contraseña es inválida."}, 401
            tok = auth_create_session(conn, row["id"])
        finally:
            conn.close()

    return {"token": tok, "user": auth_row_to_user(row)}, 200


def auth_handle_google(handler, data: dict):
    credential = (data.get("credential") or "").strip()
    role = (data.get("role") or "").strip().lower()
    if not credential:
        return {"error": "Falta credencial de Google."}, 400

    try:
        info = auth_verify_google_token(credential)
    except ValueError as err:
        return {"error": str(err)}, 401

    google_sub = info.get("sub")
    email = normalize_email(info.get("email"))
    display_name = (info.get("name") or info.get("given_name") or email.split("@")[0] if email else "Usuario").strip()

    if not google_sub or not email:
        return {"error": "Google no entrego email o identificador."}, 400

    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            auth_prune_expired_sessions(conn)
            row = conn.execute("SELECT id, email, google_sub, password_hash, display_name, role FROM users WHERE google_sub = ?", (google_sub,)).fetchone()
            if not row:
                row = conn.execute("SELECT id, email, google_sub, password_hash, display_name, role FROM users WHERE email = ?", (email,)).fetchone()
                if row:
                    if row["google_sub"] and row["google_sub"] != google_sub:
                        return {"error": "Este correo ya esta vinculado a otra cuenta Google."}, 409
                    conn.execute("UPDATE users SET google_sub = ? WHERE id = ?", (google_sub, row["id"]))
                    conn.commit()
                    row = conn.execute(
                        "SELECT id, email, google_sub, password_hash, display_name, role FROM users WHERE id = ?",
                        (row["id"],),
                    ).fetchone()
            if not row:
                if role not in REGISTER_ROLES:
                    return {"error": "Con Google solo puedes registrarte como estudiante o docente."}, 400
                now = time.time()
                uid = insert_returning_id(
                    conn,
                    """
                    INSERT INTO users (
                        email, password_hash, google_sub, display_name, role, created_at, active, email_verified
                    ) VALUES (?, NULL, ?, ?, ?, ?, 1, 1)
                    """,
                    (email, google_sub, display_name, role, now),
                )
                conn.commit()
                row = conn.execute(
                    """
                    SELECT id, email, display_name, role,
                           COALESCE(active,1) AS active,
                           COALESCE(email_verified,1) AS email_verified
                    FROM users WHERE id = ?
                    """,
                    (uid,),
                ).fetchone()
            uid_final = row["id"]
            row = conn.execute(
                """
                SELECT id, email, display_name, role,
                       COALESCE(active, 1) AS active,
                       COALESCE(email_verified, 1) AS email_verified
                FROM users WHERE id = ?
                """,
                (uid_final,),
            ).fetchone()
            if not row["active"]:
                return {"error": "Cuenta inactiva. Contacta al administrador."}, 403
            tok = auth_create_session(conn, row["id"])
        finally:
            conn.close()

    return {"token": tok, "user": auth_row_to_user(row)}, 200


def auth_handle_logout(handler):
    tok = auth_get_session_token(handler)
    if not tok:
        return {"ok": True}, 200
    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            conn.execute("DELETE FROM sessions WHERE token = ?", (tok,))
            conn.commit()
        finally:
            conn.close()
    return {"ok": True}, 200


def api_require_user(handler, roles=None):
    _, user = auth_resolve_user(handler, touch=True)
    if not user:
        return None, {"error": "Sesion invalida o expirada."}, 401
    if roles is not None and user.get("role") not in roles:
        return None, {"error": "No autorizado para esta acción."}, 403
    return user, None, None


def auth_handle_forgot(handler, data: dict):
    email = normalize_email(data.get("email"))
    if not email or "@" not in email:
        return {"error": "Correo electrónico invalido"}, 400
    msg = (
        "Si el correo esta registrado, puedes restablecer la contrasena con el codigo. "
        "En entornos de prueba el codigo tambien aparece en la consola del servidor."
    )
    out: dict = {"message": msg}
    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            row = conn.execute(
                "SELECT id FROM users WHERE email = ? AND COALESCE(active, 1) = 1",
                (email,),
            ).fetchone()
            if not row:
                return out, 200
            code = str(random.randint(100000, 999999))
            now = time.time()
            conn.execute(
                """INSERT OR REPLACE INTO password_resets (email, code, expires_at, created_at)
                   VALUES (?, ?, ?, ?)""",
                (email, code, now + 900, now),
            )
            conn.commit()
        finally:
            conn.close()
    print(f"[AVI recuperacion] {email}: codigo {code} (consola servidor)")
    if os.environ.get("AVI_DEBUG_PASSWORD_RESET", "").strip().lower() in ("1", "true", "yes"):
        out["reset_code"] = code
    return out, 200


def auth_handle_verify_reset(handler, data: dict):
    email = normalize_email(data.get("email"))
    code = (data.get("code") or "").strip()
    if not email or not code:
        return {"error": "Datos incompletos."}, 400
    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            row = conn.execute(
                "SELECT code, expires_at FROM password_resets WHERE email = ?",
                (email,),
            ).fetchone()
            if not row or str(row["code"]) != code or row["expires_at"] <= time.time():
                return {"error": "Código invalido"}, 400
        finally:
            conn.close()
    return {"ok": True}, 200


def auth_handle_reset_password(handler, data: dict):
    email = normalize_email(data.get("email"))
    code = (data.get("code") or "").strip()
    pw = data.get("password") or ""
    pw2 = data.get("password_confirm") or ""
    if not email or not code:
        return {"error": "Datos incompletos."}, 400
    if len(pw) > 256 or len(pw2) > 256:
        return {"error": "La contraseña es demasiado larga."}, 400
    if not secrets.compare_digest(pw, pw2):
        return {"error": "Las contraseña no coincide"}, 400
    pol = auth_password_policy_violation(pw)
    if pol:
        return {"error": pol}, 400
    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            row = conn.execute(
                "SELECT code, expires_at FROM password_resets WHERE email = ?",
                (email,),
            ).fetchone()
            if not row or str(row["code"]) != code or row["expires_at"] <= time.time():
                return {"error": "Código invalido"}, 400
            ph = auth_hash_password(pw)
            conn.execute("UPDATE users SET password_hash = ? WHERE email = ?", (ph, email))
            conn.execute("DELETE FROM password_resets WHERE email = ?", (email,))
            conn.commit()
        finally:
            conn.close()
    return {"message": "Contraseña actualizada"}, 200


ENGINE = CorpusEngine(CORPUS_PATH)


def teacher_handle_post(handler, route: str, data: dict):
    user, err, st_code = api_require_user(handler, {"docente"})
    if err:
        return err, st_code
    teacher_id = user["id"]
    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            if route == "/api/teacher/groups":
                name = (data.get("name") or "").strip()
                if not name:
                    return {"error": "Por favor diligenciar el nombre del grupo"}, 400
                dup = conn.execute(
                    """
                    SELECT id FROM teacher_groups
                    WHERE teacher_user_id = ? AND LOWER(TRIM(name)) = LOWER(?)
                    """,
                    (teacher_id, name),
                ).fetchone()
                if dup:
                    return {"error": "Ya existe un grupo con ese nombre. Elige otro nombre."}, 409
                valid_grades = {
                    "Transición", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
                }
                grade = (data.get("grade") or "").strip()
                if grade and grade not in valid_grades:
                    return {"error": "Grado inválido. Use Transición o grados del 1 al 11."}, 400
                edu = (data.get("education_level") or "").strip()
                if not edu:
                    if grade in ("Transición",):
                        edu = "Preescolar"
                    elif grade in ("1", "2", "3", "4", "5"):
                        edu = "Primaria"
                    elif grade in ("6", "7", "8", "9", "10", "11"):
                        edu = "Secundaria"
                    else:
                        edu = "General"
                grade_id = int(data.get("grade_id", 0) or 0)
                diff = (data.get("difficulty_default") or "intermedio").strip()
                if grade_id > 0:
                    gr = conn.execute(
                        "SELECT id, name FROM grades WHERE id = ? AND active = 1",
                        (grade_id,),
                    ).fetchone()
                    if not gr:
                        return {"error": "Grado no encontrado."}, 404
                    if not grade:
                        grade = gr["name"]
                gid = insert_returning_id(
                    conn,
                    """
                    INSERT INTO teacher_groups (
                        teacher_user_id, name, education_level, grade, grade_id, difficulty_default, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (teacher_id, name, edu, grade, grade_id or None, diff, time.time()),
                )
                conn.commit()
                return {
                    "group": {"id": gid, "name": name, "education_level": edu, "grade": grade, "grade_id": grade_id or None},
                }, 201
            if route == "/api/teacher/group-assign":
                gid = int(data.get("group_id", 0) or 0)
                sids = data.get("student_ids") or []
                if not isinstance(sids, list) or not sids:
                    return {"error": "Debe seleccionar al menos un estudiante"}, 400
                g = conn.execute(
                    "SELECT id FROM teacher_groups WHERE id = ? AND teacher_user_id = ?",
                    (gid, teacher_id),
                ).fetchone()
                if not g:
                    return {"error": "Grupo no encontrado."}, 404
                now = time.time()
                for sid in sids:
                    try:
                        sid = int(sid)
                    except (TypeError, ValueError):
                        continue
                    stu = conn.execute(
                        "SELECT id, role FROM users WHERE id = ? AND COALESCE(active, 1) = 1",
                        (sid,),
                    ).fetchone()
                    if not stu or stu["role"] != "estudiante":
                        continue
                    other = conn.execute(
                        "SELECT group_id FROM group_members WHERE student_user_id = ?",
                        (sid,),
                    ).fetchone()
                    if other:
                        return {"error": "El estudiante ya está asignado a un grupo"}, 409
                    conn.execute(
                        """
                        INSERT OR IGNORE INTO group_members (group_id, student_user_id, assigned_at)
                        VALUES (?, ?, ?)
                        """,
                        (gid, sid, now),
                    )
                conn.commit()
                chk = scalar_from_row(
                    conn.execute(
                        "SELECT COUNT(*) FROM group_members WHERE group_id = ?",
                        (gid,),
                    ).fetchone()
                )
                if chk == 0:
                    return {"error": "Debe seleccionar al menos un estudiante"}, 400
                return {"message": "¡Asignación correcta!", "members": chk}, 200
            if route == "/api/teacher/activities":
                title = (data.get("title") or "").strip()
                description = (data.get("description") or "").strip()
                category = normalize_text(data.get("category") or "comida")
                difficulty = (data.get("difficulty") or "intermedio").strip()
                mode = (data.get("mode") or "quiz").strip()
                grade_id = int(data.get("grade_id", 0) or 0)
                group_id = int(data.get("group_id", 0) or 0)
                student_ids = data.get("student_ids") or []
                if not title:
                    return {"error": "Titulo requerido."}, 400
                if not description:
                    description = title
                raw_st = normalize_text(data.get("status") or data.get("workflow_status") or "active").lower()
                if raw_st in ("borrador", "draft"):
                    wf_status = "draft"
                elif raw_st in ("programada", "scheduled"):
                    wf_status = "scheduled"
                else:
                    wf_status = "active"
                if grade_id:
                    g = conn.execute("SELECT id FROM grades WHERE id = ? AND active = 1", (grade_id,)).fetchone()
                    if not g:
                        return {"error": "Grado inválido."}, 404
                if group_id:
                    g = conn.execute(
                        "SELECT id FROM teacher_groups WHERE id = ? AND teacher_user_id = ?",
                        (group_id, teacher_id),
                    ).fetchone()
                    if not g:
                        return {"error": "Grupo inválido."}, 404
                now = time.time()
                aid = insert_returning_id(
                    conn,
                    """
                    INSERT INTO learning_activities (
                        title, description, category, difficulty, mode, creator_user_id, creator_role, status, created_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, 'docente', ?, ?, ?)
                    """,
                    (title, description, category, difficulty, mode, teacher_id, wf_status, now, now),
                )
                if grade_id or group_id:
                    conn.execute(
                        """
                        INSERT INTO activity_assignments (
                            activity_id, grade_id, group_id, student_user_id, assigned_by_user_id, assigned_at
                        ) VALUES (?, ?, ?, NULL, ?, ?)
                        """,
                        (aid, grade_id or None, group_id or None, teacher_id, now),
                    )
                if isinstance(student_ids, list):
                    for sid in student_ids:
                        try:
                            sid = int(sid)
                        except (TypeError, ValueError):
                            continue
                        conn.execute(
                            """
                            INSERT INTO activity_assignments (
                                activity_id, grade_id, group_id, student_user_id, assigned_by_user_id, assigned_at
                            ) VALUES (?, NULL, NULL, ?, ?, ?)
                            """,
                            (aid, sid, teacher_id, now),
                        )
                conn.commit()
                return {"ok": True, "activity_id": aid}, 201
            if route == "/api/teacher/content-submit":
                kind = (data.get("kind") or "termino").strip()
                title = (data.get("title") or "").strip()
                if not title:
                    return {"error": "Titulo requerido."}, 400
                now = time.time()
                sid = insert_returning_id(
                    conn,
                    """
                    INSERT INTO content_submissions (
                        teacher_user_id, kind, title, espanol, nasa_yuwe, translation,
                        image_url, audio_url, notes, status, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?)
                    """,
                    (
                        teacher_id,
                        kind,
                        title,
                        (data.get("espanol") or "").strip(),
                        (data.get("nasa_yuwe") or "").strip(),
                        (data.get("translation") or "").strip(),
                        (data.get("image_url") or "").strip(),
                        (data.get("audio_url") or "").strip(),
                        (data.get("notes") or "").strip(),
                        now,
                    ),
                )
                conn.commit()
                return {"ok": True, "submission_id": sid, "status": "pending"}, 201
            if route == "/api/teacher/activity-assign":
                aid = int(data.get("activity_id", 0) or 0)
                group_id = int(data.get("group_id", 0) or 0)
                grade_id = int(data.get("grade_id", 0) or 0)
                if not aid:
                    return {"error": "Actividad invalida."}, 400
                if not group_id and not grade_id:
                    return {"error": "Selecciona un grupo o grado institucional."}, 400
                row = conn.execute(
                    """
                    SELECT id FROM learning_activities
                    WHERE id = ? AND creator_user_id = ? AND creator_role = 'docente'
                    """,
                    (aid, teacher_id),
                ).fetchone()
                if not row:
                    return {"error": "Actividad no encontrada."}, 404
                if group_id:
                    g = conn.execute(
                        "SELECT id FROM teacher_groups WHERE id = ? AND teacher_user_id = ?",
                        (group_id, teacher_id),
                    ).fetchone()
                    if not g:
                        return {"error": "Grupo invalido."}, 404
                if grade_id:
                    gr = conn.execute(
                        "SELECT id FROM grades WHERE id = ? AND active = 1",
                        (grade_id,),
                    ).fetchone()
                    if not gr:
                        return {"error": "Grado invalido."}, 404
                now = time.time()
                existing = conn.execute(
                    """
                    SELECT id FROM activity_assignments
                    WHERE activity_id = ? AND group_id IS ? AND grade_id IS ?
                    """,
                    (aid, group_id or None, grade_id or None),
                ).fetchone()
                if existing:
                    conn.execute(
                        """
                        UPDATE activity_assignments
                        SET assigned_by_user_id = ?, assigned_at = ?
                        WHERE id = ?
                        """,
                        (teacher_id, now, existing["id"]),
                    )
                else:
                    conn.execute(
                        """
                        INSERT INTO activity_assignments (
                            activity_id, grade_id, group_id, student_user_id, assigned_by_user_id, assigned_at
                        ) VALUES (?, ?, ?, NULL, ?, ?)
                        """,
                        (aid, grade_id or None, group_id or None, teacher_id, now),
                    )
                conn.execute(
                    """
                    UPDATE learning_activities
                    SET status = 'active', updated_at = ?
                    WHERE id = ? AND creator_user_id = ?
                    """,
                    (now, aid, teacher_id),
                )
                conn.commit()
                return {"ok": True, "activity_id": aid, "message": "Actividad asignada correctamente."}, 200
            if route == "/api/teacher/activity-update":
                aid = int(data.get("activity_id", 0) or 0)
                if not aid:
                    return {"error": "Actividad invalida."}, 400
                row = conn.execute(
                    """
                    SELECT id FROM learning_activities
                    WHERE id = ? AND creator_user_id = ? AND creator_role = 'docente'
                    """,
                    (aid, teacher_id),
                ).fetchone()
                if not row:
                    return {"error": "Actividad no encontrada."}, 404
                title = (data.get("title") or "").strip()
                if not title:
                    return {"error": "Titulo requerido."}, 400
                description = (data.get("description") or "").strip() or title
                category = normalize_text(data.get("category") or "comida")
                difficulty = (data.get("difficulty") or "intermedio").strip()
                mode = (data.get("mode") or "quiz").strip()
                raw_st = normalize_text(data.get("status") or data.get("workflow_status") or "active").lower()
                if raw_st in ("borrador", "draft"):
                    wf_status = "draft"
                elif raw_st in ("programada", "scheduled"):
                    wf_status = "scheduled"
                else:
                    wf_status = "active"
                now = time.time()
                conn.execute(
                    """
                    UPDATE learning_activities
                    SET title = ?, description = ?, category = ?, difficulty = ?, mode = ?, status = ?, updated_at = ?
                    WHERE id = ? AND creator_user_id = ?
                    """,
                    (title, description, category, difficulty, mode, wf_status, now, aid, teacher_id),
                )
                conn.commit()
                return {"ok": True, "activity_id": aid}, 200
            if route == "/api/teacher/group-unassign":
                gid = int(data.get("group_id", 0) or 0)
                sid = int(data.get("student_id", 0) or 0)
                if not gid or not sid:
                    return {"error": "Grupo y estudiante requeridos."}, 400
                g = conn.execute(
                    "SELECT id FROM teacher_groups WHERE id = ? AND teacher_user_id = ?",
                    (gid, teacher_id),
                ).fetchone()
                if not g:
                    return {"error": "Grupo no encontrado."}, 404
                conn.execute(
                    "DELETE FROM group_members WHERE group_id = ? AND student_user_id = ?",
                    (gid, sid),
                )
                conn.commit()
                return {"message": "Estudiante retirado del grupo."}, 200
            if route == "/api/teacher/messaging-state":
                try:
                    payload_clean = _validate_teacher_messaging_payload(data)
                    user_app_state_put_payload(conn, teacher_id, _NS_TEACHER_MESSAGING, payload_clean)
                except ValueError as err:
                    return {"error": str(err)}, 413
                conn.commit()
                return {"ok": True}, 200
            return {"error": "Ruta invalida"}, 404
        finally:
            conn.close()


def teacher_handle_get(handler, route: str, parsed):
    user, err, st_code = api_require_user(handler, {"docente"})
    if err:
        return err, st_code
    teacher_id = user["id"]
    if route == "/api/teacher/groups":
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                rows = conn.execute(
                    """
                    SELECT g.id, g.name, g.education_level, g.grade, g.grade_id, g.difficulty_default,
                           (SELECT COUNT(*) FROM group_members m WHERE m.group_id = g.id) AS n_students
                    FROM teacher_groups g
                    WHERE g.teacher_user_id = ?
                    ORDER BY g.created_at DESC
                    """,
                    (teacher_id,),
                ).fetchall()
                groups = [
                    {
                        "id": r["id"],
                        "name": r["name"],
                        "education_level": r["education_level"],
                        "grade": r["grade"],
                        "grade_id": r["grade_id"] if "grade_id" in r.keys() else None,
                        "difficulty_default": r["difficulty_default"],
                        "students": r["n_students"],
                    }
                    for r in rows
                ]
            finally:
                conn.close()
        return {"groups": groups}, 200
    if route == "/api/teacher/students":
        q = (parse_qs(parsed.query).get("q") or [""])[0].strip().lower()
        like = f"%{q}%" if q else "%"
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                rows = conn.execute(
                    """
                    SELECT u.id, u.email, u.display_name,
                           m.group_id AS member_group_id,
                           tg.name AS member_group_name
                    FROM users u
                    LEFT JOIN group_members m ON m.student_user_id = u.id
                    LEFT JOIN teacher_groups tg ON tg.id = m.group_id
                    WHERE u.role = 'estudiante' AND COALESCE(u.active, 1) = 1
                      AND (LOWER(u.display_name) LIKE ? OR LOWER(u.email) LIKE ?)
                      AND (m.group_id IS NULL OR tg.teacher_user_id = ?)
                    ORDER BY u.display_name LIMIT 80
                    """,
                    (like, like, teacher_id),
                ).fetchall()
                students = [
                    {
                        "id": r["id"],
                        "email": r["email"],
                        "display_name": r["display_name"],
                        "member_group_id": r["member_group_id"],
                        "member_group_name": r["member_group_name"],
                    }
                    for r in rows
                ]
            finally:
                conn.close()
        return {"students": students}, 200
    if route == "/api/teacher/grades":
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                rows = conn.execute(
                    "SELECT id, name, level FROM grades WHERE active = 1 ORDER BY level, name"
                ).fetchall()
                grades = [{"id": r["id"], "name": r["name"], "level": r["level"]} for r in rows]
            finally:
                conn.close()
        return {"grades": grades}, 200
    if route == "/api/teacher/activities":
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                rows = conn.execute(
                    """
                    SELECT a.id, a.title, a.description, a.category, a.difficulty, a.mode, a.status,
                           a.created_at,
                           (
                             SELECT g.name FROM activity_assignments aa
                             JOIN teacher_groups g ON g.id = aa.group_id
                             WHERE aa.activity_id = a.id AND aa.group_id IS NOT NULL
                             ORDER BY aa.assigned_at DESC LIMIT 1
                           ) AS group_name,
                           (
                             SELECT MAX(aa.assigned_at) FROM activity_assignments aa
                             WHERE aa.activity_id = a.id
                           ) AS assigned_at
                    FROM learning_activities a
                    WHERE a.creator_user_id = ? AND a.creator_role = 'docente'
                    ORDER BY a.created_at DESC
                    LIMIT 200
                    """,
                    (teacher_id,),
                ).fetchall()
                acts = [{k: r[k] for k in r.keys()} for r in rows]
                catalog_rows = conn.execute(
                    """
                    SELECT id, title, description, category, difficulty, mode, status, created_at,
                           creator_user_id
                    FROM learning_activities
                    WHERE status = 'active'
                    ORDER BY created_at DESC
                    LIMIT 300
                    """,
                ).fetchall()
                catalog = [{k: r[k] for k in r.keys()} for r in catalog_rows]
                assigned_rows = conn.execute(
                    """
                    SELECT DISTINCT aa.activity_id
                    FROM activity_assignments aa
                    JOIN teacher_groups g ON g.id = aa.group_id
                    WHERE g.teacher_user_id = ? AND aa.group_id IS NOT NULL
                    """,
                    (teacher_id,),
                ).fetchall()
                assigned_ids = [int(r["activity_id"]) for r in assigned_rows if r["activity_id"]]
            finally:
                conn.close()
        return {"activities": acts, "catalog": catalog, "assigned_ids": assigned_ids}, 200
    if route == "/api/teacher/reports-summary":
        raw_days = (parse_qs(parsed.query).get("days") or ["30"])[0]
        try:
            days = int(raw_days)
        except (TypeError, ValueError):
            days = 30
        if days not in (7, 30, 90):
            days = 30
        cutoff = time.time() - days * 86400
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                n_groups = int(
                    scalar_from_row(
                        conn.execute(
                            "SELECT COUNT(*) FROM teacher_groups WHERE teacher_user_id = ?",
                            (teacher_id,),
                        ).fetchone()
                    )
                    or 0
                )
                n_students = int(
                    scalar_from_row(
                        conn.execute(
                            """
                            SELECT COUNT(*) FROM group_members m
                            JOIN teacher_groups g ON g.id = m.group_id
                            WHERE g.teacher_user_id = ?
                            """,
                            (teacher_id,),
                        ).fetchone()
                    )
                    or 0
                )
                acts_created = int(
                    scalar_from_row(
                        conn.execute(
                            """
                            SELECT COUNT(*) FROM learning_activities
                            WHERE creator_user_id = ? AND creator_role = 'docente' AND created_at >= ?
                            """,
                            (teacher_id, cutoff),
                        ).fetchone()
                    )
                    or 0
                )
                assigns_win = int(
                    scalar_from_row(
                        conn.execute(
                            """
                            SELECT COUNT(*) FROM activity_assignments aa
                            JOIN teacher_groups g ON g.id = aa.group_id
                            WHERE g.teacher_user_id = ? AND aa.group_id IS NOT NULL AND aa.assigned_at >= ?
                            """,
                            (teacher_id, cutoff),
                        ).fetchone()
                    )
                    or 0
                )
                n_active_all = int(
                    scalar_from_row(
                        conn.execute(
                            """
                            SELECT COUNT(*) FROM learning_activities
                            WHERE creator_user_id = ? AND creator_role = 'docente' AND status = 'active'
                            """,
                            (teacher_id,),
                        ).fetchone()
                    )
                    or 0
                )
                g_rows = conn.execute(
                    """
                    SELECT g.id, g.name,
                           (SELECT COUNT(*) FROM group_members m WHERE m.group_id = g.id) AS students,
                           (SELECT COUNT(*) FROM activity_assignments aa
                            WHERE aa.group_id = g.id AND aa.assigned_at >= ?) AS assigns_w
                    FROM teacher_groups g
                    WHERE g.teacher_user_id = ?
                    ORDER BY g.created_at DESC
                    LIMIT 50
                    """,
                    (cutoff, teacher_id),
                ).fetchall()
                max_aw = max((int(r["assigns_w"] or 0) for r in g_rows), default=0)
                group_bars = []
                for r in g_rows:
                    aw = int(r["assigns_w"] or 0)
                    bar_pct = min(100, round(100 * aw / max_aw)) if max_aw else 0
                    group_bars.append(
                        {
                            "id": r["id"],
                            "name": r["name"],
                            "students": int(r["students"] or 0),
                            "assignments_window": aw,
                            "bar_pct": bar_pct,
                        }
                    )
                recent_rows = conn.execute(
                    """
                    SELECT a.id, a.title, a.mode, a.created_at,
                           (
                             SELECT MAX(aa.assigned_at) FROM activity_assignments aa
                             WHERE aa.activity_id = a.id
                           ) AS assigned_at,
                           (
                             SELECT g.name FROM activity_assignments aa
                             JOIN teacher_groups g ON g.id = aa.group_id
                             WHERE aa.activity_id = a.id AND aa.group_id IS NOT NULL
                             ORDER BY aa.assigned_at DESC LIMIT 1
                           ) AS group_name
                    FROM learning_activities a
                    WHERE a.creator_user_id = ? AND a.creator_role = 'docente'
                      AND (
                        a.created_at >= ?
                        OR EXISTS (
                          SELECT 1 FROM activity_assignments aa
                          WHERE aa.activity_id = a.id AND aa.assigned_at >= ?
                            AND aa.group_id IN (SELECT id FROM teacher_groups WHERE teacher_user_id = ?)
                        )
                      )
                    ORDER BY COALESCE(
                             (SELECT MAX(aa.assigned_at) FROM activity_assignments aa WHERE aa.activity_id = a.id),
                             a.created_at
                           ) DESC
                    LIMIT 8
                    """,
                    (teacher_id, cutoff, cutoff, teacher_id),
                ).fetchall()
                recent_activities = [
                    {
                        "id": r["id"],
                        "title": r["title"],
                        "mode": r["mode"],
                        "created_at": r["created_at"],
                        "assigned_at": r["assigned_at"],
                        "group_name": r["group_name"],
                    }
                    for r in recent_rows
                ]
                act_tab = conn.execute(
                    """
                    SELECT a.id, a.title, a.mode, a.category, a.status, a.created_at,
                           (
                             SELECT MAX(aa.assigned_at) FROM activity_assignments aa
                             WHERE aa.activity_id = a.id
                           ) AS assigned_at,
                           (
                             SELECT g.name FROM activity_assignments aa
                             JOIN teacher_groups g ON g.id = aa.group_id
                             WHERE aa.activity_id = a.id AND aa.group_id IS NOT NULL
                             ORDER BY aa.assigned_at DESC LIMIT 1
                           ) AS group_name
                    FROM learning_activities a
                    WHERE a.creator_user_id = ? AND a.creator_role = 'docente'
                      AND (
                        a.created_at >= ?
                        OR EXISTS (
                          SELECT 1 FROM activity_assignments aa
                          WHERE aa.activity_id = a.id AND aa.assigned_at >= ?
                            AND aa.group_id IN (SELECT id FROM teacher_groups WHERE teacher_user_id = ?)
                        )
                      )
                    ORDER BY COALESCE(
                             (SELECT MAX(aa.assigned_at) FROM activity_assignments aa WHERE aa.activity_id = a.id),
                             a.created_at
                           ) DESC
                    LIMIT 80
                    """,
                    (teacher_id, cutoff, cutoff, teacher_id),
                ).fetchall()
                activities_tab = [
                    {
                        "id": r["id"],
                        "title": r["title"],
                        "mode": r["mode"],
                        "category": r["category"],
                        "status": r["status"],
                        "created_at": r["created_at"],
                        "assigned_at": r["assigned_at"],
                        "group_name": r["group_name"],
                    }
                    for r in act_tab
                ]
                stud_rows = conn.execute(
                    """
                    SELECT u.id AS student_id, u.display_name, u.email, g.name AS group_name
                    FROM group_members m
                    JOIN users u ON u.id = m.student_user_id
                    JOIN teacher_groups g ON g.id = m.group_id
                    WHERE g.teacher_user_id = ?
                    ORDER BY g.name, u.display_name
                    LIMIT 500
                    """,
                    (teacher_id,),
                ).fetchall()
                students_tab = [
                    {
                        "student_id": r["student_id"],
                        "display_name": r["display_name"],
                        "email": r["email"],
                        "group_name": r["group_name"],
                    }
                    for r in stud_rows
                ]
            finally:
                conn.close()
        return {
            "days": days,
            "totals": {
                "groups": n_groups,
                "students_in_groups": n_students,
                "activities_created_window": acts_created,
                "group_assignments_window": assigns_win,
                "active_activities_all": n_active_all,
            },
            "group_bars": group_bars,
            "recent_activities": recent_activities,
            "activities_tab": activities_tab,
            "students_tab": students_tab,
        }, 200
    if route == "/api/teacher/group-report":
        gid = int(parse_qs(parsed.query).get("group_id", ["0"])[0] or 0)
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                g = conn.execute(
                    "SELECT id, name FROM teacher_groups WHERE id = ? AND teacher_user_id = ?",
                    (gid, teacher_id),
                ).fetchone()
                if not g:
                    return {"error": "Grupo no encontrado."}, 404
                members = conn.execute(
                    """
                    SELECT u.id, u.display_name, u.email FROM group_members m
                    JOIN users u ON u.id = m.student_user_id
                    WHERE m.group_id = ?
                    """,
                    (gid,),
                ).fetchall()
                roster = [{"id": r["id"], "display_name": r["display_name"], "email": r["email"]} for r in members]
                n_act = scalar_from_row(
                    conn.execute(
                        """
                        SELECT COUNT(DISTINCT aa.activity_id) FROM activity_assignments aa
                        WHERE aa.group_id = ?
                        """,
                        (gid,),
                    ).fetchone()
                )
                avg_txt = "—"
                if roster and n_act:
                    avg_txt = f"{(n_act / len(roster)):.1f}"
            finally:
                conn.close()
        return {
            "group": {"id": int(g["id"]), "name": g["name"]},
            "students": roster,
            "summary": {
                "total_estudiantes": len(roster),
                "actividades_asignadas_grupo": int(n_act or 0),
                "promedio_actividades_por_estudiante": avg_txt,
                "nota": "Indicadores derivados de asignaciones registradas en AVI.",
            },
        }, 200
    if route == "/api/teacher/messaging-state":
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                data = user_app_state_get_payload(conn, teacher_id, _NS_TEACHER_MESSAGING)
            finally:
                conn.close()
        return {"messaging": data}, 200
    return {"error": "Not found"}, 404


def admin_handle_post(handler, route: str, data: dict):
    user, err, st_code = api_require_user(handler, {"administrador"})
    if err:
        return err, st_code
    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            if route == "/api/admin/user-update":
                uid = int(data.get("id", 0) or 0)
                role = (data.get("role") or "").strip().lower()
                if role and role not in AUTH_ROLES:
                    return {"error": "Rol invalido"}, 400
                row = conn.execute("SELECT id FROM users WHERE id = ?", (uid,)).fetchone()
                if not row:
                    return {"error": "Usuario no existe"}, 404
                if role:
                    conn.execute("UPDATE users SET role = ? WHERE id = ?", (role, uid))
                if "active" in data:
                    conn.execute(
                        "UPDATE users SET active = ? WHERE id = ?",
                        (1 if data.get("active") else 0, uid),
                    )
                if data.get("display_name"):
                    conn.execute(
                        "UPDATE users SET display_name = ? WHERE id = ?",
                        ((data.get("display_name") or "").strip(), uid),
                    )
                if "grade_id" in data:
                    gid = int(data.get("grade_id", 0) or 0)
                    row_u = conn.execute("SELECT role FROM users WHERE id = ?", (uid,)).fetchone()
                    if row_u and row_u["role"] == "estudiante":
                        if gid > 0:
                            gr = conn.execute("SELECT id FROM grades WHERE id = ? AND active = 1", (gid,)).fetchone()
                            if not gr:
                                return {"error": "Grado no existe."}, 404
                            conn.execute(
                                """
                                INSERT INTO student_grades (student_user_id, grade_id, assigned_at)
                                VALUES (?, ?, ?)
                                ON CONFLICT(student_user_id) DO UPDATE SET
                                    grade_id = excluded.grade_id,
                                    assigned_at = excluded.assigned_at
                                """,
                                (uid, gid, time.time()),
                            )
                        else:
                            conn.execute("DELETE FROM student_grades WHERE student_user_id = ?", (uid,))
                parts = [f"id={uid}"]
                if role:
                    parts.append(f"rol={role}")
                if "active" in data:
                    parts.append(f"activo={1 if data.get('active') else 0}")
                if data.get("display_name"):
                    parts.append("nombre_actualizado")
                if "grade_id" in data:
                    parts.append(f"grade_id={(data.get('grade_id'))}")
                admin_audit_insert(conn, user, "USER_UPDATE", " ".join(parts))
                conn.commit()
                return {"message": "Rol asignado con éxito" if role else "Usuario actualizado"}, 200
            if route == "/api/admin/user-delete":
                uid = int(data.get("id", 0) or 0)
                if uid <= 0:
                    return {"error": "Usuario inválido."}, 400
                if uid == int(user["id"]):
                    return {"error": "No puede eliminar su propia cuenta de administrador."}, 400
                conn.execute(
                    "DELETE FROM activity_assignments WHERE assigned_by_user_id = ? OR student_user_id = ?",
                    (uid, uid),
                )
                conn.execute("DELETE FROM learning_activities WHERE creator_user_id = ?", (uid,))
                conn.execute("DELETE FROM content_submissions WHERE teacher_user_id = ?", (uid,))
                conn.execute("DELETE FROM student_settings WHERE student_user_id = ?", (uid,))
                conn.execute("DELETE FROM student_grades WHERE student_user_id = ?", (uid,))
                conn.execute("DELETE FROM user_app_state WHERE user_id = ?", (uid,))
                conn.execute(
                    """DELETE FROM group_members WHERE student_user_id = ?
                       OR group_id IN (SELECT id FROM teacher_groups WHERE teacher_user_id = ?)""",
                    (uid, uid),
                )
                conn.execute("DELETE FROM teacher_groups WHERE teacher_user_id = ?", (uid,))
                conn.execute("DELETE FROM group_members WHERE student_user_id = ?", (uid,))
                conn.execute("DELETE FROM sessions WHERE user_id = ?", (uid,))
                conn.execute("DELETE FROM users WHERE id = ?", (uid,))
                admin_audit_insert(conn, user, "USER_DELETE", f"id={uid}")
                conn.commit()
                return {"message": "Usuario eliminado"}, 200
            if route == "/api/admin/cms-save":
                kind = (data.get("kind") or "termino").strip()
                title = (data.get("title") or "").strip()
                body = (data.get("body") or "").strip()
                st_raw = normalize_text(data.get("status") or "published").lower()
                cms_status = "draft" if st_raw in ("draft", "borrador") else "published"
                if not title:
                    return {"error": "Titulo requerido"}, 400
                cid = data.get("id")
                now = time.time()
                if cid is not None and str(cid).isdigit():
                    cid_i = int(cid)
                    conn.execute(
                        "UPDATE cms_items SET kind = ?, title = ?, body = ?, updated_at = ?, status = ? WHERE id = ?",
                        (kind, title, body, now, cms_status, cid_i),
                    )
                    admin_audit_insert(conn, user, "CMS_UPDATE", f"id={cid_i} titulo={title[:120]}")
                else:
                    new_id = insert_returning_id(
                        conn,
                        "INSERT INTO cms_items (kind, title, body, updated_at, status) VALUES (?, ?, ?, ?, ?)",
                        (kind, title, body, now, cms_status),
                    )
                    admin_audit_insert(conn, user, "CMS_CREATE", f"id={new_id} titulo={title[:120]}")
                conn.commit()
                return {"ok": True}, 200
            if route == "/api/admin/cms-delete":
                cid = int(data.get("id", 0) or 0)
                conn.execute("DELETE FROM cms_items WHERE id = ?", (cid,))
                admin_audit_insert(conn, user, "CMS_DELETE", f"id={cid}")
                conn.commit()
                return {"ok": True}, 200
            if route == "/api/admin/grades":
                name = (data.get("name") or "").strip()
                level = (data.get("level") or "General").strip() or "General"
                if not name:
                    return {"error": "Nombre de grado requerido."}, 400
                now = time.time()
                conn.execute(
                    """
                    INSERT INTO grades (name, level, active, created_at)
                    VALUES (?, ?, 1, ?)
                    ON CONFLICT(name) DO UPDATE SET level = excluded.level, active = 1
                    """,
                    (name, level, now),
                )
                admin_audit_insert(conn, user, "GRADE_UPSERT", f"nombre={name} nivel={level}")
                conn.commit()
                return {"ok": True}, 200
            if route == "/api/admin/grade-delete":
                gid = int(data.get("id", 0) or 0)
                if gid <= 0:
                    return {"error": "Grado inválido."}, 400
                conn.execute("DELETE FROM student_grades WHERE grade_id = ?", (gid,))
                conn.execute("UPDATE teacher_groups SET grade_id = NULL WHERE grade_id = ?", (gid,))
                conn.execute("DELETE FROM grades WHERE id = ?", (gid,))
                admin_audit_insert(conn, user, "GRADE_DELETE", f"id={gid}")
                conn.commit()
                return {"ok": True}, 200
            if route == "/api/admin/student-grade-assign":
                uid = int(data.get("student_user_id", 0) or 0)
                gid = int(data.get("grade_id", 0) or 0)
                st = conn.execute("SELECT id FROM users WHERE id = ? AND role = 'estudiante'", (uid,)).fetchone()
                if not st:
                    return {"error": "Estudiante no encontrado."}, 404
                if gid <= 0:
                    conn.execute("DELETE FROM student_grades WHERE student_user_id = ?", (uid,))
                else:
                    gr = conn.execute("SELECT id FROM grades WHERE id = ? AND active = 1", (gid,)).fetchone()
                    if not gr:
                        return {"error": "Grado no encontrado."}, 404
                    conn.execute(
                        """
                        INSERT INTO student_grades (student_user_id, grade_id, assigned_at)
                        VALUES (?, ?, ?)
                        ON CONFLICT(student_user_id) DO UPDATE SET
                            grade_id = excluded.grade_id,
                            assigned_at = excluded.assigned_at
                        """,
                        (uid, gid, time.time()),
                    )
                admin_audit_insert(
                    conn,
                    user,
                    "STUDENT_GRADE_ASSIGN",
                    f"estudiante_id={uid} grado_id={gid}",
                )
                conn.commit()
                return {"ok": True}, 200
            if route == "/api/admin/content-review":
                sid = int(data.get("id", 0) or 0)
                action = (data.get("action") or "").strip().lower()
                review_notes = (data.get("review_notes") or "").strip()
                if action not in ("approve", "reject"):
                    return {"error": "Acción inválida."}, 400
                row = conn.execute(
                    "SELECT * FROM content_submissions WHERE id = ?",
                    (sid,),
                ).fetchone()
                if not row:
                    return {"error": "Propuesta no encontrada."}, 404
                status = "approved" if action == "approve" else "rejected"
                now = time.time()
                conn.execute(
                    """
                    UPDATE content_submissions
                    SET status = ?, review_notes = ?, reviewed_by_user_id = ?, reviewed_at = ?
                    WHERE id = ?
                    """,
                    (status, review_notes, user["id"], now, sid),
                )
                if status == "approved":
                    title = row["title"] or "Propuesta docente"
                    body_lines = [
                        f"Nasa Yuwe: {row['nasa_yuwe'] or '—'}",
                        f"Español: {row['espanol'] or '—'}",
                        f"Traducción: {row['translation'] or '—'}",
                        f"Imagen: {row['image_url'] or '—'}",
                        f"Audio: {row['audio_url'] or '—'}",
                        f"Notas: {row['notes'] or '—'}",
                    ]
                    conn.execute(
                        "INSERT INTO cms_items (kind, title, body, updated_at, status) VALUES (?, ?, ?, ?, ?)",
                        (row["kind"] or "termino", title, "\n".join(body_lines), now, "published"),
                    )
                admin_audit_insert(
                    conn,
                    user,
                    "CONTENT_REVIEW",
                    f"propuesta_id={sid} resultado={status}",
                )
                conn.commit()
                return {"ok": True, "status": status}, 200
            if route == "/api/admin/mail-send":
                subject = (data.get("subject") or "").strip()
                mail_body = (data.get("body") or "").strip()
                audience = (data.get("audience") or "all").strip().lower()
                if audience not in _MAIL_AUDIENCE_KEYS:
                    audience = "all"
                if not subject:
                    return {"error": "Asunto requerido."}, 400
                now_m = time.time()
                conn.execute(
                    """INSERT INTO admin_mail_messages (created_at, subject, body, audience, state)
                       VALUES (?, ?, ?, ?, ?)""",
                    (now_m, subject[:500], mail_body[:16000], audience, "Entregado"),
                )
                admin_audit_insert(
                    conn,
                    user,
                    "MAIL_SEND",
                    f"{subject[:120]} -> {_mail_audience_label(audience)}",
                )
                conn.commit()
                return {"ok": True}, 200
            if route == "/api/admin/support-ticket":
                topic = (data.get("topic") or "").strip()
                priority = (data.get("priority") or "Media").strip()
                if not topic or len(topic) < 4:
                    return {"error": "Describe el tema del ticket (min. 4 caracteres)."}, 400
                if priority not in ("Baja", "Media", "Alta"):
                    priority = "Media"
                now_t = time.time()
                rn = user.get("display_name") or "Usuario"
                re = user.get("email") or ""
                conn.execute(
                    """INSERT INTO admin_support_tickets
                       (created_at, topic, requester_name, requester_email, priority, state, created_by_user_id)
                       VALUES (?, ?, ?, ?, ?, 'Abierto', ?)""",
                    (now_t, topic[:500], rn, re, priority, user["id"]),
                )
                admin_audit_insert(conn, user, "SUPPORT_TICKET", topic[:160])
                conn.commit()
                return {"ok": True}, 200
            if route == "/api/admin/user-create":
                email_cr = normalize_email(data.get("email"))
                pw = data.get("password") or ""
                display_name_cr = (data.get("display_name") or "").strip()
                role_cr = (data.get("role") or "").strip().lower()
                if not email_cr or "@" not in email_cr:
                    return {"error": "Correo invalido."}, 400
                pol = auth_password_policy_violation(pw)
                if pol:
                    return {"error": pol}, 400
                if len(display_name_cr) < 2:
                    return {"error": "Nombre mínimo 2 caracteres."}, 400
                if role_cr not in AUTH_ROLES:
                    return {"error": "Rol invalido."}, 400
                if conn.execute("SELECT 1 FROM users WHERE email = ?", (email_cr,)).fetchone():
                    return {"error": "Ya existe una cuenta con este correo."}, 409
                cr_now = time.time()
                new_uid = insert_returning_id(
                    conn,
                    """INSERT INTO users (
                        email, password_hash, google_sub, display_name, role,
                        created_at, active, email_verified)
                       VALUES (?, ?, NULL, ?, ?, ?, 1, 1)""",
                    (email_cr, auth_hash_password(pw), display_name_cr, role_cr, cr_now),
                )
                admin_audit_insert(conn, user, "USER_CREATE", f"id={new_uid} email={email_cr} rol={role_cr}")
                conn.commit()
                return {"message": "Usuario creado", "user_id": new_uid}, 200
            return {"error": "Ruta invalida"}, 404
        finally:
            conn.close()


def _admin_usage_series_sql(conn) -> dict:
    """Últimos 5 meses: registros nuevos de usuarios y sesiones creadas (aprox. uso)."""
    today = date.today()
    y, m = today.year, today.month
    months_order: list[tuple[int, int]] = []
    for _ in range(5):
        months_order.insert(0, (y, m))
        m -= 1
        if m == 0:
            m = 12
            y -= 1
    labels_es = ("", "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic")
    labels: list[str] = []
    new_users: list[int] = []
    sessions: list[int] = []
    for year, month in months_order:
        labels.append(labels_es[month])
        start = datetime(year, month, 1, tzinfo=timezone.utc).timestamp()
        if month == 12:
            end = datetime(year + 1, 1, 1, tzinfo=timezone.utc).timestamp()
        else:
            end = datetime(year, month + 1, 1, tzinfo=timezone.utc).timestamp()
        nu = int(
            scalar_from_row(
                conn.execute(
                    "SELECT COUNT(*) FROM users WHERE created_at >= ? AND created_at < ?",
                    (start, end),
                ).fetchone()
            )
            or 0
        )
        ns = int(
            scalar_from_row(
                conn.execute(
                    "SELECT COUNT(*) FROM sessions WHERE created_at >= ? AND created_at < ?",
                    (start, end),
                ).fetchone()
            )
            or 0
        )
        new_users.append(nu)
        sessions.append(ns)
    return {"months": labels, "new_users": new_users, "sessions": sessions}


def admin_handle_get(handler, route: str):
    user, err, st_code = api_require_user(handler, {"administrador"})
    if err:
        return err, st_code
    if route == "/api/admin/users":
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                rows = conn.execute(
                    """
                    SELECT id, email, display_name, role,
                           COALESCE(active, 1) AS active,
                           COALESCE(email_verified, 1) AS email_verified,
                           (SELECT g.id FROM student_grades sg JOIN grades g ON g.id = sg.grade_id WHERE sg.student_user_id = users.id) AS grade_id,
                           (SELECT g.name FROM student_grades sg JOIN grades g ON g.id = sg.grade_id WHERE sg.student_user_id = users.id) AS grade_name
                    FROM users ORDER BY id
                    """
                ).fetchall()
                users_list = []
                for r in rows:
                    users_list.append(
                        {
                            "id": r["id"],
                            "email": r["email"],
                            "display_name": r["display_name"],
                            "role": r["role"],
                            "active": bool(r["active"]),
                            "email_verified": bool(r["email_verified"]),
                            "grade_id": r["grade_id"],
                            "grade_name": r["grade_name"],
                        }
                    )
            finally:
                conn.close()
        return {"users": users_list}, 200
    if route == "/api/admin/grades":
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                rows = conn.execute(
                    """
                    SELECT g.id, g.name, g.level, g.active,
                           (SELECT COUNT(*) FROM student_grades sg WHERE sg.grade_id = g.id) AS students
                    FROM grades g
                    ORDER BY g.level, g.name
                    """
                ).fetchall()
                grades = [{k: r[k] for k in r.keys()} for r in rows]
            finally:
                conn.close()
        return {"grades": grades}, 200
    if route == "/api/admin/cms":
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                rows = conn.execute(
                    "SELECT id, kind, title, body, updated_at, COALESCE(status, 'published') AS status FROM cms_items ORDER BY updated_at DESC LIMIT 300"
                ).fetchall()
                items = [{k: r[k] for k in r.keys()} for r in rows]
            finally:
                conn.close()
        cats = sorted(ENGINE.by_category.keys())
        return {
            "cms_items": items,
            "categories": cats[:240],
            "corpus_snapshot": ENGINE.stats(),
        }, 200
    if route == "/api/admin/stats-dash":
        usage_series: dict = {"months": [], "new_users": [], "sessions": []}
        n_cms = 0
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                n_users = scalar_from_row(conn.execute("SELECT COUNT(*) FROM users").fetchone())
                n_st = scalar_from_row(
                    conn.execute("SELECT COUNT(*) FROM users WHERE role = 'estudiante'").fetchone()
                )
                n_dc = scalar_from_row(conn.execute("SELECT COUNT(*) FROM users WHERE role = 'docente'").fetchone())
                n_ad = scalar_from_row(
                    conn.execute(
                        "SELECT COUNT(*) FROM users WHERE role = 'administrador'",
                    ).fetchone()
                )
                n_act = scalar_from_row(
                    conn.execute(
                        "SELECT COUNT(*) FROM users WHERE COALESCE(active, 1) = 1",
                    ).fetchone()
                )
                n_cms = int(scalar_from_row(conn.execute("SELECT COUNT(*) FROM cms_items").fetchone()) or 0)
                usage_series = _admin_usage_series_sql(conn)
            finally:
                conn.close()
        st = ENGINE.stats()
        total_entries = len(ENGINE.rows)
        if n_users == 0:
            payload = {
                "message": "No existen estadísticas disponibles",
                "empty": True,
                "usage_series": usage_series,
                "cms_items_count": n_cms,
            }
        else:
            payload = {
                "empty": False,
                "platform": {
                    "usuarios_registrados": int(n_users or 0),
                    "estudiantes": int(n_st or 0),
                    "docentes": int(n_dc or 0),
                    "administradores": int(n_ad or 0),
                    "cuentas_activas": int(n_act or 0),
                },
                "corpus": {
                    "entradas": total_entries,
                    "categorias": st.get("categories", 0),
                    "cms_items_count": n_cms,
                },
                "usage_series": usage_series,
            }
        return payload, 200
    if route == "/api/admin/content-submissions":
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                rows = conn.execute(
                    """
                    SELECT s.id, s.kind, s.title, s.espanol, s.nasa_yuwe, s.translation,
                           s.image_url, s.audio_url, s.notes, s.status, s.review_notes,
                           s.created_at, s.reviewed_at,
                           u.display_name AS teacher_name
                    FROM content_submissions s
                    JOIN users u ON u.id = s.teacher_user_id
                    ORDER BY
                        CASE s.status WHEN 'pending' THEN 0 WHEN 'approved' THEN 1 ELSE 2 END,
                        s.created_at DESC
                    LIMIT 400
                    """
                ).fetchall()
                items = [{k: r[k] for k in r.keys()} for r in rows]
            finally:
                conn.close()
        return {"items": items}, 200
    if route == "/api/admin/groups":
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                rows = conn.execute(
                    """
                    SELECT g.id, g.name, g.education_level, g.grade,
                           COALESCE(gr.name,'') AS inst_grade_name,
                           g.difficulty_default,
                           u.display_name AS teacher_name,
                           (SELECT COUNT(*) FROM group_members m WHERE m.group_id = g.id) AS students
                    FROM teacher_groups g
                    JOIN users u ON u.id = g.teacher_user_id
                    LEFT JOIN grades gr ON gr.id = g.grade_id
                    ORDER BY g.created_at DESC
                    LIMIT 400
                    """
                ).fetchall()
                groups_payload = []
                for r in rows:
                    lvl = (r["education_level"] or r["inst_grade_name"] or r["grade"] or "General").strip() or "General"
                    groups_payload.append(
                        {
                            "id": int(r["id"]),
                            "name": r["name"],
                            "teacher": r["teacher_name"],
                            "level": lvl,
                            "students": int(r["students"] or 0),
                            "active": True,
                        }
                    )
            finally:
                conn.close()
        return {"groups": groups_payload}, 200
    if route == "/api/admin/audit":
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                rows = conn.execute(
                    """
                    SELECT id, created_at, actor_name, action, detail
                    FROM admin_audit_log
                    ORDER BY created_at DESC
                    LIMIT 450
                    """
                ).fetchall()
                audit_rows_sql = [{k: r[k] for k in r.keys()} for r in rows]
            finally:
                conn.close()
        now_dt = datetime.now()
        day0 = now_dt.replace(hour=0, minute=0, second=0, microsecond=0).timestamp()
        week0 = (now_dt - timedelta(days=7)).timestamp()
        log_rows = []
        n_today = 0
        n_week = 0
        for r in audit_rows_sql:
            ts = float(r["created_at"])
            if ts >= day0:
                n_today += 1
            if ts >= week0:
                n_week += 1
            log_rows.append(
                {
                    "id": r["id"],
                    "when": admin_audit_fmt_when(ts),
                    "actor": r["actor_name"],
                    "action": r["action"],
                    "detail": r["detail"],
                }
            )
        review_like = sum(1 for r in audit_rows_sql if ("REVIEW" in (r["action"] or "").upper() or "ALERT" in (r["action"] or "").upper()))
        pct = 100 if not audit_rows_sql else max(72, min(100, int(100 - (review_like * 100 / max(len(audit_rows_sql), 1)) * 0.15)))
        return {"rows": log_rows, "kpis": {"today": n_today, "week": n_week, "alerts_reviewed_pct": pct}}, 200
    if route == "/api/admin/mail-history":
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                rows = conn.execute(
                    """
                    SELECT id, created_at, subject, audience, state
                    FROM admin_mail_messages
                    ORDER BY created_at DESC
                    LIMIT 120
                    """
                ).fetchall()
                mail_sql = [{k: r[k] for k in r.keys()} for r in rows]
            finally:
                conn.close()
        items = []
        now_ts = time.time()
        cutoff = now_ts - 30 * 86400
        sent_30 = 0
        for r in mail_sql:
            ts = float(r["created_at"])
            if ts >= cutoff:
                sent_30 += 1
            items.append(
                {
                    "id": r["id"],
                    "subject": r["subject"],
                    "audience": _mail_audience_label(str(r["audience"])),
                    "when": admin_audit_fmt_when(ts),
                    "state": r["state"],
                }
            )
        scheduled = sum(1 for r in mail_sql if r["state"] and "rogram" in r["state"])
        kpis = {
            "sent_30d": sent_30,
            "scheduled": scheduled,
            "open_rate_estimate": min(94, 48 + min(sent_30, 42)),
        }
        return {"items": items, "kpis": kpis}, 200
    if route == "/api/admin/support-tickets":
        with _AUTH_DB_LOCK:
            conn = auth_connect()
            try:
                rows = conn.execute(
                    """
                    SELECT id, created_at, topic, requester_name, requester_email, priority, state
                    FROM admin_support_tickets
                    ORDER BY created_at DESC
                    LIMIT 200
                    """
                ).fetchall()
            finally:
                conn.close()
        tickets = []
        for r in rows:
            frm = (r["requester_email"] or "").strip() or r["requester_name"]
            st_map = {"Abierto": "Abierto", "Resuelto": "Resuelto"}
            disp_st = r["state"]
            if disp_st and disp_st not in st_map:
                if "prog" in disp_st.lower():
                    disp_st = "En progreso"
            tickets.append(
                {
                    "id": f"T-{int(r['id'])}",
                    "topic": r["topic"],
                    "from": frm,
                    "priority": r["priority"],
                    "state": disp_st,
                }
            )
        open_n = sum(1 for x in tickets if x["state"] == "Abierto")
        resolved_recent = sum(1 for x in tickets if x["state"] == "Resuelto")
        return {
            "tickets": tickets,
            "kpis": {"open": open_n, "resolved_month": resolved_recent, "sla_hint": "4h"},
        }, 200
    return {"error": "Not found"}, 404


_NS_TEACHER_MESSAGING = "teacher_messaging_v1"
_MAX_VOCAB_DIARY_JSON = 48_000
_MAX_AVI_CHAT_JSON = 280_000
_MAX_CHAT_MSGS = 72
_MAX_DICT_CATEGORIES = 48


def _utc_today_ymd() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def _ymd_minus_one(ymd: str) -> str:
    d = date.fromisoformat(ymd)
    return (d - timedelta(days=1)).isoformat()


def _streak_week_slots(streak_n: int) -> list[bool]:
    n = max(0, min(int(streak_n), 7))
    return [i >= 7 - n for i in range(7)]


def _json_parse_obj(raw, default: dict):
    if raw is None:
        return dict(default)
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, (bytes, bytearray)):
        raw = raw.decode("utf-8", errors="replace")
    if isinstance(raw, str):
        s = raw.strip()
        if not s:
            return dict(default)
        try:
            out = json.loads(s)
            return out if isinstance(out, dict) else dict(default)
        except json.JSONDecodeError:
            return dict(default)
    return dict(default)


def _json_parse_list(raw, default: list):
    if raw is None:
        return list(default)
    if isinstance(raw, list):
        return raw
    if isinstance(raw, (bytes, bytearray)):
        raw = raw.decode("utf-8", errors="replace")
    if isinstance(raw, str):
        s = raw.strip()
        if not s:
            return list(default)
        try:
            out = json.loads(s)
            return out if isinstance(out, list) else list(default)
        except json.JSONDecodeError:
            return list(default)
    return list(default)


def student_ensure_settings_row(conn, student_id: int) -> None:
    now = time.time()
    conn.execute(
        """
        INSERT INTO student_settings (student_user_id, updated_at)
        VALUES (?, ?)
        ON CONFLICT (student_user_id) DO NOTHING
        """,
        (student_id, now),
    )


def student_streak_touch_and_read(conn, student_id: int) -> tuple[int, list[bool]]:
    row = conn.execute(
        """
        SELECT streak_current, streak_last_active_ymd
        FROM student_settings WHERE student_user_id = ?
        """,
        (student_id,),
    ).fetchone()
    streak = int(row["streak_current"] or 0) if row else 0
    raw_last = row["streak_last_active_ymd"] if row else None
    last = raw_last.strip() if isinstance(raw_last, str) and raw_last.strip() else None
    today = _utc_today_ymd()
    if last == today:
        return streak, _streak_week_slots(streak)
    if last is None:
        streak = 1
    elif last == _ymd_minus_one(today):
        streak = streak + 1
    else:
        streak = 1
    now = time.time()
    conn.execute(
        """
        UPDATE student_settings
        SET streak_current = ?, streak_last_active_ymd = ?, updated_at = ?
        WHERE student_user_id = ?
        """,
        (streak, today, now, student_id),
    )
    return streak, _streak_week_slots(streak)


def _validate_vocab_diary(obj: object) -> dict:
    d = obj if isinstance(obj, dict) else {}
    items_in = d.get("items")
    items: list = []
    if isinstance(items_in, list):
        for it in items_in[:30]:
            if not isinstance(it, dict):
                continue
            tid = it.get("id")
            if tid is None:
                continue
            items.append(
                {
                    "id": tid,
                    "espanol": str(it.get("espanol") or "")[:240],
                    "nasa_yuwe": str(it.get("nasa_yuwe") or "")[:240],
                    "progress": max(0, min(100, int(it.get("progress") or 0))),
                }
            )
    validated = max(0, min(30, int(d.get("validated") or 0)))
    out = {"validated": validated, "items": items}
    raw = json.dumps(out, ensure_ascii=False)
    if len(raw.encode("utf-8")) > _MAX_VOCAB_DIARY_JSON:
        out["items"] = items[:12]
        out["validated"] = min(validated, 12)
    return out


def _validate_dictionary_categories(obj: object) -> list[str]:
    if not isinstance(obj, list):
        return []
    out: list[str] = []
    for x in obj[:_MAX_DICT_CATEGORIES]:
        s = str(x).strip()[:64]
        if s and s not in out:
            out.append(s)
    return out


def _validate_avi_chat_messages(obj: object) -> list[dict]:
    if not isinstance(obj, list):
        return []
    out: list[dict] = []
    for m in obj[:_MAX_CHAT_MSGS]:
        if not isinstance(m, dict):
            continue
        role = str(m.get("role") or "user")[:24]
        text = str(m.get("text") or "")[:8000]
        at = str(m.get("at") or "")[:80]
        o = {"role": role, "text": text}
        if at:
            o["at"] = at
        if m.get("audio"):
            o["audio"] = True
        out.append(o)
    return out


def _validate_teacher_messaging_payload(obj: object) -> dict:
    if not isinstance(obj, dict):
        return {"threads": [], "active": ""}
    threads_in = obj.get("threads")
    threads: list[dict] = []
    if isinstance(threads_in, list):
        for th in threads_in[:24]:
            if not isinstance(th, dict):
                continue
            tid = str(th.get("id") or "")[:48] or secrets.token_hex(4)
            with_ = str(th.get("with") or "Chat")[:200]
            msgs_in = th.get("msgs")
            msgs: list[dict] = []
            if isinstance(msgs_in, list):
                for m in msgs_in[:120]:
                    if not isinstance(m, dict):
                        continue
                    text = str(m.get("text") or "")[:4000]
                    msgs.append(
                        {
                            "me": bool(m.get("me")),
                            "text": text,
                            "at": str(m.get("at") or "")[:80],
                        }
                    )
            threads.append({"id": tid, "with": with_, "msgs": msgs, "last": str(th.get("last") or "")[:80]})
    active = str(obj.get("active") or "")[:48]
    return {"threads": threads, "active": active}


def user_app_state_get_payload(conn, user_id: int, namespace: str) -> dict:
    row = conn.execute(
        "SELECT payload FROM user_app_state WHERE user_id = ? AND namespace = ?",
        (user_id, namespace),
    ).fetchone()
    if not row:
        return {}
    return _json_parse_obj(row["payload"], {})


def user_app_state_put_payload(conn, user_id: int, namespace: str, payload: dict) -> None:
    now = time.time()
    body = json.dumps(payload, ensure_ascii=False)
    if len(body.encode("utf-8")) > 400_000:
        raise ValueError("Estado demasiado grande")
    conn.execute(
        """
        INSERT INTO user_app_state (user_id, namespace, payload, updated_at)
        VALUES (?, ?, ?, ?)
        ON CONFLICT (user_id, namespace) DO UPDATE SET
            payload = excluded.payload,
            updated_at = excluded.updated_at
        """,
        (user_id, namespace, body, now),
    )


def student_handle_get(handler, route: str, parsed):
    user, err, st_code = api_require_user(handler, {"estudiante"})
    if err:
        return err, st_code
    student_id = user["id"]
    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            if route == "/api/student/profile-school":
                grade = conn.execute(
                    """
                    SELECT g.id, g.name, g.level
                    FROM student_grades sg
                    JOIN grades g ON g.id = sg.grade_id
                    WHERE sg.student_user_id = ?
                    """,
                    (student_id,),
                ).fetchone()
                groups = conn.execute(
                    """
                    SELECT g.id, g.name, g.grade
                    FROM group_members m
                    JOIN teacher_groups g ON g.id = m.group_id
                    WHERE m.student_user_id = ?
                    ORDER BY g.created_at DESC
                    """,
                    (student_id,),
                ).fetchall()
                return {
                    "grade": ({k: grade[k] for k in grade.keys()} if grade else None),
                    "groups": [{k: r[k] for k in r.keys()} for r in groups],
                }, 200
            if route == "/api/student/activities":
                assigned = conn.execute(
                    """
                    SELECT DISTINCT a.id, a.title, a.description, a.category, a.difficulty, a.mode, a.created_at
                    FROM learning_activities a
                    JOIN activity_assignments aa ON aa.activity_id = a.id
                    LEFT JOIN student_grades sg ON sg.student_user_id = ?
                    LEFT JOIN group_members gm ON gm.student_user_id = ?
                    WHERE a.status = 'active'
                      AND (
                        aa.student_user_id = ?
                        OR (aa.grade_id IS NOT NULL AND aa.grade_id = sg.grade_id)
                        OR (aa.group_id IS NOT NULL AND aa.group_id = gm.group_id)
                      )
                    ORDER BY a.created_at DESC
                    LIMIT 200
                    """,
                    (student_id, student_id, student_id),
                ).fetchall()
                catalog = conn.execute(
                    """
                    SELECT id, title, description, category, difficulty, mode, created_at
                    FROM learning_activities
                    WHERE status = 'active'
                    ORDER BY created_at DESC
                    LIMIT 300
                    """,
                ).fetchall()
                return {
                    "activities": [{k: r[k] for k in r.keys()} for r in assigned],
                    "catalog": [{k: r[k] for k in r.keys()} for r in catalog],
                }, 200
            if route == "/api/student/settings":
                student_ensure_settings_row(conn, student_id)
                streak_n, week_slots = student_streak_touch_and_read(conn, student_id)
                row = conn.execute(
                    """
                    SELECT language, theme, level, goal, reminders,
                           notif_daily, notif_content, notif_streak, notif_tips, consent_given,
                           vocab_diary_json, dictionary_categories_json, avi_chat_json
                    FROM student_settings
                    WHERE student_user_id = ?
                    """,
                    (student_id,),
                ).fetchone()
                defaults = {
                    "language": "Espanol",
                    "theme": "Claro Nasa",
                    "level": "Intermedio",
                    "goal": "Conversacion fluida",
                    "reminders": 1,
                    "notif_daily": 1,
                    "notif_content": 1,
                    "notif_streak": 1,
                    "notif_tips": 0,
                    "consent_given": 1,
                }
                data = {**defaults, **({k: row[k] for k in row.keys()} if row else {})}
                vocab_diary = _json_parse_obj(data.get("vocab_diary_json"), {"validated": 0, "items": []})
                dictionary_last_categories = _json_parse_list(data.get("dictionary_categories_json"), [])
                avi_chat_messages = _json_parse_list(data.get("avi_chat_json"), [])
                conn.commit()
                return {
                    "settings": {
                        "language": data["language"],
                        "theme": data["theme"],
                        "level": data["level"],
                        "goal": data["goal"],
                        "reminders": bool(data["reminders"]),
                        "notifications": {
                            "daily": bool(data["notif_daily"]),
                            "content": bool(data["notif_content"]),
                            "streak": bool(data["notif_streak"]),
                            "tips": bool(data["notif_tips"]),
                        },
                        "consent_given": bool(data["consent_given"]),
                        "vocab_diary": vocab_diary,
                        "dictionary_last_categories": dictionary_last_categories,
                        "avi_chat_messages": avi_chat_messages,
                        "streak": {"current": streak_n, "week_slots": week_slots},
                    }
                }, 200
            if route == "/api/student/sessions":
                rows = conn.execute(
                    """
                    SELECT token, created_at, expires_at
                    FROM sessions
                    WHERE user_id = ? AND expires_at > ?
                    ORDER BY created_at DESC
                    LIMIT 15
                    """,
                    (student_id, time.time()),
                ).fetchall()
                current_tok = auth_get_session_token(handler)
                items = []
                for idx, r in enumerate(rows):
                    items.append(
                        {
                            "id": idx + 1,
                            "created_at": r["created_at"],
                            "expires_at": r["expires_at"],
                            "current": bool(current_tok and current_tok == r["token"]),
                        }
                    )
                return {"sessions": items}, 200
        finally:
            conn.close()
    return {"error": "Not found"}, 404


def student_handle_post(handler, route: str, data: dict):
    user, err, st_code = api_require_user(handler, {"estudiante"})
    if err:
        return err, st_code
    student_id = user["id"]
    payload = data or {}
    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            if route == "/api/student/settings":
                student_ensure_settings_row(conn, student_id)
                curr = conn.execute(
                    """
                    SELECT language, theme, level, goal, reminders,
                           notif_daily, notif_content, notif_streak, notif_tips, consent_given,
                           vocab_diary_json, dictionary_categories_json, avi_chat_json
                    FROM student_settings
                    WHERE student_user_id = ?
                    """,
                    (student_id,),
                ).fetchone()
                cur = {k: curr[k] for k in curr.keys()} if curr else {}
                notifications = payload.get("notifications") or {}
                language = (payload.get("language") or cur.get("language") or "Espanol").strip() or "Espanol"
                theme = (payload.get("theme") or cur.get("theme") or "Claro Nasa").strip() or "Claro Nasa"
                level = (payload.get("level") or cur.get("level") or "Intermedio").strip() or "Intermedio"
                goal = (payload.get("goal") or cur.get("goal") or "Conversacion fluida").strip() or "Conversacion fluida"
                reminders = 1 if bool(payload.get("reminders", cur.get("reminders", 1))) else 0
                notif_daily = 1 if bool(notifications.get("daily", cur.get("notif_daily", 1))) else 0
                notif_content = 1 if bool(notifications.get("content", cur.get("notif_content", 1))) else 0
                notif_streak = 1 if bool(notifications.get("streak", cur.get("notif_streak", 1))) else 0
                notif_tips = 1 if bool(notifications.get("tips", cur.get("notif_tips", 0))) else 0
                consent_given = 1 if bool(payload.get("consent_given", cur.get("consent_given", 1))) else 0
                now = time.time()
                conn.execute(
                    """
                    INSERT INTO student_settings (
                        student_user_id, language, theme, level, goal, reminders,
                        notif_daily, notif_content, notif_streak, notif_tips, consent_given,
                        updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT (student_user_id) DO UPDATE SET
                        language = excluded.language,
                        theme = excluded.theme,
                        level = excluded.level,
                        goal = excluded.goal,
                        reminders = excluded.reminders,
                        notif_daily = excluded.notif_daily,
                        notif_content = excluded.notif_content,
                        notif_streak = excluded.notif_streak,
                        notif_tips = excluded.notif_tips,
                        consent_given = excluded.consent_given,
                        updated_at = excluded.updated_at
                    """,
                    (
                        student_id,
                        language,
                        theme,
                        level,
                        goal,
                        reminders,
                        notif_daily,
                        notif_content,
                        notif_streak,
                        notif_tips,
                        consent_given,
                        now,
                    ),
                )
                extra_sets: list[str] = []
                extra_vals: list[object] = []
                if "vocab_diary" in payload:
                    dj = _validate_vocab_diary(payload.get("vocab_diary"))
                    extra_sets.append("vocab_diary_json = ?")
                    extra_vals.append(json.dumps(dj, ensure_ascii=False))
                if "dictionary_last_categories" in payload:
                    dc = _validate_dictionary_categories(payload.get("dictionary_last_categories"))
                    extra_sets.append("dictionary_categories_json = ?")
                    extra_vals.append(json.dumps(dc, ensure_ascii=False))
                if "avi_chat_messages" in payload:
                    cm = _validate_avi_chat_messages(payload.get("avi_chat_messages"))
                    blob = json.dumps(cm, ensure_ascii=False)
                    if len(blob.encode("utf-8")) > _MAX_AVI_CHAT_JSON:
                        cm = cm[:40]
                        blob = json.dumps(cm, ensure_ascii=False)
                    extra_sets.append("avi_chat_json = ?")
                    extra_vals.append(blob)
                if extra_sets:
                    extra_vals.append(now)
                    extra_vals.append(student_id)
                    conn.execute(
                        "UPDATE student_settings SET "
                        + ", ".join(extra_sets)
                        + ", updated_at = ? WHERE student_user_id = ?",
                        tuple(extra_vals),
                    )
                conn.commit()
                return {"ok": True}, 200
            if route == "/api/student/change-password":
                new_password = str(payload.get("new_password") or "")
                current_password = str(payload.get("current_password") or "")
                if len(new_password) > 256:
                    return {"error": "La nueva contraseña es demasiado larga."}, 400
                pol = auth_password_policy_violation(new_password)
                if pol:
                    return {"error": pol}, 400
                row = conn.execute("SELECT password_hash FROM users WHERE id = ?", (student_id,)).fetchone()
                if not row:
                    return {"error": "Usuario no encontrado."}, 404
                if row["password_hash"] and current_password:
                    if not auth_verify_password(current_password, row["password_hash"]):
                        return {"error": "Contraseña actual incorrecta."}, 400
                conn.execute("UPDATE users SET password_hash = ? WHERE id = ?", (auth_hash_password(new_password), student_id))
                conn.commit()
                return {"ok": True}, 200
            if route == "/api/student/delete-account":
                conn.execute("UPDATE users SET active = 0 WHERE id = ?", (student_id,))
                conn.execute("DELETE FROM sessions WHERE user_id = ?", (student_id,))
                conn.commit()
                return {"ok": True}, 200
        finally:
            conn.close()
    return {"error": "Not found"}, 404


class AVIHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        acao = _cors_allow_origin(self)
        if acao is None and CORS_ALLOWED_ORIGINS:
            data = {"error": "Origen no autorizado para la API (revisa AVI_CORS_ORIGINS en el servidor)."}
            status = 403
            acao = None
        payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        if acao:
            self.send_header("Access-Control-Allow-Origin", acao)
            if CORS_ALLOWED_ORIGINS:
                self.send_header("Vary", "Origin")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def _send_file(self, path: Path, content_type: str):
        if not path.exists():
            self.send_error(404, "File not found")
            return
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _content_type(self, path: Path) -> str:
        content_map = {
            ".css": "text/css; charset=utf-8",
            ".js": "application/javascript; charset=utf-8",
            ".html": "text/html; charset=utf-8",
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".svg": "image/svg+xml",
            ".ico": "image/x-icon",
            ".webp": "image/webp",
            ".json": "application/json; charset=utf-8",
        }
        return content_map.get(path.suffix.lower(), "application/octet-stream")

    def _send_react_app(self, route: str) -> bool:
        if not FRONTEND_DIST_DIR.exists():
            return False
        requested = (FRONTEND_DIST_DIR / route.lstrip("/")).resolve()
        dist_root = FRONTEND_DIST_DIR.resolve()
        if str(requested).startswith(str(dist_root)) and requested.is_file():
            self._send_file(requested, self._content_type(requested))
            return True
        self._send_file(FRONTEND_DIST_DIR / "index.html", "text/html; charset=utf-8")
        return True

    def do_OPTIONS(self):
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api"):
            acao = _cors_allow_origin(self)
            if acao is None and CORS_ALLOWED_ORIGINS:
                self.send_error(403, "CORS origin not allowed")
                return
            self.send_response(204)
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
            self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
            if acao:
                self.send_header("Access-Control-Allow-Origin", acao)
                if CORS_ALLOWED_ORIGINS:
                    self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Max-Age", "86400")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            return
        self.send_error(404, "Route not found")

    def do_HEAD(self):
        """Render y otros proxies usan HEAD para health checks; sin esto: 501 Unsupported method ('HEAD')."""
        parsed = urlparse(self.path)
        route = parsed.path

        if route == "/api/health":
            acao = _cors_allow_origin(self)
            if acao is None and CORS_ALLOWED_ORIGINS:
                self.send_response(403)
                self.end_headers()
                return
            body = json.dumps(
                {
                    "status": "ok",
                    "corpus_entries": len(ENGINE.rows),
                    "categories": len(ENGINE.by_category.keys()),
                    "model": ENGINE.model.get("model_name", "runtime"),
                    "training_rows": ENGINE.model.get("training_rows", 0),
                    "solo_png_count": solo_images_bootstrap.png_count(SOLO_IMG_DIR),
                    "solo_images_ready": solo_images_bootstrap.is_corpus_complete(SOLO_IMG_DIR),
                    "solo_bootstrap": solo_images_bootstrap.bootstrap_status(),
                    "firebase_storage": firebase_storage_urls.firebase_storage_enabled(),
                    "solo_img_cdn": firebase_storage_urls.cdn_base() or None,
                    "message": "AVI operativo",
                },
                ensure_ascii=False,
            ).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            if acao:
                self.send_header("Access-Control-Allow-Origin", acao)
                if CORS_ALLOWED_ORIGINS:
                    self.send_header("Vary", "Origin")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
            self.send_header("X-Frame-Options", "SAMEORIGIN")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            return

        if route in ("/", "/index.html"):
            p = STATIC_DIR / "index.html"
            if not p.exists():
                self.send_error(404, "File not found")
                return
            data = p.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
            self.send_header("X-Frame-Options", "SAMEORIGIN")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            return

        self.send_error(404, "Route not found")

    def do_POST(self):
        parsed = urlparse(self.path)
        route = parsed.path
        if route.startswith("/api/auth"):
            rate_routes = (
                "/api/auth/login",
                "/api/auth/register",
                "/api/auth/google",
                "/api/auth/forgot-password",
                "/api/auth/verify-reset-code",
                "/api/auth/reset-password",
            )
            if route in rate_routes:
                ok_rl, rl_msg = auth_rate_allow(self)
                if not ok_rl:
                    self._send_json({"error": rl_msg}, 429)
                    return
        data = api_read_json(self)
        if route.startswith("/api/auth"):
            if route == "/api/auth/register":
                payload, status = auth_handle_register(self, data)
                self._send_json(payload, status)
                return
            if route == "/api/auth/login":
                payload, status = auth_handle_login(self, data)
                self._send_json(payload, status)
                return
            if route == "/api/auth/google":
                payload, status = auth_handle_google(self, data)
                self._send_json(payload, status)
                return
            if route == "/api/auth/logout":
                payload, status = auth_handle_logout(self)
                self._send_json(payload, status)
                return
            if route == "/api/auth/forgot-password":
                payload, status = auth_handle_forgot(self, data)
                self._send_json(payload, status)
                return
            if route == "/api/auth/verify-reset-code":
                payload, status = auth_handle_verify_reset(self, data)
                self._send_json(payload, status)
                return
            if route == "/api/auth/reset-password":
                payload, status = auth_handle_reset_password(self, data)
                self._send_json(payload, status)
                return
            self.send_error(404, "Route not found")
            return

        if route.startswith("/api/teacher/"):
            payload, status = teacher_handle_post(self, route, data)
            self._send_json(payload, status)
            return

        if route.startswith("/api/admin/"):
            payload, status = admin_handle_post(self, route, data)
            self._send_json(payload, status)
            return

        if route == "/api/student/profile-school":
            self.send_error(405, "Use GET")
            return
        if route == "/api/student/activities":
            self.send_error(405, "Use GET")
            return
        if route in ("/api/student/settings", "/api/student/change-password", "/api/student/delete-account"):
            payload, status = student_handle_post(self, route, data)
            self._send_json(payload, status)
            return

        self.send_error(404, "Route not found")

    def do_GET(self):
        parsed = urlparse(self.path)
        route = parsed.path

        if route == "/api/auth/config":
            self._send_json(
                {
                    "googleConfigured": bool(GOOGLE_CLIENT_ID),
                    "googleClientId": GOOGLE_CLIENT_ID,
                },
            )
            return
        if route == "/api/auth/me":
            _, user = auth_resolve_user(self)
            if not user:
                self._send_json({"error": "Sesion invalida o expirada."}, 401)
                return
            self._send_json({"user": user})
            return

        if route == "/api/dictionary/search":
            q = parse_qs(parsed.query).get("q", [""])[0]
            self._send_json(ENGINE.dictionary_search(q))
            return

        if route in (
            "/api/teacher/groups",
            "/api/teacher/students",
            "/api/teacher/group-report",
            "/api/teacher/reports-summary",
            "/api/teacher/grades",
            "/api/teacher/activities",
            "/api/teacher/messaging-state",
        ):
            payload, status = teacher_handle_get(self, route, parsed)
            self._send_json(payload, status)
            return

        if route in (
            "/api/admin/users",
            "/api/admin/cms",
            "/api/admin/stats-dash",
            "/api/admin/grades",
            "/api/admin/content-submissions",
            "/api/admin/groups",
            "/api/admin/audit",
            "/api/admin/mail-history",
            "/api/admin/support-tickets",
        ):
            payload, status = admin_handle_get(self, route)
            self._send_json(payload, status)
            return

        if route in ("/api/student/profile-school", "/api/student/activities", "/api/student/settings", "/api/student/sessions"):
            payload, status = student_handle_get(self, route, parsed)
            self._send_json(payload, status)
            return

        if route == "/api/health":
            self._send_json(
                {
                    "status": "ok",
                    "corpus_entries": len(ENGINE.rows),
                    "categories": len(ENGINE.by_category.keys()),
                    "model": ENGINE.model.get("model_name", "runtime"),
                    "training_rows": ENGINE.model.get("training_rows", 0),
                    "solo_png_count": solo_images_bootstrap.png_count(SOLO_IMG_DIR),
                    "solo_images_ready": solo_images_bootstrap.is_corpus_complete(SOLO_IMG_DIR),
                    "solo_bootstrap": solo_images_bootstrap.bootstrap_status(),
                    "firebase_storage": firebase_storage_urls.firebase_storage_enabled(),
                    "solo_img_cdn": firebase_storage_urls.cdn_base() or None,
                    "message": "AVI operativo",
                }
            )
            return
        if route == "/api/stats":
            self._send_json(ENGINE.stats())
            return

        if not route.startswith("/api/") and self._send_react_app(route):
            return

        if route == "/" or route == "/index.html":
            self._send_file(STATIC_DIR / "index.html", "text/html; charset=utf-8")
            return
        if route in ("/chat", "/chat.html"):
            self._send_file(STATIC_DIR / "chat.html", "text/html; charset=utf-8")
            return
        if route in ("/diccionario", "/diccionario.html"):
            self._send_file(STATIC_DIR / "diccionario.html", "text/html; charset=utf-8")
            return
        if route in ("/actividades", "/actividades.html"):
            self._send_file(STATIC_DIR / "actividades.html", "text/html; charset=utf-8")
            return

        # static asset passthrough
        if route.startswith("/"):
            candidate = (STATIC_DIR / route.lstrip("/")).resolve()
            if str(candidate).startswith(str(STATIC_DIR.resolve())) and candidate.exists():
                self._send_file(candidate, self._content_type(candidate))
                return
        if route == "/api/search":
            q = parse_qs(parsed.query).get("q", [""])[0]
            top_k = parse_qs(parsed.query).get("top_k", ["5"])[0]
            try:
                top_k = max(1, min(int(top_k), 10))
            except ValueError:
                top_k = 5
            result = ENGINE.ask(q, top_k=top_k)
            self._send_json(result)
            return
        if route == "/api/lesson":
            cat = parse_qs(parsed.query).get("category", [""])[0]
            limit = parse_qs(parsed.query).get("limit", ["8"])[0]
            try:
                limit = max(3, min(int(limit), 20))
            except ValueError:
                limit = 8
            result = ENGINE.lesson(cat, limit=limit)
            self._send_json(result)
            return
        if route == "/api/dictionary/full":
            qs = parse_qs(parsed.query)
            lim_raw = (qs.get("limit") or ["12000"])[0]
            try:
                lim_i = int(lim_raw)
            except ValueError:
                lim_i = 12000
            terms = ENGINE.lexicon_terms_flat(lim_i)
            self._send_json({"terms": terms, "count": len(terms)})
            return
        if route == "/api/dictionary":
            cat = parse_qs(parsed.query).get("category", [""])[0]
            limit = parse_qs(parsed.query).get("limit", ["12"])[0]
            try:
                lim = int(limit)
            except ValueError:
                lim = 12
            # limit=0 -> todos los terminos lexicos de la categoria
            if lim != 0:
                lim = max(1, min(lim, 500_000))
            result = ENGINE.lesson(cat, limit=lim)
            self._send_json(result)
            return
        if route == "/api/activity":
            cat = parse_qs(parsed.query).get("category", [""])[0]
            limit = parse_qs(parsed.query).get("limit", ["5"])[0]
            diff = parse_qs(parsed.query).get("difficulty", ["intermedio"])[0]
            mode = parse_qs(parsed.query).get("mode", ["quiz"])[0]
            try:
                limit = max(3, min(int(limit), 12))
            except ValueError:
                limit = 5
            result = ENGINE.activity(cat, limit=limit, difficulty=diff, mode=mode)
            self._send_json(result)
            return
        if route == "/api/dialogues":
            cat = parse_qs(parsed.query).get("category", [""])[0]
            limit = parse_qs(parsed.query).get("limit", ["6"])[0]
            try:
                limit = max(1, min(int(limit), 20))
            except ValueError:
                limit = 6
            result = ENGINE.dialogues(cat, limit=limit)
            self._send_json(result)
            return
        if route.startswith("/api/corpus-img/"):
            rel = route[len("/api/corpus-img/") :].lstrip("/")
            rel = unquote(rel).replace("\\", "/").lstrip("/")
            if not firebase_storage_urls.is_safe_corpus_rel_path(rel):
                self.send_error(400, "Bad path")
                return
            try:
                p = (SOLO_IMG_DIR / rel).resolve()
                root = SOLO_IMG_DIR.resolve()
            except OSError:
                self.send_error(500)
                return
            if not str(p).startswith(str(root)) or not p.is_file():
                fb = firebase_storage_urls.firebase_corpus_image_url(rel)
                if fb:
                    acao = _cors_allow_origin(self)
                    self.send_response(302)
                    self.send_header("Location", fb)
                    self.send_header("Cache-Control", "public, max-age=604800")
                    if acao:
                        self.send_header("Access-Control-Allow-Origin", acao)
                    self.end_headers()
                    return
                self.send_error(404, "PNG no encontrado")
                return
            if p.suffix.lower() != ".png":
                self.send_error(404, "Solo PNG")
                return
            try:
                st = p.stat()
            except OSError:
                self.send_error(404)
                return
            etag = f'"{int(st.st_mtime)}-{st.st_size}"'
            inm = self.headers.get("If-None-Match", "").strip()
            acao = _cors_allow_origin(self)
            if inm and inm == etag:
                self.send_response(304)
                self.send_header("ETag", etag)
                self.send_header("Cache-Control", "public, max-age=604800, immutable")
                if acao:
                    self.send_header("Access-Control-Allow-Origin", acao)
                self.end_headers()
                return
            data = p.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "image/png")
            self.send_header("Cache-Control", "public, max-age=604800, immutable")
            self.send_header("ETag", etag)
            self.send_header("X-Content-Type-Options", "nosniff")
            if acao:
                self.send_header("Access-Control-Allow-Origin", acao)
                if CORS_ALLOWED_ORIGINS:
                    self.send_header("Vary", "Origin")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        if route == "/api/image":
            q = parse_qs(parsed.query).get("q", [""])[0]
            cat = parse_qs(parsed.query).get("category", [""])[0]
            tid = (parse_qs(parsed.query).get("id") or [""])[0]
            self._send_json(fetch_commons_image(q, cat, tid))
            return

        self.send_error(404, "Route not found")


def run():
    init_auth_db()
    server = HTTPServer((HOST, PORT), AVIHandler)
    print(f"AVI web app corriendo en http://{HOST}:{PORT}")
    print(
        "[AVI] Entra SOLO en esa URL. Si usas Live Server, abrir index.html o python -m http.server, "
        "el login muestra Error 501 (no existe API en ese servidor).\n"
        "[AVI] Opcion npm run dev: el backend PYTHON debe estar en marcha para /api.",
    )
    if os.environ.get("AVI_SKIP_DEMO_USERS", "").strip().lower() not in ("1", "true", "yes"):
        auth_write_demo_credentials_file()
        print(
            "[AVI] Demo — estudiante: estudiante.demo@nasayuwe.local | docente: docente.demo@nasayuwe.local | "
            f"admin: admin.demo@nasayuwe.local | contraseña cuentas base: {DEMO_LOGIN_PASSWORD}\n"
            f"[AVI] Docentes con panel lleno (grupos + actividades): "
            f"docente.ana@nasayuwe.local, docente.carlos@nasayuwe.local, docente.lucia@nasayuwe.local | "
            f"contraseña: {DEMO_TEACHER_PANEL_PASSWORD}",
        )
    print(
        f"[AVI] Seguridad: rate-limit auth {AUTH_RL_MAX}/{int(AUTH_RL_WINDOW_SEC)}s por IP | "
        f"CORS={'lista AVI_CORS_ORIGINS' if CORS_ALLOWED_ORIGINS else '* (desarrollo)'}",
    )
    if firebase_storage_urls.remote_images_enabled():
        src = firebase_storage_urls.cdn_base() or os.environ.get("FIREBASE_STORAGE_BUCKET", "")
        print(f"[AVI] Imagenes del diccionario via CDN remoto ({src})", flush=True)
    else:
        solo_images_bootstrap.start_background_fetch(SOLO_IMG_DIR)
    server.serve_forever()


if __name__ == "__main__":
    run()
