/**
 * Firebase Web SDK (modular). Opcional: si faltan VITE_FIREBASE_*, no se inicializa.
 * Copia los valores de la consola Firebase → Configuración del proyecto → Tus apps → SDK.
 * No subas .env.production con claves a repos públicos sin revisar políticas del equipo.
 */
import { initializeApp, getApps } from 'firebase/app'
import { getAnalytics, isSupported } from 'firebase/analytics'

function firebaseConfigFromEnv() {
  return {
    apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
    authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
    projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
    storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
    messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID,
    appId: import.meta.env.VITE_FIREBASE_APP_ID,
    measurementId: import.meta.env.VITE_FIREBASE_MEASUREMENT_ID || undefined,
  }
}

/** @type {import('firebase/app').FirebaseApp | null} */
let _app = null

/**
 * Inicializa Firebase App y (en producción, si el navegador lo permite) Analytics.
 * @returns {import('firebase/app').FirebaseApp | null}
 */
export function initFirebase() {
  if (_app) {
    return _app
  }
  const cfg = firebaseConfigFromEnv()
  if (!cfg.apiKey || !cfg.projectId) {
    if (import.meta.env.DEV) {
      console.info('[Firebase] Variables VITE_FIREBASE_* no definidas; SDK no iniciado.')
    }
    return null
  }
  _app = getApps().length > 0 ? getApps()[0] : initializeApp(cfg)
  if (import.meta.env.PROD && typeof window !== 'undefined') {
    isSupported()
      .then((ok) => {
        if (ok) {
          getAnalytics(_app)
        }
      })
      .catch(() => {})
  }
  return _app
}

export function getFirebaseApp() {
  return _app
}
