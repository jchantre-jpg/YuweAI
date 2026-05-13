# Evaluacion tecnica del modelo AVI

## Objetivo evaluado

Evaluar precision y coherencia del modelo PLN de recuperacion usado por el AVI sobre el corpus semantico Nasa Yuwe-Espanol.

## Configuracion

- Corpus cargado: **4593** registros.
- Modelo: **AVI Retrieval Model v1**.
- Filas de entrenamiento: **3673**.
- Vocabulario del modelo: **6693** terminos.
- Optimizador: `idf_overlap + mmr + ttl_cache + lexical_priority + pedagogical_dialogue_boost`.

## Metricas

| Prueba | Casos | Metrica | Resultado |
|---|---:|---|---:|
| Traduccion lexica | 393 | Precision exacta top-1 | 93.89% |
| Traduccion lexica | 393 | Precision por categoria top-1 | 98.47% |
| Traduccion lexica | 393 | Coherencia de respuesta | 100.0% |
| Dialogo pedagogico | 36 | Recuperacion dialogal top-1 | 100.0% |
| Dialogo pedagogico | 36 | Coherencia dialogal | 100.0% |

## Criterios de coherencia

- La respuesta no debe estar vacia.
- Debe recuperar al menos un contexto.
- El contexto debe incluir fuente trazable.
- En traduccion directa debe priorizar registros lexicos.
- En practica pedagogica debe priorizar registros dialogales.

## Evidencia generada

- Detalle por consulta: `C:/Users/Juliana/OneDrive/Desktop/GRADO ING/avi_webapp/reports/model_evaluation_details.csv`.
- La evaluacion usa el motor real de la aplicacion (`CorpusEngine`) y el modelo de recuperacion entrenado.
