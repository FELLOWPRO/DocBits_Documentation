# DocBits MCP

DocBits expone un servidor de **Model Context Protocol (MCP)** que permite a los asistentes de IA trabajar con sus documentos, la extracción, la búsqueda, los análisis y la configuración, directamente desde un chat o una sesión de programación. Cualquier cliente compatible con MCP puede conectarse: **Claude Code**, **Claude Desktop**, **Google Gemini CLI**, **OpenAI Codex** o cualquier integración personalizada.

El servidor está montado en la API de DocBits en `/v3/mcp` y está limitado a su organización: cada llamada se ejecuta con los permisos del usuario (o de la clave de API) que se conectó.

{% hint style="info" %}
**Endpoint: utilice su región (EU o US):**

* Production (EU) — `https://eu.api.docbits.com/v3/mcp`
* Production (US) — `https://us.api.docbits.com/v3/mcp`

Consulte [Setup & Configuration](setup-and-configuration.md) para ver la matriz completa de hosts y cómo iniciar sesión con OAuth.
{% endhint %}

## ¿Qué puede hacer?

Con DocBits MCP, un asistente puede, en su nombre:

* **Buscar y leer documentos**: listar, buscar (texto completo y por campos), abrir un documento y leer su estado, registros, imágenes de página y vista previa de exportación
* **Trabajar con los datos extraídos**: leer campos y tablas extraídos, corregir valores de campos, extraer tablas con IA, validar, aprobar y exportar a su ERP
* **Consultar el panel**: ejecutar consultas del panel en lenguaje natural, comparar modos de búsqueda e inspeccionar las capacidades de búsqueda
* **Obtener analíticas**: resúmenes ejecutivos, tasas de éxito, tendencias de volumen, tipos de documento principales y detalle de tareas pendientes
* **Gestionar facturas electrónicas (eDocs)**: listar tipos de documentos electrónicos, probar y verificar documentos electrónicos, gestionar atributos de extracción personalizados
* **Gestionar datos maestros**: actualizar o crear datos maestros de proveedores, activar búsquedas de proveedores, importar BOD de facturas de proveedor, mantener asignaciones de condiciones de pago y descuentos
* **Leer y modificar la configuración**: preferencias de la organización, tipos de documento, ajustes de campos, usuarios y caché
* **Comprobar el estado**: estado de la API y de Celery, usuario actual e información de la API

## Resumen de herramientas

DocBits MCP agrupa bastante más de un centenar de herramientas en las categorías siguientes (el número exacto crece con cada versión; su asistente lista el conjunto actual). La mayoría reflejan endpoints REST existentes de DocBits; consulte la [API Reference](../../) para ver el detalle de solicitudes y respuestas. Un asistente elige automáticamente la herramienta adecuada a partir de su solicitud; las tablas son un mapa de lo que está disponible.

### Documents & Processing

| Herramienta                             | Descripción                                                          |
| --------------------------------------- | -------------------------------------------------------------------- |
| `list_documents`                        | Lista los documentos de la organización (filtrable)                  |
| `get_document` / `get_document_by_name` | Abre un documento por ID o nombre de archivo                         |
| `upload_document`                       | Sube un documento nuevo para su procesamiento                        |
| `get_document_status`                   | Estado actual del pipeline de un documento                           |
| `get_document_logs`                     | Entradas del registro de procesamiento de un documento               |
| `query_org_logs`                        | Recorre página a página los registros de servicio de la organización |
| `restart_document`                      | Vuelve a ejecutar el pipeline de procesamiento                       |
| `delete_document`                       | Elimina un documento                                                 |
| `get_pending_documents_count`           | Cuántos documentos esperan validación                                |

### Extraction & Validation

| Herramienta                                         | Descripción                                                                                   |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `get_extracted_fields` / `get_document_fields`      | Lee los campos de cabecera extraídos                                                          |
| `get_extracted_tables`                              | Lee las tablas de líneas extraídas                                                            |
| `get_document_for_validation` / `get_next_document` | Abre un documento tal como lo hace la pantalla de validación; obtiene el siguiente de la cola |
| `get_page_image`                                    | Imagen de página para comprobaciones visuales                                                 |
| `update_document_fields`                            | Corrige o establece valores de campos                                                         |
| `validate_document`                                 | Ejecuta las reglas de validación de campos                                                    |
| `approve_document`                                  | Aprueba un documento validado                                                                 |
| `validate_and_export`                               | Valida y después exporta al ERP                                                               |
| `get_export_preview`                                | Vista previa de la carga útil de exportación antes de enviarla                                |

