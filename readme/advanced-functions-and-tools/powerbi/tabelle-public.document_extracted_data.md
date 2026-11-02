# Tabla public.document\_extracted\_data

## Columnas

* `id`: internal
* `org_id`: ID to organisation
* `doc_id`: internal
* `field_name`: internal
* `field_value`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `field_type`: internal

## Análisis y descripción

```markdown
# Documentación técnica de la tabla `public.document_extracted_data`

## Introducción

La tabla `public.document_extracted_data` está diseñada para almacenar los datos extraídos de diversos documentos, probablemente con fines de procesamiento y análisis de documentos. Cada entrada de la tabla corresponde a un campo específico extraído de un documento, como una factura, e incluye metadatos sobre el proceso de extracción. La tabla facilita el seguimiento y la gestión de los datos de los documentos al asociarlos con organizaciones y documentos concretos.

## Descripción de las columnas

### id
- **Significado**: Un identificador único para cada entrada de datos extraídos.
- **Función**: Clave primaria.
- **Contenido típico**: Una cadena con formato UUID que identifica de forma única el registro de datos extraídos.

### org_id
- **Significado**: Identificador de la organización asociada a los datos del documento.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena con formato UUID que representa la organización.

### doc_id
- **Significado**: Identificador del documento del que se han extraído los datos.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena con formato UUID que representa el documento.

### field_name
- **Significado**: El nombre del campo extraído del documento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadenas como 'invoice_id', 'invoice_date', etc., que indican el tipo de dato extraído.

### field_value
- **Significado**: El valor asociado al campo extraído.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadenas que representan diversos tipos de datos, como números de factura, fechas o importes.

### created_by
- **Significado**: El identificador del usuario o proceso que creó la entrada de datos.
- **Función**: Campo técnico.
- **Contenido típico**: Entero que representa un ID de usuario o un ID de proceso.

### created_on
- **Significado**: La marca de tiempo del momento en que se creó la entrada de datos.
- **Función**: Campo técnico.
- **Contenido típico**: Marca de tiempo con datos de zona horaria que indica la fecha y la hora de creación.

### last_modified_on
- **Significado**: La marca de tiempo de la última modificación realizada en la entrada de datos.
- **Función**: Campo técnico.
- **Contenido típico**: Marca de tiempo con datos de zona horaria que indica la fecha y la hora de la última modificación (puede ser nula si nunca se ha modificado).

### is_deleted
- **Significado**: Un indicador que señala si la entrada de datos se ha marcado como eliminada.
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano, donde `False` indica entradas activas y `True` indica entradas eliminadas.

### field_type
- **Significado**: El tipo de dato almacenado en la columna `field_value`.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadenas como 'date', 'AMOUNT', o nulo si no se ha especificado el tipo.

Este modelo de datos estructurado permite el almacenamiento y la recuperación eficientes de los datos relacionados con documentos y admite una amplia gama de aplicaciones, desde el procesamiento de facturas hasta la gestión del cumplimiento normativo.
```
