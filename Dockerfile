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
    && rm -rf /tmp/corpus_in

ENV AVI_CORPUS_PATH=/app/corpus/data/corpus_bilingue_v5.csv

RUN mkdir -p /app/web/data \
    && chown -R user:user /app

USER user
WORKDIR /app/web

EXPOSE 8090
CMD ["python", "server.py"]
