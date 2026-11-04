# Campo

## Columnas

* `id`: interno
* `org_id`: ID de la organización
* `doc_type`: DOC Type
* `is_sub_doc_type_field`: boolean
* `profile`: interno
* `field_name`: interno
* `field_type`: interno
* `title`: interno
* `translation_key`: interno
* `hide_label`: boolean
* `input_type`: interno
* `input_size`: interno
* `icon_left`: interno
* `icon_right`: interno
* `icon_above`: interno
* `group_id`: interno
* `row_order`: integer
* `sort_order`: integer
* `fuzzy_name`: interno
* `fuzzy_field`: interno
* `fuzzy_primary_field`: boolean
* `label_align`: interno
* `calculation_formula`: text
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `placeholder`: interno
* `coordinates`: interno
* `normalized_coordinates`: interno
* `threshold`: interno
* `reference_point`: interno
* `checkbox_group`: interno
* `list_of_values`: interno
* `enforce_list_of_values`: boolean
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean
* `costing_element`: interno
* `erp_field_name`: interno

## Análisis y descripción

```markdown
# Documentación técnica de la tabla `public.field`

## Introducción

La tabla `public.field` parece estar diseñada para gestionar los metadatos y la configuración de los distintos campos asociados a los documentos, probablemente en el ámbito de los seguros. Cada fila de la tabla parece representar la configuración de un campo concreto, incluidos su tipo, su etiqueta, sus ajustes de visibilidad y otras propiedades que determinan cómo debe presentarse y procesarse el campo.

## Columnas

### id
- **Significado**: Identificador único de cada configuración de campo.
- **Función**: Clave primaria.
- **Contenido típico**: Una cadena UUID que identifica de forma única cada entrada de la tabla.

### org_id
- **Significado**: Identificador de la organización asociada a la configuración del campo.
- **Función**: Clave externa.
- **Contenido típico**: Un UUID que hace referencia a una organización.

### doc_type
- **Significado**: Indica el tipo de documento al que está asociado el campo.
- **Función**: Posiblemente una clave externa o un identificador categórico.
- **Contenido típico**: Una cadena con el formato `INSURANCE_DOCUMENTS_<UUID>` que indica el tipo de documento.

### is_sub_doc_type_field
- **Significado**: Indica si el campo es un subtipo del tipo de documento.
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano (True o False).

### profile
- **Significado**: Posiblemente define el perfil o el ámbito del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Con frecuencia vacío o una breve descripción de texto.

### field_name
- **Significado**: El nombre interno del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena que representa el nombre del campo en un contexto técnico (p. ej., `Schadennummer`).

### field_type
- **Significado**: Define el tipo de datos que contiene el campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadenas descriptivas como `STRING`, `AMOUNT`.

### title
- **Significado**: El título visible del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadena en mayúsculas utilizada para mostrar la etiqueta del campo.

### translation_key
- **Significado**: Clave para la traducción a distintos idiomas.
- **Función**: Campo técnico.
- **Contenido típico**: Cadena en minúsculas que representa la clave de traducción.

### hide_label
- **Significado**: Indica si la etiqueta del campo debe ocultarse en la interfaz.
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano (True o False).

### input_type
- **Significado**: Indica el método de entrada del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Puede estar vacío o contener cadenas que definen el tipo de entrada.

### input_size
- **Significado**: Determina el tamaño del campo de entrada.
- **Función**: Campo descriptivo.
- **Contenido típico**: Puede estar vacío o contener cadenas que definen el tamaño de entrada.

### icon_left
- **Significado**: Icono que se muestra a la izquierda del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con identificadores de iconos.

### icon_right
- **Significado**: Icono que se muestra a la derecha del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con identificadores de iconos.

### icon_above
- **Significado**: Icono que se muestra encima del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con identificadores de iconos.

### group_id
- **Significado**: Identificador del grupo de campos al que pertenece este campo.
- **Función**: Clave externa.
- **Contenido típico**: Un UUID que hace referencia a un grupo de campos.

### row_order
- **Significado**: Determina el orden del campo en una lista o formulario.
- **Función**: Campo técnico.
- **Contenido típico**: Entero que indica la posición.

### sort_order
- **Significado**: Indica el orden de clasificación del campo.
- **Función**: Campo técnico.
- **Contenido típico**: Entero que define la prioridad de clasificación.

### fuzzy_name
- **Significado**: Un nombre alternativo para la coincidencia aproximada (fuzzy).
- **Función**: Campo descriptivo.
- **Contenido típico**: Con frecuencia vacío o con una cadena para fines de coincidencia.

### fuzzy_field
- **Significado**: Indica si el campo se utiliza en la coincidencia aproximada (fuzzy).
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con una cadena.

### fuzzy_primary_field
- **Significado**: Indica si es el campo principal para la coincidencia aproximada (fuzzy).
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano (True o False).

### label_align
- **Significado**: Ajuste de alineación de la etiqueta del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Con frecuencia vacío o con información de alineación (p. ej., izquierda, derecha, centro).

### calculation_formula
- **Significado**: Fórmula utilizada en los cálculos que involucran al campo.
- **Función**: Campo técnico.
- **Contenido típico**: Texto con una fórmula o una lógica de cálculo.

### clean_field
- **Significado**: Indica si el campo debe someterse a una limpieza de datos.
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano (True o False).

### alphanumeric_field
- **Significado**: Indica si el campo debe aceptar únicamente caracteres alfanuméricos.
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano (True o False).

### placeholder
- **Significado**: Texto de marcador de posición del campo de entrada.
- **Función**: Campo descriptivo.
- **Contenido típico**: Con frecuencia vacío o con un texto orientativo.

### coordinates
- **Significado**: Datos de coordenadas asociados al campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con información de coordenadas.

### normalized_coordinates
- **Significado**: Versión normalizada de las coordenadas para garantizar la coherencia.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con datos de coordenadas normalizadas.

### threshold
- **Significado**: Valor umbral relacionado con la validación o el procesamiento del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con valores umbral.

### reference_point
- **Significado**: Punto de referencia utilizado en cálculos o en el posicionamiento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Con frecuencia vacío o con datos del punto de referencia.

### checkbox_group
- **Significado**: Identificador de agrupación de los campos de casilla de verificación.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con identificadores de grupo.

### list_of_values
- **Significado**: Indica una lista de valores permitidos para el campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con una lista de valores.

### enforce_list_of_values
- **Significado**: Indica si la lista de valores debe aplicarse de forma estricta.
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano (True o False).

### created_by
- **Significado**: Identificador del usuario que creó la entrada del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Entero que hace referencia a un ID de usuario.

### created_on
- **Significado**: Marca de tiempo de la creación del campo.
- **Función**: Campo técnico.
- **Contenido típico**: Fecha y hora en UTC.

### last_modified_on
- **Significado**: Marca de tiempo de la última modificación del campo.
- **Función**: Campo técnico.
- **Contenido típico**: Fecha y hora en UTC.

### is_deleted
- **Significado**: Indica si el campo se ha marcado como eliminado.
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano (True o False).

### costing_element
- **Significado**: Elemento de costes asociado al campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con identificadores de elementos de costes.

### erp_field_name
- **Significado**: Nombre del campo tal como se utiliza en los sistemas ERP.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con nombres de campo específicos del ERP.

Esta documentación ofrece una visión detallada de la estructura y la finalidad de cada columna de la tabla `public.field`. Sirve de guía para que los desarrolladores comprendan el modelo de datos y su aplicación en el sistema.
```
