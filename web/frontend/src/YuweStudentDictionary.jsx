import { useCallback, useEffect, useMemo, useState } from 'react'
import { getDictionary, getDictionaryFull, getStats, submitTeacherContent } from './api'
import { DictionaryTermImage } from './DictionaryTermImage'
import {
  bumpDictionaryImagePriority,
  prefetchDictionaryImages,
  preloadDictionaryImageLinks,
} from './dictionaryImagePrefetch'
import { examplePhrases, phoneticHint, speakText } from './corpusUtils'
import {
  buildDictCategoryOptions,
  categoryDisplayLabel,
  categoryMatchesRow,
  dedupeCatalogByTermId,
  isHiddenDictCategory,
  mergeCatalogRows,
  resolveDictSemanticSlug,
} from './dictionaryCatalogUtils'
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

/** Una fila del listado (termino + categoria semantica para filtros). */
function rowFromLexTerm(term, categoryTag) {
  const row = {
    id: term.id,
    nasa_yuwe: term.nasa_yuwe,
    espanol: term.espanol,
    fuente_nombre: term.fuente_nombre,
    categoria: term.categoria || '',
    image_url: term.image_url || '',
  }
  const cat = String(categoryTag ?? term.categoria ?? 'general').trim() || 'general'
  return { term: row, category: cat }
}

/** Intenta /api/dictionary/full con topes decrecientes (evita timeout en produccion). */
async function fetchFullLexiconLadder() {
  for (const lim of [12000, 8000, 5000, 3000, 1500]) {
    try {
      const pack = await getDictionaryFull(lim)
      const terms = pack.terms || []
      if (terms.length) {
        return terms.map((term) => rowFromLexTerm(term, String(term.categoria || 'general').trim() || 'general'))
      }
    } catch {
      /* siguiente tope */
    }
  }
  return []
}

/** Une varias categorias; cada peticion aislada para que un fallo no vacie todo el diccionario. */
async function mergeCategoryChunks(catList, perCatLimit) {
  const uniq = [...new Set(catList.map((c) => String(c || '').trim()).filter(Boolean))]
  if (!uniq.length) return []
  const chunks = await Promise.all(
    uniq.map((c) =>
      getDictionary(c, perCatLimit)
        .then((d) => (d.terms || []).map((term) => rowFromLexTerm(term, c)))
        .catch(() => []),
    ),
  )
  return dedupeCatalogByTermId(chunks.flat())
}

function dedupeCatalogRows(a, b) {
  return mergeCatalogRows(a, b)
}

