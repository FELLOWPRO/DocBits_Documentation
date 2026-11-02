# public.lookup\_field\_configuration

## Tabla `public.lookup_field_configuration`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `lookup_rec_id`: interno
* `field_id`: interno
* `lookup_field`: interno
* `is_searchable`: boolean
* `parent_field_id`: interno
* `auto_trigger`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `search_operator`: interno
* `last_modified_by`: interno
* `deleted_by`: interno

### Análisis y descripción

## Documentación de la tabla: `public.lookup_field_configuration`

### Introducción

La tabla `public.lookup_field_configuration` parece ser una tabla de configuración utilizada para definir y gestionar campos de lookup dentro de una aplicación. La tabla incluye metadatos de cada campo, como su identificador, la organización asociada, la capacidad de búsqueda y la información de auditoría. Esta tabla probablemente forma parte de un sistema más amplio para gestionar campos dinámicos o definidos por el usuario, que permite realizar consultas complejas y ofrece capacidades de configuración.

### Descripción de las columnas

#### `id`

* **Significado**: El identificador único de cada registro de la tabla.
* **Función**: Clave primaria.
* **Contenido típico**: Una cadena UUID que identifica de forma única cada entrada de configuración.

#### `org_id`

* **Significado**: El identificador de la organización a la que está asociada esta configuración.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID que representa la organización.

#### `lookup_rec_id`

* **Significado**: Un identificador del registro de lookup específico al que se aplica esta configuración.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID que hace referencia a un registro de lookup específico.

#### `field_id`

* **Significado**: El identificador del campo que se está configurando.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID que hace referencia a un campo concreto.

#### `lookup_field`

* **Significado**: El nombre o la etiqueta del campo que se está configurando.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que representa el nombre del campo, como "address\_1" o "taxratefree".

#### `is_searchable`

* **Significado**: Indica si el campo puede incluirse en las operaciones de búsqueda.
* **Función**: Indicador de configuración.
* **Contenido típico**: Un valor booleano (`True` o `False`).

#### `parent_field_id`

* **Significado**: Identificador del campo principal, si procede.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID o `None` si no existe un campo principal.

#### `auto_trigger`

* **Significado**: Especifica si la configuración del campo debe activar automáticamente determinadas acciones.
* **Función**: Indicador de configuración.
* **Contenido típico**: Un valor booleano (`True` o `False`).

#### `created_by`

* **Significado**: El identificador del usuario que creó la entrada de configuración.
* **Función**: Campo de auditoría.
* **Contenido típico**: Un entero que representa el ID de usuario.

#### `created_on`

* **Significado**: La marca de tiempo de cuándo se creó la entrada de configuración.
* **Función**: Campo de auditoría.
* **Contenido típico**: Una marca de tiempo con información de zona horaria.

#### `last_modified_on`

* **Significado**: La marca de tiempo de la modificación más reciente de la entrada de configuración.
* **Función**: Campo de auditoría.
* **Contenido típico**: Una marca de tiempo con información de zona horaria, o `None` si nunca se ha modificado.

#### `is_deleted`

* **Significado**: Indica si la entrada de configuración se ha marcado como eliminada.
* **Función**: Indicador de borrado lógico.
* **Contenido típico**: Un valor booleano (`True` o `False`).

#### `deleted_on`

* **Significado**: La marca de tiempo de cuándo se marcó la entrada de configuración como eliminada.
* **Función**: Campo de auditoría.
* **Contenido típico**: Una marca de tiempo con información de zona horaria, o `None` si no se ha eliminado.

#### `search_operator`

* **Significado**: Define el operador de búsqueda utilizado para el campo.
* **Función**: Campo de configuración.
* **Contenido típico**: Una cadena como "contains" que indica el tipo de operación de búsqueda.

#### `last_modified_by`

* **Significado**: Identificador del usuario que modificó la entrada de configuración por última vez.
* **Función**: Campo de auditoría.
* **Contenido típico**: Una cadena UUID o `None` si nunca se ha modificado.

#### `deleted_by`

* **Significado**: Identificador del usuario que marcó la entrada como eliminada.
* **Función**: Campo de auditoría.
* **Contenido típico**: Una cadena UUID o `None` si no se ha eliminado.

Esta documentación ofrece una visión detallada de la estructura y la finalidad de cada columna de la tabla `public.lookup_field_configuration`, y proporciona a los desarrolladores una comprensión completa de cómo se configuran y gestionan los campos de lookup dentro del sistema.
