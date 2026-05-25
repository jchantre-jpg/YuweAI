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

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/web

COPY YuweAI/web/server.py ./
COPY YuweAI/web/static ./static/
COPY YuweAI/web/models ./models/
COPY --from=frontend /build/dist ./frontend/dist/

RUN mkdir -p /app/corpus/data /app/corpus/generadas-img-ia-solo /app/web/data
COPY corpus/data/corpus_bilingue_v5.csv /app/corpus/data/
COPY YuweAI/corpus/generadas-img-ia-solo/ /app/corpus/generadas-img-ia-solo/

# Misma logica que Dockerfile en la raiz YuweAI (tarball anidado o plano).
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
      python3 -c "import pathlib; p=pathlib.Path('/app/corpus/generadas-img-ia-solo'); n=sum(1 for _ in p.rglob('*.png')); print('solo PNG count:', n); assert n >= 1, 'SOLO_IMG_TARBALL_URL: no se encontro ningun PNG'"; \
    else \
      echo "SOLO_IMG_TARBALL_URL unset; generadas-img-ia-solo solo desde el contexto de build."; \
    fi

ENV AVI_CORPUS_PATH=/app/corpus/data/corpus_bilingue_v5.csv

EXPOSE 8090
CMD ["python", "server.py"]
