import csv
import json
import math
import os
import random
import re
import secrets
from avi_db import USE_POSTGRES, connect_auth, insert_returning_id, scalar_from_row
import threading
import time
import hashlib
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, urlparse


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


# Combinan varias categorias del CSV bajo un slug de UI (mas terminos en pantalla)
VIRTUAL_CATEGORIES = {
    "comida": ("alimentos", "frutas_verduras"),
}

# Palabras frecuentes en espanol (vocab por tema)
ESP_STOP_QUERY = {
    "el", "la", "los", "las", "un", "una", "unos", "unas", "de", "y", "del", "al", "a", "en", "lo", "o",
    "le", "les", "con", "por", "para", "se", "su", "sus", "al", "como", "más", "mas",
}

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
    "arracacha": "arracacha", "choclo": "corn on the cob", "chicha": "fermented corn drink",
    "quinua": "quinoa", "quinoa": "quinoa", "camote": "sweet potato", "batata": "sweet potato",
    "remolacha": "beet", "zanahoria": "carrot", "apio": "celery", "espinaca": "spinach",
    "coliflor": "cauliflower", "brocoli": "broccoli", "brócoli": "broccoli", "repollo": "cabbage",
    "aji": "chili pepper", "ají": "chili pepper",
}

ANIMAL_ES_A_EN = {
    "gato": "cat", "perro": "dog", "pez": "fish", "vaca": "cow", "caballo": "horse", "oso": "bear", "leon": "lion", "león": "lion",
    "pajaro": "bird", "pájaro": "bird", "oveja": "sheep", "cerdo": "pig", "rana": "frog", "serpiente": "snake", "pato": "duck",
    "gallina": "chicken", "gallo": "rooster", "tortuga": "turtle", "conejo": "rabbit", "cabra": "goat", "elefante": "elephant",
}


def _core_phrase_for_image(q: str) -> str:
    """Quita Articulos y deja 2–5 palabras con significado para buscar en Commons."""
    toks = [t for t in tokenize(q) if t not in ESP_STOP_QUERY]
    if not toks:
        toks = [t for t in tokenize(q) if t]
    return " ".join(toks[:5])


def _image_cat_hint_ui(cat: str) -> str:
    c = normalize_text(cat)
    if c == "comida" or c == "frutas_verduras":
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
    if k in ALIMENTO_ES_A_EN:
        return "food", ALIMENTO_ES_A_EN[k]
    if k in ANIMAL_ES_A_EN:
        return "animal", ANIMAL_ES_A_EN[k]
    return None, None


