# Estilo **solo tema** — Yuwe / Nasa Yuwe (significado fiel + fondo blanco)

## Nasa Yuwe ≠ NASA espacio

Igual que en `generadas-img-ia/ESTILO_NASA_YUWE_IA.md`: **Nasa** = pueblo y lengua **Nasa Yuwe** del **Cauca (Colombia)**. **No** la agencia aeroespacial estadounidense: sin cohetes, astronautas, trajes espaciales.

## Prioridad: **qué enseña el lema** (semántica)

- La imagen debe responder a la **gloss en español** del MD: lo que vería un niño o una niña para entender la palabra **correctamente**.
- **Acciones / verbos** (bailar, correr, escribir, lavar…): mostrar **personajes estilizados** (3D tipo Pixar) **haciendo esa acción**, con vestuario y accesorios coherentes. Ejemplo pedagógico: **«bailar»** → **dos personas bailando** con traje de baile, **no** solo un vestido y zapatos sueltos sin bailarines.
- **Animales, plantas, comidas, objetos**: mostrar **esa** entidad, reconocible y centrada.
- **Cualidades** (mojado, sucio, redondo…): un ejemplo visual **inequívoco** (charcos, manchas, bola, etc.).
- **Fondo**: **blanco sólido** `#FFFFFF` como estudio; sin paisaje, horizonte, suelo de baldosas ni patrón de transparencia.
- **Color del contenido**: **solo el fondo es blanco**. Personajes, animales, plantas, comidas, herramientas y accesorios deben ir **a color vivo y saturado** (rojos, verdes, azules, amarillos, tierras, etc. según el tema). Evitar ilustraciones **grises**, **beige** o **blanco sobre blanco** que no se distingan del fondo.

## Excepciones ya acotadas en prompts

- **`parentescos`**: una figura (busto 3D o **art toy / vinyl**) que encarne el rol familiar.
- **`nombres_propios`**: un **avatar** estilizado (sin tipografías con el nombre); ropa y piel **a color**, no apagado.

## Familia visual

- 3D estilizado, superficies suaves, luz suave, colores vivos, **no** foto stock hiperrealista.
- **Aksu** (rombos de color) opcional y discreto en ropa u objetos.
- Sin texto ni marca de agua en la imagen (categoría **nombres_propios**: sin letras con el nombre; retrato/avatar a color).
- Tono escolar, respetuoso; sin contenido sexual explícito ni violencia.

## Exportación de prompts

Los textos en inglés para IA se generan con:

`python scripts/export_prompts_solo_desde_lexico_md.py`

→ `corpus/generadas-img-ia-solo/prompts_solo_full.jsonl`

Copiar PNG generados (Cursor **assets**) al corpus:

`python scripts/sync_solo_imagenes_desde_assets.py`

## Frase base (plantilla general; ver JSONL para el resto)

La plantilla larga vive en `scripts/export_prompts_solo_desde_lexico_md.py` (`SOLO_LEXICO_SEMANTIC` + gloss). Regenera el JSONL tras cambiar reglas.
