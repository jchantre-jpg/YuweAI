-- Estado de publicación para ítems CMS (alineado con SQLite auth_migrate_tables).
ALTER TABLE cms_items ADD COLUMN IF NOT EXISTS status TEXT NOT NULL DEFAULT 'published';