### Table Extraction

Todo lo que la pantalla de validación y los ajustes de columnas de tabla pueden hacer con las tablas de líneas. Las herramientas de configuración modifican los tipos de documento de la organización; las herramientas de extracción y corrección trabajan sobre un documento; las herramientas de reglas almacenan lo que DocBits aprendió de un proveedor.

| Herramienta                                                   | Descripción                                                                                                                                           |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `list_tables` / `get_table_config`                            | Tablas y columnas de un tipo de documento, con los indicadores Required / Read Only / Hidden / Use AI                                                 |
| `create_table`                                                | Añade una segunda tabla de líneas a un tipo de documento                                                                                              |
| `add_table_column` / `delete_table_column`                    | Añade o elimina de forma lógica una columna de tabla                                                                                                  |
| `set_ai_table_config`                                         | Activa la extracción de tablas con IA, la visión y el modo estructurado para la organización                                                          |
| `extract_table_ai`                                            | Ejecuta la extracción de tablas con IA en un documento (texto o visión)                                                                               |
| `extract_table_only`                                          | Extrae la tabla sin tocar los campos de cabecera (reglas o IA)                                                                                        |
| `extract_table_nonai`                                         | Extracción basada en reglas a partir de las coordenadas que usted indique; es el primer paso de un entrenamiento de tablas mediante la API            |
| `apply_ai_table_formatting` / `apply_table_feedback`          | Reformatea una tabla de IA: oculta columnas, reasigna, aplica la retroalimentación del usuario                                                        |
| `remap_table_columns`                                         | Cambia qué columna extraída alimenta qué columna configurada                                                                                          |
| `save_table_rules` / `save_table_training_rules`              | Almacena las reglas de coordenadas o las reglas de formato de IA para el proveedor, de modo que el siguiente documento se extraiga de la misma manera |
| `delete_table_training_rules`                                 | Elimina las reglas guardadas de un proveedor; el siguiente documento vuelve a usar la IA                                                              |
| `get_table_extraction_report` / `list_table_report_suppliers` | Informe por proveedor sobre cómo se extraen las tablas (reglas, IA, modelo), con vista previa                                                         |
| `compare_table_extraction_models`                             | Extrae el mismo documento con dos niveles de IA y compara las tablas                                                                                  |

### Search & Dashboard

| Herramienta                                       | Descripción                                                                                                 |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `search_documents` / `search_documents_by_name`   | Búsqueda de texto completo y por nombre de archivo                                                          |
| `query_document_dashboard`                        | Consulta del panel en lenguaje natural                                                                      |
| `explain_document_dashboard_query`                | Muestra cómo se interpretó una consulta                                                                     |
| `get_search_capabilities`                         | Qué funciones de búsqueda tiene activadas la organización                                                   |
| `compare_search_modes`                            | Compara resultados por palabra clave frente a vectoriales                                                   |
| `diagnose_document_search`                        | Por qué un documento aparece o no en una búsqueda determinada, clásica frente a texto completo, lado a lado |
| `inspect_document_search_index`                   | Si un documento está presente en los índices de documento, texto y vectorial, y cuándo se escribió cada uno |
| `get_dashboard_columns` / `set_dashboard_columns` | Lee o cambia las columnas que se muestran en el panel de documentos                                         |

### Touchless Intelligence

Por qué los documentos necesitan intervención humana y qué cambiar para que lo necesiten menos. Todas las herramientas de esta sección son de solo lectura excepto `touchless_apply_change`, que escribe exactamente un cambio de ajuste previsualizado.

