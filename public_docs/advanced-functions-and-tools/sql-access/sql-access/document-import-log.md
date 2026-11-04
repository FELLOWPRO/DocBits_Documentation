# Registro de importación de documentos

## Columnas

* `id`: integer
* `org_id`: ID de la organización
* `sub_org_id`: interno
* `original_filename`: interno
* `filename`: interno
* `imported_on`: interno
* `source_type`: interno
* `source`: interno
* `success`: boolean
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean
* `import_id`: text
* `extra_data`: text
* `doc_id`: interno
* `email_connection_id`: integer
* `subject`: interno
* `body`: text
* `sender`: interno
* `error_resp`: interno
* `source_received_on`: marca de tiempo con zona horaria

## Análisis y descripción

```markdown
# Documentación técnica de la tabla `public.document_import_log`

## Introducción

La tabla `public.document_import_log` está diseñada para registrar los detalles de las importaciones de documentos en el sistema. Recoge información sobre cada documento, incluidos su origen, el estado de la importación y los metadatos relacionados. Esta tabla es esencial para realizar el seguimiento de las actividades de importación de documentos y diagnosticar los problemas que puedan surgir durante el proceso de importación.

## Descripción de las columnas

### id
- **Significado**: Un identificador único para cada entrada del registro de importación.
- **Función**: Clave primaria
- **Contenido típico**: Valores enteros secuenciales que identifican de forma única cada registro.

### org_id
- **Significado**: El identificador de la organización asociada a la importación.
- **Función**: Clave externa
- **Contenido típico**: UUID o identificador de cadena único similar que representa la organización.

### sub_org_id
- **Significado**: El identificador de una suborganización o departamento dentro de la organización principal.
- **Función**: Clave externa
- **Contenido típico**: UUID o identificador de cadena único similar; puede ser `None` si no procede.

### original_filename
- **Significado**: El nombre original del archivo del documento tal como se cargó.
- **Función**: Campo descriptivo
- **Contenido típico**: Cadena que representa el nombre del archivo, p. ej., `anton_invoice-1.pdf`.

### filename
- **Significado**: El nombre del archivo del documento una vez procesado o almacenado en el sistema.
- **Función**: Campo descriptivo
- **Contenido típico**: Cadena que representa el nombre del archivo, a menudo idéntico a `original_filename`.

### imported_on
- **Significado**: La fecha y la hora en que se importó el documento.
- **Función**: Campo descriptivo
- **Contenido típico**: Marca de tiempo con formato ISO 8601.

### source_type
- **Significado**: El tipo de origen desde el que se importó el documento.
- **Función**: Campo descriptivo
- **Contenido típico**: Cadena, p. ej., `EMAIL`, que indica el tipo de origen.

### source
- **Significado**: Información detallada sobre el origen de la importación.
- **Función**: Campo descriptivo
- **Contenido típico**: Cadena que detalla el origen, p. ej., `Email:O365:demo@fellow-digital.de:Tini Test`.

### success
- **Significado**: Indica si la importación se realizó correctamente.
- **Función**: Campo de estado
- **Contenido típico**: Valor booleano (`True` o `False`).

### created_by
- **Significado**: El identificador del usuario que inició la importación.
- **Función**: Clave externa
- **Contenido típico**: Entero que representa el ID de usuario.

### created_on
- **Significado**: La fecha y la hora en que se creó la entrada del registro de importación.
- **Función**: Campo técnico
- **Contenido típico**: Marca de tiempo con zona horaria.

### last_modified_on
- **Significado**: La fecha y la hora de la última modificación de la entrada del registro de importación.
- **Función**: Campo técnico
- **Contenido típico**: Marca de tiempo con zona horaria; puede ser `None` si no se ha modificado.

### is_deleted
- **Significado**: Indica si la entrada del registro de importación se ha marcado como eliminada.
- **Función**: Campo de estado
- **Contenido típico**: Valor booleano (`True` o `False`).

### import_id
- **Significado**: Un identificador único del proceso de importación.
- **Función**: Campo técnico
- **Contenido típico**: Cadena o texto que representa un ID de proceso único.

### extra_data
- **Significado**: Metadatos adicionales relacionados con la importación.
- **Función**: Campo descriptivo
- **Contenido típico**: Cadena JSON con datos adicionales, como fecha, remitente, asunto y recuento.

### doc_id
- **Significado**: El identificador del documento.
- **Función**: Clave externa
- **Contenido típico**: UUID o identificador de cadena único similar; puede ser `None`.

### email_connection_id
- **Significado**: El identificador de la conexión de correo electrónico utilizada en la importación.
- **Función**: Clave externa
- **Contenido típico**: Entero que representa el ID de la conexión de correo electrónico; puede ser `None`.

### subject
- **Significado**: La línea de asunto del correo electrónico desde el que se importó el documento.
- **Función**: Campo descriptivo
- **Contenido típico**: Cadena que representa el asunto del correo electrónico.

### body
- **Significado**: El contenido del cuerpo del correo electrónico desde el que se importó el documento.
- **Función**: Campo descriptivo
- **Contenido típico**: Texto con el contenido del cuerpo del correo electrónico; puede ser `None`.

### sender
- **Significado**: La dirección de correo electrónico del remitente del documento.
- **Función**: Campo descriptivo
- **Contenido típico**: Cadena con la dirección de correo electrónico del remitente.

### error_resp
- **Significado**: Respuesta o mensaje de error si la importación falló.
- **Función**: Campo de estado
- **Contenido típico**: Cadena con los detalles del error; puede ser `None`.

### source_received_on
- **Significado**: La fecha y la hora en que se recibió el documento desde el origen.
- **Función**: Campo descriptivo
- **Contenido típico**: Marca de tiempo con zona horaria.

Esta documentación ofrece una visión detallada de la tabla `public.document_import_log` y sus columnas, que son esenciales para comprender y gestionar las importaciones de documentos en el sistema.
```
