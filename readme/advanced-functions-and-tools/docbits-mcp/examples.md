# Ejemplos

Una vez conectado DocBits MCP (consulte [Configuración e instalación](setup-and-configuration.md)), usted habla con su asistente en lenguaje natural y este elige por usted las herramientas de DocBits adecuadas. A continuación se muestran tareas reales que realizan los clientes, con el tipo de instrucción que escribiría y las herramientas que el asistente utiliza en segundo plano.

{% hint style="info" %}
Estos ejemplos funcionan igual en Claude Code, Gemini CLI y Codex: las instrucciones están en lenguaje natural, no son comandos.
{% endhint %}

## Priorizar la cola de trabajo

> *"¿Cuántos documentos están esperando validación y de qué tipos son?"*

Utiliza `get_pending_documents_count`, `get_pending_tasks_detail`, `get_top_document_types`. El asistente resume el trabajo pendiente y puede profundizar en cualquier documento.

> *"Muéstrame las facturas que han dado error hoy y dime por qué."*

Utiliza `search_documents` / `query_document_dashboard` + `get_document_logs` para encontrar los documentos con error y explicar el fallo a partir de los registros.

## Buscar e inspeccionar un documento

> *"Abre la factura INV-2026-00231 y muestra los campos extraídos y las líneas."*

Utiliza `get_document_by_name`, `get_extracted_fields`, `get_extracted_tables`. El asistente devuelve los datos de cabecera y la tabla, y puede obtener la imagen de la página con `get_page_image` si desea ver el origen.

> *"Busca todos los documentos del proveedor 'ACME GmbH' del mes pasado por más de 10.000 €."*

Utiliza `search_documents` / `query_document_dashboard` con filtros por campo.

## Corregir y aprobar

> *"En el documento 84213, establece el número de orden de compra en 4500098123 y la fecha de vencimiento en 2026-07-15, y luego valídalo."*

Utiliza `update_document_fields` y después `validate_document`. El asistente informa de los errores de validación para que pueda corregirlos.

> *"Valida y exporta el documento 84213 al ERP, pero muéstrame primero la vista previa de la exportación."*

Utiliza `get_export_preview` y, una vez que usted lo confirma, `validate_and_export`.

## Corregir una extracción de tabla

> *"La tabla de líneas de este albarán de entrega tiene dos filas que faltan; vuelve a extraerla con IA, oculta la columna *Charges* y conserva esto para este proveedor."*

Utiliza `extract_table_ai` para volver a ejecutar la tabla de IA en el documento, `apply_ai_table_formatting` para ocultar la columna y `save_table_training_rules` para guardar el resultado para el proveedor; el siguiente albarán de entrega de ese proveedor se extrae de la misma manera. `get_extracted_tables` muestra la tabla final. Resulta útil en documentos en los que la extracción basada en reglas omitió filas.

## Analítica e informes

> *"Dame un resumen ejecutivo de este mes: tendencia de volumen, tasa de procesamiento sin intervención y los 5 principales tipos de documento."*

Utiliza `get_executive_summary`, `get_volume_trends`, `get_success_rates`, `get_top_document_types`. Ideal para una actualización rápida para la dirección sin abrir el panel.

## Facturación electrónica (eDocs)

> *"¿Qué formatos de factura electrónica tenemos activados y se extrae correctamente este archivo ZUGFeRD?"*

Utiliza `list_electronic_document_types` + `test_electronic_document` y, después, `verify_electronic_documents` para confirmar los campos extraídos.

## Datos maestros y enriquecimiento de proveedores

> *"Añade un nuevo proveedor (nombre, NIF-IVA, IBAN) a los datos maestros y vuelve a ejecutar la búsqueda de proveedor en el documento 84500."*

Utiliza `upsert_vendor_master_data` + `trigger_supplier_lookup`.

## Cambios de configuración

> *"Activa la extracción de códigos QR para nuestra organización y confirma que la preferencia está establecida."*

Utiliza `set_preference` (que borra la caché automáticamente) + `get_preference` para confirmar.

> *"Enumera nuestros tipos de documento y muestra los ajustes de campo de 'Invoice'."*

Utiliza `list_document_types` + `get_field_settings`.

## Estado y diagnóstico

> *"¿Están bien ahora mismo la API de DocBits y el worker de procesamiento? ¿Con qué usuario estoy conectado?"*

Utiliza `check_api_health`, `check_celery_health`, `get_current_user`.

---

## Consejos

- **Sea específico con el documento**: un ID o un nombre de archivo exacto es lo más rápido; de lo contrario, el asistente buscará primero.
- **Pida una vista previa antes de exportar**: `get_export_preview` le permite confirmar los datos que se enviarán al ERP antes de que `validate_and_export` los envíe.
- **Se aplican los permisos**: el asistente solo puede hacer lo que su usuario de DocBits o su clave de API tengan permitido. Las aprobaciones y las exportaciones respetan su rol y sus ACL.
- **Precaución en producción**: el MCP actúa sobre datos reales. En entornos de cliente o de producción, prefiera las acciones de lectura y vista previa y confirme antes de aprobar, exportar o eliminar.
