/** Base del API. En dev suele ir vacío (proxy Vite a :8090). En prod, si falta VITE_API_BASE en el build, se usa el host Render por defecto. */
const DEFAULT_PROD_API = 'https://yuweai-avi-api.onrender.com'
const _rawBase = (import.meta.env.VITE_API_BASE ?? '').toString().trim().replace(/\/+$/, '')
const API_BASE =
  _rawBase ||
  (import.meta.env.PROD ? DEFAULT_PROD_API : '')

export class ApiError extends Error {
  constructor(message, status) {
    super(message)
    this.name = 'ApiError'
    this.status = status
  }
}

async function parseJsonSafe(response) {
  const text = await response.text()
  const trimmed = text.trimStart()
  const looksJson = trimmed.startsWith('{') || trimmed.startsWith('[')
  if (!looksJson && trimmed.startsWith('<')) {
    return { __htmlError: true, status: response.status }
  }
  if (!text) return {}
  try {
    return JSON.parse(text)
  } catch {
    return {}
  }
}

function throwIfHtmlPayload(data, response) {
  if (data && data.__htmlError) {
    throw new ApiError(
      'El servidor devolvio HTML en lugar de JSON. Revisa VITE_API_BASE o que el API AVI este activo.',
      data.status || response.status || 502,
    )
  }
}

async function request(path) {
  const response = await fetch(`${API_BASE}${path}`)
  const text = await response.text()
  const trimmed = text.trimStart()
  const looksJson = trimmed.startsWith('{') || trimmed.startsWith('[')
  if (!looksJson && trimmed.startsWith('<')) {
    throw new ApiError(
      'El servidor devolvio HTML en lugar de JSON. Revisa VITE_API_BASE o que el API AVI este activo.',
      response.status || 502,
    )
  }
  let data = {}
  try {
    data = trimmed ? JSON.parse(text) : {}
  } catch {
    throw new ApiError(`Respuesta no valida (${response.status}).`, response.status)
  }
  if (!response.ok) {
    throw new ApiError(data.error || `Error ${response.status}`, response.status)
  }
  return data
}

async function postJson(path, body, token = null) {
  const headers = { 'Content-Type': 'application/json; charset=utf-8' }
  if (token) {
    headers.Authorization = `Bearer ${token}`
  }
  const response = await fetch(`${API_BASE}${path}`, {
    method: 'POST',
    headers,
    body: JSON.stringify(body ?? {}),
  })
  const data = await parseJsonSafe(response)
  throwIfHtmlPayload(data, response)
  if (!response.ok) {
    throw new ApiError(data.error || `Error ${response.status}`, response.status)
  }
  return data
}

async function getJsonAuthorized(path, token) {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: token ? { Authorization: `Bearer ${token}` } : {},
  })
  const data = await parseJsonSafe(response)
  throwIfHtmlPayload(data, response)
  if (!response.ok) {
    throw new ApiError(data.error || `Error ${response.status}`, response.status)
  }
  return data
}

export function getHealth() {
  return request('/api/health')
}

export function getStats() {
  return request('/api/stats')
}

export function searchAVI(query, topK = 5) {
  return request(`/api/search?q=${encodeURIComponent(query)}&top_k=${topK}`)
}

/**
 * @param limit 0 = todas las entradas lexico de la categoria (servidor).
 *   Por omision, un tope moderado por si se llama sin argumento.
 */
export function getDictionary(category, limit = 200) {
  return request(`/api/dictionary?category=${encodeURIComponent(category)}&limit=${limit}`)
}

/** Todos los términos léxicos del corpus (una petición; tope en servidor). */
export function getDictionaryFull(limit = 25000) {
  return request(`/api/dictionary/full?limit=${encodeURIComponent(String(limit))}`)
}

export function getActivity(category, limit = 6) {
  return request(`/api/activity?category=${encodeURIComponent(category)}&limit=${limit}`)
}

export function getDialogues(category, limit = 6) {
  return request(`/api/dialogues?category=${encodeURIComponent(category)}&limit=${limit}`)
}

/**
 * Imagen educativa (Wikimedia Commons vía backend).
 */
export function getImage(query, category = '', termId = '') {
  const q = encodeURIComponent(query || '')
  const c = encodeURIComponent(category || '')
  const id = (termId || '').trim()
  const idq = id ? `&id=${encodeURIComponent(id)}` : ''
  return request(`/api/image?q=${q}&category=${c}${idq}`)
}

/** ---------- Autenticación ---------- */

export function fetchAuthConfig() {
  return request('/api/auth/config')
}

/** Registro: ya no devuelve token; el usuario debe iniciar sesión después. */
export function authRegister(body) {
  return postJson('/api/auth/register', body)
}

/** @returns {{ token: string, user: { id, email, display_name, role } }} */
export function authLogin(body) {
  return postJson('/api/auth/login', body)
}

/**
 * credential: JWT de Google Identity Services
 * role: estudiante | docente | administrador (obligatorio para cuentas nuevas)
 */
export function authGoogle(body) {
  return postJson('/api/auth/google', body)
}

