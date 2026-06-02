/** Categorías “cajón” que no se muestran como filtro (equivale a «Todas»). */
export const HIDDEN_DICT_CATEGORIES = new Set(['general', 'diccionario_general', 'vocabulario_general'])

const CATEGORY_LABELS = {
  alimentos: 'Alimentos',
  animales: 'Animales',
  casa: 'Casa',
  colores: 'Colores',
  comida: 'Comida',
  cuerpo_partes: 'Cuerpo',
  cultura: 'Cultura',
  dias_semana: 'Días de la semana',
  elementos_agua: 'Agua y naturaleza',
  familia_personas: 'Familia y personas',
  frutas_verduras: 'Frutas y verduras',
  lugares: 'Lugares',
  meses: 'Meses',
  naturaleza: 'Naturaleza',
  numeros: 'Números',
  objetos: 'Objetos',
  plantas: 'Plantas',
  ropa: 'Ropa',
  saludos: 'Saludos',
  tiempo: 'Tiempo',
  transporte: 'Transporte',
  verbos: 'Verbos',
}

export function normalizeDictCategory(cat) {
  return String(cat || '')
    .trim()
    .toLowerCase()
    .replace(/\s+/g, '_')
    .replace(/_+/g, '_')
}

export function isHiddenDictCategory(cat) {
  return HIDDEN_DICT_CATEGORIES.has(normalizeDictCategory(cat))
}

/** Nasa Yuwe normalizado (sin guiones iniciales, minúsculas). */
export function normalizeNasaYuwe(ny) {
  return String(ny || '')
    .trim()
    .toLowerCase()
    .replace(/^[-\s]+/, '')
}

/** Español núcleo: sin artículo, sin paréntesis, primera acepción. */
export function coreSpanishGloss(espanol) {
  let t = String(espanol || '')
    .trim()
    .toLowerCase()
  t = t.replace(/\([^)]*\)/g, ' ')
  t = t.replace(/^(el|la|los|las|un|una|unos|unas)\s+/i, '')
  t = t.replace(/[.,;:!?]+/g, ' ')
  t = t.replace(/\s+/g, ' ')
    .trim()
  if (t.includes(',')) t = t.split(',')[0].trim()
  return t
}

/** Clave para fusionar entradas duplicadas (Am/am + Hacha/el hacha). */
export function termSemanticKey(row) {
  const t = row?.term || row
  const ny = normalizeNasaYuwe(t?.nasa_yuwe)
  const es = coreSpanishGloss(t?.espanol)
  if (!ny || !es) return ''
  return `${ny}|${es}`
}

function idRank(id) {
  const s = String(id || '')
  if (s.startsWith('LEX-')) return 2
  if (s.startsWith('LEXR-')) return 1
  return 0
}

function formatCategorySlug(slug) {
  if (!slug) return 'Sin categoría'
  return slug
    .split('_')
    .filter(Boolean)
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(' ')
}

/** Etiqueta legible para UI; vacío si es categoría oculta. */
export function categoryDisplayLabel(cat) {
  const k = normalizeDictCategory(cat)
  if (isHiddenDictCategory(k)) return ''
  return CATEGORY_LABELS[k] || formatCategorySlug(k)
}

function categoryRank(cat) {
  return isHiddenDictCategory(cat) ? 0 : 1
}

export function pickPreferredCatalogRow(a, b) {
  const ra = categoryRank(a.category)
  const rb = categoryRank(b.category)
  if (ra !== rb) return ra > rb ? a : b
  if (Boolean(a.term.image_url) !== Boolean(b.term.image_url)) {
    return a.term.image_url ? a : b
  }
  const ida = idRank(a.term.id)
  const idb = idRank(b.term.id)
  if (ida !== idb) return ida > idb ? a : b
  const la = String(a.term.espanol || '').length
  const lb = String(b.term.espanol || '').length
  if (la !== lb) return la < lb ? a : b
  const nya = String(a.term.nasa_yuwe || '')
  const nyb = String(b.term.nasa_yuwe || '')
  if (nya && nyb && nya !== nyb) {
    if (nya[0] === nya[0]?.toUpperCase() && nyb[0] !== nyb[0]?.toUpperCase()) return a
    if (nyb[0] === nyb[0]?.toUpperCase() && nya[0] !== nya[0]?.toUpperCase()) return b
  }
  return a
}

/** Una entrada por término: por id y por clave semántica (evita Am/am duplicados). */
export function dedupeCatalogByTermId(rows) {
  const byId = new Map()
  for (const row of rows || []) {
    const id = row?.term?.id
    if (id == null || id === '') continue
    const prev = byId.get(id)
    if (!prev) byId.set(id, row)
    else byId.set(id, pickPreferredCatalogRow(prev, row))
  }
  const bySem = new Map()
  for (const row of byId.values()) {
    const sem = termSemanticKey(row)
    const key = sem || `__id__:${row.term.id}`
    const prev = bySem.get(key)
    if (!prev) bySem.set(key, row)
    else bySem.set(key, pickPreferredCatalogRow(prev, row))
  }
  return [...bySem.values()]
}

export function mergeCatalogRows(a, b) {
  return dedupeCatalogByTermId([...(a || []), ...(b || [])])
}

export function buildDictCategoryOptions(catalog) {
  const counts = new Map()
  for (const row of catalog || []) {
    const k = normalizeDictCategory(row.category)
    if (isHiddenDictCategory(k)) continue
    counts.set(k, (counts.get(k) || 0) + 1)
  }
  return [...counts.entries()]
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0], 'es', { sensitivity: 'base' }))
    .map(([slug, count]) => ({
      slug,
      count,
      label: categoryDisplayLabel(slug),
    }))
}

export function categoryMatchesRow(rowCat, slug) {
  const a = normalizeDictCategory(rowCat)
  const b = normalizeDictCategory(slug)
  if (!b || b === 'todas') return true
  if (a === b) return true
  if (b === 'comida' && (a === 'alimentos' || a === 'frutas_verduras' || a === 'comida')) return true
  if (b === 'alimentos' && (a === 'comida' || a === 'frutas_verduras' || a === 'alimentos')) return true
  return false
}

export function resolveDictSemanticSlug(slug) {
  const k = normalizeDictCategory(slug)
  if (!k || k === 'todas' || isHiddenDictCategory(k)) return 'todas'
  return k
}
