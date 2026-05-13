import { useCallback, useEffect, useMemo, useState } from 'react'
import { getDictionary } from './api'
import { examplePhrases, phoneticHint, speakText } from './corpusUtils'
import { DictionaryTermImage } from './dictionaryTerm'
import {
  ArrowLeft,
  Bookmark,
  Download,
  LayoutGrid,
  Leaf,
  List,
  MapPin,
  MessageCircle,
  Search,
  Share2,
  Sprout,
  UsersRound,
  Volume2,
  BookOpen,
} from 'lucide-react'

function labelSlug(value) {
  return String(value || '').replaceAll('_', ' ')
}

function titleLabel(value) {
  const cl = labelSlug(value)
  return cl ? cl.charAt(0).toUpperCase() + cl.slice(1) : 'Categoría'
}

function cleanWord(value) {
  return String(value || '—').replace(/^(el|la|los|las|un|una|unos|unas)\s+/i, '').trim() || '—'
}

function grammarRoleSpanish(espanol) {
  const w = String(espanol || '').trim().split(/\s+/)[0] || ''
  const lw = w.toLowerCase()
  if (lw.length >= 4 && /(ar|er|ir)$/.test(lw.replace(/[^a-záéíóúñü]/gi, ''))) return 'Verbo'
  return 'Sustantivo'
}

function frequencyTier(id) {
  const seed = typeof id === 'number' ? id : String(id || '').length * 97
  return Math.max(3, Math.min(5, 3 + (seed % 3)))
}

const CATEGORY_ROW_ICONS = [Sprout, UsersRound, Leaf, BookOpen, MapPin]