export function authMe(token) {
  return getJsonAuthorized('/api/auth/me', token)
}

export async function authLogout(token) {
  await postJson('/api/auth/logout', {}, token)
}

export function postAuthorized(path, token, body) {
  return postJson(path, body ?? {}, token)
}

export function dictionarySearch(q) {
  return request(`/api/dictionary/search?q=${encodeURIComponent(q)}`)
}

export function getActivityAdv(category, limit, difficulty, mode) {
  const c = encodeURIComponent(category || '')
  return request(
    `/api/activity?category=${c}&limit=${limit}&difficulty=${encodeURIComponent(difficulty || 'intermedio')}&mode=${encodeURIComponent(mode || 'quiz')}`,
  )
}

export function getTeacherGroups(token) {
  return getJsonAuthorized('/api/teacher/groups', token)
}

export function getTeacherStudents(token, q = '') {
  return getJsonAuthorized(`/api/teacher/students?q=${encodeURIComponent(q)}`, token)
}

export function getTeacherGroupReport(token, groupId) {
  return getJsonAuthorized(`/api/teacher/group-report?group_id=${encodeURIComponent(groupId)}`, token)
}

export function getTeacherGrades(token) {
  return getJsonAuthorized('/api/teacher/grades', token)
}

export function getTeacherActivities(token) {
  return getJsonAuthorized('/api/teacher/activities', token)
}

/** @param days 7 | 30 | 90 */
export function getTeacherReportsSummary(token, days = 30) {
  return getJsonAuthorized(`/api/teacher/reports-summary?days=${encodeURIComponent(String(days))}`, token)
}

export function updateTeacherActivity(token, body) {
  return postJson('/api/teacher/activity-update', body, token)
}

export function postTeacherGroupUnassign(token, body) {
  return postJson('/api/teacher/group-unassign', body, token)
}

export function createTeacherActivity(token, body) {
  return postJson('/api/teacher/activities', body, token)
}

export function submitTeacherContent(token, body) {
  return postJson('/api/teacher/content-submit', body, token)
}

export function getAdminUsers(token) {
  return getJsonAuthorized('/api/admin/users', token)
}

export function getAdminCms(token) {
  return getJsonAuthorized('/api/admin/cms', token)
}

export function getAdminStatsDash(token) {
  return getJsonAuthorized('/api/admin/stats-dash', token)
}

export function getAdminGrades(token) {
  return getJsonAuthorized('/api/admin/grades', token)
}

export function saveAdminGrade(token, body) {
  return postJson('/api/admin/grades', body, token)
}

export function deleteAdminGrade(token, gradeId) {
  return postJson('/api/admin/grade-delete', { id: gradeId }, token)
}

export function assignStudentGrade(token, studentUserId, gradeId) {
  return postJson('/api/admin/student-grade-assign', { student_user_id: studentUserId, grade_id: gradeId }, token)
}

export function getAdminContentSubmissions(token) {
  return getJsonAuthorized('/api/admin/content-submissions', token)
}

export function reviewAdminContentSubmission(token, body) {
  return postJson('/api/admin/content-review', body, token)
}

export function getAdminGroups(token) {
  return getJsonAuthorized('/api/admin/groups', token)
}

export function getAdminAudit(token) {
  return getJsonAuthorized('/api/admin/audit', token)
}

export function getAdminMailHistory(token) {
  return getJsonAuthorized('/api/admin/mail-history', token)
}

export function postAdminMailSend(token, body) {
  return postJson('/api/admin/mail-send', body, token)
}

export function getAdminSupportTickets(token) {
  return getJsonAuthorized('/api/admin/support-tickets', token)
}

export function postAdminSupportTicket(token, body) {
  return postJson('/api/admin/support-ticket', body, token)
}

export function postAdminUserCreate(token, body) {
  return postJson('/api/admin/user-create', body, token)
}

export function getStudentProfileSchool(token) {
  return getJsonAuthorized('/api/student/profile-school', token)
}

export function getStudentActivities(token) {
  return getJsonAuthorized('/api/student/activities', token)
}

export function getStudentSettings(token) {
  return getJsonAuthorized('/api/student/settings', token)
}

export function saveStudentSettings(token, body) {
  return postJson('/api/student/settings', body, token)
}

export function getTeacherMessagingState(token) {
  return getJsonAuthorized('/api/teacher/messaging-state', token)
}

export function saveTeacherMessagingState(token, body) {
  return postJson('/api/teacher/messaging-state', body, token)
}

export function getStudentSessions(token) {
  return getJsonAuthorized('/api/student/sessions', token)
}

export function changeStudentPassword(token, body) {
  return postJson('/api/student/change-password', body, token)
}

export function deleteStudentAccount(token) {
  return postJson('/api/student/delete-account', {}, token)
}

export function authForgotPassword(body) {
  return postJson('/api/auth/forgot-password', body)
}

export function authVerifyResetCode(body) {
  return postJson('/api/auth/verify-reset-code', body)
}

export function authResetPassword(body) {
  return postJson('/api/auth/reset-password', body)
}
