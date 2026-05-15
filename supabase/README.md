# Supabase (esquema preparado)

- **`migrations/20250512000000_initial_schema.sql`**: tablas equivalentes al SQLite de `web/server.py`. Ejecútalo en el **SQL Editor** de tu proyecto Supabase **antes** de definir `DATABASE_URL` en el servidor.
- El backend (`server.py`) usa **PostgreSQL** cuando la variable de entorno **`DATABASE_URL`** está definida; si no, usa SQLite local (`web/avi_db.py`).
- Guía de despliegue conjunta con Render y Firebase: [`deploy/PLATAFORMA-SUPABASE-RENDER-FIREBASE.md`](../deploy/PLATAFORMA-SUPABASE-RENDER-FIREBASE.md).
