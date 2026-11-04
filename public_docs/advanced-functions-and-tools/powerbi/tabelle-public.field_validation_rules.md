# Tabla public.field\_validation\_rules

## Columnas

* `id`: internal
* `org_id`: ID to organisation
* `field_id`: internal
* `doc_type`: DOC Type
* `is_sub_doc_type_field`: boolean
* `profile`: internal
* `field_name`: internal
* `field_length`: integer
* `field_label`: internal
* `is_required`: boolean
* `is_readonly`: boolean
* `is_hidden`: boolean
* `force_validation`: boolean
* `validation_pattern`: internal
* `confidence_threshold`: integer
* `match_score_threshold`: integer
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `additional_attributes`: text

## Análisis y descripción

```markdown
# Documentación técnica de la tabla `public.field_validation_rules`

## Introducción

La tabla `public.field_validation_rules` parece almacenar metadatos y reglas de validación de los campos asociados a los distintos tipos de documento de una organización. Es probable que se utilice para garantizar la integridad y la coherencia de los datos en formularios o documentos, al especificar requisitos como si un campo es obligatorio, su longitud, su visibilidad y los patrones de validación que deben aplicarse.

## Descripción de las columnas

### id
- **Significado**: Un identificador único para cada regla de validación de campo.
- **Función**: Clave primaria.
- **Contenido típico**: Una cadena UUID que identifica de forma única un registro.

### org_id
- **Significado**: Identificador de la organización a la que se aplica la regla de validación.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que hace referencia a una organización concreta.

### field_id
- **Significado**: Identificador del campo concreto con el que está asociada la regla de validación.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que hace referencia a un campo concreto.

### doc_type
- **Significado**: Especifica el tipo de documento con el que está asociada la regla de validación del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena que indica el tipo de documento (por ejemplo, `PURCHASE_ORDER_FORM`).

### is_sub_doc_type_field
- **Significado**: Indica si el campo forma parte de un subtipo de documento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Valor booleano (`True` o `False`).

### profile
- **Significado**: Representa el perfil o el contexto en el que se aplica la validación del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena como `DEFAULT`.

### field_name
- **Significado**: El nombre del campo para el que se define la regla de validación.
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena que representa el nombre del campo (por ejemplo, `Test`).

### field_length
- **Significado**: La longitud máxima permitida para el contenido del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Un entero que especifica el límite de caracteres.

### field_label
- **Significado**: La etiqueta o el nombre para mostrar del campo en la interfaz de usuario.
- **Función**: Campo descriptivo.
- **Contenido típico**: Normalmente nulo en los datos de ejemplo.

### is_required
- **Significado**: Indica si el campo es obligatorio para el documento.
- **Función**: Indicador de restricción.
- **Contenido típico**: Valor booleano (`True` o `False`).

### is_readonly
- **Significado**: Especifica si el campo es editable o de solo lectura.
- **Función**: Indicador de restricción.
- **Contenido típico**: Valor booleano (`True` o `False`).

### is_hidden
- **Significado**: Indica si el campo debe ocultarse en la interfaz de usuario.
- **Función**: Indicador de restricción.
- **Contenido típico**: Valor booleano (`True` o `False`).

### force_validation
- **Significado**: Determina si debe aplicarse la validación independientemente de otras condiciones.
- **Función**: Indicador de restricción.
- **Contenido típico**: Valor booleano (`True` o `False`).

### validation_pattern
- **Significado**: Un patrón (probablemente una expresión regular) con el que debe coincidir el contenido del campo.
- **Función**: Regla de validación.
- **Contenido típico**: Normalmente nulo en los datos de ejemplo.

### confidence_threshold
- **Significado**: El nivel mínimo de confianza necesario para la validación del campo.
- **Función**: Restricción de validación.
- **Contenido típico**: Un valor entero que representa el umbral de confianza.

### match_score_threshold
- **Significado**: La puntuación mínima de coincidencia necesaria para la validación del contenido del campo.
- **Función**: Restricción de validación.
- **Contenido típico**: Un valor entero que representa el umbral de puntuación de coincidencia.

### created_by
- **Significado**: Identificador del usuario que creó esta regla de validación.
- **Función**: Campo descriptivo.
- **Contenido típico**: Un entero que representa el ID de usuario.

### created_on
- **Significado**: Marca de tiempo que indica cuándo se creó la regla de validación.
- **Función**: Campo técnico.
- **Contenido típico**: Una marca de tiempo con zona horaria.

### last_modified_on
- **Significado**: Marca de tiempo que indica la última modificación de la regla de validación.
- **Función**: Campo técnico.
- **Contenido típico**: Una marca de tiempo con zona horaria; puede ser nula si nunca se ha modificado.

### is_deleted
- **Significado**: Indica si la regla de validación se ha marcado como eliminada.
- **Función**: Indicador de eliminación lógica (soft delete).
- **Contenido típico**: Valor booleano (`True` o `False`).

### additional_attributes
- **Significado**: Almacena atributos o metadatos adicionales asociados a la regla de validación del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Texto, a menudo nulo en los datos de ejemplo.
```
