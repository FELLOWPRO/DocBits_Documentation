# Custom\_classification\_document\_label

## Tabla `public.custom_classification_document_label`

### Columnas

* `id`: integer
* `org_id`: ID de la organización
* `doc_id`: interno
* `label_id`: integer
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean

### Análisis y descripción

## Documentación técnica de la tabla `public.custom_classification_document_label`

### Introducción

La tabla `public.custom_classification_document_label` está diseñada para gestionar y almacenar las asociaciones entre documentos y sus etiquetas correspondientes dentro de una organización. Esta tabla facilita la categorización y la recuperación de documentos a partir de etiquetas personalizadas y ofrece una forma estructurada de gestionar la clasificación de documentos según las distintas necesidades de la organización.

### Descripción de las columnas

#### id

* **Significado**: Esta columna sirve como identificador único de cada registro de la tabla.
* **Función**: Clave primaria
* **Contenido típico**: Un valor entero que identifica de forma única cada fila.
* **Nota**: Cada entrada de la tabla tiene un `id` distinto para garantizar la integridad de los datos y permitir referencias eficientes.

#### org\_id

* **Significado**: Representa la organización a la que pertenece la asociación documento-etiqueta.
* **Función**: Clave externa
* **Contenido típico**: Una cadena de caracteres, probablemente un UUID, que identifica de forma única una organización.
* **Nota**: Garantiza que la asociación entre documentos y etiquetas se circunscriba al contexto organizativo correcto.

#### doc\_id

* **Significado**: Identifica el documento al que se aplica la etiqueta.
* **Función**: Clave externa
* **Contenido típico**: Una cadena de caracteres, probablemente un UUID, que identifica de forma única un documento.
* **Nota**: Permite vincular documentos concretos con etiquetas y hace posible la categorización de documentos.

#### label\_id

* **Significado**: Hace referencia a la etiqueta aplicada al documento.
* **Función**: Clave externa
* **Contenido típico**: Un entero que hace referencia a una etiqueta de una tabla de etiquetas independiente.
* **Nota**: Facilita la asociación entre los documentos y sus etiquetas correspondientes.

#### created\_by

* **Significado**: Identifica al usuario que creó el registro.
* **Función**: Clave externa (posiblemente a una tabla de usuarios)
* **Contenido típico**: Un entero que representa el ID del usuario.
* **Nota**: Registra el origen de cada asociación documento-etiqueta con fines de auditoría y responsabilidad.

#### created\_on

* **Significado**: Indica cuándo se creó el registro.
* **Función**: Campo técnico
* **Contenido típico**: Una marca de tiempo con información de zona horaria.
* **Nota**: Proporciona el contexto temporal de cuándo se estableció la relación documento-etiqueta.

#### last\_modified\_on

* **Significado**: Registra la marca de tiempo de la última modificación del registro.
* **Función**: Campo técnico
* **Contenido típico**: Una marca de tiempo con información de zona horaria; puede ser `None` si nunca se ha modificado.
* **Nota**: Útil para rastrear el historial de cambios de las asociaciones documento-etiqueta.

#### is\_deleted

* **Significado**: Indica si el registro se ha marcado como eliminado.
* **Función**: Campo técnico
* **Contenido típico**: Un valor booleano (`True` o `False`).
* **Nota**: Admite prácticas de eliminación lógica, que permiten retirar datos de forma lógica sin eliminarlos físicamente de la base de datos.
