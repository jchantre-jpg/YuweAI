# Contexto de build: carpeta raíz del proyecto (donde están las carpetas YuweAI/ y corpus/).
# Ejemplo: docker compose build desde YuweAI/deploy con context ../..
# Hugging Face Space usa el Dockerfile en la raíz del repo YuweAI: ../Dockerfile (mismo stack, otros paths).
#
# syntax=docker/dockerfile:1
FROM node:22-alpine AS frontend
WORKDIR /build
COPY YuweAI/web/frontend/package.json YuweAI/web/frontend/package-lock.json ./
RUN npm ci
COPY YuweAI/web/frontend/ ./
RUN npm run build

FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app/web

COPY YuweAI/web/server.py ./
COPY YuweAI/web/static ./static/
COPY YuweAI/web/models ./models/
COPY --from=frontend /build/dist ./frontend/dist/

RUN mkdir -p /app/corpus/data /app/corpus/generadas-img-ia-solo /app/web/data
COPY corpus/data/corpus_bilingue_v5.csv /app/corpus/data/
COPY YuweAI/corpus/generadas-img-ia-solo/ /app/corpus/generadas-img-ia-solo/

ENV AVI_CORPUS_PATH=/app/corpus/data/corpus_bilingue_v5.csv

EXPOSE 8090
CMD ["python", "server.py"]
