-- Esquema PostgreSQL equivalente al SQLite de YuweAI (server.py / auth_migrate_tables).
-- Ejecutar en Supabase: SQL Editor > New query > pegar y Run.
-- Tras esto, la app aún debe migrarse de sqlite3 a psycopg en código; este archivo prepara la BD.

CREATE EXTENSION IF NOT EXISTS citext;

CREATE TABLE IF NOT EXISTS users (
    id BIGSERIAL PRIMARY KEY,
    email CITEXT NOT NULL UNIQUE,
    password_hash TEXT,
    google_sub TEXT UNIQUE,
    display_name TEXT NOT NULL,
    role TEXT NOT NULL,
    created_at DOUBLE PRECISION NOT NULL,
    active SMALLINT NOT NULL DEFAULT 1,
    email_verified SMALLINT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS sessions (
    token TEXT PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at DOUBLE PRECISION NOT NULL,
    expires_at DOUBLE PRECISION NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_sessions_exp ON sessions(expires_at);

CREATE TABLE IF NOT EXISTS password_resets (
    email CITEXT PRIMARY KEY,
    code TEXT NOT NULL,
    expires_at DOUBLE PRECISION NOT NULL,
    created_at DOUBLE PRECISION NOT NULL
);

CREATE TABLE IF NOT EXISTS grades (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    level TEXT NOT NULL DEFAULT 'General',
    active SMALLINT NOT NULL DEFAULT 1,
    created_at DOUBLE PRECISION NOT NULL
);

CREATE TABLE IF NOT EXISTS teacher_groups (
    id BIGSERIAL PRIMARY KEY,
    teacher_user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    education_level TEXT,
    grade TEXT,
    difficulty_default TEXT,
    created_at DOUBLE PRECISION NOT NULL,
    grade_id BIGINT REFERENCES grades(id) ON DELETE SET NULL
);
CREATE INDEX IF NOT EXISTS idx_groups_teacher ON teacher_groups(teacher_user_id);

CREATE TABLE IF NOT EXISTS group_members (
    group_id BIGINT NOT NULL REFERENCES teacher_groups(id) ON DELETE CASCADE,
    student_user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    assigned_at DOUBLE PRECISION NOT NULL,
    PRIMARY KEY (group_id, student_user_id)
);
CREATE INDEX IF NOT EXISTS idx_members_student ON group_members(student_user_id);

CREATE TABLE IF NOT EXISTS cms_items (
    id BIGSERIAL PRIMARY KEY,
    kind TEXT NOT NULL,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    updated_at DOUBLE PRECISION NOT NULL
);

CREATE TABLE IF NOT EXISTS student_grades (
    student_user_id BIGINT PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    grade_id BIGINT NOT NULL REFERENCES grades(id) ON DELETE RESTRICT,
    assigned_at DOUBLE PRECISION NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_student_grades_grade ON student_grades(grade_id);

CREATE TABLE IF NOT EXISTS student_settings (
    student_user_id BIGINT PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    language TEXT NOT NULL DEFAULT 'Espanol',
    theme TEXT NOT NULL DEFAULT 'Claro Nasa',
    level TEXT NOT NULL DEFAULT 'Intermedio',
    goal TEXT NOT NULL DEFAULT 'Conversacion fluida',
    reminders SMALLINT NOT NULL DEFAULT 1,
    notif_daily SMALLINT NOT NULL DEFAULT 1,
    notif_content SMALLINT NOT NULL DEFAULT 1,
    notif_streak SMALLINT NOT NULL DEFAULT 1,
    notif_tips SMALLINT NOT NULL DEFAULT 0,
    consent_given SMALLINT NOT NULL DEFAULT 1,
    updated_at DOUBLE PRECISION NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS learning_activities (
    id BIGSERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    mode TEXT NOT NULL,
    creator_user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    creator_role TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'active',
    created_at DOUBLE PRECISION NOT NULL,
    updated_at DOUBLE PRECISION NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_activities_creator ON learning_activities(creator_user_id);

CREATE TABLE IF NOT EXISTS activity_assignments (
    id BIGSERIAL PRIMARY KEY,
    activity_id BIGINT NOT NULL REFERENCES learning_activities(id) ON DELETE CASCADE,
    grade_id BIGINT REFERENCES grades(id) ON DELETE SET NULL,
    group_id BIGINT REFERENCES teacher_groups(id) ON DELETE SET NULL,
    student_user_id BIGINT REFERENCES users(id) ON DELETE SET NULL,
    assigned_by_user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    assigned_at DOUBLE PRECISION NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_activity_assignments_activity ON activity_assignments(activity_id);
CREATE INDEX IF NOT EXISTS idx_activity_assignments_grade ON activity_assignments(grade_id);
CREATE INDEX IF NOT EXISTS idx_activity_assignments_group ON activity_assignments(group_id);

CREATE TABLE IF NOT EXISTS content_submissions (
    id BIGSERIAL PRIMARY KEY,
    teacher_user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    kind TEXT NOT NULL,
    title TEXT NOT NULL,
    espanol TEXT,
    nasa_yuwe TEXT,
    translation TEXT,
    image_url TEXT,
    audio_url TEXT,
    notes TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    review_notes TEXT,
    reviewed_by_user_id BIGINT REFERENCES users(id) ON DELETE SET NULL,
    created_at DOUBLE PRECISION NOT NULL,
    reviewed_at DOUBLE PRECISION
);
CREATE INDEX IF NOT EXISTS idx_content_submissions_status ON content_submissions(status);

CREATE TABLE IF NOT EXISTS admin_audit_log (
    id BIGSERIAL PRIMARY KEY,
    created_at DOUBLE PRECISION NOT NULL,
    actor_user_id BIGINT REFERENCES users(id) ON DELETE SET NULL,
    actor_name TEXT NOT NULL,
    action TEXT NOT NULL,
    detail TEXT NOT NULL DEFAULT ''
);
CREATE INDEX IF NOT EXISTS idx_audit_created ON admin_audit_log(created_at);

CREATE TABLE IF NOT EXISTS admin_mail_messages (
    id BIGSERIAL PRIMARY KEY,
    created_at DOUBLE PRECISION NOT NULL,
    subject TEXT NOT NULL,
    body TEXT NOT NULL DEFAULT '',
    audience TEXT NOT NULL DEFAULT 'all',
    state TEXT NOT NULL DEFAULT 'Entregado'
);

CREATE TABLE IF NOT EXISTS admin_support_tickets (
    id BIGSERIAL PRIMARY KEY,
    created_at DOUBLE PRECISION NOT NULL,
    topic TEXT NOT NULL,
    requester_name TEXT NOT NULL DEFAULT '',
    requester_email TEXT,
    priority TEXT NOT NULL DEFAULT 'Media',
    state TEXT NOT NULL DEFAULT 'Abierto',
    created_by_user_id BIGINT REFERENCES users(id) ON DELETE SET NULL
);
