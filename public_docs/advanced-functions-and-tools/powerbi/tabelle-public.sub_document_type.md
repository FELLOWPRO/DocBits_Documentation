# Tabla public.sub\_document\_type

## Columnas

* `id`: internal
* `org_id`: ID to organisation
* `doc_type_key`: internal
* `sub_doc_type_key`: internal
* `name`: internal
* `title`: internal
* `translation_key`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

## Análisis y descripción

```markdown
# Tabla `public.sub_document_type`

## Introducción

La tabla `sub_document_type` está diseñada para almacenar información detallada sobre los distintos subtipos de documento dentro de una organización. Esto incluye identificadores únicos, asociaciones organizativas, nombres descriptivos y metadatos relacionados con la creación y la modificación de estos subtipos de documento. La tabla también mantiene el estado de eliminación lógica de los registros.

## Descripción de las columnas

### id
- **Significado**: Esta columna almacena el identificador único de cada subtipo de documento.
- **Función**: Clave primaria.
- **Contenido típico**: Una cadena UUID que identifica de forma única un registro de subtipo de documento (por ejemplo, `'c2cc2d62-e4be-491b-a43e-c4123dff5aa6'`).

### org_id
- **Significado**: Esta columna indica la organización a la que pertenece el subtipo de documento.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que hace referencia a una organización (por ejemplo, `'23f3d697-7411-4c95-981d-faf089d266be'`).

### doc_type_key
- **Significado**: Representa la clave del tipo de documento asociada al subtipo de documento.
- **Función**: Clave externa (implícita por la convención de nomenclatura).
- **Contenido típico**: Una clave de cadena que enlaza con un tipo de documento más amplio (por ejemplo, `'TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### sub_doc_type_key
- **Significado**: Denota una clave específica del subtipo de documento dentro de una categoría de documento.
- **Función**: Identificador único del subtipo de documento en el ámbito de un tipo de documento.
- **Contenido típico**: Una clave de cadena que identifica de forma única un subtipo de documento (por ejemplo, `'TEST_SUB_TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### name
- **Significado**: Almacena un nombre corto o un código del subtipo de documento.
- **Función**: Descriptivo.
- **Contenido típico**: Un identificador o código conciso (por ejemplo, `'TEST_SUB_TEST'`).

### title
- **Significado**: Contiene un título legible del subtipo de documento.
- **Función**: Descriptivo.
- **Contenido típico**: Un título descriptivo para interfaces de usuario o informes (por ejemplo, `'Test Sub Test'`).

### translation_key
- **Significado**: Clave utilizada para la internacionalización y la localización con el fin de traducir el nombre del subtipo de documento.
- **Función**: Técnico.
- **Contenido típico**: Una cadena utilizada en los archivos de traducción (por ejemplo, `'test_sub_test'`).

### created_by
- **Significado**: Identifica al usuario que creó la entrada del subtipo de documento.
- **Función**: Técnico.
- **Contenido típico**: Un entero que representa el ID de usuario (por ejemplo, `8`).

### created_on
- **Significado**: Marca de tiempo que indica cuándo se creó el subtipo de documento.
- **Función**: Técnico.
- **Contenido típico**: Una marca de tiempo con zona horaria (por ejemplo, `2022-12-13 08:34:13.932893+00:00`).

### last_modified_on
- **Significado**: Marca de tiempo que indica cuándo se modificó por última vez el subtipo de documento.
- **Función**: Técnico.
- **Contenido típico**: Una marca de tiempo con zona horaria, posiblemente `None` si nunca se ha modificado tras su creación.

### is_deleted
- **Significado**: Indicador booleano que señala si el subtipo de documento se ha eliminado de forma lógica (soft delete).
- **Función**: Técnico.
- **Contenido típico**: `True` o `False`, que indica el estado de eliminación (por ejemplo, `False`).
```