def fetch_commons_image(query: str, category: str = ""):
    """
    Imagen de Wikimedia Commons, con busqueda guiada por tema y puntuacion estricta
    (evita iconos, mapas o resultados con poca relacion).
    """
    core = _core_phrase_for_image(query or "")
    q = normalize_text(core) or normalize_text(query or "")
    cat = normalize_text(category)
    if not q:
        return {"ok": False, "message": "query vacia"}
    cache_key = f"{q}|{cat}"
    if cache_key in IMAGE_CACHE:
        return IMAGE_CACHE[cache_key]

    cat_hint = _image_cat_hint_ui(category)
    toks = tokenize(q)
    first = normalize_text(toks[0]) if toks else ""

    # Solo Commons si el primer término está en un glosario (evita mapas, documentos, ruido).
    gkind, gval = _gloss_lookup(first)
    if gkind is None:
        r = {"ok": False, "message": "sin mapeo de imagen (se muestra icono en la app)"}
        IMAGE_CACHE[cache_key] = r
        return r
    if gkind == "num":
        search_q = f"{gval} number"
    elif gkind == "color":
        search_q = f"{gval} color"
    elif gkind == "food":
        gv = str(gval)
        search_q = gv if (" " in gv or len(gv) > 14) else f"{gv} food"
    else:
        search_q = f"{gval} animal"

    api_url = (
        "https://commons.wikimedia.org/w/api.php"
        "?action=query"
        "&format=json"
        "&generator=search"
        "&gsrnamespace=6"
        f"&gsrsearch={quote(search_q)}"
        "&gsrlimit=24"
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
        IMAGE_CACHE[cache_key] = result
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
    match_tokens = set(q_tokens) | en_extra

    banned_title = {
        "logo", "icon", "symbol", "flag", "map", "escudo", "vector", "svg", "diagram", "chart",
        "coa", "coat", "arms", "fountain", "pennon", "route", "highway", "location", "crystal",
        "document", "manuscript", "parchment", "scroll", "letter", "facsimile", "monument",
    }
    ranked = []

    for page in pages.values():
        infos = page.get("imageinfo") or []
        if not infos:
            continue
        info = infos[0]
        title_raw = page.get("title", "")
        title = title_raw.replace("File:", "")
        title_norm = normalize_text(title)
        title_tokens = set(tokenize(title_norm))
        if title_tokens & banned_title:
            continue
        if int(info.get("width", 0) or 0) < 200 or int(info.get("height", 0) or 0) < 200:
            continue

        overlap = len(match_tokens & title_tokens)
        en_overlap = 0
        for w in toks:
            wn = normalize_text(w)
            for enp in (ALIMENTO_ES_A_EN.get(wn), ANIMAL_ES_A_EN.get(wn), COLOR_ES_A_EN.get(wn)):
                if enp and str(enp) and normalize_text(str(enp)) in title_norm:
                    en_overlap += 2
        exact_bonus = 0
        if first and first in title_norm:
            exact_bonus = 4
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
        if score < 1 and (q_tokens and overlap == 0 and en_overlap == 0):
            continue
        ranked.append((score, candidate))

    ranked.sort(key=lambda x: x[0], reverse=True)
    if ranked and ranked[0][0] >= 3:
        result = ranked[0][1]
        IMAGE_CACHE[cache_key] = result
        return result

    result = {"ok": False, "message": "no se encontro imagen adecuada"}
    IMAGE_CACHE[cache_key] = result
    return result


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
                cat = row.get("categoria", "general")
                record_type = row.get("record_type", "lexico")
                source = row.get("fuente_nombre", "desconocida")

                text = f"{nasa} {esp} {cat} {record_type}"
                toks = set(tokenize(text))
                if not toks:
                    continue

                self.rows.append(
                    {
                        "idx": i,
                        "id": rid,
                        "nasa_yuwe": nasa,
                        "espanol": esp,
                        "categoria": cat,
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
                self.by_category[cat].append(i)

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
            return {"answer": "Por favor escribe una pregunta.", "contexts": []}

        cached = self._cached(query_norm)
        if cached:
            cached["meta"]["cache_hit"] = True
            self.metrics["cache_hit"] += 1
            return cached

        q_tokens = tokenize(query_norm)
        translation_intent = (
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

        # direct lexical optimization for "como se dice X en nasa yuwe"
        direct_target = None
        m = re.search(r"dice (.+?) en nasa yuwe", query_norm)
        if m:
            direct_target = normalize_text(m.group(1))
        if not direct_target:
            m2 = re.search(r"traduce (.+?) a nasa yuwe", query_norm)
            if m2:
                direct_target = normalize_text(m2.group(1))
        if not cand:
            data = {
                "answer": "No encontre contexto suficiente en el corpus. Intenta con una pregunta mas especifica.",
                "contexts": [],
                "meta": {"cache_hit": False, "candidates": 0},
            }
            self.cache[query_norm] = {"time": time.time(), "data": data}
            self.metrics["empty_result"] += 1
            return data

        scored = []
        for doc_id in cand:
            row_doc = self.rows[doc_id]
            if translation_intent and row_doc.get("record_type", "").strip().lower() in {"qa", "dialogo"}:
                # avoid generated conversational records when user asks direct lexical translation
                continue
            if direct_target and row_doc.get("record_type", "").strip().lower() == "lexico":
                # boost direct match in spanish gloss
                if row_doc.get("espanol_norm") == direct_target:
                    scored.append((doc_id, 999.0))
                    continue
            sc = self._score(q_tokens, doc_id, pedagogical_intent=pedagogical_intent)
            if sc > 0:
                scored.append((doc_id, sc))
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

        # Tutor response template
        best = contexts[0] if contexts else None
        if best and best.get("record_type") == "dialogo":
            answer = (
                "Encontré un diálogo pedagógico útil para practicar: "
                f"{best['nasa_yuwe']} "
                f"Referencia en español: {best['espanol']} "
                f"Fuente: {best['fuente_nombre']} ({best.get('source_kind', 'sin tipo')})."
            )
        elif best:
            answer = (
                f"En el corpus encuentro como referencia principal: "
                f"'{best['espanol']}' -> '{best['nasa_yuwe']}'. "
                f"Categoria: {best['categoria']}. "
                f"Fuente: {best['fuente_nombre']} ({best.get('source_kind', 'sin tipo')}). "
                f"Te sugiero practicar esta expresion en una frase corta y comparar con los ejemplos mostrados."
            )
        else:
            answer = "No encontre una respuesta confiable en el corpus."

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
                {
                    "id": row["id"],
                    "nasa_yuwe": row["nasa_yuwe"],
                    "espanol": row["espanol"],
                    "fuente_nombre": row["fuente_nombre"],
                }
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
                entry = {
                    "id": row.get("id"),
                    "espanol": row.get("espanol", ""),
                    "nasa_yuwe": row.get("nasa_yuwe", ""),
                    "categoria": row.get("categoria", ""),
                    "fuente_nombre": row.get("fuente_nombre", ""),
                }
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

        if len(lex_rows) < max(4, num_opts):
            return {
                "category": cat_norm,
                "questions": [],
                "message": "No hay suficientes terminos para actividad.",
                "mode": act_mode,
                "difficulty": diff,
            }

        random.shuffle(lex_rows)
        cap = max(limit, num_opts + 1)
        base = lex_rows[: max(cap, 5)]
        all_answers = [r["nasa_yuwe"] for r in lex_rows if r.get("nasa_yuwe")]
        questions = []
        qid = 1
        for row in base[:limit]:
            answer = row["nasa_yuwe"]
            es = row.get("espanol", "") or ""
            distractors = [x for x in all_answers if x and x != answer]
            random.shuffle(distractors)
            if diff == "avanzado" and len(answer) > 2:
                ln = len(answer)
                closer = [x for x in distractors if abs(len(x) - ln) <= 2]
                pool = closer if len(closer) >= n_distractors else distractors
            else:
                pool = distractors
            picks = pool[:n_distractors]
            options = [answer] + picks
            random.shuffle(options)

            if act_mode == "quiz":
                prompt = f"Selecciona la traduccion en Nasa Yuwe para: '{es}'"
                q = {
                    "id": f"{cat_norm}-{qid}",
                    "type": "quiz",
                    "prompt": prompt,
                    "answer": answer,
                    "options": options[:num_opts],
                    "categoria": cat_norm,
                    "espanol": es,
                }
            elif act_mode == "completar":
                prompt = f"Completa: La expresion en Nasa Yuwe que corresponde a '{es}' es _____"
                q = {
                    "id": f"{cat_norm}-c-{qid}",
                    "type": "completar",
                    "prompt": prompt,
                    "answer": answer,
                    "options": options[:num_opts],
                    "categoria": cat_norm,
                    "espanol": es,
                }
            else:
                img = fetch_commons_image(es, cat_norm)
                img_ok = bool(img.get("ok")) if isinstance(img, dict) else False
                q = {
                    "id": f"{cat_norm}-i-{qid}",
                    "type": "imagen",
                    "prompt": f"Asocia la imagen con la palabra en Nasa Yuwe relacionada con '{es}'",
                    "answer": answer,
                    "options": options[:num_opts],
                    "categoria": cat_norm,
                    "espanol": es,
                    "image_url": img.get("image_url") if isinstance(img, dict) else None,
                    "image_ok": img_ok,
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
                    updated_at REAL NOT NULL
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
            f"Contraseña para los tres usuarios: {DEMO_LOGIN_PASSWORD}\n\n",
        ]
        for email, _dn, role in DEMO_ACCOUNTS:
            lines.append(f"  {email}  ({role})\n")
        lines.append(
            "\nSe crean solas la primera vez que inicias server.py "
            "(excepto si AVI_SKIP_DEMO_USERS=1).\n",
        )
        path.write_text("".join(lines), encoding="utf-8")
    except OSError:
        pass


def auth_seed_demo_users() -> None:
    if os.environ.get("AVI_SKIP_DEMO_USERS", "").strip().lower() in ("1", "true", "yes"):
        return
    auth_write_demo_credentials_file()
    now = time.time()
    created = []
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
            conn.commit()
        finally:
            conn.close()
    if created:
        print(
            f"[AVI] Creadas {len(created)} cuentas de prueba. "
            f"Contraseña: {DEMO_LOGIN_PASSWORD} — ver {AUTH_DB_PATH.parent / 'CUENTAS_PRUEBA.txt'}",
        )


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
    if len(password) < 8:
        return {"error": "La contraseña debe tener al menos 8 caracteres."}, 400
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
            uid = insert_returning_id(
                conn,
                """
                INSERT INTO users (
                    email, password_hash, google_sub, display_name, role, created_at, active, email_verified
                ) VALUES (?, ?, NULL, ?, ?, ?, 1, 1)
                """,
                (email, ph, dn, role, now),
            )
            conn.commit()
            tok = auth_create_session(conn, uid)
            row = conn.execute(
                """
                SELECT id, email, display_name, role, COALESCE(active,1) AS active,
                       COALESCE(email_verified,1) AS email_verified
                FROM users WHERE id = ?
                """,
                (uid,),
            ).fetchone()
        finally:
            conn.close()
    return (
        {
            "token": tok,
            "user": auth_row_to_user(row),
            "message": "Registro Exitoso.",
            "verification_email_sent": False,
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
    with _AUTH_DB_LOCK:
        conn = auth_connect()
        try:
            row = conn.execute(
                "SELECT id FROM users WHERE email = ? AND COALESCE(active, 1) = 1",
                (email,),
            ).fetchone()
            if not row:
                return {"error": "Correo electrónico invalido"}, 400
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
    print(f"[AVI recuperacion] {email}: codigo {code} (consola servidor; usar en demo)")
    return {"message": "Correo electrónico enviado"}, 200


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
    if len(pw) < 8:
        return {"error": "La contraseña debe tener al menos 8 caracteres."}, 400
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
                edu = (data.get("education_level") or "").strip() or "General"
                grade = (data.get("grade") or "").strip()
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
                    SELECT id, email, display_name FROM users
                    WHERE role = 'estudiante' AND COALESCE(active, 1) = 1
                      AND (LOWER(display_name) LIKE ? OR LOWER(email) LIKE ?)
                    ORDER BY display_name LIMIT 80
                    """,
                    (like, like),
                ).fetchall()
                students = [{"id": r["id"], "email": r["email"], "display_name": r["display_name"]} for r in rows]
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
            finally:
                conn.close()
        return {"activities": acts}, 200
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
            finally:
                conn.close()
        return {
            "group": {"id": int(g["id"]), "name": g["name"]},
            "students": roster,
            "summary": {
                "total_estudiantes": len(roster),
                "promedio_actividades": "—",
                "nota": "Complementar con registros locales de práctica cuando estén enlazados.",
            },
        }, 200
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
                if not title:
                    return {"error": "Titulo requerido"}, 400
                cid = data.get("id")
                now = time.time()
                if cid is not None and str(cid).isdigit():
                    cid_i = int(cid)
                    conn.execute(
                        "UPDATE cms_items SET kind = ?, title = ?, body = ?, updated_at = ? WHERE id = ?",
                        (kind, title, body, now, cid_i),
                    )
                    admin_audit_insert(conn, user, "CMS_UPDATE", f"id={cid_i} titulo={title[:120]}")
                else:
                    new_id = insert_returning_id(
                        conn,
                        "INSERT INTO cms_items (kind, title, body, updated_at) VALUES (?, ?, ?, ?)",
                        (kind, title, body, now),
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
                        "INSERT INTO cms_items (kind, title, body, updated_at) VALUES (?, ?, ?, ?)",
                        (row["kind"] or "termino", title, "\n".join(body_lines), now),
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
                if len(pw) < 8:
                    return {"error": "La contraseña debe tener al menos 8 caracteres."}, 400
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
                    "SELECT id, kind, title, body, updated_at FROM cms_items ORDER BY updated_at DESC LIMIT 300"
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
            finally:
                conn.close()
        st = ENGINE.stats()
        total_entries = len(ENGINE.rows)
        if n_users == 0:
            payload = {"message": "No existen estadísticas disponibles", "empty": True}
        else:
            payload = {
                "empty": False,
                "platform": {
                    "usuarios_registrados": n_users,
                    "estudiantes": n_st,
                    "docentes": n_dc,
                    "administradores": n_ad,
                    "cuentas_activas": n_act,
                },
                "corpus": {
                    "entradas": total_entries,
                    "categorias": st.get("categories", 0),
                },
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
                rows = conn.execute(
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
                return {"activities": [{k: r[k] for k in r.keys()} for r in rows]}, 200
            if route == "/api/student/settings":
                row = conn.execute(
                    """
                    SELECT language, theme, level, goal, reminders,
                           notif_daily, notif_content, notif_streak, notif_tips, consent_given
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
                curr = conn.execute(
                    """
                    SELECT language, theme, level, goal, reminders,
                           notif_daily, notif_content, notif_streak, notif_tips, consent_given
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
                    ON CONFLICT(student_user_id) DO UPDATE SET
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
                conn.commit()
                return {"ok": True}, 200
            if route == "/api/student/change-password":
                new_password = str(payload.get("new_password") or "")
                current_password = str(payload.get("current_password") or "")
                if len(new_password) < 8:
                    return {"error": "La nueva contraseña debe tener al menos 8 caracteres."}, 400
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
            "/api/teacher/grades",
            "/api/teacher/activities",
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
        if route == "/api/image":
            q = parse_qs(parsed.query).get("q", [""])[0]
            cat = parse_qs(parsed.query).get("category", [""])[0]
            self._send_json(fetch_commons_image(q, cat))
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
            f"admin: admin.demo@nasayuwe.local | contraseña: {DEMO_LOGIN_PASSWORD}",
        )
    print(
        f"[AVI] Seguridad: rate-limit auth {AUTH_RL_MAX}/{int(AUTH_RL_WINDOW_SEC)}s por IP | "
        f"CORS={'lista AVI_CORS_ORIGINS' if CORS_ALLOWED_ORIGINS else '* (desarrollo)'}",
    )
    server.serve_forever()


if __name__ == "__main__":
    run()
