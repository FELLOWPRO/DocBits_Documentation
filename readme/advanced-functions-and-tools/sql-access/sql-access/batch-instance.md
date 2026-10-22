# Instancia de lote

## Tabla `public.batch_instance`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean

### Análisis y descripción

## Documentación de la tabla: `public.batch_instance`

### Introducción

La tabla `public.batch_instance` está diseñada para almacenar información sobre las distintas instancias de lote dentro de una organización. Contiene metadatos clave de cada instancia, incluidos su identificación única, la organización a la que pertenece y los detalles de creación y modificación. Esta tabla es esencial para el seguimiento del ciclo de vida y la gestión de las instancias de lote, probablemente en una aplicación de software que trabaja con procesamiento por lotes.

### Columnas

#### `id`

* **Significado**: Esta columna almacena el identificador único de cada instancia de lote.
* **Función**: Clave primaria (`id`).
* **Contenido típico**: Una cadena UUID que identifica de forma única cada instancia de lote, p. ej., `'e9aa9ad7-6c36-4d7c-b31c-6e10bb8fbd87'`.

#### `org_id`

* **Significado**: Esta columna almacena el identificador de la organización asociada a la instancia de lote.
* **Función**: Clave externa (`org_id`).
* **Contenido típico**: Una cadena UUID que representa la organización, p. ej., `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### `created_by`

* **Significado**: Esta columna indica el usuario o la entidad del sistema que creó la instancia de lote.
* **Función**: Posiblemente una clave externa que hace referencia a una tabla de usuarios o similar.
* **Contenido típico**: Un entero que representa el ID del creador, p. ej., `1`.

#### `created_on`

* **Significado**: Esta columna registra la marca de tiempo de cuándo se creó la instancia de lote.
* **Función**: Campo técnico para fines de auditoría y seguimiento.
* **Contenido típico**: Una marca de tiempo con zona horaria, p. ej., `2021-09-22 10:55:59.755627+00`.

#### `last_modified_on`

* **Significado**: Esta columna recoge la marca de tiempo de la última modificación realizada en la instancia de lote.
* **Función**: Campo técnico para auditar los cambios.
* **Contenido típico**: Normalmente nulo, o una marca de tiempo con zona horaria si se han producido modificaciones.

#### `is_deleted`

* **Significado**: Esta columna indica si la instancia de lote está marcada como eliminada.
* **Función**: Campo técnico para la eliminación lógica.
* **Contenido típico**: Un valor booleano, normalmente `False` si la instancia está activa, p. ej., `False`.

Esta documentación ofrece una visión completa de la tabla `public.batch_instance` y detalla la finalidad y la estructura de cada columna, algo fundamental para los desarrolladores que trabajan con este modelo de datos.
