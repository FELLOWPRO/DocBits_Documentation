# Tabla public.field

## Columnas

* `id`: internal
* `org_id`: ID to organisation
* `doc_type`: DOC Type
* `is_sub_doc_type_field`: boolean
* `profile`: internal
* `field_name`: internal
* `field_type`: internal
* `title`: internal
* `translation_key`: internal
* `hide_label`: boolean
* `input_type`: internal
* `input_size`: internal
* `icon_left`: internal
* `icon_right`: internal
* `icon_above`: internal
* `group_id`: internal
* `row_order`: integer
* `sort_order`: integer
* `fuzzy_name`: internal
* `fuzzy_field`: internal
* `fuzzy_primary_field`: boolean
* `label_align`: internal
* `calculation_formula`: text
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `placeholder`: internal
* `coordinates`: internal
* `normalized_coordinates`: internal
* `threshold`: internal
* `reference_point`: internal
* `checkbox_group`: internal
* `list_of_values`: internal
* `enforce_list_of_values`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `costing_element`: internal
* `erp_field_name`: internal

## Análisis y descripción

```markdown
# Documentación técnica de la tabla `public.field`

## Introducción

La tabla `public.field` parece estar diseñada para gestionar los metadatos y la configuración de los distintos campos asociados a los documentos, probablemente dentro del ámbito de los seguros. Cada fila de la tabla parece representar una configuración de campo específica, que incluye su tipo, su etiqueta, los ajustes de visibilidad y otras propiedades que determinan cómo debe presentarse y procesarse el campo.

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
- **Significado**: Especifica el tipo de documento con el que está asociado el campo.
- **Función**: Posiblemente una clave externa o un identificador categórico.
- **Contenido típico**: Una cadena con el formato `INSURANCE_DOCUMENTS_<UUID>` que indica el tipo de documento.

### is_sub_doc_type_field
- **Significado**: Indica si el campo es un subtipo del tipo de documento.
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano (True o False).

### profile
- **Significado**: Define potencialmente el perfil o el ámbito del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: A menudo vacío o una breve descripción de texto.

### field_name
- **Significado**: El nombre interno del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena que representa el nombre del campo en un contexto técnico (por ejemplo, `Schadennummer`).

### field_type
- **Significado**: Define el tipo de datos que contiene el campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadenas descriptivas como `STRING`, `AMOUNT`.

### title
- **Significado**: El título del campo que se muestra.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadena en mayúsculas utilizada para mostrar la etiqueta del campo.

### translation_key
- **Significado**: Clave para la traducción a distintos idiomas.
- **Función**: Campo técnico.
- **Contenido típico**: Cadena en minúsculas que representa la clave de traducción.

### hide_label
- **Significado**: Indica si la etiqueta del campo debe ocultarse en la interfaz de usuario.
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano (True o False).

### input_type
- **Significado**: Especifica el método de entrada del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Puede estar vacío o contener cadenas que definen el tipo de entrada.

### input_size
- **Significado**: Determina el tamaño del campo de entrada.
- **Función**: Campo descriptivo.
- **Contenido típico**: Puede estar vacío o contener cadenas que definen el tamaño de entrada.

### icon_left
- **Significado**: Icono que se muestra en el lado izquierdo del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con identificadores de iconos.

### icon_right
- **Significado**: Icono que se muestra en el lado derecho del campo.
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
- **Significado**: Especifica el orden de clasificación del campo.
- **Función**: Campo técnico.
- **Contenido típico**: Entero que define la precedencia de ordenación.

### fuzzy_name
- **Significado**: Un nombre alternativo para la coincidencia aproximada (fuzzy matching).
- **Función**: Campo descriptivo.
- **Contenido típico**: A menudo vacío o con una cadena para fines de coincidencia.

### fuzzy_field
- **Significado**: Especifica si el campo se utiliza en la coincidencia aproximada.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con una cadena.

### fuzzy_primary_field
- **Significado**: Indica si este es el campo principal para la coincidencia aproximada.
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano (True o False).

### label_align
- **Significado**: Ajuste de alineación de la etiqueta del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: A menudo vacío o con información de alineación (por ejemplo, left, right, center).

### calculation_formula
- **Significado**: Fórmula utilizada para los cálculos en los que interviene el campo.
- **Función**: Campo técnico.
- **Contenido típico**: Texto que contiene una fórmula o lógica de cálculo.

### clean_field
- **Significado**: Indica si el campo debe someterse a depuración de datos.
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano (True o False).

### alphanumeric_field
- **Significado**: Especifica si el campo debe aceptar solo caracteres alfanuméricos.
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano (True o False).

### placeholder
- **Significado**: Texto de marcador de posición del campo de entrada.
- **Función**: Campo descriptivo.
- **Contenido típico**: A menudo vacío o con un texto orientativo.

### coordinates
- **Significado**: Datos de coordenadas asociados al campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con información de coordenadas.

### normalized_coordinates
- **Significado**: Versión normalizada de las coordenadas para garantizar la coherencia.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con datos de coordenadas normalizadas.

### threshold
- **Significado**: Valor de umbral relacionado con la validación o el procesamiento del campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con valores de umbral.

### reference_point
- **Significado**: Punto de referencia utilizado en cálculos o en el posicionamiento.
- **Función**: Campo descriptivo.
- **Contenido típico**: A menudo vacío o con datos del punto de referencia.

### checkbox_group
- **Significado**: Identificador de agrupación de los campos de casilla de verificación.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con identificadores de grupo.

### list_of_values
- **Significado**: Especifica una lista de valores permitidos para el campo.
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
- **Significado**: Marca de tiempo del momento en que se creó el campo.
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
- **Significado**: Elemento de coste asociado al campo.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con identificadores de elementos de coste.

### erp_field_name
- **Significado**: Nombre del campo tal como se utiliza en los sistemas ERP.
- **Función**: Campo descriptivo.
- **Contenido típico**: Por lo general vacío o con nombres de campo específicos del ERP.

Esta documentación ofrece una visión detallada de la estructura y la finalidad de cada columna de la tabla `public.field`. Sirve de guía para que los desarrolladores comprendan el modelo de datos y su aplicación en el sistema.
```
