# Tabla public.preferences

## Columnas

* `id`: internal
* `org_id`: ID to organisation
* `pref_key`: internal
* `pref_value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `deleted_on`: timestamp with time zone
* `is_deleted`: boolean
* `user_id`: integer
* `sub_org_id`: internal

## Análisis y descripción

```markdown
# Documentación técnica de la tabla `public.preferences`

## Introducción
La tabla `public.preferences` está diseñada para almacenar ajustes de configuración y preferencias de diversas entidades organizativas dentro de un sistema. Cada entrada de la tabla representa una clave de preferencia específica y su valor correspondiente, asociados a una organización o suborganización. Estos datos de configuración pueden incluir ajustes relacionados con números de IVA, ajustes de extracción, activación de módulos y más.

## Descripción de las columnas

### id
- **Significado**: Esta columna almacena el identificador único de cada entrada de preferencia.
- **Función**: Clave primaria.
- **Contenido típico**: Una cadena UUID que identifica de forma única cada fila, como `23f3d697-7411-4c95-981d-faf089d266be`.

### org_id
- **Significado**: Esta columna almacena el identificador de la organización a la que está asociada la preferencia.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que coincide con una organización, similar a `23f3d697-7411-4c95-981d-faf089d266be`.

### pref_key
- **Significado**: Esta columna representa la clave o el nombre del ajuste de preferencia.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadenas que representan claves de configuración, como `VAT_NUMBERS`, `TABLE_EXTRACTION_SETTING`.

### pref_value
- **Significado**: Esta columna contiene el valor de la preferencia correspondiente a `pref_key`.
- **Función**: Campo descriptivo.
- **Contenido típico**: Varía según `pref_key`; algunos ejemplos son números de IVA separados por comas o valores booleanos como `true` o `false`.

### created_by
- **Significado**: Esta columna indica el ID de usuario de la persona que creó la entrada de preferencia.
- **Función**: Campo descriptivo.
- **Contenido típico**: Un entero que representa un ID de usuario, por ejemplo, `1`.

### created_on
- **Significado**: Esta columna registra la marca de tiempo del momento en que se creó la preferencia.
- **Función**: Campo técnico.
- **Contenido típico**: Una marca de tiempo con zona horaria, por ejemplo, `2021-11-09 11:04:18+00`.

### last_modified_on
- **Significado**: Esta columna recoge la marca de tiempo de la última modificación de la preferencia.
- **Función**: Campo técnico.
- **Contenido típico**: Una marca de tiempo con zona horaria que indica la hora de la última actualización, como `2023-12-04 10:10:26+00`.

### deleted_on
- **Significado**: Esta columna anota la marca de tiempo del momento en que la preferencia se marcó como eliminada.
- **Función**: Campo técnico.
- **Contenido típico**: Normalmente `null`, salvo que la fila esté marcada para su eliminación.

### is_deleted
- **Significado**: Esta columna indica si la preferencia se ha marcado como eliminada.
- **Función**: Campo técnico.
- **Contenido típico**: Un valor booleano, normalmente `false`.

### user_id
- **Significado**: Esta columna almacena el ID de usuario asociado a la preferencia.
- **Función**: Campo descriptivo, potencialmente una clave externa.
- **Contenido típico**: Un entero o `null` si no procede.

### sub_org_id
- **Significado**: Esta columna identifica la suborganización asociada a la preferencia.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID o `null` si no procede.

La tabla `public.preferences` ofrece una forma flexible y completa de gestionar los ajustes de configuración de las distintas entidades organizativas, lo que permite ajustar y registrar las preferencias de forma dinámica a lo largo del tiempo.
```
