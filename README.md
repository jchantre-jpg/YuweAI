# YuweAI

Código fuente del asistente virtual inteligente (**AVI**) para enseñanza de **Nasa Yuwe**: aplicación **web** (Python + React/Vite) y envoltorio **móvil** (Expo / WebView).

Repositorio público: [github.com/jchantre-jpg/YuweAI](https://github.com/jchantre-jpg/YuweAI)

## Contenido

| Carpeta | Descripción |
|--------|---------------|
| [`web/`](web/) | Backend (`server.py`), API JSON, `frontend/` (React + Vite), `static/`, modelos y scripts. |
| [`mobile/`](mobile/) | App Expo que abre la misma interfaz web en un `WebView` dentro de la red local. |

No se incluye el **corpus** completo ni la memoria de grado: coloca el CSV según [`web/README.md`](web/README.md) o la ruta que configures.

## Requisitos

- Python 3.x y `pip install -r web/requirements.txt`
- Node.js LTS para `npm install` en `web/frontend` y en `mobile/`

## Inicio rápido

1. Backend: `cd web` → `python server.py` (puerto **8090** por defecto).
2. Frontend desarrollo: en otra terminal, `cd web/frontend` → `npm install` → `npm run dev`.
3. Móvil: `cd mobile` → `npm install` → `npx expo start --host lan` (ajusta `mobile/app.json` con la IP de tu PC).

Detalle en los README de cada carpeta.

## Licencia

Define la licencia aquí si aplica (p. ej. MIT) según acuerdos institucionales y comunitarios.