export function StudentDictionaryRoute({
  t,
  notify,
  navigateHome,
  category: appCategory,
  setCategory: setAppCategory,
  categories: appCategories,
  preferredTab,
  onPreferredTabConsumed,
  userRole,
}) {
  const fallbackCats = useMemo(
    () => ['comida', 'alimentos', 'animales', 'familia_personas', 'numeros'],
    [],
  )
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
  const [showPropose, setShowPropose] = useState(true)
  const [submission, setSubmission] = useState({
    kind: 'termino',
    title: '',
    espanol: '',
    nasa_yuwe: '',
    translation: '',
    image_url: '',
    audio_url: '',
    notes: '',
  })
  const [submittingWord, setSubmittingWord] = useState(false)
  const isTeacher = userRole === 'docente'
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('avi-session-token') : ''

  const catFingerprint = useMemo(() => catOptions.join('\0'), [catOptions])

  useEffect(() => {
    if (!preferredTab) return
    if (preferredTab === 'categoria' && appCategory) {
      setSemanticSlug(resolveDictSemanticSlug(appCategory))
    }
    onPreferredTabConsumed?.()
  }, [preferredTab, appCategory, onPreferredTabConsumed])

  useEffect(() => {
    if (semanticSlug !== 'todas' && isHiddenDictCategory(semanticSlug)) {
      setSemanticSlug('todas')
    }
  }, [semanticSlug, catalog])

  const dictCategoryOptions = useMemo(() => buildDictCategoryOptions(catalog), [catalog])

  useEffect(() => {
    let cancelled = false
    async function loadCatalog() {
      setLoading(true)
      try {
        let merged = await fetchFullLexiconLadder()

        if (!merged.length) {
          let statsCats = []
          try {
            const st = await getStats()
            const dist = st?.category_distribution || {}
            statsCats = Object.keys(dist)
              .filter((k) => typeof k === 'string' && k.trim() && (dist[k] || 0) > 0)
              .sort((a, b) => (dist[b] || 0) - (dist[a] || 0))
          } catch {
            /* ignore */
          }
          const mergedCats = []
          const pushCat = (c) => {
            const s = String(c || '').trim()
            if (!s || mergedCats.includes(s)) return
            mergedCats.push(s)
          }
          for (const c of statsCats.slice(0, 28)) pushCat(c)
          for (const c of catOptions) pushCat(c)
          const fetchCats = mergedCats.length ? mergedCats : catOptions
          const perCatLimit = fetchCats.length > 14 ? 220 : 500
          merged = await mergeCategoryChunks(fetchCats, perCatLimit)
        }

        if (!cancelled && merged.length < 12) {
          try {
            const st = await getStats()
            const dist = st?.category_distribution || {}
            const allCats = Object.keys(dist)
              .filter((k) => typeof k === 'string' && k.trim() && (dist[k] || 0) > 0)
              .sort((a, b) => (dist[b] || 0) - (dist[a] || 0))
            const extra = await mergeCategoryChunks(allCats.slice(0, 24), 0)
            merged = dedupeCatalogRows(merged, extra)
          } catch {
            /* ignore */
          }
        }

        if (cancelled) return
        setCatalog(dedupeCatalogByTermId(merged))
        if (!cancelled && merged.length === 0) {
          notify(t('dict.loadEmpty'))
        }
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
  }, [catFingerprint, notify, t])

  const filtered = useMemo(() => {
    let out = catalog
    if (semanticSlug !== 'todas') {
      const narrowed = out.filter((r) => categoryMatchesRow(r.category, semanticSlug))
      out = narrowed.length ? narrowed : out
    }
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

  const pageImageSources = useMemo(
    () => pageSlice.map((r) => r.term.image_url).filter(Boolean),
    [pageSlice],
  )

  /** Precarga: primero las de la página visible (orden del listado), luego la página siguiente en segundo plano. */
  useEffect(() => {
    if (loading || !pageImageSources.length) return undefined
    let cancelled = false
    const urgent = listMode === 'list' ? 4 : 12
    void prefetchDictionaryImages(pageImageSources, { urgentCount: urgent, concurrency: 6 }).then(() => {
      if (cancelled) return
      const start = pageSafe * pageSize
      const nextUrls = filtered
        .slice(start, start + pageSize)
        .map((r) => r.term.image_url)
        .filter(Boolean)
      if (nextUrls.length) {
        void prefetchDictionaryImages(nextUrls, { urgentCount: 0, concurrency: 4 })
      }
    })
    const cleanupPreload = preloadDictionaryImageLinks(pageImageSources, listMode === 'list' ? 3 : 6)
    return () => {
      cancelled = true
      cleanupPreload()
    }
  }, [pageImageSources, pageSafe, pageSize, filtered, loading, listMode])

  useEffect(() => {
    if (!selected?.term?.image_url) return undefined
    const heroSrc = selected.term.image_url
    const relatedSrc = catalog
      .filter((r) => r.category === selected.category && r.term.id !== selected.term.id && r.term.image_url)
      .slice(0, 6)
      .map((r) => r.term.image_url)
    void prefetchDictionaryImages([heroSrc, ...relatedSrc], { urgentCount: 4, concurrency: 4 })
    return preloadDictionaryImageLinks([heroSrc, ...relatedSrc], 4)
  }, [selected, catalog])

  const openRow = useCallback(
    (row) => {
      if (row.term.image_url) bumpDictionaryImagePriority(row.term.image_url)
      setSelected(row)
      setAppCategory?.(row.category)
    },
    [setAppCategory],
  )

  const prefetchPage = useCallback(
    (pageNum) => {
      const start = (pageNum - 1) * pageSize
      const urls = filtered
        .slice(start, start + pageSize)
        .map((r) => r.term.image_url)
        .filter(Boolean)
      if (urls.length) void prefetchDictionaryImages(urls, { urgentCount: 6, concurrency: 6 })
    },
    [filtered, pageSize],
  )

  async function sendWordProposal(ev) {
    ev.preventDefault()
    if (!submission.title.trim() && !submission.nasa_yuwe.trim()) {
      notify(t('teacher.submissionNeedTitle'))
      return
    }
    setSubmittingWord(true)
    try {
      await submitTeacherContent(token, {
        ...submission,
        title: (submission.title || submission.nasa_yuwe).trim(),
      })
      setSubmission({
        kind: 'termino',
        title: '',
        espanol: '',
        nasa_yuwe: '',
        translation: '',
        image_url: '',
        audio_url: '',
        notes: '',
      })
      notify(t('teacher.submissionSentOk'))
      setShowPropose(false)
    } catch (e) {
      notify(e.message || String(e))
    } finally {
      setSubmittingWord(false)
    }
  }

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
    const relatedPool = catalog.filter((r) => {
      if (r.term.id === sel.id) return false
      if (isHiddenDictCategory(selCat)) return Boolean(r.term.image_url)
      return categoryMatchesRow(r.category, selCat)
    })
    const related = [...relatedPool.filter((r) => r.term.image_url), ...relatedPool.filter((r) => !r.term.image_url)].slice(
      0,
      6,
    )

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
              {sel.image_url ? (
                <DictionaryTermImage
                  src={sel.image_url}
                  alt={`Ilustración: ${cleanWord(sel.espanol)}`}
                  className="yuwe-dict-hero-img dict-gallery-img"
                  variant="hero"
                  priority="high"
                />
              ) : null}

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
                  {related.map((r, relIdx) => (
                    <button key={`${r.term.id}-${r.category}`} type="button" className="yuwe-dict-related-chip" onClick={() => openRow(r)}>
                      {r.term.image_url ? (
                        <DictionaryTermImage
                          src={r.term.image_url}
                          alt=""
                          className="yuwe-dict-related-thumb-img"
                          variant="thumb"
                          priority={relIdx < 2 ? 'high' : 'low'}
                        />
                      ) : null}
                      <span className="yuwe-dict-related-chip-body">
                        <strong>{cleanWord(r.term.nasa_yuwe)}</strong>
                        <small>{cleanWord(r.term.espanol)}</small>
                      </span>
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
                <p>
                  {categoryDisplayLabel(selCat)
                    ? `Vocabulario del ámbito «${categoryDisplayLabel(selCat)}» vinculado con territorio y memoria lingüística.`
                    : 'Entrada del léxico general del corpus AVI, útil en conversación y actividades guiadas.'}
                </p>
              </article>
              <article className="yuwe-dict-meta-card">
                <h4>Categoría temática</h4>
                <p>{categoryDisplayLabel(selCat) || 'Todas (léxico general)'}</p>
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
            <span>Categoría gramatical</span>
            <select value={grammarFilter} onChange={(e) => setGrammarFilter(e.target.value)}>
              <option value="todos">Todas</option>
              <option value="Sustantivo">Sustantivo</option>
              <option value="Verbo">Verbo</option>
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

          {isTeacher ? (
            <section className="yuwe-dict-propose-section">
              <button
                type="button"
                className="yuwe-dict-propose-toggle"
                onClick={() => setShowPropose((v) => !v)}
                aria-expanded={showPropose}
              >
                <BookOpen size={16} aria-hidden /> {t('teacher.proposeSectionTitle')}
              </button>
              {showPropose ? (
                <form className="yuwe-dict-propose-form" onSubmit={sendWordProposal}>
                  <p className="yuwe-dict-propose-hint">{t('teacher.proposeSectionHint')}</p>
                  <label className="yuwe-dict-field">
                    <span>{t('teacher.proposePhTitle')}</span>
                    <input
                      value={submission.title}
                      onChange={(e) => setSubmission((s) => ({ ...s, title: e.target.value }))}
                      placeholder={t('teacher.proposePhTitle')}
                    />
                  </label>
                  <label className="yuwe-dict-field">
                    <span>{t('teacher.proposePhEspanol')}</span>
                    <input
                      value={submission.espanol}
                      onChange={(e) => setSubmission((s) => ({ ...s, espanol: e.target.value }))}
                      placeholder={t('teacher.proposePhEspanol')}
                    />
                  </label>
                  <label className="yuwe-dict-field">
                    <span>{t('teacher.proposePhNasa')}</span>
                    <input
                      value={submission.nasa_yuwe}
                      onChange={(e) => setSubmission((s) => ({ ...s, nasa_yuwe: e.target.value }))}
                      placeholder={t('teacher.proposePhNasa')}
                      required
                    />
                  </label>
                  <label className="yuwe-dict-field">
                    <span>{t('teacher.proposePhTrans')}</span>
                    <input
                      value={submission.translation}
                      onChange={(e) => setSubmission((s) => ({ ...s, translation: e.target.value }))}
                      placeholder={t('teacher.proposePhTrans')}
                    />
                  </label>
                  <label className="yuwe-dict-field">
                    <span>{t('teacher.proposePhImg')}</span>
                    <input
                      type="url"
                      value={submission.image_url}
                      onChange={(e) => setSubmission((s) => ({ ...s, image_url: e.target.value }))}
                      placeholder="https://…/imagen.png"
                    />
                  </label>
                  <label className="yuwe-dict-field">
                    <span>{t('teacher.proposePhAudio')}</span>
                    <input
                      type="url"
                      value={submission.audio_url}
                      onChange={(e) => setSubmission((s) => ({ ...s, audio_url: e.target.value }))}
                      placeholder="https://…/audio.mp3"
                    />
                  </label>
                  <label className="yuwe-dict-field">
                    <span>{t('teacher.proposePhNotes')}</span>
                    <textarea
                      value={submission.notes}
                      onChange={(e) => setSubmission((s) => ({ ...s, notes: e.target.value }))}
                      placeholder={t('teacher.proposePhNotes')}
                      rows={2}
                    />
                  </label>
                  <button type="submit" className="yuwe-dict-propose-submit" disabled={submittingWord}>
                    {submittingWord ? t('teacher.sending') : t('teacher.proposeSubmitBtn')}
                  </button>
                </form>
              ) : null}
            </section>
          ) : null}

          <section className="yuwe-dict-sem-group">
            <h4>Categorías temáticas</h4>
            <p className="yuwe-dict-sem-hint">«Todas» muestra el léxico completo. Elige un tema para acotar.</p>
            <div className="yuwe-dict-chip-list">
              <button
                type="button"
                className={`yuwe-dict-chip${semanticSlug === 'todas' ? ' active' : ''}`}
                onClick={() => setSemanticSlug('todas')}
              >
                <LayoutGrid size={16} aria-hidden />
                <span className="yuwe-dict-chip-label">Todas</span>
                <span className="yuwe-dict-chip-count">{catalog.length}</span>
              </button>
              {dictCategoryOptions.map((opt, idx) => {
                const Ico = CATEGORY_ROW_ICONS[idx % CATEGORY_ROW_ICONS.length]
                return (
                  <button
                    key={opt.slug}
                    type="button"
                    className={`yuwe-dict-chip${semanticSlug === opt.slug ? ' active' : ''}`}
                    onClick={() => setSemanticSlug(opt.slug)}
                  >
                    <Ico size={16} aria-hidden />
                    <span className="yuwe-dict-chip-label">{opt.label}</span>
                    <span className="yuwe-dict-chip-count">{opt.count}</span>
                  </button>
                )
              })}
            </div>
          </section>
        </aside>

        <div className="yuwe-dict-main">
          <div className="yuwe-dict-toolbar">
            <div className="yuwe-dict-count-block">
              <p className="yuwe-dict-count">
                {semanticSlug !== 'todas' ? (
                  <>
                    <strong>{filtered.length}</strong> en {categoryDisplayLabel(semanticSlug)}
                  </>
                ) : filterQuery.trim() || grammarFilter !== 'todos' ? (
                  <>
                    <strong>{filtered.length}</strong> de {catalog.length} palabras
                  </>
                ) : (
                  <>
                    <strong>{catalog.length}</strong> palabras en el diccionario
                  </>
                )}
              </p>
              {totalPages > 1 ? (
                <p className="yuwe-dict-page-hint">
                  Página {pageSafe} de {totalPages}
                </p>
              ) : null}
            </div>
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
                {pageSlice.map((row, cardIdx) => {
                  const g = grammarRoleSpanish(row.term.espanol)
                  const hasImg = Boolean(row.term.image_url)
                  const catLabel = categoryDisplayLabel(row.category)
                  const imgPriority = cardIdx < 8 ? 'high' : cardIdx < 16 ? 'auto' : 'low'
                  return (
                    <button
                      key={`${row.term.id}-${row.category}`}
                      type="button"
                      className={`yuwe-dict-word-card${hasImg ? ' yuwe-dict-word-card--has-img' : ''}`}
                      onClick={() => openRow(row)}
                      onMouseEnter={() => {
                        if (row.term.image_url) bumpDictionaryImagePriority(row.term.image_url)
                      }}
                      onFocus={() => {
                        if (row.term.image_url) bumpDictionaryImagePriority(row.term.image_url)
                      }}
                    >
                      {hasImg ? (
                        <DictionaryTermImage
                          src={row.term.image_url}
                          alt={`Ilustración: ${cleanWord(row.term.espanol)}`}
                          variant="card"
                          priority={imgPriority}
                        />
                      ) : (
                        <div className="yuwe-dict-card-img yuwe-dict-card-img--text-only" aria-hidden>
                          <span>{cleanWord(row.term.nasa_yuwe).charAt(0)}</span>
                        </div>
                      )}
                      <div className="yuwe-dict-card-body">
                        <strong>{cleanWord(row.term.nasa_yuwe)}</strong>
                        <small className="yuwe-dict-card-es">{cleanWord(row.term.espanol)}</small>
                        <div className="yuwe-dict-card-meta">
                          <span className="yuwe-dict-card-pos">{g}</span>
                          {catLabel ? <span className="yuwe-dict-card-cat">{catLabel}</span> : null}
                          <span className="yuwe-dict-card-audio-pair">
                            <span title="Esp">
                              <Volume2 size={14} aria-hidden />
                            </span>
                            <span title="Ny">
                              <Volume2 size={14} aria-hidden />
                            </span>
                          </span>
                        </div>
                      </div>
                    </button>
                  )
                })}
              </div>

              {!pageSlice.length ? <p className="yuwe-dict-empty">Sin resultados para los filtros actuales.</p> : null}

              {totalPages > 1 ? (
                <nav className="yuwe-dict-pagination" aria-label="Paginación">
                  <button type="button" disabled={pageSafe <= 1} onClick={() => setPage((p) => Math.max(1, p - 1))} onMouseEnter={() => prefetchPage(pageSafe - 1)}>
                    Anterior
                  </button>
                  <div className="yuwe-dict-page-nums">
                    {pageNumbers.map((n) => (
                      <button
                        key={n}
                        type="button"
                        className={n === pageSafe ? 'current' : ''}
                        onClick={() => setPage(n)}
                        onMouseEnter={() => prefetchPage(n)}
                      >
                        {n}
                      </button>
                    ))}
                    {totalPages > lastNum ? <span aria-hidden>…</span> : null}
                  </div>
                  <button type="button" disabled={pageSafe >= totalPages} onClick={() => setPage((p) => Math.min(totalPages, p + 1))} onMouseEnter={() => prefetchPage(pageSafe + 1)}>
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
