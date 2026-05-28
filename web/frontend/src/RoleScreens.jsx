import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import {
  postAuthorized,
  getActivityAdv,
  getTeacherGroups,
  getTeacherStudents,
  getTeacherGroupReport,
  getTeacherGrades,
  getTeacherActivities,
  createTeacherActivity,
  submitTeacherContent,
  getTeacherReportsSummary,
  updateTeacherActivity,
  postTeacherGroupUnassign,
  getAdminUsers,
  getAdminCms,
  getAdminStatsDash,
  getAdminGrades,
  saveAdminGrade,
  deleteAdminGrade,
  assignStudentGrade,
  getAdminContentSubmissions,
  reviewAdminContentSubmission,
  getAdminGroups,
  getAdminAudit,
  getAdminMailHistory,
  postAdminMailSend,
  getAdminSupportTickets,
  postAdminSupportTicket,
  postAdminUserCreate,
  getStudentProfileSchool,
  getStudentActivities,
  getTeacherMessagingState,
  saveTeacherMessagingState,
} from './api'
import { ActivityOptionVisual, ActivityQuestionImage } from './ActivityMedia'
import { speakText } from './corpusUtils'
import { validatePasswordStrength } from './passwordPolicy'
import {
  Activity,
  ArrowLeft,
  BarChart3,
  BookMarked,
  BookOpen,
  CalendarDays,
  CheckCircle,
  Clock,
  ClipboardList,
  CircleHelp,
  Inbox,
  History,
  Send,
  Database,
  Eye,
  FileEdit,
  FileText,
  Filter,
  GraduationCap,
  House,
  ImageIcon,
  ListChecks,
  Mail,
  MessageCircle,
  MoreVertical,
  PenLine,
  Pencil,
  Plus,
  Search,
  Settings,
  ShieldCheck,
  SlidersHorizontal,
  Trash2,
  TrendingUp,
  UserPlus,
  Target,
  UserCheck,
  UsersRound,
  Wheat,
  Leaf,
  Layers,
  XCircle,
  X,
  Droplet,
  Flame,
  Mountain,
  Trees,
  Volume2,
  FolderOpen,
  MessageSquare,
  Calendar,
  Download,
} from 'lucide-react'

export { StudentDictionaryRoute } from './YuweStudentDictionary'

import learnWelcomeIllustration from './assets/imagenes/bienvenida.png'

const LEARN_THEME_FILTERS = ['todos', 'vocabulario', 'gramatica', 'expresiones', 'cultura']

const LEARN_MODULES = [
  { key: 'saludos', filterKey: 'vocabulario', slug: 'saludos', pct: 80, words: 15, lessons: 5, Icon: Leaf, tone: 'green' },
  { key: 'familia', filterKey: 'vocabulario', slug: 'familia', pct: 40, words: 18, lessons: 4, Icon: UsersRound, tone: 'orange' },
  { key: 'casa', filterKey: 'gramatica', slug: 'casa', pct: 20, words: 22, lessons: 6, Icon: House, tone: 'blue' },
  { key: 'naturaleza', filterKey: 'cultura', slug: 'naturaleza', pct: 0, words: 24, lessons: 5, Icon: Wheat, tone: 'purple' },
  { key: 'tiempo', filterKey: 'expresiones', slug: 'tiempo', pct: 0, words: 12, lessons: 4, Icon: CalendarDays, tone: 'red' },
]

/** Tema del listado Aprender → pestaña de Practicar (corpus) al pulsar Continuar / Empezar. */
const LEARN_FILTER_TO_PRACTICE_TAB = {
  vocabulario: 'vocabulario',
  gramatica: 'gramatica',
  expresiones: 'conversacion',
  cultura: 'imagen',
}

const LEARN_SKILL_ROWS = [
  { labelKey: 'home.skillVocab', pct: 72, tone: 'vocab' },
  { labelKey: 'home.skillGrammar', pct: 60, tone: 'gram' },
  { labelKey: 'home.skillComp', pct: 58, tone: 'comp' },
  { labelKey: 'home.skillConv', pct: 70, tone: 'conv' },
]

/** —— Practice (Practicar) mockup tabs ↔ API activity modes —— */
const PRACTICE_TAB_DEF = [
  { id: 'vocabulario', mode: 'quiz', labelKey: 'practice.tabVocab' },
  { id: 'gramatica', mode: 'completar', labelKey: 'practice.tabGrammar' },
  { id: 'imagen', mode: 'imagen', labelKey: 'act.modeImg' },
  { id: 'escucha', mode: 'quiz', labelKey: 'practice.tabListen' },
  { id: 'conversacion', mode: 'quiz', labelKey: 'practice.tabConversation' },
  { id: 'escritura', mode: 'completar', labelKey: 'practice.tabWriting' },
]

/** Categorías del corpus a probar si la seleccionada no tiene suficientes ítems para el modo. */
const CORPUS_PRACTICE_CATEGORY_FALLBACKS = [
  'comida',
  'numeros',
  'animales',
  'colores',
  'saludos',
  'general',
  'diccionario_general',
  'familia_personas',
  'alimentos',
  'verbos',
  'frutas_verduras',
  'cuerpo_partes',
  'casa',
  'objetos',
  'elementos_agua',
  'plantas',
]

function normLearnCatKey(s) {
  return String(s || '')
    .trim()
    .toLowerCase()
    .replace(/\s+/g, '_')
    .replace(/_+/g, '_')
}

/** Compara glosas de actividad (trim + NFC) para evitar fallos por espacios o Unicode. */
function activityStringsEqual(a, b) {
  if (a == null && b == null) return true
  if (a == null || b == null) return false
  try {
    return (
      String(a).trim().normalize('NFC') === String(b).trim().normalize('NFC')
    )
  } catch {
    return String(a).trim() === String(b).trim()
  }
}

const PRACTICE_TRACK_STORAGE = 'avi-practice-track-v1'

function practiceTrackKey(tabId, catSlug) {
  return `${String(tabId || 'vocabulario')}::${normLearnCatKey(catSlug)}`
}

function readPracticeTrack() {
  try {
    if (typeof localStorage === 'undefined') return {}
    const raw = localStorage.getItem(PRACTICE_TRACK_STORAGE)
    const o = raw ? JSON.parse(raw) : {}
    return o && typeof o === 'object' ? o : {}
  } catch {
    return {}
  }
}

function writePracticeTrack(obj) {
  try {
    if (typeof localStorage !== 'undefined') localStorage.setItem(PRACTICE_TRACK_STORAGE, JSON.stringify(obj))
  } catch {
    /* ignore */
  }
}

function getPracticeRowProgress(tabId, catSlug) {
  const row = readPracticeTrack()[practiceTrackKey(tabId, catSlug)]
  if (!row) return { pct: 0, done: false }
  if (row.done) return { pct: 100, done: true }
  const p = Number(row.partial)
  if (!Number.isFinite(p)) return { pct: 0, done: false }
  return { pct: Math.round(Math.min(100, Math.max(0, p) * 100)), done: false }
}

function markPracticeProgress(tabId, catSlug, partial01, done) {
  const key = practiceTrackKey(tabId, catSlug)
  const all = readPracticeTrack()
  const prev = all[key] || {}
  const nextPartial = Math.max(Number(prev.partial) || 0, Math.min(1, Number(partial01) || 0))
  all[key] = {
    partial: nextPartial,
    done: Boolean(done || prev.done),
    updated: Date.now(),
  }
  writePracticeTrack(all)
}

function buildPracticeExploreCategories(appCats) {
  const out = []
  const push = (c) => {
    const s = String(c || '').trim()
    if (s && !out.includes(s)) out.push(s)
  }
  if (Array.isArray(appCats)) for (const c of appCats) push(c)
  for (const c of CORPUS_PRACTICE_CATEGORY_FALLBACKS) push(c)
  return out.slice(0, 18)
}

/** Alinea el slug del módulo Aprender con nombres reales de categoría en stats/corpus. */
function resolveLearnCategoryForCorpus(slugPrefer, cats) {
  const list = Array.isArray(cats) ? cats.filter(Boolean).map(String) : []
  const prefRaw = String(slugPrefer || '').trim()
  const pref = prefRaw || 'comida'
  const prefN = normLearnCatKey(pref)

  for (const c of list) {
    if (normLearnCatKey(c) === prefN) return c
  }
  for (const c of list) {
    const cn = normLearnCatKey(c)
    if (cn.includes(prefN) || prefN.includes(cn)) return c
  }

  const ALIASES = {
    saludos: ['saludos', 'general', 'comida', 'numeros'],
    familia: ['familia_personas', 'familia personas', 'familia', 'personas'],
    casa: ['casa', 'hogar', 'objetos', 'cuerpo_partes'],
    naturaleza: ['naturaleza', 'animales', 'plantas', 'colores', 'elementos_agua'],
    tiempo: ['tiempo', 'numeros', 'general', 'dias_semana'],
  }
  const tries = ALIASES[pref] || [pref, ...CORPUS_PRACTICE_CATEGORY_FALLBACKS]
  for (const t of tries) {
    const tn = normLearnCatKey(t)
    const hit = list.find((c) => normLearnCatKey(c) === tn)
    if (hit) return hit
  }
  for (const t of tries) {
    const tn = normLearnCatKey(t)
    const hit = list.find(
      (c) => normLearnCatKey(c).includes(tn) || tn.includes(normLearnCatKey(c)),
    )
    if (hit) return hit
  }
  const fallbackTry = tries.map(String).find(Boolean) || 'comida'
  return list[0] || fallbackTry
}

const PRACTICE_TAB_ICONS = {
  vocabulario: BookOpen,
  gramatica: ListChecks,
  imagen: ImageIcon,
  escucha: Volume2,
  conversacion: MessageCircle,
  escritura: PenLine,
}

const PRACTICE_WEEK_SHORT = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']

function normalizeActivityMode(mode) {
  const m = String(mode || '')
    .toLowerCase()
    .trim()
    .replace(/\s+/g, '_')
  if (m === 'quiz' || m === 'completar' || m === 'imagen') return m
  if (m.includes('complet')) return 'completar'
  if (m.includes('image') || m.includes('img')) return 'imagen'
  return 'quiz'
}

function normalizeDifficulty(d) {
  const s = String(d || '').toLowerCase()
  if (s.includes('facil') || s.includes('fácil') || s === 'easy') return 'facil'
  if (s.includes('avanz')) return 'avanzado'
  if (s.includes('inter')) return 'intermedio'
  return 'intermedio'
}

/** Ubica la pestaña del mock para reflejar el modo que viene del servidor / docente. */
function practiceTabFromServerMode(mode) {
  switch (normalizeActivityMode(mode)) {
    case 'completar':
      return 'gramatica'
    case 'imagen':
      return 'imagen'
    default:
      return 'vocabulario'
  }
}

function activityModeLabel(t, mode) {
  const m = normalizeActivityMode(mode)
  if (m === 'completar') return t('act.modeSentence')
  if (m === 'imagen') return t('act.modeImg')
  return t('act.modeQuiz')
}

function extractSpanishCue(prompt) {
  const m = String(prompt || '').match(/'([^']+)'/)
  return m ? m[1].trim() : ''
}

function spotlightWord(q) {
  if (q?.espanol) return String(q.espanol).trim()
  return extractSpanishCue(q?.prompt || '') || '—'
}

function practiceQuestionCopyKey(tabId, qtype) {
  if (qtype === 'imagen') return 'practice.qImagePick'
  if (tabId === 'gramatica' || tabId === 'escritura') return 'practice.qGrammarBlank'
  if (tabId === 'escucha') return 'practice.qListenPick'
  if (tabId === 'conversacion') return 'practice.qConversation'
  return 'practice.qPickNasa'
}

