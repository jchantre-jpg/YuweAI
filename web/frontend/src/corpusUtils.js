import { getImage } from './api'

/**
 * Traduccion pedagogica ES -> EN para la vista trilingue (cuando el corpus no trae ingles).
 */
const ES_EN = {
  agua: 'Water',
  tierra: 'Earth / Land',
  fuego: 'Fire',
  aire: 'Air',
  sol: 'Sun',
  luna: 'Moon',
  estrella: 'Star',
  arbol: 'Tree',
  flor: 'Flower',
  rio: 'River',
  montana: 'Mountain',
  cielo: 'Sky',
  nube: 'Cloud',
  lluvia: 'Rain',
  viento: 'Wind',
  dia: 'Day',
  noche: 'Night',
  casa: 'House',
  perro: 'Dog',
  gato: 'Cat',
  pajaro: 'Bird',
  pez: 'Fish',
  caballo: 'Horse',
  vaca: 'Cow',
  mano: 'Hand',
  pie: 'Foot',
  cabeza: 'Head',
  ojo: 'Eye',
  boca: 'Mouth',
  corazon: 'Heart',
  madre: 'Mother',
  padre: 'Father',
  hijo: 'Son',
  hija: 'Daughter',
  hermano: 'Brother',
  hermana: 'Sister',
  familia: 'Family',
  amigo: 'Friend',
  rojo: 'Red',
  verde: 'Green',
  azul: 'Blue',
  amarillo: 'Yellow',
  blanco: 'White',
  negro: 'Black',
  uno: 'One',
  dos: 'Two',
  tres: 'Three',
  comida: 'Food',
  pan: 'Bread',
  leche: 'Milk',
  sal: 'Greeting (context)',
  ninos: 'Children',
  nina: 'Girl',
  nino: 'Boy',
  maestro: 'Teacher',
  escuela: 'School',
  bien: 'Well / good',
  mal: 'Bad',
  grande: 'Big',
  pequeno: 'Small',
  buenos: 'Good (pl.)',
  dias: 'Days',
  noches: 'Nights',
  gracias: 'Thanks',
  hola: 'Hello',
  adios: 'Goodbye',
}

export function spanishToEnglish(espanol) {
  if (!espanol || typeof espanol !== 'string') return '—'
  const clean = espanol
    .toLowerCase()
    .replace(/[.,;:!?¿¡]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
  const noArticle = clean.replace(/^(el|la|los|las|un|una)\s+/i, '').trim()
  const first = noArticle.split(/\s+/)[0] || noArticle
  if (ES_EN[noArticle]) return ES_EN[noArticle]
  if (ES_EN[first]) return ES_EN[first]
  if (ES_EN[clean]) return ES_EN[clean]
  // Capitalize literal fallback for long phrases
  const words = noArticle.split(/\s+/).slice(0, 3)
  const mapped = words.map((w) => ES_EN[w] || w).join(' ')
  return mapped.length < 64 ? `${mapped} (EN)` : '—'
}

let synthWarned = false

export function speakText(text, mode = 'es') {
  if (typeof window === 'undefined' || !window.speechSynthesis) {
    if (!synthWarned) {
      synthWarned = true
      console.warn('Speech synthesis not available')
    }
    return false
  }
  const t = (text || '').trim()
  if (!t) return false
  window.speechSynthesis.cancel()
  const u = new SpeechSynthesisUtterance(t)
  if (mode === 'en') {
    u.lang = 'en-US'
    u.rate = 0.95
  } else if (mode === 'es') {
    u.lang = 'es-CO'
    u.rate = 0.95
  } else {
    // Nasa Yuwe: sin voz nativa; lectura lenta con fonética aproximada
    u.lang = 'es-CO'
    u.rate = 0.75
  }
  window.speechSynthesis.speak(u)
  return true
}

import { saveStudentSettings } from './api'

const _emptyDiary = () => ({ validated: 0, items: [] })

/** Sin token no hay persistencia; la fuente de verdad es el servidor (`vocab_diary` en ajustes de estudiante). */
export function loadVocabDiary() {
  return _emptyDiary()
}

export function saveVocabDiary(_diary) {
  /* Usar syncVocabDiaryToServer(token, diary) cuando exista sesión. */
}

export async function syncVocabDiaryToServer(token, diary) {
  if (!token) return
  await saveStudentSettings(token, { vocab_diary: diary })
}

export async function fetchTermImage(espanol, category, termId = '') {
  try {
    return await getImage(espanol || '', category || '', termId || '')
  } catch {
    return { ok: false }
  }
}

export function phoneticHint(text) {
  const t = String(text || '').trim()
  if (!t) return ''
  return t.length > 24 ? `${t.slice(0, 24)}…` : t
}

export function examplePhrases(espanol, nasa, id) {
  const es = String(espanol || '').trim()
  const ny = String(nasa || '').trim()
  return {
    es: es ? `Ejemplo: «${es}»` : '',
    nasa: ny ? `Nasa Yuwe: «${ny}»` : '',
  }
}

export function mergeDiaryItem(diary, entry) {
  const id = entry.id
  const items = Array.isArray(diary.items) ? [...diary.items] : []
  const ix = items.findIndex((x) => x.id === id)
  const next = { ...entry, progress: entry.progress ?? 0 }
  if (ix >= 0) {
    items[ix] = { ...items[ix], ...next, progress: Math.max(0, Math.min(100, next.progress)) }
  } else {
    items.unshift({ ...next, progress: next.progress || 0 })
  }
  const trimmed = items.slice(0, 24)
  const validated = trimmed.filter((x) => (x.progress || 0) >= 80).length
  return { ...diary, items: trimmed, validated }
}
