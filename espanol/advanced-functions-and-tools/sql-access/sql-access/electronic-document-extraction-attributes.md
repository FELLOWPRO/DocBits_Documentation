# Atributos de extracción de documentos electrónicos

## Tabla `public.electronic_document_extraction_attributes`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `doc_type_key`: interno
* `sub_doc_type_key`: interno
* `electronic_document_type`: interno
* `attribute_name`: interno
* `attribute_type`: interno
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean
* `deleted_on`: marca de tiempo con zona horaria
* `last_modified_by`: interno
* `deleted_by`: interno

### Análisis y descripción

## Documentación técnica de `public.electronic_document_extraction_attributes`

### Introducción

La tabla `public.electronic_document_extraction_attributes` parece gestionar los atributos relacionados con la extracción de documentos electrónicos. Esto implica almacenar diversas características y metadatos sobre los tipos de documentos electrónicos, sus métodos de procesamiento y las organizaciones asociadas. La tabla parece admitir funcionalidades como la identificación de tipos de documento, las transformaciones, las vistas previas y las descripciones de estructura, que son esenciales para tratar los documentos electrónicos de forma eficaz.

### Descripción de las columnas

#### id

* **Significado**: Un identificador único para cada registro de la tabla.
* **Función**: Clave primaria.
* **Contenido típico**: Una cadena UUID que identifica de forma única cada entrada de atributo de extracción de documentos.
* **Nota**: Sirve como referencia única de cada fila.

#### org\_id

* **Significado**: Identificador de la organización relacionada con los atributos del documento.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID que enlaza con la organización asociada.
* **Nota**: Conecta los atributos de extracción de documentos con una organización concreta.

#### doc\_type\_key

* **Significado**: Una clave que representa el tipo de documento.
* **Función**: Identificador para categorizar documentos.
* **Contenido típico**: Una cadena que indica el tipo de documento, como 'INVOICE' u 'ORDER\_CONFIRMATION'.
* **Nota**: Se utiliza para determinar la categoría del documento.

#### sub\_doc\_type\_key

* **Significado**: Representa una subcategoría del tipo de documento principal.
* **Función**: Identificador para una clasificación más detallada.
* **Contenido típico**: Nulo o una cadena de subtipo concreta.
* **Nota**: Útil para lograr una mayor granularidad en la clasificación de documentos.

#### electronic\_document\_type

* **Significado**: El formato o estándar del documento electrónico.
* **Función**: Campo descriptivo del formato del documento.
* **Contenido típico**: Cadenas como 'EDI' o 'FACTURX'.
* **Nota**: Indica el estándar o formato del documento.

#### attribute\_name

* **Significado**: El nombre del atributo relacionado con el proceso de extracción de documentos.
* **Función**: Campo descriptivo.
* **Contenido típico**: Cadenas como 'PREVIEW' o 'TRANSFORMATION'.
* **Nota**: Describe el atributo concreto relacionado con el tratamiento del documento.

#### attribute\_type

* **Significado**: El tipo del atributo relacionado con la extracción de documentos.
* **Función**: Campo descriptivo.
* **Contenido típico**: Cadenas como 'XSLT' o 'JSON'.
* **Nota**: Especifica el formato de datos o el método utilizado para el atributo.

#### created\_by

* **Significado**: ID del usuario que creó el registro.
* **Función**: Clave externa.
* **Contenido típico**: Entero que representa un ID de usuario.
* **Nota**: Registra quién creó inicialmente el registro.

#### created\_on

* **Significado**: Marca de tiempo de cuándo se creó el registro.
* **Función**: Campo técnico.
* **Contenido típico**: Fecha y hora en UTC.
* **Nota**: Indica la hora de creación del registro.

#### last\_modified\_on

* **Significado**: Marca de tiempo de la última modificación del registro.
* **Función**: Campo técnico.
* **Contenido típico**: Fecha y hora en UTC, o nulo si no se ha modificado.
* **Nota**: Registra la actualización más reciente del registro.

#### is\_deleted

* **Significado**: Indica si el registro está marcado como eliminado.
* **Función**: Campo técnico.
* **Contenido típico**: Valor booleano, `True` o `False`.
* **Nota**: Ayuda a gestionar la eliminación lógica.

#### deleted\_on

* **Significado**: Marca de tiempo de cuándo se marcó el registro como eliminado.
* **Función**: Campo técnico.
* **Contenido típico**: Fecha y hora en UTC, o una fecha muy antigua por defecto si no se ha eliminado.
* **Nota**: Se utiliza para registrar cuándo se eliminó el registro.

#### last\_modified\_by

* **Significado**: ID del usuario que modificó el registro por última vez.
* **Función**: Clave externa.
* **Contenido típico**: Cadena UUID, o nulo si no se ha modificado.
* **Nota**: Identifica al usuario responsable de la última modificación.

#### deleted\_by

* **Significado**: ID del usuario que marcó el registro como eliminado.
* **Función**: Clave externa.
* **Contenido típico**: Cadena UUID, o nulo si no se ha eliminado.
* **Nota**: Registra quién realizó la acción de eliminación.

Esta documentación ofrece una visión detallada de la estructura de la tabla y de sus columnas, lo que facilita su comprensión y su uso por parte de desarrolladores y administradores de bases de datos.