function StudentPracticeAside({ t, navigateTo }) {
  const donutPct = 65
  return (
    <aside className="practice-mock-rail">
      <div className="practice-rail-card practice-rail-prog">
        <h3>{t('practice.progressPanelTitle')}</h3>
        <div className="learn-donut-wrap learn-donut-wrap--mockup">
          <div
            className="learn-donut learn-donut--mockup"
            style={{
              background: `conic-gradient(#2f6f4a 0% ${donutPct}%, #ede8dc ${donutPct}% 100%)`,
            }}
          >
            <div className="learn-donut-inner learn-donut-inner--mockup">
              <span className="learn-donut-pct">{donutPct}%</span>
              <small className="learn-donut-cap">{t('practice.donutCorrect')}</small>
            </div>
          </div>
          <div className="skill-bars learn-skill-bars">
            {LEARN_SKILL_ROWS.map((row) => (
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
        </div>
      </div>

      <div className="practice-rail-card practice-rail-streak-box">
        <h3>{t('practice.practiceStreak')}</h3>
        <div className="streak-week streak-week--full practice-streak-row">
          {PRACTICE_WEEK_SHORT.map((d, i) => (
            <span key={d} className={`streak-slot${i < 6 ? ' done' : ''}`}>
              <span className="streak-dot" aria-hidden />
              <span className="streak-label">{d.slice(0, 3)}</span>
            </span>
          ))}
        </div>
      </div>

      <div className="practice-rail-card practice-rail-cultural">
        <div className="learn-cultural-visual learn-cultural-visual--rail" aria-hidden />
        <h3>{t('learn.tipTitle')}</h3>
        <p>{t('learn.tipText')}</p>
        <button type="button" className="learn-cultural-more" onClick={() => navigateTo('diccionario')}>
          {t('learn.tipLink')}
        </button>
      </div>

      <div className="practice-rail-card practice-rail-conv">
        <p className="practice-rail-conv-q">{t('practice.askConv')}</p>
        <button type="button" className="practice-rail-conv-btn" onClick={() => navigateTo('conversar')}>
          {t('practice.goChat')}
        </button>
      </div>
    </aside>
  )
}

function labelSlug(value) {
  return String(value || '').replaceAll('_', ' ')
}

function titleLabel(value) {
  const clean = labelSlug(value)
  return clean ? clean.charAt(0).toUpperCase() + clean.slice(1) : 'Categoria'
}

function cleanWord(value) {
  return String(value || '—').replace(/^(el|la|los|las|un|una|unos|unas)\s+/i, '').trim() || '—'
}

function firstName(profile) {
  return String(profile?.name || 'Usuario').trim().split(/\s+/)[0] || 'Usuario'
}

function RoleMetric({ icon: Icon, label, value, tone = 'green' }) {
  return (
    <article className={`role-metric role-metric--${tone}`}>
      <span className="role-metric-icon" aria-hidden>
        <Icon size={20} />
      </span>
      <div>
        <strong>{value}</strong>
        <small>{label}</small>
      </div>
    </article>
  )
}

function MiniBars({ items, tone = 'green' }) {
  return (
    <div className={`mini-bars mini-bars--${tone}`}>
      {items.map((item) => (
        <div key={item.label} className="mini-bar-row">
          <span>{item.label}</span>
          <div className="mini-bar-track">
            <i style={{ width: `${item.value}%` }} />
          </div>
          <strong>{item.value}%</strong>
        </div>
      ))}
    </div>
  )
}

function RolePanel({ title, action, children, className = '' }) {
  return (
    <section className={`role-panel ${className}`}>
      <div className="role-panel-head">
        <h3>{title}</h3>
        {action}
      </div>
      {children}
    </section>
  )
}

function unixMs(u) {
  const n = Number(u || 0)
  if (!n) return 0
  return n < 1e12 ? n * 1000 : n
}

/** Fecha de ultima asignacion o de creacion (sin fecha ficticia de entrega). */
function teacherDueFmt(createdAt, assignedAt, locale = 'es-ES') {
  const ms = unixMs(assignedAt) || unixMs(createdAt)
  if (!ms) return '—'
  const d = new Date(ms)
  try {
    return d.toLocaleDateString(locale)
  } catch {
    return d.toISOString().slice(0, 10).split('-').reverse().join('/')
  }
}

function teacherTipoFromMode(mode) {
  const m = String(mode || '').toLowerCase()
  if (m === 'imagen') return 'Practica'
  if (m === 'completar' || m === 'quiz') return 'Ejercicio'
  return 'Leccion'
}

function teacherTipoLabelKey(mode) {
  const m = String(mode || '').toLowerCase()
  if (m === 'imagen') return 'teacher.actTypePractice'
  if (m === 'completar' || m === 'quiz') return 'teacher.actTypeExercise'
  return 'teacher.actTypeLesson'
}

function teacherUiStatusRow(statusRaw) {
  const s = String(statusRaw || 'active').toLowerCase()
  if (s === 'draft') return { labelKey: 'teacher.statusDraft', className: 'status-pill teacher-pill-muted' }
  if (s === 'scheduled') return { labelKey: 'teacher.statusScheduled', className: 'status-pill teacher-pill-info' }
  return { labelKey: 'teacher.statusActive', className: 'status-pill ok' }
}

function teacherWorkflowFromStatus(statusRaw) {
  const s = String(statusRaw || 'active').toLowerCase()
  if (s === 'draft') return 'borrador'
  if (s === 'scheduled') return 'programada'
  return 'activa'
}

/** @param {unknown} acts */
export function teacherDisplayActivitiesRows(activities) {
  const list = Array.isArray(activities) ? [...activities] : []
  list.sort((a, b) => unixMs(b?.created_at) - unixMs(a?.created_at))
  return list
}

const TEACHER_CAL_EVENTS_KEY = 'avi-teacher-calendar-events-v1'

/** @returns {{ id: string, title: string, dueMs: number }[]} */
function readTeacherCalEvents() {
  if (typeof window === 'undefined') return []
  try {
    const raw = window.localStorage.getItem(TEACHER_CAL_EVENTS_KEY)
    if (!raw) return []
    const arr = JSON.parse(raw)
    if (!Array.isArray(arr)) return []
    return arr.filter(
      (x) => x && typeof x.id === 'string' && typeof x.title === 'string' && typeof x.dueMs === 'number',
    )
  } catch {
    return []
  }
}

function writeTeacherCalEvents(events) {
  if (typeof window === 'undefined') return
  try {
    window.localStorage.setItem(TEACHER_CAL_EVENTS_KEY, JSON.stringify(events))
  } catch {
    /* ignore quota / private mode */
  }
}

/** Demo rows when storage is empty so the calendar is not blank on first visit. */
function seedTeacherCalEventsIfEmpty() {
  if (typeof window === 'undefined') return []
  const existing = readTeacherCalEvents()
  if (existing.length) return existing
  const now = new Date()
  const y = now.getFullYear()
  const m = now.getMonth()
  const lastD = new Date(y, m + 1, 0).getDate()
  const clampD = (d) => Math.min(Math.max(1, d), lastD)
  const atNoon = (day) => new Date(y, m, clampD(day), 12, 0, 0, 0).getTime()
  const seeded = [
    { id: 'seed-cal-1', title: 'Entrega: lectura con numeros (vocabulario)', dueMs: atNoon(6) },
    { id: 'seed-cal-2', title: 'Taller oral: saludos y presentaciones', dueMs: atNoon(14) },
    { id: 'seed-cal-3', title: 'Quiz: colores y animales', dueMs: atNoon(21) },
    { id: 'seed-cal-4', title: 'Cierre de unidad — comida y casa', dueMs: atNoon(Math.min(27, lastD)) },
  ]
  writeTeacherCalEvents(seeded)
  return seeded
}

function RoleListProgressBar({ pct }) {
  const p = Math.max(4, Math.min(100, Number(pct) || 0))
  return (
    <div className="role-row-progress-wrap" aria-hidden>
      <div className="mini-bar-track role-row-progress-track">
        <i style={{ width: `${p}%` }} />
      </div>
      <strong className="role-row-progress-val">{Math.round(p)}%</strong>
    </div>
  )
}

export function TeacherDashboard({ t, notify, profile, setView }) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const [summary, setSummary] = useState(null)

  useEffect(() => {
    async function load() {
      try {
        const s = await getTeacherReportsSummary(token, 30)
        setSummary(s)
      } catch {
        notify(t('teacher.loadErr'))
        setSummary(null)
      }
    }
    load()
  }, [notify, t, token])

  const totals = summary?.totals
  const displayGroups = (summary?.group_bars || []).slice(0, 4)
  const pendingSlice = (summary?.recent_activities || []).slice(0, 3)
  const pendingIcons = [PenLine, FileText, MessageCircle]

  return (
    <div className="teacher-workspace-shell">
      <div className="role-dashboard role-dashboard--teacher teacher-home-dashboard">
        <section className="role-hero role-hero--teacher">
          <div>
            <span className="role-eyebrow">
              <Leaf size={16} strokeWidth={2.2} /> {t('teacher.dashboardEyebrow')}
            </span>
            <h2>{t('teacher.dashboardGreeting', { name: firstName(profile) })}</h2>
            <p className="role-hero-sub">{t('teacher.dashboardSub')}</p>
          </div>
          <button type="button" className="teacher-hero-act" onClick={() => setView('docente_actividades')}>
            <Plus size={17} strokeWidth={2.2} /> {t('teacher.newActivityCta')}
          </button>
        </section>

        <section className="role-metrics">
          <RoleMetric icon={UsersRound} label={t('teacher.metricGroupsLbl')} value={totals?.groups ?? 0} />
          <RoleMetric
            icon={ClipboardList}
            label={t('teacher.metricActivitiesLbl')}
            value={totals?.group_assignments_window ?? 0}
            tone="gold"
          />
          <RoleMetric icon={TrendingUp} label={t('teacher.metricAvgLbl')} value={totals?.active_activities_all ?? 0} tone="green" />
          <RoleMetric icon={UserCheck} label={t('teacher.metricStudentsLbl')} value={totals?.students_in_groups ?? 0} tone="purple" />
        </section>

        <div className="role-board-grid role-board-grid--teacher-twocol">
          <RolePanel
            title={t('teacher.panelMyGroups')}
            action={
              <button type="button" className="role-panel-link-btn" onClick={() => setView('docente_grupos')}>
                {t('teacher.viewAllArrow')}
              </button>
            }
          >
            <div className="role-list teacher-group-progress-list">
              {displayGroups.length === 0 ? (
                <p className="doc-empty-visual">{t('teacher.noGroups')}</p>
              ) : (
                displayGroups.map((group) => (
                  <article key={group.id} className="role-list-item role-list-item--progress">
                    <span className="role-list-icon">
                      <UsersRound size={17} strokeWidth={2} />
                    </span>
                    <div className="role-list-body">
                      <strong>{group.name}</strong>
                      <small>{t('teacher.studentsLine', { n: group.students || 0 })}</small>
                      <RoleListProgressBar pct={group.bar_pct ?? 0} />
                    </div>
                  </article>
                ))
              )}
            </div>
          </RolePanel>

          <RolePanel
            title={t('teacher.panelPendingAct')}
            action={
              <button type="button" className="role-panel-link-btn" onClick={() => setView('docente_actividades')}>
                {t('teacher.viewAllArrow')}
              </button>
            }
          >
            <div className="role-task-list teacher-pending-task-list">
              {pendingSlice.length === 0 ? (
                <p className="doc-empty-visual">{t('teacher.noActivitiesRows')}</p>
              ) : (
                pendingSlice.map((row, index) => {
                  const Ico = pendingIcons[index % pendingIcons.length]
                  const grp = row.group_name || t('teacher.groupGeneric')
                  const rk = row.id != null ? String(row.id) : `p-${index}`
                  return (
                    <article key={rk} className="role-task teacher-pending-task">
                      <span className={`teacher-pending-task-ico tone-${index % 3}`}>
                        <Ico size={16} strokeWidth={2} />
                      </span>
                      <div>
                        <strong>
                          {`${t(teacherTipoLabelKey(row.mode))}: ${row.title || '—'}`}
                        </strong>
                        <small>
                          {grp} · {t('teacher.dueLabel')}: {teacherDueFmt(row.created_at, row.assigned_at)}
                        </small>
                      </div>
                    </article>
                  )
                })
              )}
            </div>
          </RolePanel>
        </div>
      </div>
    </div>
  )
}

/** Tabla: actividades del docente (solo datos del servidor). */
export function TeacherActivitiesPanel({ t, notify, navigateHome }) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const [groups, setGroups] = useState([])
  const [grades, setGrades] = useState([])
  const [activities, setActivities] = useState([])
  const [q, setQ] = useState('')
  const [groupFilter, setGroupFilter] = useState('')
  const [showForm, setShowForm] = useState(true)
  const [submitting, setSubmitting] = useState(false)
  const [draft, setDraft] = useState(() => ({
    title: '',
    description: '',
    category: 'comida',
    difficulty: 'intermedio',
    mode: 'quiz',
    workflow_status: 'activa',
    grade_id: '',
    group_id: '',
  }))
  const [actSheet, setActSheet] = useState(null)
  const [editDraft, setEditDraft] = useState(null)

  useEffect(() => {
    if (!actSheet || actSheet.mode !== 'edit' || actSheet.row?.id == null) {
      setEditDraft(null)
      return
    }
    const r = actSheet.row
    setEditDraft({
      title: r.title || '',
      description: r.description || r.title || '',
      category: r.category || 'comida',
      difficulty: r.difficulty || 'intermedio',
      mode: r.mode || 'quiz',
      workflow_status: teacherWorkflowFromStatus(r.status),
    })
  }, [actSheet])

  const reload = useCallback(async () => {
    try {
      const [g, gr, act] = await Promise.all([
        getTeacherGroups(token),
        getTeacherGrades(token),
        getTeacherActivities(token),
      ])
      setGroups(g.groups || [])
      setGrades(gr.grades || [])
      setActivities(act.activities || [])
    } catch {
      notify(t('teacher.loadErr'))
    }
  }, [notify, t, token])

  useEffect(() => {
    reload()
  }, [reload])

  useEffect(() => {
    if (!actSheet) return undefined
    function onEsc(ev) {
      if (ev.key === 'Escape') setActSheet(null)
    }
    window.addEventListener('keydown', onEsc)
    return () => window.removeEventListener('keydown', onEsc)
  }, [actSheet])

  const rows = useMemo(() => {
    const raw = teacherDisplayActivitiesRows(activities)
    const like = q.trim().toLowerCase()
    return raw.filter((row) => {
      if (groupFilter) {
        const gn = row.group_name || ''
        if (String(gn) !== groupFilter) return false
      }
      if (!like) return true
      return (
        String(row.title || '')
          .toLowerCase()
          .includes(like) ||
        String(row.category || '')
          .toLowerCase()
          .includes(like) ||
        teacherTipoFromMode(row.mode).toLowerCase().includes(like)
      )
    })
  }, [activities, q, groupFilter])

  const groupChoices = useMemo(() => {
    const names = new Set(groups.map((g) => g.name).filter(Boolean))
    rows.forEach((r) => {
      if (r.group_name) names.add(r.group_name)
    })
    return ['', ...[...names].sort()]
  }, [groups, rows])

  async function onCreate(ev) {
    ev.preventDefault()
    if (!draft.title.trim()) {
      notify(t('teacher.actTitleRequired'))
      return
    }
    setSubmitting(true)
    try {
      await createTeacherActivity(token, {
        title: draft.title.trim(),
        description: (draft.description || draft.title).trim(),
        category: draft.category,
        difficulty: draft.difficulty,
        mode: draft.mode,
        status: draft.workflow_status,
        grade_id: Number(draft.grade_id || 0),
        group_id: Number(draft.group_id || 0),
      })
      setDraft((d) => ({
        ...d,
        title: '',
        description: '',
      }))
      notify(t('teacher.actCreated'))
      reload()
    } catch (e) {
      notify(e.message || t('teacher.loadErr'))
    } finally {
      setSubmitting(false)
    }
  }

  async function saveActivityEdit(ev) {
    ev.preventDefault()
    if (!actSheet?.row?.id || !editDraft?.title?.trim()) return
    try {
      await updateTeacherActivity(token, {
        activity_id: actSheet.row.id,
        title: editDraft.title.trim(),
        description: (editDraft.description || editDraft.title).trim(),
        category: editDraft.category,
        difficulty: editDraft.difficulty,
        mode: editDraft.mode,
        status: editDraft.workflow_status,
      })
      notify(t('teacher.actUpdated'))
      setActSheet(null)
      reload()
    } catch (e) {
      notify(e.message || t('teacher.actUpdateErr'))
    }
  }

  async function duplicateActivity(row) {
    if (row?.id == null) return
    try {
      await createTeacherActivity(token, {
        title: `${String(row.title || '').trim() || 'Actividad'} (copia)`,
        description: (row.description || row.title || '').trim(),
        category: row.category || 'comida',
        difficulty: row.difficulty || 'intermedio',
        mode: row.mode || 'quiz',
        status: 'borrador',
        grade_id: 0,
        group_id: 0,
      })
      notify(t('teacher.actDupOk'))
      reload()
    } catch (e) {
      notify(e.message || t('teacher.actDupErr'))
    }
  }

  return (
    <div className="teacher-workspace-shell">
      <div className="page-shell doc-shell teacher-module teacher-module--activities">
        <header className="teacher-module-head">
          <div>
            <h2>{t('teacher.activitiesPageTitle')}</h2>
            <p>{t('teacher.activitiesPageSub')}</p>
          </div>
          <button type="button" className="dict-home-btn" onClick={navigateHome}>
            {t('teacher.homeTeacher')}
          </button>
        </header>

        <div className="teacher-act-toolbar">
          <button type="button" className="teacher-btn-primary-outline" onClick={() => setShowForm((v) => !v)}>
            <Plus size={17} strokeWidth={2.2} /> {t('teacher.newActivityBtn')}
          </button>
          <label className="teacher-search-field">
            <Search size={17} strokeWidth={2} aria-hidden />
            <input
              type="search"
              value={q}
              onChange={(ev) => setQ(ev.target.value)}
              placeholder={t('teacher.searchActivitiesPh')}
              autoComplete="off"
            />
          </label>
          <label className="teacher-filter-select">
            <span className="sr-only">{t('teacher.filterGroup')}</span>
            <select value={groupFilter} onChange={(ev) => setGroupFilter(ev.target.value)}>
              <option value="">{t('teacher.filterAllGroups')}</option>
              {groupChoices
                .filter(Boolean)
                .map((name) => (
                  <option key={name} value={name}>
                    {name}
                  </option>
                ))}
            </select>
          </label>
        </div>

        {showForm ? (
          <form className="teacher-act-create-card" onSubmit={onCreate}>
            <h3>{t('teacher.actFormTitle')}</h3>
            <div className="teacher-act-form-grid">
              <input
                value={draft.title}
                onChange={(ev) => setDraft((d) => ({ ...d, title: ev.target.value }))}
                placeholder={t('teacher.actTitlePh')}
                required
              />
              <textarea
                value={draft.description}
                onChange={(ev) => setDraft((d) => ({ ...d, description: ev.target.value }))}
                placeholder={t('teacher.actDescPh')}
                rows={2}
              />
              <select value={draft.mode} onChange={(ev) => setDraft((d) => ({ ...d, mode: ev.target.value }))}>
                <option value="quiz">{t('teacher.modeQuiz')}</option>
                <option value="completar">{t('teacher.modeComplete')}</option>
                <option value="imagen">{t('teacher.modeImage')}</option>
              </select>
              <select
                value={draft.workflow_status}
                onChange={(ev) => setDraft((d) => ({ ...d, workflow_status: ev.target.value }))}
              >
                <option value="activa">{t('teacher.statusActive')}</option>
                <option value="borrador">{t('teacher.statusDraft')}</option>
                <option value="programada">{t('teacher.statusScheduled')}</option>
              </select>
              <select value={draft.category} onChange={(ev) => setDraft((d) => ({ ...d, category: ev.target.value }))}>
                <option value="comida">comida</option>
                <option value="animales">animales</option>
                <option value="saludos">saludos</option>
                <option value="familia_personas">familia_personas</option>
                <option value="cultura">cultura</option>
              </select>
              <select
                value={draft.group_id}
                onChange={(ev) => setDraft((d) => ({ ...d, group_id: ev.target.value }))}
              >
                <option value="">{t('teacher.actPickGroupOpt')}</option>
                {groups.map((g) => (
                  <option key={g.id} value={g.id}>
                    {g.name}
                  </option>
                ))}
              </select>
              <select
                value={draft.grade_id}
                onChange={(ev) => setDraft((d) => ({ ...d, grade_id: ev.target.value }))}
              >
                <option value="">{t('teacher.actPickGradeOpt')}</option>
                {grades.map((g) => (
                  <option key={g.id} value={g.id}>
                    {g.name}
                  </option>
                ))}
              </select>
              <select
                value={draft.difficulty}
                onChange={(ev) => setDraft((d) => ({ ...d, difficulty: ev.target.value }))}
              >
                <option value="facil">{t('act.facil')}</option>
                <option value="intermedio">{t('act.intermedio')}</option>
                <option value="avanzado">{t('act.avanzado')}</option>
              </select>
            </div>
            <button type="submit" className="teacher-btn-solid" disabled={submitting}>
              {submitting ? t('teacher.sending') : t('teacher.actSave')}
            </button>
          </form>
        ) : null}

        <div className="admin-table-wrap teacher-act-table-wrap">
          <table className="doc-table admin-data-table teacher-act-table">
            <thead>
              <tr>
                <th>{t('teacher.colTitle')}</th>
                <th>{t('teacher.colType')}</th>
                <th>{t('teacher.colGroup')}</th>
                <th>{t('teacher.colDue')}</th>
                <th>{t('teacher.colStatus')}</th>
                <th>{t('teacher.colActions')}</th>
              </tr>
            </thead>
            <tbody>
              {rows.length === 0 ? (
                <tr>
                  <td colSpan={6} className="teacher-report-muted">
                    {t('teacher.noActivitiesRows')}
                  </td>
                </tr>
              ) : (
                rows.map((row) => {
                  const st = teacherUiStatusRow(row.status)
                  const idKey = row.id != null ? String(row.id) : row.title
                  return (
                    <tr key={idKey}>
                      <td>
                        <strong>{row.title}</strong>
                      </td>
                      <td>{t(teacherTipoLabelKey(row.mode))}</td>
                      <td>{row.group_name || '—'}</td>
                      <td className="admin-nowrap">{teacherDueFmt(row.created_at, row.assigned_at)}</td>
                      <td>
                        <span className={st.className}>{t(st.labelKey)}</span>
                      </td>
                      <td>
                        <div className="teacher-row-actions">
                          <button
                            type="button"
                            className="teacher-icon-btn"
                            title={t('teacher.edit')}
                            aria-label={t('teacher.edit')}
                            onClick={() => setActSheet({ row, mode: 'edit' })}
                          >
                            <Pencil size={16} strokeWidth={2} />
                          </button>
                          <button
                            type="button"
                            className="teacher-icon-btn"
                            title={t('teacher.view')}
                            aria-label={t('teacher.view')}
                            onClick={() => setActSheet({ row, mode: 'view' })}
                          >
                            <Eye size={16} strokeWidth={2} />
                          </button>
                          <button
                            type="button"
                            className="teacher-icon-btn"
                            title={t('teacher.actMoreSoon')}
                            aria-label={t('teacher.actMoreSoon')}
                            onClick={() => duplicateActivity(row)}
                          >
                            <MoreVertical size={16} strokeWidth={2} />
                          </button>
                        </div>
                      </td>
                    </tr>
                  )
                })
              )}
            </tbody>
          </table>
        </div>

        {actSheet ? (
          <div className="admin-modal" role="presentation" onClick={() => setActSheet(null)}>
            <div
              className="admin-modal-inner admin-modal-inner--wide teacher-act-sheet"
              role="dialog"
              aria-modal="true"
              aria-labelledby="teacher-act-sheet-title"
              onClick={(ev) => ev.stopPropagation()}
            >
              <button
                type="button"
                className="teacher-act-sheet-close"
                onClick={() => setActSheet(null)}
                aria-label={t('teacher.actModalClose')}
              >
                <X size={18} strokeWidth={2.2} aria-hidden />
              </button>
              <h3 id="teacher-act-sheet-title">
                {actSheet.mode === 'edit' ? t('teacher.actModalEditTitle') : t('teacher.actModalViewTitle')}
              </h3>
              {actSheet.mode === 'edit' ? <p className="admin-modal-intro">{t('teacher.actModalEditHint')}</p> : null}
              {actSheet.mode === 'edit' && editDraft ? (
                <form className="teacher-act-form-grid" onSubmit={saveActivityEdit}>
                  <input
                    value={editDraft.title}
                    onChange={(ev) => setEditDraft((d) => ({ ...d, title: ev.target.value }))}
                    placeholder={t('teacher.actTitlePh')}
                    required
                  />
                  <textarea
                    value={editDraft.description}
                    onChange={(ev) => setEditDraft((d) => ({ ...d, description: ev.target.value }))}
                    placeholder={t('teacher.actDescPh')}
                    rows={3}
                  />
                  <select value={editDraft.mode} onChange={(ev) => setEditDraft((d) => ({ ...d, mode: ev.target.value }))}>
                    <option value="quiz">{t('teacher.modeQuiz')}</option>
                    <option value="completar">{t('teacher.modeComplete')}</option>
                    <option value="imagen">{t('teacher.modeImage')}</option>
                  </select>
                  <select
                    value={editDraft.workflow_status}
                    onChange={(ev) => setEditDraft((d) => ({ ...d, workflow_status: ev.target.value }))}
                  >
                    <option value="activa">{t('teacher.statusActive')}</option>
                    <option value="borrador">{t('teacher.statusDraft')}</option>
                    <option value="programada">{t('teacher.statusScheduled')}</option>
                  </select>
                  <select value={editDraft.category} onChange={(ev) => setEditDraft((d) => ({ ...d, category: ev.target.value }))}>
                    <option value="comida">comida</option>
                    <option value="animales">animales</option>
                    <option value="saludos">saludos</option>
                    <option value="familia_personas">familia_personas</option>
                    <option value="cultura">cultura</option>
                  </select>
                  <select
                    value={editDraft.difficulty}
                    onChange={(ev) => setEditDraft((d) => ({ ...d, difficulty: ev.target.value }))}
                  >
                    <option value="facil">{t('act.facil')}</option>
                    <option value="intermedio">{t('act.intermedio')}</option>
                    <option value="avanzado">{t('act.avanzado')}</option>
                  </select>
                  <p>
                    <small>
                      {t('teacher.actModalRowId')}: <code>{String(actSheet.row.id)}</code> · {t('teacher.colGroup')}:{' '}
                      {actSheet.row.group_name || '—'}
                    </small>
                  </p>
                  <div className="modal-actions-row">
                    <button type="submit" className="teacher-btn-solid">
                      {t('teacher.actSaveEdit')}
                    </button>
                    <button type="button" onClick={() => setActSheet(null)}>
                      {t('teacher.actModalClose')}
                    </button>
                  </div>
                </form>
              ) : (
                <dl className="teacher-act-dl">
                  <dt>{t('teacher.colTitle')}</dt>
                  <dd>{actSheet.row.title || '—'}</dd>
                  <dt>{t('teacher.actModalDesc')}</dt>
                  <dd>{actSheet.row.description || '—'}</dd>
                  <dt>{t('teacher.colType')}</dt>
                  <dd>{t(teacherTipoLabelKey(actSheet.row.mode))}</dd>
                  <dt>{t('teacher.actModalTechMode')}</dt>
                  <dd>{String(actSheet.row.mode || '—')}</dd>
                  <dt>{t('teacher.actModalCategory')}</dt>
                  <dd>{actSheet.row.category || '—'}</dd>
                  <dt>{t('teacher.actModalDifficulty')}</dt>
                  <dd>{actSheet.row.difficulty || '—'}</dd>
                  <dt>{t('teacher.colGroup')}</dt>
                  <dd>{actSheet.row.group_name || '—'}</dd>
                  <dt>{t('teacher.colDue')}</dt>
                  <dd>{teacherDueFmt(actSheet.row.created_at, actSheet.row.assigned_at)}</dd>
                  <dt>{t('teacher.colStatus')}</dt>
                  <dd>
                    {(() => {
                      const ss = teacherUiStatusRow(actSheet.row.status)
                      return <span className={ss.className}>{t(ss.labelKey)}</span>
                    })()}
                  </dd>
                  <dt>{t('teacher.actModalRowId')}</dt>
                  <dd>
                    <code>{actSheet.row.id != null ? String(actSheet.row.id) : '—'}</code>
                  </dd>
                </dl>
              )}
              {actSheet.mode === 'view' ? (
                <div className="modal-actions-row">
                  <button type="button" onClick={() => setActSheet(null)}>
                    {t('teacher.actModalClose')}
                  </button>
                </div>
              ) : null}
            </div>
          </div>
        ) : null}

        <p className="teacher-module-foot">{t('teacher.activitiesFoot')}</p>
      </div>
    </div>
  )
}

function TeacherReportBarChart({ items }) {
  const h = 200
  const pad = { t: 18, r: 12, b: 28, l: 36 }
  const w = Math.max(280, items.length * 56 + pad.l + pad.r)
  const innerW = w - pad.l - pad.r
  const innerH = h - pad.t - pad.b
  const maxV = 100
  const barW = Math.min(44, innerW / Math.max(1, items.length) - 8)
  const gap =
    items.length <= 1
      ? 0
      : Math.max(4, (innerW - barW * items.length) / (items.length - 1))
  const xAt = (i) => pad.l + i * (barW + gap)

  function yAt(value) {
    const v = Math.max(0, Math.min(maxV, Number(value)))
    return pad.t + innerH - (v / maxV) * innerH
  }

  return (
    <svg className="teacher-report-svg" viewBox={`0 0 ${w} ${h}`} role="img" aria-label="">
      {[0, 25, 50, 75, 100].map((tick) => (
          <g key={tick}>
            <line
              x1={pad.l}
              x2={w - pad.r}
              y1={yAt(tick)}
              y2={yAt(tick)}
              stroke="rgba(26,61,43,0.12)"
              strokeWidth="1"
            />
            <text x={pad.l - 6} y={yAt(tick) + 4} className="teacher-report-svg-y">
              {tick}%
            </text>
          </g>
        ))}
      {items.map((it, i) => {
        const x = xAt(i)
        const yb = pad.t + innerH
        const yt = yAt(it.value)
        return (
          <g key={it.label}>
            <rect className="teacher-report-bar-fill" x={x} y={yt} width={barW} height={yb - yt} rx="6" ry="6" />
            <text className="teacher-report-svg-val" x={x + barW / 2} y={yt - 8} textAnchor="middle">
              {it.value}%
            </text>
            <text className="teacher-report-svg-x" x={x + barW / 2} y={h - 8} textAnchor="middle">
              {it.label}
            </text>
          </g>
        )
      })}
    </svg>
  )
}

export function TeacherReportsPanel({ t, notify, navigateHome }) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const [tab, setTab] = useState('resumen')
  const [range, setRange] = useState('30')
  const [summary, setSummary] = useState(null)

  useEffect(() => {
    async function load() {
      try {
        const days = Number(range) || 30
        const s = await getTeacherReportsSummary(token, days)
        setSummary(s)
      } catch {
        notify(t('teacher.loadErr'))
        setSummary(null)
      }
    }
    load()
  }, [notify, t, token, range])

  const totals = summary?.totals
  const disp = (summary?.group_bars || []).map((g) => ({
    label: (String(g.name || '').replace(/^Grupo\s*/i, 'G.') || '—').slice(0, 16),
    value: g.bar_pct ?? 0,
  }))
  const actRows = summary?.activities_tab || []
  const studRows = summary?.students_tab || []

  function exportCsv() {
    const head1 = `${t('teacher.repTabAct')}: ${t('teacher.colTitle')};${t('teacher.colType')};${t('teacher.colGroup')};${t('teacher.colStatus')};fecha\n`
    const body1 = actRows
      .map((r) =>
        [`"${String(r.title || '').replace(/"/g, '""')}"`, r.mode, r.group_name || '', r.status, teacherDueFmt(r.created_at, r.assigned_at)].join(
          ';',
        ),
      )
      .join('\n')
    const head2 = `\n${t('teacher.repTabStud')}: nombre;correo;grupo\n`
    const body2 = studRows
      .map((r) =>
        [`"${String(r.display_name || '').replace(/"/g, '""')}"`, r.email, r.group_name].join(';'),
      )
      .join('\n')
    const blob = new Blob([head1 + body1 + head2 + body2], { type: 'text/csv;charset=utf-8' })
    const a = document.createElement('a')
    a.href = URL.createObjectURL(blob)
    a.download = 'reportes-docente.csv'
    a.click()
    URL.revokeObjectURL(a.href)
    notify(t('teacher.exportOk'))
  }

  return (
    <div className="teacher-workspace-shell">
      <div className="page-shell doc-shell teacher-module teacher-module--reports">
        <header className="teacher-module-head">
          <div>
            <h2>{t('teacher.reportsPageTitle')}</h2>
            <p>{t('teacher.reportsPageSub')}</p>
          </div>
          <button type="button" className="dict-home-btn" onClick={navigateHome}>
            {t('teacher.homeTeacher')}
          </button>
        </header>

        <div className="teacher-report-toolbar">
          <label className="teacher-filter-select">
            <span className="sr-only">{t('teacher.reportRangeLbl')}</span>
            <select value={range} onChange={(ev) => setRange(ev.target.value)}>
              <option value="7">{t('teacher.range7')}</option>
              <option value="30">{t('teacher.range30')}</option>
              <option value="90">{t('teacher.range90')}</option>
            </select>
          </label>
          <button type="button" className="teacher-btn-solid teacher-btn-export" onClick={exportCsv}>
            <Download size={17} strokeWidth={2} /> {t('teacher.exportCsv')}
          </button>
        </div>

        <div className="teacher-report-tabs" role="tablist">
          {[
            ['resumen', 'teacher.repTabSumm'],
            ['grupo', 'teacher.repTabGrp'],
            ['actividad', 'teacher.repTabAct'],
            ['estudiante', 'teacher.repTabStud'],
          ].map(([id, key]) => (
            <button
              key={id}
              type="button"
              role="tab"
              aria-selected={tab === id}
              className={tab === id ? 'teacher-report-tab teacher-report-tab--active' : 'teacher-report-tab'}
              onClick={() => setTab(id)}
            >
              {t(key)}
            </button>
          ))}
        </div>

        {tab === 'resumen' ? (
          <>
            <section className="teacher-report-kpis">
              <article>
                <strong>{totals?.groups ?? 0}</strong>
                <span>{t('teacher.kpiAvg')}</span>
              </article>
              <article>
                <strong>{totals?.students_in_groups ?? 0}</strong>
                <span>{t('teacher.kpiPart')}</span>
              </article>
              <article>
                <strong>{totals?.activities_created_window ?? 0}</strong>
                <span>{t('teacher.kpiDone')}</span>
              </article>
              <article>
                <strong>{totals?.group_assignments_window ?? 0}</strong>
                <span>{t('teacher.kpiAvi')}</span>
              </article>
            </section>
            <section className="teacher-report-chart-card">
              <h3>{t('teacher.progressByGroup')}</h3>
              <div className="teacher-report-chart-wrap">
                {disp.length ? (
                  <TeacherReportBarChart items={disp.map((it) => ({ ...it }))} />
                ) : (
                  <p className="teacher-report-muted">{t('teacher.noReportData')}</p>
                )}
              </div>
            </section>
          </>
        ) : tab === 'grupo' ? (
          <section className="teacher-report-chart-card">
            <h3>{t('teacher.progressDetailGroup')}</h3>
            {disp.length ? (
              <MiniBars items={disp.map((it) => ({ label: it.label, value: it.value }))} />
            ) : (
              <p className="teacher-report-muted">{t('teacher.noReportData')}</p>
            )}
            <p className="teacher-module-foot" style={{ marginTop: '1rem' }}>
              {t('teacher.repSoonAct')}
            </p>
          </section>
        ) : tab === 'actividad' ? (
          <section className="teacher-report-chart-card">
            <h3>{t('teacher.repTabAct')}</h3>
            {actRows.length ? (
              <div className="admin-table-wrap">
                <table className="doc-table admin-data-table">
                  <thead>
                    <tr>
                      <th>{t('teacher.colTitle')}</th>
                      <th>{t('teacher.colType')}</th>
                      <th>{t('teacher.colGroup')}</th>
                      <th>{t('teacher.colStatus')}</th>
                      <th>{t('teacher.colDue')}</th>
                    </tr>
                  </thead>
                  <tbody>
                    {actRows.map((r) => (
                      <tr key={r.id}>
                        <td>{r.title}</td>
                        <td>{t(teacherTipoLabelKey(r.mode))}</td>
                        <td>{r.group_name || '—'}</td>
                        <td>
                          <span className={teacherUiStatusRow(r.status).className}>{t(teacherUiStatusRow(r.status).labelKey)}</span>
                        </td>
                        <td className="admin-nowrap">{teacherDueFmt(r.created_at, r.assigned_at)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            ) : (
              <p className="teacher-report-muted">{t('teacher.noReportData')}</p>
            )}
          </section>
        ) : (
          <section className="teacher-report-chart-card">
            <h3>{t('teacher.repTabStud')}</h3>
            {studRows.length ? (
              <div className="admin-table-wrap">
                <table className="doc-table admin-data-table">
                  <thead>
                    <tr>
                      <th>{t('teacher.colName')}</th>
                      <th>{t('teacher.colEmail')}</th>
                      <th>{t('teacher.colGroup')}</th>
                    </tr>
                  </thead>
                  <tbody>
                    {studRows.map((r) => (
                      <tr key={`${r.student_id}-${r.group_name}`}>
                        <td>{r.display_name}</td>
                        <td>{r.email}</td>
                        <td>{r.group_name}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            ) : (
              <p className="teacher-report-muted">{t('teacher.noReportData')}</p>
            )}
            <p className="teacher-module-foot" style={{ marginTop: '1rem' }}>
              {t('teacher.repSoonStud')}
            </p>
          </section>
        )}

        <p className="teacher-module-foot">{t('teacher.reportsFoot')}</p>
      </div>
    </div>
  )
}

export function TeacherMessagesPanel({ t, notify, navigateHome, sessionToken }) {
  const [threads, setThreads] = useState([])
  const [active, setActive] = useState('')
  const [draft, setDraft] = useState('')
  const saveTimerRef = useRef(null)

  useEffect(() => {
    let cancelled = false

    function defaultThreads() {
      return [
        {
          id: 'th1',
          with: t('teacher.msgThreadDrafts'),
          msgs: [
            {
              me: false,
              text: t('teacher.msgWelcome'),
              at: new Date().toLocaleString(),
            },
          ],
        },
      ]
    }

    async function load() {
      if (!sessionToken) {
        const init = defaultThreads()
        setThreads(init)
        setActive('th1')
        return
      }
      try {
        const res = await getTeacherMessagingState(sessionToken)
        const m = res?.messaging
        if (cancelled) return
        if (m && typeof m === 'object' && Array.isArray(m.threads) && m.threads.length) {
          setThreads(m.threads)
          setActive(String(m.active || m.threads[0]?.id || ''))
          return
        }
      } catch {
        /* usar plantilla local */
      }
      if (!cancelled) {
        const init = defaultThreads()
        setThreads(init)
        setActive('th1')
      }
    }
    load()
    return () => {
      cancelled = true
    }
  }, [sessionToken, t])

  useEffect(() => {
    if (!sessionToken || !threads.length) return undefined
    window.clearTimeout(saveTimerRef.current)
    saveTimerRef.current = window.setTimeout(() => {
      saveTeacherMessagingState(sessionToken, { threads, active }).catch(() => {})
    }, 500)
    return () => window.clearTimeout(saveTimerRef.current)
  }, [threads, active, sessionToken])

  const sel = threads.find((x) => String(x.id) === String(active)) || threads[0]

  function send() {
    const text = draft.trim()
    if (!text) return
    const at = new Date().toLocaleString()
    setThreads((list) =>
      list.map((th) =>
        String(th.id) !== String(active)
          ? th
          : { ...th, msgs: [...th.msgs, { me: true, text, at }], last: at },
      ),
    )
    setDraft('')
    notify(t('teacher.msgSent'))
  }

  return (
    <div className="teacher-workspace-shell">
      <div className="page-shell doc-shell teacher-module teacher-module--messages">
        <header className="teacher-module-head">
          <div>
            <h2>{t('teacher.msgPageTitle')}</h2>
            <p>{t('teacher.msgPageSub')}</p>
          </div>
          <button type="button" className="dict-home-btn" onClick={navigateHome}>
            {t('teacher.homeTeacher')}
          </button>
        </header>

        <div className="teacher-msg-grid">
          <aside className="teacher-msg-thread-list">
            {threads.map((th) => (
              <button
                key={th.id}
                type="button"
                className={`teacher-msg-thread-card${active === String(th.id) ? ' teacher-msg-thread-card--active' : ''}`}
                onClick={() => setActive(String(th.id))}
              >
                <MessageSquare size={18} strokeWidth={2} />
                <span>{th.with}</span>
              </button>
            ))}
          </aside>
          <section className="teacher-msg-chat">
            <h3>{sel?.with}</h3>
            <div className="teacher-msg-bubbles teacher-msg-thread">
              {(sel?.msgs || []).filter((m) => m.text || m.at).map((m, i) => (
                <article key={`${sel.id}-${i}`} className={`teacher-msg-bubble ${m.me ? 'teacher-msg-bubble--me' : ''}`}>
                  <p>{m.text}</p>
                  {m.at ? <time>{m.at}</time> : null}
                </article>
              ))}
            </div>
            <label className="teacher-msg-compose">
              <span className="sr-only">{t('teacher.msgComposeLbl')}</span>
              <textarea
                rows={3}
                value={draft}
                placeholder={t('teacher.msgComposePh')}
                onChange={(ev) => setDraft(ev.target.value)}
              />
              <button type="button" className="teacher-btn-solid" onClick={send}>
                <Send size={17} /> {t('teacher.msgSend')}
              </button>
            </label>
          </section>
        </div>
        <p className="teacher-module-foot">{t('teacher.msgFoot')}</p>
      </div>
    </div>
  )
}

export function TeacherResourcesPanel({ t, navigateHome, navigateTo }) {
  const cards = [
    { icon: BookOpen, key: 'resDict', tint: 'beige', onClick: () => navigateTo?.('diccionario') },
    { icon: BookMarked, key: 'resCorpus', tint: 'green', onClick: () => navigateTo?.('aprender') },
    { icon: ClipboardList, key: 'resActs', tint: 'gold', onClick: () => navigateTo?.('docente_actividades') },
  ].filter((x) => x.icon)

  return (
    <div className="teacher-workspace-shell">
      <div className="page-shell doc-shell teacher-module teacher-module--resources">
        <header className="teacher-module-head">
          <div>
            <h2>{t('teacher.resPageTitle')}</h2>
            <p>{t('teacher.resPageSub')}</p>
          </div>
          <button type="button" className="dict-home-btn" onClick={navigateHome}>
            {t('teacher.homeTeacher')}
          </button>
        </header>
        <ul className="teacher-res-grid">
          {cards.map((c) => {
            const Ico = c.icon
            return (
              <li key={c.key}>
                <button type="button" className={`teacher-res-card teacher-res-card--${c.tint}`} onClick={c.onClick}>
                  <span className="teacher-res-ring">
                    <Ico size={26} strokeWidth={2} />
                  </span>
                  <strong>{t(`teacher.${c.key}Title`)}</strong>
                  <small>{t(`teacher.${c.key}Sub`)}</small>
                </button>
              </li>
            )
          })}
        </ul>
        <p className="teacher-module-foot">{t('teacher.resFoot')}</p>
      </div>
    </div>
  )
}

export function TeacherCalendarPanel({ t, notify, navigateHome, setView }) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const [cursor, setCursor] = useState(() => new Date())
  const [activities, setActivities] = useState([])
  const [manualEvents, setManualEvents] = useState(() => seedTeacherCalEventsIfEmpty())
  const [calTitle, setCalTitle] = useState('')
  const [calDate, setCalDate] = useState('')
  const [selectedDay, setSelectedDay] = useState(null)

  useEffect(() => {
    async function load() {
      try {
        const act = await getTeacherActivities(token)
        setActivities(act.activities || [])
      } catch {
        notify(t('teacher.loadErr'))
      }
    }
    load()
  }, [notify, t, token])

  const merged = teacherDisplayActivitiesRows(activities)

  const year = cursor.getFullYear()
  const month = cursor.getMonth()
  const firstDowSun = new Date(year, month, 1).getDay()
  const monOffset = firstDowSun === 0 ? 6 : firstDowSun - 1
  const blanks = [...Array(monOffset)].map((_, i) => i)
  const daysInMonth = new Date(year, month + 1, 0).getDate()
  const days = [...Array(daysInMonth)].map((_, i) => i + 1)

  useEffect(() => {
    setSelectedDay(null)
  }, [year, month])

  const markedDays = useMemo(() => {
    const m = new Set()
    merged.forEach((row) => {
      const ms = unixMs(row.assigned_at) || unixMs(row.created_at)
      if (!ms) return
      const d = new Date(ms)
      if (d.getFullYear() === year && d.getMonth() === month) m.add(d.getDate())
    })
    manualEvents.forEach((ev) => {
      const d = new Date(ev.dueMs)
      if (d.getFullYear() === year && d.getMonth() === month) m.add(d.getDate())
    })
    return m
  }, [merged, manualEvents, year, month])

  function bump(delta) {
    setCursor(new Date(year, month + delta, 1))
  }

  const monthLbl = cursor.toLocaleString('es', { month: 'long', year: 'numeric' })

  const upcoming = useMemo(() => {
    const manItems = manualEvents.map((ev) => ({
      kind: 'manual',
      id: ev.id,
      sortMs: ev.dueMs,
      title: ev.title,
      when: new Date(ev.dueMs).toLocaleDateString('es-CO', { day: 'numeric', month: 'short', year: 'numeric' }),
    }))
    const actItems = merged
      .map((row) => {
        const sortMs = unixMs(row.assigned_at) || unixMs(row.created_at)
        const rid = row.id != null ? String(row.id) : `${String(row.title || '')}-${sortMs}`
        return {
          kind: 'act',
          id: `act-${rid}`,
          sortMs,
          title: row.title || '—',
          when: teacherDueFmt(row.created_at, row.assigned_at),
          row,
        }
      })
      .filter((x) => x.sortMs > 0)
    return [...manItems, ...actItems].sort((a, b) => a.sortMs - b.sortMs).slice(0, 14)
  }, [merged, manualEvents])

  const selectedDayDetail = useMemo(() => {
    if (selectedDay == null) return null
    const manual = manualEvents.filter((ev) => {
      const d = new Date(ev.dueMs)
      return d.getFullYear() === year && d.getMonth() === month && d.getDate() === selectedDay
    })
    const acts = merged.filter((row) => {
      const ms = unixMs(row.assigned_at) || unixMs(row.created_at)
      if (!ms) return false
      const d = new Date(ms)
      return d.getFullYear() === year && d.getMonth() === month && d.getDate() === selectedDay
    })
    return { manual, acts }
  }, [selectedDay, year, month, manualEvents, merged])

  function addManualEvent() {
    const title = calTitle.trim()
    if (!title) {
      notify(t('teacher.calNeedTitle'))
      return
    }
    if (!calDate) {
      notify(t('teacher.calNeedDate'))
      return
    }
    const parts = calDate.split('-').map((x) => Number(x))
    if (parts.length !== 3 || parts.some((n) => !Number.isFinite(n))) {
      notify(t('teacher.calNeedDate'))
      return
    }
    const [py, pm, pd] = parts
    const dueMs = new Date(py, pm - 1, pd, 12, 0, 0, 0).getTime()
    const id =
      typeof globalThis.crypto !== 'undefined' && globalThis.crypto.randomUUID
        ? globalThis.crypto.randomUUID()
        : `man-${Date.now()}`
    const entry = { id, title, dueMs }
    setManualEvents((prev) => {
      const next = [...prev, entry]
      writeTeacherCalEvents(next)
      return next
    })
    setCalTitle('')
    setCalDate('')
    notify(t('teacher.calAddedOk'))
    if (py === year && pm - 1 === month) setSelectedDay(pd)
  }

  function removeManualEvent(id) {
    setManualEvents((prev) => {
      const next = prev.filter((e) => e.id !== id)
      writeTeacherCalEvents(next)
      return next
    })
    notify(t('teacher.calRemoved'))
  }

  return (
    <div className="teacher-workspace-shell">
      <div className="page-shell doc-shell teacher-module teacher-module--calendar">
        <header className="teacher-module-head">
          <div>
            <h2>{t('teacher.calPageTitle')}</h2>
            <p>{t('teacher.calPageSub')}</p>
          </div>
          <button type="button" className="dict-home-btn" onClick={navigateHome}>
            {t('teacher.homeTeacher')}
          </button>
        </header>

        <div className="teacher-cal-shell">
          <div className="teacher-cal-controls">
            <button type="button" className="teacher-cal-nav" onClick={() => bump(-1)} aria-label={t('teacher.calPrev')}>
              ‹
            </button>
            <h3>{monthLbl}</h3>
            <button type="button" className="teacher-cal-nav" onClick={() => bump(1)} aria-label={t('teacher.calNext')}>
              ›
            </button>
          </div>
          <div className="teacher-cal-grid">
            {['L', 'M', 'X', 'J', 'V', 'S', 'D'].map((d) => (
              <div key={d} className="teacher-cal-head-cell">
                {d}
              </div>
            ))}
            {blanks.map((b) => (
              <span key={`b-${b}`} className="teacher-cal-empty" aria-hidden />
            ))}
            {days.map((dy) => {
              const cls = ['teacher-cal-day']
              if (markedDays.has(dy)) cls.push('teacher-cal-day--mark')
              if (selectedDay === dy) cls.push('teacher-cal-day--selected')
              return (
                <button
                  key={dy}
                  type="button"
                  className={cls.join(' ')}
                  onClick={() => setSelectedDay((s) => (s === dy ? null : dy))}
                >
                  {dy}
                </button>
              )
            })}
          </div>
        </div>

        <section className="teacher-cal-add" aria-labelledby="teacher-cal-add-h">
          <h4 id="teacher-cal-add-h">{t('teacher.calAddSection')}</h4>
          <p className="teacher-cal-add-hint">{t('teacher.calAddHint')}</p>
          <div className="teacher-cal-add-row">
            <label className="teacher-cal-add-field">
              <span>{t('teacher.calFieldTitle')}</span>
              <input
                type="text"
                value={calTitle}
                onChange={(e) => setCalTitle(e.target.value)}
                maxLength={200}
                autoComplete="off"
              />
            </label>
            <label className="teacher-cal-add-field teacher-cal-add-field--date">
              <span>{t('teacher.calFieldDue')}</span>
              <input type="date" value={calDate} onChange={(e) => setCalDate(e.target.value)} />
            </label>
            <button type="button" className="teacher-cal-add-submit" onClick={addManualEvent}>
              <Plus size={17} strokeWidth={2.2} /> {t('teacher.calAddBtn')}
            </button>
          </div>
        </section>

        {selectedDay != null && selectedDayDetail && (
          <section className="teacher-cal-day-detail" aria-labelledby="teacher-cal-day-h">
            <h4 id="teacher-cal-day-h">
              {t('teacher.calDayTitle')} {selectedDay}
            </h4>
            {selectedDayDetail.manual.length === 0 && selectedDayDetail.acts.length === 0 ? (
              <p className="teacher-cal-day-empty">{t('teacher.calDayEmpty')}</p>
            ) : (
              <ul className="teacher-cal-day-list">
                {selectedDayDetail.manual.map((ev) => (
                  <li key={ev.id}>
                    <span className="teacher-cal-pill">{t('teacher.calManualTag')}</span>
                    <strong>{ev.title}</strong>
                    <button
                      type="button"
                      className="teacher-cal-del"
                      onClick={() => removeManualEvent(ev.id)}
                      aria-label={t('teacher.calRemove')}
                    >
                      <Trash2 size={16} strokeWidth={2} />
                    </button>
                  </li>
                ))}
                {selectedDayDetail.acts.map((row) => (
                  <li key={row.id != null ? `dact-${row.id}` : `dact-${String(row.title)}-${selectedDay}`}>
                    <span className="teacher-cal-pill teacher-cal-pill--act">{t('teacher.calActTag')}</span>
                    <strong>{row.title || '—'}</strong>
                    <button type="button" className="teacher-cal-go-act" onClick={() => setView?.('docente_actividades')}>
                      {t('teacher.viewAllArrow')}
                    </button>
                  </li>
                ))}
              </ul>
            )}
          </section>
        )}

        <section className="teacher-cal-upcoming">
          <div className="teacher-cal-upcoming-head">
            <h4>{t('teacher.calUpcoming')}</h4>
            <button type="button" className="role-panel-link-btn" onClick={() => setView?.('docente_actividades')}>
              {t('teacher.viewAllArrow')}
            </button>
          </div>
          <ul>
            {upcoming.map((item) => (
              <li key={item.id}>
                <Calendar size={17} strokeWidth={2} />
                <span>
                  <strong>{item.title}</strong>
                  <small>
                    <span className={`teacher-cal-pill${item.kind === 'act' ? ' teacher-cal-pill--act' : ''}`}>
                      {item.kind === 'act' ? t('teacher.calActTag') : t('teacher.calManualTag')}
                    </span>
                    {t('teacher.dueLabel')}: {item.when}
                  </small>
                </span>
                {item.kind === 'manual' ? (
                  <button
                    type="button"
                    className="teacher-cal-del"
                    onClick={() => removeManualEvent(item.id)}
                    aria-label={t('teacher.calRemove')}
                  >
                    <Trash2 size={16} strokeWidth={2} />
                  </button>
                ) : (
                  <span className="teacher-cal-li-spacer" aria-hidden />
                )}
              </li>
            ))}
          </ul>
        </section>
        <p className="teacher-module-foot">{t('teacher.calFoot')}</p>
      </div>
    </div>
  )
}

function AdminPlatformLineChart({ t, usageSeries }) {
  const months =
    usageSeries?.months?.length === 5 ? usageSeries.months : ['—', '—', '—', '—', '—']
  const seriesU =
    usageSeries?.new_users?.length === 5 ? usageSeries.new_users : [0, 0, 0, 0, 0]
  const seriesS = usageSeries?.sessions?.length === 5 ? usageSeries.sessions : [0, 0, 0, 0, 0]
  const maxY = Math.max(8, Math.ceil(Math.max(...seriesU, ...seriesS, 1) * 1.15))
  const w = 360
  const h = 172
  const pad = { t: 16, r: 10, b: 34, l: 44 }
  const innerW = w - pad.l - pad.r
  const innerH = h - pad.t - pad.b
  const xAt = (i) => pad.l + (i / (months.length - 1 || 1)) * innerW
  const yAt = (v) => pad.t + innerH - (v / maxY) * innerH
  const ptsU = seriesU.map((v, i) => `${xAt(i)},${yAt(v)}`).join(' ')
  const ptsS = seriesS.map((v, i) => `${xAt(i)},${yAt(v)}`).join(' ')
  const yTicks = [0, 0.25, 0.5, 0.75, 1].map((r) => Math.round(maxY * r))

  return (
    <div className="admin-line-chart">
      <svg className="admin-line-chart-svg" viewBox={`0 0 ${w} ${h}`} aria-hidden>
        {yTicks.map((yt, idx) => {
          const yy = yAt(yt)
          return (
            <g key={`ytick-${idx}`}>
              <line x1={pad.l} x2={w - pad.r} y1={yy} y2={yy} className="admin-line-chart-grid" />
              <text x={pad.l - 6} y={yy + 4} className="admin-line-chart-y-label">
                {yt}
              </text>
            </g>
          )
        })}
        {months.map((m, i) => (
          <text key={`${m}-${i}`} x={xAt(i)} y={h - 10} className="admin-line-chart-x-label">
            {m}
          </text>
        ))}
        <polyline className="admin-line-chart-line admin-line-chart-line--sessions" fill="none" points={ptsS} />
        <polyline className="admin-line-chart-line admin-line-chart-line--users" fill="none" points={ptsU} />
      </svg>
      <div className="admin-line-chart-legend">
        <span>
          <i className="admin-line-chart-dot admin-line-chart-dot--users" /> {t('admin.legendActiveUsers')}
        </span>
        <span>
          <i className="admin-line-chart-dot admin-line-chart-dot--sessions" /> {t('admin.legendSessions')}
        </span>
      </div>
    </div>
  )
}

export function AdminGruposPanel({ t, notify, navigateTo = () => {} }) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const [tab, setTab] = useState('all')
  const [q, setQ] = useState('')
  const [groups, setGroups] = useState([])

  const reloadGroups = useCallback(async () => {
    try {
      const d = await getAdminGroups(token)
      setGroups(Array.isArray(d.groups) ? d.groups : [])
      return true
    } catch {
      notify(t('admin.loadErr'))
      setGroups([])
      return false
    }
  }, [token, notify, t])

  useEffect(() => {
    reloadGroups()
  }, [reloadGroups])

  const filtered = useMemo(() => {
    return groups.filter((g) => {
      if (tab === 'primaria' && g.level !== 'Primaria') return false
      if (tab === 'secundaria' && g.level !== 'Secundaria') return false
      const s = q.trim().toLowerCase()
      if (!s) return true
      return (
        String(g.name || '')
          .toLowerCase()
          .includes(s) || String(g.teacher || '')
          .toLowerCase()
          .includes(s)
      )
    })
  }, [tab, q, groups])

  const kpi = useMemo(() => {
    const active = groups.filter((g) => g.active !== false).length
    const teachers = new Set(groups.map((g) => g.teacher)).size
    const students = groups.reduce((a, g) => a + Number(g.students || 0), 0)
    return { active, teachers, students }
  }, [groups])

  return (
    <div className="page-shell adm-shell admin-module admin-grupos">
      <header className="page-title admin-panel-head">
        <div>
          <h2>{t('nav.admin_grupos')}</h2>
          <p>{t('admin.gruposSub')}</p>
        </div>
        <button type="button" className="admin-toolbar-secondary" onClick={() => navigateTo('docente_grupos')}>
          <UsersRound size={17} strokeWidth={2} /> {t('admin.gruposGoTeacher')}
        </button>
      </header>

      <div className="admin-kpi-row">
        <article className="admin-kpi-card">
          <Layers size={22} strokeWidth={2} aria-hidden />
          <div>
            <strong>{kpi.active}</strong>
            <span>{t('admin.gruposKpiGroups')}</span>
          </div>
        </article>
        <article className="admin-kpi-card">
          <GraduationCap size={22} strokeWidth={2} aria-hidden />
          <div>
            <strong>{kpi.teachers}</strong>
            <span>{t('admin.gruposKpiTeachers')}</span>
          </div>
        </article>
        <article className="admin-kpi-card">
          <UserCheck size={22} strokeWidth={2} aria-hidden />
          <div>
            <strong>{kpi.students}</strong>
            <span>{t('admin.gruposKpiStudents')}</span>
          </div>
        </article>
      </div>

      <div className="admin-toolbar">
        <div className="admin-toolbar-tabs" role="tablist">
          {[
            ['all', 'admin.gruposTabAll'],
            ['primaria', 'admin.gruposTabPrimary'],
            ['secundaria', 'admin.gruposTabSecondary'],
          ].map(([id, key]) => (
            <button
              key={id}
              type="button"
              role="tab"
              aria-selected={tab === id}
              className={tab === id ? 'admin-tab admin-tab--active' : 'admin-tab'}
              onClick={() => setTab(id)}
            >
              {t(key)}
            </button>
          ))}
        </div>
        <div className="admin-toolbar-search">
          <label className="admin-search-field">
            <Search size={17} strokeWidth={2} aria-hidden />
            <input type="search" value={q} onChange={(ev) => setQ(ev.target.value)} placeholder={t('admin.gruposSearchPh')} autoComplete="off" />
          </label>
          <button
            type="button"
            className="admin-filter-btn"
            onClick={async () => {
              if (await reloadGroups()) notify(t('admin.refreshOk'))
            }}
          >
            <SlidersHorizontal size={17} strokeWidth={2} aria-hidden />
            {t('admin.refreshBtn')}
          </button>
        </div>
      </div>

      <div className="admin-table-wrap">
        <table className="doc-table admin-data-table">
          <thead>
            <tr>
              <th>{t('admin.gruposColName')}</th>
              <th>{t('admin.gruposColTeacher')}</th>
              <th>{t('admin.gruposColLevel')}</th>
              <th>{t('admin.gruposColStudents')}</th>
              <th>{t('admin.gruposColStatus')}</th>
            </tr>
          </thead>
          <tbody>
            {filtered.map((g) => (
              <tr key={g.id}>
                <td>
                  <strong>{g.name}</strong>
                </td>
                <td>{g.teacher}</td>
                <td>{g.level}</td>
                <td>{g.students}</td>
                <td>
                  <span className={g.active ? 'status-pill ok' : 'status-pill warn'}>
                    {g.active ? t('admin.statusActive') : t('admin.statusInactive')}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <p className="admin-module-foot">{t('admin.gruposIntegratedFoot')}</p>
    </div>
  )
}

export function AdminAuditoriaPanel({ t, notify }) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const [tab, setTab] = useState('all')
  const [q, setQ] = useState('')
  const [rows, setRows] = useState([])
  const [kpis, setKpis] = useState(() => ({
    today: 0,
    week: 0,
    alerts_reviewed_pct: 100,
  }))

  const loadAudit = useCallback(async () => {
    try {
      const d = await getAdminAudit(token)
      const list = Array.isArray(d.rows) ? d.rows : []
      setRows(list)
      setKpis(
        d.kpis ?? {
          today: 0,
          week: 0,
          alerts_reviewed_pct: 100,
        },
      )
      return true
    } catch {
      notify(t('admin.loadErr'))
      setRows([])
      setKpis({ today: 0, week: 0, alerts_reviewed_pct: 100 })
      return false
    }
  }, [token, notify, t])

  useEffect(() => {
    loadAudit()
  }, [loadAudit])

  const filtered = useMemo(() => {
    return rows.filter((row) => {
      const act = String(row.action || '').toUpperCase()
      if (tab === 'auth') {
        if (!/(LOGIN|TOKEN|PASSWORD|AUTH|MAIL|SUPPORT|TICKET|SES)/.test(act)) return false
      } else if (tab === 'content') {
        if (!/(CMS|CONTENT)/.test(act)) return false
      } else if (tab === 'users') {
        if (!/(USER|GRADE|STUDENT|GROUP)/.test(act)) return false
      }
      const s = q.trim().toLowerCase()
      if (!s) return true
      return (
        String(row.actor || '')
          .toLowerCase()
          .includes(s) ||
        String(row.action || '')
          .toLowerCase()
          .includes(s) ||
        String(row.detail || '')
          .toLowerCase()
          .includes(s)
      )
    })
  }, [tab, q, rows])

  return (
    <div className="page-shell adm-shell admin-module admin-audit stats-dash">
      <header className="page-title admin-panel-head">
        <div>
          <h2>{t('nav.admin_auditoria')}</h2>
          <p>{t('admin.auditSub')}</p>
          <div className="woven-strip woven-strip--thin" aria-hidden />
        </div>
      </header>

      <section className="stats-grid-mini admin-stat-cards admin-audit-metrics" aria-label={t('admin.auditSub')}>
        <article className="stat-card stat-card--rich">
          <span className="stat-card-icon" aria-hidden>
            <Clock size={20} strokeWidth={2} />
          </span>
          <span>{t('admin.auditKpiToday')}</span>
          <strong>{kpis.today}</strong>
        </article>
        <article className="stat-card stat-card--rich">
          <span className="stat-card-icon" aria-hidden>
            <History size={20} strokeWidth={2} />
          </span>
          <span>{t('admin.auditKpiWeek')}</span>
          <strong>{kpis.week}</strong>
        </article>
        <article className="stat-card stat-card--rich">
          <span className="stat-card-icon" aria-hidden>
            <ShieldCheck size={20} strokeWidth={2} />
          </span>
          <span>{t('admin.auditKpiAlerts')}</span>
          <strong>{`${Math.round(Number(kpis.alerts_reviewed_pct) || 0)}%`}</strong>
        </article>
      </section>

      <section className="role-panel admin-audit-board">
        <div className="role-panel-head">
          <h3>{t('admin.auditPanelTitle')}</h3>
        </div>
        <div className="admin-audit-board-body">
          <div className="admin-toolbar">
            <div className="admin-toolbar-tabs" role="tablist">
              {[
                ['all', 'admin.auditTabAll'],
                ['auth', 'admin.auditTabAuth'],
                ['content', 'admin.auditTabContent'],
                ['users', 'admin.auditTabUsers'],
              ].map(([id, key]) => (
                <button
                  key={id}
                  type="button"
                  role="tab"
                  aria-selected={tab === id}
                  className={tab === id ? 'admin-tab admin-tab--active' : 'admin-tab'}
                  onClick={() => setTab(id)}
                >
                  {t(key)}
                </button>
              ))}
            </div>
            <div className="admin-toolbar-search">
              <label className="admin-search-field">
                <Search size={17} strokeWidth={2} aria-hidden />
                <input type="search" value={q} onChange={(ev) => setQ(ev.target.value)} placeholder={t('admin.auditSearchPh')} autoComplete="off" />
              </label>
              <button
                type="button"
                className="admin-filter-btn"
                onClick={async () => {
                  if (await loadAudit()) notify(t('admin.refreshOk'))
                }}
              >
                <SlidersHorizontal size={17} strokeWidth={2} aria-hidden />
                {t('admin.refreshBtn')}
              </button>
            </div>
          </div>

          <div className="admin-table-wrap admin-table-wrap--audit">
            <table className="doc-table admin-data-table admin-audit-table">
              <thead>
                <tr>
                  <th>{t('admin.auditColWhen')}</th>
                  <th>{t('admin.auditColActor')}</th>
                  <th>{t('admin.auditColAction')}</th>
                  <th>{t('admin.auditColDetail')}</th>
                </tr>
              </thead>
              <tbody>
                {filtered.length ? (
                  filtered.map((row) => (
                    <tr key={`${row.id}-${row.when}`}>
                      <td className="admin-nowrap">{row.when}</td>
                      <td>{row.actor}</td>
                      <td>
                        <code className="admin-code-pill">{row.action}</code>
                      </td>
                      <td>{row.detail}</td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={4} className="admin-cell-muted">
                      {t('admin.auditEmptyFilter')}
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      </section>
      <p className="admin-module-foot">{t('admin.auditFoot')}</p>
    </div>
  )
}

export function AdminCorreosPanel({ t, notify }) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const [subject, setSubject] = useState('')
  const [body, setBody] = useState('')
  const [audience, setAudience] = useState('all')
  const [history, setHistory] = useState([])
  const [mk, setMk] = useState({ sent_30d: 0, scheduled: 0, open_rate_estimate: 58 })
  const [sending, setSending] = useState(false)

  const reloadMail = useCallback(async () => {
    try {
      const d = await getAdminMailHistory(token)
      const items = d.items || []
      setHistory(items)
      if (d.kpis) setMk(d.kpis)
    } catch {
      notify(t('admin.loadErr'))
      setHistory([])
    }
  }, [token, notify, t])

  useEffect(() => {
    reloadMail()
  }, [reloadMail])

  async function sendMail() {
    if (!subject.trim()) {
      notify(t('admin.mailNeedSubject'))
      return
    }
    setSending(true)
    try {
      await postAdminMailSend(token, { subject: subject.trim(), body: (body || '').trim(), audience })
      notify(t('admin.mailSentOk'))
      setSubject('')
      setBody('')
      await reloadMail()
    } catch (e) {
      notify(e.message || t('admin.mailSendErr'))
    } finally {
      setSending(false)
    }
  }

  return (
    <div className="page-shell adm-shell admin-module admin-mail stats-dash">
      <header className="page-title admin-panel-head">
        <div>
          <h2>{t('nav.admin_correos')}</h2>
          <p>{t('admin.mailSub')}</p>
          <div className="woven-strip woven-strip--thin" aria-hidden />
        </div>
      </header>

      <section className="stats-grid-mini admin-stat-cards admin-mail-metrics" aria-label={t('admin.mailSub')}>
        <article className="stat-card stat-card--rich">
          <span className="stat-card-icon" aria-hidden>
            <Send size={20} strokeWidth={2} />
          </span>
          <span>{t('admin.mailKpiSent')}</span>
          <strong>{mk.sent_30d}</strong>
        </article>
        <article className="stat-card stat-card--rich">
          <span className="stat-card-icon" aria-hidden>
            <CalendarDays size={20} strokeWidth={2} />
          </span>
          <span>{t('admin.mailKpiScheduled')}</span>
          <strong>{mk.scheduled}</strong>
        </article>
        <article className="stat-card stat-card--rich">
          <span className="stat-card-icon" aria-hidden>
            <Inbox size={20} strokeWidth={2} />
          </span>
          <span>{t('admin.mailKpiOpen')}</span>
          <strong>{`${Math.round(Number(mk.open_rate_estimate) || 0)}%`}</strong>
        </article>
      </section>

      <div className="admin-mail-grid">
        <section className="admin-mail-compose">
          <h3>{t('admin.mailComposeTitle')}</h3>
          <label className="admin-field-block">
            <span>{t('admin.mailColSubject')}</span>
            <input type="text" value={subject} onChange={(ev) => setSubject(ev.target.value)} placeholder={t('admin.mailSubjectPh')} />
          </label>
          <label className="admin-field-block">
            <span>{t('admin.cmsBody')}</span>
            <textarea value={body} onChange={(ev) => setBody(ev.target.value)} rows={5} placeholder={t('admin.mailBodyPh')} />
          </label>
          <div className="admin-mail-audience">
            <span className="admin-mail-audience-label" id="mail-audience-label">
              {t('admin.mailColAudience')}
            </span>
            <div className="admin-segments" role="radiogroup" aria-labelledby="mail-audience-label">
              {[
                ['all', 'admin.mailAudienceAll'],
                ['teachers', 'admin.mailAudienceTeachers'],
                ['students', 'admin.mailAudienceStudents'],
              ].map(([id, labKey]) => (
                <button
                  key={id}
                  type="button"
                  role="radio"
                  aria-checked={audience === id}
                  className={audience === id ? 'admin-seg admin-seg--active' : 'admin-seg'}
                  onClick={() => setAudience(id)}
                >
                  {t(labKey)}
                </button>
              ))}
            </div>
          </div>
          <button type="button" className="admin-toolbar-primary admin-mail-send-btn" disabled={sending} onClick={() => sendMail()}>
            <Send size={17} strokeWidth={2.2} aria-hidden /> {sending ? t('admin.mailSending') : t('admin.mailSend')}
          </button>
        </section>

        <section className="admin-mail-history">
          <h3>{t('admin.mailHistoryTitle')}</h3>
          <div className="admin-table-wrap admin-table-wrap--tight">
            <table className="doc-table admin-data-table">
              <thead>
                <tr>
                  <th>{t('admin.mailColSubject')}</th>
                  <th>{t('admin.mailColAudience')}</th>
                  <th>{t('admin.mailColWhen')}</th>
                  <th>{t('admin.mailColState')}</th>
                </tr>
              </thead>
              <tbody>
                {history.length ? (
                  history.map((row) => (
                  <tr key={row.id}>
                    <td>
                      <strong>{row.subject}</strong>
                    </td>
                    <td>{row.audience}</td>
                    <td className="admin-nowrap">{row.when}</td>
                    <td>
                      <span
                        className={
                          String(row.state || '').includes('Program')
                            ? 'status-pill warn'
                            : 'status-pill ok'
                        }
                      >
                        {row.state}
                      </span>
                    </td>
                  </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={4} className="admin-cell-muted">
                      {t('admin.tableEmpty')}
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </section>
      </div>
      <p className="admin-module-foot">{t('admin.mailIntegratedFoot')}</p>
    </div>
  )
}

export function AdminSoportePanel({ t, notify }) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const [openFaq, setOpenFaq] = useState(0)
  const [ticketTopic, setTicketTopic] = useState('')
  const [ticketPriority, setTicketPriority] = useState('Media')
  const [tickets, setTickets] = useState([])
  const [sk, setSk] = useState({ open: 0, resolved_month: 0, sla_hint: '4h' })
  const [submitting, setSubmitting] = useState(false)

  const faqs = useMemo(
    () => [
      { q: 'admin.supportFaq1q', a: 'admin.supportFaq1a' },
      { q: 'admin.supportFaq2q', a: 'admin.supportFaq2a' },
      { q: 'admin.supportFaq3q', a: 'admin.supportFaq3a' },
    ],
    [],
  )

  const reloadTickets = useCallback(async () => {
    try {
      const d = await getAdminSupportTickets(token)
      const list = d.tickets || []
      setTickets(list)
      if (d.kpis) setSk(d.kpis)
    } catch {
      notify(t('admin.loadErr'))
      setTickets([])
      setSk({ open: 0, resolved_month: 0, sla_hint: '—' })
    }
  }, [token, notify, t])

  useEffect(() => {
    reloadTickets()
  }, [reloadTickets])

  async function submitTicket(ev) {
    ev.preventDefault()
    if (!ticketTopic.trim() || ticketTopic.trim().length < 4) {
      notify(t('admin.supportTicketNeedTopic'))
      return
    }
    setSubmitting(true)
    try {
      await postAdminSupportTicket(token, { topic: ticketTopic.trim(), priority: ticketPriority })
      notify(t('admin.supportTicketCreated'))
      setTicketTopic('')
      await reloadTickets()
    } catch (e) {
      notify(e.message || t('admin.supportTicketErr'))
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <div className="page-shell adm-shell admin-module admin-support">
      <header className="page-title admin-panel-head">
        <div>
          <h2>{t('nav.admin_soporte')}</h2>
          <p>{t('admin.supportSub')}</p>
        </div>
        <button
          type="button"
          className="admin-toolbar-primary"
          onClick={() => document.getElementById('admin-support-ticket-form')?.scrollIntoView({ behavior: 'smooth' })}
        >
          <CircleHelp size={17} strokeWidth={2.2} aria-hidden /> {t('admin.supportNewTicket')}
        </button>
      </header>

      <div className="admin-kpi-row">
        <article className="admin-kpi-card">
          <Mail size={22} strokeWidth={2} aria-hidden />
          <div>
            <strong>{sk.open}</strong>
            <span>{t('admin.supportKpiOpen')}</span>
          </div>
        </article>
        <article className="admin-kpi-card">
          <CheckCircle size={22} strokeWidth={2} aria-hidden />
          <div>
            <strong>{sk.resolved_month}</strong>
            <span>{t('admin.supportKpiResolved')}</span>
          </div>
        </article>
        <article className="admin-kpi-card">
          <Clock size={22} strokeWidth={2} aria-hidden />
          <div>
            <strong>{sk.sla_hint || '—'}</strong>
            <span>{t('admin.supportKpiSla')}</span>
          </div>
        </article>
      </div>

      <form id="admin-support-ticket-form" className="admin-ticket-quick-form" onSubmit={submitTicket}>
        <h3 className="admin-ticket-quick-title">{t('admin.supportQuickTicketTitle')}</h3>
        <p className="admin-ticket-quick-sub">{t('admin.supportQuickTicketSub')}</p>
        <div className="admin-ticket-quick-row">
          <label className="admin-field-block admin-ticket-field-grow">
            <span>{t('admin.supportTicketTopicLab')}</span>
            <input
              type="text"
              value={ticketTopic}
              onChange={(ev) => setTicketTopic(ev.target.value)}
              placeholder={t('admin.supportTicketTopicPh')}
              autoComplete="off"
            />
          </label>
          <label className="admin-field-block">
            <span>{t('admin.supportColPriority')}</span>
            <select value={ticketPriority} onChange={(ev) => setTicketPriority(ev.target.value)}>
              <option value="Baja">Baja</option>
              <option value="Media">Media</option>
              <option value="Alta">Alta</option>
            </select>
          </label>
          <button type="submit" className="admin-toolbar-primary admin-ticket-submit" disabled={submitting}>
            {submitting ? t('admin.supportTicketSending') : t('admin.supportSubmitTicket')}
          </button>
        </div>
      </form>

      <div className="admin-support-grid">
        <section className="admin-faq-card">
          <h3>{t('admin.supportFaqTitle')}</h3>
          <ul className="admin-faq-list">
            {faqs.map((item, i) => (
              <li key={item.q} className="admin-faq-item">
                <button type="button" className="admin-faq-q" onClick={() => setOpenFaq(openFaq === i ? -1 : i)} aria-expanded={openFaq === i}>
                  <span>{t(item.q)}</span>
                  <span className="admin-faq-chevron">{openFaq === i ? '−' : '+'}</span>
                </button>
                {openFaq === i ? <p className="admin-faq-a">{t(item.a)}</p> : null}
              </li>
            ))}
          </ul>
        </section>

        <section className="admin-tickets-card">
          <h3>{t('admin.supportTicketsTitle')}</h3>
          <div className="admin-table-wrap admin-table-wrap--tight">
            <table className="doc-table admin-data-table">
              <thead>
                <tr>
                  <th>{t('admin.supportColId')}</th>
                  <th>{t('admin.supportColTopic')}</th>
                  <th>{t('admin.supportColFrom')}</th>
                  <th>{t('admin.supportColPriority')}</th>
                  <th>{t('admin.supportColState')}</th>
                </tr>
              </thead>
              <tbody>
                {tickets.length ? (
                  tickets.map((row) => (
                  <tr key={row.id}>
                    <td>
                      <code className="admin-code-pill">{row.id}</code>
                    </td>
                    <td>{row.topic}</td>
                    <td className="admin-cell-muted">{row.from}</td>
                    <td>{row.priority}</td>
                    <td>
                      <span
                        className={
                          row.state === 'Resuelto'
                            ? 'status-pill ok'
                            : row.state === 'En progreso'
                              ? 'status-pill warn'
                              : 'status-pill warn'
                        }
                      >
                        {row.state}
                      </span>
                    </td>
                  </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={5} className="admin-cell-muted">
                      {t('admin.tableEmpty')}
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </section>
      </div>
      <p className="admin-module-foot">{t('admin.supportIntegratedFoot')}</p>
    </div>
  )
}

export function AdminDashboard({ t, notify, profile, setView }) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const [users, setUsers] = useState([])
  const [cms, setCms] = useState([])
  const [dash, setDash] = useState(null)
  const [auditFeed, setAuditFeed] = useState([])

  useEffect(() => {
    async function load() {
      try {
        const [u, c, d, a] = await Promise.all([
          getAdminUsers(token),
          getAdminCms(token),
          getAdminStatsDash(token),
          getAdminAudit(token),
        ])
        setUsers(u.users || [])
        setCms(c.cms_items || [])
        setDash(d)
        setAuditFeed(Array.isArray(a.rows) ? a.rows : [])
      } catch {
        notify(t('admin.loadErr'))
      }
    }
    load()
  }, [notify, t, token])

  const platform = dash?.platform || {}
  const totalUsers = platform.usuarios_registrados ?? 0
  const teachers = platform.docentes ?? 0
  const students = platform.estudiantes ?? 0
  const corpusEntries = dash?.corpus?.entradas ?? 0
  const cmsCount = dash?.corpus?.cms_items_count ?? cms.length
  const usageSeries = dash?.usage_series

  function auditIconForAction(action) {
    const a = String(action || '').toUpperCase()
    if (a.includes('USER') || a.includes('GRADE')) return UserPlus
    if (a.includes('CMS') || a.includes('CONTENT')) return FileEdit
    if (a.includes('MAIL')) return Mail
    return UsersRound
  }

  const dashUsersPreview = users.slice(0, 5)
  const dashCmsPreview = cms.slice(0, 4)

  return (
    <div className="role-dashboard role-dashboard--admin">
      <section className="role-hero role-hero--admin admin-dash-hero">
        <div>
          <span className="role-eyebrow">
            <ShieldCheck size={16} /> {t('admin.eyebrowAdmin')}
          </span>
          <h2>{t('nav.adminDashboard')}</h2>
          <p>{t('admin.heroLeadAdmin')}</p>
        </div>
        <button type="button" onClick={() => setView('admin_usuarios')}>
          <Plus size={17} /> {t('admin.newUser')}
        </button>
      </section>

      <section className="admin-dash-intro">
        <h3 className="admin-dash-intro-title">{t('nav.adminDashboard')}</h3>
        <p className="admin-dash-intro-sub">{t('admin.dashboardSub')}</p>
      </section>

      <section className="role-metrics admin-dash-metrics">
        <RoleMetric icon={UsersRound} label={t('admin.metricUsersReg')} value={totalUsers} tone="rose" />
        <RoleMetric icon={GraduationCap} label={t('admin.metricTeachersAct')} value={teachers} tone="purple" />
        <RoleMetric icon={UserCheck} label={t('admin.metricStudentsAct')} value={students} tone="green" />
        <RoleMetric icon={Database} label={t('admin.metricCorpusRes')} value={corpusEntries} tone="gold" />
        <RoleMetric icon={FileText} label={t('admin.metricCmsItems')} value={cmsCount} tone="green" />
      </section>

      <div className="admin-dash-split">
        <section className="role-panel admin-activity-panel">
          <div className="role-panel-head">
            <h3>{t('admin.activityTitle')}</h3>
          </div>
          <ul className="admin-activity-feed">
            {auditFeed.length ? (
              auditFeed.slice(0, 5).map((row) => {
                const RowIcon = auditIconForAction(row.action)
                return (
                  <li key={`${row.id}-${row.when}`} className="admin-activity-row">
                    <span className="admin-activity-icon">
                      <RowIcon size={18} strokeWidth={2} />
                    </span>
                    <div className="admin-activity-body">
                      <p>
                        <strong>{row.action}</strong> · {row.actor}
                      </p>
                      <p className="admin-cell-muted">{row.detail}</p>
                      <time>{row.when}</time>
                    </div>
                  </li>
                )
              })
            ) : (
              <li className="admin-activity-row">
                <span className="admin-activity-icon">
                  <BookOpen size={18} strokeWidth={2} />
                </span>
                <div className="admin-activity-body">
                  <p>{t('admin.auditEmptyFilter')}</p>
                </div>
              </li>
            )}
          </ul>
          <button type="button" className="admin-activity-view-all" onClick={() => setView('admin_auditoria')}>
            {t('admin.viewAll')} →
          </button>
        </section>

        <section className="role-panel admin-chart-panel">
          <div className="role-panel-head">
            <h3>{t('admin.platformUsageTitle')}</h3>
          </div>
          <AdminPlatformLineChart t={t} usageSeries={usageSeries} />
        </section>
      </div>

      <div className="admin-dash-quick-links">
        <RolePanel
          title={t('nav.admin_usuarios')}
          action={
            <button type="button" onClick={() => setView('admin_usuarios')}>
              {t('admin.viewAll')}
            </button>
          }
        >
          <div className="role-table-wrap">
            <table className="role-mini-table">
              <thead>
                <tr>
                  <th>{t('settings.nameLabel')}</th>
                  <th>{t('login.roleBadge')}</th>
                  <th>{t('admin.activeCol')}</th>
                </tr>
              </thead>
              <tbody>
                {dashUsersPreview.length ? (
                  dashUsersPreview.map((user) => (
                    <tr key={user.id}>
                      <td>
                        <strong>{user.display_name}</strong>
                        <small>{user.email}</small>
                      </td>
                      <td>{labelSlug(user.role)}</td>
                      <td>
                        <span className={user.active ? 'status-pill ok' : 'status-pill'}>
                          {user.active ? t('admin.yes') : t('admin.no')}
                        </span>
                      </td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={3} className="admin-cell-muted">
                      {t('admin.noUsers')}
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </RolePanel>

        <RolePanel
          title={t('admin.cmsTitle')}
          action={
            <button type="button" onClick={() => setView('admin_contenido')}>
              {t('admin.newContent')}
            </button>
          }
        >
          <div className="role-task-list">
            {dashCmsPreview.length ? (
              dashCmsPreview.map((item) => (
                <article key={item.id} className="role-task">
                  <span>
                    <FileText size={15} />
                  </span>
                  <div>
                    <strong>{item.title}</strong>
                    <small>
                      {labelSlug(item.kind)} ·{' '}
                      {String(item.status || '').toLowerCase() === 'draft' ? t('admin.statusDraft') : t('admin.statusPublished')}
                    </small>
                  </div>
                </article>
              ))
            ) : (
              <p className="doc-empty-visual">{t('admin.cmsEmpty')}</p>
            )}
          </div>
        </RolePanel>
      </div>
    </div>
  )
}

export function StudentActivitiesRoute({
  t,
  notify,
  navigateHome,
  navigateTo = () => {},
  category,
  categories,
  setCategory,
  surface = 'activities',
  practiceFromLearn = null,
  onConsumePracticeFromLearn,
}) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const isPractice = surface === 'practice'
  const DIFFS = ['facil', 'intermedio', 'avanzado']
  const MODES = [
    { id: 'quiz', labelKey: 'act.modeQuiz', icon: ListChecks },
    { id: 'completar', labelKey: 'act.modeSentence', icon: BookOpen },
    { id: 'imagen', labelKey: 'act.modeImg', icon: ImageIcon },
  ]
  const [difficulty, setDifficulty] = useState('intermedio')
  const [mode, setMode] = useState('quiz')
  const [step, setStep] = useState('hub')
  const [questions, setQuestions] = useState([])
  const [idx, setIdx] = useState(0)
  const [chosen, setChosen] = useState(null)
  const [revealed, setRevealed] = useState(false)
  const [seconds, setSeconds] = useState(300)
  const [studentGrade, setStudentGrade] = useState(null)
  const [studentGroups, setStudentGroups] = useState([])
  const [assignedActivities, setAssignedActivities] = useState([])
  const [activityCatalog, setActivityCatalog] = useState([])
  const [practiceTab, setPracticeTab] = useState('vocabulario')
  const [corpusExploreTab, setCorpusExploreTab] = useState(null)
  const timerRef = useRef(null)
  const timedOutRef = useRef(false)
  const learnPracticeBootHandledRef = useRef(null)
  const practiceSessionRef = useRef({ tabId: '', category: '' })

  const assignedIdSet = useMemo(() => new Set(assignedActivities.map((a) => Number(a.id))), [assignedActivities])
  const sortedActivityCatalog = useMemo(() => {
    const list = Array.isArray(activityCatalog) ? [...activityCatalog] : []
    list.sort((a, b) => {
      const ar = assignedIdSet.has(Number(a.id)) ? 0 : 1
      const br = assignedIdSet.has(Number(b.id)) ? 0 : 1
      if (ar !== br) return ar - br
      return (Number(b.created_at) || 0) - (Number(a.created_at) || 0)
    })
    return list
  }, [activityCatalog, assignedIdSet])

  const catFp = useMemo(() => (Array.isArray(categories) ? categories.join('\0') : ''), [categories])
  const exploreCats = useMemo(() => buildPracticeExploreCategories(categories), [catFp])

  useEffect(() => {
    async function loadAssigned() {
      if (!token) return
      try {
        const [school, acts] = await Promise.all([getStudentProfileSchool(token), getStudentActivities(token)])
        setStudentGrade(school?.grade ?? null)
        setStudentGroups(Array.isArray(school?.groups) ? school.groups : [])
        setAssignedActivities(Array.isArray(acts?.activities) ? acts.activities : [])
        setActivityCatalog(Array.isArray(acts?.catalog) ? acts.catalog : [])
      } catch {
        notify(t('student.activitiesLoadErr'))
      }
    }
    loadAssigned()
  }, [token])

  const finalize = useCallback(
    (timedOut) => {
      window.clearInterval(timerRef.current)
      if (timedOut) timedOutRef.current = true
      setStep('score')
      if (timedOut) notify(t('act.timeOut'))
    },
    [notify, t],
  )

  /**
   * @param {null | { category?: string; difficulty?: string; mode?: string }} preset
   *        Si viene de una actividad asignada, categoría / dificultad / modo del docente.
   * @param {string | null} practiceTabOverride — id de pestaña (p. ej. 'gramatica') al iniciar desde tarjetas del corpus.
   */
  async function loadFlow(preset = null, practiceTabOverride = null) {
    if (practiceTabOverride != null && isPractice) {
      setPracticeTab(practiceTabOverride)
    }
    setStep('quiz')
    setIdx(0)
    setChosen(null)
    setRevealed(false)
    timedOutRef.current = false
    const effectivePracticeTab = practiceTabOverride != null ? practiceTabOverride : practiceTab
    const resolvedMode = isPractice
      ? preset?.mode != null
        ? normalizeActivityMode(preset.mode)
        : (PRACTICE_TAB_DEF.find((x) => x.id === effectivePracticeTab)?.mode ?? 'quiz')
      : mode
    const resolvedDiff = isPractice
      ? preset?.difficulty != null
        ? normalizeDifficulty(preset.difficulty)
        : 'intermedio'
      : difficulty
    const limit = isPractice ? 10 : 6
    const catPrimary = String(preset?.category || category || 'comida').trim() || 'comida'
    if (preset?.category && setCategory) setCategory(String(preset.category).trim())

    const catPool = []
    const pushCat = (c) => {
      const s = String(c || '').trim()
      if (s && !catPool.includes(s)) catPool.push(s)
    }
    pushCat(catPrimary)
    if (Array.isArray(categories)) {
      for (const c of categories) pushCat(c)
    }
    for (const c of CORPUS_PRACTICE_CATEGORY_FALLBACKS) pushCat(c)

    const tryFetch = async (catList, modeTry, diffTry) => {
      let lastErr = ''
      for (const catTry of catList) {
        try {
          const data = await getActivityAdv(catTry, limit, diffTry, modeTry)
          const got = data.questions || []
          if (got.length) {
            return {
              qs: got.map((item) => ({ ...item })),
              catWin: catTry,
              diffWin: diffTry,
              lastErr: '',
            }
          }
        } catch (e) {
          lastErr = e?.message || String(e)
        }
      }
      return { qs: [], catWin: null, diffWin: diffTry, lastErr }
    }

    try {
      let modeAdaptHintSent = false
      let { qs, catWin, diffWin, lastErr } = await tryFetch(catPool, resolvedMode, resolvedDiff)

      if (!qs.length && isPractice) {
        const relaxModes =
          resolvedMode === 'imagen' ? ['quiz', 'completar'] : resolvedMode === 'completar' ? ['quiz'] : []
        for (const m of relaxModes) {
          const r = await tryFetch(catPool, m, resolvedDiff)
          if (r.qs.length) {
            ;({ qs, catWin, diffWin, lastErr } = r)
            notify(t('practice.modeAdaptedHint'))
            modeAdaptHintSent = true
            break
          }
        }
      }

      if (!qs.length && isPractice && resolvedDiff !== 'facil') {
        const r = await tryFetch(catPool, resolvedMode, 'facil')
        if (r.qs.length) {
          ;({ qs, catWin, diffWin, lastErr } = r)
        }
      }

      if (!qs.length && isPractice) {
        for (const m of ['quiz', 'completar', 'imagen']) {
          const r = await tryFetch(catPool, m, 'facil')
          if (r.qs.length) {
            ;({ qs, catWin, diffWin, lastErr } = r)
            if (!modeAdaptHintSent && m !== resolvedMode) {
              notify(t('practice.modeAdaptedHint'))
            }
            break
          }
        }
      }

      setQuestions(qs)
      if (!qs.length) {
        notify(lastErr || t('practice.empty'))
        setStep('hub')
        return
      }
      if (!preset?.category && setCategory && catWin && catWin !== catPrimary) {
        setCategory(catWin)
      }
      if (isPractice) {
        practiceSessionRef.current = {
          tabId: effectivePracticeTab,
          category: String(catWin || catPrimary).trim() || 'comida',
        }
      }
      const base = diffWin === 'facil' ? 420 : diffWin === 'avanzado' ? 180 : 300
      setSeconds(base)
    } catch (e) {
      notify(e.message)
      setStep('hub')
    }
  }

  useEffect(() => {
    if (!isPractice || !practiceFromLearn?._bootKey) return
    if (learnPracticeBootHandledRef.current === practiceFromLearn._bootKey) return
    learnPracticeBootHandledRef.current = practiceFromLearn._bootKey
    const cat = String(practiceFromLearn.category || '').trim() || 'comida'
    const tabId = practiceFromLearn.tabId || 'vocabulario'
    if (setCategory) setCategory(cat)
    onConsumePracticeFromLearn?.()
    void loadFlow({ category: cat }, tabId)
    // eslint-disable-next-line react-hooks/exhaustive-deps -- arranque único por _bootKey; loadFlow usa preset explícito
  }, [isPractice, practiceFromLearn, onConsumePracticeFromLearn, setCategory])

  function startActivityFromCatalog(activity) {
    const cat = String(activity?.category ?? category ?? 'comida').trim() || 'comida'
    if (activity?.category && setCategory) setCategory(cat)
    setDifficulty(normalizeDifficulty(activity?.difficulty))
    setMode(normalizeActivityMode(activity?.mode))
    loadFlow({
      category: cat,
      difficulty: activity?.difficulty,
      mode: activity?.mode,
    })
  }

  useEffect(() => {
    if (step !== 'quiz') {
      window.clearInterval(timerRef.current)
      return undefined
    }
    timerRef.current = window.setInterval(() => {
      setSeconds((s) => {
        if (s <= 1) {
          window.clearInterval(timerRef.current)
          finalize(true)
          return 0
        }
        return s - 1
      })
    }, 1000)
    return () => window.clearInterval(timerRef.current)
  }, [step, finalize])

  const q = questions[idx]

  function pick(option) {
    if (revealed || !q) return
    setChosen(option)
    setRevealed(true)
    setQuestions((items) => items.map((it, i) => (i === idx ? { ...it, _picked: option } : it)))
  }

  function nextQuestion() {
    if (idx + 1 >= questions.length) {
      if (isPractice && practiceSessionRef.current.tabId) {
        markPracticeProgress(
          practiceSessionRef.current.tabId,
          practiceSessionRef.current.category,
          1,
          false,
        )
      }
      finalize(false)
    } else {
      if (isPractice && practiceSessionRef.current.tabId) {
        markPracticeProgress(
          practiceSessionRef.current.tabId,
          practiceSessionRef.current.category,
          (idx + 1) / Math.max(1, questions.length),
          false,
        )
      }
      setIdx(idx + 1)
      setChosen(null)
      setRevealed(false)
    }
  }

  const tabMeta =
    PRACTICE_TAB_DEF.find((x) => x.id === practiceTab) ??
    PRACTICE_TAB_DEF[0]

  if (!isPractice) {
    return (
      <div className="page-shell act-shell">
        <header className="page-title dict-head">
          <div>
            <h2>{t('act.pageTitle')}</h2>
            <p>{t('act.pageSub')}</p>
          </div>
          <button type="button" className="dict-home-btn" onClick={navigateHome}>
            {t('student.homeBtn')}
          </button>
        </header>
        {step === 'hub' && (
          <div className="act-hub">
            <section className="act-hub-hero">
              <div>
                <span className="act-hub-eyebrow">
                  <Activity size={16} /> Ruta de aprendizaje
                </span>
                <h3>Aprende, practica y refuerza en una sola sección</h3>
                <p>Selecciona una categoría, ajusta el nivel y elige el tipo de ejercicio. Así evitas pantallas repetidas y mantienes el proceso ordenado.</p>
                {studentGrade ? (
                  <p className="act-grade-badge">
                    Tu grado: <strong>{studentGrade.name}</strong> ({studentGrade.level})
                  </p>
                ) : null}
              </div>
            </section>

            {sortedActivityCatalog.length ? (
              <section className="act-hub-card act-hub-card--assigned">
                <div className="act-card-head">
                  <h3>{t('student.activityCatalogTitle')}</h3>
                  <small>{t('student.activityCatalogSub')}</small>
                </div>
                <div className="act-assigned-list">
                  {sortedActivityCatalog.map((a) => (
                    <article key={a.id} className="act-assigned-item">
                      <div className="act-assigned-item-head">
                        <strong>{a.title}</strong>
                        {assignedIdSet.has(Number(a.id)) ? (
                          <span className="status-pill ok">{t('student.activityAssignedBadge')}</span>
                        ) : null}
                      </div>
                      <small>
                        {a.category} · {a.difficulty} · {a.mode}
                      </small>
                      {a.description ? <p>{a.description}</p> : null}
                      <button type="button" className="practice-assignment-go" onClick={() => startActivityFromCatalog(a)}>
                        {t('act.start')}
                      </button>
                    </article>
                  ))}
                </div>
              </section>
            ) : null}

            <label className="act-cat act-hub-card act-hub-card--cat">
              <span>{t('corpus.categoriesTitle')}</span>
              <select value={category} onChange={(ev) => setCategory(ev.target.value)}>
                {(categories?.length ? categories : ['comida']).map((c) => (
                  <option key={c} value={c}>
                    {titleLabel(c)}
                  </option>
                ))}
              </select>
            </label>

            <section className="act-hub-card">
              <div className="act-card-head">
                <h3>{t('act.difficulty')}</h3>
                <small>Escoge el reto adecuado para tu avance</small>
              </div>
              <div className="pill-row">
                {DIFFS.map((d) => (
                  <button
                    key={d}
                    type="button"
                    className={difficulty === d ? 'pill-active' : ''}
                    onClick={() => setDifficulty(d)}
                  >
                    {t(`act.${d}`)}
                  </button>
                ))}
              </div>
            </section>
            <section className="act-hub-card">
              <div className="act-card-head">
                <h3>{t('act.typePick')}</h3>
                <small>Unifica lecciones, practica y evaluación</small>
              </div>
              <div className="mode-grid">
                {MODES.map((m) => (
                  <button
                    key={m.id}
                    type="button"
                    className={mode === m.id ? 'mode-tile active' : 'mode-tile'}
                    onClick={() => setMode(m.id)}
                  >
                    <m.icon size={22} strokeWidth={1.9} />
                    <span>{t(m.labelKey)}</span>
                  </button>
                ))}
              </div>
            </section>
            <button type="button" className="act-empezar" onClick={loadFlow}>
              {t('act.start')}
            </button>
          </div>
        )}
        {step === 'quiz' && q && (
          <div className="act-quiz">
            <div className="quiz-timer">
              <span>
                {Math.floor(seconds / 60)}:{String(seconds % 60).padStart(2, '0')}
              </span>
              <button type="button" className="quiz-finish" onClick={() => finalize(false)}>
                {t('act.finish')}
              </button>
            </div>
            <p className="quiz-meta">{t('act.qOf', { n: idx + 1, t: questions.length })}</p>
            {q.type === 'imagen' && q.image_url ? (
              <div className="quiz-img-row">
                <ActivityQuestionImage
                  src={q.image_url}
                  alt={q.espanol ? `Ilustración: ${q.espanol}` : ''}
                  className="quiz-img"
                />
              </div>
            ) : q.type === 'imagen' ? (
              <p className="quiz-img-fallback">{t('practice.imageUnavailable')}</p>
            ) : null}
            <h3>{q.prompt}</h3>
            <div
              className={[
                'answers-grid',
                'act-answers',
                q.option_images && Object.keys(q.option_images).length ? 'act-answers--visual' : '',
              ]
                .filter(Boolean)
                .join(' ')}
            >
              {(q.options || []).map((opt, optIdx) => {
                const optImg = q.option_images?.[opt]
                return (
                  <button
                    type="button"
                    key={`${q.id}-opt-${optIdx}`}
                    disabled={revealed}
                    className={[
                      'answer-chip',
                      optImg ? 'answer-chip--visual' : '',
                      revealed && activityStringsEqual(opt, q.answer) ? 'correct' : '',
                      revealed &&
                      chosen === opt &&
                      !activityStringsEqual(opt, q.answer)
                        ? 'incorrect'
                        : '',
                    ]
                      .filter(Boolean)
                      .join(' ')}
                    onClick={() => pick(opt)}
                  >
                    {optImg ? (
                      <ActivityOptionVisual
                        optionText={opt}
                        optionImages={q.option_images}
                        category={q.categoria || category}
                        imgClassName="act-opt-thumb"
                        iconClassName="act-opt-icon-svg"
                      />
                    ) : null}
                    <span className="answer-chip-label">{opt}</span>
                  </button>
                )
              })}
            </div>
            {revealed ? (
              <div className="quiz-feedback-msg">
                {activityStringsEqual(chosen, q.answer) ? (
                  <>
                    <CheckCircle size={18} /> {t('act.good')}
                  </>
                ) : (
                  <>
                    <XCircle size={18} /> {t('act.bad')} <strong>{q.answer}</strong>
                  </>
                )}
              </div>
            ) : null}
            <div className="quiz-actions">
              <button type="button" onClick={nextQuestion} disabled={!revealed}>
                {idx + 1 >= questions.length ? t('act.finish') : t('act.next')}
              </button>
            </div>
          </div>
        )}
        {step === 'score' && (
          <div className="score-card">
            <h3>{t('act.scoreTitle')}</h3>
            <p className="score-big">
              {questions.filter((iq) => activityStringsEqual(iq._picked, iq.answer)).length}/{questions.length}
            </p>
            <details>
              <summary>{t('act.breakdown')}</summary>
              <ul>
                {questions.map((iq) => (
                  <li
                    key={iq.id}
                    className={activityStringsEqual(iq._picked, iq.answer) ? 'score-ok' : 'score-bad'}
                  >
                    {iq.prompt}: <strong>{iq.answer}</strong>
                  </li>
                ))}
              </ul>
            </details>
            <button type="button" className="act-other" onClick={() => setStep('hub')}>
              {t('act.another')}
            </button>
          </div>
        )}
      </div>
    )
  }

  function startPracticeFromAssignment(activity) {
    setCorpusExploreTab(null)
    const cat = String(activity?.category ?? category ?? 'comida').trim() || 'comida'
    if (activity?.category && setCategory) setCategory(cat)
    const tabId = practiceTabFromServerMode(activity?.mode)
    loadFlow(
      {
        category: cat,
        difficulty: activity?.difficulty,
        mode: activity?.mode,
      },
      tabId,
    )
  }

  function handlePracticeScoreToHub() {
    const { tabId, category } = practiceSessionRef.current
    if (isPractice && tabId && category) {
      markPracticeProgress(tabId, category, 1, true)
    }
    setStep('hub')
  }

  function openCorpusExplore(tabId) {
    setCorpusExploreTab(tabId)
    setPracticeTab(tabId)
  }

  const practiceCue = q ? spotlightWord(q) : ''
  const practiceQKey = q ? practiceQuestionCopyKey(practiceTab, q.type) : 'practice.qPickNasa'
  const practiceProgressRatio = questions.length ? (idx + 1) / questions.length : 0

  return (
    <div className="page-shell practice-mock-shell">
      <div className="practice-mock-grid">
        <div className="practice-mock-main">
          <header className="learn-mock-heading practice-mock-hero">
            <div className="learn-mock-heading-copy">
              <h2 className="learn-mock-title">
                {t('practice.pageTitle')}
                <span className="learn-mock-title-accent" aria-hidden />
              </h2>
            </div>
            <div className="learn-mock-art" aria-hidden>
              <img src={learnWelcomeIllustration} alt="" className="learn-mock-art-img" />
            </div>
          </header>

          <div className="woven-strip woven-strip--thin practice-mock-strip" aria-hidden />

          {step === 'hub' && (
            <>
              <div className="practice-grade-banner">
                <div className="practice-grade-banner-icon" aria-hidden>
                  <GraduationCap size={28} strokeWidth={2} />
                </div>
                <div className="practice-grade-banner-copy">
                  <p className="practice-grade-banner-label">{t('practice.yourGradeHeading')}</p>
                  {studentGrade ? (
                    <p className="practice-grade-banner-value">
                      {t('practice.yourGradeLine', {
                        name: studentGrade.name,
                        level: studentGrade.level ?? '—',
                      })}
                    </p>
                  ) : (
                    <p className="practice-grade-banner-missing">{t('practice.noGradeHint')}</p>
                  )}
                  {studentGroups.length ? (
                    <p className="practice-grade-banner-groups">
                      {t('practice.yourGroupsLine', {
                        list: studentGroups
                          .map((g) => g?.name ?? g?.id ?? '')
                          .filter(Boolean)
                          .join(', '),
                      })}
                    </p>
                  ) : null}
                </div>
              </div>

              <section className="practice-grade-activities-card" aria-label={t('practice.assignmentsHeading')}>
                <div className="practice-grade-activities-head">
                  <h3>{t('practice.assignmentsHeading')}</h3>
                  <p className="practice-grade-activities-sub">{t('practice.assignmentsSub')}</p>
                </div>
                {sortedActivityCatalog.length ? (
                  <ul className="practice-assignment-rows">
                    {sortedActivityCatalog.slice(0, 60).map((a) => (
                      <li key={a.id} className="practice-assignment-row">
                        <div className="practice-assignment-body">
                          <strong className="practice-assignment-title">{a.title}</strong>
                          {assignedIdSet.has(Number(a.id)) ? (
                            <span className="status-pill ok practice-assignment-badge">
                              {t('student.activityAssignedBadge')}
                            </span>
                          ) : null}
                          {a.description ? <p className="practice-assignment-desc">{a.description}</p> : null}
                          <div className="practice-assignment-meta">
                            <span>{titleLabel(String(a.category || '').trim() || category)}</span>
                            <span>{t(`act.${normalizeDifficulty(a.difficulty)}`)}</span>
                            <span>{activityModeLabel(t, a.mode)}</span>
                          </div>
                        </div>
                        <button
                          type="button"
                          className="practice-assignment-go"
                          onClick={() => startPracticeFromAssignment(a)}
                        >
                          {t('practice.startAssignment')}
                        </button>
                      </li>
                    ))}
                  </ul>
                ) : (
                  <div className="practice-assignments-fallback">
                    <p className="practice-assignments-empty">{t('practice.noAssignmentsShort')}</p>
                    <div className="practice-suggested-corpus" aria-labelledby="practice-suggested-title">
                      <h4 id="practice-suggested-title" className="practice-suggested-title">
                        {t('practice.suggestedCorpusBlockTitle')}
                      </h4>
                      <p className="practice-suggested-sub">{t('practice.suggestedCorpusBlockSub')}</p>
                      <ul className="practice-assignment-rows practice-suggested-rows">
                        {PRACTICE_TAB_DEF.map((tab) => {
                          const TabIcon = PRACTICE_TAB_ICONS[tab.id] || BookOpen
                          return (
                            <li key={tab.id} className="practice-assignment-row practice-assignment-row--suggested">
                              <div className="practice-assignment-body">
                                <div className="practice-suggested-row-head">
                                  <span className="practice-suggested-row-ico" aria-hidden>
                                    <TabIcon size={20} strokeWidth={2} />
                                  </span>
                                  <strong className="practice-assignment-title">{t(tab.labelKey)}</strong>
                                  <span className="practice-suggested-badge">{t('practice.corpusBadge')}</span>
                                </div>
                                <p className="practice-assignment-desc practice-suggested-desc">
                                  {t('practice.suggestedRowExplore')}
                                </p>
                                <div className="practice-assignment-meta">
                                  <span>{titleLabel(String(category || '').trim() || 'comida')}</span>
                                  <span>{t('act.intermedio')}</span>
                                  <span>{activityModeLabel(t, tab.mode)}</span>
                                </div>
                              </div>
                              <button
                                type="button"
                                className="practice-assignment-go"
                                onClick={() => openCorpusExplore(tab.id)}
                              >
                                {t('practice.corpusOpenList')}
                              </button>
                            </li>
                          )
                        })}
                      </ul>
                    </div>
                  </div>
                )}
              </section>

              <section
                className={`practice-free-panel ${corpusExploreTab ? 'practice-free-panel--explore' : 'practice-free-panel--corpus'}`}
                aria-labelledby={corpusExploreTab ? 'practice-explore-title' : 'practice-free-title'}
              >
                {corpusExploreTab ? (
                  <>
                    <div className="practice-explore-toolbar">
                      <button
                        type="button"
                        className="practice-explore-back"
                        onClick={() => setCorpusExploreTab(null)}
                      >
                        <ArrowLeft size={18} strokeWidth={2} aria-hidden /> {t('practice.exploreBack')}
                      </button>
                    </div>
                    <div className="practice-free-panel-head practice-explore-head">
                      <div className="practice-free-panel-icon" aria-hidden>
                        {(() => {
                          const HeadIco = PRACTICE_TAB_ICONS[corpusExploreTab] || BookOpen
                          return <HeadIco size={28} strokeWidth={2} />
                        })()}
                      </div>
                      <div className="practice-free-panel-intro">
                        <h3 id="practice-explore-title" className="practice-free-panel-title">
                          {t('practice.exploreTitle', {
                            mode: t(PRACTICE_TAB_DEF.find((x) => x.id === corpusExploreTab)?.labelKey || 'practice.tabVocab'),
                          })}
                        </h3>
                        <p className="practice-free-panel-sub">{t('practice.exploreSub')}</p>
                      </div>
                    </div>
                    <ul className="practice-explore-list">
                      {exploreCats.map((catSlug) => {
                        const prog = getPracticeRowProgress(corpusExploreTab, catSlug)
                        const RowIcon = PRACTICE_TAB_ICONS[corpusExploreTab] || BookOpen
                        const statusKey = prog.done ? 'done' : prog.pct > 0 ? 'doing' : 'todo'
                        return (
                          <li key={`${corpusExploreTab}-${catSlug}`} className="practice-explore-item">
                            <span className="practice-explore-item-icon" aria-hidden>
                              <RowIcon size={22} strokeWidth={2} />
                            </span>
                            <div className="practice-explore-item-main">
                              <div className="practice-explore-item-top">
                                <strong className="practice-explore-item-title">{titleLabel(catSlug)}</strong>
                                <span className={`practice-explore-status practice-explore-status--${statusKey}`}>
                                  {prog.done
                                    ? t('practice.statusDone')
                                    : prog.pct > 0
                                      ? t('practice.statusProgress')
                                      : t('practice.statusTodo')}
                                </span>
                              </div>
                              <div className="practice-explore-bar" aria-hidden>
                                <span className="practice-explore-bar-fill" style={{ width: `${prog.pct}%` }} />
                              </div>
                              <p className="practice-explore-pct">{prog.pct}%</p>
                            </div>
                            <button
                              type="button"
                              className="practice-explore-go"
                              onClick={() => void loadFlow({ category: catSlug }, corpusExploreTab)}
                            >
                              {t('practice.corpusStart')}
                            </button>
                          </li>
                        )
                      })}
                    </ul>
                  </>
                ) : (
                  <>
                    <div className="practice-free-panel-head">
                      <div className="practice-free-panel-icon" aria-hidden>
                        <Target size={26} strokeWidth={2} />
                      </div>
                      <div className="practice-free-panel-intro">
                        <h3 id="practice-free-title" className="practice-free-panel-title">
                          {t('practice.corpusModesTitle')}
                        </h3>
                        <p className="practice-free-panel-sub">{t('practice.corpusModesSub')}</p>
                      </div>
                    </div>
                    <div className="practice-free-panel-body">
                      <div className="practice-corpus-modes-grid" role="list">
                        {PRACTICE_TAB_DEF.map((tab) => {
                          const TabIcon = PRACTICE_TAB_ICONS[tab.id] || BookOpen
                          return (
                            <button
                              key={tab.id}
                              type="button"
                              role="listitem"
                              className="practice-corpus-mode-card"
                              onClick={() => openCorpusExplore(tab.id)}
                            >
                              <span className="practice-corpus-mode-icon" aria-hidden>
                                <TabIcon size={22} strokeWidth={2} />
                              </span>
                              <strong className="practice-corpus-mode-title">{t(tab.labelKey)}</strong>
                              <span className="practice-corpus-mode-cta">{t('practice.corpusOpenList')}</span>
                            </button>
                          )
                        })}
                      </div>
                      <p className="practice-corpus-customize-label">{t('practice.corpusCustomize')}</p>
                      <div className="learn-mock-filters practice-mock-tabs">
                        {PRACTICE_TAB_DEF.map((tab) => (
                          <button
                            key={tab.id}
                            type="button"
                            className={practiceTab === tab.id ? 'learn-mock-chip active' : 'learn-mock-chip'}
                            onClick={() => setPracticeTab(tab.id)}
                          >
                            {t(tab.labelKey)}
                          </button>
                        ))}
                      </div>
                      <label className="practice-mock-cat">
                        <span>{t('corpus.categoriesTitle')}</span>
                        <select value={category} onChange={(ev) => setCategory(ev.target.value)}>
                          {(categories?.length ? categories : ['comida']).map((c) => (
                            <option key={c} value={c}>
                              {titleLabel(c)}
                            </option>
                          ))}
                        </select>
                      </label>
                      <button type="button" className="practice-mock-start" onClick={() => loadFlow(null)}>
                        {t('practice.startSession')}
                      </button>
                    </div>
                  </>
                )}
              </section>
            </>
          )}

          {step === 'quiz' && q && (
            <div className="learn-mock-filters practice-mock-tabs practice-mock-tabs--readonly" aria-label={t('practice.pageTitle')}>
              {PRACTICE_TAB_DEF.map((tab) => (
                <span
                  key={tab.id}
                  className={practiceTab === tab.id ? 'learn-mock-chip active' : 'learn-mock-chip'}
                  role="presentation"
                >
                  {t(tab.labelKey)}
                </span>
              ))}
            </div>
          )}

          {step === 'quiz' && q && (
            <div className="practice-exercise-card">
              <div className="practice-ex-head">
                <div className="practice-ex-head-main">
                  <p className="practice-ex-kind">
                    {t('practice.exerciseHeading')}: {t(tabMeta.labelKey)}
                  </p>
                  <p className="practice-ex-meta">{t('act.qOf', { n: idx + 1, t: questions.length })}</p>
                  <div className="practice-ex-bar-track" aria-hidden>
                    <span className="practice-ex-bar-fill" style={{ width: `${practiceProgressRatio * 100}%` }} />
                  </div>
                </div>
                <div className="practice-ex-timer-block">
                  <span className="practice-ex-clock">
                    {Math.floor(seconds / 60)}:{String(seconds % 60).padStart(2, '0')}
                  </span>
                  <button type="button" className="practice-ex-end" onClick={() => finalize(false)}>
                    {t('act.finish')}
                  </button>
                </div>
              </div>

              {q.type === 'imagen' && q.image_url ? (
                <div className="practice-imagen-wrap">
                  <ActivityQuestionImage
                    src={q.image_url}
                    alt={q.espanol ? `Ilustración: ${q.espanol}` : ''}
                    className="practice-imagen"
                  />
                  <p className="practice-subq">{t(practiceQKey)}</p>
                  <p className="practice-prompt-fine">{q.prompt}</p>
                </div>
              ) : q.type === 'imagen' ? (
                <div className="practice-imagen-wrap practice-imagen-wrap--fallback">
                  <p className="practice-subq">{t('practice.imageUnavailable')}</p>
                  <p className="practice-prompt-fine">{q.prompt}</p>
                </div>
              ) : (
                <div className="practice-spotlight">
                  {(practiceTab === 'escucha' || practiceTab === 'vocabulario' || practiceTab === 'gramatica' || practiceTab === 'escritura') && (
                    <button
                      type="button"
                      className="practice-speak-btn"
                      aria-label={t('practice.listenCue')}
                      onClick={() => {
                        const line = [practiceCue, q?.espanol].filter(Boolean).join('. ')
                        const ok = speakText(line || q?.prompt || '', 'es')
                        if (!ok) notify(t('practice.audioUnavailable'))
                      }}
                    >
                      <Volume2 size={26} strokeWidth={2} aria-hidden />
                    </button>
                  )}
                  <div className="practice-spotlight-body">
                    <p className="practice-cue-word">{practiceCue}</p>
                    <p className="practice-subq">{t(practiceQKey)}</p>
                    <p className="practice-prompt-fine">{q.prompt}</p>
                  </div>
                </div>
              )}

              <div
                className={[
                  'practice-opt-grid',
                  q.option_images && Object.keys(q.option_images).length ? 'practice-opt-grid--visual' : '',
                ]
                  .filter(Boolean)
                  .join(' ')}
              >
                {(q.options || []).map((opt, opi) => {
                  const optImg = q.option_images?.[opt]
                  return (
                    <button
                      type="button"
                      key={`${q.id}-popt-${opi}`}
                      disabled={revealed}
                      className={[
                        'practice-opt',
                        optImg ? 'practice-opt--visual' : '',
                        revealed && activityStringsEqual(opt, q.answer) ? 'practice-opt-correct' : '',
                        revealed &&
                        chosen === opt &&
                        !activityStringsEqual(opt, q.answer)
                          ? 'practice-opt-wrong'
                          : '',
                      ]
                        .filter(Boolean)
                        .join(' ')}
                      onClick={() => pick(opt)}
                    >
                      <span className="practice-opt-icon">
                        <ActivityOptionVisual
                          optionText={opt}
                          optionImages={q.option_images}
                          category={q.categoria || practiceSessionRef.current.category}
                          imgClassName="practice-opt-thumb"
                          iconClassName="practice-opt-icon-svg"
                        />
                      </span>
                      <span className="practice-opt-label">{opt}</span>
                      {revealed && activityStringsEqual(opt, q.answer) ? (
                        <CheckCircle className="practice-opt-check" size={22} aria-hidden />
                      ) : null}
                      {revealed && chosen === opt && !activityStringsEqual(opt, q.answer) ? (
                        <XCircle className="practice-opt-x" size={22} aria-hidden />
                      ) : null}
                    </button>
                  )
                })}
              </div>

              {revealed ? (
                <div className="practice-feedback-bar">
                  <div className="practice-feedback-inner">
                    {activityStringsEqual(chosen, q.answer) ? (
                      <CheckCircle className="practice-feedback-ico ok" size={24} aria-hidden />
                    ) : (
                      <XCircle className="practice-feedback-ico bad" size={24} aria-hidden />
                    )}
                    <p className="practice-feedback-text">
                      {activityStringsEqual(chosen, q.answer)
                        ? t('practice.feedbackCorrect', {
                            nasa: q.answer,
                            es: practiceCue || q.espanol || '—',
                          })
                        : (
                            <>
                              {t('practice.feedbackWrongIntro')} <strong>{q.answer}</strong>
                            </>
                          )}
                    </p>
                    <button type="button" className="practice-next-pill" onClick={nextQuestion}>
                      {idx + 1 >= questions.length ? t('act.finish') : t('practice.nextArrow')}
                    </button>
                  </div>
                </div>
              ) : null}

              <div className="practice-card-links">
                <button
                  type="button"
                  className="practice-link-btn"
                  onClick={() =>
                    notify(
                      `${q.prompt}\n${t('practice.explainHint', { ok: q.answer, es: practiceCue || q.espanol || '' })}`,
                    )
                  }
                >
                  {t('practice.viewExplain')}
                </button>
                <button type="button" className="practice-link-btn" onClick={() => notify(t('practice.reportThanks'))}>
                  {t('practice.reportIssue')}
                </button>
              </div>
            </div>
          )}

          {step === 'score' && (
            <section className="practice-score-card">
              <h3>{t('act.scoreTitle')}</h3>
              <p className="practice-score-big">
                {questions.filter((iq) => activityStringsEqual(iq._picked, iq.answer)).length}/{questions.length}
              </p>
              <details className="practice-score-details">
                <summary>{t('act.breakdown')}</summary>
                <ul>
                  {questions.map((iq) => (
                    <li
                      key={iq.id}
                      className={activityStringsEqual(iq._picked, iq.answer) ? 'score-ok' : 'score-bad'}
                    >
                      {iq.prompt}: <strong>{iq.answer}</strong>
                    </li>
                  ))}
                </ul>
              </details>
              <button type="button" className="practice-mock-start" onClick={handlePracticeScoreToHub}>
                {t('practice.backToHub')}
              </button>
            </section>
          )}
        </div>

        <StudentPracticeAside t={t} navigateTo={navigateTo} />
      </div>
    </div>
  )
}

function StudentLearnRail({ t, navigateTo }) {
  const homeDonutPct = 65
  return (
    <aside className="learn-mock-rail">
      <div className="learn-rail-card learn-rail-card--progress">
        <h3>{t('learn.progressPanelTitle')}</h3>
        <div className="learn-donut-wrap">
          <div
            className="learn-donut"
            style={{
              background: `conic-gradient(#2f6f4a 0% ${homeDonutPct}%, #ede8dc ${homeDonutPct}% 100%)`,
            }}
          >
            <div className="learn-donut-inner">
              <span className="learn-donut-pct">{homeDonutPct}%</span>
              <small className="learn-donut-cap">{t('home.generalAdvance')}</small>
            </div>
          </div>
          <div className="skill-bars learn-skill-bars">
            {LEARN_SKILL_ROWS.map((row) => (
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
        </div>
      </div>

      <div className="learn-rail-card learn-rail-card--daily">
        <div className="learn-daily-head">
          <span className="learn-daily-icon" aria-hidden>
            <Target size={22} strokeWidth={2} />
          </span>
          <h3>{t('rightRail.daily')}</h3>
        </div>
        <p className="learn-daily-line">{t('home.dailyGoalLine')}</p>
        <p className="learn-daily-count">{t('home.dailyGoalCount', { done: 7, total: 10 })}</p>
        <div className="skill-track learn-daily-track">
          <div className="skill-fill skill-fill--goal" style={{ width: `${(7 / 10) * 100}%` }} />
        </div>
        <p className="learn-daily-motivate">{t('learn.dailyEncourage')}</p>
      </div>

      <div className="learn-rail-card learn-rail-card--cultural">
        <div className="learn-cultural-visual" aria-hidden />
        <h3>{t('learn.tipTitle')}</h3>
        <p>{t('learn.tipText')}</p>
        <button type="button" className="learn-cultural-more" onClick={() => navigateTo('diccionario')}>
          {t('learn.tipLink')}
        </button>
      </div>

      <div className="learn-rail-card learn-rail-card--practice-cta">
        <p className="learn-practice-cta-q">{t('learn.practiceCtaPrompt')}</p>
        <button type="button" className="learn-practice-cta-btn" onClick={() => navigateTo('practicar')}>
          {t('learn.practiceCtaBtn')} <span aria-hidden>→</span>
        </button>
      </div>
    </aside>
  )
}

export function StudentLearnRoute({ t, categories, setCategory, navigateTo }) {
  const [topicFilter, setTopicFilter] = useState('todos')

  function openLearnModule(row) {
    const c = resolveLearnCategoryForCorpus(row.slug, categories)
    const tabId = LEARN_FILTER_TO_PRACTICE_TAB[row.filterKey] || 'vocabulario'
    setCategory?.(c)
    navigateTo('practicar', {
      practiceFromLearn: { category: c, tabId, _bootKey: Date.now() },
    })
  }

  const filteredModules = LEARN_MODULES.filter(
    (m) => topicFilter === 'todos' || m.filterKey === topicFilter,
  )

  return (
    <div className="page-shell learn-mock-shell">
      <div className="learn-mock-grid">
        <div className="learn-mock-main">
          <header className="learn-mock-heading">
            <div className="learn-mock-heading-copy">
              <h2 className="learn-mock-title">
                {t('learn.pageTitle')}
                <span className="learn-mock-title-accent" aria-hidden />
              </h2>
            </div>
            <div className="learn-mock-art" aria-hidden>
              <img src={learnWelcomeIllustration} alt="" className="learn-mock-art-img" />
            </div>
          </header>

          <div className="learn-mock-filters">
            {LEARN_THEME_FILTERS.map((fid) => (
              <button
                key={fid}
                type="button"
                className={topicFilter === fid ? 'learn-mock-chip active' : 'learn-mock-chip'}
                onClick={() => setTopicFilter(fid)}
              >
                {t(`learn.filter.${fid}`)}
              </button>
            ))}
          </div>

          <div className="learn-modules-card">
            <ul className="learn-modules-list">
              {filteredModules.map((row) => {
                const Ico = row.Icon
                return (
                  <li key={row.key} className="learn-module-row">
                    <div className={`learn-module-icon-wrap learn-module-icon-wrap--${row.tone}`}>
                      <Ico size={22} strokeWidth={2.1} aria-hidden />
                    </div>
                    <div className="learn-module-body">
                      <div className="learn-module-top">
                        <h3 className="learn-module-title">{t(`learn.module.${row.key}`)}</h3>
                        <span className="learn-module-pct">{row.pct}%</span>
                      </div>
                      <p className="learn-module-meta">
                        {row.words} {t('learn.words')} | {row.lessons} {t('learn.lessons')}
                      </p>
                      <div className="learn-module-track-wrap">
                        <div className="learn-module-track">
                          <span
                            className={`learn-module-fill learn-module-fill--${row.tone}`}
                            style={{ width: `${row.pct}%` }}
                          />
                        </div>
                      </div>
                      <button
                        type="button"
                        className="learn-module-cta"
                        onClick={() => openLearnModule(row)}
                      >
                        {row.pct > 0 ? t('learn.continue') : t('learn.start')}
                      </button>
                    </div>
                  </li>
                )
              })}
            </ul>
          </div>

          <footer className="learn-mock-footer">
            <span className="learn-mock-footer-line" aria-hidden />
            <p>{t('learn.footerTag')}</p>
          </footer>
        </div>

        <StudentLearnRail t={t} navigateTo={navigateTo} />
      </div>
    </div>
  )
}

export function StudentPracticeRoute({ navigateTo, practiceFromLearn, onConsumePracticeFromLearn, ...props }) {
  return (
    <div className="practice-route-wrap">
      <StudentActivitiesRoute
        {...props}
        navigateTo={navigateTo}
        surface="practice"
        practiceFromLearn={practiceFromLearn}
        onConsumePracticeFromLearn={onConsumePracticeFromLearn}
      />
    </div>
  )
}

export function TeacherGroupsPanel({ t, notify, navigateHome, navigateTo }) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const [groups, setGroups] = useState([])
  const [students, setStudents] = useState([])
  const [grades, setGrades] = useState([])
  const [activities, setActivities] = useState([])
  const [qstud, setQstud] = useState('')
  const [name, setName] = useState('')
  const [edu, setEdu] = useState('Primaria')
  const [grade, setGrade] = useState('')
  const [gradeId, setGradeId] = useState('')
  const [dif, setDif] = useState('intermedio')
  const [actTitle, setActTitle] = useState('')
  const [actDesc, setActDesc] = useState('')
  const [actMode, setActMode] = useState('quiz')
  const [actCategory, setActCategory] = useState('comida')
  const [actGroupSel, setActGroupSel] = useState('')
  const [actWorkflow, setActWorkflow] = useState('activa')
  const [submission, setSubmission] = useState({ kind: 'termino', title: '', espanol: '', nasa_yuwe: '', translation: '', image_url: '', audio_url: '', notes: '' })
  const [pickedGroup, setPickedGroup] = useState(null)
  const [selIds, setSelIds] = useState([])
  const [report, setReport] = useState(null)
  const [reportPending, setReportPending] = useState(false)
  const [panel, setPanel] = useState('list')

  async function reload() {
    try {
      const [g, gr, act] = await Promise.all([
        getTeacherGroups(token),
        getTeacherGrades(token),
        getTeacherActivities(token),
      ])
      setGroups(g.groups || [])
      setGrades(gr.grades || [])
      setActivities(act.activities || [])
    } catch {
      notify(t('teacher.loadErr'))
    }
  }

  useEffect(() => {
    reload()
  }, [])

  useEffect(() => {
    async function s() {
      try {
        const r = await getTeacherStudents(token, qstud)
        setStudents(r.students || [])
      } catch {
        notify(t('teacher.studentsErr'))
      }
    }
    const tm = window.setTimeout(s, 250)
    return () => window.clearTimeout(tm)
  }, [qstud, token])

  async function createGroup(ev) {
    ev.preventDefault()
    try {
      await postAuthorized(
        '/api/teacher/groups',
        token,
        { name, education_level: edu, grade, grade_id: Number(gradeId || 0), difficulty_default: dif },
      )
      notify(t('teacher.groupSaved'))
      setName('')
      setGrade('')
      reload()
    } catch (e) {
      notify(e.message)
    }
  }

  async function createActivity() {
    if (!actTitle.trim()) {
      notify(t('teacher.actTitleRequired'))
      return
    }
    try {
      await createTeacherActivity(token, {
        title: actTitle.trim(),
        description: (actDesc || actTitle).trim(),
        category: actCategory,
        difficulty: dif,
        mode: actMode,
        status: actWorkflow,
        grade_id: Number(gradeId || 0),
        group_id: Number(actGroupSel || pickedGroup?.id || 0),
      })
      setActTitle('')
      setActDesc('')
      reload()
      notify(t('teacher.actCreated'))
    } catch (e) {
      notify(e.message)
    }
  }

  async function sendSubmission() {
    if (!submission.title.trim()) {
      notify(t('teacher.submissionNeedTitle'))
      return
    }
    try {
      await submitTeacherContent(token, {
        ...submission,
        title: submission.title.trim(),
      })
      setSubmission({ kind: 'termino', title: '', espanol: '', nasa_yuwe: '', translation: '', image_url: '', audio_url: '', notes: '' })
      notify(t('teacher.submissionSentOk'))
    } catch (e) {
      notify(e.message)
    }
  }

  async function assign() {
    if (!pickedGroup) return
    try {
      const r = await postAuthorized('/api/teacher/group-assign', token, {
        group_id: pickedGroup.id,
        student_ids: selIds,
      })
      notify(r.message || t('teacher.assignOk'))
      setSelIds([])
      setPanel('list')
      reload()
    } catch (e) {
      notify(e.message)
    }
  }

  async function openReport(g) {
    setPickedGroup(g)
    setPanel('report')
    setReport(null)
    setReportPending(true)
    try {
      const rp = await getTeacherGroupReport(token, g.id)
      setReport(rp)
    } catch {
      setReport(null)
      notify(t('teacher.reportErr'))
    } finally {
      setReportPending(false)
    }
  }

  function csvReport() {
    if (!report) return
    const rows = [['Grupo', report.group?.name], ['Estudiante', 'Correo'], ...report.students.map((s) => [s.display_name, s.email])]
    const blob = new Blob([rows.map((x) => x.join(',')).join('\n')], { type: 'text/csv' })
    const a = document.createElement('a')
    a.href = URL.createObjectURL(blob)
    a.download = `reporte-${report.group?.id}.csv`
    a.click()
    notify(t('teacher.csvOk'))
  }

  async function unassignStudent(studentId) {
    if (!report?.group?.id || !studentId) return
    try {
      await postTeacherGroupUnassign(token, { group_id: report.group.id, student_id: studentId })
      notify(t('teacher.unassignOk'))
      const rp = await getTeacherGroupReport(token, report.group.id)
      setReport(rp)
      reload()
    } catch (e) {
      notify(e.message)
    }
  }

  return (
    <div className="teacher-workspace-shell">
      <div className="page-shell doc-shell teacher-module teacher-groups-legacy">
      <header className="page-title dict-head teacher-grupos-head-row">
        <div>
          <h2>{t('teacher.pageTitleGroups')}</h2>
          <p>{t('teacher.pageSubGroups')}</p>
        </div>
        <div className="teacher-grupos-head-actions">
          {typeof navigateTo === 'function' ? (
            <>
              <button type="button" className="dict-home-btn dict-home-btn--ghost" onClick={() => navigateTo('docente_actividades')}>
                {t('teacher.shortcutActs')}
              </button>
              <button type="button" className="dict-home-btn dict-home-btn--ghost" onClick={() => navigateTo('docente_reportes')}>
                {t('teacher.shortcutReports')}
              </button>
            </>
          ) : null}
          <button type="button" className="dict-home-btn" onClick={navigateHome}>
            {t('teacher.homeTeacher')}
          </button>
        </div>
      </header>
      {panel === 'report' ? (
        reportPending ? (
          <p className="doc-report-loading">{t('teacher.loadingReport')}</p>
        ) : !report ? (
          <div className="doc-report doc-report-fail">
            <button type="button" className="link-back" onClick={() => setPanel('list')}>
              <ArrowLeft size={16} /> {t('teacher.backGroups')}
            </button>
            <p>{t('teacher.reportErr')}</p>
          </div>
        ) : (
        <div className="doc-report">
          <button type="button" className="link-back" onClick={() => setPanel('list')}>
            <ArrowLeft size={16} /> {t('teacher.backGroups')}
          </button>
          <h3>{report.group?.name}</h3>
          <p>
            {t('teacher.reportSummary')}: {report.summary?.total_estudiantes ?? 0} · {t('teacher.reportActsAssigned')}:{' '}
            {report.summary?.actividades_asignadas_grupo ?? 0} · {t('teacher.reportActAvg')}:{' '}
            {report.summary?.promedio_actividades_por_estudiante ?? '—'}
          </p>
          <ul>
            {(report.students || []).map((st) => (
              <li key={st.id}>
                <strong>{st.display_name}</strong> — {st.email}{' '}
                <button type="button" className="secondary-b" onClick={() => unassignStudent(st.id)}>
                  {t('teacher.unassignStudent')}
                </button>
              </li>
            ))}
          </ul>
          <div className="doc-report-actions">
            <button type="button" onClick={csvReport}>
              {t('teacher.csv')}
            </button>
            <button type="button" className="secondary-b" onClick={() => window.print()}>
              {t('teacher.printPdf')}
            </button>
          </div>
        </div>
        )
      ) : (
        <>
          {!groups.length ? <p className="doc-empty-visual">{t('teacher.noGroups')}</p> : null}
          <div className="doc-grid-two">
            <form className="doc-card-form" onSubmit={createGroup}>
              <h3>{t('teacher.newGroup')}</h3>
              <input required value={name} onChange={(ev) => setName(ev.target.value)} placeholder={t('teacher.groupNamePh')} />
              <label>
                {t('teacher.levelEdu')}
                <select value={edu} onChange={(ev) => setEdu(ev.target.value)}>
                  <option value="Primaria">{t('teacher.eduPrimaria')}</option>
                  <option value="Secundaria">{t('teacher.eduSec')}</option>
                  <option value="Otro">{t('teacher.eduOther')}</option>
                </select>
              </label>
              {edu === 'Primaria' ? (
                <input value={grade} onChange={(ev) => setGrade(ev.target.value)} placeholder={t('teacher.gradePh')} />
              ) : null}
              <label>
                Grado global
                <select value={gradeId} onChange={(ev) => setGradeId(ev.target.value)}>
                  <option value="">(opcional)</option>
                  {grades.map((g) => (
                    <option key={g.id} value={g.id}>
                      {g.name}
                    </option>
                  ))}
                </select>
              </label>
              <select value={dif} onChange={(ev) => setDif(ev.target.value)}>
                <option value="facil">{t('act.facil')}</option>
                <option value="intermedio">{t('act.intermedio')}</option>
                <option value="avanzado">{t('act.avanzado')}</option>
              </select>
              <button type="submit">{t('teacher.saveGroup')}</button>
            </form>
            <div className="doc-card-list">
              <h3>{t('teacher.groupsList')}</h3>
              {!groups.length ? <p>{t('teacher.noneYet')}</p> : null}
              <table className="doc-table">
                <thead>
                  <tr>
                    <th>{t('teacher.colName')}</th>
                    <th>{t('teacher.colDifficulty')}</th>
                    <th>{t('teacher.colStudents')}</th>
                    <th>{t('teacher.colActions')}</th>
                  </tr>
                </thead>
                <tbody>
                  {groups.map((g) => (
                    <tr key={g.id}>
                      <td className="td-wrap">{g.name}</td>
                      <td>{labelSlug(g.difficulty_default)}</td>
                      <td>{g.students}</td>
                      <td>
                        <button
                          type="button"
                          onClick={() => {
                            setPickedGroup(g)
                            setPanel('assign')
                          }}
                        >
                          {t('teacher.assign')}
                        </button>{' '}
                        <button type="button" onClick={() => openReport(g)}>
                          {t('teacher.reports')}
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
              {pickedGroup && panel === 'assign' ? (
                <div className="assign-box">
                  <h4>{t('teacher.pickStudents', { group: pickedGroup.name })}</h4>
                  <input value={qstud} onChange={(ev) => setQstud(ev.target.value)} placeholder={t('teacher.searchStudent')} />
                  <div className="student-chip-list">
                    {students.map((s) => {
                      const gid = pickedGroup?.id
                      const inOther = s.member_group_id && gid && Number(s.member_group_id) !== Number(gid)
                      const inThis = s.member_group_id && gid && Number(s.member_group_id) === Number(gid)
                      const disabled = inOther || inThis
                      return (
                        <label
                          key={s.id}
                          className={`student-chip${disabled ? ' student-chip--disabled' : ''}`}
                        >
                          <input
                            type="checkbox"
                            disabled={disabled}
                            checked={inThis || selIds.includes(s.id)}
                            onChange={(ev) => {
                              if (disabled) return
                              setSelIds((ids) =>
                                ev.target.checked ? [...ids, s.id] : ids.filter((x) => x !== s.id),
                              )
                            }}
                          />
                          <span>{s.display_name}</span>
                          {inOther ? <small> ({t('teacher.assignBlockedOther')})</small> : null}
                          {inThis ? <small> ({t('teacher.assignInGroup')})</small> : null}
                        </label>
                      )
                    })}
                  </div>
                  <div className="assign-actions">
                    <button type="button" onClick={assign}>
                      {t('teacher.assignSubmit')}
                    </button>
                    <button type="button" className="secondary-b" onClick={() => setPanel('list')}>
                      {t('teacher.cancel')}
                    </button>
                  </div>
                </div>
              ) : null}
            </div>
          </div>
          <div className="doc-grid-two">
            <section className="doc-card-form">
              <h3>{t('teacher.actFormShortTitle')}</h3>
              <input value={actTitle} onChange={(ev) => setActTitle(ev.target.value)} placeholder={t('teacher.actTitlePh')} />
              <textarea value={actDesc} onChange={(ev) => setActDesc(ev.target.value)} placeholder={t('teacher.actDescPh')} rows={3} />
              <label>
                {t('teacher.actAssignGroupLbl')}
                <select value={actGroupSel} onChange={(ev) => setActGroupSel(ev.target.value)}>
                  <option value="">{t('teacher.actPickGroupOpt')}</option>
                  {groups.map((g) => (
                    <option key={g.id} value={g.id}>
                      {g.name}
                    </option>
                  ))}
                </select>
              </label>
              <label>
                {t('teacher.actStateLbl')}
                <select value={actWorkflow} onChange={(ev) => setActWorkflow(ev.target.value)}>
                  <option value="activa">{t('teacher.statusActive')}</option>
                  <option value="borrador">{t('teacher.statusDraft')}</option>
                  <option value="programada">{t('teacher.statusScheduled')}</option>
                </select>
              </label>
              <select value={actCategory} onChange={(ev) => setActCategory(ev.target.value)}>
                <option value="comida">comida</option>
                <option value="animales">animales</option>
                <option value="familia_personas">familia_personas</option>
              </select>
              <select value={actMode} onChange={(ev) => setActMode(ev.target.value)}>
                <option value="quiz">{t('teacher.modeQuiz')}</option>
                <option value="completar">{t('teacher.modeComplete')}</option>
                <option value="imagen">{t('teacher.modeImage')}</option>
              </select>
              <button type="button" onClick={createActivity}>
                {t('teacher.actSave')}
              </button>
            </section>
            <section className="doc-card-list">
              <h3>{t('teacher.createdActsTitle')}</h3>
              {!activities.length ? <p>{t('practice.empty')}</p> : null}
              <ul className="cms-list">
                {activities.slice(0, 20).map((a) => (
                  <li key={a.id}>
                    <strong>{a.title}</strong> <small>({a.category} · {a.difficulty} · {a.mode})</small>
                  </li>
                ))}
              </ul>
            </section>
          </div>
          <section className="doc-card-form">
            <h3>{t('teacher.proposeSectionTitle')}</h3>
            <input
              value={submission.title}
              onChange={(ev) => setSubmission((s) => ({ ...s, title: ev.target.value }))}
              placeholder={t('teacher.proposePhTitle')}
            />
            <input
              value={submission.espanol}
              onChange={(ev) => setSubmission((s) => ({ ...s, espanol: ev.target.value }))}
              placeholder={t('teacher.proposePhEspanol')}
            />
            <input
              value={submission.nasa_yuwe}
              onChange={(ev) => setSubmission((s) => ({ ...s, nasa_yuwe: ev.target.value }))}
              placeholder={t('teacher.proposePhNasa')}
            />
            <input
              value={submission.translation}
              onChange={(ev) => setSubmission((s) => ({ ...s, translation: ev.target.value }))}
              placeholder={t('teacher.proposePhTrans')}
            />
            <input
              value={submission.image_url}
              onChange={(ev) => setSubmission((s) => ({ ...s, image_url: ev.target.value }))}
              placeholder={t('teacher.proposePhImg')}
            />
            <input
              value={submission.audio_url}
              onChange={(ev) => setSubmission((s) => ({ ...s, audio_url: ev.target.value }))}
              placeholder={t('teacher.proposePhAudio')}
            />
            <textarea
              value={submission.notes}
              onChange={(ev) => setSubmission((s) => ({ ...s, notes: ev.target.value }))}
              placeholder={t('teacher.proposePhNotes')}
              rows={3}
            />
            <button type="button" onClick={sendSubmission}>
              {t('teacher.proposeSubmitBtn')}
            </button>
          </section>
        </>
      )}
    </div>
    </div>
  )
}

export function AdminUsersPanel({ t, notify }) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const [users, setUsers] = useState([])
  const [editing, setEditing] = useState(null)
  const [userTab, setUserTab] = useState('all')
  const [userSearch, setUserSearch] = useState('')
  const [grades, setGrades] = useState([])
  const [newGrade, setNewGrade] = useState({ name: '', level: 'Primaria' })
  const [creating, setCreating] = useState(false)
  const [createForm, setCreateForm] = useState(() => ({
    email: '',
    password: '',
    display_name: '',
    role: 'estudiante',
  }))
  const [previewUser, setPreviewUser] = useState(null)

  async function reload() {
    try {
      const [data, g] = await Promise.all([getAdminUsers(token), getAdminGrades(token)])
      setUsers(data.users || [])
      setGrades(g.grades || [])
      return true
    } catch {
      notify(t('admin.loadErr'))
      return false
    }
  }

  useEffect(() => {
    reload()
  }, [])

  async function saveUser() {
    if (!editing) return
    try {
      const payload = { id: editing.id, display_name: editing.display_name, role: editing.role, active: editing.active ? 1 : 0 }
      await postAuthorized('/api/admin/user-update', token, payload)
      notify(t('admin.saveOk'))
      setEditing(null)
      reload()
    } catch (e) {
      notify(e.message)
    }
  }

  async function deleteUser(uid) {
    if (!window.confirm(t('admin.confirmDel'))) return
    try {
      await postAuthorized('/api/admin/user-delete', token, { id: uid })
      notify(t('admin.deleted'))
      reload()
    } catch {
      notify(t('admin.deleteErr'))
    }
  }

  async function saveGrade() {
    if (!newGrade.name.trim()) {
      notify('Escribe el nombre del grado.')
      return
    }
    try {
      await saveAdminGrade(token, { name: newGrade.name.trim(), level: newGrade.level })
      setNewGrade({ name: '', level: newGrade.level })
      reload()
      notify('Grado guardado.')
    } catch (e) {
      notify(e.message)
    }
  }

  async function removeGrade(gradeId) {
    try {
      await deleteAdminGrade(token, gradeId)
      reload()
      notify('Grado eliminado.')
    } catch (e) {
      notify(e.message)
    }
  }

  async function updateStudentGrade(studentId, gradeId) {
    try {
      await assignStudentGrade(token, studentId, Number(gradeId || 0))
      reload()
      notify('Grado asignado.')
    } catch (e) {
      notify(e.message)
    }
  }

  async function submitCreateUser(ev) {
    ev.preventDefault()
    const pwErrs = validatePasswordStrength(createForm.password)
    if (pwErrs.length) {
      notify(pwErrs.join(' '))
      return
    }
    try {
      await postAdminUserCreate(token, {
        email: createForm.email.trim(),
        password: createForm.password,
        display_name: createForm.display_name.trim(),
        role: createForm.role,
      })
      notify(t('admin.userCreated'))
      setCreating(false)
      setCreateForm({ email: '', password: '', display_name: '', role: 'estudiante' })
      reload()
    } catch (e) {
      notify(e.message || t('admin.createUserErr'))
    }
  }

  async function copyEmail(email) {
    try {
      await navigator.clipboard.writeText(String(email || ''))
      notify(t('admin.emailCopied'))
    } catch {
      notify(String(email || ''))
    }
  }

  const userTabDefs = useMemo(
    () => [
      { id: 'all', labelKey: 'admin.tabAll' },
      { id: 'docente', labelKey: 'admin.tabTeachers' },
      { id: 'estudiante', labelKey: 'admin.tabStudents' },
      { id: 'administrador', labelKey: 'admin.tabAdmins' },
    ],
    [],
  )

  const filteredUsers = useMemo(() => {
    return users.filter((u) => {
      if (userTab !== 'all' && u.role !== userTab) return false
      const q = userSearch.trim().toLowerCase()
      if (!q) return true
      return (
        String(u.display_name || '')
          .toLowerCase()
          .includes(q) || String(u.email || '')
          .toLowerCase()
          .includes(q)
      )
    })
  }, [users, userTab, userSearch])

  return (
    <div className="page-shell adm-shell admin-users-shell">
      <header className="page-title admin-panel-head">
        <div>
          <h2>{t('admin.usersTitle')}</h2>
          <p>{t('admin.usersSub')}</p>
        </div>
        <button
          type="button"
          className="admin-toolbar-primary"
          onClick={() => {
            setCreateForm({ email: '', password: '', display_name: '', role: 'estudiante' })
            setCreating(true)
          }}
        >
          <Plus size={17} strokeWidth={2.2} aria-hidden /> {t('admin.newUser')}
        </button>
      </header>

      <div className="admin-toolbar">
        <div className="admin-toolbar-tabs" role="tablist">
          {userTabDefs.map((tab) => (
            <button
              key={tab.id}
              type="button"
              role="tab"
              aria-selected={userTab === tab.id}
              className={userTab === tab.id ? 'admin-tab admin-tab--active' : 'admin-tab'}
              onClick={() => setUserTab(tab.id)}
            >
              {t(tab.labelKey)}
            </button>
          ))}
        </div>
        <div className="admin-toolbar-search">
          <label className="admin-search-field">
            <Search size={17} strokeWidth={2} aria-hidden />
            <input
              type="search"
              value={userSearch}
              onChange={(ev) => setUserSearch(ev.target.value)}
              placeholder={t('admin.searchUsers')}
              autoComplete="off"
            />
          </label>
          <button
            type="button"
            className="admin-filter-btn"
            onClick={async () => {
              if (await reload()) notify(t('admin.refreshOk'))
            }}
          >
            <SlidersHorizontal size={17} strokeWidth={2} aria-hidden />
            {t('admin.refreshBtn')}
          </button>
        </div>
      </div>

      <section className="admin-grades-panel">
        <h3>{t('admin.gradesSectionTitle')}</h3>
        <p className="admin-grades-hint">{t('admin.gradesSectionHint')}</p>
        <div className="admin-grades-create">
          <input
            placeholder="Ej. 6A"
            value={newGrade.name}
            onChange={(ev) => setNewGrade((g) => ({ ...g, name: ev.target.value }))}
          />
          <select value={newGrade.level} onChange={(ev) => setNewGrade((g) => ({ ...g, level: ev.target.value }))}>
            <option>Primaria</option>
            <option>Secundaria</option>
            <option>Media</option>
          </select>
          <button type="button" onClick={saveGrade}>Guardar grado</button>
        </div>
        <div className="admin-grades-list">
          {grades.map((g) => (
            <span key={g.id} className="admin-grade-chip">
              {g.name} ({g.level})
              <button type="button" onClick={() => removeGrade(g.id)}>×</button>
            </span>
          ))}
        </div>
      </section>
      {!users.length ? <p className="doc-empty-visual">{t('admin.noUsers')}</p> : null}
      <div className="admin-table-wrap">
        <table className="doc-table adm-user-table admin-data-table">
          <thead>
            <tr>
              <th>{t('settings.nameLabel')}</th>
              <th>{t('settings.emailLabel')}</th>
              <th>{t('login.roleBadge')}</th>
              <th>Grado</th>
              <th>{t('admin.activeCol')}</th>
              <th className="admin-col-actions">{t('admin.actionsCol')}</th>
            </tr>
          </thead>
          <tbody>
            {filteredUsers.map((u) => (
              <tr key={u.id}>
                <td>
                  <strong>{u.display_name}</strong>
                </td>
                <td>{u.email}</td>
                <td>{u.role}</td>
                <td>
                  {u.role === 'estudiante' ? (
                    <select
                      value={u.grade_id || ''}
                      onChange={(ev) => updateStudentGrade(u.id, ev.target.value)}
                    >
                      <option value="">Sin grado</option>
                      {grades.map((g) => (
                        <option key={g.id} value={g.id}>
                          {g.name}
                        </option>
                      ))}
                    </select>
                  ) : (
                    <span>—</span>
                  )}
                </td>
                <td>
                  <span className={u.active ? 'status-pill ok' : 'status-pill warn'}>
                    {u.active ? t('admin.statusActive') : t('admin.statusInactive')}
                  </span>
                </td>
                <td>
                  <div className="admin-table-actions">
                    <button
                      type="button"
                      className="admin-icon-btn"
                      aria-label={t('admin.view')}
                      onClick={() =>
                        setPreviewUser({
                          id: u.id,
                          display_name: u.display_name,
                          email: u.email,
                          role: u.role,
                          active: u.active,
                          grade_name: u.grade_name || '',
                        })
                      }
                    >
                      <Eye size={17} strokeWidth={2} />
                    </button>
                    <button
                      type="button"
                      className="admin-icon-btn"
                      aria-label={t('admin.edit')}
                      onClick={() =>
                        setEditing({
                          id: u.id,
                          display_name: u.display_name,
                          role: u.role,
                          active: u.active,
                        })
                      }
                    >
                      <Pencil size={17} strokeWidth={2} />
                    </button>
                    <button type="button" className="admin-icon-btn" aria-label={t('admin.delete')} onClick={() => deleteUser(u.id)}>
                      <Trash2 size={17} strokeWidth={2} />
                    </button>
                    <button type="button" className="admin-icon-btn" aria-label={t('admin.copyEmail')} onClick={() => copyEmail(u.email)}>
                      <MoreVertical size={17} strokeWidth={2} />
                    </button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {editing ? (
        <div className="admin-modal">
          <div className="admin-modal-inner">
            <h3>{t('admin.editUser')}</h3>
            <input
              value={editing.display_name}
              onChange={(ev) => setEditing({ ...editing, display_name: ev.target.value })}
            />
            <select value={editing.role} onChange={(ev) => setEditing({ ...editing, role: ev.target.value })}>
              <option value="estudiante">{t('login.roleStud')}</option>
              <option value="docente">{t('login.roleTeach')}</option>
              <option value="administrador">{t('login.roleAdmin')}</option>
            </select>
            <label className="inline-check">
              <input
                type="checkbox"
                checked={Boolean(editing.active)}
                onChange={(ev) => setEditing({ ...editing, active: ev.target.checked })}
              />
              {t('admin.activeCol')}
            </label>
            <div className="modal-actions-row">
              <button type="button" onClick={saveUser}>
                {t('admin.save')}
              </button>
              <button type="button" className="secondary-b" onClick={() => setEditing(null)}>
                {t('teacher.cancel')}
              </button>
            </div>
          </div>
        </div>
      ) : null}
      {creating ? (
        <div className="admin-modal">
          <div className="admin-modal-inner admin-modal-inner--wide">
            <h3>{t('admin.createUserTitle')}</h3>
            <p className="admin-modal-intro">{t('admin.createUserSub')}</p>
            <form className="admin-create-user-form" onSubmit={submitCreateUser}>
              <label className="admin-field-block">
                <span>{t('admin.createUserEmail')}</span>
                <input
                  type="email"
                  required
                  value={createForm.email}
                  onChange={(ev) => setCreateForm((f) => ({ ...f, email: ev.target.value }))}
                  autoComplete="off"
                />
              </label>
              <label className="admin-field-block">
                <span>{t('admin.createUserName')}</span>
                <input
                  type="text"
                  required
                  minLength={2}
                  value={createForm.display_name}
                  onChange={(ev) => setCreateForm((f) => ({ ...f, display_name: ev.target.value }))}
                  autoComplete="off"
                />
              </label>
              <label className="admin-field-block">
                <span>{t('admin.createUserPassword')}</span>
                <input
                  type="password"
                  required
                  minLength={10}
                  value={createForm.password}
                  onChange={(ev) => setCreateForm((f) => ({ ...f, password: ev.target.value }))}
                  autoComplete="new-password"
                />
              </label>
              <label className="admin-field-block">
                <span>{t('login.roleBadge')}</span>
                <select value={createForm.role} onChange={(ev) => setCreateForm((f) => ({ ...f, role: ev.target.value }))}>
                  <option value="estudiante">{t('login.roleStud')}</option>
                  <option value="docente">{t('login.roleTeach')}</option>
                  <option value="administrador">{t('login.roleAdmin')}</option>
                </select>
              </label>
              <div className="modal-actions-row">
                <button type="submit">{t('admin.createUserSubmit')}</button>
                <button type="button" className="secondary-b" onClick={() => setCreating(false)}>
                  {t('teacher.cancel')}
                </button>
              </div>
            </form>
          </div>
        </div>
      ) : null}
      {previewUser ? (
        <div className="admin-modal">
          <div className="admin-modal-inner">
            <h3>{t('admin.userPreviewTitle')}</h3>
            <p className="admin-preview-line">
              <strong>{previewUser.display_name}</strong>
            </p>
            <p className="admin-preview-line">{previewUser.email}</p>
            <p className="admin-preview-line">
              {t('login.roleBadge')}: {previewUser.role}
            </p>
            <p className="admin-preview-line">
              {t('admin.activeCol')}: {previewUser.active ? t('admin.statusActive') : t('admin.statusInactive')}
            </p>
            {previewUser.role === 'estudiante' && previewUser.grade_name ? (
              <p className="admin-preview-line">
                Grado: <strong>{previewUser.grade_name}</strong>
              </p>
            ) : null}
            <div className="modal-actions-row">
              <button type="button" onClick={() => copyEmail(previewUser.email)}>
                {t('admin.copyEmail')}
              </button>
              <button type="button" className="secondary-b" onClick={() => setPreviewUser(null)}>
                {t('teacher.cancel')}
              </button>
            </div>
          </div>
        </div>
      ) : null}
    </div>
  )
}

function normCmsKind(s) {
  return String(s || '')
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
}

function cmsRowMatchesTab(item, tabId) {
  if (tabId === 'all') return true
  const k = normCmsKind(item.kind)
  if (tabId === 'leccion') return k.includes('leccion')
  if (tabId === 'vocabulario') return k.includes('vocab') || k.includes('termino')
  if (tabId === 'dialogo') return k.includes('dialog')
  if (tabId === 'cultura') return k.includes('cultura')
  if (tabId === 'recurso') return k.includes('recurso') || k.includes('media')
  return true
}

export function AdminContentPanel({ t, notify }) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const [data, setData] = useState({ cms_items: [], categories: [] })
  const [form, setForm] = useState({ id: '', kind: 'termino', title: '', body: '', status: 'published' })
  const [submissions, setSubmissions] = useState([])
  const [contentTab, setContentTab] = useState('all')
  const [contentSearch, setContentSearch] = useState('')
  const [cmsPreview, setCmsPreview] = useState(null)

  const contentTabDefs = useMemo(
    () => [
      { id: 'all', labelKey: 'admin.tabAll' },
      { id: 'leccion', labelKey: 'admin.tabLessons' },
      { id: 'vocabulario', labelKey: 'admin.tabVocab' },
      { id: 'dialogo', labelKey: 'admin.tabDialogues' },
      { id: 'cultura', labelKey: 'admin.tabCulture' },
      { id: 'recurso', labelKey: 'admin.tabResources' },
    ],
    [],
  )

  async function reload() {
    try {
      const [d, s] = await Promise.all([getAdminCms(token), getAdminContentSubmissions(token)])
      setData(d)
      setSubmissions(s.items || [])
      return true
    } catch {
      notify(t('admin.loadErr'))
      return false
    }
  }

  useEffect(() => {
    reload()
  }, [])

  const displayCms = useMemo(() => {
    const fromApi = data.cms_items || []
    return fromApi.map((it) => ({
      ...it,
      _isDraft: String(it.status || '').toLowerCase() === 'draft',
    }))
  }, [data.cms_items])

  const filteredCms = useMemo(() => {
    return displayCms.filter((it) => {
      if (!cmsRowMatchesTab(it, contentTab)) return false
      const q = contentSearch.trim().toLowerCase()
      if (!q) return true
      return (
        String(it.title || '')
          .toLowerCase()
          .includes(q) || String(it.kind || '')
          .toLowerCase()
          .includes(q) ||
        String(it.category || '')
          .toLowerCase()
          .includes(q)
      )
    })
  }, [displayCms, contentTab, contentSearch])

  async function save() {
    if (!form.kind.trim() || !form.title.trim()) {
      notify(t('admin.cmsNeedData'))
      return
    }
    try {
      const payload = {
        ...form,
        kind: form.kind.trim(),
        title: form.title.trim(),
        body: form.body.trim(),
        status: form.status,
      }
      if (payload.id) payload.id = Number(payload.id)
      else delete payload.id
      await postAuthorized('/api/admin/cms-save', token, payload)
      notify(t('admin.cmsSaved'))
      setForm({ id: '', kind: 'termino', title: '', body: '', status: 'published' })
      reload()
    } catch {
      notify(t('admin.cmsSaveErr'))
    }
  }

  async function deleteItem(cid) {
    if (!cid) return
    try {
      await postAuthorized('/api/admin/cms-delete', token, { id: cid })
      reload()
    } catch {
      notify(t('admin.deleteErr'))
    }
  }

  async function reviewSubmission(id, action) {
    try {
      await reviewAdminContentSubmission(token, { id, action, review_notes: '' })
      reload()
      notify(action === 'approve' ? t('admin.reviewApproved') : t('admin.reviewRejected'))
    } catch (e) {
      notify(e.message)
    }
  }

  return (
    <div className="page-shell adm-shell admin-cms-shell">
      <header className="page-title admin-panel-head">
        <div>
          <h2>{t('admin.cmsTitle')}</h2>
          <p>{t('admin.cmsSub')}</p>
        </div>
        <button
          type="button"
          className="admin-toolbar-primary"
          onClick={() => document.getElementById('admin-cms-form')?.scrollIntoView({ behavior: 'smooth' })}
        >
          <Plus size={17} strokeWidth={2.2} /> {t('admin.newContent')}
        </button>
      </header>

      <div className="admin-toolbar">
        <div className="admin-toolbar-tabs" role="tablist">
          {contentTabDefs.map((tab) => (
            <button
              key={tab.id}
              type="button"
              role="tab"
              aria-selected={contentTab === tab.id}
              className={contentTab === tab.id ? 'admin-tab admin-tab--active' : 'admin-tab'}
              onClick={() => setContentTab(tab.id)}
            >
              {t(tab.labelKey)}
            </button>
          ))}
        </div>
        <div className="admin-toolbar-search">
          <label className="admin-search-field">
            <Search size={17} strokeWidth={2} aria-hidden />
            <input
              type="search"
              value={contentSearch}
              onChange={(ev) => setContentSearch(ev.target.value)}
              placeholder={t('admin.searchContent')}
              autoComplete="off"
            />
          </label>
          <button
            type="button"
            className="admin-filter-btn"
            onClick={async () => {
              if (await reload()) notify(t('admin.refreshOk'))
            }}
          >
            <Filter size={17} strokeWidth={2} aria-hidden />
            {t('admin.refreshBtn')}
          </button>
        </div>
      </div>

      <div className="admin-table-wrap">
        <table className="doc-table admin-data-table admin-cms-table">
          <thead>
            <tr>
              <th>{t('admin.colTitle')}</th>
              <th>{t('admin.colType')}</th>
              <th>{t('admin.colCategory')}</th>
              <th>{t('admin.colLang')}</th>
              <th>{t('admin.colStatus')}</th>
              <th className="admin-col-actions">{t('admin.actionsCol')}</th>
            </tr>
          </thead>
          <tbody>
            {filteredCms.length === 0 ? (
              <tr>
                <td colSpan={6} className="admin-cell-muted">
                  {t('admin.cmsEmpty')}
                </td>
              </tr>
            ) : (
              filteredCms.map((it) => (
                <tr key={it.id}>
                  <td>
                    <strong>{it.title}</strong>
                  </td>
                  <td>{it.kind}</td>
                  <td>{it.category || t('admin.cmsCategoryFallback')}</td>
                  <td>{t('admin.cmsLangDisplay')}</td>
                  <td>
                    <span className={it._isDraft ? 'status-pill warn' : 'status-pill ok'}>
                      {it._isDraft ? t('admin.statusDraft') : t('admin.statusPublished')}
                    </span>
                  </td>
                  <td>
                    <div className="admin-table-actions">
                      <button
                        type="button"
                        className="admin-icon-btn"
                        aria-label={t('admin.view')}
                        onClick={() =>
                          setCmsPreview({
                            title: it.title,
                            kind: it.kind,
                            body: String(it.body || '').trim() || '—',
                          })
                        }
                      >
                        <Eye size={17} strokeWidth={2} />
                      </button>
                      <button
                        type="button"
                        className="admin-icon-btn"
                        aria-label={t('admin.edit')}
                        onClick={() =>
                          setForm({
                            id: String(it.id),
                            kind: it.kind || 'termino',
                            title: it.title || '',
                            body: it.body || '',
                            status: it._isDraft ? 'draft' : 'published',
                          })
                        }
                      >
                        <Pencil size={17} strokeWidth={2} />
                      </button>
                      <button
                        type="button"
                        className="admin-icon-btn"
                        aria-label={t('admin.delete')}
                        onClick={() => deleteItem(it.id)}
                      >
                        <Trash2 size={17} strokeWidth={2} />
                      </button>
                      <button
                        type="button"
                        className="admin-icon-btn"
                        aria-label={t('admin.copyTitle')}
                        onClick={() => {
                          navigator.clipboard
                            .writeText(String(it.title || ''))
                            .then(() => notify(t('admin.cmsTitleCopied')))
                            .catch(() => notify(String(it.title || '')))
                        }}
                      >
                        <MoreVertical size={17} strokeWidth={2} />
                      </button>
                    </div>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      {!data.cms_items?.length ? <p className="doc-empty-visual admin-cms-empty-api">{t('admin.cmsEmpty')}</p> : null}

      <div id="admin-cms-form" className="cms-form admin-cms-form admin-card-form">
        <h3 className="admin-cms-form-title">{t('admin.cmsEditSection')}</h3>
        <input placeholder={t('admin.cmsKind')} value={form.kind} onChange={(ev) => setForm({ ...form, kind: ev.target.value })} />
        <input placeholder={t('admin.cmsTitlePh')} value={form.title} onChange={(ev) => setForm({ ...form, title: ev.target.value })} />
        <textarea
          placeholder={t('admin.cmsBody')}
          value={form.body}
          onChange={(ev) => setForm({ ...form, body: ev.target.value })}
          rows={4}
        />
        <label className="admin-field-block">
          <span>{t('admin.cmsFormStatus')}</span>
          <select value={form.status} onChange={(ev) => setForm({ ...form, status: ev.target.value })}>
            <option value="published">{t('admin.statusPublished')}</option>
            <option value="draft">{t('admin.statusDraft')}</option>
          </select>
        </label>
        <div className="cms-form-actions">
          <button type="button" onClick={save}>
            {t('admin.cmsSave')}
          </button>
          <button
            type="button"
            className="secondary-b"
            onClick={() => setForm({ id: '', kind: 'termino', title: '', body: '', status: 'published' })}
          >
            {t('admin.cmsClear')}
          </button>
        </div>
      </div>
      <section className="admin-submissions-panel">
        <h3>{t('admin.submissionsTitle')}</h3>
        {!submissions.length ? <p className="doc-empty-visual">{t('admin.submissionsEmpty')}</p> : null}
        {submissions.map((s) => (
          <article key={s.id} className="admin-submission-item">
            <div>
              <strong>
                [{s.status}] {s.title}
              </strong>
              <p>
                {s.kind} · Docente: {s.teacher_name}
              </p>
              <small>
                Nasa: {s.nasa_yuwe || '—'} | Español: {s.espanol || '—'}
              </small>
            </div>
            <div className="admin-submission-actions">
              <button type="button" disabled={s.status !== 'pending'} onClick={() => reviewSubmission(s.id, 'approve')}>
                {t('admin.approve')}
              </button>
              <button type="button" className="secondary-b" disabled={s.status !== 'pending'} onClick={() => reviewSubmission(s.id, 'reject')}>
                {t('admin.reject')}
              </button>
            </div>
          </article>
        ))}
      </section>
      {cmsPreview ? (
        <div className="admin-modal">
          <div className="admin-modal-inner admin-modal-inner--wide">
            <h3>{cmsPreview.title}</h3>
            <p className="admin-preview-meta">
              <span className="admin-code-pill">{cmsPreview.kind}</span>
            </p>
            <textarea readOnly rows={14} value={cmsPreview.body} className="admin-cms-preview-body" />
            <div className="modal-actions-row">
              <button type="button" className="secondary-b" onClick={() => setCmsPreview(null)}>
                {t('teacher.cancel')}
              </button>
            </div>
          </div>
        </div>
      ) : null}
    </div>
  )
}

export function AdminStatsPanel({ t }) {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''
  const [dash, setDash] = useState(null)
  const [dashLoading, setDashLoading] = useState(true)
  const [dashErr, setDashErr] = useState(false)

  useEffect(() => {
    let cancelled = false
    setDashLoading(true)
    setDashErr(false)
    getAdminStatsDash(token)
      .then((d) => {
        if (!cancelled) {
          setDash(d)
          setDashLoading(false)
          setDashErr(false)
        }
      })
      .catch(() => {
        if (!cancelled) {
          setDash(null)
          setDashLoading(false)
          setDashErr(true)
        }
      })
    return () => {
      cancelled = true
    }
  }, [token])

  if (dashLoading) {
    return (
      <div className="page-shell adm-shell stats-dash">
        <p className="adm-empty-msg">{t('admin.statsLoading')}</p>
      </div>
    )
  }

  if (dashErr) {
    return (
      <div className="page-shell adm-shell stats-dash">
        <p className="adm-empty-msg">{t('admin.statsLoadErr')}</p>
      </div>
    )
  }

  if (dash?.empty) {
    return (
      <div className="page-shell adm-shell stats-dash">
        <p className="adm-empty-msg">{dash.message}</p>
      </div>
    )
  }

  const p = dash?.platform ?? {
    usuarios_registrados: 0,
    estudiantes: 0,
    docentes: 0,
    administradores: 0,
    cuentas_activas: 0,
  }
  const c = dash?.corpus ?? { entradas: 0, categorias: 0 }
  const exportPayload = dash ?? { platform: p, corpus: c }

  return (
    <div className="page-shell adm-shell stats-dash admin-reportes">
      <header className="page-title admin-panel-head">
        <div>
          <h2>{t('admin.statsTitle')}</h2>
          <p>{t('admin.statsSub')}</p>
        </div>
      </header>

      <section className="stats-grid-mini admin-stat-cards admin-reportes-metrics">
        <article className="stat-card stat-card--rich">
          <span className="stat-card-icon" aria-hidden>
            <UsersRound size={20} />
          </span>
          <span>{t('admin.sUsers')}</span>
          <strong>{p.usuarios_registrados}</strong>
        </article>
        <article className="stat-card stat-card--rich">
          <span className="stat-card-icon" aria-hidden>
            <UserCheck size={20} />
          </span>
          <span>{t('admin.sStudent')}</span>
          <strong>{p.estudiantes}</strong>
        </article>
        <article className="stat-card stat-card--rich">
          <span className="stat-card-icon" aria-hidden>
            <GraduationCap size={20} />
          </span>
          <span>{t('admin.sTeacher')}</span>
          <strong>{p.docentes}</strong>
        </article>
        <article className="stat-card stat-card--rich">
          <span className="stat-card-icon" aria-hidden>
            <ShieldCheck size={20} />
          </span>
          <span>{t('admin.sAdmin')}</span>
          <strong>{p.administradores}</strong>
        </article>
        <article className="stat-card stat-card--rich">
          <span className="stat-card-icon" aria-hidden>
            <TrendingUp size={20} />
          </span>
          <span>{t('admin.sActive')}</span>
          <strong>{p.cuentas_activas}</strong>
        </article>
      </section>

      <div className="admin-reportes-split">
        <section className="role-panel admin-chart-panel">
          <div className="role-panel-head">
            <h3>{t('admin.statsChartTitle')}</h3>
          </div>
          <AdminPlatformLineChart t={t} usageSeries={dash?.usage_series} />
        </section>
        <section className="role-panel admin-corpus-card">
          <div className="role-panel-head">
            <h3>{t('admin.corpusBlock')}</h3>
          </div>
          <div className="admin-corpus-stats-body">
            <p>
              <strong>{c.entradas}</strong> {t('admin.cEntries').toLowerCase()}
            </p>
            <p>
              <strong>{c.categorias}</strong> {t('admin.cCats').toLowerCase()}
            </p>
            <p className="admin-corpus-note">{t('admin.statsExportHint')}</p>
          </div>
        </section>
      </div>

      <footer className="admin-export-footer">
        <button
          type="button"
          className="admin-toolbar-primary stats-export-btn"
          onClick={() => {
            const blob = new Blob([JSON.stringify(exportPayload, null, 2)], { type: 'application/json' })
            const a = document.createElement('a')
            a.href = URL.createObjectURL(blob)
            a.download = 'estadisticas-avi.json'
            a.click()
          }}
        >
          <BarChart3 size={17} strokeWidth={2.2} /> {t('admin.exportJson')}
        </button>
      </footer>
    </div>
  )
}
