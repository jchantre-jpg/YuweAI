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

### Render (PNG fuera de Git)

Los PNG suelen estar en `.gitignore`; el build en la nube no los ve. Opcion recomendada: **archivo `.tar.gz` + variable `SOLO_IMG_TARBALL_URL`**.

1. Desde la raiz del repo `YuweAI` (donde estan `corpus/` y `web/`), con la carpeta local completa (incluye PNG):

   ```bash
   tar -czvf solo-img-ia.tar.gz -C corpus generadas-img-ia-solo
   ```

2. Sube `solo-img-ia.tar.gz` a un almacen con **URL de descarga directa** (por ejemplo bucket S3/R2 publico, release en GitHub con asset, Hugging Face con enlace raw que acepte `curl`).

3. En [Render](https://dashboard.render.com) → tu servicio **yuweai-avi-api** → **Environment** → añade:

   - **Key:** `SOLO_IMG_TARBALL_URL`
   - **Value:** la URL HTTPS del `.tar.gz`

   Render inyecta las variables del servicio como **Docker ARG** durante el build: el `Dockerfile` descarga el tarball y lo descomprime sobre `/app/corpus/generadas-img-ia-solo/` antes de arrancar.

4. Vuelve a desplegar (**Manual Deploy** o push a la rama conectada). El build fallara con un mensaje claro si la URL no devuelve un gzip valido o si dentro del archivo no hay ningun `.png` (revisa que el `tar` se creo con `-C corpus generadas-img-ia-solo` para que las rutas relativas coincidan).

Si no defines `SOLO_IMG_TARBALL_URL`, la imagen solo lleva lo que venga en Git (metadatos sin PNG) y la app seguira usando Wikimedia donde no haya archivo local.

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
