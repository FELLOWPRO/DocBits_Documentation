# Document status trigger

## Tabla `public.document_status_trigger`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `trigger_doc_type`: interno
* `trigger_doc_status`: interno
* `trigger_url`: interno
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Análisis y descripción

## Documentación técnica de la tabla `public.document_status_trigger`

### Introducción

La tabla `public.document_status_trigger` está diseñada para gestionar y rastrear el estado de los documentos dentro de una organización. Esta tabla parece gestionar los desencadenadores relacionados con el procesamiento de documentos, probablemente en un sistema de flujos de trabajo. Recoge información sobre los tipos de documento y sus cambios de estado, y puede desencadenar acciones o flujos de trabajo a través de URL especificadas.

### Descripción de las columnas

#### id

* **Significado**: Esta columna almacena un identificador único para cada registro de la tabla.
* **Función**: Clave primaria.
* **Contenido típico**: Una cadena UUID, p. ej., `8103b700-c03c-40cb-9322-e9e1ddbe0cb1`.

#### org\_id

* **Significado**: Representa el identificador único de una organización.
* **Función**: Clave externa que enlaza con una entidad de organización.
* **Contenido típico**: Una cadena UUID, p. ej., `23f3d697-7411-4c95-981d-faf089d266be`.

#### trigger\_doc\_type

* **Significado**: Especifica el tipo de documento asociado al desencadenador.
* **Función**: Campo descriptivo que indica el tipo de documento.
* **Contenido típico**: Nombres de tipos de documento, como `INVOICE`.

#### trigger\_doc\_status

* **Significado**: Indica el estado concreto del documento que activa el desencadenador.
* **Función**: Campo descriptivo que detalla el estado del documento.
* **Contenido típico**: Descripciones de estado, como `approved_pending_second_approval`.

#### trigger\_url

* **Significado**: URL que se invoca cuando el estado del documento cumple determinadas condiciones.
* **Función**: Campo técnico para la automatización de flujos de trabajo.
* **Contenido típico**: URL, p. ej., `https://test-wf-stage.workflow.polydocs.io/webhook/3c3ab41b-a1d9-40a9-8e33-2968d33c989e/webhook`.

#### is\_active

* **Significado**: Indica si el desencadenador está activo actualmente.
* **Función**: Campo técnico para gestionar los estados del desencadenador.
* **Contenido típico**: Valores booleanos, `True` o `False`.

#### created\_by

* **Significado**: Identifica al usuario que creó el registro.
* **Función**: Clave externa a una entidad de usuario.
* **Contenido típico**: ID de usuario enteros, p. ej., `1`.

#### created\_on

* **Significado**: Marca de tiempo de cuándo se creó el registro.
* **Función**: Campo técnico para la auditoría y el seguimiento de cambios.
* **Contenido típico**: Marcas de tiempo con zona horaria, p. ej., `2022-09-16 07:26:55 UTC`.

#### last\_modified\_on

* **Significado**: Marca de tiempo de la última modificación del registro.
* **Función**: Campo técnico para la auditoría y el seguimiento de cambios.
* **Contenido típico**: Marcas de tiempo con zona horaria; puede ser `None` si no se ha modificado.

#### is\_deleted

* **Significado**: Indica si el registro se considera eliminado o inactivo.
* **Función**: Campo técnico para la eliminación lógica.
* **Contenido típico**: Valores booleanos, `True` o `False`.

Esta tabla ofrece un enfoque estructurado para gestionar los estados de los documentos y los desencadenadores asociados dentro del sistema de flujos de trabajo de una organización, de modo que puedan ejecutarse acciones automáticamente a medida que los documentos avanzan por los distintos estados.
