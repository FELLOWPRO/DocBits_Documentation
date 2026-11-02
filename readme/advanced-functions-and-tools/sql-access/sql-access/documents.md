# Documentos

## Columnas

* `id`: interno
* `org_id`: ID de la organización
* `batch_id`: interno
* `doc_path`: interno
* `doc_type`: DOC Type
* `status`: interno
* `message`: text
* `export_attempts`: integer
* `last_attempted_on`: marca de tiempo con zona horaria
* `next_attempt_on`: marca de tiempo con zona horaria
* `assigned_to`: integer
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean
* `task_id`: interno
* `filename`: interno
* `assigned_on`: marca de tiempo con zona horaria
* `pages`: integer
* `auto_processed`: boolean
* `exception_info`: text
* `doc_language`: Language
* `is_trimmed`: boolean
* `doc_origin`: Doc Origin
* `doc_locale`: Doc Locale
* `is_doc2landing_doc`: boolean
* `extraction_time`: double precision
* `export_time`: double precision
* `po_all_matched`: boolean
* `restart_allowed`: boolean
* `table_version`: interno
* `force_ocr`: boolean
* `locked_by`: integer
* `locked_on`: marca de tiempo con zona horaria
* `lock_renewed_on`: marca de tiempo con zona horaria
* `lock_key`: interno
* `last_saved_by`: integer
* `last_saved_on`: marca de tiempo con zona horaria
* `document_version`: integer
* `lock_session_key`: interno
* `sub_org_id`: interno
* `doc_source`: interno
* `sub_doc_type`: interno
* `assigned_to_group`: interno
* `status_changed_on`: marca de tiempo con zona horaria
* `improve_quality`: boolean
* `priority`: integer
* `metadata_field`: json
* `doc_classification_label`: interno
* `doc_start_page`: integer
* `doc_classification_class`: interno
* `celery_task_token`: interno
* `celery_task_attempt`: integer
* `celery_task_priority`: integer
* `has_zugferd`: boolean
* `has_peppol`: boolean
* `timestamp_for_validation`: marca de tiempo con zona horaria
* `exception_details`: text
* `has_annotated_version`: boolean
* `po_match_status`: interno
* `tr_ocr_extracted_data`: text
* `pending_workflow_execution`: boolean
* `extracted_document_id`: interno
* `extracted_supplier_id`: interno
* `classification_manually_corrected`: boolean
* `supplier_as_org_id`: interno
* `extracted_data_basic`: jsonb
* `celery_task_queue`: interno
* `extracted_data`: jsonb
* `extracted_data_jsonb`: jsonb
* `warnings`: jsonb

## Análisis y descripción

