# Despliegue gratis: VM con Docker (Oracle u otro proveedor)

## Lo honesto: “todo en la nube” sin tarjeta en ningún sitio

Las **máquinas virtuales** de proveedores grandes (Oracle, Google, AWS, Azure, Fly.io, etc.) **casi siempre piden tarjeta** aunque el plan diga “gratis”: es verificación y antifraude, no un cobro fijo. **No hay** un servicio serio que te garantice **24/7 + disco persistente + backend + BD** sin que en algún momento pidan tarjeta o método de pago.

**Lo que sí puedes hacer sin poner tarjeta en la nube:**

| Objetivo | Cómo | Tarjeta |
|-----------|------|---------|
| **Código** guardado y versionado | **GitHub** (correo) | No |
| **Una URL HTTPS** para que otros prueben tu app (backend + SQLite + corpus en tu PC) | **Cloudflare Quick Tunnel** (URL **cambia** cada vez) o **túnel con nombre + dominio** (URL **fija**) | No (modo rápido; dominio propio puede costar poco al año) |
| **Demo pública** con Docker | **Hugging Face Space** (correo) | No en la cuenta básica |
| **Solo la web estática** (`dist`) | **Cloudflare Pages** o **GitHub Pages** (conectando repo) | Suele **no** pedir tarjeta |
| **URL pública sin comprar dominio** | Subdominio **gratis** del proveedor (ej. `*.hf.space`, `*.web.app`, `*.pages.dev`) | Suele **no** pedir tarjeta |
| **Stack Supabase + Render + Firebase** | BD/Storage en Supabase, API en Render (`render.yaml` + `Dockerfile` raíz), front en Firebase Hosting | Render/Supabase pueden pedir verificación según cuenta; ver [`PLATAFORMA-SUPABASE-RENDER-FIREBASE.md`](PLATAFORMA-SUPABASE-RENDER-FIREBASE.md) |

**Lo que no es realista sin tarjeta:** una **VM propia** en la nube encendida todo el día con la misma comodidad que Oracle/Google. Ahí el camino real es **túnel + tu ordenador**, o aceptar **demo** (HF) con limitaciones.

---

La idea base con **Docker en una VM** es para quien **sí** pueda usar un proveedor con tarjeta de verificación: ahí van **backend** (`server.py`), **SQLite**, **corpus** y el **frontend** compilado.

**Oracle Cloud** suele ser la opción “gratis para siempre” más conocida, pero **a muchas personas les bloquea el registro** (verificación, país, tarjeta, etc.). Por eso abajo tienes **alternativas** con el **mismo `Dockerfile` y `docker compose`** que ya tienes en `YuweAI/deploy/`.

> **Importante:** yo no puedo crear cuentas en tu nombre. Los pasos SSH y Docker son iguales en casi todas las VMs; solo cambia **dónde creas la instancia** y cómo abres el puerto.

---

## Sin tarjeta (Oracle y Google cobran o bloquean)

Muchas nubes **exigen tarjeta** aunque digan “gratis” (verificación, microcargos, antifraude). Si **no quieres** o **no puedes** usar tarjeta, usa primero estas rutas:

### Recomendada: **Cloudflare Quick Tunnel** (HTTPS sin VM, sin tarjeta en el modo rápido)

Tu app sigue corriendo **en tu PC** en el puerto **8090**; el túnel da una URL pública `https://....trycloudflare.com`.

1. Descarga **cloudflared** para Windows: [Instalación oficial](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/).
2. Levanta YuweAI en local (`python server.py` en `YuweAI\web` o Docker en `YuweAI\deploy`).
3. En PowerShell (donde esté `cloudflared.exe`):

```powershell
.\cloudflared.exe tunnel --url http://127.0.0.1:8090
```

4. Copia la URL que muestra y compártela con quien deba probar la app.

**Ventajas:** no Oracle ni Google; **sin tarjeta** para este túnel rápido.  
**Inconvenientes:** el **PC encendido**; la URL **cambia** cada vez que reinicias el túnel (no sirve si necesitas **una sola dirección** para muchas personas durante semanas).

---

### URL siempre la misma (compartir con muchas personas)

El modo rápido (`--url`) no da un enlace fijo. Para **la misma URL** (por ejemplo `https://avi.tudominio.com`) sigue este orden: primero el **dominio en Cloudflare**, luego **Zero Trust + túnel con nombre**, luego **instalar el conector en Windows** y por último **probar**.

**Importante:** el túnel solo **expone** tu app; **no copia** la base de datos a la nube. Los datos siguen en el disco del ordenador donde corre el servidor.

#### A. Cuenta Cloudflare y dominio con DNS en Cloudflare

