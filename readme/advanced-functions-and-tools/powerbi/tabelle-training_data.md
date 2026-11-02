# Tabla training\_data

## Tabla `public.training_data`

### Columnas

* `id`: internal
* `org_id`: ID to organisation
* `doc_type`: DOC Type
* `doc_origin`: Doc Origin
* `doc_locale`: Doc Locale
* `doc_language`: Language
* `first_page_content`: text
* `supplier_name`: Supplier Name
* `supplier_vat`: internal
* `doc_created_on`: timestamp with time zone
* `is_training_sample`: boolean
* `sample_doc_id`: internal
* `sample_file_name`: internal
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_table_training_sample`: boolean

### Análisis y descripción

## Documentación técnica de la tabla `public.training_data`

### Introducción

La tabla `public.training_data` parece estar diseñada para almacenar diversos datos relacionados con documentos, probablemente utilizados para entrenar modelos o sistemas que procesan y analizan el contenido de los documentos. La tabla incluye información sobre el tipo de documento, el origen, el idioma, los datos del proveedor y las marcas de tiempo relacionadas con la creación y la modificación de los registros, entre otros atributos. Parece centrarse especialmente en facturas y recibos médicos, lo que sugiere su uso en aplicaciones de procesamiento de datos financieros o sanitarios.

### Descripción de las columnas

#### id

* **Significado**: Identificador único de cada registro de la tabla.
* **Función**: Clave primaria.
* **Contenido típico**: Un identificador único universal (UUID) en formato de caracteres.
* **Nota**: Imprescindible para identificar de forma única cada entrada.

#### org\_id

* **Significado**: Identificador de la organización asociada al documento.
* **Función**: Clave externa que enlaza con un registro de organización.
* **Contenido típico**: UUID que representa una organización.
* **Nota**: Ayuda a asociar los documentos con organizaciones concretas.

#### doc\_type

* **Significado**: Tipo de documento almacenado en el registro.
* **Función**: Campo descriptivo.
* **Contenido típico**: Valores como 'INVOICE' o 'MEDICAL\_RECEIPT'.
* **Nota**: Útil para categorizar los documentos.

#### doc\_origin

* **Significado**: Origen o código del país de procedencia del documento.
* **Función**: Campo descriptivo.
* **Contenido típico**: Código de país como 'DE' para Alemania.
* **Nota**: Indica el origen geográfico del documento.

#### doc\_locale

* **Significado**: Información de configuración regional del documento.
* **Función**: Campo descriptivo.
* **Contenido típico**: Código de configuración regional como 'en\_DE'.
* **Nota**: Combina idioma y región con fines de localización.

#### doc\_language

* **Significado**: Idioma en el que está redactado el documento.
* **Función**: Campo descriptivo.
* **Contenido típico**: Código de idioma como 'en' o 'de'.
* **Nota**: Indica el idioma principal utilizado en el documento.

#### first\_page\_content

* **Significado**: Contenido de la primera página del documento.
* **Función**: Campo descriptivo.
* **Contenido típico**: Datos de texto que contienen el contenido de la primera página del documento.
* **Nota**: Puede utilizarse para el análisis o el procesamiento de texto.

#### supplier\_name

* **Significado**: Nombre del proveedor asociado al documento.
* **Función**: Campo descriptivo.
* **Contenido típico**: Nombre del proveedor en formato de texto.
* **Nota**: Importante para identificar el origen o el emisor del documento.

#### supplier\_vat

* **Significado**: Número de identificación a efectos del IVA del proveedor.
* **Función**: Campo descriptivo.
* **Contenido típico**: NIF-IVA, por ejemplo, 'DE 129375678'.
* **Nota**: Útil para procesos fiscales y tributarios.

#### doc\_created\_on

* **Significado**: Marca de tiempo del momento en que se creó el documento.
* **Función**: Campo descriptivo.
* **Contenido típico**: Fecha y hora en formato UTC.
* **Nota**: Proporciona el contexto temporal de la creación del documento.

#### is\_training\_sample

* **Significado**: Indicador que señala si el registro se utiliza como muestra de entrenamiento.
* **Función**: Campo técnico.
* **Contenido típico**: Valor booleano (`True` o `False`).
* **Nota**: Identifica los registros marcados específicamente con fines de entrenamiento.

#### sample\_doc\_id

* **Significado**: Identificador del documento de muestra.
* **Función**: Campo descriptivo o posible clave externa.
* **Contenido típico**: UUID que enlaza con otro documento.
* **Nota**: Puede hacer referencia a un documento relacionado u original utilizado para el muestreo.

#### sample\_file\_name

* **Significado**: Nombre del archivo asociado a la muestra del documento.
* **Función**: Campo descriptivo.
* **Contenido típico**: Nombre de archivo en formato de texto.
* **Nota**: Útil para los procesos de gestión o recuperación de archivos.

#### created\_on

* **Significado**: Marca de tiempo del momento en que se creó el registro.
* **Función**: Campo técnico.
* **Contenido típico**: Fecha y hora en formato UTC.
* **Nota**: Indica cuándo se añadió el registro a la base de datos.

#### last\_modified\_on

* **Significado**: Marca de tiempo de la última modificación del registro.
* **Función**: Campo técnico.
* **Contenido típico**: Fecha y hora en formato UTC.
* **Nota**: Registra cuándo se actualizó el registro por última vez.

#### is\_deleted

* **Significado**: Indicador que señala si el registro se ha marcado como eliminado.
* **Función**: Campo técnico.
* **Contenido típico**: Valor booleano (`True` o `False`).
* **Nota**: Admite la funcionalidad de eliminación lógica (soft delete).

#### is\_table\_training\_sample

* **Significado**: Indicador que señala si el registro es una muestra de entrenamiento específica de tablas.
* **Función**: Campo técnico.
* **Contenido típico**: Valor booleano (`True` o `False`).
* **Nota**: Se diferencia de las muestras de entrenamiento generales y se centra en los datos de tablas.
