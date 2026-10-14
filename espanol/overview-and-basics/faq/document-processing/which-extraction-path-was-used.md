# ¿Qué ruta de extracción se utilizó?

"¿Por qué esta tabla se ve así?" se responde averiguando _qué_ hizo DocBits con este documento: reglas guardadas, la tabla AI, qué nivel de IA y dónde salió mal. Esta página es la lista de comprobación que usan soporte y los partners antes de cambiar cualquier configuración.

## 1. Mira las pestañas de la pantalla de validación

Abre el documento y mira las pestañas encima de la tabla de líneas de detalle:

| Qué ves                                                                                        | Ruta                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Filas en la pestaña **Tabla extraída** (_Extracted table_)                                     | Ruta basada en reglas. El proveedor tiene una tabla entrenada; las filas proceden de las reglas de coordenadas guardadas y la IA no ha intervenido (salvo en las columnas marcadas como _Usar IA_).                                       |
| Filas en la pestaña **Tabla extraída por IA** (_AI Extracted table_), campo _Etiquetas_ debajo | Ruta de IA. Ninguna regla guardada coincidió; la extracción de tablas por IA generó las filas, usando el nivel de IA de la organización o el nivel establecido para este proveedor en _Más ajustes_ → _Modelo de IA basado en proveedor_. |
| Tooltip _AI table not found_ en la pestaña de IA                                               | La ruta de IA se ejecutó y no devolvió nada para este documento.                                                                                                                                                                          |
| Ninguna pestaña de tabla                                                                       | Ambos ajustes de tabla están desactivados para la organización; nada extrajo la tabla.                                                                                                                                                    |
| _No line items yet_                                                                            | La ruta se ejecutó pero no encontró filas (sin texto legible, sin tabla en la página, o las reglas no coincidieron con este diseño).                                                                                                      |

Los campos de cabecera llevan su propia insignia de origen junto al valor: _Extracted using AI_, _Learned from validated AI extraction_, _Extracted using saved rules (FELLOW\_KV2)_, _Extracted from electronic document_, _Calculated from vendor master data_. Estas insignias describen el campo de cabecera, no la tabla.

## 2. Comprueba la configuración del proveedor

* **Configuración → Procesamiento de documentos → Clasificación y extracción → Modelo de IA**: la tabla debajo del selector lista todos los proveedores con un modelo o un entrenamiento almacenado. Un proveedor de esta lista con _datos de entrenamiento_ tiene reglas guardadas; _restablecer los datos de entrenamiento_ las elimina.
* **Configuración → Procesamiento de documentos → Configuración de OCR**: _Usar E-Text si está disponible_ y _Usar datos de IA para tablas_ cambian el texto que ve la extracción. Un proveedor puede sobrescribir E-Text en _Más ajustes_ de la pantalla de validación.
* **Configuración → Configuración global → Tipos de documentos → Columnas de tabla**: indicadores de oculta, obligatoria y _Usar IA_. Una columna oculta nunca se rellena; una columna con _Usar IA_ la rellena la IA incluso en proveedores con reglas.

## 3. Reproducir sin la interfaz (API / MCP)

Con acceso a la API o al MCP puedes hacer las mismas preguntas de forma programática:

| Pregunta                                                | Herramienta                                                                                                                                                                                                     |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ¿Esta tabla la generó la IA?                            | `get_extracted_tables(doc_id)`: cada tabla lleva `is_ai_table: true/false`.                                                                                                                                     |
| ¿Qué dan las reglas y qué da la IA?                     | `get_table_extraction_report(doc_id, mode="nonai")` y de nuevo con `mode="ai"`; el informe muestra la estructura configurada, las filas extraídas y la vista previa de la página para cada ruta. Compara ambos. |
| ¿Qué columnas están configuradas y con qué indicadores? | `get_table_config(doc_type)`                                                                                                                                                                                    |
| ¿Influye el nivel de IA?                                | `compare_table_extraction_models(doc_id)`, ejecuta dos niveles sobre el mismo documento (necesita un documento con número de proveedor).                                                                        |
| Repetir la extracción en este documento                 | `extract_table_ai(doc_id)` (IA) o `restart_document(doc_id)` (todo el pipeline).                                                                                                                                |
| ¿Qué registró el pipeline para este documento?          | `get_document_logs(doc_id)`                                                                                                                                                                                     |