export function StudentDictionaryRoute({
  t,
  notify,
  navigateHome,
  category: appCategory,
  setCategory: setAppCategory,
  categories: appCategories,
  preferredTab,
  onPreferredTabConsumed,
}) {
  const fallbackCats = useMemo(() => {
    try {
      const raw = JSON.parse(window.localStorage.getItem('avi-last-categories') || '[]')
      const base = Array.isArray(raw) && raw.length ? raw : ['comida', 'alimentos', 'animales', 'familia_personas', 'numeros']
      return ['comida', ...base.filter((c) => c !== 'comida')].slice(0, 40)
    } catch {
      return ['comida', 'alimentos', 'animales', 'familia_personas', 'numeros']
    }
  }, [])
  const catOptions = appCategories?.length ? appCategories : fallbackCats

  const [catalog, setCatalog] = useState([])
  const [loading, setLoading] = useState(true)
  const [filterQuery, setFilterQuery] = useState('')
  const [grammarFilter, setGrammarFilter] = useState('todos')
  const [semanticSlug, setSemanticSlug] = useState('todas')
  const [sortBy, setSortBy] = useState('nasa')
  const [page, setPage] = useState(1)
  const [pageSize, setPageSize] = useState(12)
  const [listMode, setListMode] = useState('grid')
  const [selected, setSelected] = useState(null)

  const catFingerprint = useMemo(() => catOptions.join('\0'), [catOptions])

  useEffect(() => {
    if (!preferredTab) return
    if (preferredTab === 'categoria' && appCategory) setSemanticSlug(appCategory)
    onPreferredTabConsumed?.()
  }, [preferredTab, appCategory, onPreferredTabConsumed])

  useEffect(() => {
    let cancelled = false
    async function loadCatalog() {
      setLoading(true)
      try {
        const chunks = await Promise.all(
          catOptions.map((c) =>
            getDictionary(c, 96).then((d) =>
              (d.terms || []).map((term) => ({
                term,
                category: c,
              })),
            ),
          ),
        )
        if (cancelled) return
        const seen = new Set()
        const merged = []
        for (const part of chunks) {
          for (const row of part) {
            const k = `${row.term.id}-${row.category}`
            if (seen.has(k)) continue
            seen.add(k)
            merged.push(row)
          }
        }
        setCatalog(merged)
      } catch (e) {
        if (!cancelled) {
          notify(e.message || String(e))
          setCatalog([])
        }
      } finally {
        if (!cancelled) setLoading(false)
      }
    }
    loadCatalog()
    return () => {
      cancelled = true
    }
  }, [catFingerprint, notify])

  const filtered = useMemo(() => {
    let out = catalog
    if (semanticSlug !== 'todas') out = out.filter((r) => r.category === semanticSlug)
    const q = filterQuery.trim().toLowerCase()
    if (q) {
      out = out.filter((r) => {
        const ny = String(r.term.nasa_yuwe || '').toLowerCase()
        const es = String(r.term.espanol || '').toLowerCase()
        return ny.includes(q) || es.includes(q)
      })
    }
    if (grammarFilter !== 'todos') {
      out = out.filter((r) => grammarRoleSpanish(r.term.espanol) === grammarFilter)
    }
    const sorted = [...out]
    const cmpNasa = (a, b) =>
      cleanWord(a.term.nasa_yuwe).localeCompare(cleanWord(b.term.nasa_yuwe), 'es', { sensitivity: 'base' })
    const cmpEs = (a, b) =>
      cleanWord(a.term.espanol).localeCompare(cleanWord(b.term.espanol), 'es', { sensitivity: 'base' })
    sorted.sort(sortBy === 'es' ? cmpEs : cmpNasa)
    return sorted
  }, [catalog, semanticSlug, filterQuery, grammarFilter, sortBy])

  const totalPages = Math.max(1, Math.ceil(filtered.length / pageSize))
  const pageSafe = Math.min(page, totalPages)

  useEffect(() => setPage(1), [filterQuery, grammarFilter, semanticSlug, sortBy, pageSize])

  const pageSlice = useMemo(() => {
    const start = (pageSafe - 1) * pageSize
    return filtered.slice(start, start + pageSize)
  }, [filtered, pageSafe, pageSize])

  const openRow = useCallback(
    (row) => {
      setSelected(row)
      setAppCategory?.(row.category)
    },
    [setAppCategory],
  )

  const exportDictionary = useCallback(() => {
    const header = 'nasa_yuwe,espanol,categoria,pos\n'
    const body = filtered
      .map(
        (r) =>
          `"${String(r.term.nasa_yuwe).replace(/"/g, '""')}","${String(r.term.espanol).replace(/"/g, '""')}","${r.category}","${grammarRoleSpanish(r.term.espanol)}"`,
      )
      .join('\n')
    const blob = new Blob([header + body], { type: 'text/csv;charset=utf-8' })
    const a = document.createElement('a')
    a.href = URL.createObjectURL(blob)
    a.download = 'diccionario-nasa-yuwe.csv'
    a.click()
    URL.revokeObjectURL(a.href)
    notify('Listado exportado como CSV.')
  }, [filtered, notify])

  const pageNumbers = useMemo(() => {
    const maxBtns = 5
    const nums = []
    let start = Math.max(1, pageSafe - 2)
    const endpt = Math.min(totalPages, start + maxBtns - 1)
    start = Math.max(1, endpt - maxBtns + 1)
    for (let i = start; i <= endpt; i += 1) nums.push(i)
    return nums
  }, [pageSafe, totalPages])

  const lastNum = pageNumbers.length ? pageNumbers[pageNumbers.length - 1] : 1

  if (selected) {
    const { term: sel, category: selCat } = selected
    const phrases = examplePhrases(sel.espanol, sel.nasa_yuwe, sel.id)
    const pos = grammarRoleSpanish(sel.espanol)
    const posLong = pos === 'Verbo' ? 'Verbo' : 'Sustantivo común'
    const dots = frequencyTier(sel.id)
    const related = catalog.filter((r) => r.category === selCat && r.term.id !== sel.id).slice(0, 6)

    return (
      <div className="page-shell dict-shell yuwe-dict-shell">
        <div className="yuwe-dict-detail">
          <div className="yuwe-dict-detail-toolbar">
            <button type="button" className="yuwe-dict-link-back" onClick={() => setSelected(null)}>
              <ArrowLeft size={18} aria-hidden /> Volver al listado
            </button>
            <button type="button" className="yuwe-dict-ghost-inline" onClick={navigateHome}>
              {t('student.homeBtn')}
            </button>
          </div>

          <nav className="yuwe-dict-bc" aria-label="Migas">
            <button type="button" className="yuwe-dict-bc-link" onClick={() => setSelected(null)}>
              Diccionario
            </button>
            <span aria-hidden>/</span>
            <span>{cleanWord(sel.nasa_yuwe)}</span>
          </nav>

          <div className="yuwe-dict-detail-head">
            <div className="yuwe-dict-title-block">
              <h1 className="yuwe-dict-word-title">
                <Leaf size={26} aria-hidden /> {cleanWord(sel.nasa_yuwe)}
              </h1>
              <span className="yuwe-dict-pos-pill">{pos}</span>
            </div>
            <div className="yuwe-dict-detail-actions">
              <button type="button" className="yuwe-dict-mini-btn" onClick={() => notify('Guardado próximo en tu perfil.')}>
                <Bookmark size={17} aria-hidden /> Guardar
              </button>
              <button
                type="button"
                className="yuwe-dict-mini-btn"
                onClick={() => {
                  const line = `${cleanWord(sel.nasa_yuwe)} — ${cleanWord(sel.espanol)}`
                  navigator.clipboard?.writeText?.(line).then(() => notify('Copiado al portapapeles.')).catch(() => notify('Copia manual la ficha.'))
                }}
              >
                <Share2 size={17} aria-hidden /> Compartir
              </button>
            </div>
          </div>

          <p className="yuwe-dict-def-lead">{cleanWord(sel.espanol)}.</p>

          <div className="yuwe-dict-detail-split">
            <div className="yuwe-dict-detail-maincard">
              <div className="yuwe-dict-hero-visual">
                <DictionaryTermImage term={sel} category={selCat} className="yuwe-dict-hero-img" />
                <span className="yuwe-dict-leaf-ring" aria-hidden>
                  <Leaf size={28} strokeWidth={1.5} />
                </span>
              </div>

              <div className="yuwe-dict-lang-row">
                <div className="yuwe-dict-lang-card">
                  <span className="yuwe-dict-lang-label">Español</span>
                  <strong>{cleanWord(sel.espanol)}</strong>
                  <button type="button" className="yuwe-dict-listen" onClick={() => speakText(sel.espanol, 'es')}>
                    <Volume2 size={18} aria-hidden /> Escuchar
                  </button>
                </div>
                <div className="yuwe-dict-lang-card">
                  <span className="yuwe-dict-lang-label">Nasa Yuwe</span>
                  <strong>{cleanWord(sel.nasa_yuwe)}</strong>
                  <small className="yuwe-dict-phon">{phoneticHint(sel.nasa_yuwe)}</small>
                  <button type="button" className="yuwe-dict-listen" onClick={() => speakText(sel.nasa_yuwe, 'nasa')}>
                    <Volume2 size={18} aria-hidden /> Escuchar
                  </button>
                </div>
              </div>

              <section className="yuwe-dict-example-wide">
                <div className="yuwe-dict-example-head">
                  <MessageCircle size={18} aria-hidden />
                  <h3>Ejemplo en contexto</h3>
                </div>
                <p className="yuwe-dict-example-nasa">{phrases.nasa}</p>
                <p className="yuwe-dict-example-ipa">({phoneticHint(sel.nasa_yuwe)})</p>
                <p className="yuwe-dict-example-es">{phrases.es}</p>
              </section>

              <section className="yuwe-dict-related-wrap">
                <h3>Palabras relacionadas</h3>
                <div className="yuwe-dict-related-row">
                  {related.map((r) => (
                    <button key={`${r.term.id}-${r.category}`} type="button" className="yuwe-dict-related-chip" onClick={() => openRow(r)}>
                      <strong>{cleanWord(r.term.nasa_yuwe)}</strong>
                      <small>{cleanWord(r.term.espanol)}</small>
                      <span className="yuwe-dict-related-audio">
                        <Volume2 size={14} aria-hidden />
                      </span>
                    </button>
                  ))}
                  {!related.length ? <p className="yuwe-dict-muted">Sin sugerencias adicionales en esta categoría.</p> : null}
                </div>
              </section>
            </div>

            <aside className="yuwe-dict-side-meta" aria-label="Información de la entrada">
              <article className="yuwe-dict-meta-card">
                <h4>Información cultural</h4>
                <p>Vocabulario del ámbito «{titleLabel(selCat)}» que refuerza vínculos con territorio y memoria lingüística propia.</p>
              </article>
              <article className="yuwe-dict-meta-card">
                <h4>Categoría gramatical</h4>
                <p>{posLong}</p>
              </article>
              <article className="yuwe-dict-meta-card">
                <h4>Uso</h4>
                <p>Nómbralo en conversación cotidiana, actividades guiadas en Aprender o refuerzos en Practicar.</p>
              </article>
              <article className="yuwe-dict-meta-card">
                <h4>Frecuencia</h4>
                <span className="yuwe-dict-freq-cap">{dots >= 4 ? 'Alta' : 'Media'} en AVI</span>
                <div className="yuwe-dict-dot-row" aria-hidden>
                  {[1, 2, 3, 4, 5].map((i) => (
                    <span key={i} className={`yuwe-dict-dot${i <= dots ? ' on' : ''}`} />
                  ))}
                </div>
              </article>
            </aside>
          </div>
          <div className="woven-strip woven-strip--thin yuwe-dict-woven-footer" aria-hidden />
        </div>
      </div>
    )
  }

  return (
    <div className="page-shell dict-shell yuwe-dict-shell">
      <header className="yuwe-dict-global-search">
        <div className="yuwe-dict-search-inner">
          <Search size={20} aria-hidden />
          <input
            type="search"
            value={filterQuery}
            onChange={(e) => setFilterQuery(e.target.value)}
            placeholder="Buscar palabra en Nasa Yuwe o en español..."
            aria-label="Buscar en el diccionario"
          />
        </div>
      </header>

      <div className="yuwe-dict-page-head">
        <div className="yuwe-dict-page-titles">
          <h2 className="yuwe-dict-h2">
            <span className="yuwe-dict-leaf-accent">
              <Leaf size={28} aria-hidden />
            </span>{' '}
            Diccionario Nasa Yuwe
          </h2>
          <p>{t('dict.pageSub')}</p>
        </div>
        <div className="yuwe-dict-page-actions">
          <button type="button" className="yuwe-dict-download" onClick={exportDictionary}>
            <Download size={18} aria-hidden /> Descargar diccionario
          </button>
          <button type="button" className="dict-home-btn" onClick={navigateHome}>
            {typeof t === 'function' ? t('student.homeBtn') : 'Inicio'}
          </button>
        </div>
      </div>

      <div className="yuwe-dict-split">
        <aside className="yuwe-dict-filters">
          <h3 className="yuwe-dict-filters-heading">Filtrar palabras</h3>
          <label className="yuwe-dict-field">
            <span>Búsqueda rápida</span>
            <input value={filterQuery} onChange={(e) => setFilterQuery(e.target.value)} placeholder="Texto…" />
          </label>
          <label className="yuwe-dict-field">
            <span>Categoría gramatical</span>
            <select value={grammarFilter} onChange={(e) => setGrammarFilter(e.target.value)}>
              <option value="todos">Todas</option>
              <option value="Sustantivo">Sustantivo</option>
              <option value="Verbo">Verbo</option>
            </select>
          </label>
          <label className="yuwe-dict-field">
            <span>Categoría semántica</span>
            <select value={semanticSlug} onChange={(e) => setSemanticSlug(e.target.value)}>
              <option value="todas">Todas las categorías</option>
              {catOptions.map((c) => (
                <option key={c} value={c}>
                  {titleLabel(c)}
                </option>
              ))}
            </select>
          </label>
          <label className="yuwe-dict-field">
            <span>Ordenar por</span>
            <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
              <option value="nasa">Alfabético (Nasa Yuwe)</option>
              <option value="es">Alfabético (español)</option>
            </select>
          </label>
          <button
            type="button"
            className="yuwe-dict-clear"
            onClick={() => {
              setFilterQuery('')
              setGrammarFilter('todos')
              setSemanticSlug('todas')
              setSortBy('nasa')
            }}
          >
            Limpiar filtros
          </button>

          <section className="yuwe-dict-sem-group">
            <h4>Categorías semánticas</h4>
            <div className="yuwe-dict-chip-list">
              <button type="button" className={`yuwe-dict-chip${semanticSlug === 'todas' ? ' active' : ''}`} onClick={() => setSemanticSlug('todas')}>
                <LayoutGrid size={16} aria-hidden /> Todas
              </button>
              {catOptions.slice(0, 9).map((c, idx) => {
                const Ico = CATEGORY_ROW_ICONS[idx % CATEGORY_ROW_ICONS.length]
                return (
                  <button key={c} type="button" className={`yuwe-dict-chip${semanticSlug === c ? ' active' : ''}`} onClick={() => setSemanticSlug(c)}>
                    <Ico size={16} aria-hidden /> {titleLabel(c)}
                  </button>
                )
              })}
            </div>
          </section>
        </aside>

        <div className="yuwe-dict-main">
          <div className="yuwe-dict-toolbar">
            <p className="yuwe-dict-count">
              <strong>{filtered.length}</strong> palabras encontradas
            </p>
            <div className="yuwe-dict-toolbar-tools">
              <div className="yuwe-dict-toggle" role="group" aria-label="Vista">
                <button type="button" className={listMode === 'grid' ? 'on' : ''} onClick={() => setListMode('grid')} aria-pressed={listMode === 'grid'}>
                  <LayoutGrid size={18} aria-hidden />
                </button>
                <button type="button" className={listMode === 'list' ? 'on' : ''} onClick={() => setListMode('list')} aria-pressed={listMode === 'list'}>
                  <List size={18} aria-hidden />
                </button>
              </div>
              <label className="yuwe-dict-per-page">
                <span>Por página</span>
                <select value={pageSize} onChange={(e) => setPageSize(Number(e.target.value))}>
                  <option value={8}>8</option>
                  <option value={12}>12</option>
                  <option value={16}>16</option>
                  <option value={24}>24</option>
                </select>
              </label>
            </div>
          </div>

          {loading ? (
            <p className="yuwe-dict-loading">Cargando palabras del diccionario…</p>
          ) : (
            <>
              <div className={`yuwe-dict-grid${listMode === 'list' ? ' list-mode' : ''}`}>
                {pageSlice.map((row) => {
                  const g = grammarRoleSpanish(row.term.espanol)
                  return (
                    <button key={`${row.term.id}-${row.category}`} type="button" className="yuwe-dict-word-card" onClick={() => openRow(row)}>
                      <div className="yuwe-dict-card-img">
                        <DictionaryTermImage term={row.term} category={row.category} />
                      </div>
                      <strong>{cleanWord(row.term.nasa_yuwe)}</strong>
                      <small className="yuwe-dict-card-es">{cleanWord(row.term.espanol)}</small>
                      <span className="yuwe-dict-card-pos">{g}</span>
                      <span className="yuwe-dict-card-audio-pair">
                        <span title="Esp">
                          <Volume2 size={14} aria-hidden />
                        </span>
                        <span title="Ny">
                          <Volume2 size={14} aria-hidden />
                        </span>
                      </span>
                    </button>
                  )
                })}
              </div>

              {!pageSlice.length ? <p className="yuwe-dict-empty">Sin resultados para los filtros actuales.</p> : null}

              {totalPages > 1 ? (
                <nav className="yuwe-dict-pagination" aria-label="Paginación">
                  <button type="button" disabled={pageSafe <= 1} onClick={() => setPage((p) => Math.max(1, p - 1))}>
                    Anterior
                  </button>
                  <div className="yuwe-dict-page-nums">
                    {pageNumbers.map((n) => (
                      <button key={n} type="button" className={n === pageSafe ? 'current' : ''} onClick={() => setPage(n)}>
                        {n}
                      </button>
                    ))}
                    {totalPages > lastNum ? <span aria-hidden>…</span> : null}
                  </div>
                  <button type="button" disabled={pageSafe >= totalPages} onClick={() => setPage((p) => Math.min(totalPages, p + 1))}>
                    Siguiente
                  </button>
                </nav>
              ) : null}
            </>
          )}
        </div>
      </div>

      <div className="woven-strip woven-strip--thin yuwe-dict-woven-footer" aria-hidden />
    </div>
  )
}
