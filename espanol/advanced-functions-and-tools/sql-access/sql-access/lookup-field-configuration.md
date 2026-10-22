# Configuración del campo de búsqueda

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
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean
* `deleted_on`: marca de tiempo con zona horaria
* `search_operator`: interno
* `last_modified_by`: interno
* `deleted_by`: interno

### Análisis y descripción

## Documentación de la tabla: `public.lookup_field_configuration`

### Introducción

La tabla `public.lookup_field_configuration` parece ser una tabla de configuración que sirve para definir y gestionar los campos de lookup dentro de una aplicación. La tabla incluye metadatos de cada campo, como su identificador, la organización asociada, la posibilidad de búsqueda y la información de auditoría. Probablemente forma parte de un sistema más amplio para gestionar campos dinámicos o definidos por el usuario, y permite realizar consultas complejas y configuraciones avanzadas.

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

* **Significado**: Un identificador del registro de lookup concreto al que se aplica esta configuración.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID que hace referencia a un registro de lookup concreto.

#### `field_id`

* **Significado**: El identificador del campo que se configura.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID que hace referencia a un campo determinado.

#### `lookup_field`

* **Significado**: El nombre o la etiqueta del campo que se configura.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que representa el nombre del campo, como "address\_1" o "taxratefree".

#### `is_searchable`

* **Significado**: Indica si el campo puede incluirse en las operaciones de búsqueda.
* **Función**: Indicador de configuración.
* **Contenido típico**: Un valor booleano (`True` o `False`).

#### `parent_field_id`

* **Significado**: Identificador del campo principal (padre), si procede.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID o `None` si no existe un campo principal.

#### `auto_trigger`

* **Significado**: Especifica si la configuración del campo debe desencadenar automáticamente determinadas acciones.
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
* **Función**: Indicador de eliminación lógica.
* **Contenido típico**: Un valor booleano (`True` o `False`).

#### `deleted_on`

* **Significado**: La marca de tiempo de cuándo se marcó como eliminada la entrada de configuración.
* **Función**: Campo de auditoría.
* **Contenido típico**: Una marca de tiempo con información de zona horaria, o `None` si no se ha eliminado.

#### `search_operator`

* **Significado**: Define el operador de búsqueda que se utiliza para el campo.
* **Función**: Campo de configuración.
* **Contenido típico**: Una cadena como "contains" que indica el tipo de operación de búsqueda.

#### `last_modified_by`

* **Significado**: Identificador del usuario que modificó por última vez la entrada de configuración.
* **Función**: Campo de auditoría.
* **Contenido típico**: Una cadena UUID o `None` si nunca se ha modificado.

#### `deleted_by`

* **Significado**: Identificador del usuario que marcó la entrada como eliminada.
* **Función**: Campo de auditoría.
* **Contenido típico**: Una cadena UUID o `None` si no se ha eliminado.

Esta documentación ofrece una visión detallada de la estructura y la finalidad de cada columna de la tabla `public.lookup_field_configuration` y proporciona a los desarrolladores una comprensión completa de cómo se configuran y gestionan los campos de lookup dentro del sistema.