| Herramienta                                                      | Descripción                                                                                                            |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `touchless_get_summary`                                          | Cuadro de mando touchless de la organización: cuántos documentos pasaron sin intervención, por período y segmento      |
| `touchless_list_segments`                                        | Valores por los que puede segmentar las cifras (proveedor, tipo de documento, …)                                       |
| `touchless_rank_supplier_opportunities`                          | Proveedores ordenados según cuánto trabajo manual causan                                                               |
| `touchless_diagnose_supplier`                                    | Por qué los documentos de un proveedor se detienen para una persona                                                    |
| `touchless_get_issue_cluster`                                    | Un problema recurrente y los documentos a los que afectó                                                               |
| `touchless_get_document_trace`                                   | Historial touchless completo de un documento                                                                           |
| `touchless_explain_pipeline`                                     | En qué punto del pipeline se detuvo un documento o un clúster                                                          |
| `touchless_explain_po_match` / `touchless_get_po_match_evidence` | Por qué la coincidencia de pedidos de compra tuvo éxito o falló, con el conjunto de reglas y el cálculo de tolerancias |
| `touchless_get_recommendations`                                  | Qué cambiar, no solo qué salió mal                                                                                     |
| `touchless_list_change_proposals`                                | Cambios de ajustes que aumentarían la tasa touchless, con la mejora esperada                                           |
| `touchless_preview_change`                                       | Simulación de una propuesta: no se escribe nada                                                                        |
| `touchless_apply_change`                                         | Aplica a la organización una propuesta previsualizada                                                                  |
| `touchless_verify_change`                                        | Qué valor aportó finalmente un cambio aplicado                                                                         |

### Analytics & BI

| Herramienta                | Descripción                                 |
| -------------------------- | ------------------------------------------- |
| `get_executive_summary`    | KPI de alto nivel de la organización        |
| `get_success_rates`        | Tasas touchless / de procesamiento directo  |
| `get_volume_trends`        | Volumen de documentos a lo largo del tiempo |
| `get_top_document_types`   | Tipos de documento más frecuentes           |
| `get_pending_tasks_detail` | Detalle del trabajo pendiente               |

### Electronic Documents (e-invoices)

| Herramienta                                                    | Descripción                                                                      |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `list_electronic_document_types`                               | Formatos de factura electrónica admitidos (ZUGFeRD, XRechnung, Factur-X, UBL, …) |
| `test_electronic_document`                                     | Clasifica y extrae un documento electrónico de muestra                           |
| `verify_electronic_documents` / `validate_all_edocs`           | Verifica la extracción de documentos electrónicos                                |
| `list_edoc_custom_attributes` / `create_edoc_custom_attribute` | Gestiona atributos de extracción personalizados                                  |

### Master Data

| Herramienta                                               | Descripción                                                                                   |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `upsert_vendor_master_data`                               | Crea o actualiza los datos maestros de proveedores                                            |
| `trigger_supplier_lookup`                                 | Enriquece un documento con los datos maestros del proveedor                                   |
| `import_supplier_invoice_bod`                             | Importa un BOD de factura de proveedor                                                        |
| `get_supplier_invoice`                                    | Lee los datos persistidos de la factura de proveedor (BOD) por factura, proveedor o documento |
| `upsert_payment_term_mapping` / `upsert_discount_mapping` | Mantiene las asignaciones de cálculo                                                          |

### Configuration, Admin & Health

| Herramienta                                             | Descripción                                                 |
| ------------------------------------------------------- | ----------------------------------------------------------- |
| `get_preferences` / `get_preference` / `set_preference` | Lee y modifica las preferencias de la organización          |
| `list_document_types` / `get_field_settings`            | Inspecciona la configuración de tipos de documento y campos |
| `list_users`                                            | Lista los usuarios de la organización                       |
| `clear_org_cache`                                       | Borra la configuración almacenada en caché                  |
| `check_api_health` / `check_celery_health`              | Estado de los servicios                                     |
| `get_current_user` / `get_api_info`                     | Identidad y metadatos de la API                             |

## Siguientes pasos

* [**Setup & Configuration**](setup-and-configuration.md) — conecte Claude Code, Gemini CLI o Codex (con inicio de sesión o clave de API)
* [**Examples**](examples.md) — cosas reales que los clientes piden al asistente
* [**Electronic Documents (eDocs)**](edocs-mcp/) — análisis detallado de las herramientas de eDoc: inspeccione y pruebe el procesamiento de facturas electrónicas y gestione reglas personalizadas de extracción y vista previa (mismo endpoint, mismo inicio de sesión)
* [**Workflows & Cards (DocFlow)**](docflow-mcp/) — gestione flujos de trabajo avanzados y tarjetas de socios

{% hint style="info" %}
**Un único MCP para todo.** Las herramientas de eDoc y las de **Workflows & Cards (DocFlow)** se ejecutan en el **mismo** endpoint `api.docbits.com/v3/mcp` con el mismo inicio de sesión de DocBits. Las herramientas de DocFlow aparecen allí con el prefijo `docflow_` (por ejemplo, `docflow_list_workflows`); la página de DocFlow las documenta con sus nombres sin prefijo. Conectarse directamente al host de DocFlow sigue siendo posible, pero ya no es necesario.
{% endhint %}
