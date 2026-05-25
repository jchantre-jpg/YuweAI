# Corpus para YuweAI

Para **Render / Docker** (imagen en la raíz del repo `YuweAI`), el build copia:

`corpus/data/corpus_bilingue_v5.csv`

Ese fichero debe ser el **corpus bilingüe completo** (miles de filas). Si trabajas con el monorepo del grado, la fuente de verdad suele estar en `../corpus/data/corpus_bilingue_v5.csv` (carpeta `corpus` junto a `YuweAI`): cópiala aquí antes de commit o despliegue.

- Si el CSV **no** está en Git (por tamaño o privacidad), define en el build la variable **`CORPUS_URL`** con una URL de descarga directa (véase `deploy/DESPLIEGUE-GRATIS.md`).
- Si pesa mucho para Git normal, usa **Git LFS** para ese CSV.