```markdown
# Documentación técnica de la tabla `public.documents`

## Introducción

La tabla `public.documents` está diseñada para almacenar y gestionar los metadatos y la información de procesamiento relacionados con la gestión de documentos dentro de una organización. Esto incluye el seguimiento del estado de los documentos, los intentos de procesamiento, el idioma y otros detalles administrativos. La tabla está estructurada para admitir la clasificación de documentos, el flujo de trabajo de procesamiento y las asignaciones de usuarios, lo que la hace fundamental para el sistema de gestión de documentos.

## Descripción de las columnas

### id
- **Significado**: Identificador único de cada documento.
- **Función**: Clave primaria.
- **Contenido típico**: Una cadena UUID que representa el documento.

### org_id
- **Significado**: Identificador de la organización asociada al documento.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que representa la organización.

### batch_id
- **Significado**: Identificador del lote en el que se procesó el documento.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que representa el lote.

### doc_path
- **Significado**: Ruta del archivo donde se almacena el documento.
- **Función**: Campo técnico.
- **Contenido típico**: Ruta al archivo del documento, p. ej., `documents/{id}/{id}.pdf`.

### doc_type
- **Significado**: Tipo de documento almacenado (p. ej., factura).
- **Función**: Clasificación del documento.
- **Contenido típico**: Una cadena como `INVOICE`.

### status
- **Significado**: Estado de procesamiento actual del documento.
- **Función**: Indicador del flujo de trabajo.
- **Contenido típico**: Una cadena que indica el estado, p. ej., `ready_for_validation`.

### message
- **Significado**: Información sobre el estado de procesamiento del documento o sobre errores.
- **Función**: Campo descriptivo.
- **Contenido típico**: Texto que describe errores o mensajes relacionados con el procesamiento del documento.

### export_attempts
- **Significado**: Número de veces que se ha intentado exportar el documento.
- **Función**: Seguimiento del procesamiento.
- **Contenido típico**: Recuento entero de intentos de exportación.

### last_attempted_on
- **Significado**: Marca de tiempo del último intento de procesar o exportar el documento.
- **Función**: Campo de marca de tiempo.
- **Contenido típico**: Fecha y hora con zona horaria.

### next_attempt_on
- **Significado**: Marca de tiempo programada para el siguiente intento de procesar o exportar el documento.
- **Función**: Campo de programación.
- **Contenido típico**: Fecha y hora con zona horaria.

### assigned_to
- **Significado**: Identificador del usuario asignado a este documento.
- **Función**: Clave externa.
- **Contenido típico**: Entero que representa el ID de usuario.

### created_by
- **Significado**: Identificador del usuario que creó o cargó el documento.
- **Función**: Clave externa.
- **Contenido típico**: Entero que representa el ID de usuario.

### created_on
- **Significado**: Marca de tiempo de cuándo se creó o cargó el documento.
- **Función**: Campo de marca de tiempo.
- **Contenido típico**: Fecha y hora con zona horaria.

### last_modified_on
- **Significado**: Marca de tiempo de la última modificación realizada en el registro del documento.
- **Función**: Campo de marca de tiempo.
- **Contenido típico**: Fecha y hora con zona horaria.

### is_deleted
- **Significado**: Indica si el documento está marcado como eliminado.
- **Función**: Indicador de eliminación lógica.
- **Contenido típico**: Valor booleano (True o False).

### task_id
- **Significado**: Identificador de la tarea asociada al procesamiento del documento.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que representa la tarea.

### filename
- **Significado**: Nombre de archivo original del documento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Nombre del archivo, p. ej., `document.pdf`.

### assigned_on
- **Significado**: Marca de tiempo de cuándo se asignó el documento a un usuario.
- **Función**: Campo de marca de tiempo.
- **Contenido típico**: Fecha y hora con zona horaria.

### pages
- **Significado**: Número de páginas del documento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Entero que indica el número de páginas.

### auto_processed
- **Significado**: Indica si el documento se procesó automáticamente.
- **Función**: Indicador del estado de procesamiento.
- **Contenido típico**: Valor booleano (True o False).

### exception_info
- **Significado**: Información sobre las excepciones surgidas durante el procesamiento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Texto que describe las excepciones de procesamiento.

### doc_language
- **Significado**: Idioma del contenido del documento.
- **Función**: Clasificación del idioma.
- **Contenido típico**: Código de idioma ISO, p. ej., `en`, `de`.

### is_trimmed
- **Significado**: Indica si el documento se ha recortado.
- **Función**: Indicador de modificación del documento.
- **Contenido típico**: Valor booleano (True o False).

### doc_origin
- **Significado**: Origen del documento, que posiblemente indica el país o el sistema de origen.
- **Función**: Campo descriptivo.
- **Contenido típico**: Código de país o identificador de origen, p. ej., `DE`.

### doc_locale
- **Significado**: Configuración regional del documento, que indica el idioma y la región.
- **Función**: Clasificación de la configuración regional.
- **Contenido típico**: Cadena de configuración regional, p. ej., `de_DE.ISO8859-1`.

### is_doc2landing_doc
- **Significado**: Indica si el documento está relacionado con un flujo de trabajo de procesamiento concreto (Doc2Landing).
- **Función**: Indicador del flujo de trabajo.
- **Contenido típico**: Valor booleano (True o False).

### extraction_time
- **Significado**: Tiempo empleado en extraer los datos del documento.
- **Función**: Métrica de rendimiento.
- **Contenido típico**: Valor de doble precisión que representa el tiempo de extracción.

### export_time
- **Significado**: Tiempo empleado en exportar el documento.
- **Función**: Métrica de rendimiento.
- **Contenido típico**: Valor de doble precisión que representa el tiempo de exportación.

### po_all_matched
- **Significado**: Indica si se han conciliado todos los pedidos de compra relacionados con el documento.
- **Función**: Indicador del estado de conciliación.
- **Contenido típico**: Valor booleano (True o False).

### restart_allowed
- **Significado**: Indica si se puede reiniciar el procesamiento del documento.
- **Función**: Indicador de control del flujo de trabajo.
- **Contenido típico**: Valor booleano (True o False).

### table_version
- **Significado**: Versión de la estructura de tabla utilizada para el documento.
- **Función**: Control de versiones.
- **Contenido típico**: Cadena que indica la versión, p. ej., `v3`.

### force_ocr
- **Significado**: Indica si se fuerza el procesamiento OCR del documento.
- **Función**: Indicador de control del procesamiento.
- **Contenido típico**: Valor booleano (True o False).

### locked_by
- **Significado**: Identificador del usuario que ha bloqueado el documento para su edición.
- **Función**: Clave externa.
- **Contenido típico**: Entero que representa el ID de usuario.

### locked_on
- **Significado**: Marca de tiempo de cuándo se bloqueó el documento para su edición.
- **Función**: Campo de marca de tiempo.
- **Contenido típico**: Fecha y hora con zona horaria.

### lock_renewed_on
- **Significado**: Marca de tiempo de la última renovación del bloqueo del documento.
- **Función**: Campo de marca de tiempo.
- **Contenido típico**: Fecha y hora con zona horaria.

### lock_key
- **Significado**: Clave asociada al bloqueo del documento.
- **Función**: Control del bloqueo.
- **Contenido típico**: Cadena que representa la clave de bloqueo.

### last_saved_by
- **Significado**: Identificador del usuario que guardó el documento por última vez.
- **Función**: Clave externa.
- **Contenido típico**: Entero que representa el ID de usuario.

### last_saved_on
- **Significado**: Marca de tiempo de cuándo se guardó el documento por última vez.
- **Función**: Campo de marca de tiempo.
- **Contenido típico**: Fecha y hora con zona horaria.

### document_version
- **Significado**: Número de versión del documento.
- **Función**: Seguimiento de versiones.
- **Contenido típico**: Entero que representa la versión del documento.

### lock_session_key
- **Significado**: Clave de sesión asociada al bloqueo del documento.
- **Función**: Control del bloqueo.
- **Contenido típico**: Cadena que representa la clave de sesión.

### sub_org_id
- **Significado**: Identificador de una suborganización asociada al documento.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que representa la suborganización.

### doc_source
- **Significado**: Sistema de origen o procedencia del documento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadena que indica el origen, p. ej., `doc2app`.

### sub_doc_type
- **Significado**: Clasificación del subtipo del documento.
- **Función**: Clasificación del documento.
- **Contenido típico**: Cadena que indica el subtipo.

### assigned_to_group
- **Significado**: Identificador del grupo al que está asignado el documento.
- **Función**: Seguimiento de asignaciones.
- **Contenido típico**: Una cadena UUID que representa el grupo.

### status_changed_on
- **Significado**: Marca de tiempo de cuándo cambió el estado del documento por última vez.
- **Función**: Campo de marca de tiempo.
- **Contenido típico**: Fecha y hora con zona horaria.

### improve_quality
- **Significado**: Indica si se aplican al documento procesos de mejora de la calidad.
- **Función**: Indicador de control de calidad.
- **Contenido típico**: Valor booleano (True o False).

### priority
- **Significado**: Prioridad de procesamiento del documento.
- **Función**: Control del flujo de trabajo.
- **Contenido típico**: Entero que indica el nivel de prioridad.

### metadata_field
- **Significado**: Campo JSON que contiene metadatos relacionados con el documento.
- **Función**: Almacenamiento de metadatos.
- **Contenido típico**: Estructura JSON con diversos campos de metadatos.

### doc_classification_label
- **Significado**: Etiqueta que indica la clasificación del documento.
- **Función**: Etiqueta de clasificación.
- **Contenido típico**: Cadena que indica la clasificación, p. ej., `INVOICE`.

### doc_start_page
- **Significado**: Número de página en la que comienza el contenido del documento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Entero que indica la página de inicio.

### doc_classification_class
- **Significado**: Clase que indica la clasificación detallada del documento.
- **Función**: Detalle de la clasificación.
- **Contenido típico**: Cadena que indica la clase de clasificación.

### celery_task_token
- **Significado**: Token para el seguimiento de la tarea de Celery asociada al documento.
- **Función**: Seguimiento de tareas.
- **Contenido típico**: Cadena que representa el token de la tarea.

### celery_task_attempt
- **Significado**: Número de intentos realizados para la tarea de Celery.
- **Función**: Seguimiento de tareas.
- **Contenido típico**: Recuento entero de intentos de la tarea.

### celery_task_priority
- **Significado**: Nivel de prioridad de la tarea de Celery.
- **Función**: Control de tareas.
- **Contenido típico**: Entero que indica la prioridad de la tarea.

### has_zugferd
- **Significado**: Indica si el documento está en formato ZUGFeRD.
- **Función**: Indicador de formato.
- **Contenido típico**: Valor booleano (True o False).

### has_peppol
- **Significado**: Indica si el documento está en formato PEPPOL.
- **Función**: Indicador de formato.
- **Contenido típico**: Valor booleano (True o False).

### timestamp_for_validation
- **Significado**: Marca de tiempo de cuándo se validó el documento.
- **Función**: Seguimiento de la validación.
- **Contenido típico**: Fecha y hora con zona horaria.

### exception_details
- **Significado**: Información detallada sobre las excepciones durante el procesamiento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Texto con los detalles de la excepción.

### has_annotated_version
- **Significado**: Indica si existe una versión anotada del documento.
- **Función**: Indicador de versión.
- **Contenido típico**: Valor booleano (True o False).

### po_match_status
- **Significado**: Estado de la conciliación de pedidos de compra.
- **Función**: Indicador del estado de conciliación.
- **Contenido típico**: Cadena que indica el estado de la conciliación.

### tr_ocr_extracted_data
- **Significado**: Datos extraídos del documento mediante OCR.
- **Función**: Almacenamiento de datos.
- **Contenido típico**: Texto con los datos extraídos.

### pending_workflow_execution
- **Significado**: Indica si hay ejecuciones de flujo de trabajo pendientes.
- **Función**: Indicador del estado del flujo de trabajo.
- **Contenido típico**: Valor booleano (True o False).

### extracted_document_id
- **Significado**: Identificador del documento extraído.
- **Función**: Seguimiento de la extracción.
- **Contenido típico**: Una cadena UUID que representa el documento extraído.

### extracted_supplier_id
- **Significado**: Identificador del proveedor extraído.
- **Función**: Seguimiento de la extracción.
- **Contenido típico**: Una cadena UUID que representa el proveedor extraído.

### classification_manually_corrected
- **Significado**: Indica si la clasificación del documento se corrigió manualmente.
- **Función**: Indicador del estado de la clasificación.
- **Contenido típico**: Valor booleano (True o False).

### supplier_as_org_id
- **Significado**: Identificador del proveedor tratado como organización.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que representa la organización del proveedor.

### extracted_data_basic
- **Significado**: Datos extraídos básicos en formato JSONB.
- **Función**: Almacenamiento de datos.
- **Contenido típico**: Estructura JSONB con los campos de datos extraídos.

### celery_task_queue
- **Significado**: Nombre de la cola de tareas de Celery.
- **Función**: Gestión de tareas.
- **Contenido típico**: Cadena que indica el nombre de la cola.

### extracted_data
- **Significado**: Datos extraídos del documento en formato JSONB.
- **Función**: Almacenamiento de datos.
- **Contenido típico**: Estructura JSONB con los campos de datos extraídos.

### extracted_data_jsonb
- **Significado**: Campo JSONB que contiene los datos extraídos detallados.
- **Función**: Almacenamiento de datos.
- **Contenido típico**: Estructura JSONB con los campos de datos extraídos.

### warnings
- **Significado**: Advertencias relacionadas con el procesamiento del documento, almacenadas en formato JSONB.
- **Función**: Almacenamiento de advertencias.
- **Contenido típico**: Estructura JSONB con mensajes de advertencia.
```
