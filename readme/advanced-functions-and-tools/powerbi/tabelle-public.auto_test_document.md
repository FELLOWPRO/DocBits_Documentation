# Tabla public.auto\_test\_document

## Columnas

* `id`: internal
* `org_id`: ID to organisation
* `doc_id`: internal
* `doc_type`: DOC Type
* `extracted_data`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `filename`: internal

## Análisis y descripción

```markdown
# Documentación de la tabla: `public.auto_test_document`

## Introducción

La tabla `public.auto_test_document` está diseñada para almacenar metadatos y resultados de extracción del procesamiento de documentos dentro de una organización. La tabla recoge información sobre los documentos, sus tipos y los datos extraídos de ellos. Incluye campos para la identificación del documento, metadatos de procesamiento e indicadores de estado, que son esenciales para gestionar los flujos de trabajo de documentos y garantizar la integridad de los datos.

## Descripción de las columnas

### id
- **Significado**: Identificador único de cada entrada de documento de la tabla.
- **Función**: Clave primaria.
- **Contenido típico**: Cadena UUID.
- **Nota**: Sirve como identificador único de los registros y garantiza que cada entrada sea distinta.

### org_id
- **Significado**: Identificador de la organización asociada al documento.
- **Función**: Clave externa.
- **Contenido típico**: Cadena UUID.
- **Nota**: Vincula el documento con una organización concreta dentro del sistema.

### doc_id
- **Significado**: Identificador del documento que se está procesando.
- **Función**: Clave externa.
- **Contenido típico**: Cadena UUID.
- **Nota**: Se utiliza para asociar los datos extraídos con el documento original.

### doc_type
- **Significado**: Tipo o categoría del documento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadena como "MEDI_ORDER".
- **Nota**: Ayuda a categorizar los documentos para su procesamiento y análisis.

### extracted_data
- **Significado**: Estructura JSON que contiene los datos detallados extraídos del documento.
- **Función**: Campo de datos.
- **Contenido típico**: Texto JSON con campos, valores y metadatos de extracción.
- **Nota**: Almacena los resultados del proceso de extracción de datos del documento.

### created_by
- **Significado**: Identificador del usuario que creó el registro del documento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Entero que representa un ID de usuario.
- **Nota**: Registra qué usuario inició la entrada del documento en el sistema.

### created_on
- **Significado**: Marca de tiempo que indica cuándo se creó el registro del documento.
- **Función**: Campo técnico.
- **Contenido típico**: Fecha y hora con información de zona horaria.
- **Nota**: Útil para la auditoría y el seguimiento del ciclo de vida del documento.

### last_modified_on
- **Significado**: Marca de tiempo que indica la última modificación realizada en el registro del documento.
- **Función**: Campo técnico.
- **Contenido típico**: Fecha y hora con información de zona horaria.
- **Nota**: Ayuda a realizar un seguimiento de los cambios y las actualizaciones del registro del documento.

### is_deleted
- **Significado**: Indicador que señala si el registro del documento se ha marcado como eliminado.
- **Función**: Campo de estado.
- **Contenido típico**: Valor booleano.
- **Nota**: Facilita la eliminación lógica (soft delete) de registros y permite su recuperación si es necesario.

### filename
- **Significado**: Nombre del archivo asociado al documento.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadena, por ejemplo, "7.pdf".
- **Nota**: Proporciona una referencia al archivo físico asociado a la entrada del documento.

```
