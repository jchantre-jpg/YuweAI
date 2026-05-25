-- Persistencia unificada: ajustes extra del estudiante + estado por usuario (docente mensajes, etc.)
-- Ejecutar en Supabase si el proyecto ya existía antes de incluir estas columnas en initial_schema.

ALTER TABLE student_settings ADD COLUMN IF NOT EXISTS vocab_diary_json TEXT NOT NULL DEFAULT '{}';
ALTER TABLE student_settings ADD COLUMN IF NOT EXISTS dictionary_categories_json TEXT NOT NULL DEFAULT '[]';
ALTER TABLE student_settings ADD COLUMN IF NOT EXISTS streak_current INTEGER NOT NULL DEFAULT 0;
ALTER TABLE student_settings ADD COLUMN IF NOT EXISTS streak_last_active_ymd TEXT;
ALTER TABLE student_settings ADD COLUMN IF NOT EXISTS avi_chat_json TEXT NOT NULL DEFAULT '[]';

CREATE TABLE IF NOT EXISTS user_app_state (
    user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    namespace TEXT NOT NULL,
    payload TEXT NOT NULL DEFAULT '{}',
    updated_at DOUBLE PRECISION NOT NULL,
    PRIMARY KEY (user_id, namespace)
);
