import { useState } from 'react'
import { apiAssetUrl } from './api'

/**
 * Ilustracion del corpus (generadas-img-ia-solo). Si no hay src o falla la carga, no renderiza nada.
 */
export function DictionaryTermImage({ src, alt = '', className = 'dict-gallery-img' }) {
  const [failed, setFailed] = useState(false)
  const url = apiAssetUrl(src)
  if (!url || failed) return null
  return (
    <img
      src={url}
      alt={alt}
      className={className}
      loading="lazy"
      decoding="async"
      onError={() => setFailed(true)}
    />
  )
}
