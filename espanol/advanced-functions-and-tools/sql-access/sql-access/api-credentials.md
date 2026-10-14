# API credentials

## Columnas

* `id`: interno
* `org_id`: ID de la organización
* `sub_org_id`: interno
* `title`: interno
* `credentials_type`: interno
* `credentials_json`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `last_modified_by`: interno
* `deleted_by`: interno

## Análisis y descripción

```markdown
# Documentación de la tabla: `public.api_credentials`

## Introducción

La tabla `public.api_credentials` está diseñada para almacenar y gestionar la información de credenciales de API. Esta tabla es fundamental para que las organizaciones gestionen de forma segura sus datos de autenticación de API, de modo que los distintos servicios puedan interactuar entre sí con las credenciales correctas. Incluye información sobre el tipo de credenciales, la organización a la que pertenecen y metadatos sobre su creación y modificación.

## Descripción de las columnas

### id
- **Significado**: Un identificador único para cada entrada de la tabla.
- **Función**: Clave primaria.
- **Contenido típico**: Un identificador único universal (UUID) que representa un conjunto concreto de credenciales de API.

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
- **Contenido típico**: Una cadena como "ionapi" que indica el formato o el protocolo que utilizan las credenciales.

### credentials_json
- **Significado**: Un objeto JSON que contiene información detallada de las credenciales.
- **Función**: Campo técnico.
- **Contenido típico**: Cadena JSON con diversos pares clave-valor que detallan los parámetros de autenticación.

### created_by
- **Significado**: ID de usuario de la persona que creó el registro de credenciales.
- **Función**: Campo técnico.
- **Contenido típico**: Un entero que representa el ID del usuario.

### created_on
- **Significado**: Marca de tiempo que indica cuándo se crearon las credenciales.
- **Función**: Campo técnico.
- **Contenido típico**: Un valor de fecha y hora con zona horaria, p. ej., `2024-04-08 11:54:55 UTC`.

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
