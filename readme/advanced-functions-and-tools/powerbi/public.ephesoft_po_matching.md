# public.ephesoft\_po\_matching

## Tabla `public.ephesoft_po_matching`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `doc_id`: interno
* `doc_type`: Tipo de documento
* `ephesoft_doc_id`: interno
* `extracted_data`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Análisis y descripción

## Documentación técnica de la tabla `public.ephesoft_po_matching`

### Introducción

La tabla `public.ephesoft_po_matching` está diseñada para almacenar y gestionar datos relacionados con la coincidencia de pedidos de compra con documentos, como facturas, procesados por el sistema Ephesoft. Esta tabla recoge diversos detalles sobre los documentos, su proceso de extracción y el estado de coincidencia con los pedidos de compra.

### Descripción de las columnas

#### id

* **Significado**: Un identificador único para cada registro de la tabla, que probablemente representa un documento o una transacción procesados concretos.
* **Función**: Clave primaria.
* **Contenido típico**: Identificador único universal (UUID) en formato de cadena, p. ej., `ea587c89-0d4f-4a47-a3ac-89cfb2bed9cb`.

#### org\_id

* **Significado**: Identificador de la organización asociada con el documento o la transacción.
* **Función**: Clave externa, posiblemente con enlace a una tabla de organizaciones.
* **Contenido típico**: UUID en formato de cadena, p. ej., `23f3d697-7411-4c95-981d-faf089d266be`.

#### doc\_id

* **Significado**: Identificador del documento procesado por el sistema.
* **Función**: Clave externa, con enlace a una tabla de documentos o similar.
* **Contenido típico**: UUID en formato de cadena, p. ej., `f46c6c90-568b-42ee-ae71-c5a3c22211de`.

#### doc\_type

* **Significado**: Tipo del documento procesado, que indica la naturaleza del documento (p. ej., INVOICE).
* **Función**: Campo descriptivo.
* **Contenido típico**: Cadena que indica el tipo de documento, p. ej., `INVOICE`.

#### ephesoft\_doc\_id

* **Significado**: Identificador utilizado por el sistema Ephesoft para realizar el seguimiento del documento.
* **Función**: Campo descriptivo.
* **Contenido típico**: Cadena corta, posiblemente un identificador, p. ej., `DOC1`.

#### extracted\_data

* **Significado**: Datos JSON que contienen la información extraída del documento, incluidos campos, tablas y metadatos.
* **Función**: Campo de almacenamiento de datos para el contenido extraído del documento.
* **Contenido típico**: Estructura JSON con detalles como el tipo de documento, los campos, las tablas y los metadatos.

#### created\_by

* **Significado**: Identificador del usuario o del sistema que creó el registro.
* **Función**: Clave externa, posiblemente con enlace a una tabla de usuarios.
* **Contenido típico**: Entero que representa el ID de usuario, p. ej., `1`.

#### created\_on

* **Significado**: Marca de tiempo de cuándo se creó el registro.
* **Función**: Campo técnico para el seguimiento de registros.
* **Contenido típico**: Marca de tiempo con zona horaria, p. ej., `2022-02-19 10:43:37 UTC`.

#### last\_modified\_on

* **Significado**: Marca de tiempo de la última modificación del registro.
* **Función**: Campo técnico para el seguimiento de registros.
* **Contenido típico**: Marca de tiempo con zona horaria; puede ser nula si no se ha modificado desde su creación.

#### is\_deleted

* **Significado**: Indicador que señala si el registro está marcado como eliminado.
* **Función**: Campo técnico para el borrado lógico.
* **Contenido típico**: Booleano, `true` si el registro está eliminado y `false` en caso contrario.
