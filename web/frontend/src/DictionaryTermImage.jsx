import { useEffect, useRef, useState } from 'react'
import { apiAssetUrl } from './api'
import {
  isDictionaryImageCached,
  markDictionaryImageLoaded,
} from './dictionaryImagePrefetch'

/**
 * Ilustración del corpus: una sola petición por imagen (sin prefetch + img duplicado).
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
  const eager = priority === 'high'
  const [inView, setInView] = useState(eager)
  const [ready, setReady] = useState(() => Boolean(src && isDictionaryImageCached(src)))
  const [failed, setFailed] = useState(false)

  useEffect(() => {
    if (eager) {
      setInView(true)
      return undefined
    }
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

  useEffect(() => {
    if (!src || !url || failed || !inView || ready) return undefined
    if (isDictionaryImageCached(src)) {
      setReady(true)
    }
    return undefined
  }, [src, url, failed, inView, ready])

  if (!url) return null

  const showSkeleton = inView && !ready && !failed
  const startLoad = inView && !failed

  const handleLoad = () => {
    markDictionaryImageLoaded(url)
    setReady(true)
  }

  const bindImgRef = (el) => {
    if (el?.complete && el.naturalWidth > 0) handleLoad()
  }

  const img = startLoad ? (
    <img
      ref={bindImgRef}
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

  if (variant === 'card') {
    return (
      <div ref={wrapRef} className="yuwe-dict-card-img">
        {placeholder}
        {missing}
        {img}
      </div>
    )
  }
  if (variant === 'hero') {
    return (
      <div ref={wrapRef} className="yuwe-dict-hero-visual">
        {placeholder}
        {missing}
        {img}
      </div>
    )
  }
  if (variant === 'thumb') {
    return (
      <span ref={wrapRef} className="yuwe-dict-related-thumb">
        {placeholder}
        {missing}
        {img}
      </span>
    )
  }

  if (!startLoad && !showSkeleton && !failed) {
    return <span ref={wrapRef} className="yuwe-dict-img-io-anchor" aria-hidden />
  }
  return (
    <span ref={wrapRef} className="yuwe-dict-img-io-wrap">
      {placeholder}
      {missing}
      {img}
    </span>
  )
}
