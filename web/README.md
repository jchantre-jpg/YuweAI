# App web — AVI (stack completo)

Aquí está **todo el sistema web**: backend Python, base de datos SQLite, estáticos, modelos, scripts y el **frontend React + Vite**.

## Estructura

| Ruta | Rol |
|------|-----|
| `server.py` | API HTTP, autenticación, diccionario, actividades, roles (docente/admin/estudiante), sirve `frontend/dist` y `static/`. |
| `data/` | SQLite (`avi_auth.db`) y archivos de datos / cuentas demo. |
| `static/` | HTML/JS/CSS legacy opcional. |
| `models/` | Modelo de recuperación (`retrieval_model_v1.json`). |
| `scripts/` | Utilidades (build modelo, smoke tests, etc.). |
| `reports/` | Reportes de evaluación. |
| `frontend/` | React + Vite: `npm run dev` / `npm run build`. |
| `requirements.txt` | Dependencias Python. |
| `.env.example` | Variables de entorno de ejemplo. |

El corpus CSV se espera **fuera de este repositorio** (por tamaño y gobernanza), por defecto un nivel arriba de `web/`:

`../corpus/data/corpus_bilingue_v5.csv` (por ejemplo, si clonas `YuweAI` junto a la carpeta `corpus` del proyecto de grado).

## Arranque rápido

Los comandos siguientes asumen que tu terminal está en la carpeta **`web/`** (esta carpeta).

**1. Backend (puerto 8090, escucha en `0.0.0.0` para móvil en LAN):**

```powershell
python server.py
```

**2. Solo interfaz compilada (recomendado para producción local):**

```powershell
cd frontend
npm install
npm run build
cd ..
python server.py
```

Abrir: `http://127.0.0.1:8090`

**3. Desarrollo frontend con recarga en vivo (proxy `/api` → 8090):**

Terminal A (en `web/`): `python server.py`  
Terminal B:

```powershell
cd frontend
npm install
npm run dev
```

Abrir: `http://localhost:5173`

## App móvil (Expo)

La versión móvil vive en **`../mobile/`** (mismo repositorio) y carga esta misma UI vía `WebView`. Ajusta la IP en `mobile\app.json` (`extra.webAppUrl`) para que apunte a tu PC en la red WiFi.

## Nota sobre `avi_webapp/`

En el monorepo [YuweAI](https://github.com/jchantre-jpg/YuweAI), el código activo de producto es **`web/`** y **`mobile/`**.
