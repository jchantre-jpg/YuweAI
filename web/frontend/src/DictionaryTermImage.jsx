import { useEffect, useRef, useState } from 'react'
import { apiAssetUrl } from './api'
import {
  isDictionaryImageCached,
  markDictionaryImageLoaded,
} from './dictionaryImagePrefetch'

/** Clasifica la imagen y devuelve clase + aspect-ratio del contenedor. */
function measureImageFit(naturalWidth, naturalHeight) {
  if (!naturalWidth || !naturalHeight) {
    return { fitClass: 'yuwe-dict-img--square', aspectRatio: 1 }
  }
  const ratio = naturalWidth / naturalHeight
  if (ratio >= 1.12) {
    return {
      fitClass: 'yuwe-dict-img--wide',
      aspectRatio: Math.min(1.9, Math.max(1.08, ratio)),
    }
  }
  if (ratio <= 0.88) {
    return {
      fitClass: 'yuwe-dict-img--tall',
      aspectRatio: Math.max(0.58, Math.min(0.92, ratio)),
    }
  }
  return { fitClass: 'yuwe-dict-img--square', aspectRatio: 1 }
}

function wrapClass(variant, fitClass) {
  if (variant === 'card') return `yuwe-dict-card-img${fitClass ? ` ${fitClass}` : ''}`
  if (variant === 'hero') return `yuwe-dict-hero-visual${fitClass ? ` ${fitClass}` : ''}`
  if (variant === 'thumb') return `yuwe-dict-related-thumb${fitClass ? ` ${fitClass}` : ''}`
  return 'yuwe-dict-img-io-wrap'
}

/**
 * Ilustración del corpus: el marco se adapta a la proporción real (sin recortar).
 */
export function DictionaryTermImage({
  src,
  alt = '',
  className = 'dict-gallery-img',
  priority = 'auto',
  variant = 'inline',
  rootMargin = '280px',
}) {
  const url = apiAssetUrl(src)
  const wrapRef = useRef(null)
  const imgRef = useRef(null)
  const metricsDoneRef = useRef(false)
  const eager = priority === 'high'
  const [inView, setInView] = useState(eager)
  const [ready, setReady] = useState(() => Boolean(src && isDictionaryImageCached(src)))
  const [failed, setFailed] = useState(false)
  const [fit, setFit] = useState({ fitClass: '', aspectRatio: null })

  useEffect(() => {
    metricsDoneRef.current = false
    setFit({ fitClass: '', aspectRatio: null })
    setFailed(false)
    setReady(Boolean(src && isDictionaryImageCached(src)))
    if (!eager) setInView(false)
    else setInView(true)
  }, [src, eager])

  useEffect(() => {
    if (eager) return undefined
    const el = wrapRef.current
    if (!el) return undefined
    const margin = priority === 'low' ? '80px' : rootMargin
    const io = new IntersectionObserver(
      ([entry]) => {
        if (entry?.isIntersecting) setInView(true)
      },
      { rootMargin: margin, threshold: 0.01 },
    )
    io.observe(el)
    return () => io.disconnect()
  }, [eager, priority, rootMargin, src])

  const applyImageMetrics = (imgEl) => {
    if (!imgEl?.naturalWidth || metricsDoneRef.current) return
    metricsDoneRef.current = true
    setFit(measureImageFit(imgEl.naturalWidth, imgEl.naturalHeight))
    markDictionaryImageLoaded(url)
    setReady(true)
  }

  const handleLoad = (e) => {
    applyImageMetrics(e?.target)
  }

  useEffect(() => {
    if (!inView || failed || ready) return undefined
    const el = imgRef.current
    if (el?.complete && el.naturalWidth > 0) applyImageMetrics(el)
    return undefined
  }, [inView, failed, ready, url])

  if (!url) return null

  const showSkeleton = inView && !ready && !failed
  const startLoad = inView && !failed

  const wrapStyle =
    fit.aspectRatio && variant !== 'thumb'
      ? { aspectRatio: String(fit.aspectRatio) }
      : undefined

  const img = startLoad ? (
    <img
      ref={imgRef}
      src={url}
      alt={alt}
      className={`${className} yuwe-dict-img-ready${ready ? ' is-visible' : ''}`.trim()}
      loading={eager ? 'eager' : 'lazy'}
      fetchPriority={priority === 'high' ? 'high' : priority === 'low' ? 'low' : 'auto'}
      decoding="async"
      onLoad={handleLoad}
      onError={() => setFailed(true)}
    />
  ) : null

  const placeholder = showSkeleton ? (
    <div className="yuwe-dict-img-skeleton" aria-hidden>
      <span className="yuwe-dict-img-skeleton-shimmer" />
    </div>
  ) : null

  const missing = failed ? (
    <div className="yuwe-dict-img-missing" aria-hidden title="Ilustración no disponible">
      <span>◌</span>
    </div>
  ) : null

  const wrapCls = wrapClass(variant, fit.fitClass)

  if (variant === 'card' || variant === 'hero' || variant === 'thumb') {
    return (
      <div ref={wrapRef} className={wrapCls} style={wrapStyle}>
        {placeholder}
        {missing}
        {img}
      </div>
    )
  }

  if (!startLoad && !showSkeleton && !failed) {
    return <span ref={wrapRef} className="yuwe-dict-img-io-anchor" aria-hidden />
  }
  return (
    <span ref={wrapRef} className={wrapCls} style={wrapStyle}>
      {placeholder}
      {missing}
      {img}
    </span>
  )
}
