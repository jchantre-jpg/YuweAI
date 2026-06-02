import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import {
  BarChart3,
  Bell,
  BookOpen,
  Calendar,
  Camera,
  Check,
  ChevronDown,
  ChevronRight,
  CircleHelp,
  Compass,
  ClipboardList,
  Download,
  Droplet,
  Dumbbell,
  Eye,
  FileSearch,
  FolderOpen,
  Flame,
  GraduationCap,
  Home,
  Info,
  KeyRound,
  LayoutDashboard,
  Layers,
  Leaf,
  LifeBuoy,
  Lightbulb,
  LogOut,
  Mail,
  Menu,
  MessageCircle,
  Mic,
  Moon,
  Palette,
  ShieldCheck,
  PenLine,
  Search,
  Send,
  Star,
  Settings,
  Type,
  Shield,
  Sun,
  Sparkles,
  Target as TargetIcon,
  Target,
  Trash2,
  Trophy,
  User,
  UsersRound,
  Volume2,
  RefreshCw,
  CheckCheck,
  Waves,
  X,
} from 'lucide-react'
import {
  ApiError,
  authForgotPassword,
  authLogin,
  authLogout,
  authMe,
  authRegister,
  authResetPassword,
  changeStudentPassword,
  deleteStudentAccount,
  getHealth,
  getStudentSessions,
  getStudentSettings,
  getStats,
  getTeacherReportsSummary,
  saveStudentSettings,
  searchAVI,
} from './api'
import { PASSWORD_POLICY_HINT, validatePasswordStrength } from './passwordPolicy'
import {
  AdminAuditoriaPanel,
  AdminContentPanel,
  AdminCorreosPanel,
  AdminDashboard,
  AdminGruposPanel,
  AdminSoportePanel,
  AdminStatsPanel,
  AdminUsersPanel,
  StudentDictionaryRoute,
  StudentLearnRoute,
  StudentPracticeRoute,
  TeacherActivitiesPanel,
  TeacherCatalogActivitiesPanel,
  TeacherCalendarPanel,
  TeacherDashboard,
  TeacherGroupsPanel,
  TeacherReportsPanel,
} from './RoleScreens'
import { createTranslator, getThemeDataAttr } from './i18n'
import { isHiddenDictCategory, normalizeDictCategory } from './dictionaryCatalogUtils'
import './App.css'
import logoImg from './assets/imagenes/logo.png'
import welcomeImg from './assets/imagenes/bienvenida.png'
import chatLogoImg from './assets/imagenes/logo-chat-avi.png'

const SESSION_TOKEN_KEY = 'avi-session-token'
const AUTH_DEFAULT = { isLoggedIn: false, email: '', displayName: '', role: '' }

const NAV_REGISTRY = {
  inicio: { labelKey: 'nav.inicio', hintKey: 'navHint.inicio', icon: Home },
  aprender: { labelKey: 'nav.aprender', hintKey: 'navHint.aprender', icon: GraduationCap },
  practicar: { labelKey: 'nav.practicar', hintKey: 'navHint.practicar', icon: Dumbbell },
  conversar: { labelKey: 'nav.conversar', hintKey: 'navHint.conversar', icon: MessageCircle },
  diccionario: { labelKey: 'nav.diccionario', hintKey: 'navHint.diccionario', icon: Search },
  progreso: { labelKey: 'nav.progreso', hintKey: 'navHint.progreso', icon: BarChart3 },
  configuracion: { labelKey: 'nav.configuracion', hintKey: 'navHint.configuracion', icon: Settings },
  actividades_hub: { labelKey: 'nav.practicar', hintKey: 'navHint.actividades', icon: Target },
  docente_grupos: { labelKey: 'nav.docente_grupos', hintKey: 'navHint.docente_grupos', icon: UsersRound },
  docente_actividades: { labelKey: 'nav.docente_actividades', hintKey: 'navHint.docente_actividades', icon: PenLine },
  docente_catalogo_actividades: { labelKey: 'nav.docente_catalogo_actividades', hintKey: 'navHint.docente_catalogo_actividades', icon: Target },
  docente_reportes: { labelKey: 'nav.docente_reportes', hintKey: 'navHint.docente_reportes', icon: BarChart3 },
  docente_recursos: { labelKey: 'nav.docente_recursos', hintKey: 'navHint.docente_recursos', icon: FolderOpen },
  docente_calendario: { labelKey: 'nav.docente_calendario', hintKey: 'navHint.docente_calendario', icon: Calendar },
  admin_usuarios: { labelKey: 'nav.admin_usuarios', hintKey: 'navHint.admin_usuarios', icon: Shield },
  admin_contenido: { labelKey: 'nav.admin_contenido', hintKey: 'navHint.admin_contenido', icon: ClipboardList },
  admin_stats: { labelKey: 'nav.admin_stats', hintKey: 'navHint.admin_stats', icon: LayoutDashboard },
  admin_grupos: { labelKey: 'nav.admin_grupos', hintKey: 'navHint.admin_grupos', icon: Layers },
  admin_reportes: { labelKey: 'nav.admin_reportes', hintKey: 'navHint.admin_reportes', icon: BarChart3 },
  admin_auditoria: { labelKey: 'nav.admin_auditoria', hintKey: 'navHint.admin_auditoria', icon: FileSearch },
  admin_correos: { labelKey: 'nav.admin_correos', hintKey: 'navHint.admin_correos', icon: Mail },
  admin_soporte: { labelKey: 'nav.admin_soporte', hintKey: 'navHint.admin_soporte', icon: LifeBuoy },
}

const VIEW_ALIASES = {
  actividades_hub: 'practicar',
  admin_stats: 'admin_reportes',
  docente_recursos: 'docente_actividades',
}

const ROLE_NAV_IDS = {
  estudiante: ['inicio', 'aprender', 'practicar', 'conversar', 'diccionario', 'progreso', 'configuracion'],
  docente: [
    'inicio',
    'docente_grupos',
    'docente_catalogo_actividades',
    'docente_actividades',
    'docente_reportes',
    'docente_calendario',
    'diccionario',
    'configuracion',
  ],
  administrador: [
    'inicio',
    'admin_usuarios',
    'admin_contenido',
    'admin_grupos',
    'admin_reportes',
    'admin_auditoria',
    'admin_correos',
    'admin_soporte',
    'configuracion',
  ],
}

const BOTTOM_NAV_STUDENT = ['inicio', 'aprender', 'practicar', 'conversar', 'diccionario']
const BOTTOM_NAV_DOCENTE = ['inicio', 'docente_grupos', 'docente_catalogo_actividades', 'docente_reportes', 'diccionario']
const BOTTOM_NAV_ADMIN = ['inicio', 'admin_usuarios', 'admin_contenido', 'admin_reportes', 'configuracion']

const VALID_VIEWS = new Set(Object.keys(NAV_REGISTRY))
const DOCENTE_CONTENT_VIEWS = new Set(['aprender', 'practicar', 'conversar'])
const PREFERRED_CATEGORIES = ['comida', 'animales', 'saludos', 'colores', 'numeros', 'alimentos']

function formatChatRecordType(rt) {
  const r = String(rt || '').toLowerCase()
  if (r === 'lexico') return 'Vocabulario'
  if (r === 'dialogo') return 'Diálogo'
  if (r === 'qa') return 'Pregunta / respuesta'
  return r ? r : 'Texto'
}

function formatChatEvidenceSource(c) {
  const sk = String(c.source_kind || '').toLowerCase()
  const fn = String(c.fuente_nombre || '').trim()
  if (!fn) return ''
  if (sk.includes('sintetic') || fn.toLowerCase().includes('synthetic')) return 'Ejemplo pedagógico'
  return fn.length > 44 ? `${fn.slice(0, 41)}…` : fn
}

const PROGRESS_WEEK_LABELS = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']

const CHAT_QUICK_KEYS = ['chat.quickGreeting', 'chat.quickFamily', 'chat.quickThanks', 'chat.quickFarewell']

/** Métricas del carril derecho (mock alta fidelidad). */
const CHAT_CONVERSATION_METRICS = [
  { labelKey: 'home.skillVocab', pct: 70, tone: 'vocab' },
  { labelKey: 'home.skillGrammar', pct: 60, tone: 'gram' },
  { labelKey: 'chat.skillUnderstand', pct: 65, tone: 'comp' },
  { labelKey: 'chat.skillPronounce', pct: 68, tone: 'conv' },
]

const CHAT_EXPRESSION_KEYS = ['chat.expr1', 'chat.expr2', 'chat.expr3', 'chat.expr4']

const CHAT_MESSAGES_SEED = [
  {
    role: 'avi',
    text: 'Pa kiwe thegnas. ¿Kako estas? (Hola, ¿cómo estás?)',
    audio: true,
  },
  {
    role: 'user',
    text: 'Quiero hablar un poco de mi familia y de saludos cotidianos.',
    at: '09:58',
  },
]

function chatTimeNow() {
  try {
    return new Date().toLocaleTimeString(undefined, {
      hour: '2-digit',
      minute: '2-digit',
      hour12: false,
    })
  } catch {
    return ''
  }
}

const HOME_CHIP_KEYS = ['home.chipTranslate', 'home.chipHowSay', 'home.chipExplain', 'home.chipExample']

const HOME_SKILL_ROWS = [
  { labelKey: 'home.skillVocab', pct: 72, tone: 'vocab' },
  { labelKey: 'home.skillGrammar', pct: 60, tone: 'gram' },
  { labelKey: 'home.skillComp', pct: 58, tone: 'comp' },
  { labelKey: 'home.skillConv', pct: 70, tone: 'conv' },
]

const THEMES = ['Claro Nasa', 'Oscuro', 'Cultural']
const BRAND_ASSETS = {
  logo: logoImg,
  welcome: welcomeImg,
  chat: chatLogoImg,
}

/** Rutas eliminadas de la navegacion: enlaces viejos abren el diccionario. */
const LEGACY_VIEW_TARGETS = Object.freeze({
  corpus: 'diccionario',
  dialogos: 'diccionario',
})

function getInitialView() {
  if (typeof window === 'undefined') return 'inicio'
  const raw = window.location.hash.replace('#', '').trim()
  if (!raw) return 'inicio'
  const resolved = VIEW_ALIASES[raw] ?? LEGACY_VIEW_TARGETS[raw] ?? raw
  if (!VALID_VIEWS.has(resolved)) return 'inicio'
  return resolved
}

