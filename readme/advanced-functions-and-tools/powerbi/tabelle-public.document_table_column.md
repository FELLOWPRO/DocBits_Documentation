# Tabla public.document\_table\_column

## Columnas

* `id`: internal
* `document_table_id`: internal
* `table_name`: internal
* `org_id`: ID to organisation
* `column_name`: internal
* `column_type`: internal
* `title`: internal
* `translation_key`: internal
* `sort_order`: integer
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

## Análisis y descripción

```markdown
# Documentación técnica de `public.document_table_column`

## Introducción

La tabla `public.document_table_column` parece estar diseñada para almacenar metadatos sobre las columnas de diversas tablas relacionadas con documentos, como las tablas de facturas o de albaranes. Estos metadatos incluyen información sobre el nombre, el tipo y las propiedades de cada columna, así como identificadores organizativos y técnicos. La tabla admite la generación y la gestión dinámicas de los esquemas de documentos dentro del sistema.

## Descripción de las columnas

### id
- **Significado**: Un identificador único para cada entrada de columna de la tabla.
- **Función**: Clave primaria.
- **Nota**: Normalmente una cadena UUID que identifica de forma única una fila de esta tabla.

### document_table_id
- **Significado**: Hace referencia a la tabla que contiene el documento del que forma parte esta columna.
- **Función**: Clave externa.
- **Nota**: Probablemente un UUID que enlaza con otra tabla en la que se definen las tablas de documentos.

### table_name
- **Significado**: El nombre de la tabla de documentos a la que pertenece esta columna.
- **Función**: Campo descriptivo.
- **Contenido típico**: Nombres como `INVOICE_TABLE`, `DELIVERY_NOTE_TABLE`.
- **Nota**: Facilita saber a qué estructura de documento pertenece la columna.

### org_id
- **Significado**: Identificador de la organización propietaria o administradora de la tabla de documentos.
- **Función**: Clave externa.
- **Nota**: Normalmente un UUID que enlaza con una entidad de organización.

### column_name
- **Significado**: El nombre técnico de la columna dentro de su tabla de documentos.
- **Función**: Campo descriptivo.
- **Contenido típico**: Nombres como `COUNTRY_ORIGIN`, `ORDERED_QUANTITY`.
- **Nota**: Representa el nombre real del campo en la tabla de documentos.

### column_type
- **Significado**: Describe el tipo de dato de la columna.
- **Función**: Campo descriptivo.
- **Contenido típico**: `STRING`, `DATE`.
- **Nota**: Indica el tipo de datos almacenados en la columna.

### title
- **Significado**: Un título o etiqueta legible para la columna.
- **Función**: Campo descriptivo.
- **Contenido típico**: `COUNTRY_ORIGIN`, `Ordered Quantity`.
- **Nota**: Se utiliza para mostrar los nombres de las columnas de forma clara para el usuario.

### translation_key
- **Significado**: Clave utilizada para la internacionalización y la localización del título de la columna.
- **Función**: Campo técnico.
- **Nota**: Actualmente está vacía en los datos de ejemplo, lo que sugiere un uso opcional.

### sort_order
- **Significado**: Define el orden de las columnas cuando se muestran.
- **Función**: Campo descriptivo.
- **Contenido típico**: Enteros como `16`, `5`.
- **Nota**: Determina la secuencia de las columnas en la vista de la tabla de documentos.

### clean_field
- **Significado**: Indica si la columna contiene datos depurados.
- **Función**: Indicador booleano.
- **Contenido típico**: `True` o `False`.
- **Nota**: Se utiliza para la validación de datos o el estado de depuración.

### alphanumeric_field
- **Significado**: Especifica si la columna debe tratarse como un campo alfanumérico.
- **Función**: Indicador booleano.
- **Contenido típico**: `True` o `False`.
- **Nota**: Útil para la validación de entradas o con fines de formato.

### created_by
- **Significado**: Identificador del usuario que creó esta entrada de columna.
- **Función**: Clave externa.
- **Contenido típico**: Valores enteros como `1`, `8`.
- **Nota**: Enlaza con el usuario o la entidad del sistema responsable de la creación.

### created_on
- **Significado**: Marca de tiempo del momento en que se creó la entrada de columna.
- **Función**: Campo técnico.
- **Contenido típico**: Valores de fecha y hora en UTC.
- **Nota**: Útil para la auditoría y el seguimiento de los cambios.

### last_modified_on
- **Significado**: Marca de tiempo de la última modificación realizada en la entrada de columna.
- **Función**: Campo técnico.
- **Nota**: Actualmente es `None` en los datos de ejemplo, lo que indica que no se ha producido ninguna modificación después de la creación.

### is_deleted
- **Significado**: Indica si la entrada de columna se ha eliminado de forma lógica.
- **Función**: Indicador booleano.
- **Contenido típico**: `True` o `False`.
- **Nota**: Ayuda a gestionar las eliminaciones lógicas (soft delete) sin retirar físicamente los datos.

```
