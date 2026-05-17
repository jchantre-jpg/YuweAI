/** Debe coincidir con la política en `server.py` (`auth_password_policy_violation`). */

const SPECIALS = new Set('!@#$%^&*()_+-=[]{};\'\\",.<>?/|`~')

export const PASSWORD_POLICY_HINT =
  'Mínimo 10 caracteres, con mayúscula, minúscula, número y un símbolo (!@#$%…).'

export function validatePasswordStrength(password) {
  const pw = String(password || '')
  const errors = []
  if (pw.length < 10) errors.push('Al menos 10 caracteres.')
  if (pw.length > 256) errors.push('Contraseña demasiado larga.')
  try {
    if (!/\p{Ll}/u.test(pw)) errors.push('Incluye al menos una letra minúscula.')
    if (!/\p{Lu}/u.test(pw)) errors.push('Incluye al menos una letra mayúscula.')
    if (!/\p{Nd}/u.test(pw)) errors.push('Incluye al menos un número.')
  } catch {
    if (!/[a-z]/.test(pw)) errors.push('Incluye al menos una letra minúscula.')
    if (!/[A-Z]/.test(pw)) errors.push('Incluye al menos una letra mayúscula.')
    if (!/\d/.test(pw)) errors.push('Incluye al menos un número.')
  }
  if (![...pw].some((c) => SPECIALS.has(c))) errors.push('Incluye al menos un símbolo (!@#$%…).')
  return errors
}

export function isPasswordStrong(password) {
  return validatePasswordStrength(password).length === 0
}