function loadStored(key, fallback) {
  try {
    const stored = window.localStorage.getItem(key)
    return stored ? { ...fallback, ...JSON.parse(stored) } : fallback
  } catch {
    return fallback
  }
}

function initials(name) {
  const parts = String(name || '')
    .trim()
    .split(/\s+/)
    .filter(Boolean)
  if (!parts.length) return '?'
  if (parts.length === 1) return parts[0].slice(0, 2).toUpperCase()
  return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase()
}

function BrandSymbol({ variant = 'sidebar' }) {
  return (
    <div className={`brand-symbol${variant === 'header' ? ' brand-symbol--header' : ''}`}>
      <img src={BRAND_ASSETS.logo} alt="" />
    </div>
  )
}

export default function App() {
  const [auth, setAuth] = useState(AUTH_DEFAULT)
  const [authReady, setAuthReady] = useState(
    typeof window !== 'undefined' && !window.localStorage.getItem(SESSION_TOKEN_KEY),
  )
  const [authTab, setAuthTab] = useState('login')
  /** Recuperar contraseña: 0 = pedir correo, 1 = código + nueva clave */
  const [recoverStep, setRecoverStep] = useState(0)
  const [recoverEmailInput, setRecoverEmailInput] = useState('')
  const [mobileNavOpen, setMobileNavOpen] = useState(false)
  /** Misma ruptura que bottom-nav (max 1024px = móvil): en escritorio el menú verde queda abierto. */
  const [wideNavLayout, setWideNavLayout] = useState(() =>
    typeof window !== 'undefined' ? window.matchMedia('(min-width: 1025px)').matches : false,
  )
  const wideNavWasTrueRef = useRef(false)
  const [view, setView] = useState(getInitialView)
  const [health, setHealth] = useState(null)
  const [stats, setStats] = useState(null)
  const [status, setStatus] = useState('')
  const [notice, setNotice] = useState('')
  const [category, setCategory] = useState('comida')
  const [query, setQuery] = useState('')
  const [homeComposerText, setHomeComposerText] = useState('')
  const [chatContexts, setChatContexts] = useState([])
  const [chatBusy, setChatBusy] = useState(false)
  const [dictionaryPreferredTab, setDictionaryPreferredTab] = useState(null)
  /** Arranque desde Aprender: abre Practicar y dispara ejercicios del corpus (una vez por _bootKey). */
  const [practiceFromLearn, setPracticeFromLearn] = useState(null)
  const [chatLang, setChatLang] = useState('nasa')
  const [settingsTab, setSettingsTab] = useState('general')
  const [regRole, setRegRole] = useState('estudiante')
  const [messages, setMessages] = useState(() => [...CHAT_MESSAGES_SEED])
  const [profile, setProfile] = useState(() =>
    loadStored('avi-profile', {
      name: 'Usuario',
      email: '',
      level: 'Intermedio',
      goal: 'Conversación fluida',
      language: 'Español',
      theme: 'Claro Nasa',
      reminders: true,
    }),
  )
  const [notifPrefs, setNotifPrefs] = useState({
    daily: true,
    content: true,
    streak: true,
    tips: false,
  })
  const [consentGiven, setConsentGiven] = useState(true)
  const [showSessions, setShowSessions] = useState(false)
  const [studentSessions, setStudentSessions] = useState([])
  const [dictionaryPersisted, setDictionaryPersisted] = useState([])
  const [streakDays, setStreakDays] = useState(0)
  const [streakWeekSlots, setStreakWeekSlots] = useState(() => [
    false,
    false,
    false,
    false,
    false,
    false,
    false,
  ])
  const [studentUiHydrated, setStudentUiHydrated] = useState(false)
  const settingsHydratedRef = useRef(false)
  const settingsSaveTimerRef = useRef(null)
  const chatSaveTimerRef = useRef(null)
  const t = useMemo(() => createTranslator(profile.language), [profile.language])

  const categories = useMemo(() => {
    const dist = stats?.category_distribution || {}
    const keys = Object.keys(dist)
    const out = []
    const push = (c) => {
      const s = normalizeDictCategory(c)
      if (!s || isHiddenDictCategory(s) || out.includes(s)) return
      out.push(s)
    }
    for (const p of PREFERRED_CATEGORIES) push(p)
    for (const k of keys.slice(0, 16)) push(k)
    for (const c of dictionaryPersisted) {
      if (typeof c === 'string' && c.trim()) push(c)
    }
    if (out.length) return out
    if (dictionaryPersisted.length) {
      return dictionaryPersisted.map((c) => normalizeDictCategory(c)).filter((c) => c && !isHiddenDictCategory(c))
    }
    return PREFERRED_CATEGORIES
  }, [stats, dictionaryPersisted])

  useEffect(() => {
    if (!auth.isLoggedIn) setStudentUiHydrated(false)
  }, [auth.isLoggedIn])

  useEffect(() => {
    if (typeof window === 'undefined') return undefined
    const mq = window.matchMedia('(min-width: 1025px)')
    const sync = () => setWideNavLayout(mq.matches)
    sync()
    mq.addEventListener('change', sync)
    return () => mq.removeEventListener('change', sync)
  }, [])

  useEffect(() => {
    if (wideNavWasTrueRef.current && !wideNavLayout) {
      setMobileNavOpen(false)
    }
    wideNavWasTrueRef.current = wideNavLayout
  }, [wideNavLayout])

  const sidebarOpen = wideNavLayout || mobileNavOpen

  const navItems = useMemo(() => {
    const role = auth.role === 'docente' || auth.role === 'administrador' ? auth.role : 'estudiante'
    const ids = ROLE_NAV_IDS[role] || ROLE_NAV_IDS.estudiante
    return ids.map((id) => {
      const base = { id, ...(NAV_REGISTRY[id] || NAV_REGISTRY.inicio) }
      if (role === 'administrador' && id === 'inicio') {
        return { ...base, labelKey: 'nav.adminDashboard', hintKey: 'navHint.adminDashboard' }
      }
      return base
    })
  }, [auth.role])

  const bottomNavIds = useMemo(() => {
    if (auth.role === 'docente') return BOTTOM_NAV_DOCENTE
    if (auth.role === 'administrador') return BOTTOM_NAV_ADMIN
    return BOTTOM_NAV_STUDENT
  }, [auth.role])

  const bottomNavItems = useMemo(() => {
    const role = auth.role === 'administrador' ? 'administrador' : null
    return bottomNavIds.map((id) => {
      const base = { id, ...(NAV_REGISTRY[id] || NAV_REGISTRY.inicio) }
      if (role === 'administrador' && id === 'inicio') {
        return { ...base, labelKey: 'nav.adminDashboard', hintKey: 'navHint.adminDashboard' }
      }
      return base
    })
  }, [bottomNavIds, auth.role])

  const consumePreferredDictTab = useCallback(() => setDictionaryPreferredTab(null), [])
  const consumePracticeFromLearn = useCallback(() => setPracticeFromLearn(null), [])

  const isSettingsSectionVisible = useCallback(
    (section) => settingsTab === 'general' || settingsTab === section,
    [settingsTab],
  )

  const notify = useCallback((message) => {
    setNotice(message)
    setStatus(message)
    window.clearTimeout(window.__aviNoticeTimer)
    window.__aviNoticeTimer = window.setTimeout(() => setNotice(''), 6500)
  }, [])

  const handleChangePassword = useCallback(() => {
    const current = window.prompt('Escribe tu contraseña actual (opcional en demo):', '')
    if (current == null) return
    const next = window.prompt(`Nueva contraseña (${PASSWORD_POLICY_HINT})`, '')
    if (next == null) return
    const next2 = window.prompt('Confirma la nueva contraseña:', '')
    if (next2 == null) return
    if (String(next).trim() !== String(next2).trim()) {
      notify('Las contraseñas no coinciden.')
      return
    }
    const pwErrs = validatePasswordStrength(next)
    if (pwErrs.length) {
      notify(pwErrs.join(' '))
      return
    }
    const token = window.localStorage.getItem(SESSION_TOKEN_KEY)
    if (!token) {
      notify('Sesion expirada. Ingresa de nuevo.')
      return
    }
    changeStudentPassword(token, { current_password: current || '', new_password: next.trim() })
      .then(() => notify('Contrasena actualizada correctamente.'))
      .catch((e) => notify(e?.message || 'No se pudo actualizar la contraseña.'))
  }, [notify])

  const handleDownloadData = useCallback(() => {
    const payload = {
      profile,
      notifications: notifPrefs,
      consentGiven,
      exported_at: new Date().toISOString(),
    }
    const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' })
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = 'avi-datos-cuenta.json'
    a.click()
    window.URL.revokeObjectURL(url)
    notify('Descarga iniciada: avi-datos-cuenta.json')
  }, [consentGiven, notifPrefs, notify, profile])

  const handleDeleteAccount = useCallback(() => {
    const ok = window.confirm('¿Seguro que deseas eliminar esta cuenta? Esta acción no se puede deshacer.')
    if (!ok) return
    const token = window.localStorage.getItem(SESSION_TOKEN_KEY)
    if (!token) {
      notify('Sesion expirada. Ingresa de nuevo.')
      return
    }
    deleteStudentAccount(token)
      .then(() => {
        notify('Cuenta desactivada.')
        window.localStorage.removeItem(SESSION_TOKEN_KEY)
        setAuth(AUTH_DEFAULT)
        setView('inicio')
        window.history.replaceState(null, '', '#inicio')
        setMobileNavOpen(false)
      })
      .catch((e) => notify(e?.message || 'No se pudo eliminar la cuenta.'))
  }, [notify])

  const handleToggleSessions = useCallback(() => {
    const next = !showSessions
    setShowSessions(next)
    if (!next) return
    const token = window.localStorage.getItem(SESSION_TOKEN_KEY)
    if (!token) return
    getStudentSessions(token)
      .then((res) => setStudentSessions(res?.sessions || []))
      .catch(() => setStudentSessions([]))
  }, [showSessions])

  useEffect(() => {
    window.localStorage.setItem('avi-profile', JSON.stringify(profile))
  }, [profile])

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', getThemeDataAttr(profile.theme))
  }, [profile.theme])

  useEffect(() => {
    if (!auth.isLoggedIn || auth.role !== 'estudiante') return
    const token = window.localStorage.getItem(SESSION_TOKEN_KEY)
    if (!token) return
    let cancelled = false
    ;(async () => {
      try {
        const [st, sess] = await Promise.all([getStudentSettings(token), getStudentSessions(token)])
        if (cancelled) return
        const s = st?.settings || {}
        setProfile((p) => ({
          ...p,
          language: s.language || p.language,
          theme: s.theme || p.theme,
          level: s.level || p.level,
          goal: s.goal || p.goal,
          reminders: typeof s.reminders === 'boolean' ? s.reminders : p.reminders,
        }))
        if (s.notifications) {
          setNotifPrefs({
            daily: !!s.notifications.daily,
            content: !!s.notifications.content,
            streak: !!s.notifications.streak,
            tips: !!s.notifications.tips,
          })
        }
        if (s.streak && typeof s.streak.current === 'number') {
          setStreakDays(Math.max(0, s.streak.current))
          if (Array.isArray(s.streak.week_slots) && s.streak.week_slots.length === 7) {
            setStreakWeekSlots(s.streak.week_slots.map((x) => !!x))
          }
        }
        if (Array.isArray(s.dictionary_last_categories) && s.dictionary_last_categories.length) {
          setDictionaryPersisted(s.dictionary_last_categories.map((x) => String(x)))
        }
        if (Array.isArray(s.avi_chat_messages) && s.avi_chat_messages.length) {
          setMessages(
            s.avi_chat_messages.map((m) => ({
              role: m.role === 'avi' ? 'avi' : 'user',
              text: String(m.text || ''),
              at: m.at ? String(m.at) : '',
              audio: !!m.audio,
            })),
          )
        }
        setConsentGiven(s.consent_given !== false)
        setStudentSessions(sess?.sessions || [])
        settingsHydratedRef.current = true
        setStudentUiHydrated(true)
      } catch {
        settingsHydratedRef.current = true
        setStudentUiHydrated(true)
      }
    })()
    return () => {
      cancelled = true
    }
  }, [auth.isLoggedIn, auth.role])

  useEffect(() => {
    if (!auth.isLoggedIn || auth.role !== 'estudiante' || !settingsHydratedRef.current) return
    const token = window.localStorage.getItem(SESSION_TOKEN_KEY)
    if (!token) return
    window.clearTimeout(settingsSaveTimerRef.current)
    settingsSaveTimerRef.current = window.setTimeout(() => {
      saveStudentSettings(token, {
        language: profile.language,
        theme: profile.theme,
        level: profile.level,
        goal: profile.goal,
        reminders: !!profile.reminders,
        notifications: notifPrefs,
        consent_given: !!consentGiven,
        dictionary_last_categories: categories,
      }).catch(() => {
        /* ignore transient errors */
      })
    }, 450)
    return () => window.clearTimeout(settingsSaveTimerRef.current)
  }, [
    auth.isLoggedIn,
    auth.role,
    profile.language,
    profile.theme,
    profile.level,
    profile.goal,
    profile.reminders,
    notifPrefs,
    consentGiven,
    categories,
  ])

  useEffect(() => {
    if (!auth.isLoggedIn || auth.role !== 'estudiante' || !settingsHydratedRef.current || !studentUiHydrated)
      return undefined
    const token = window.localStorage.getItem(SESSION_TOKEN_KEY)
    if (!token) return undefined
    window.clearTimeout(chatSaveTimerRef.current)
    chatSaveTimerRef.current = window.setTimeout(() => {
      const cleaned = messages.slice(-60).map((m) => ({
        role: m.role === 'avi' ? 'avi' : 'user',
        text: String(m.text || '').slice(0, 8000),
        ...(m.at ? { at: String(m.at).slice(0, 80) } : {}),
        ...(m.audio ? { audio: true } : {}),
      }))
      saveStudentSettings(token, { avi_chat_messages: cleaned }).catch(() => {})
    }, 650)
    return () => window.clearTimeout(chatSaveTimerRef.current)
  }, [messages, auth.isLoggedIn, auth.role, studentUiHydrated])

  useEffect(() => {
    let cancelled = false
    async function bootstrap() {
      const token = window.localStorage.getItem(SESSION_TOKEN_KEY)
      if (!token) {
        window.localStorage.removeItem('avi-auth')
        setAuthReady(true)
        return
      }
      try {
        const { user } = await authMe(token)
        if (cancelled) return
        setAuth({
          isLoggedIn: true,
          email: user.email,
          displayName: user.display_name,
          role: user.role || '',
        })
        setProfile((c) => ({ ...c, email: user.email, name: user.display_name }))
      } catch {
        window.localStorage.removeItem(SESSION_TOKEN_KEY)
        setAuth(AUTH_DEFAULT)
      } finally {
        if (!cancelled) setAuthReady(true)
      }
    }
    bootstrap()
    return () => {
      cancelled = true
    }
  }, [])

  useEffect(() => {
    function syncHash() {
      const raw = window.location.hash.replace('#', '').trim()
      if (!raw) return
      const resolved = VIEW_ALIASES[raw] ?? raw
      if (!VALID_VIEWS.has(resolved)) return
      setView(resolved)
      if (resolved !== raw) {
        window.history.replaceState(null, '', `#${resolved}`)
      }
    }
    window.addEventListener('hashchange', syncHash)
    return () => window.removeEventListener('hashchange', syncHash)
  }, [])

  useEffect(() => {
    if (window.location.hash.replace('#', '') !== view) {
      window.history.replaceState(null, '', `#${view}`)
    }
  }, [view])

  useEffect(() => {
    if (!auth.isLoggedIn) return undefined
    let cancelled = false
    ;(async () => {
      try {
        setStatus(t('statusConnecting'))
        const [h, s] = await Promise.all([getHealth(), getStats()])
        if (cancelled) return
        setHealth(h)
        setStats(s)
        const dist = s.category_distribution || {}
        const first =
          PREFERRED_CATEGORIES.find((c) => dist[c]) || Object.keys(dist)[0] || 'comida'
        setCategory(first)
        setStatus(t('statusOk'))
      } catch (e) {
        if (!cancelled) setStatus(String(e?.message || e))
      }
    })()
    return () => {
      cancelled = true
    }
  }, [auth.isLoggedIn, t])

  useEffect(() => {
    if (!auth.isLoggedIn || !authReady) return
    const ok = new Set(navItems.map((x) => x.id))
    if (auth.role === 'docente') {
      DOCENTE_CONTENT_VIEWS.forEach((id) => ok.add(id))
    }
    if (!ok.has(view)) {
      setView('inicio')
      window.history.replaceState(null, '', '#inicio')
    }
  }, [auth.isLoggedIn, authReady, auth.role, navItems, view])

  const applySession = useCallback((payload) => {
    const { token, user } = payload
    window.localStorage.setItem(SESSION_TOKEN_KEY, token)
    setAuth({
      isLoggedIn: true,
      email: user.email,
      displayName: user.display_name,
      role: user.role || '',
    })
    setProfile((c) => ({ ...c, email: user.email, name: user.display_name }))
  }, [])

  const handleLogout = useCallback(async () => {
    const token = window.localStorage.getItem(SESSION_TOKEN_KEY)
    if (token) {
      try {
        await authLogout(token)
      } catch {
        /* ignore */
      }
    }
    window.localStorage.removeItem(SESSION_TOKEN_KEY)
    setAuth(AUTH_DEFAULT)
    setView('inicio')
    window.history.replaceState(null, '', '#inicio')
    setMobileNavOpen(false)
    notify(t('login.logoutMsg') || 'Sesión cerrada')
  }, [notify, t])

  const navigateTo = useCallback((target, opts) => {
    const canon = VIEW_ALIASES[target] ?? LEGACY_VIEW_TARGETS[target] ?? target
    if (opts?.dictTab != null) {
      setDictionaryPreferredTab(opts.dictTab)
    }
    if (opts?.practiceFromLearn != null) {
      const pl = opts.practiceFromLearn
      setPracticeFromLearn({
        category: pl.category,
        tabId: pl.tabId,
        _bootKey: pl._bootKey ?? Date.now(),
      })
    }
    setView(canon)
    window.history.replaceState(null, '', `#${canon}`)
  }, [])

  const sendChatMessage = useCallback(async (text) => {
    const clean = String(text || '').trim()
    if (!clean) return
    setChatBusy(true)
    const at = chatTimeNow()
    setMessages((m) => [...m, { role: 'user', text: clean, at }])
    setQuery('')
    try {
      const data = await searchAVI(clean, 5)
      setChatContexts(Array.isArray(data.contexts) ? data.contexts : [])
      setMessages((m) => [
        ...m,
        { role: 'avi', text: data.answer || '…', audio: true, at: chatTimeNow() },
      ])
    } catch (e) {
      setChatContexts([])
      setMessages((m) => [
        ...m,
        { role: 'avi', text: String(e?.message || e), audio: true, at: chatTimeNow() },
      ])
    } finally {
      setChatBusy(false)
    }
  }, [])

  const goChatWith = useCallback(
    (text) => {
      navigateTo('conversar')
      void sendChatMessage(text)
    },
    [navigateTo, sendChatMessage],
  )

  const submitHomeComposer = useCallback(
    (ev) => {
      ev.preventDefault()
      const text = homeComposerText.trim()
      if (!text) return
      setHomeComposerText('')
      navigateTo('conversar')
      void sendChatMessage(text)
    },
    [homeComposerText, navigateTo, sendChatMessage],
  )

  async function submitLogin(ev) {
    ev.preventDefault()
    const email = String(ev.target.email?.value || profile.email || '').trim()
    const password = ev.target.password?.value || ''
    if (!email || !password) {
      notify(t('login.emptyFields') || 'Completa correo y contraseña')
      return
    }
    try {
      const payload = await authLogin({ email, password })
      applySession(payload)
      notify(t('login.success') || 'OK')
    } catch (err) {
      notify(err instanceof ApiError ? err.message : String(err))
    }
  }

  async function submitRegister(ev) {
    ev.preventDefault()
    const fd = new FormData(ev.target)
    const display_name = String(fd.get('display_name') || '').trim()
    const email = String(fd.get('email') || '').trim()
    const password = String(fd.get('password') || '')
    const password_confirm = String(fd.get('password_confirm') || '')
    if (!display_name || !email || !password) {
      notify('Completa nombre, correo y contraseña.')
      return
    }
    if (password.length > 256 || password_confirm.length > 256) {
      notify('La contraseña es demasiado larga.')
      return
    }
    if (password !== password_confirm) {
      notify('Las contraseñas no coinciden.')
      return
    }
    const pwErrs = validatePasswordStrength(password)
    if (pwErrs.length) {
      notify(pwErrs.join(' '))
      return
    }
    try {
      const payload = await authRegister({
        email,
        password,
        password_confirm,
        display_name,
        role: regRole,
      })
      if (payload.token) {
      applySession(payload)
      notify(payload.message || 'Cuenta creada.')
      } else {
        notify(payload.message || 'Cuenta registrada. Ahora inicia sesión con tu correo y contraseña.')
        setAuthTab('login')
        setRecoverStep(0)
        ev.target.reset()
      }
    } catch (err) {
      notify(err instanceof ApiError ? err.message : String(err))
    }
  }

  async function submitForgotEmail(ev) {
    ev.preventDefault()
    const em = String(ev.target.email?.value || '').trim()
    if (!em) {
      notify(t('login.forgotNeedEmail'))
      return
    }
    try {
      const res = await authForgotPassword({ email: em })
      setRecoverEmailInput(em)
      if (res.reset_code) {
        notify(t('login.resetCodeDemo', { code: res.reset_code }))
      } else {
        notify(res.message || t('login.forgotGenericOk'))
      }
      setRecoverStep(1)
    } catch (err) {
      notify(err instanceof ApiError ? err.message : String(err))
    }
  }

  async function submitRecoverPassword(ev) {
    ev.preventDefault()
    const fd = new FormData(ev.target)
    const code = String(fd.get('code') || '').trim()
    const password = String(fd.get('password') || '')
    const password_confirm = String(fd.get('password_confirm') || '')
    if (!code || !password) {
      notify(t('login.resetNeedFields'))
      return
    }
    if (password !== password_confirm) {
      notify(t('login.resetPassMismatch'))
      return
    }
    const pwErrs = validatePasswordStrength(password)
    if (pwErrs.length) {
      notify(pwErrs.join(' '))
      return
    }
    try {
      await authResetPassword({
        email: recoverEmailInput,
        code,
        password,
        password_confirm,
      })
      notify(t('login.resetSuccess'))
      setRecoverStep(0)
      setAuthTab('login')
      ev.target.reset()
    } catch (err) {
      notify(err instanceof ApiError ? err.message : String(err))
    }
  }

  async function askChat(ev) {
    ev.preventDefault()
    await sendChatMessage(query)
  }

  const resetChatConversation = useCallback(() => {
    setMessages([...CHAT_MESSAGES_SEED])
    setChatContexts([])
    setQuery('')
  }, [])

  /** Donut en inicio — alineado al mockup; se puede enlazar a stats mas adelante. */
  const homeDonutPct = 65

  if (!auth.isLoggedIn) {
    return (
      <div className="app-login-wrap">
        {!authReady ? (
          <div className="login-screen" data-theme="light">
            <p className="login-boot-text">{t('login.boot') || 'Cargando…'}</p>
          </div>
        ) : (
          <div className="login-screen" data-theme="light">
            <div className="login-inner">
              <div className="login-art">
                <div className="login-brand-row">
                  <BrandSymbol />
                  <div>
                    <h1>{t('brandTitle')}</h1>
                    <p>{t('brandSubtitle')}</p>
                  </div>
                </div>
                <div className="login-art-circle">
                  <img src={BRAND_ASSETS.welcome} alt="Bienvenida AVI" />
                </div>
                <p className="login-art-caption">{t('quote')}</p>
                <div className="woven-strip woven-strip--thin" aria-hidden />
              </div>

              <div className="login-card-wrap">
                {authTab === 'recover' ? (
                  <>
                    <button
                      type="button"
                      className="login-back-link"
                      onClick={() => {
                        setAuthTab('login')
                        setRecoverStep(0)
                      }}
                    >
                      {t('login.recoverBack')}
                    </button>
                    <h2 className="login-title">
                      {recoverStep === 0 ? t('login.recoverTitle') : t('login.recoverTitleNew')}
                    </h2>
                    <p className="login-sub">
                      {recoverStep === 0
                        ? t('login.recoverSub0')
                        : t('login.recoverSub1', { email: recoverEmailInput })}
                    </p>
                    {recoverStep === 0 ? (
                      <form className="login-form" onSubmit={submitForgotEmail}>
                        <div className="field">
                          <label htmlFor="forgot-email">{t('login.email')}</label>
                          <div className="input-icon-wrap">
                            <User size={18} />
                            <input
                              id="forgot-email"
                              name="email"
                              type="email"
                              required
                              autoComplete="email"
                              defaultValue={recoverEmailInput || profile.email || ''}
                            />
                          </div>
                        </div>
                        <button type="submit" className="login-submit">
                          {t('login.recoverContinue')}
                        </button>
                      </form>
                    ) : (
                      <form className="login-form" onSubmit={submitRecoverPassword}>
                        <div className="field">
                          <label htmlFor="reset-code">{t('login.recoverCodeLabel')}</label>
                          <div className="input-icon-wrap">
                            <KeyRound size={18} />
                            <input
                              id="reset-code"
                              name="code"
                              type="text"
                              inputMode="numeric"
                              pattern="[0-9]{6}"
                              maxLength={6}
                              required
                              autoComplete="one-time-code"
                            />
                          </div>
                        </div>
                        <div className="field">
                          <label htmlFor="reset-pass">{t('login.recoverNewPass')}</label>
                          <div className="input-icon-wrap">
                            <Sparkles size={18} />
                            <input id="reset-pass" name="password" type="password" minLength={10} required autoComplete="new-password" />
                          </div>
                        </div>
                        <div className="field">
                          <label htmlFor="reset-pass2">{t('login.recoverConfirmPass')}</label>
                          <div className="input-icon-wrap">
                            <Sparkles size={18} />
                            <input id="reset-pass2" name="password_confirm" type="password" minLength={10} required autoComplete="new-password" />
                          </div>
                        </div>
                        <p className="login-policy-hint">{PASSWORD_POLICY_HINT}</p>
                        <button type="submit" className="login-submit">
                          {t('login.recoverSave')}
                        </button>
                      </form>
                    )}
                  </>
                ) : (
                  <>
                <div className="login-tabs">
                  <button
                    type="button"
                    className={`login-tab${authTab === 'login' ? ' active' : ''}`}
                        onClick={() => {
                          setAuthTab('login')
                          setRecoverStep(0)
                        }}
                  >
                        {t('login.tabLogin')}
                  </button>
                  <button
                    type="button"
                    className={`login-tab${authTab === 'create' ? ' active' : ''}`}
                        onClick={() => {
                          setAuthTab('create')
                          setRecoverStep(0)
                        }}
                  >
                        {t('login.tabRegister')}
                  </button>
                </div>
                <div className="login-diamonds" aria-hidden>
                  <span />
                  <span />
                  <span />
                </div>
                {authTab === 'login' ? (
                  <>
                        <h2 className="login-title">{t('login.title')}</h2>
                        <p className="login-sub">{t('login.subtitle')}</p>
                    <form className="login-form" onSubmit={submitLogin}>
                      <div className="field">
                        <label htmlFor="login-email">{t('login.email')}</label>
                        <div className="input-icon-wrap">
                          <User size={18} />
                          <input
                            id="login-email"
                            name="email"
                            type="email"
                            placeholder="correo@ejemplo.com"
                            defaultValue={profile.email}
                            onBlur={(e) => setProfile((p) => ({ ...p, email: e.target.value }))}
                            required
                          />
                        </div>
                      </div>
                      <div className="field">
                        <label htmlFor="login-pass">{t('login.password')}</label>
                        <div className="input-icon-wrap">
                          <Sparkles size={18} />
                              <input id="login-pass" name="password" type="password" minLength={10} required autoComplete="current-password" />
                        </div>
                      </div>
                          <div className="login-recover-row">
                            <button
                              type="button"
                              className="login-recover-btn"
                              onClick={() => {
                                setAuthTab('recover')
                                setRecoverStep(0)
                              }}
                            >
                              {t('login.recoverPassword')}
                            </button>
                          </div>
                      <button type="submit" className="login-submit">
                        {t('login.submit')}
                      </button>
                    </form>
                  </>
                ) : (
                  <>
                        <h2 className="login-title">{t('login.tabRegister')}</h2>
                        <p className="login-sub">{t('login.subtitle')}</p>
                    <form className="login-form" onSubmit={submitRegister}>
                      <div className="field">
                        <label htmlFor="reg-name">{t('login.name')}</label>
                        <div className="input-icon-wrap">
                          <User size={18} />
                          <input id="reg-name" name="display_name" type="text" minLength={2} required />
                        </div>
                      </div>
                      <div className="field">
                        <label htmlFor="reg-email">{t('login.email')}</label>
                        <div className="input-icon-wrap">
                          <User size={18} />
                              <input id="reg-email" name="email" type="email" required autoComplete="email" />
                        </div>
                      </div>
                      <div className="field">
                        <label htmlFor="reg-role">Rol</label>
                        <select id="reg-role" value={regRole} onChange={(e) => setRegRole(e.target.value)}>
                          <option value="estudiante">Estudiante</option>
                          <option value="docente">Docente</option>
                        </select>
                      </div>
                      <div className="field">
                        <label htmlFor="reg-pass">{t('login.password')}</label>
                            <div className="input-icon-wrap">
                              <Sparkles size={18} />
                              <input id="reg-pass" name="password" type="password" minLength={10} required autoComplete="new-password" />
                            </div>
                      </div>
                      <div className="field">
                        <label htmlFor="reg-pass2">Confirmar contraseña</label>
                            <div className="input-icon-wrap">
                              <Sparkles size={18} />
                              <input id="reg-pass2" name="password_confirm" type="password" minLength={10} required autoComplete="new-password" />
                      </div>
                          </div>
                          <p className="login-policy-hint">{PASSWORD_POLICY_HINT}</p>
                      <button type="submit" className="login-submit">
                        Registrarme
                      </button>
                    </form>
                      </>
                    )}
                  </>
                )}
                {notice ? <p className="login-notice">{notice}</p> : null}
              </div>
            </div>
          </div>
        )}
      </div>
    )
  }

  return (
    <div className={`app-frame app-frame--${auth.role || 'estudiante'}`}>
      <aside
        className={`sidebar${sidebarOpen ? ' is-open' : ''}`}
        id="avi-app-drawer"
        aria-hidden={!sidebarOpen}
      >
        <div className="brand">
          <button
            type="button"
            className="sidebar-close-btn"
            onClick={() => setMobileNavOpen(false)}
            aria-label="Cerrar menú"
          >
            <X size={22} strokeWidth={2.2} />
          </button>
          <BrandSymbol />
          <div>
            <h1>{t('brandTitle')}</h1>
            <p>
              {auth.role === 'docente'
                ? t('brandSubtitleTeacher')
                : auth.role === 'administrador'
                  ? t('brandSubtitleAdmin')
                  : t('brandSubtitle')}
            </p>
          </div>
        </div>
        <div className="woven-strip woven-strip--thin" aria-hidden />
        <nav className="nav-list">
          {navItems.map((item) => (
            <button
              type="button"
              key={item.id}
              className={view === item.id ? 'nav-button active' : 'nav-button'}
              onClick={() => {
                navigateTo(item.id)
                setMobileNavOpen(false)
              }}
            >
              <item.icon size={20} />
              <span>
                <strong>{t(item.labelKey)}</strong>
                {t(item.hintKey).trim() ? <small>{t(item.hintKey)}</small> : null}
              </span>
            </button>
          ))}
        </nav>
        <blockquote className="sidebar-quote">
          {t('quote')}
          <cite>{t('quoteBy')}</cite>
        </blockquote>
        <div className="woven-strip" aria-hidden />
        <button type="button" className="logout-sidebar" onClick={handleLogout}>
          <LogOut size={18} /> {t('logout')}
        </button>
      </aside>

      <main className="main-area">
        <div className="app-global-header-shell">
          <header className="topbar topbar--app-global topbar--app-global-rich" role="banner">
            <button
              type="button"
              className="topbar-global-menu-btn menu-toggle"
              onClick={() => setMobileNavOpen(true)}
              aria-label={
                sidebarOpen
                  ? 'Menú lateral abierto. Cierra con el botón X en la barra verde.'
                  : 'Abrir menú principal'
              }
              aria-expanded={sidebarOpen}
              aria-controls="avi-app-drawer"
            >
              <Menu size={22} strokeWidth={2.2} />
            </button>
            <div className={`topbar-global-greet-zone${auth.role === 'docente' ? ' topbar-global-greet-zone--docente' : ''}`}>
              {auth.role === 'docente' ? (
                <p className="topbar-docente-lead">
                  <Leaf size={17} strokeWidth={2} className="topbar-docente-leaf" aria-hidden />
                  <span>{t('teacher.topBarTeacherLine')}</span>
                </p>
              ) : (
                <div className="topbar-global-greet">
                  <p className="topbar-global-greet-line">
                    <strong>
                      {t('topGreeting')}, {profile.name || 'María'}
                    </strong>
                    <Leaf size={17} strokeWidth={2} className="leaf--after-name" aria-hidden />
                  </p>
                  <p className="topbar-global-greet-tagline">{t('topBarTagline')}</p>
                </div>
              )}
            </div>
            <div className={`topbar-global-actions${auth.role === 'docente' ? ' topbar-global-actions--docente' : ' topbar-global-actions--rich'}`}>
              {auth.role !== 'docente' ? (
                <>
                  <div className="topbar-metric" aria-label={`${t('streak')}: ${streakDays} ${t('days')}`}>
                    <span className="topbar-metric-icon topbar-metric-icon--fire">
                      <Flame size={22} strokeWidth={2} />
                    </span>
                    <span className="topbar-metric-text">
                      <span className="topbar-metric-label">{t('streak')}</span>
                      <span className="topbar-metric-value">
                        {streakDays} {t('days')}
                      </span>
                    </span>
                  </div>
                  <div className="topbar-metric" aria-label={`${t('level')}: ${profile.level}`}>
                    <span className="topbar-metric-badge" aria-hidden>
                      <Star size={15} fill="currentColor" strokeWidth={0} />
                    </span>
                    <span className="topbar-metric-text">
                      <span className="topbar-metric-label">{t('level')}</span>
                      <span className="topbar-metric-value">{profile.level}</span>
                    </span>
                  </div>
                </>
              ) : (
                <>
                  <button
                    type="button"
                    className="topbar-bell-btn"
                    onClick={async () => {
                      try {
                        const tok =
                          typeof window !== 'undefined' ? window.localStorage.getItem(SESSION_TOKEN_KEY) : ''
                        const s = await getTeacherReportsSummary(tok, 30)
                        const tot = s?.totals || {}
                        notify(
                          t('teacher.bellDigest', {
                            g: tot.groups ?? 0,
                            st: tot.students_in_groups ?? 0,
                            aw: tot.group_assignments_window ?? 0,
                          }),
                        )
                      } catch {
                        notify(t('teacher.loadErr'))
                      }
                    }}
                    aria-label="Notificaciones"
                  >
                    <Bell size={21} strokeWidth={2} />
                  </button>
                  <span className="topbar-global-actions-rule topbar-global-actions-rule--mini" aria-hidden />
                </>
              )}
              <span className="topbar-global-actions-rule" aria-hidden />
              <button type="button" className="topbar-global-profile" onClick={() => navigateTo('configuracion')}>
                <span className="topbar-global-profile-photo">
                  <img src={BRAND_ASSETS.welcome} alt="" />
                </span>
                <span className="topbar-global-profile-name">{profile.name || 'María'}</span>
                <ChevronDown size={18} aria-hidden />
              </button>
            </div>
          </header>
          <div className="woven-strip woven-strip--thin woven-strip--under-header" aria-hidden />
        </div>

        {notice && view !== 'inicio' && view !== 'configuracion' ? <div className="notice-bar">{notice}</div> : null}

        {view === 'diccionario' && (
          <StudentDictionaryRoute
            t={t}
            notify={notify}
            navigateHome={() => navigateTo('inicio')}
            category={category}
            categories={categories}
            setCategory={setCategory}
            preferredTab={dictionaryPreferredTab || undefined}
            onPreferredTabConsumed={consumePreferredDictTab}
            userRole={auth.role}
          />
        )}
        {view === 'aprender' && (
          <StudentLearnRoute
            t={t}
            navigateTo={navigateTo}
            categories={categories}
            setCategory={setCategory}
          />
        )}
        {view === 'practicar' && (
          <StudentPracticeRoute
            t={t}
            notify={notify}
            navigateTo={navigateTo}
            navigateHome={() => navigateTo('inicio')}
            category={category}
            categories={categories}
            setCategory={setCategory}
            practiceFromLearn={practiceFromLearn}
            onConsumePracticeFromLearn={consumePracticeFromLearn}
          />
        )}
        {view === 'docente_grupos' && (
          <TeacherGroupsPanel t={t} notify={notify} navigateHome={() => navigateTo('inicio')} navigateTo={navigateTo} />
        )}
        {view === 'docente_catalogo_actividades' && (
          <TeacherCatalogActivitiesPanel
            t={t}
            notify={notify}
            navigateHome={() => navigateTo('inicio')}
            navigateTo={navigateTo}
          />
        )}
        {view === 'docente_actividades' && (
          <TeacherActivitiesPanel t={t} notify={notify} navigateHome={() => navigateTo('inicio')} />
        )}
        {view === 'docente_reportes' && (
          <TeacherReportsPanel t={t} notify={notify} navigateHome={() => navigateTo('inicio')} />
        )}
        {view === 'docente_calendario' && (
          <TeacherCalendarPanel t={t} notify={notify} navigateHome={() => navigateTo('inicio')} setView={navigateTo} />
        )}
        {view === 'admin_usuarios' && <AdminUsersPanel t={t} notify={notify} />}
        {view === 'admin_contenido' && <AdminContentPanel t={t} notify={notify} />}
        {view === 'admin_reportes' && <AdminStatsPanel t={t} />}
        {view === 'admin_grupos' && <AdminGruposPanel t={t} notify={notify} navigateTo={navigateTo} />}
        {view === 'admin_auditoria' && <AdminAuditoriaPanel t={t} notify={notify} />}
        {view === 'admin_correos' && <AdminCorreosPanel t={t} notify={notify} />}
        {view === 'admin_soporte' && <AdminSoportePanel t={t} notify={notify} />}

        {view === 'inicio' && auth.role === 'docente' && (
          <TeacherDashboard t={t} notify={notify} profile={profile} setView={navigateTo} />
        )}
        {view === 'inicio' && auth.role === 'administrador' && (
          <AdminDashboard t={t} notify={notify} profile={profile} setView={navigateTo} />
        )}
        {view === 'inicio' && auth.role !== 'docente' && auth.role !== 'administrador' && (
          <div className="home-dashboard dashboard-rich">
            <div className="home-main">
              <section className="home-hero home-hero--mockup">
                <div className="home-hero-visual home-hero-visual--mockup" aria-hidden>
                  <img src={BRAND_ASSETS.welcome} alt="" className="home-hero-welcome home-hero-welcome--mockup" />
                </div>
                <div className="home-hero-copy home-hero-copy--mockup">
                  <h2>{t('home.title')}</h2>
                  <p className="home-hero-lead">{t('home.lead')}</p>
                </div>
              </section>

              <h2 className="home-quick-title">{t('home.quickTitle')}</h2>
              <div className="action-grid action-grid--home">
                <button type="button" className="action-tile action-tile--learn" onClick={() => navigateTo('aprender')}>
                  <span className="action-tile-icon action-tile-icon--learn">
                    <BookOpen size={22} />
                  </span>
                  <span>{t('home.actionLearn')}</span>
                </button>
                <button type="button" className="action-tile action-tile--practice" onClick={() => navigateTo('practicar')}>
                  <span className="action-tile-icon action-tile-icon--practice">
                    <MessageCircle size={22} strokeWidth={2.2} />
                  </span>
                  <span>{t('home.actionPractice')}</span>
                </button>
                <button type="button" className="action-tile action-tile--listen" onClick={() => navigateTo('diccionario')}>
                  <span className="action-tile-icon action-tile-icon--listen">
                    <Waves size={22} />
                  </span>
                  <span>{t('home.actionListen')}</span>
                </button>
                <button type="button" className="action-tile action-tile--explore" onClick={() => navigateTo('diccionario')}>
                  <span className="action-tile-icon action-tile-icon--explore">
                    <Type size={22} strokeWidth={2.2} />
                  </span>
                  <span>{t('home.actionCorpus')}</span>
                </button>
              </div>

              <section className="home-composer" aria-label={t('nav.conversar')}>
                <form className="home-composer-form" onSubmit={submitHomeComposer}>
                  <input
                    type="text"
                    value={homeComposerText}
                    onChange={(e) => setHomeComposerText(e.target.value)}
                    placeholder={t('home.placeholder')}
                    autoComplete="off"
                  />
                  <button type="submit" className="home-composer-send" aria-label={t('home.send')}>
                    <Send size={20} strokeWidth={2.2} />
                  </button>
                </form>
                <div className="home-composer-chips">
                  {HOME_CHIP_KEYS.map((key) => (
                    <button key={key} type="button" onClick={() => goChatWith(t(key))}>
                      {t(key)}
                    </button>
                  ))}
                </div>
              </section>

              <footer className="home-footer-tag home-footer-tag--woven">
                Nasa Yuwe: nuestra voz, nuestra identidad, nuestro pensamiento.
              </footer>
            </div>

            <aside className="home-rail home-rail--mockup">
              <div className="rail-card rail-card--progress">
                <h3>{t('nav.progreso')}</h3>
                <div className="donut-wrap donut-wrap--mockup">
                  <div className="donut donut--mockup" style={{ background: `conic-gradient(#2f6f4a 0% ${homeDonutPct}%, #ede8dc ${homeDonutPct}% 100%)` }}>
                    <div className="donut-inner donut-inner--mockup">
                      <span className="donut-inner-pct">{homeDonutPct}%</span>
                      <small className="donut-inner-cap">{t('home.generalAdvance')}</small>
                    </div>
                  </div>
                  <div className="skill-bars">
                    {HOME_SKILL_ROWS.map((row) => (
                      <div key={row.labelKey} className="skill-row">
                        <span>
                          <span>{t(row.labelKey)}</span>
                          <span>{row.pct}%</span>
                        </span>
                        <div className="skill-track">
                          <div
                            className={`skill-fill skill-fill--${row.tone}`}
                            style={{ width: `${row.pct}%` }}
                          />
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              <div className="rail-card rail-card--daily-goal">
                <h3>{t('rightRail.daily')}</h3>
                <p className="daily-goal-label">{t('home.dailyGoalLine')}</p>
                <div className="daily-goal-meta">
                  <span className="daily-goal-count">{t('home.dailyGoalCount', { done: 7, total: 10 })}</span>
                </div>
                <div className="daily-goal-track-wrap">
                  <div className="skill-track daily-goal-track">
                    <div className="skill-fill skill-fill--goal" style={{ width: `${(7 / 10) * 100}%` }} />
                  </div>
                </div>
              </div>

              <div className="rail-card word-day rail-card-word-mockup">
                <h3>{t('rightRail.wordDay')}</h3>
                <div className="word-day-actions">
                  <p className="word">Çxhab</p>
                  <span className="word-day-mini">
                    <button type="button" className="word-day-icon-btn" aria-label="Audio">
                      <Volume2 size={18} strokeWidth={2} />
                    </button>
                    <button type="button" className="word-day-icon-btn" aria-label={t('rightRail.waterNote')}>
                      <Droplet size={18} strokeWidth={2} />
                    </button>
                  </span>
                </div>
                <p className="trans">{t('rightRail.waterNote')}</p>
              </div>

              <div className="rail-card rail-card--streak-mock">
                <h3>{t('home.streakPanel')}</h3>
                <div className="streak-week streak-week--full">
                  {PROGRESS_WEEK_LABELS.map((d, i) => (
                    <span key={d} className={`streak-slot${streakWeekSlots[i] ? ' done' : ''}`}>
                      <span className="streak-dot" />
                      <span className="streak-label">{d.slice(0, 3)}</span>
                    </span>
                  ))}
                </div>
              </div>

              <div className="rail-card rail-card--explore-promo">
                <h3>{t('rightRail.exploreTitle')}</h3>
                <p className="explore-promo-meta">{t('rightRail.exploreMeta')}</p>
                <button type="button" className="explore-promo-btn" onClick={() => navigateTo('diccionario')}>
                  {t('rightRail.explore')}
                </button>
              </div>
            </aside>
          </div>
        )}

        {view === 'conversar' && (
          <div className="page-shell chat-mock-page">
            <div className="chat-mock-toolbar">
              <div className="chat-mock-toolbar-title">
                <MessageCircle className="chat-mock-toolbar-ico" size={26} strokeWidth={2} aria-hidden />
                <div>
                  <h2 className="chat-mock-toolbar-heading">{t('chat.pageTitle')}</h2>
                  <p className="chat-mock-toolbar-sub">{t('chat.pageSub')}</p>
                </div>
              </div>
              <div className="chat-mock-toolbar-actions">
                <div className="chat-lang-toggle chat-lang-toggle--mock" role="group" aria-label={t('chat.langUiLabel')}>
                  <button type="button" className={chatLang === 'nasa' ? 'active' : ''} onClick={() => setChatLang('nasa')}>
                    {t('chat.modeNasa')}
                  </button>
                  <button type="button" className={chatLang === 'es' ? 'active' : ''} onClick={() => setChatLang('es')}>
                    {t('chat.modeEs')}
                  </button>
                </div>
                <button
                  type="button"
                  className="chat-mock-tips-btn"
                  onClick={() => notify(t('chat.tipsBlurb'))}
                >
                  <Lightbulb size={18} strokeWidth={2} aria-hidden />
                  {t('chat.tipsBtn')}
                </button>
              </div>
            </div>

            <div className="chat-mock-grid">
              <div className="chat-mock-main-col">
                <div className="chat-mock-thread-card">
                  <div className="messages-panel chat-mock-messages" role="log" aria-live="polite">
                    {messages.map((m, i) =>
                      m.role === 'avi' ? (
                        <div key={`m-${i}`} className="bubble avi chat-mock-bubble-avi">
                          <div className="chat-mock-avi-head">
                            <img src={BRAND_ASSETS.chat} alt="" className="chat-bubble-avatar chat-bubble-avatar--lg" />
                            <span className="chat-mock-avi-name">{t('chat.avi')}</span>
                            {m.audio ? (
                              <button
                                type="button"
                                className="chat-mock-speak-btn"
                                aria-label={t('practice.audioSoon')}
                                onClick={() => notify(t('practice.audioSoon'))}
                              >
                                <Volume2 size={18} strokeWidth={2} aria-hidden />
                              </button>
                            ) : null}
                          </div>
                          <p className="chat-mock-msg-text">{m.text}</p>
                        </div>
                      ) : (
                        <div key={`m-${i}`} className="bubble user chat-mock-bubble-user">
                          <div className="chat-mock-user-head">
                            <strong>{t('chat.you')}</strong>
                          </div>
                          <p className="chat-mock-msg-text">{m.text}</p>
                          <div className="chat-mock-user-foot">
                            <CheckCheck size={16} strokeWidth={2} className="chat-mock-read" aria-hidden />
                            {m.at ? <span className="chat-mock-ts">{m.at}</span> : null}
                          </div>
                        </div>
                      ),
                    )}
                  </div>
                  <div className="chat-quick chat-mock-quick">
                    {CHAT_QUICK_KEYS.map((qk) => (
                      <button
                        key={qk}
                        type="button"
                        disabled={chatBusy}
                        onClick={() => void sendChatMessage(t(qk))}
                      >
                        {t(qk)}
                      </button>
                    ))}
                    <button
                      type="button"
                      className="chat-quick-refresh"
                      aria-label={t('chat.resetThread')}
                      onClick={resetChatConversation}
                    >
                      <RefreshCw size={17} strokeWidth={2} aria-hidden />
                    </button>
                  </div>
                </div>

                <form onSubmit={askChat} className="chat-input chat-mock-input">
                  <button type="button" className="mic" aria-label={t('chat.micLabel')}>
                    <Mic size={20} aria-hidden />
                  </button>
                  <input
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder={t('chat.placeholder')}
                    aria-label={t('chat.placeholder')}
                  />
                  <button type="submit" className="send" disabled={chatBusy} aria-label={t('home.send')}>
                    <Send size={20} aria-hidden />
                  </button>
                </form>
              </div>

              <aside className="chat-mock-rail" aria-label={t('chat.railAria')}>
                <div className="rail-card chat-mock-rail-card chat-mock-rail-card--progress">
                  <h3>{t('chat.progressRailTitle')}</h3>
                  <div className="learn-donut-wrap chat-mock-donut-wrap">
                    <div
                      className="learn-donut"
                      style={{
                        background:
                          'conic-gradient(#2f6f4a 0% 68%, #ede8dc 68% 100%)',
                      }}
                    >
                      <div className="learn-donut-inner donut-inner--mockup">
                        <span className="learn-donut-pct">68%</span>
                        <small className="learn-donut-cap">{t('chat.fluencyLabel')}</small>
                      </div>
                    </div>
                  </div>
                  <div className="skill-bars learn-skill-bars">
                    {CHAT_CONVERSATION_METRICS.map((row) => (
                      <div key={row.labelKey} className="skill-row">
                        <span>
                          <span>{t(row.labelKey)}</span>
                          <span>{row.pct}%</span>
                        </span>
                        <div className="skill-track">
                          <div className={`skill-fill skill-fill--${row.tone}`} style={{ width: `${row.pct}%` }} />
                        </div>
                      </div>
                    ))}
                  </div>
                  <button type="button" className="chat-mock-rail-more" onClick={() => navigateTo('progreso')}>
                    {t('chat.moreProgress')}
                  </button>
                </div>

                <div className="rail-card chat-mock-rail-card chat-mock-rail-card--expr">
                  <h3>{t('chat.useful')}</h3>
                  <ul className="chat-mock-expr-list">
                    {CHAT_EXPRESSION_KEYS.map((ek) => (
                      <li key={ek}>
                        <button type="button" className="chat-mock-expr-chip" onClick={() => setQuery(t(ek))}>
                          {t(ek)}
                        </button>
                      </li>
                    ))}
                  </ul>
                </div>

                <div className="rail-card chat-mock-rail-card chat-mock-rail-card--culture">
                  <h3>{t('corpus.cultural')}</h3>
                  <div className="chat-mock-culture-art" aria-hidden />
                  <p className="chat-mock-culture-text">{t('chat.culturalBlurb')}</p>
                </div>

                {chatContexts.length ? (
                  <div className="rail-card chat-mock-rail-card chat-mock-rail-card--evidence">
                    <h3>{t('chat.evidence')}</h3>
                    <div className="chat-evidence-list chat-evidence-list--rail">
                      {chatContexts.map((c, idx) => (
                        <article key={c.id != null ? String(c.id) : `ctx-${idx}`} className="chat-context-card">
                          <span className="chat-context-type">{formatChatRecordType(c.record_type)}</span>
                          <strong className="chat-context-nasa">{c.nasa_yuwe}</strong>
                          <p className="chat-context-es">{c.espanol}</p>
                          <small className="chat-context-meta">
                            {c.categoria}
                            {formatChatEvidenceSource(c) ? ` · ${formatChatEvidenceSource(c)}` : ''}
                          </small>
                        </article>
                      ))}
                    </div>
                  </div>
                ) : null}

                <div className="rail-card chat-mock-rail-card chat-mock-rail-card--pronounce">
                  <Mic className="chat-mock-pron-ico" size={36} strokeWidth={2} aria-hidden />
                  <p className="chat-mock-pron-title">{t('chat.pronounceTitle')}</p>
                  <p className="chat-mock-pron-sub">{t('chat.pronounceSub')}</p>
                  <button
                    type="button"
                    className="explore-promo-btn chat-mock-pron-cta"
                    onClick={() => notify(t('practice.audioSoon'))}
                  >
                    {t('chat.pronounceAction')}
                  </button>
                </div>
              </aside>
            </div>

            <footer className="chat-mock-footer woven-strip-muted">
              <span className="chat-mock-footer-diamond" aria-hidden />
              <p>{t('pageFoot')}</p>
              <span className="chat-mock-footer-diamond" aria-hidden />
            </footer>
          </div>
        )}

        {view === 'progreso' && (
          <div className="page-shell progress-page">
            <div className="progress-dash-layout">
              <div className="progress-dash-main">
                <header className="progress-page-intro">
                  <h2>{t('progress.pageTitle')}</h2>
                  <p>{t('progress.pageSub')}</p>
                  <p className="progress-demo-ribbon">{t('progress.demoRibbon')}</p>
                </header>
                <div className="progress-kpi-grid">
                  <article className="stat-card stat-card--kpi stat-card--bar-green">
                    <label>{t('progress.lessons')}</label>
                    <div className="val">24 / 48</div>
                    <div className="bar">
                      <i style={{ width: '50%' }} />
                    </div>
                  </article>
                  <article className="stat-card stat-card--kpi stat-card--bar-mustard">
                    <label>{t('progress.exercises')}</label>
                    <div className="val">156 / 230</div>
                    <div className="bar">
                      <i style={{ width: '68%' }} />
                    </div>
                  </article>
                  <article className="stat-card stat-card--kpi stat-card--bar-lilac">
                    <label>{t('progress.score')}</label>
                    <div className="val">85%</div>
                    <div className="bar">
                      <i style={{ width: '85%' }} />
                    </div>
                  </article>
                  <article className="stat-card stat-card--kpi stat-card--bar-sky">
                    <label>{t('progress.time')}</label>
                    <div className="val">18 h 45 m</div>
                    <div className="bar">
                      <i style={{ width: '72%' }} />
                    </div>
                  </article>
                </div>

                <div className="progress-mid-grid">
                  <article className="progress-panel progress-panel--trend">
                    <h3>{t('progress.chart1')}</h3>
                    <div className="progress-trend-body">
                      <svg className="progress-line-chart" viewBox="0 0 400 120" preserveAspectRatio="none">
                        <title>Avance últimos días</title>
                        <defs>
                          <linearGradient id="progressLineGrad" x1="0" y1="0" x2="0" y2="1">
                            <stop offset="0%" stopColor="rgba(45,106,79,0.35)" />
                            <stop offset="100%" stopColor="rgba(45,106,79,0.02)" />
                          </linearGradient>
                        </defs>
                        <path
                          fill="url(#progressLineGrad)"
                          d="M0,105 L40,95 L80,92 L120,82 L160,74 L200,62 L240,52 L280,42 L320,38 L360,34 L400,28 L400,120 L0,120 Z"
                        />
                        <polyline
                          fill="none"
                          stroke="var(--forest-soft)"
                          strokeWidth="3"
                          strokeLinejoin="round"
                          strokeLinecap="round"
                          points="0,105 40,95 80,92 120,82 160,74 200,62 240,52 280,42 320,38 360,34 400,28"
                        />
                      </svg>
                      <div className="progress-trend-caption">
                        <strong>65%</strong>
                        <span>Avance actual</span>
                      </div>
                    </div>
                  </article>
                  <article className="progress-panel">
                    <h3>{t('progress.chart2')}</h3>
                    <ul className="progress-skill-rows">
                      {[
                        ['Vocabulario', 72],
                        ['Gramática', 60],
                        ['Comprensión', 68],
                        ['Conversación', 70],
                        ['Escritura', 55],
                      ].map(([label, pct]) => (
                        <li key={label}>
                          <div className="progress-skill-label">
                            <span>{label}</span>
                            <span>{pct}%</span>
                          </div>
                          <div className="progress-mini-bar">
                            <i style={{ width: `${pct}%` }} />
                          </div>
                        </li>
                      ))}
                    </ul>
                  </article>
                </div>

                <div className="progress-bottom-grid">
                  <article className="progress-panel">
                    <h3>Progreso por temas</h3>
                    <ul className="progress-skill-rows progress-skill-rows--topics">
                      {[
                        ['Saludos', 80],
                        ['Familia', 65],
                        ['Hogar', 72],
                        ['Naturaleza', 58],
                        ['Tiempo', 62],
                      ].map(([label, pct]) => (
                        <li key={label}>
                          <div className="progress-skill-label">
                            <span>{label}</span>
                            <span>{pct}%</span>
                          </div>
                          <div className="progress-mini-bar progress-mini-bar--sage">
                            <i style={{ width: `${pct}%` }} />
                          </div>
                        </li>
                      ))}
                    </ul>
                  </article>
                  <article className="progress-panel progress-panel--achievements">
                    <h3>Logros recientes</h3>
                    <ul className="progress-badge-list">
                      <li>
                        <span className="progress-badge-ico progress-badge-ico--msg">
                          <MessageCircle size={18} aria-hidden />
                        </span>
                        <div>
                          <strong>Conversador</strong>
                          <small>Hace 2 días</small>
                        </div>
                      </li>
                      <li>
                        <span className="progress-badge-ico progress-badge-ico--compass">
                          <Compass size={18} aria-hidden />
                        </span>
                        <div>
                          <strong>Explorador</strong>
                          <small>Hace 5 días</small>
                        </div>
                      </li>
                      <li>
                        <span className="progress-badge-ico progress-badge-ico--cup">
                          <Trophy size={18} aria-hidden />
                        </span>
                        <div>
                          <strong>Constancia</strong>
                          <small>Hace 1 semana</small>
                        </div>
                      </li>
                    </ul>
                  </article>
                </div>

                <div className="progress-footer-banner" aria-hidden="false">
                  <img src={BRAND_ASSETS.welcome} alt="" className="progress-footer-visual" />
                  <div className="progress-footer-copy">
                    <p className="progress-footer-call">¡Pá kiwe thegnas!</p>
                    <p>Sigue hilando cada palabra como semilla para nuestra comunidad.</p>
                  </div>
                </div>
              </div>

              <aside className="progress-dash-aside" aria-label="Resumen y actividad">
                <section className="progress-aside-card progress-aside-card--streak">
                  <h4>Racha de aprendizaje</h4>
                  <div className="progress-streak-ring">
                    <span>{streakDays}</span>
                    <small>días</small>
                  </div>
                  <div className="progress-week-mini" role="list">
                    {PROGRESS_WEEK_LABELS.map((d, idx) => (
                      <span
                        key={d}
                        role="listitem"
                        className={streakWeekSlots[idx] ? 'week-on' : 'week-off'}
                      >
                        <small>{d}</small>
                        {streakWeekSlots[idx] ? <Check size={14} aria-hidden /> : <span className="week-dot" />}
                      </span>
                    ))}
                  </div>
                </section>

                <section className="progress-aside-card">
                  <h4>Nivel actual</h4>
                  <div className="progress-level-pill">{profile.level}</div>
                  <p className="progress-level-meta">65% camino al nivel Avanzado</p>
                  <div className="progress-mini-bar progress-mini-bar--gold">
                    <i style={{ width: '65%' }} />
                  </div>
                </section>

                <section className="progress-aside-card progress-aside-card--activity">
                  <h4>Actividad reciente</h4>
                  <ul>
                    <li>
                      Completaste la lección «Familia y personas»
                      <small>Hace 2 horas</small>
                    </li>
                    <li>
                      Practicaste 12 ejercicios de vocabulario
                      <small>Ayer</small>
                    </li>
                    <li>
                      Conversación con AVI sobre saludos cotidianos
                      <small>Hace 1 día</small>
                    </li>
                  </ul>
                </section>
              </aside>
            </div>
          </div>
        )}

        {view === 'configuracion' && (
          <div className={`page-shell settings-page${auth.role === 'administrador' ? ' settings-page--admin' : ''}`}>
            <header className="page-title settings-title-wrap">
              <h2>{t('nav.configuracion')}</h2>
              <p>{auth.role === 'administrador' ? t('admin.settingsAdminIntro') : t('settings.pageSub')}</p>
              <div className="woven-strip woven-strip--thin" />
            </header>
            {auth.role === 'administrador' ? (
              <section className="settings-admin-strip" aria-label={t('admin.settingsAdminQuick')}>
                <h3 className="settings-admin-strip-title">{t('admin.settingsAdminQuick')}</h3>
                <div className="settings-admin-quick-grid">
                  {[
                    'admin_usuarios',
                    'admin_contenido',
                    'admin_reportes',
                    'admin_grupos',
                    'admin_auditoria',
                    'admin_correos',
                    'admin_soporte',
                  ].map((id) => (
                    <button key={id} type="button" className="settings-admin-quick-tile" onClick={() => navigateTo(id)}>
                      {t(NAV_REGISTRY[id]?.labelKey || 'nav.inicio')}
                    </button>
                  ))}
                </div>
                <p className="settings-admin-strip-note">{t('admin.settingsAdminHideStudent')}</p>
              </section>
            ) : null}
            <div className="settings-tabs">
              {[
                ['general', 'General'],
                ['learning', 'Aprendizaje'],
                ['notifications', 'Notificaciones'],
                ['privacy', 'Privacidad'],
                ['appearance', 'Idioma y apariencia'],
              ].map(([id, lab]) => (
                <button
                  key={id}
                  type="button"
                  className={settingsTab === id ? 'active' : ''}
                  onClick={() => setSettingsTab(id)}
                >
                  {lab}
                </button>
              ))}
            </div>
            <div className="settings-layout">
              <div className="settings-main">
                {(settingsTab === 'general' || settingsTab === 'learning') && (
                <section className="settings-card settings-card--feature">
                  <div className="settings-feature-icon feature-green">
                    <User size={20} />
                  </div>
                  <div className="settings-feature-body">
                    <div className="settings-card-head">
                      <div>
                        <h3>Perfil y cuenta</h3>
                        <p>Gestiona tu informacion personal y preferencias de cuenta.</p>
                      </div>
                      <button type="button" onClick={() => notify('Puedes editar tu nombre directamente en este formulario.')}>
                        Editar perfil
                      </button>
                    </div>
                    <div className="settings-fields-2">
                      <label className="row">
                        Nombre
                        <input
                          type="text"
                          value={profile.name || 'María'}
                          onChange={(e) => setProfile((p) => ({ ...p, name: e.target.value }))}
                        />
                      </label>
                      <label className="row">
                        Correo electronico
                        <input type="email" value={profile.email || 'estudiante.demo@nasayuwe.local'} readOnly />
                      </label>
                    </div>
                  </div>
                </section>
                )}

                {isSettingsSectionVisible('learning') && (
                <section className="settings-card settings-card--feature">
                  <div className="settings-feature-icon feature-amber">
                    <BookOpen size={20} />
                  </div>
                  <div className="settings-feature-body">
                    <div className="settings-card-head">
                      <div>
                        <h3>Preferencias de aprendizaje</h3>
                        <p>Ajusta como y que quieres aprender.</p>
                      </div>
                      <button type="button" onClick={() => notify('Preferencias actualizadas.')}>Personalizar</button>
                    </div>
                    <div className="settings-fields-3">
                      <label className="row">
                        Nivel de dificultad
                        <select value={profile.level} onChange={(e) => setProfile((p) => ({ ...p, level: e.target.value }))}>
                          <option>Basico</option>
                          <option>Intermedio</option>
                          <option>Avanzado</option>
                        </select>
                      </label>
                      <label className="row">
                        Objetivo de estudio
                        <select value={profile.goal} onChange={(e) => setProfile((p) => ({ ...p, goal: e.target.value }))}>
                          <option>Conversación fluida</option>
                          <option>Comprension lectora</option>
                          <option>Vocabulario diario</option>
                        </select>
                      </label>
                      <label className="row row-toggle">
                        <span>Recordatorios de estudio</span>
                        <input
                          type="checkbox"
                          checked={profile.reminders}
                          onChange={(e) => setProfile((p) => ({ ...p, reminders: e.target.checked }))}
                        />
                      </label>
                    </div>
                  </div>
                </section>
                )}

                {isSettingsSectionVisible('notifications') && (
                <section className="settings-card settings-card--feature">
                  <div className="settings-feature-icon feature-lilac">
                    <Bell size={20} />
                  </div>
                  <div className="settings-feature-body">
                    <div className="settings-card-head">
                      <div>
                        <h3>Notificaciones</h3>
                        <p>Elige como y cuando quieres recibir notificaciones.</p>
                      </div>
                      <button type="button" onClick={() => notify('Configuración de notificaciones guardada.')}>Configurar</button>
                    </div>
                    <div className="settings-check-grid">
                      <label>
                        <input
                          type="checkbox"
                          checked={notifPrefs.daily}
                          onChange={(e) => setNotifPrefs((c) => ({ ...c, daily: e.target.checked }))}
                        />
                        Recordatorios de actividades diarias
                      </label>
                      <label>
                        <input
                          type="checkbox"
                          checked={notifPrefs.streak}
                          onChange={(e) => setNotifPrefs((c) => ({ ...c, streak: e.target.checked }))}
                        />
                        Logros y racha de aprendizaje
                      </label>
                      <label>
                        <input
                          type="checkbox"
                          checked={notifPrefs.content}
                          onChange={(e) => setNotifPrefs((c) => ({ ...c, content: e.target.checked }))}
                        />
                        Nuevas lecciones y contenidos
                      </label>
                      <label>
                        <input
                          type="checkbox"
                          checked={notifPrefs.tips}
                          onChange={(e) => setNotifPrefs((c) => ({ ...c, tips: e.target.checked }))}
                        />
                        Consejos y recomendaciones
                      </label>
                    </div>
                  </div>
                </section>
                )}

                {isSettingsSectionVisible('appearance') && (
                <section className="settings-card settings-card--feature">
                  <div className="settings-feature-icon feature-blue">
                    <Palette size={20} />
                  </div>
                  <div className="settings-feature-body">
                    <div className="settings-card-head">
                      <div>
                        <h3>Idioma y apariencia</h3>
                        <p>Personaliza el idioma de la interfaz y el tema visual.</p>
                      </div>
                      <button type="button">Personalizar</button>
                    </div>
                    <div className="settings-fields-2">
                      <label className="row">
                        Idioma de la interfaz
                        <select
                          value={profile.language}
                          onChange={(e) => setProfile((p) => ({ ...p, language: e.target.value }))}
                        >
                          <option>Español</option>
                          <option>Nasa Yuwe</option>
                          <option>Bilingüe</option>
                        </select>
                      </label>
                      <div className="row">
                        Tema visual
                        <div className="theme-pills">
                          <button
                            type="button"
                            className={profile.theme === 'Claro Nasa' ? 'active' : ''}
                            onClick={() => setProfile((p) => ({ ...p, theme: 'Claro Nasa' }))}
                          >
                            <Sun size={14} /> Claro
                          </button>
                          <button
                            type="button"
                            className={profile.theme === 'Oscuro' ? 'active' : ''}
                            onClick={() => setProfile((p) => ({ ...p, theme: 'Oscuro' }))}
                          >
                            <Moon size={14} /> Oscuro
                          </button>
                          <button
                            type="button"
                            className={profile.theme === 'Cultural' ? 'active' : ''}
                            onClick={() => setProfile((p) => ({ ...p, theme: 'Cultural' }))}
                          >
                            <TargetIcon size={14} /> Nasa
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </section>
                )}
              </div>

              <aside className="settings-side-stack">
                <section className="settings-aside">
                  <h4>Mi cuenta</h4>
                  <div className="settings-avatar-wrap">
                    <img src={BRAND_ASSETS.welcome} alt="Perfil AVI" className="settings-avatar-image" />
                    <button
                      type="button"
                      className="settings-avatar-camera"
                      aria-label="Cambiar foto"
                      onClick={() => notify('Carga de foto disponible en la siguiente versión.')}
                    >
                      <Camera size={12} />
                    </button>
                  </div>
                  <strong>{profile.name || 'María'}</strong>
                  <p className="settings-level-pill">
                    <ShieldCheck size={14} /> {profile.level}
                  </p>
                  <small>Miembro desde: 12/04/2024</small>
                </section>
                <section className="settings-side-card">
                  <h4>Seguridad</h4>
                  <button type="button" onClick={handleChangePassword}>
                    <KeyRound size={14} /> Cambiar contraseña <ChevronRight size={14} />
                  </button>
                  <button type="button" onClick={handleToggleSessions}>
                    <Eye size={14} /> Ver sesiones activas <ChevronRight size={14} />
                  </button>
                  {showSessions ? (
                    <div className="settings-inline-note">
                      {studentSessions.length ? (
                        studentSessions.map((s) => (
                          <p key={s.id}>
                            {s.current ? 'Sesion actual' : 'Sesion activa'} · expira{' '}
                            {new Date(Number(s.expires_at || 0) * 1000).toLocaleString('es-CO')}
                          </p>
                        ))
                      ) : (
                        <p>No hay sesiones activas para mostrar.</p>
                      )}
                    </div>
                  ) : null}
                  {auth.role !== 'administrador' ? (
                    <button type="button" onClick={handleDeleteAccount}>
                      <Trash2 size={14} /> Eliminar cuenta <ChevronRight size={14} />
                    </button>
                  ) : (
                    <p className="settings-inline-note">{t('admin.settingsAdminHideStudent')}</p>
                  )}
                </section>
                <section className="settings-side-card">
                  <h4>Datos y privacidad</h4>
                  <button type="button" onClick={handleDownloadData}>
                    <Download size={14} /> Descargar mis datos <ChevronRight size={14} />
                  </button>
                </section>
              </aside>
            </div>
          </div>
        )}
      </main>

      <nav className="bottom-nav" aria-label="Navegación principal">
        {bottomNavItems.map((item) => (
          <button
            key={item.id}
            type="button"
            className={view === item.id ? 'active' : ''}
            onClick={() => navigateTo(item.id)}
          >
            <item.icon size={22} strokeWidth={view === item.id ? 2.2 : 1.8} />
            {t(item.labelKey)}
          </button>
        ))}
        <button
          type="button"
          className={`bottom-nav-menu-all${mobileNavOpen ? ' active' : ''}`}
          onClick={() => setMobileNavOpen(true)}
          aria-label={t('nav.fullMenu')}
          title={t('navHint.fullMenu')}
        >
          <Menu size={22} strokeWidth={mobileNavOpen ? 2.2 : 1.8} />
          {t('nav.fullMenu')}
        </button>
      </nav>
    </div>
  )
}
