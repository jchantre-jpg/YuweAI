# App móvil — AVI (Expo Go)

Proyecto **Expo SDK 54** que abre la **misma SPA del frontend web** dentro de un `WebView`. No hay una segunda copia de pantallas en React Native: **estudiante, docente y administrador** ven exactamente las mismas rutas, formularios y llamadas a API que en el navegador, siempre que la URL cargada sirva ese build.

En pantallas ≤1024px la web muestra barra inferior con accesos rapidos y un boton **Menú** que abre el panel lateral con **todas** las secciones del rol (incluido admin: auditoria, correos, soporte, etc.).

## Requisito

El stack web debe estar corriendo en tu red local. Desde la raíz del repositorio:

`cd web` → `python server.py`

## Configurar IP

Edita `app.json`:

- `expo.extra.webAppUrl` — URL que abre el WebView (ej. `http://192.168.43.243:8090`).
- `expo.extra.apiBase` — misma base si otras herramientas lo usan (opcional).

PC y celular en la **misma WiFi**.

## Ejecutar

```powershell
cd mobile
npm install
npx expo start --host lan
```

En Expo Go, abre la URL tipo `exp://<IP-de-tu-PC>:8081`.

## Estructura

| Archivo | Rol |
|---------|-----|
| `App.js` | `WebView` (misma web que el navegador), area segura superior, tecla Atras Android, bandera `window.__AVI_EXPO_SHELL__`. |
| `app.json` | Nombre del proyecto y `extra.webAppUrl`. |
| `package.json` | Dependencias Expo / React Native. |
| `babel.config.js` | Preset Expo. |
| `index.js` | Entrada Expo. |

Todo el **backend, BD y frontend** están en `../web/` del mismo repositorio.