Las herramientas del DocBits MCP se describen en la documentación de [DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp) (en inglés).

## 4. Lee los registros

**Configuración → Configuración de Registros** (registro de actividad) muestra los eventos de todos los servicios. Para una pregunta sobre tablas:

* Filtra por el nombre de archivo o el ID del documento en _Buscar registros_.
* Usa el filtro _Servicio_: la extracción en sí se ejecuta en el servicio de extracción y en los workers de Celery, no en el servicio `api`. Si solo ves líneas de `api`, amplía el filtro.
* Una ejecución normal registra, en este orden: documento recibido → OCR / E-Text → clasificación → extracción de campos → extracción de tablas (búsqueda de reglas y, si ninguna coincide, IA) → validación → cambio de estado. El paso que falta o que informa de un error es el que hay que revisar.

## 5. Decide: configuración, datos o error

| Síntoma                                                                                     | Causa más probable                                                                                    | Siguiente paso                                                                                                                      |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Tabla correcta para el proveedor A, incorrecta para el proveedor B, mismo tipo de documento | Por proveedor: B no tiene reglas, o tiene reglas antiguas que ya no coinciden con el diseño de B      | Entrena la tabla de B una vez (o elimina las reglas de B para que la IA tome el relevo).                                            |
| Tabla incorrecta para todos los proveedores desde una fecha concreta                        | Cambió un ajuste de la organización (nivel de IA, extracción estructurada, vision, columnas de tabla) | Compara los ajustes con la fecha del cambio; reinicia un documento para confirmarlo.                                                |
| Mismo documento: ruta de reglas vacía, ruta de IA correcta                                  | Las reglas no coinciden con esta variante del diseño                                                  | Vuelve a entrenar con este documento o elimina las reglas.                                                                          |
| Mismo documento: ambas rutas vacías                                                         | Sin texto legible (escaneo sin texto OCR, PDF solo imagen)                                            | Vista OCR en la pantalla de validación; activa E-Text si el PDF tiene capa de texto; prueba otra versión de OCR.                    |
| Una columna incorrecta en todas las filas, el resto bien                                    | Asignación de columnas o indicador _Usar IA_                                                          | Configuración de Columnas de tabla; reasigna en el entrenamiento de tablas.                                                         |
| Faltan filas en los saltos de página o después de un subtotal                               | Diseño que la IA o las reglas no siguieron                                                            | Entrena la tabla con un documento de varias páginas; añade una etiqueta como _"la tabla continúa en la página 2"_.                  |
| Falta el paso de extracción en los registros, documento atascado en _running_               | Infraestructura (cola de workers), no configuración                                                   | Comprueba las tareas pendientes (`get_pending_tasks_detail` a través del MCP) y contacta con soporte indicando el ID del documento. |

## Qué enviar a soporte

* ID del documento y organización
* Qué pestaña contiene las filas (Tabla extraída / Tabla extraída por IA / ninguna) y el nivel de IA en uso
* Si el proveedor tiene reglas guardadas y cuándo se guardaron por última vez
* Un documento de ejemplo en el que funciona y otro en el que no, si tienes ambos

## Páginas relacionadas

* [Solución de problemas de extracción de tablas](table-extraction-troubleshoot.md): calidad de extracción, OCR, E-Text, mensajes de la tabla
* [Entrenamiento de Campos de Línea / Tabla de Entrenamiento](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/)
* [Tabla AI](../../../end-user-and-partner-section/end-user-section/ai-table/)
* [Configuración de Registros](../../../administration-and-setup/settings/log-settings/)
