# Tabla public.document\_report

## Columnas

* `id`: internal
* `org_id`: ID to organisation
* `doc_id`: internal
* `doc_type`: DOC Type
* `sub_doc_type`: internal
* `time_spent`: internal
* `fields_total`: integer
* `fields_correct`: integer
* `checkbox_fields_total`: integer
* `checkbox_fields_correct`: integer
* `table_values_total`: integer
* `table_values_correct`: integer
* `detail_report`: text
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `validated_by`: integer
* `sub_org_id`: internal

## Análisis y descripción

```markdown
# Documentación de la tabla Document Report

## Introducción
La tabla `public.document_report` está diseñada para almacenar información detallada sobre los informes de procesamiento de documentos, en concreto los relacionados con la validación y la extracción de campos de documentos como las facturas. La tabla recoge metadatos del documento, métricas de procesamiento y resultados de validación, que pueden utilizarse para la auditoría, el seguimiento y la mejora de los flujos de trabajo de procesamiento de documentos.

## Descripción de las columnas

### id
- **Significado**: Identificador único de cada entrada del informe de documento.
- **Función**: Clave primaria
- **Contenido típico**: Un UUID que representa el informe de documento único.

### org_id
- **Significado**: Identificador de la organización asociada al documento.
- **Función**: Clave externa
- **Contenido típico**: Un UUID que enlaza con una organización.

### doc_id
- **Significado**: Identificador del documento concreto sobre el que se informa.
- **Función**: Clave externa
- **Contenido típico**: Un UUID que representa el documento único.

### doc_type
- **Significado**: Tipo del documento que se está procesando, por ejemplo, una factura.
- **Función**: Campo descriptivo
- **Contenido típico**: Valores como `INVOICE`.

### sub_doc_type
- **Significado**: Subtipo del documento, que proporciona una categorización adicional.
- **Función**: Campo descriptivo
- **Contenido típico**: Puede ser `null` o subtipos específicos como "Cost Invoice".

### time_spent
- **Significado**: Tiempo dedicado a la validación del documento.
- **Función**: Campo de métrica
- **Contenido típico**: Normalmente '0', que mide el tiempo en unidades predefinidas.

### fields_total
- **Significado**: Número total de campos extraídos del documento.
- **Función**: Campo de métrica
- **Contenido típico**: Un entero que representa el total de campos, por ejemplo, 13.

### fields_correct
- **Significado**: Número de campos extraídos y validados correctamente.
- **Función**: Campo de métrica
- **Contenido típico**: Un entero que representa los campos procesados correctamente, por ejemplo, 12.

### checkbox_fields_total
- **Significado**: Número total de campos de casilla de verificación procesados.
- **Función**: Campo de métrica
- **Contenido típico**: Normalmente `0`, que indica los campos de casilla de verificación procesados.

### checkbox_fields_correct
- **Significado**: Número de campos de casilla de verificación validados correctamente.
- **Función**: Campo de métrica
- **Contenido típico**: Normalmente `0`, que indica los campos de casilla de verificación validados correctamente.

### table_values_total
- **Significado**: Número total de valores de tabla extraídos del documento.
- **Función**: Campo de métrica
- **Contenido típico**: Normalmente `0`, que indica el total de valores de tabla procesados.

### table_values_correct
- **Significado**: Número de valores de tabla validados correctamente.
- **Función**: Campo de métrica
- **Contenido típico**: Normalmente `0`, que indica los valores de tabla validados correctamente.

### detail_report
- **Significado**: Contenido JSON que proporciona un informe detallado de los campos del documento y de su estado de validación.
- **Función**: Campo descriptivo/técnico
- **Contenido típico**: Cadena JSON con información detallada de los campos.

### created_on
- **Significado**: Marca de tiempo del momento en que se creó la entrada del informe de documento.
- **Función**: Campo técnico
- **Contenido típico**: Marca de tiempo en UTC, por ejemplo, `2025-03-10 08:07:24+00`.

### last_modified_on
- **Significado**: Marca de tiempo de la última modificación del informe de documento.
- **Función**: Campo técnico
- **Contenido típico**: Marca de tiempo en UTC que indica la hora de la última actualización.

### is_deleted
- **Significado**: Indica si el informe de documento se ha marcado como eliminado.
- **Función**: Campo técnico
- **Contenido típico**: Valor booleano; `False` si no se ha eliminado.

### validated_by
- **Significado**: Identificador del usuario que validó el documento.
- **Función**: Clave externa
- **Contenido típico**: Un entero que representa el ID del validador, por ejemplo, `1`.

### sub_org_id
- **Significado**: Identificador de una suborganización relacionada con el documento.
- **Función**: Clave externa
- **Contenido típico**: Un UUID que enlaza con una suborganización.
```
