# public.custom\_classification\_document

## Tabla `public.custom_classification_document`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `first_page_content`: text
* `content`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Análisis y descripción

## Documentación técnica de la tabla `public.custom_classification_document`

### Introducción

La tabla `public.custom_classification_document` está diseñada para almacenar información detallada sobre la clasificación de documentos dentro de una organización. Esto incluye metadatos del documento, como su contenido, los detalles de su creación y el contexto organizativo. La estructura de la tabla sugiere su uso en la gestión de documentos relacionados con procesos de la organización, posiblemente facturas o formularios de pedido, según se deduce de los datos de ejemplo.

### Descripción de las columnas

#### id

* **Significado**: Esta columna probablemente almacena un identificador único para cada entrada de documento.
* **Función**: Clave primaria
* **Contenido típico**: Un UUID que representa un identificador único de documento.

#### org\_id

* **Significado**: Esta columna almacena el identificador de la organización asociada con el documento.
* **Función**: Clave externa
* **Contenido típico**: Un UUID que vincula el documento con una organización específica.

#### first\_page\_content

* **Significado**: Esta columna contiene el contenido de texto de la primera página del documento.
* **Función**: Campo de datos
* **Contenido típico**: Representación textual de un documento de una organización, que posiblemente incluye encabezados, direcciones y los detalles iniciales de una factura o un pedido.

#### content

* **Significado**: Esta columna almacena el contenido de texto completo del documento.
* **Función**: Campo de datos
* **Contenido típico**: Contenido textual completo del documento, incluidos todos los detalles presentes en la primera página y en las páginas siguientes.

#### created\_by

* **Significado**: Esta columna indica el usuario que creó la entrada del documento.
* **Función**: Campo de datos
* **Contenido típico**: Un entero que representa el ID de usuario del creador.

#### created\_on

* **Significado**: Esta columna registra la fecha y la hora en que se creó la entrada del documento.
* **Función**: Campo técnico
* **Contenido típico**: Una marca de tiempo con información de zona horaria que indica la fecha y la hora de creación.

#### last\_modified\_on

* **Significado**: Esta columna almacena la fecha y la hora de la última modificación de la entrada del documento.
* **Función**: Campo técnico
* **Contenido típico**: Una marca de tiempo con información de zona horaria que indica la fecha y la hora de la última modificación. En ocasiones es `None` si no se han producido modificaciones tras la creación.

#### is\_deleted

* **Significado**: Esta columna indica si la entrada del documento se ha marcado como eliminada.
* **Función**: Campo técnico
* **Contenido típico**: Un valor booleano (`True` o `False`) que muestra el estado de eliminación de la entrada del documento.

Esta tabla ofrece una estructura sólida para gestionar los datos de los documentos, de modo que cada documento pueda identificarse de forma única, asociarse con una organización y seguirse a lo largo de su ciclo de vida de creación y modificación.
