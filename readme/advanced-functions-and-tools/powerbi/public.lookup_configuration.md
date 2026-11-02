# public.lookup\_configuration

## Tabla `public.lookup_configuration`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `doc_type`: Tipo de documento
* `lookup_dataset_name`: interno
* `lookup_name`: interno
* `conflict_handle`: interno
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `match_all`: boolean
* `last_modified_by`: interno
* `deleted_by`: interno
* `context`: interno
* `context_detail`: interno

### Análisis y descripción

## Documentación técnica de la tabla `public.lookup_configuration`

### Introducción

La tabla `public.lookup_configuration` está diseñada para almacenar los ajustes de configuración de diversas operaciones de búsqueda de datos (lookup) dentro de una organización. Incluye información sobre la organización, el tipo de documentos implicados y los conjuntos de datos y nombres específicos utilizados en las búsquedas. La tabla también registra la creación y la modificación de estas configuraciones, así como su estado actual (activa o eliminada).

### Descripción de las columnas

#### id

* **Significado**: Un identificador único para cada entrada de configuración de lookup de la tabla.
* **Función**: Clave primaria que identifica de forma única cada fila.
* **Contenido típico**: Valores UUID, p. ej., `'68454d10-e045-4d64-8dd3-774bcb5b6013'`.

#### org\_id

* **Significado**: Representa la organización asociada con la configuración de lookup.
* **Función**: Clave externa que enlaza con una organización de otra tabla.
* **Contenido típico**: Valores UUID que indican identificadores de organización, p. ej., `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### doc\_type

* **Significado**: Especifica el tipo de documento al que se aplica la configuración de lookup.
* **Función**: Campo descriptivo que indica el contexto de la configuración.
* **Contenido típico**: Cadenas como `'MEDI_ORDER'`, `'INVOICE'`, etc.

#### lookup\_dataset\_name

* **Significado**: El nombre del conjunto de datos utilizado para realizar las búsquedas.
* **Función**: Campo descriptivo utilizado para identificar conjuntos de datos.
* **Contenido típico**: Cadenas descriptivas como `'customer_tini'`, `'supplier'`.

#### lookup\_name

* **Significado**: El nombre específico o alias utilizado para la operación de lookup.
* **Función**: Campo descriptivo que indica el nombre operativo.
* **Contenido típico**: Cadenas como `'customer_tini'`, `'supplier (copy)'`.

#### conflict\_handle

* **Significado**: Indica la estrategia para gestionar los conflictos durante las búsquedas.
* **Función**: Campo descriptivo de la estrategia de resolución de conflictos.
* **Contenido típico**: Valores como `'BEST_SCORE'`, `'RETURN_NONE'`.

#### created\_by

* **Significado**: El ID del usuario que creó la configuración de lookup.
* **Función**: Campo técnico para registrar quién creó la entrada.
* **Contenido típico**: Valores enteros que representan ID de usuario, p. ej., `1`.

#### created\_on

* **Significado**: Marca de tiempo de cuándo se creó la configuración de lookup.
* **Función**: Campo técnico para registrar la hora de creación.
* **Contenido típico**: Marcas de tiempo, p. ej., `2024-02-08 11:24:14 UTC`.

#### last\_modified\_on

* **Significado**: Marca de tiempo de la última modificación realizada en la configuración de lookup.
* **Función**: Campo técnico para registrar la hora de la última actualización.
* **Contenido típico**: Marcas de tiempo, normalmente `None` si no se ha modificado.

#### is\_deleted

* **Significado**: Indica si la configuración de lookup se ha marcado como eliminada.
* **Función**: Campo booleano para el seguimiento del estado.
* **Contenido típico**: Valores booleanos, `False` para las entradas activas.

#### deleted\_on

* **Significado**: Marca de tiempo de cuándo se marcó la configuración de lookup como eliminada.
* **Función**: Campo técnico para registrar la hora de eliminación.
* **Contenido típico**: A menudo se establece por defecto en una fecha de marcador de posición, p. ej., `0002-01-01 11:00:00 UTC`.

#### match\_all

* **Significado**: Especifica si el lookup debe cumplir todas las condiciones.
* **Función**: Campo booleano para los ajustes de configuración.
* **Contenido típico**: Valores booleanos, normalmente `False`.

#### last\_modified\_by

* **Significado**: El ID del usuario que modificó la configuración de lookup por última vez.
* **Función**: Campo técnico para registrar el usuario que actualizó la entrada por última vez.
* **Contenido típico**: UUID o identificador del usuario que la modificó, a menudo `None`.

#### deleted\_by

* **Significado**: El ID del usuario que marcó la configuración de lookup como eliminada.
* **Función**: Campo técnico para registrar el usuario responsable de la eliminación.
* **Contenido típico**: UUID o identificador, a menudo `None`.

#### context

* **Significado**: El contexto en el que se aplica el lookup, como una sección de un documento.
* **Función**: Campo descriptivo del contexto operativo.
* **Contenido típico**: Cadenas como `'header'`.

#### context\_detail

* **Significado**: Detalles adicionales sobre el contexto del lookup.
* **Función**: Campo descriptivo para información de contexto ampliada.
* **Contenido típico**: A menudo `None`; se utiliza para una descripción adicional del contexto.
