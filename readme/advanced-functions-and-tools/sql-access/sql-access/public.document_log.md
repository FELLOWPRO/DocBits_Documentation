# public.document\_log

## Tabla `public.document_log`

### Columnas

* `id`: integer
* `org_id`: ID de la organización
* `doc_id`: interno
* `action_type`: interno
* `action_description`: text
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean
* `is_hidden`: boolean
* `previous_status`: interno
* `current_status`: interno

### Análisis y descripción

## Documentación técnica: tabla `public.document_log`

### Introducción

La tabla `public.document_log` está diseñada para registrar el historial y los cambios de estado de los documentos dentro de una organización. Registra las acciones realizadas sobre los documentos, como las actualizaciones de estado, junto con los detalles del usuario que realizó la acción y las marcas de tiempo que indican cuándo se produjeron. Esta tabla es fundamental para auditar los flujos de procesamiento de documentos y comprender el ciclo de vida de cada documento.

### Descripción de las columnas

#### id

* **Significado**: Identificador único de cada entrada del registro.
* **Función**: Clave primaria. Esta columna sirve como identificador único de cada registro de la tabla.
* **Contenido típico**: Valores enteros que se incrementan con cada nueva entrada.

#### org\_id

* **Significado**: Identificador de la organización asociada al documento.
* **Función**: Clave externa. Enlaza con una entidad de organización, aunque no se define de forma explícita en este contexto.
* **Contenido típico**: Cadenas de caracteres, probablemente UUID, que representan identificadores de organización.

#### doc\_id

* **Significado**: Identificador del documento asociado a la entrada del registro.
* **Función**: Clave externa. Esta columna hace referencia a un documento concreto del sistema.
* **Contenido típico**: Cadenas de caracteres, probablemente UUID, que representan identificadores de documento.

#### action\_type

* **Significado**: Tipo de acción registrada.
* **Función**: Campo descriptivo. Indica la categoría de la acción realizada.
* **Contenido típico**: Cadenas como `STATUS_CHANGE`, que indican la naturaleza de la acción.

#### action\_description

* **Significado**: Descripción detallada de la acción realizada.
* **Función**: Campo descriptivo. Aporta contexto o detalles sobre la acción.
* **Contenido típico**: Descripciones de texto, p. ej., "Data extraction started", "Error occurred processing document".

#### created\_by

* **Significado**: Identificador del usuario que creó la entrada del registro.
* **Función**: Clave externa. Enlaza con una entidad de usuario e indica quién realizó la acción.
* **Contenido típico**: Valores enteros que representan identificadores de usuario.

#### created\_on

* **Significado**: Marca de tiempo de cuándo se creó la entrada del registro.
* **Función**: Campo técnico. Registra el momento exacto en que se anotó una acción.
* **Contenido típico**: Marcas de tiempo con información de zona horaria, p. ej., `2025-04-01 13:07:51.291193 UTC`.

#### last\_modified\_on

* **Significado**: Marca de tiempo de la última modificación de la entrada del registro.
* **Función**: Campo técnico. Indica el momento de la última actualización de la entrada.
* **Contenido típico**: Marcas de tiempo; pueden ser nulas si no se modificó tras la creación.

#### is\_deleted

* **Significado**: Indicador que señala si la entrada del registro está marcada como eliminada.
* **Función**: Campo técnico. Se utiliza para la eliminación lógica de entradas.
* **Contenido típico**: Valores booleanos: `False` indica entradas activas y `True`, entradas eliminadas.

#### is\_hidden

* **Significado**: Indicador que señala si la entrada del registro está oculta de la vista normal.
* **Función**: Campo técnico. Se utiliza para controlar la visibilidad de las entradas del registro.
* **Contenido típico**: Valores booleanos: `False` indica entradas visibles y `True`, entradas ocultas.

#### previous\_status

* **Significado**: Estado del documento antes de realizar la acción.
* **Función**: Campo descriptivo. Indica el estado del documento previo a la acción registrada.
* **Contenido típico**: Cadenas como `new`, `validating`, `running`, que representan estados del documento.

#### current\_status

* **Significado**: Estado del documento después de realizar la acción.
* **Función**: Campo descriptivo. Indica el estado actualizado del documento tras la acción.
* **Contenido típico**: Cadenas como `running`, `ready_for_validation`, `error`, que representan estados del documento.

Esta documentación ofrece una visión general de la tabla `public.document_log` y detalla la finalidad y la estructura de cada columna, algo fundamental para los desarrolladores que gestionan flujos de trabajo de documentos y mantienen pistas de auditoría.