1. Crea una cuenta en [dash.cloudflare.com](https://dash.cloudflare.com/) (plan gratuito del sitio web vale).
2. Necesitas un **nombre de dominio** del que seas dueña (registrado en Namecheap, GoDaddy, DonDominio, etc.) **o** un subdominio institucional que te permitan apuntar a Cloudflare (menos común). Sin un dominio **no** podrás tener `https://avi.algo-que-controlas.com` con este método.
3. En Cloudflare: **Add a site** → escribe tu dominio (ej. `tudominio.com`) → elige el plan **Free** → continúa.
4. Cloudflare te mostrará **dos nameservers** (algo como `xxx.ns.cloudflare.com`). En el panel de **donde compraste el dominio**, sustituye los nameservers antiguos por esos dos y guarda.
5. Espera la propagación DNS (a veces **15–60 minutos**, a veces hasta **24 h**). En Cloudflare, cuando el sitio pase a **Active** y no pida más pasos de DNS, sigue.

> **Universidad:** si te dan solo un subdominio (`proyecto.universidad.edu`) y **no** puedes cambiar nameservers hacia Cloudflare, este tutorial **no** aplica tal cual; tendrías que pedir a TI que creen un registro/CNAME según política del centro.

#### B. Activar Zero Trust (una sola vez)

1. Entra en [Zero Trust / Cloudflare One](https://one.dash.cloudflare.com/) (enlace **Zero Trust** desde el panel de Cloudflare, o busca “Cloudflare Zero Trust”).
2. La primera vez te pedirá un **nombre de equipo** (team name), acepta el **plan Free** de Zero Trust si lo ofrece y completa el asistente.  
   - Si en tu país o cuenta te pide **tarjeta** como verificación y no quieres usarla, no podrás usar esta vía; en muchos casos **no** hace falta tarjeta para el plan gratuito.

#### C. Crear el túnel con nombre

1. En Zero Trust, abre el menú lateral **Networks** (Redes) → **Connectors** (Conectores) → **Cloudflare Tunnels** (a veces aparece solo como **Tunnels**).
2. Pulsa **Create a tunnel** (Crear túnel).
3. Elige **Cloudflared** como tipo de conector (es el programa en tu PC).
4. Pon un **nombre** al túnel (ej. `yuweai-pc-juliana`); es interno, no es la URL pública. **Save tunnel**.

#### D. Instalar `cloudflared` en Windows (conector)

1. En la misma pantalla del túnel, elige **Windows** y copia el comando que te da Cloudflare. Suele parecerse a:

   ```powershell
   cloudflared.exe service install EYxxxxxxxx...
   ```

   Ese texto largo es el **token**; no lo compartas públicamente.

2. Si aún no tienes `cloudflared`, instálalo (por ejemplo con **winget** en CMD/PowerShell **nuevo** tras instalar):

   ```powershell
   winget install Cloudflare.cloudflared
   ```

   Cierra y abre la terminal para que se actualice el `PATH`, o usa la ruta completa al `.exe`.

3. Ejecuta el comando **como administrador** (clic derecho en PowerShell → **Ejecutar como administrador**), pegando el `service install ...` que te dio el panel. Eso registra **cloudflared** como **servicio de Windows** que se inicia al arrancar el PC.

4. Vuelve al panel del túnel: el estado del conector debería pasar a **healthy** / conectado en unos segundos (si no, revisa firewall o antivirus bloqueando salida HTTPS).

#### E. Public Hostname (la URL fija → tu YuweAI)

1. Dentro del túnel creado, pestaña **Public Hostname** (o **Public hostnames**) → **Add a public hostname**.
2. Rellena:
   - **Subdomain:** `avi` (o el que quieras).
   - **Domain:** tu dominio ya en Cloudflare (`tudominio.com`).
   - **Path:** déjalo vacío (o `/` según el formulario).
   - **Service type:** **HTTP**.
   - **URL:** `http://127.0.0.1:8090` (o el puerto donde ejecutes `python server.py` en `YuweAI\web`).
3. Guarda (**Save hostname**). Cloudflare suele crear solo el registro DNS tipo **CNAME** hacia el túnel.

#### F. Probar

1. En tu PC, arranca YuweAI (`python server.py` en `YuweAI\web` hasta que escuche en **8090**).
2. Abre en el navegador `https://avi.tudominio.com` (sustituye por tu subdominio y dominio reales).
3. Si falla: comprueba que el **servicio** `cloudflared` esté **En ejecución** (services.msc), que **no** haya otro firewall bloqueando el puerto local, y en Cloudflare **SSL/TLS** del dominio suele ir bien en **Full** o **Flexible** para túneles HTTP al origen; si hay error de certificado en el navegador, revisa la documentación de [Public Hostnames](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/routing-to-tunnel/).

**Resumen:** la URL pública **no cambia** mientras exista ese hostname en el túnel. Tu PC debe estar **encendido** y con **YuweAI + cloudflared** activos para que la web responda.

---

### Dónde se guardan usuarios y todo lo demás (y cómo no perderlo)

Con YuweAI en local, **cuentas y datos** van a **SQLite** en tu máquina, no al túnel:

- Ruta típica: `YuweAI\web\data\avi_auth.db` (y otros archivos en `data\` si usas corpus o ficheros generados).

Eso **sí se guarda en disco**: si apagas el PC y lo vuelves a encender, **los usuarios siguen ahí** siempre que no borres esa carpeta ni reinstales encima sin copia.

**Recomendación:** haz **copia de seguridad** de `data\` (al menos `avi_auth.db`) a OneDrive, USB u otra carpeta, antes de actualizar el proyecto o formatear. El túnel (rápido o con nombre) **no sustituye** un respaldo: si se rompe el disco o se pierde la carpeta, se pierden las cuentas.

## Opción más fiable para conservar **todos** los datos de la BD (y el resto)

Tu app guarda casi todo en **SQLite** (`avi_auth.db`) y archivos bajo `web/data/`. La opción **más fiable** con el **código actual** (sin reescribir la aplicación) es:

### 1. Recomendada: **máquina virtual en la nube + Docker + volumen persistente**

- **Qué es:** un servidor (por ejemplo **Oracle Cloud Always Free**, u otro proveedor si te deja) donde corres **`docker compose`** desde `YuweAI/deploy` con el **volumen** `avi_auth_data` ya definido en `docker-compose.yml`, de modo que **`avi_auth.db` y lo que escriba la app en `/app/web/data` vivan en disco que sobrevive a reinicios del contenedor**.
- **Por qué es la más sólida:** el disco del volumen en la VM es **persistente** (no es el contenedor efímero de Hugging Face free ni el disco efímero típico de Render free). Reinicias el servicio o actualizas la imagen y **la base sigue ahí** mientras no borres el volumen ni la VM.
- **Seguridad práctica:** abre solo el puerto necesario (8090 o 80/443 detrás de un proxy), **HTTPS** (certificado con Caddy/nginx o el propio proveedor), contraseñas fuertes, actualizar el SO y **copias de seguridad periódicas** del volumen o del fichero `avi_auth.db` (descarga a tu PC o subcarpeta con fecha).

Si Oracle u otros te **bloquean o piden tarjeta** que no quieres usar, la alternativa sería, dentro de “persistencia real”, la opción 2.

### 2. Sin nube (o como respaldo): **tu PC + túnel + respaldos automáticos**

- **Qué es:** `python server.py` o Docker en tu equipo, acceso público con **Cloudflare Tunnel** (idealmente túnel con nombre si tienes dominio), y una **rutina de copia** de `YuweAI\web\data\` (como mínimo `avi_auth.db`) a OneDrive u otro sitio **cada día o después de sesiones importantes**.
- **Por qué funciona:** los datos están en **tu disco**; el túnel solo expone la app. El riesgo es apagado del PC, robo o fallo de disco: por eso los **respaldos** son obligatorios si esto es tu única “nube”.

### 3. Evolución (máxima robustez a largo plazo, con desarrollo)

- Sustituir SQLite por una **base gestionada** (PostgreSQL en Supabase, Neon, etc.): copias automáticas, recuperación ante desastres y mejor escala; **exige cambiar código** en `server.py` y pruebas.

**Resumen:** para “**todo super bien guardado**” con lo que ya tienes, apunta a **VM + Docker + volumen + backups**. Hugging Face Space gratis y Render free **no** son la opción más segura para datos definitivos.

### Sin comprar dominio: URL gratis, y ¿“partir” web / BD / corpus?

**No necesitas comprar un dominio** para tener una dirección pública: muchos servicios te dan un **subdominio gratis** (es “tu nombre” dentro de su dominio). Ejemplos: `tunombre.web.app` (Firebase Hosting), `tunombre.pages.dev` (Cloudflare Pages), `usuario-mirepo.hf.space` (Hugging Face Space). Eso **no** es comprar `tudominio.com`; es gratis y fijo mientras no borres el proyecto.

**¿Se puede poner una cosa en Firebase, la BD en otro lado y el corpus en otro?** En la práctica, **sí en general** (arquitectura “microservicios”), pero **el YuweAI que tienes ahora no está hecho así**: `server.py` sirve la web, lee el **corpus** desde disco o `AVI_CORPUS_PATH`, y guarda usuarios en **SQLite** (`avi_auth.db`) en la misma máquina. Para repartir sin reescribir:

| Pieza | Dónde “gratis” encaja | Con el código actual |
|--------|------------------------|----------------------|
| **URL / “dominio” público** | Subdominio del proveedor (HF, Firebase, Pages…) | Necesitas **un** sitio que ejecute el **backend** (Python) o un túnel a tu PC |
| **Solo interfaz web compilada** (`frontend/dist`) | Firebase Hosting, GitHub Pages, Cloudflare Pages | Falta un **API** en otro sitio y configurar **CORS** y la URL del API en el front |
| **Base de datos** | Supabase, Neon, Firebase Firestore, etc. (planes free con límites) | Habría que **sustituir SQLite** por ese proveedor en el código |
| **Corpus (CSV grande)** | Repo GitHub (raw), Hugging Face Dataset, bucket con enlace público | El servidor tendría que **descargar o leer por URL**; hoy espera **archivo local** (`AVI_CORPUS_PATH` ayuda si montas ruta en Docker) |

**Conclusión para “gratis y poco trabajo”:** lo más alineado con tu proyecto es **una sola ubicación** que ejecute Docker o Python con disco persistente (por ejemplo **Hugging Face Space** con tu `Dockerfile`, sabiendo límites de persistencia), o **tu PC + túnel**. Repartir Firebase + Supabase + corpus en otro sitio **sí se puede**, pero es **otro proyecto de integración** (varias semanas de desarrollo y pruebas), no solo “subir archivos”.

Si más adelante quisieras partirlo, orden típico sería: (1) API en un host con Python; (2) sustituir SQLite por una BD gestionada free; (3) subir el CSV a almacenamiento estable y leerlo con `AVI_CORPUS_PATH` o lógica nueva; (4) front estático en Pages/Firebase apuntando al API.

#### Ejemplo “Firebase + Supabase + backend aparte” (gratis con límites; **no** es configuración sola)

Sí existe un esquema **más “de nube”** y con **PostgreSQL gestionado** (copias, etc.), pero **no lo hace Firebase Hosting solo**: Hosting sirve **archivos estáticos** (tu `dist`). El **backend** (lógica de AVI, sesiones, diccionario) tiene que vivir en **otro sitio que ejecute Python** o tendrías que **reescribir** gran parte en Cloud Functions / otro stack.

| Capa | Servicio típico (suele tener **tier gratis**) | Qué implica con YuweAI hoy |
|------|-----------------------------------------------|-----------------------------|
| **Front** (HTML/JS del build) | [Firebase Hosting](https://firebase.google.com/docs/hosting), [Cloudflare Pages](https://pages.cloudflare.com/), [GitHub Pages](https://pages.github.com/) | Compilar `web/frontend`, subir `dist`, configurar **URL base del API** y **CORS** en el backend. |
| **API / backend** | Misma **VM + Docker**, [Railway](https://railway.app/), [Render](https://render.com/), [Fly.io](https://fly.io/), Space HF con volumen de pago, etc. | Sigue haciendo falta un proceso que ejecute **Python** (o reimplementar la API). |
| **Base de datos** | [Supabase](https://supabase.com/) (Postgres), [Neon](https://neon.tech/), [Turso](https://turso.tech/) (SQLite remoto), etc. | Sustituir **todas** las consultas SQLite en `server.py` por Postgres (u otro) + migraciones + pruebas. Opcional: usar **Auth de Supabase** en lugar del login propio (más cambios). |
| **Archivos / corpus** | [Supabase Storage](https://supabase.com/docs/guides/storage), bucket S3-compatible, dataset en Hugging Face | Subida/descarga por API; el servidor ya puede apuntar a rutas o URLs según lo que programéis. |

**“Más seguro en todos los sentidos”:** una BD gestionada ayuda a **no perder datos** por reinicios y suele incluir **copias**; no sustituye diseñar bien **permisos** (p. ej. [RLS en Supabase](https://supabase.com/docs/guides/auth/row-level-security)), **secretos** (nunca subir claves al repo), **HTTPS** y revisiones de código. Además, **más piezas** (front en un dominio, API en otro) implica más superficie de configuración (CORS, fugas de API keys si el front las expone mal).

**Resumen honesto:** **sí** puedes tener front en Firebase (o Pages), **Postgres gratis** en Supabase/Neon y API en otro host; es un camino **válido y profesional**, pero es un **proyecto de ingeniería aparte**, no un interruptor. Mientras tanto, lo más fiable **sin reescribir** sigue siendo **VM + Docker + volumen + backups** (sección anterior).

### Otras sin tarjeta (exponer `localhost`)

| Herramienta | Notas |
|---------------|--------|
| **[ngrok](https://ngrok.com/)** | Cuenta con correo; plan free con límites; confirma al registrarte si **no** pide tarjeta. |
| **localtunnel** | Con Node: `npx localtunnel --port 8090`; URL pública temporal. |

### **Hugging Face Space** (Docker, todo en un sitio — recomendado sin comprar dominio)

Enlace público estable del tipo `https://huggingface.co/spaces/TU_USUARIO/TU_SPACE` (sin dominio de pago). Este repositorio ya incluye:

| Archivo | Para qué |
|---------|----------|
| [`Dockerfile`](../Dockerfile) (raíz de `YuweAI`) | Imagen Docker: compila el front, copia `server.py`, corpus y arranca en el puerto **8090**. |
| [`README.md`](../README.md) | Bloque YAML al inicio (`sdk: docker`, `app_port: 8090`) que Hugging Face lee al conectar el repo. |
| [`corpus/data/`](../corpus/data/) | Aquí debe estar `corpus_bilingue_v5.csv` **o** usar `CORPUS_URL` en el build (ver abajo). |

#### Limitaciones honestas (plan gratuito)

- **SQLite (`avi_auth.db`):** en Spaces el disco del contenedor **no es persistente** entre reinicios o cuando HF “duerme” el Space. Eso incluye **todo lo que hoy guarda la app en esa base**: inicios de sesión (sesiones), **registros de usuarios**, roles, y en general **quién hizo qué** si eso está modelado en SQLite.
- **Tareas / actividades / bitácoras** guardadas solo en el disco del contenedor o en `avi_auth.db` **también se pueden perder** en el mismo reinicio; no cuentes el Space free como “libro de registro” permanente.
- **Aportes al corpus en caliente** (si la app permitiera editar el CSV o subir términos y solo se guardaran en el contenedor): **no quedan** de forma fiable; al reconstruir la imagen vuelve el corpus del **build** (repo o `CORPUS_URL`). Para corpus vivo haría falta **otro almacén** (Dataset en Hub, Git, base de datos, etc.) y **cambios de código** para escribir ahí.
- **Hardware:** CPU compartida; el primer arranque puede tardar.

En resumen: el Space gratis sirve para **demo y evaluación**. Si necesitas **historial serio** (cuentas, tareas, corpus ampliado por usuarios), usa **PC + túnel** (SQLite en tu disco), una **VM con volumen persistente**, o evoluciona la app hacia una **BD y almacenamiento externos** (trabajo adicional, aunque haya planes gratuitos con límites).

Documentación HF sobre datos en disco: [Docker Spaces — Data persistence](https://huggingface.co/docs/hub/spaces-sdks-docker#data-persistence).

#### Paso a paso

1. Cuenta en [huggingface.co](https://huggingface.co/join) (normalmente solo correo).
2. Sube el código a **GitHub** (el repo `YuweAI` con este `Dockerfile` y el `README.md` con el YAML del inicio).
3. **Corpus obligatorio en el build**, una de dos:
   - **A)** Copia `corpus_bilingue_v5.csv` a `YuweAI/corpus/data/` en el repo y haz commit (si pesa mucho, [Git LFS](https://git-lfs.com/)).
   - **B)** Sube el CSV a un sitio con **URL de descarga directa** (por ejemplo un archivo público en un **Dataset** de Hugging Face o un `Release` en GitHub con enlace raw). Luego en el Space: **Settings → Variables and secrets → Repository variables** (o la sección de **Build** / *Docker build args* según la UI actual) y define **`CORPUS_URL`** con esa URL. El `Dockerfile` hace `curl` en tiempo de build.
4. En Hugging Face: [**Create new Space**](https://huggingface.co/new-space) → nombre y visibilidad (p. ej. **Public**) → **SDK: Docker** → conecta el repositorio de GitHub del proyecto **YuweAI** (o sube los archivos manualmente si no usas GitHub).
5. Comprueba que el **README** del repo tenga al inicio el bloque con `sdk: docker` y `app_port: 8090` (ya está en la raíz de este proyecto).
6. Pulsa **Build** / espera a que el Space pase a **Running**. Abre la URL del Space; Hugging Face enruta el tráfico al puerto **8090** de tu contenedor.

Si el build falla con el mensaje de *falta corpus*, revisa el paso 3 (archivo en `corpus/data/` o variable `CORPUS_URL`).

Documentación oficial: [Docker Spaces](https://huggingface.co/docs/hub/spaces-sdks-docker) y [Spaces overview](https://huggingface.co/docs/hub/spaces-overview).

### **Render** (solo si no te pide tarjeta)

Prueba registro con **GitHub**. Si en algún paso **obliga** a tarjeta, no uses esta vía. El plan free tiene disco **efímero** (riesgo de perder la BD).

---

## Comparación rápida (si Oracle no te deja)

| Opción | Gratis | Persistencia SQLite | Dificultad | Notas |
|--------|--------|---------------------|------------|--------|
| **Oracle Cloud** | Sí (Always Free) | Sí (volumen Docker) | Media | A veces no deja registrarse |
| **Google Cloud e2-micro** | Sí en regiones US indicadas | Sí (volumen Docker) | Media | **Suele exigir tarjeta** (cargos de verificación) |
| **Fly.io** | Crédito mensual gratis | Sí con **volume** de Fly | Media | **Suele exigir tarjeta** |
| **Render** | Sí (tier free) | **No fiable** (disco efímero; al dormir se pierde) | Fácil | A veces **sin** tarjeta con GitHub; si la pide, no sirve |
| **Hugging Face Space** (Docker en raíz del repo `YuweAI`) | Sí (correo) | **No fiable** en free (reinicios / sueño del Space) | Media | URL fija `huggingface.co/spaces/...`; ver sección HF arriba; corpus en repo o `CORPUS_URL` |
| **Túnel Cloudflare + tu PC** | Sí | Sí en tu disco local | Fácil / media si URL fija | **Sin tarjeta** en modo rápido; URL fija con **túnel con nombre + dominio**; PC encendido |
| **ngrok / localtunnel** | Sí | Local | Fácil | **Sin tarjeta** en muchos casos (revisa al crear cuenta) |

El **backend** en todos los casos es el mismo contenedor: **`python server.py`** en el puerto **8090**.

---

## Si Oracle no te deja — opción 1: Google Cloud (Compute Engine) — **suele pedir tarjeta**

Si Google te **cobró** o **bloqueó** la cuenta, **salta esta sección** y usa **túnel Cloudflare** arriba.

1. Cuenta en [Google Cloud](https://cloud.google.com/) y crea un proyecto.
2. **Compute Engine → VM instances → Create**. Elige región donde aplique el **Always Free e2-micro** (revisa la documentación actual de “Free Tier” para tu cuenta; suele incluir `us-west1`, `us-central1`, `us-east1` en USA).
3. Imagen **Ubuntu 22.04 LTS**, máquina **e2-micro**, marca **Allow HTTP traffic** si quieres (o solo abre **8090** en firewall de red).
4. En **Firewall rules**, crea regla **ingress** TCP **8090** desde `0.0.0.0/0` (o solo tu IP).
5. Conéctate por **SSH** (botón SSH del navegador o `gcloud compute ssh`).
6. Instala **Docker** (mismos comandos que en la guía Oracle para Ubuntu: `apt install docker.io` + `docker compose plugin` o `docker-compose`).
7. Clona tu repo, entra en `YuweAI/deploy`, ejecuta `docker compose build` y `docker compose up -d`.

Documentación oficial del tier gratuito: [Free Cloud Features](https://cloud.google.com/free/docs/free-cloud-features).

---

## Si Oracle no te deja — opción 2: Fly.io (Docker) — **suele pedir tarjeta**

1. Cuenta en [fly.io](https://fly.io/) e instala la CLI: [Install flyctl](https://fly.io/docs/hands-on/install-flyctl/).
2. En tu PC (con el repo clonado), desde `YuweAI/deploy` puedes usar `fly launch` guiado o definir un `fly.toml` que use el mismo `Dockerfile` (contexto de build debe seguir siendo la **raíz del repo** con `YuweAI/` y `corpus/`).
3. Crea un **volume** para montar en `/app/web/data` y que **SQLite** sobreviva a los reinicios (ver docs “Volumes” de Fly).
4. Suele pedir **tarjeta**; el uso modesto suele entrar en la **capa gratuita** mensual.

---

## Si Oracle no te deja — opción 3: Render (solo si aceptas limitaciones)

1. [Render](https://render.com/) → **New → Web Service** → conecta **GitHub**.
2. Indica **Docker** y la ruta del `Dockerfile` (`YuweAI/deploy/Dockerfile`); el **root del build** debe ser la raíz del repo (donde están `YuweAI` y `corpus`).
3. En el plan **Free**, el disco suele ser **efímero**: al reiniciar el servicio puedes **perder** `avi_auth.db`. Útil para **demos**; si necesitas datos persistentes sin tarjeta, usa **túnel + PC** o un Space en Hugging Face con las limitaciones que conlleva.

---

## Túnel Cloudflare (detalle extra)

Los pasos mínimos del **Quick Tunnel** están arriba en **«Sin tarjeta»**. Una cuenta Cloudflare **no** es obligatoria para el modo rápido; solo si más adelante quieres túnel con nombre fijo y tu propio dominio.

---

## Dónde está el backend (en todos los casos)

| Pieza | Qué es |
|-------|--------|
| Backend | `YuweAI/web/server.py` (API + sirve el `dist`) |
| Mismo contenedor Docker | Un solo `docker compose up` levanta **todo** |

---

## Resumen de la arquitectura

| Qué | Dónde queda |
|-----|-------------|
| Código | GitHub (repositorio) |
| Frontend compilado | Dentro de la imagen Docker (`npm run build` en el Dockerfile) |
| Backend + API | Contenedor Python `server.py` |
| Base de datos SQLite | Volumen Docker `avi_auth_data` → `/app/web/data` |
| Corpus CSV | Dentro de la imagen (copiado en build); si cambia mucho, vuelve a `docker compose build` |

**App móvil (Expo):** en el código/config apunta la URL pública de tu VM, por ejemplo `http://IP_PUBLICA:8090` (mejor aún si luego pones dominio + HTTPS).

---

## Paso 0 — Subir el proyecto a GitHub (si aún no está)

1. Crea un repositorio vacío en GitHub (sin README si vas a empujar código existente).
2. En tu PC, en la carpeta raíz del proyecto (donde están `YuweAI/` y `corpus/`):

```powershell
git init
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git add .
git commit -m "Proyecto YuweAI + corpus"
git branch -M main
git push -u origin main
```

Si el corpus es muy grande y GitHub se queja, usa **Git LFS** o sube el CSV como **Release** y descárgalo en la VM con un script (se puede hacer en otro paso).

---

## Paso 1 — Crear la VM gratis en Oracle Cloud

1. Entra en [Oracle Cloud Free Tier](https://www.oracle.com/cloud/free/).
2. Crea una cuenta y una **tenancy** (puede pedir tarjeta; el tier Always Free no cobra por los recursos incluidos si no sales del free).
3. En el menú: **Compute → Instances → Create instance**.
4. Configuración recomendada para ahorrar y que funcione:
   - **Image:** Oracle Linux 8 o 9 (o Ubuntu 22.04).
   - **Shape:** la que marque **Always Free** (por ejemplo VM.Standard.A1.Flex ARM con 1 OCPU y 6 GB RAM, o la AMD gratuita si está disponible en tu región).
   - **Networking:** deja la VCN por defecto; marca **Assign public IPv4 address**.
   - **SSH keys:** genera o sube tu clave pública `.pub` (desde Windows puedes usar `ssh-keygen`).
5. **Create**. Espera a que el estado sea **RUNNING** y anota la **IP pública**.

---

## Paso 2 — Abrir el puerto 8090 (firewall)

En Oracle:

1. **Networking → Virtual Cloud Networks** → tu subred → **Security Lists** (o NSG asociada a la instancia).
2. Añade una regla **ingress**:
   - **Source:** `0.0.0.0/0` (solo para pruebas; en producción restringe a tu IP o usa solo 80/443 detrás de un proxy).
   - **IP protocol:** TCP
   - **Destination port:** `8090`

En la propia VM (si `firewalld` o `iptables` bloquean):

```bash
# Oracle Linux con firewalld
sudo firewall-cmd --permanent --add-port=8090/tcp
sudo firewall-cmd --reload
```

---

## Paso 3 — Conectar por SSH

Desde tu PC (ajusta la ruta a tu clave y la IP):

```powershell
ssh -i C:\ruta\a\tu_clave.pem opc@TU_IP_PUBLICA
```

(En Ubuntu la usuario suele ser `ubuntu`; en Oracle Linux a veces `opc`.)

---

## Paso 4 — Instalar Docker en la VM

**Oracle Linux 8/9:**

```bash
sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Cierra sesión y vuelve a entrar en SSH para que aplique el grupo `docker`.

Comprueba:

```bash
docker --version
docker compose version
```

---

## Paso 5 — Clonar el repositorio en la VM

```bash
sudo mkdir -p /opt/avi
sudo chown $USER:$USER /opt/avi
cd /opt/avi
git clone https://github.com/TU_USUARIO/TU_REPO.git src
cd src/YuweAI/deploy
```

La estructura debe ser: `src/YuweAI/...` y `src/corpus/data/corpus_bilingue_v5.csv`.

---

## Paso 6 — Construir y levantar el contenedor

```bash
docker compose build
docker compose up -d
docker compose logs -f avi
```

Deberías ver el mensaje de que AVI corre en el puerto 8090. Prueba en el navegador:

`http://TU_IP_PUBLICA:8090`

---

## Paso 7 — Cuando cambies código (flujo habitual)

En la VM:

```bash
cd /opt/avi/src
git pull
cd YuweAI/deploy
docker compose build --no-cache
docker compose up -d
```

Si **solo** cambias el corpus y no el código del servidor, basta con volver a hacer `build` (el Dockerfile copia el CSV en la imagen).

---

## Paso 8 (opcional) — Dominio y HTTPS gratis

1. Compra o usa un dominio gratis (Freenom ya no es fiable; a veces usan subdominios en servicios educativos).
2. Apunta un **A record** al IP de Oracle.
3. En la VM instala **Caddy** o **Nginx + Certbot** para escuchar en 443 y hacer proxy reverso a `localhost:8090`.

Con Caddy (ejemplo conceptual): proxy `https://tudominio.com` → `127.0.0.1:8090` y cierra el 8090 público en el firewall cuando todo vaya por 443.

En el **frontend** futuro, si sirves la web en otro host, define `VITE_API_BASE=https://tudominio.com` antes de `npm run build`.

---

## Variables de entorno útiles (ya soportadas en el servidor)

| Variable | Uso |
|----------|-----|
| `AVI_CORPUS_PATH` | Ruta absoluta al CSV (el Docker ya fija `/app/corpus/data/...`) |
| `AVI_CORS_ORIGINS` | Orígenes permitidos separados por comas (producción) |
| `AVI_SKIP_DEMO_USERS` | `1` para no crear cuentas demo en arranque |
| `GOOGLE_CLIENT_ID` | Si usas login Google |

Puedes añadirlas bajo `environment:` en `docker-compose.yml`.

---

## Alternativa “solo frontend en la nube” (gratis)

- **Cloudflare Pages** o **GitHub Pages**: subes solo el `dist` con `VITE_API_BASE` apuntando al `http(s)://IP_O_DOMINIO` del backend en Oracle.

El backend **sigue** en la VM (por SQLite y archivos).

---

## Hoja de ruta: migración “todo gratis (capas free) + persistente + trazabilidad”

Objetivo: **front**, **API (Python)**, **PostgreSQL** y **corpus** en servicios con **plan gratuito** (con límites), sin perder datos al reiniciar, y poder analizar **quién entra**, **qué tareas hizo o no**, etc.

### Qué ya guarda hoy la app (SQLite)

En `server.py` la base `avi_auth.db` ya incluye, entre otras: **usuarios**, **sesiones** (`sessions`), **grupos**, **actividades** (`learning_activities`), **asignaciones** (`activity_assignments`), **entregas** (`content_submissions`), **notas**, **auditoría admin** (`admin_audit_log`), etc. Eso es la base para “tareas hechas / no hechas” según cómo uses esas tablas en la interfaz.

Para requisitos del tipo **“quién nunca inició sesión”** o **cada intento de login (fallido o no)”**, suele hacer falta una tabla extra de **eventos** (p. ej. `auth_events`: `user_id`, `email`, `ok`, `ip`, `created_at`) o reportes sobre `sessions` + `users`. Eso es un **diseño pequeño** encima de la migración.

### Arquitectura objetivo (todo persistente en free tier, con matices)

| Pieza | Servicio típico (free con límites) | Persistencia |
|-------|-------------------------------------|--------------|
| **Base de datos** | [Supabase](https://supabase.com/) o [Neon](https://neon.tech/) (PostgreSQL) | Sí (copias del proveedor, disco gestionado) |
| **Archivos / corpus** | [Supabase Storage](https://supabase.com/docs/guides/storage) o bucket + URL firmadas | Sí (objetos en el bucket) |
| **Backend (API)** | Misma **VM Oracle** + Docker, o [Railway](https://railway.app/) / [Render](https://render.com/) / [Fly.io](https://fly.io/) si aceptas límites o tarjeta de verificación | Depende del plan: VM + volumen = sí; algunos free “duermen” el servicio |
| **Frontend estático** | [Cloudflare Pages](https://pages.cloudflare.com/) o [Firebase Hosting](https://firebase.google.com/docs/hosting) | Sí (repo + CDN; no es donde vive la BD) |

**Matiz “gratis gratis”:** los planes gratuitos **cobran en límites** (GB, horas CPU, filas, ancho de banda). Si el proyecto crece, puede hacer falta pagar o reducir uso.

### Fases recomendadas (orden realista)

1. **Diseño en Postgres** — El archivo `YuweAI/supabase/migrations/20250512000000_initial_schema.sql` replica el esquema SQLite. Ejecútalo en Supabase antes de arrancar el servidor con `DATABASE_URL`.
2. **Capa de acceso a datos** — Implementado: `web/avi_db.py` + `server.py` usan **psycopg** cuando existe **`DATABASE_URL`**; si no, siguen con SQLite local.
3. **Variables de entorno** — `DATABASE_URL` en Render (u otro host), secretos solo en el servidor; ver `deploy/PLATAFORMA-SUPABASE-RENDER-FIREBASE.md`.
4. **Corpus** — Subir el CSV a **Storage** (o seguir con `AVI_CORPUS_PATH` / imagen Docker).
5. **Front separado** — `VITE_API_BASE` + Firebase Hosting + **`AVI_CORS_ORIGINS`**.
6. **Trazabilidad extra** — Tablas de eventos (login, etc.) si lo pide la evaluación; opcional.
7. **Copiar datos viejos** — Si tenías `avi_auth.db` local, migrar a Postgres con pgloader/CSV o empezar BD vacía (ver guía de plataforma).

### Camino intermedio (menos reescritura que Postgres completo)

**[Turso](https://turso.tech/)** (SQLite remoto con libSQL): permite seguir usando SQL muy parecido a SQLite con otro conector; sigue siendo trabajo de integración, pero a veces **menos** que portar todo a Postgres. Aun así hay que tocar casi todo el acceso a BD.

### Resumen

Tu intuición (**migrar + gratis + persistente + corpus + front + quién hizo qué**) es la dirección **correcta** para un producto serio. La **conexión a Postgres** (Supabase u otro) ya está en el código vía `DATABASE_URL`; falta operativa (SQL en Supabase, variables en Render, copia de datos si aplica) y pruebas en entorno real. Mientras no uses `DATABASE_URL`, **VM + Docker + volumen + backups** sigue siendo la vía más simple para persistencia local.

---

## Límites honestos del “gratis”

- Oracle Free puede ser **lento de aprovisionar** o pedir revisión de cuenta.
- La IP puede cambiar si recreas la instancia (mejor DNS propio).
- **Backups:** copia periódica del volumen o del archivo `avi_auth.db` a tu PC u otro almacenamiento.

Si quieres, en un siguiente mensaje pega la salida de `docker compose logs` si algo falla al construir.
