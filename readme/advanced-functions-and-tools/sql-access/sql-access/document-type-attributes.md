# Document type attributes

## Columnas

* `id`: interno
* `org_id`: ID de la organización
* `doc_type_key`: interno
* `sub_doc_type_key`: interno
* `attribute_key`: interno
* `attribute_value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `sub_org_id`: interno

## Análisis y descripción

```markdown
# Documentación técnica de la tabla `public.document_type_attributes`

## Introducción

La tabla `public.document_type_attributes` parece estar diseñada para gestionar los atributos relacionados con los distintos tipos de documento dentro de un contexto organizativo. Esta tabla permite probablemente la gestión de la configuración o de los metadatos de los diferentes tipos de documento, como facturas o albaranes, al asociar atributos concretos a cada tipo de documento.

## Descripción de las columnas

### id
- **Significado**: Un identificador único para cada registro de la tabla.
- **Función**: Clave primaria.
- **Contenido típico**: Una cadena UUID que identifica de forma única una fila de la tabla.

### org_id
- **Significado**: Representa la organización a la que pertenece el atributo del tipo de documento.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que hace referencia a una organización.

### doc_type_key
- **Significado**: El tipo de documento al que se aplica el atributo (p. ej., INVOICE, DELIVERY_NOTE).
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena que representa un tipo de documento.

### sub_doc_type_key
- **Significado**: Una categorización más específica dentro del tipo de documento, si procede.
- **Función**: Campo descriptivo.
- **Contenido típico**: Normalmente `None`, lo que indica que no siempre se utiliza.

### attribute_key
- **Significado**: La clave del atributo o propiedad concreta relacionada con el tipo de documento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena que representa una clave de atributo, como `SECOND_APPROVAL_BEFORE_EXPORT`.

### attribute_value
- **Significado**: El valor asociado a la clave del atributo para el tipo de documento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Un valor de cadena o numérico que proporciona el valor del atributo, p. ej., `true`, `123`.

### created_by
- **Significado**: El identificador del usuario que creó el registro.
- **Función**: Campo descriptivo.
- **Contenido típico**: Un entero que representa un ID de usuario.

### created_on
- **Significado**: La marca de tiempo de cuándo se creó el registro.
- **Función**: Campo técnico.
- **Contenido típico**: Una marca de tiempo con zona horaria que indica cuándo se creó el registro.

### last_modified_on
- **Significado**: La marca de tiempo de la última modificación realizada en el registro.
- **Función**: Campo técnico.
- **Contenido típico**: Una marca de tiempo con zona horaria que indica la hora de la última actualización.

### is_deleted
- **Significado**: Indica si el registro está marcado como eliminado.
- **Función**: Campo técnico.
- **Contenido típico**: Un valor booleano; `false` implica que el registro está activo.

### sub_org_id
- **Significado**: Representa una suborganización dentro de la organización principal, si procede.
- **Función**: Clave externa.
- **Contenido típico**: Normalmente `None`, lo que indica que no siempre se utiliza.
```

Esta documentación ofrece una visión estructurada de la tabla `public.document_type_attributes` y permite a los desarrolladores comprender la finalidad y el uso de cada columna.
