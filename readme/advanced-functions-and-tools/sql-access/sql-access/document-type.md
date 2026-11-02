# Tipo de documento

## Columnas

* `id`: interno
* `org_id`: ID de la organización
* `document_key`: interno
* `document_name`: interno
* `title`: interno
* `translation_key`: interno
* `extraction_type`: interno
* `document_type_category`: interno
* `has_table`: boolean
* `sort_order`: integer
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean

## Análisis y descripción

```markdown
# Tabla: public.document_type

## Introducción
La tabla `public.document_type` está diseñada para almacenar información relacionada con los distintos tipos de documento dentro de una organización. Incluye identificadores y metadatos para la categorización, gestión y procesamiento de documentos, como claves de documento, nombres, títulos, claves de traducción y otros atributos que facilitan el manejo y la recuperación de documentos. La tabla también registra la creación y modificación de estas entradas, y admite tanto el estado activo como el eliminado.

## Descripción de las columnas

### id
- **Significado**: Un identificador único para cada entrada de tipo de documento.
- **Función**: Clave primaria.
- **Contenido típico**: Una cadena UUID que identifica de forma única una entrada de tipo de documento.

### org_id
- **Significado**: Identificador de la organización a la que pertenece el tipo de documento.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que hace referencia a una organización.

### document_key
- **Significado**: Una clave única para identificar el tipo de documento, potencialmente utilizada en sistemas de almacenamiento o procesamiento de documentos.
- **Función**: Identificador.
- **Contenido típico**: Una cadena que combina la información del tipo de documento con el ID de la organización.

### document_name
- **Significado**: El nombre interno del tipo de documento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena en mayúsculas que representa el nombre del tipo de documento.

### title
- **Significado**: El título visible del tipo de documento para las interfaces de usuario.
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena en formato título, legible y descriptiva del tipo de documento.

### translation_key
- **Significado**: Una clave utilizada para localizar el título o el nombre del documento en distintos idiomas.
- **Función**: Soporte de internacionalización.
- **Contenido típico**: Una cadena en minúsculas que sirve de referencia para los sistemas de traducción.

### extraction_type
- **Significado**: Indica el método o proceso mediante el cual se extraen los datos del documento.
- **Función**: Campo de metadatos.
- **Contenido típico**: Actualmente no está rellenado en los datos de ejemplo.

### document_type_category
- **Significado**: Clasifica el tipo de documento en categorías o clasificaciones más amplias.
- **Función**: Campo de categorización.
- **Contenido típico**: Actualmente no está rellenado en los datos de ejemplo.

### has_table
- **Significado**: Indica si el tipo de documento incluye datos tabulares.
- **Función**: Campo de metadatos.
- **Contenido típico**: Valor booleano (`True` o `False`) que indica la presencia de datos tabulares.

### sort_order
- **Significado**: Define el orden en que se ordenan o muestran los tipos de documento.
- **Función**: Campo de ordenación.
- **Contenido típico**: Un entero que representa la posición en la ordenación.

### created_by
- **Significado**: Identificador del usuario que creó la entrada del tipo de documento.
- **Función**: Campo de metadatos.
- **Contenido típico**: Un entero que hace referencia a un ID de usuario.

### created_on
- **Significado**: Marca de tiempo que indica cuándo se creó la entrada del tipo de documento.
- **Función**: Campo de auditoría.
- **Contenido típico**: Fecha y hora con información de zona horaria.

### last_modified_on
- **Significado**: Marca de tiempo que indica la fecha de la última modificación de la entrada del tipo de documento.
- **Función**: Campo de auditoría.
- **Contenido típico**: Fecha y hora con información de zona horaria, `None` si nunca se ha modificado.

### is_deleted
- **Significado**: Indica si la entrada del tipo de documento está marcada como eliminada.
- **Función**: Campo de estado.
- **Contenido típico**: Valor booleano (`True` o `False`) que indica el estado de eliminación.
```
