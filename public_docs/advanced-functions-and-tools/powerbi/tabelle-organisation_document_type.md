# Tabla organisation\_document\_type

## Columnas

* `id`: internal
* `org_id`: ID to organisation
* `document_type_id`: internal
* `document_type_key`: internal
* `document_locale`: internal
* `classification_method`: internal
* `is_active`: boolean
* `extraction_type`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `sub_org_id`: internal

## Análisis y descripción

```markdown
# Documentación técnica de la tabla `public.organisation_document_type`

## Introducción

La tabla `public.organisation_document_type` está diseñada para gestionar y almacenar información sobre los distintos tipos de documento asociados a las organizaciones. Esto incluye detalles como la clave del tipo de documento, la configuración regional, los métodos de clasificación y el estado del tipo de documento (activo, eliminado, etc.). Parece servir como asignación entre las organizaciones y los tipos de documento que utilizan o gestionan, junto con metadatos sobre dichos documentos.

## Descripción de las columnas

### id
- **Significado**: Identificador único de cada registro de la tabla.
- **Función**: Clave primaria.
- **Contenido típico**: Una cadena UUID que identifica de forma única una entrada de tipo de documento.
- **Nota**: Imprescindible para distinguir cada registro.

### org_id
- **Significado**: Identificador de la organización relacionada con el tipo de documento.
- **Función**: Clave externa, que probablemente hace referencia a una tabla de organizaciones.
- **Contenido típico**: Una cadena UUID.
- **Nota**: Conecta el tipo de documento con una organización concreta.

### document_type_id
- **Significado**: Identificador del tipo de documento.
- **Función**: Clave externa, posiblemente vinculada a una tabla de referencia de tipos de documento.
- **Contenido típico**: Una cadena UUID.
- **Nota**: Permite la asignación a tipos de documento específicos.

### document_type_key
- **Significado**: Una clave o código que representa el tipo de documento.
- **Función**: Campo descriptivo para la clasificación del tipo de documento.
- **Contenido típico**: Una cadena que actúa como identificador o etiqueta del tipo de documento.
- **Nota**: Se utiliza para identificar el tipo de documento en un formato legible.

### document_locale
- **Significado**: Configuración regional o de idioma del tipo de documento.
- **Función**: Campo descriptivo para la especificación de la configuración regional.
- **Contenido típico**: Una cadena, a menudo 'auto', que indica la determinación automática de la configuración regional.
- **Nota**: Útil para fines de internacionalización y localización.

### classification_method
- **Significado**: Método utilizado para clasificar el tipo de documento.
- **Función**: Campo descriptivo que indica cómo se clasifica el documento.
- **Contenido típico**: Una cadena, a menudo 'auto', que sugiere una clasificación automática.
- **Nota**: Importante para comprender el proceso de clasificación.

### is_active
- **Significado**: Estado que indica si el tipo de documento está activo.
- **Función**: Campo de estado booleano.
- **Contenido típico**: `True` o `False`.
- **Nota**: Determina si el tipo de documento está actualmente en uso.

### extraction_type
- **Significado**: Tipo de método de extracción utilizado para el documento.
- **Función**: Campo descriptivo para el proceso de extracción.
- **Contenido típico**: Cadenas como 'FIX_COORDINATES', 'FLEX_COORDINATES' o `None`.
- **Nota**: Ofrece información sobre cómo se extraen los datos de los documentos.

### created_by
- **Significado**: Identificador del usuario que creó el registro.
- **Función**: Campo técnico con fines de auditoría.
- **Contenido típico**: Un entero que representa un ID de usuario.
- **Nota**: Útil para el seguimiento de cambios y la trazabilidad.

### created_on
- **Significado**: Marca de tiempo del momento en que se creó el registro.
- **Función**: Campo técnico con fines de auditoría.
- **Contenido típico**: Una marca de tiempo con zona horaria.
- **Nota**: Importante para registrar la fecha y la hora de creación del registro.

### last_modified_on
- **Significado**: Marca de tiempo de la última modificación del registro.
- **Función**: Campo técnico con fines de auditoría.
- **Contenido típico**: Una marca de tiempo con zona horaria.
- **Nota**: Útil para el seguimiento de las actualizaciones y los cambios del registro.

### is_deleted
- **Significado**: Estado que indica si el registro se ha marcado como eliminado.
- **Función**: Campo de estado booleano.
- **Contenido típico**: `True` o `False`.
- **Nota**: Ayuda a implementar la funcionalidad de eliminación lógica (soft delete).

### sub_org_id
- **Significado**: Identificador de una suborganización relacionada con el tipo de documento.
- **Función**: Posible clave externa, que añade una estructura jerárquica de organización.
- **Contenido típico**: Una cadena UUID o `None`.
- **Nota**: Proporciona contexto adicional sobre la estructura de la organización.

```
