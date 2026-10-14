# Tabla public.api\_credentials

## Columnas

* `id`: internal
* `org_id`: ID to organisation
* `sub_org_id`: internal
* `title`: internal
* `credentials_type`: internal
* `credentials_json`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `last_modified_by`: internal
* `deleted_by`: internal

## Análisis y descripción

```markdown
# Documentación de la tabla: `public.api_credentials`

## Introducción

La tabla `public.api_credentials` está diseñada para almacenar y gestionar la información de las credenciales de API. Esta tabla es fundamental para que las organizaciones gestionen de forma segura sus datos de autenticación de API y para garantizar que los distintos servicios puedan interactuar entre sí con las credenciales correctas. Incluye información sobre el tipo de credenciales, la organización a la que pertenecen y metadatos sobre su creación y modificación.

## Descripción de las columnas

### id
- **Significado**: Un identificador único para cada entrada de la tabla.
- **Función**: Clave primaria.
- **Contenido típico**: Un identificador único universal (UUID) que representa un conjunto específico de credenciales de API.

### org_id
- **Significado**: Identificador de la organización propietaria de las credenciales.
- **Función**: Clave externa.
- **Contenido típico**: Un UUID que enlaza con el registro de la organización en otra tabla.

### sub_org_id
- **Significado**: Identificador de una suborganización dentro de la organización principal.
- **Función**: Clave externa (opcional).
- **Contenido típico**: Puede contener un UUID que enlaza con una suborganización, o `None`.

### title
- **Significado**: Un título descriptivo de las credenciales de API.
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena como "supplier_auth" que indica la finalidad o el uso de las credenciales.

### credentials_type
- **Significado**: Especifica el tipo de credenciales almacenadas.
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena como "ionapi" que indica el formato o el protocolo utilizado por las credenciales.

### credentials_json
- **Significado**: Un objeto JSON que contiene información detallada de las credenciales.
- **Función**: Campo técnico.
- **Contenido típico**: Una cadena JSON con diversos pares clave-valor que detallan los parámetros de autenticación.

### created_by
- **Significado**: ID de usuario de la persona que creó el registro de credenciales.
- **Función**: Campo técnico.
- **Contenido típico**: Un entero que representa el ID de usuario.

### created_on
- **Significado**: Marca de tiempo que indica cuándo se crearon las credenciales.
- **Función**: Campo técnico.
- **Contenido típico**: Un valor de fecha y hora con zona horaria, por ejemplo, `2024-04-08 11:54:55 UTC`.

### last_modified_on
- **Significado**: Marca de tiempo que indica la hora de la última modificación de las credenciales.
- **Función**: Campo técnico.
- **Contenido típico**: Un valor de fecha y hora con zona horaria, o `None` si nunca se ha modificado.

### is_deleted
- **Significado**: Indicador que señala si las credenciales están marcadas como eliminadas.
- **Función**: Campo técnico.
- **Contenido típico**: Un valor booleano, donde `False` indica credenciales activas.

### deleted_on
- **Significado**: Marca de tiempo que indica cuándo se marcaron las credenciales como eliminadas.
- **Función**: Campo técnico.
- **Contenido típico**: Un valor de fecha y hora con zona horaria, o `None` si no se han eliminado.

### last_modified_by
- **Significado**: Identificador del usuario que modificó las credenciales por última vez.
- **Función**: Campo técnico.
- **Contenido típico**: Una cadena de caracteres que representa el ID del usuario, o `None`.

### deleted_by
- **Significado**: Identificador del usuario que marcó las credenciales como eliminadas.
- **Función**: Campo técnico.
- **Contenido típico**: Una cadena de caracteres que representa el ID del usuario, o `None`.
```
