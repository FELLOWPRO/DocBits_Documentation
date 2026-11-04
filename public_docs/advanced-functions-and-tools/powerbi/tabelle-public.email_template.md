# Tabla public.email\_template

## Columnas

* `id`: internal
* `org_id`: ID to organisation
* `name`: internal
* `email_type`: internal
* `value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `subject`: internal
* `last_modified_by`: internal
* `deleted_by`: internal
* `doc_type`: DOC Type

## Análisis y descripción

```markdown
# Documentación técnica de la tabla `public.email_template`

## Introducción

La tabla `public.email_template` está diseñada para almacenar las plantillas de correo electrónico utilizadas en el sistema. Estas plantillas están asociadas a distintas organizaciones y probablemente se utilizan para enviar comunicaciones por correo electrónico estandarizadas. La tabla contiene metadatos sobre las plantillas, incluidos los detalles de creación y modificación, y también registra si una plantilla se ha eliminado.

## Descripción de las columnas

### id
- **Significado**: Identificador único de cada plantilla de correo electrónico.
- **Función**: Clave primaria.
- **Contenido típico**: Una cadena UUID como `da34c6ed-e659-4392-91ea-3c89f9602198`.
- **Nota**: Sirve como identificador principal del registro de la plantilla.

### org_id
- **Significado**: Identificador de la organización asociada a la plantilla de correo electrónico.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID.
- **Nota**: Vincula la plantilla con una organización concreta.

### name
- **Significado**: El nombre de la plantilla de correo electrónico.
- **Función**: Campo descriptivo.
- **Contenido típico**: Texto descriptivo como `Supplier Magic Link Email`.
- **Nota**: Se utiliza para identificar la finalidad de la plantilla.

### email_type
- **Significado**: Tipo o categoría de la plantilla de correo electrónico.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadenas como `supplier_invite`.
- **Nota**: Indica el contexto o el uso de la plantilla.

### value
- **Significado**: El contenido de la plantilla de correo electrónico, normalmente en formato HTML.
- **Función**: Campo de contenido.
- **Contenido típico**: Cadena HTML que contiene el diseño y el contenido del correo electrónico.
- **Nota**: Es la plantilla real que se utiliza en los correos electrónicos.

### created_by
- **Significado**: Identificador del usuario que creó la plantilla.
- **Función**: Campo de metadatos.
- **Contenido típico**: Un entero que representa un ID de usuario.
- **Nota**: Registra quién creó la plantilla.

### created_on
- **Significado**: Marca de tiempo del momento en que se creó la plantilla.
- **Función**: Campo de metadatos.
- **Contenido típico**: Una marca de tiempo como `2024-07-18 13:29:59 UTC`.
- **Nota**: Registra la fecha y la hora de creación.

### last_modified_on
- **Significado**: Marca de tiempo de la última modificación de la plantilla.
- **Función**: Campo de metadatos.
- **Contenido típico**: Una marca de tiempo.
- **Nota**: Registra la actualización más reciente de la plantilla.

### is_deleted
- **Significado**: Indica si la plantilla está marcada como eliminada.
- **Función**: Campo técnico.
- **Contenido típico**: Valor booleano, `True` o `False`.
- **Nota**: Se utiliza para la eliminación lógica (soft delete) de la plantilla.

### deleted_on
- **Significado**: Marca de tiempo del momento en que la plantilla se marcó como eliminada.
- **Función**: Campo de metadatos.
- **Contenido típico**: Una marca de tiempo o `None` si no se ha eliminado.
- **Nota**: Registra cuándo se eliminó la plantilla.

### subject
- **Significado**: La línea de asunto de la plantilla de correo electrónico.
- **Función**: Campo de contenido.
- **Contenido típico**: Texto como `Welcome to Testing Ruiz Foods Supplier Portal. Let's help you get set up`.
- **Nota**: Se utiliza como asunto del correo electrónico cuando se envía la plantilla.

### last_modified_by
- **Significado**: Identificador del usuario que modificó la plantilla por última vez.
- **Función**: Campo de metadatos.
- **Contenido típico**: Un identificador de usuario.
- **Nota**: Registra quién modificó la plantilla por última vez.

### deleted_by
- **Significado**: Identificador del usuario que marcó la plantilla como eliminada.
- **Función**: Campo de metadatos.
- **Contenido típico**: Un identificador de usuario.
- **Nota**: Registra quién eliminó la plantilla.

### doc_type
- **Significado**: Tipo o formato del documento relacionado con la plantilla.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadenas que indican el tipo de documento.
- **Nota**: Podría estar relacionado con el formato o la categoría del contenido del correo electrónico.
```
