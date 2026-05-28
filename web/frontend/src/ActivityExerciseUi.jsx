import { CheckCircle, XCircle } from 'lucide-react'
import { ActivityOptionVisual, ActivityQuestionImage } from './ActivityMedia'
import { getActivityExerciseLayout } from './activityExerciseLayout'

function cleanCue(value) {
  return String(value || '—').replace(/^(el|la|los|las|un|una|unos|unas)\s+/i, '').trim() || '—'
}

/** Bloque superior: imagen / pista / frase segun tipo de ejercicio. */
export function ActivityExercisePrompt({ q, t, spanishCue, classPrefix = 'practice' }) {
  const layout = getActivityExerciseLayout(q)
  const es = cleanCue(q?.espanol || spanishCue)
  const instruction = t(layout.instructionKey)

  if (layout.type === 'completar') {
    return (
      <div className={`${classPrefix}-complete-cue`}>
        <p className={`${classPrefix}-cue-word`}>{es}</p>
        <p className={`${classPrefix}-subq`}>{instruction}</p>
        <p className={`${classPrefix}-prompt-fine`}>{q?.prompt}</p>
        <p className={`${classPrefix}-blank-line`} aria-hidden>
          _____
        </p>
      </div>
    )
  }

  if (layout.type === 'imagen') {
    return (
      <div className={`${classPrefix}-imagen-wrap`}>
        {layout.showPromptImage ? (
          <ActivityQuestionImage
            src={q.image_url}
            alt=""
            className={classPrefix === 'act' ? 'quiz-img' : `${classPrefix}-imagen`}
          />
        ) : (
          <p className={`${classPrefix}-subq`}>{t('practice.imageUnavailable')}</p>
        )}
        <p className={`${classPrefix}-subq`}>{instruction}</p>
      </div>
    )
  }

  /* quiz */
  if (layout.showPromptImage) {
    return (
      <div className={`${classPrefix}-quiz-visual`}>
        <ActivityQuestionImage
          src={q.image_url}
          alt={es ? `Ilustración: ${es}` : ''}
          className={classPrefix === 'act' ? 'quiz-img' : `${classPrefix}-imagen`}
        />
        <p className={`${classPrefix}-cue-word`}>{es}</p>
        <p className={`${classPrefix}-subq`}>{instruction}</p>
      </div>
    )
  }

  return (
    <div className={`${classPrefix}-spotlight`}>
      <div className={`${classPrefix}-spotlight-body`}>
        <p className={`${classPrefix}-cue-word`}>{es}</p>
        <p className={`${classPrefix}-subq`}>{instruction}</p>
        {q?.prompt ? <p className={`${classPrefix}-prompt-fine`}>{q.prompt}</p> : null}
      </div>
    </div>
  )
}

/** Opciones de respuesta: siempre texto; icono solo si no hay modo visual de opciones. */
export function ActivityExerciseOptions({
  q,
  chosen,
  revealed,
  onPick,
  stringsEqual,
  category,
  variant = 'practice',
}) {
  const layout = getActivityExerciseLayout(q)
  const showOptImages = layout.showOptionImages && q?.option_images && Object.keys(q.option_images).length > 0

  if (variant === 'act') {
    return (
      <div className={['answers-grid', 'act-answers', showOptImages ? 'act-answers--visual' : ''].filter(Boolean).join(' ')}>
        {(q?.options || []).map((opt, optIdx) => (
          <button
            type="button"
            key={`${q.id}-opt-${optIdx}`}
            disabled={revealed}
            className={[
              'answer-chip',
              revealed && stringsEqual(opt, q.answer) ? 'correct' : '',
              revealed && chosen === opt && !stringsEqual(opt, q.answer) ? 'incorrect' : '',
            ]
              .filter(Boolean)
              .join(' ')}
            onClick={() => onPick(opt)}
          >
            {opt}
          </button>
        ))}
      </div>
    )
  }

  return (
    <div
      className={['practice-opt-grid', showOptImages ? 'practice-opt-grid--visual' : 'practice-opt-grid--text-only']
        .filter(Boolean)
        .join(' ')}
    >
      {(q?.options || []).map((opt, opi) => (
        <button
          type="button"
          key={`${q.id}-popt-${opi}`}
          disabled={revealed}
          className={[
            'practice-opt',
            showOptImages ? '' : 'practice-opt--text-only',
            revealed && stringsEqual(opt, q.answer) ? 'practice-opt-correct' : '',
            revealed && chosen === opt && !stringsEqual(opt, q.answer) ? 'practice-opt-wrong' : '',
          ]
            .filter(Boolean)
            .join(' ')}
          onClick={() => onPick(opt)}
        >
          {showOptImages ? (
            <span className="practice-opt-icon">
              <ActivityOptionVisual
                optionText={opt}
                optionImages={q.option_images}
                category={category}
                imgClassName="practice-opt-thumb"
                iconClassName="practice-opt-icon-svg"
              />
            </span>
          ) : null}
          <span className="practice-opt-label">{opt}</span>
          {revealed && stringsEqual(opt, q.answer) ? (
            <CheckCircle className="practice-opt-check" size={22} aria-hidden />
          ) : null}
          {revealed && chosen === opt && !stringsEqual(opt, q.answer) ? (
            <XCircle className="practice-opt-x" size={22} aria-hidden />
          ) : null}
        </button>
      ))}
    </div>
  )
}
