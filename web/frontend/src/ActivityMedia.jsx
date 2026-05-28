import { apiAssetUrl } from './api'
import {
  BookOpen,
  Droplet,
  Flame,
  House,
  Leaf,
  Mountain,
  Sprout,
  Trees,
  UsersRound,
  Wheat,
} from 'lucide-react'

/** Icono de respaldo alineado con la categoria del ejercicio (no iconos genericos al azar). */
export function getActivityCategoryIcon(category) {
  const c = String(category || '')
    .trim()
    .toLowerCase()
    .replace(/\s+/g, '_')
  if (!c) return Leaf
  if (c.includes('comida') || c.includes('alimento') || c.includes('fruta') || c.includes('verdura')) return Wheat
  if (c.includes('animal')) return Sprout
  if (c.includes('familia') || c.includes('persona')) return UsersRound
  if (c.includes('casa') || c.includes('objeto')) return House
  if (c.includes('numero') || c.includes('color')) return BookOpen
  if (c.includes('agua') || c.includes('ambient') || c.includes('elemento')) return Droplet
  if (c.includes('fuego') || c.includes('tiempo')) return Flame
  if (c.includes('planta') || c.includes('naturaleza')) return Trees
  if (c.includes('tierra') || c.includes('cerro') || c.includes('mont')) return Mountain
  return Leaf
}

export function ActivityQuestionImage({ src, alt = '', className = 'quiz-img' }) {
  const url = apiAssetUrl(src)
  if (!url) return null
  return (
    <img
      src={url}
      alt={alt}
      className={className}
      loading="eager"
      fetchPriority="high"
      decoding="async"
    />
  )
}

/**
 * Miniatura del corpus para una opcion Nasa, o icono tematico si no hay PNG local.
 */
export function ActivityOptionVisual({
  optionText,
  optionImages,
  category,
  iconClassName = 'practice-opt-icon-svg',
  imgClassName = 'practice-opt-thumb',
}) {
  const src = optionImages?.[optionText]
  if (src) {
    const url = apiAssetUrl(src)
    if (url) {
      return <img src={url} alt="" className={imgClassName} loading="lazy" decoding="async" />
    }
  }
  const Icon = getActivityCategoryIcon(category)
  return <Icon className={iconClassName} size={22} strokeWidth={2.1} aria-hidden />
}
