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
  return a
}

/** Una entrada por término (evita 3922 duplicados por categoría repetida). */
export function dedupeCatalogByTermId(rows) {
  const byId = new Map()
  for (const row of rows || []) {
    const id = row?.term?.id
    if (id == null || id === '') continue
    const prev = byId.get(id)
    if (!prev) byId.set(id, row)
    else byId.set(id, pickPreferredCatalogRow(prev, row))
  }
  return [...byId.values()]
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
