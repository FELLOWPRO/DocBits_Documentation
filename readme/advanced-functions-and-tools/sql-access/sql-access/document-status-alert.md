# Alerta de estado del documento

## Tabla `public.document_status_alert`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `doc_type_id`: interno
* `doc_type_key`: interno
* `doc_status`: interno
* `email_address`: text
* `send_to_assigned_user`: boolean
* `delay_delta`: integer
* `delay_delta_type`: interno
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean
* `name`: interno
* `is_recursive`: boolean
* `is_active`: boolean
* `priority`: interno
* `email_template_id`: interno

### Análisis y descripción

## Documentación de la tabla: `public.document_status_alert`

### Introducción

La tabla `public.document_status_alert` parece estar diseñada para gestionar las alertas relacionadas con los estados de los documentos dentro de una organización. Según los nombres de las columnas, la tabla almacena información sobre distintos tipos de documentos y sus estados, incluidos detalles sobre las notificaciones y los plazos de las alertas. Esta tabla se utiliza probablemente para activar alertas en función de determinados estados y condiciones de los documentos, posiblemente para notificar a los usuarios o escalar procesos.

### Descripción de las columnas

#### `id`

* **Significado**: Identificador único de cada registro de alerta.
* **Función**: Clave primaria.
* **Contenido típico**: Una cadena UUID que identifica de forma única cada fila de la tabla.

#### `org_id`

* **Significado**: Identificador de la organización asociada a la alerta.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID que enlaza con el registro de una organización.

#### `doc_type_id`

* **Significado**: Identificador del tipo de documento.
* **Función**: Clave externa (supuesta).
* **Contenido típico**: Normalmente un UUID, aunque los datos de ejemplo muestran `None`, lo que indica que este campo podría ser opcional.

#### `doc_type_key`

* **Significado**: Clave que representa el tipo de documento.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena como 'INVOICE' o 'XML\_INVOICE'.

#### `doc_status`

* **Significado**: Estado actual del documento.
* **Función**: Campo descriptivo.
* **Contenido típico**: Cadenas de estado descriptivas como 'validated\_pending\_approval' o 'error'.

#### `email_address`

* **Significado**: Dirección de correo electrónico a la que se envían las alertas.
* **Función**: Campo de notificación.
* **Contenido típico**: Una dirección de correo electrónico; puede ser `None` si no se especifica ninguna.

#### `send_to_assigned_user`

* **Significado**: Indica si la alerta debe enviarse al usuario asignado al documento.
* **Función**: Campo booleano.
* **Contenido típico**: `True` o `False`.

#### `delay_delta`

* **Significado**: Cantidad de tiempo que se retrasa la alerta.
* **Función**: Campo de temporización.
* **Contenido típico**: Entero que representa la duración del retraso.

#### `delay_delta_type`

* **Significado**: Unidad de tiempo de `delay_delta`.
* **Función**: Campo de temporización.
* **Contenido típico**: Normalmente 'minutes'.

#### `created_by`

* **Significado**: Identificador del usuario que creó el registro de la alerta.
* **Función**: Clave externa (supuesta).
* **Contenido típico**: Entero que representa un ID de usuario.

#### `created_on`

* **Significado**: Marca de tiempo de cuándo se creó el registro de la alerta.
* **Función**: Campo técnico.
* **Contenido típico**: Fecha y hora con información de zona horaria.

#### `last_modified_on`

* **Significado**: Marca de tiempo de la última modificación del registro de la alerta.
* **Función**: Campo técnico.
* **Contenido típico**: Fecha y hora con información de zona horaria; puede ser `None` si no se ha modificado.

#### `is_deleted`

* **Significado**: Indica si el registro de la alerta está marcado como eliminado.
* **Función**: Campo booleano.
* **Contenido típico**: `True` o `False`.

#### `name`

* **Significado**: Nombre o etiqueta de la alerta.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que representa el nombre de la alerta.

#### `is_recursive`

* **Significado**: Indica si la alerta debe repetirse a intervalos establecidos.
* **Función**: Campo booleano.
* **Contenido típico**: `True` o `False`.

#### `is_active`

* **Significado**: Indica si la alerta está activa actualmente.
* **Función**: Campo booleano.
* **Contenido típico**: `True` o `False`.

#### `priority`

* **Significado**: Nivel de prioridad de la alerta.
* **Función**: Campo descriptivo.
* **Contenido típico**: Pueden ser cadenas como 'High', 'Medium', 'Low'; los datos de ejemplo muestran `None`.

#### `email_template_id`

* **Significado**: Identificador de la plantilla de correo electrónico utilizada para la alerta.
* **Función**: Clave externa (supuesta).
* **Contenido típico**: Normalmente un UUID; los datos de ejemplo muestran `None`, lo que indica que este campo podría ser opcional.
