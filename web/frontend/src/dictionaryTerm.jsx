import { useEffect, useState } from 'react'
import { Leaf } from 'lucide-react'
import { fetchTermImage } from './corpusUtils'

export function DictionaryTermImage({ term, category, className = '' }) {
  const [img, setImg] = useState(null)
  const [broken, setBroken] = useState(false)

  useEffect(() => {
    let cancelled = false
    setBroken(false)
    setImg(null)
    fetchTermImage(term?.espanol, term?.categoria || category).then((data) => {
      if (!cancelled) setImg(data)
    })
    return () => {
      cancelled = true
    }
  }, [term?.id, term?.espanol, term?.categoria, category])

  if (img?.ok && img.image_url && !broken) {
    return (
      <img
        src={img.image_url}
        alt=""
        className={className || 'dict-gallery-img'}
        loading="lazy"
        decoding="async"
        onError={() => setBroken(true)}
      />
    )
  }

  return (
    <div className={`${className || 'dict-gallery-img'} dict-gallery-img--empty`} aria-hidden>
      <Leaf size={42} strokeWidth={1.4} />
    </div>
  )
}
