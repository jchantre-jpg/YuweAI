# Imágenes **solo tema** (sin personas)

Carpeta paralela a `generadas-img-ia/`: mismas rutas lógicas `\<categoria\>\<lema\>.png`, pero las ilustraciones muestran **únicamente el objeto del léxico** (lechuga, animal, herramienta…), **sin** personajes Nasa ni manos.

## Ver imagenes locales en la app (diccionario)

El backend (`web/server.py`) resuelve `/api/image` asi:

1. Si existe `term_image_routes.json` y un PNG bajo `corpus/generadas-img-ia-solo/`, se sirve por **`/api/corpus-img/...`** (prioridad sobre Wikimedia).
2. Si no hay PNG local, se sigue usando **Commons** (licencia abierta) como antes.

Regenerar el indice tras cambiar el MD o el JSONL:

```bash
python scripts/export_prompts_solo_desde_lexico_md.py
python scripts/export_term_image_map.py
```

**Despliegue:** sube al servidor la carpeta completa `corpus/generadas-img-ia-solo/` (PNG + `term_image_routes.json`) junto al codigo. Opcional: variable de entorno `AVI_SOLO_IMG_DIR` apuntando a esa carpeta si no esta dentro del repo en el host.

El cliente React pasa `id` del termino en `/api/image` para desambiguar gloss duplicados.

## Convención de export desde Cursor (assets)

Al generar en el IDE, guarda el PNG en assets con este nombre:

`solo__<categoria>__<lema>.png`

Ejemplos:

- `solo__frutas_verduras__lechuga.png` → `frutas_verduras/lechuga.png`
- `solo__alimentos__arracacha.png` → `alimentos/arracacha.png`

Luego (desde la carpeta `YuweAI`):

```bash
python scripts/sync_solo_imagenes_desde_assets.py
```

Para generar en lote los prompts alineados al `manifest.json` de `generadas-img-ia/`:

```bash
python scripts/export_prompts_solo_desde_manifest.py
python scripts/export_prompts_solo_desde_manifest.py --limit 100
```

Eso crea `corpus/generadas-img-ia-solo/prompts_solo.jsonl` (una línea JSON por entrada: `asset_filename`, `dest_rel`, `prompt_en`).

**Todo el léxico del MD** (orden del documento, miles de entradas):

```bash
python scripts/export_prompts_solo_desde_lexico_md.py
python scripts/export_prompts_solo_desde_lexico_md.py --limit 500
```

Salida: `corpus/generadas-img-ia-solo/prompts_solo_full.jsonl` (incluye `idx`, `id`, `asset_filename`, `dest_rel`, `prompt_en`). Las primeras 100 líneas coinciden con el lote del `manifest.json`; a partir de la 101 sigue el corpus completo.

## Estilo

Ver `ESTILO_SOLO_TEMA.md` (misma línea visual “app Yuwe”, Pixar-3D educativo, **cero** personas).

**Fondo:** por defecto usamos **blanco sólido** (`#FFFFFF`) en los prompts exportados — **solo el fondo**, no el objeto. Números, frutas, animales, etc. deben ir **coloridos y con buen contraste**; evitar que el tema sea blanco plano sobre blanco (salvo entradas como el color *blanco*). La IA **no asegura** transparencia real; el blanco evita el patrón de **cuadros** que a veces se ve al “transparente”. Si más adelante necesitas PNG con alfa, quita el blanco con una herramienta de recorte.
