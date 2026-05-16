# Supabase + Supabase Storage + Render + Firebase Hosting

Esta guía alinea el stack que elegiste: **PostgreSQL y Storage en Supabase**, **API (Python + Docker) en Render**, **front estático en Firebase Hosting**. Incluye los archivos ya añadidos al repo:

| Ruta | Uso |
|------|-----|
| [`supabase/migrations/20250512000000_initial_schema.sql`](../supabase/migrations/20250512000000_initial_schema.sql) | Esquema PostgreSQL equivalente al SQLite actual (listo para Supabase). |
| [`render.yaml`](../render.yaml) | Blueprint de Render (Web Service Docker en la raíz del repo `YuweAI`). |
| [`web/frontend/firebase.json`](../web/frontend/firebase.json) | Hosting: carpeta `dist` del build de Vite. |
| [`web/frontend/.firebaserc.example`](../web/frontend/.firebaserc.example) | Copia a `.firebaserc` y sustituye el ID de proyecto Firebase. |
| [`web/frontend/.env.production.example`](../web/frontend/.env.production.example) | `VITE_API_BASE` = URL pública de tu API en Render. |
| [`web/avi_db.py`](../web/avi_db.py) | Conmutador SQLite / PostgreSQL según `DATABASE_URL`. |
| [`web/.env.cloud.example`](../web/.env.cloud.example) | Variables para Render (incluye `DATABASE_URL`). |

## Sobre el plan de Render que viste (“A workspace just for you”)

Ese resumen describe el **workspace** de Render: ancho de banda incluido, **2 dominios personalizados** incluidos en esa cuota, minutos de build, varios servicios, etc. Los **excedentes** se facturan según lo indicado (p. ej. $/GB). El **tier free** del servicio web sigue teniendo límites habituales (el servicio puede **dormir** por inactividad, arranque en frío). La **persistencia de la base de datos** la resuelves en **Supabase**, no en el disco efímero del contenedor de Render.

## Estado del código (PostgreSQL)

- Si **`DATABASE_URL`** está definida (cadena de conexión de Supabase, de preferencia **Session pooler** para IPv4 en Render), `server.py` usa **`psycopg`** y el esquema de `supabase/migrations/`. Sin esa variable, sigue usando **SQLite** en `web/data/avi_auth.db`.
- Dependencia añadida: `psycopg[binary]` en `web/requirements.txt` (incluida en el Docker de la raíz del repo).

### Datos que ya tenías en SQLite

