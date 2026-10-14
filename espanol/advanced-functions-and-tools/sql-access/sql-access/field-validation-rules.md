# Field validation rules

## Columnas

* `id`: interno
* `org_id`: ID de la organización
* `field_id`: interno
* `doc_type`: DOC Type
* `is_sub_doc_type_field`: boolean
* `profile`: interno
* `field_name`: interno
* `field_length`: integer
* `field_label`: interno
* `is_required`: boolean
* `is_readonly`: boolean
* `is_hidden`: boolean
* `force_validation`: boolean
* `validation_pattern`: interno
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

La tabla `public.field_validation_rules` parece almacenar metadatos y reglas de validación de los campos asociados a los distintos tipos de documento dentro de una organización. Probablemente se utiliza para garantizar la integridad y la coherencia de los datos en formularios o documentos, mediante requisitos como si un campo es obligatorio, su longitud, su visibilidad y los patrones de validación que deben aplicarse.

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
- **Significado**: Identificador del campo concreto al que está asociada la regla de validación.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que hace referencia a un campo concreto.

### doc_type
- **Significado**: Indica el tipo de documento al que está asociada la regla de validación del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena que indica el tipo de documento (p. ej., `PURCHASE_ORDER_FORM`).

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
- **Contenido típico**: Una cadena que representa el nombre del campo (p. ej., `Test`).

### field_length
- **Significado**: La longitud máxima permitida para el contenido del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Un entero que indica el límite de caracteres.

### field_label
- **Significado**: La etiqueta o el nombre visible del campo en la interfaz de usuario.
- **Función**: Campo descriptivo.
- **Contenido típico**: Normalmente nulo en los datos de ejemplo.

### is_required
- **Significado**: Indica si el campo es obligatorio para el documento.
- **Función**: Indicador de restricción.
- **Contenido típico**: Valor booleano (`True` o `False`).

### is_readonly
- **Significado**: Indica si el campo es editable o de solo lectura.
- **Función**: Indicador de restricción.
- **Contenido típico**: Valor booleano (`True` o `False`).

### is_hidden
- **Significado**: Indica si el campo debe ocultarse en la interfaz de usuario.
- **Función**: Indicador de restricción.
- **Contenido típico**: Valor booleano (`True` o `False`).

### force_validation
- **Significado**: Determina si la validación debe aplicarse con independencia de otras condiciones.
- **Función**: Indicador de restricción.
- **Contenido típico**: Valor booleano (`True` o `False`).

### validation_pattern
- **Significado**: Un patrón (probablemente una expresión regular) con el que debe coincidir el contenido del campo.
- **Función**: Regla de validación.
- **Contenido típico**: Normalmente nulo en los datos de ejemplo.

### confidence_threshold
- **Significado**: El nivel mínimo de confianza necesario para validar el campo.
- **Función**: Restricción de validación.
- **Contenido típico**: Un valor entero que representa el umbral de confianza.

### match_score_threshold
- **Significado**: La puntuación mínima de coincidencia necesaria para validar el contenido del campo.
- **Función**: Restricción de validación.
- **Contenido típico**: Un valor entero que representa el umbral de la puntuación de coincidencia.

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
- **Función**: Indicador de borrado lógico.
- **Contenido típico**: Valor booleano (`True` o `False`).

### additional_attributes
- **Significado**: Almacena atributos o metadatos adicionales asociados a la regla de validación del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Texto, con frecuencia nulo en los datos de ejemplo.
```
