/**
 * Reglas de presentacion por tipo de actividad del API.
 * - quiz: imagen del termino (si existe) + opciones solo texto (reto).
 * - imagen: unir ilustracion con palabra Nasa; sin pista en espanol.
 * - completar: frase con hueco; sin imagenes.
 */
export function getActivityExerciseLayout(q) {
  const type = String(q?.type || 'quiz').toLowerCase()
  if (type === 'completar') {
    return {
      type,
      showPromptImage: false,
      showOptionImages: false,
      showSpanishCue: true,
      instructionKey: 'practice.qGrammarBlank',
    }
  }
  if (type === 'imagen') {
    return {
      type,
      showPromptImage: Boolean(q?.image_url),
      showOptionImages: false,
      showSpanishCue: false,
      instructionKey: 'practice.qMatchImageOnly',
    }
  }
  return {
    type: 'quiz',
    showPromptImage: Boolean(q?.image_url),
    showOptionImages: false,
    showSpanishCue: true,
    instructionKey: q?.image_url ? 'practice.qWhichNasaForWord' : 'practice.qPickNasa',
  }
}

export function activityInstructionKey(q, tabId, practiceQuestionCopyKey) {
  const layout = getActivityExerciseLayout(q)
  if (q?.type === 'quiz' || q?.type === 'imagen' || q?.type === 'completar') {
    return layout.instructionKey
  }
  return practiceQuestionCopyKey(tabId, q?.type)
}
