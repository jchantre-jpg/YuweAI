# Supabase (esquema preparado)

- **`migrations/20250512000000_initial_schema.sql`**: tablas equivalentes al SQLite de `web/server.py`. Ejecútalo en el **SQL Editor** de tu proyecto Supabase **antes** de definir `DATABASE_URL` en el servidor.
- El backend (`server.py`) usa **PostgreSQL** cuando la variable de entorno **`DATABASE_URL`** está definida; si no, usa SQLite local (`web/avi_db.py`).
- Guía de despliegue conjunta con Render y Firebase: [`deploy/PLATAFORMA-SUPABASE-RENDER-FIREBASE.md`](../deploy/PLATAFORMA-SUPABASE-RENDER-FIREBASE.md).

## Render y `DATABASE_URL` (IPv4)

La URI **directa** (`db.PROJECTREF.supabase.co:5432`) en Supabase es **solo IPv6** por defecto. **Render** (y muchos hosts) **no alcanzan** esa IPv6, así que el servicio falla al arrancar.

**Solución recomendada:** en Supabase → **Connect** → pestaña / método **Session pooler** (Supavisor). Copia la cadena que usa host tipo **`aws-0-REGION.pooler.supabase.com`**, puerto **5432**, usuario **`postgres.PROJECTREF`** (con punto), y pégala en Render como **`DATABASE_URL`** (con `sslmode=require`).

Documentación oficial: [Connect to Postgres](https://supabase.com/docs/guides/database/connecting-to-postgres) (direct vs pooler session mode).
