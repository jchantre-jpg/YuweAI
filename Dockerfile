# Hugging Face Space (sdk: docker). El build usa la raíz del repositorio YuweAI como contexto.
# Docker Compose en VM sigue usando YuweAI/deploy/Dockerfile (contexto padre con corpus/).
#
# syntax=docker/dockerfile:1
FROM node:22-alpine AS frontend
WORKDIR /build
COPY web/frontend/package.json web/frontend/package-lock.json ./
RUN npm ci
COPY web/frontend/ ./
RUN npm run build

FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m -u 1000 user

# Opcional en Hugging Face: Settings → Variables → Build-time → CORPUS_URL (enlace directo al CSV).
ARG CORPUS_URL=

WORKDIR /app/web

COPY web/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY web/server.py ./
COPY web/avi_db.py ./
COPY web/static ./static/
COPY web/models ./models/
COPY --from=frontend /build/dist ./frontend/dist/

COPY corpus/data /tmp/corpus_in/
RUN mkdir -p /app/corpus/data \
    && if [ -f /tmp/corpus_in/corpus_bilingue_v5.csv ]; then \
         install -D -m644 /tmp/corpus_in/corpus_bilingue_v5.csv /app/corpus/data/corpus_bilingue_v5.csv; \
       elif [ -n "$CORPUS_URL" ]; then \
         curl -fL "$CORPUS_URL" -o /app/corpus/data/corpus_bilingue_v5.csv; \
       else \
         echo "ERROR: Falta corpus_bilingue_v5.csv. Coloca el archivo en corpus/data/ en el repo (Git LFS si pesa mucho) o define CORPUS_URL en el Space (URL de descarga directa del CSV)." && exit 1; \
       fi \
    && rm -rf /tmp/corpus_in \
    && python -c "import pathlib; p=pathlib.Path('/app/corpus/data/corpus_bilingue_v5.csv'); n=sum(1 for _ in p.open(encoding='utf-8'))-1; assert n>=500, ('corpus_bilingue_v5.csv demasiado pequeno (%s filas). Sube el CSV completo a corpus/data/ o usa build-arg CORPUS_URL con URL raw.'%n); print('corpus build OK:', n, 'filas')"

ENV AVI_CORPUS_PATH=/app/corpus/data/corpus_bilingue_v5.csv

# Léxico visual: rutas (JSON/JSONL) y PNG si están en el contexto de build (en Git suelen ir solo metadatos).
COPY corpus/generadas-img-ia-solo/ /app/corpus/generadas-img-ia-solo/

# Opcional (Render / CI): URL HTTPS a un .tar.gz (ver corpus/generadas-img-ia-solo/README.md).
# Acepta tarball con rutas en la raiz (recomendado: tar -C corpus/generadas-img-ia-solo .)
# o con prefijo generadas-img-ia-solo/ (tar -C corpus generadas-img-ia-solo en Windows).
# Render expone las variables del servicio como Docker ARG durante el build (mismo nombre que la env).
ARG SOLO_IMG_TARBALL_URL=
RUN set -eux; \
    if [ -n "$SOLO_IMG_TARBALL_URL" ]; then \
      echo "Downloading SOLO_IMG_TARBALL_URL ..."; \
      curl -fSL "$SOLO_IMG_TARBALL_URL" -o /tmp/solo_img_ia.tar.gz; \
      rm -rf /tmp/solo_ex && mkdir -p /tmp/solo_ex; \
      tar -xzf /tmp/solo_img_ia.tar.gz -C /tmp/solo_ex; \
      if [ -d /tmp/solo_ex/generadas-img-ia-solo ]; then \
        cp -a /tmp/solo_ex/generadas-img-ia-solo/. /app/corpus/generadas-img-ia-solo/; \
      else \
        cp -a /tmp/solo_ex/. /app/corpus/generadas-img-ia-solo/; \
      fi; \
      rm -rf /tmp/solo_ex /tmp/solo_img_ia.tar.gz; \
      python3 -c "import pathlib; p=pathlib.Path('/app/corpus/generadas-img-ia-solo'); n=sum(1 for _ in p.rglob('*.png')); print('solo PNG count:', n); assert n >= 1, 'SOLO_IMG_TARBALL_URL: no se encontro ningun PNG (revisa rutas dentro del .tar.gz)'"; \
    else \
      echo "SOLO_IMG_TARBALL_URL unset; generadas-img-ia-solo solo desde el contexto de build (sin PNG si estan en .gitignore)."; \
    fi

RUN mkdir -p /app/web/data \
    && chown -R user:user /app

USER user
WORKDIR /app/web

EXPOSE 8090
CMD ["python", "server.py"]