No se migran solos. Opciones: exportar/importar con herramientas (p. ej. [pgloader](https://pgloader.io/), CSV intermedio) o empezar con Postgres vacío y volver a registrar usuarios. Si necesitas script dedicado, se puede añadir en una iteración siguiente.

---

## 1. Supabase (base de datos)

1. Crea un proyecto en [Supabase](https://supabase.com/dashboard).
2. En el panel: **SQL** → **New query**.
3. Abre el archivo `YuweAI/supabase/migrations/20250512000000_initial_schema.sql` del repo, copia todo el contenido y ejecútalo (**Run**).
4. En Supabase pulsa **Connect** (arriba en el dashboard) y copia la URI del **Session pooler** (Supavisor): host `aws-0-REGION.pooler.supabase.com`, puerto **5432**, usuario `postgres.TU_PROJECT_REF` (con punto). Añade `sslmode=require` si no viene en la cadena. En Render define el secreto **`DATABASE_URL`** con **esa** URI.  
   **Importante para Render:** la conexión **directa** (`db.xxx.supabase.co`) es **solo IPv6** en Supabase; Render no suele poder usarla. No uses la URI “Direct” en Render; usa **Session** (pooler).

**Seguridad:** no expongas la `service_role` ni la contraseña `postgres` en el frontend. Solo en variables de entorno de **Render**.

---

## 2. Supabase Storage (corpus y archivos)

1. En Supabase: **Storage** → **New bucket**. Nombre sugerido: `corpus` (marca **Private** si solo el backend debe leer; entonces el servidor usará la **service role key** para descargar).
2. Sube allí `corpus_bilingue_v5.csv` (o versiones nuevas).
3. Cuando implementes lectura desde Storage en Python, usarás `SUPABASE_URL` + `SUPABASE_SERVICE_ROLE_KEY` (Settings → API). Mientras tanto puedes seguir metiendo el CSV en la **imagen Docker** (`corpus/data/` o `CORPUS_URL` en build), como ya documenta el `Dockerfile` de la raíz.

---

## 3. Render (backend / API)

1. Repositorio en GitHub con la carpeta **`YuweAI` como raíz del repo** (como está el proyecto público): en la raíz deben existir [`Dockerfile`](../Dockerfile) y [`render.yaml`](../render.yaml).
2. En [Render Dashboard](https://dashboard.render.com/) → **New** → **Blueprint** (o **Web Service** y elige Docker).
3. Conecta el repo; Render detectará `render.yaml` o configura manualmente:
   - **Dockerfile path:** `Dockerfile`
   - **Docker context:** `.`
4. Cuando el servicio tenga URL (`https://tu-servicio.onrender.com`), cópiala.

### Variables de entorno en Render

| Clave | Valor (ejemplo) |
|-------|------------------|
| **`DATABASE_URL`** | URI del **Session pooler** de Supabase (**Connect → Session**), no la URI directa `db.*` (solo IPv6; Render falla). Con `sslmode=require`. |
| `AVI_CORS_ORIGINS` | `https://tu-app.web.app,https://tu-app.firebaseapp.com` |
| `AVI_SKIP_DEMO_USERS` | `1` (recomendado en público) |
| `GOOGLE_CLIENT_ID` | (opcional) OAuth web |

Opcional (Storage desde código más adelante):

| `SUPABASE_URL` | `https://xxx.supabase.co` |
| `SUPABASE_SERVICE_ROLE_KEY` | Secreto (solo servidor) |

## 4. Firebase Hosting (frontend) y SDK JS

1. Instala la CLI (una vez): `npm install -g firebase-tools` → [Firebase CLI](https://firebase.google.com/docs/cli).
2. En `YuweAI/web/frontend`: copia `.firebaserc.example` a `.firebaserc` con `"default": "yuwe-ai"`.
3. **SDK en la app:** ya está `npm install firebase` y `src/firebase.js`, que lee variables `VITE_FIREBASE_*`. Crea **`.env.production`** (no lo subas a Git si el repo es público; está en `.gitignore`) copiando de `.env.production.example` y pega los valores de la consola (Project settings → Your apps → **npm** / configuración).
4. `npm run build` y `firebase deploy --only hosting`.

Variables Vite usadas por `src/firebase.js`:

| Variable | Ejemplo (tu proyecto) |
|----------|------------------------|
| `VITE_FIREBASE_API_KEY` | (la que muestra la consola) |
| `VITE_FIREBASE_AUTH_DOMAIN` | `yuwe-ai.firebaseapp.com` |
| `VITE_FIREBASE_PROJECT_ID` | `yuwe-ai` |
| `VITE_FIREBASE_STORAGE_BUCKET` | `yuwe-ai.firebasestorage.app` |
| `VITE_FIREBASE_MESSAGING_SENDER_ID` | (número de la consola) |
| `VITE_FIREBASE_APP_ID` | `1:...:web:...` |
| `VITE_FIREBASE_MEASUREMENT_ID` | `G-...` (opcional; Analytics) |

**Nota:** El login de la app AVI sigue yendo al **backend** (`/api/auth/...`). Este SDK sirve para **Analytics** (y más adelante Firestore/Auth cliente si lo integráis). No sustituye solo `GOOGLE_CLIENT_ID` del servidor.

---

## 4b. Build y despliegue Hosting

1. Una vez en la vida, en la misma cuenta de Google del proyecto: `firebase login` (o `npx firebase-tools login`).
2. Crea `.env.production` con `VITE_API_BASE` (URL de Render) y opcionalmente `VITE_FIREBASE_*` para Analytics.
3. Desde `YuweAI/web/frontend`:

```powershell
npm run deploy:hosting
```

Equivale a `npm run build` + subir la carpeta **`dist`** (no `public`; en `firebase.json` el campo `public` apunta a `dist` para Vite).

Tu URL: **https://yuwe-ai.web.app** (y `https://yuwe-ai.firebaseapp.com`).

Si ves error *Failed to authenticate*, ejecuta antes `firebase login` y vuelve a lanzar el comando.

### Windows: «la ejecución de scripts está deshabilitada» (npm / npx / firebase)

PowerShell a veces bloquea `npm.ps1` y `npx.ps1` (`PSSecurityException`). Elige **una** opción:

**Opción A (recomendada):** permitir scripts solo para tu usuario (una vez):

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Cierra y abre PowerShell, luego `npm install -g firebase-tools` y `firebase login`.

**Opción B:** usar **Símbolo del sistema (cmd.exe)** en lugar de PowerShell; allí `npm` y `npx` suelen funcionar sin cambiar la política.

**Opción C:** llamar al ejecutable `.cmd` desde PowerShell (evita el `.ps1`):

```powershell
& "C:\Program Files\nodejs\npm.cmd" install -g firebase-tools
& "C:\Program Files\nodejs\npx.cmd" firebase-tools login
```

(Si Node está en otra ruta, ajusta la carpeta.)

---

## 5. CORS (obligatorio si front y API son distintos)

El navegador bloqueará las llamadas a `/api/...` si el backend no envía `Access-Control-Allow-Origin` correcto. Con `AVI_CORS_ORIGINS` en Render debes listar **exactamente** las URLs del Hosting (con `https`, sin barra final), separadas por comas. No uses patrones tipo `*.web.app`: CORS exige **orígenes concretos** (por ejemplo `https://yuwe-ai.web.app` y `https://yuwe-ai.firebaseapp.com`); el [`render.yaml`](../render.yaml) ya los trae para el proyecto `yuwe-ai`.

---

## 6. Checklist rápido

- [ ] SQL de Supabase ejecutado sin errores.
- [ ] Bucket `corpus` (u otro) creado si ya usarás Storage.
- [ ] Render construye el `Dockerfile` de la raíz y responde en `/`.
- [ ] `VITE_API_BASE` apunta a Render y el front se reconstruyó antes de `firebase deploy`.
- [ ] Variables `VITE_FIREBASE_*` en `.env.production` para el SDK (Analytics).
- [ ] `DATABASE_URL` en Render es la URI del **Session pooler** de Supabase (no `db.*` directo).
- [ ] `AVI_CORS_ORIGINS` en Render incluye las URLs de Firebase.

Para despliegues solo con VM u opciones sin tarjeta, sigue usando [`DESPLIEGUE-GRATIS.md`](DESPLIEGUE-GRATIS.md).

---

## 7. Lo que falta (orden en los paneles)

Hazlo en este orden; yo no puedo entrar a tus cuentas, pero el repo ya trae `render.yaml` con **CORS** para `yuwe-ai` y hueco para **`DATABASE_URL`**.

### A. Supabase

1. [Dashboard](https://supabase.com/dashboard) → tu proyecto.
2. **SQL** → **New query** → pega todo [`supabase/migrations/20250512000000_initial_schema.sql`](../supabase/migrations/20250512000000_initial_schema.sql) → **Run** (debe terminar sin error).
3. **Project Settings → Database** (o botón **Connect**): copia la URI del **Session pooler** (`…pooler.supabase.com:5432`), **no** la conexión directa `db.…` (IPv6; Render no la alcanza). La pegarás en Render como `DATABASE_URL`.
4. *(Opcional)* **Storage** → **New bucket** → nombre `corpus` → sube el CSV si quieres el corpus en la nube (el servidor aún puede usar el del Docker; integración por código es opcional).

### B. Render

1. [Dashboard](https://dashboard.render.com/) → **New** → **Blueprint** (o importa repo y elige *Apply render.yaml* si te lo ofrece).
2. Conecta el repo **YuweAI** (raíz con `Dockerfile` + `render.yaml`).
3. Cuando Render pida variables con **`sync: false`**, pega **`DATABASE_URL`** (la URI de Supabase del paso A.3).
4. Tras el primer deploy, abre la **URL** del servicio (p. ej. `https://yuweai-avi-api.onrender.com`) y comprueba que responde en `/` o en `/api/health` (JSON). Si el front muestra **`Failed to fetch`**, suele ser **API caída**, **CORS** o que el backend **no escuchaba en `PORT`** (Render lo define automáticamente; `server.py` ya lee `PORT` y cae en **8090** solo en local).
5. Si cambias el nombre del servicio en Render, actualiza **`VITE_API_BASE`** en `web/frontend/.env.production` y vuelve a `npm run build` + `firebase deploy`.

> El archivo [`render.yaml`](../render.yaml) ya define `AVI_CORS_ORIGINS` y `AVI_SKIP_DEMO_USERS`. Si usas otro dominio de Firebase, edita el `value` de `AVI_CORS_ORIGINS` en el YAML o sobreescribe la variable en el panel de Render.

### C. Firebase (Hosting)

Si ya desplegaste: solo vuelve a **`npm run deploy:hosting`** cuando cambies el front o la URL del API.

### D. Comprobación final

1. Abre **https://yuwe-ai.web.app** → registro o login.
2. Si en consola del navegador (F12 → *Network*) ves errores **CORS** o **failed to fetch**, revisa `AVI_CORS_ORIGINS` en Render y que `VITE_API_BASE` sea exactamente la URL HTTPS de tu servicio (sin `/` final).
3. Si el login falla por **base de datos**, revisa que `DATABASE_URL` en Render sea la de Supabase y que el SQL del paso A.2 se haya ejecutado.
