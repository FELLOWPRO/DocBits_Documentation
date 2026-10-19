# Document Script activation status

## Tabla `public.document_script_activation_status`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `sort_order`: integer
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `script_id`: interno

### Análisis y descripción

## Documentación de la tabla: `public.document_script_activation_status`

### Introducción

La tabla `public.document_script_activation_status` está diseñada para gestionar el estado de activación de los scripts asociados a los documentos dentro de una organización. Cada entrada de la tabla corresponde a un script concreto y a su estado de activación actual, lo que permite potencialmente a las organizaciones controlar y organizar la ejecución de scripts en relación con sus documentos.

### Descripción de las columnas

#### id

* **Significado**: Esta columna almacena un identificador único para cada entrada de la tabla.
* **Función**: Clave primaria.
* **Contenido típico**: Identificador único universal (UUID) como `c599a3fa-a784-446a-a48e-cf37b95d93cd`.
* **Nota**: Garantiza que cada registro sea identificable de forma única.

#### org\_id

* **Significado**: Representa el identificador de una organización.
* **Función**: Clave externa, que probablemente hace referencia a una tabla de organizaciones.
* **Contenido típico**: UUID que identifica la organización, p. ej., `23f3d697-7411-4c95-981d-faf089d266be`.
* **Nota**: Vincula el estado de activación del script con una organización concreta.

#### sort\_order

* **Significado**: Indica el orden en que deben ejecutarse o mostrarse los scripts.
* **Función**: Campo técnico.
* **Contenido típico**: Valores enteros que representan la secuencia, como `0`.
* **Nota**: Puede utilizarse para priorizar u organizar los scripts.

#### is\_active

* **Significado**: Indica si un script está activo actualmente.
* **Función**: Campo técnico.
* **Contenido típico**: Valores booleanos, `True` o `False`.
* **Nota**: Determina si debe ejecutarse el script asociado.

#### created\_by

* **Significado**: Identificador del usuario que creó el registro.
* **Función**: Clave externa, que probablemente hace referencia a una tabla de usuarios.
* **Contenido típico**: Valor entero que representa un ID de usuario, como `1`.
* **Nota**: Registra al creador del registro con fines de auditoría.

#### created\_on

* **Significado**: Marca de tiempo de cuándo se creó el registro.
* **Función**: Campo técnico.
* **Contenido típico**: Fecha y hora con zona horaria, p. ej., `2023-11-20 10:44:14.685170+00:00`.
* **Nota**: Proporciona una marca de tiempo de creación para el control de registros.

#### last\_modified\_on

* **Significado**: Marca de tiempo de la última modificación del registro.
* **Función**: Campo técnico.
* **Contenido típico**: Fecha y hora con zona horaria, o `None` si nunca se ha modificado.
* **Nota**: Útil para rastrear los cambios a lo largo del tiempo.

#### is\_deleted

* **Significado**: Indica si el registro está marcado como eliminado.
* **Función**: Campo técnico.
* **Contenido típico**: Valores booleanos, `True` o `False`.
* **Nota**: Permite la eliminación lógica de registros sin eliminarlos físicamente de la base de datos.

#### script\_id

* **Significado**: Identificador del script asociado al registro.
* **Función**: Clave externa, que probablemente hace referencia a una tabla de scripts.
* **Contenido típico**: UUID que identifica el script, p. ej., `4edc8cd7-e1bc-443a-9a23-dc490a09e80b`.
* **Nota**: Vincula el estado de activación con un script concreto.
