# Tfidf preferences

## Columnas

* `id`: interno
* `org_id`: ID de la organización
* `tfidf_id`: interno
* `pref_key`: interno
* `pref_value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_by`: interno
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_by`: interno
* `deleted_on`: timestamp with time zone
* `supplier_id`: interno

## Análisis y descripción

```markdown
# Documentación técnica de la tabla `public.tfidf_preferences`

## Introducción

La tabla `public.tfidf_preferences` parece estar diseñada para almacenar preferencias relacionadas con configuraciones o modelos TF-IDF (Term Frequency-Inverse Document Frequency). Contiene información sobre las preferencias concretas definidas por las organizaciones, incluidas las claves de preferencia y sus valores correspondientes, junto con metadatos sobre las actividades de creación, modificación y eliminación.

## Descripción de las columnas

### id
- **Significado**: Un identificador único de cada registro de la tabla.
- **Función**: Clave primaria.
- **Contenido típico**: Una cadena UUID que representa el ID único de una entrada de preferencia.

### org_id
- **Significado**: Identificador de la organización asociada a la preferencia.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que vincula la preferencia con una organización concreta.

### tfidf_id
- **Significado**: Identificador de la configuración o del modelo TF-IDF concreto.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que representa la configuración TF-IDF vinculada.

### pref_key
- **Significado**: La clave o el nombre del ajuste de preferencia.
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena que representa el nombre de la preferencia, como 'USE_ETEXT_IF_AVAILABLE' o 'AI_MODEL'.

### pref_value
- **Significado**: El valor asociado a la clave de preferencia.
- **Función**: Campo descriptivo.
- **Contenido típico**: Una cadena o un valor de texto que corresponde a la clave de preferencia, p. ej., 'true', 'false' o 'Full'.

### created_by
- **Significado**: Identificador del usuario que creó la entrada de preferencia.
- **Función**: Campo descriptivo.
- **Contenido típico**: Un entero que representa el ID de usuario del creador.

### created_on
- **Significado**: Marca de tiempo de la creación de la entrada de preferencia.
- **Función**: Campo técnico.
- **Contenido típico**: Una marca de tiempo con zona horaria que indica la fecha y la hora de creación.

### last_modified_by
- **Significado**: Identificador del usuario que modificó por última vez la entrada de preferencia.
- **Función**: Campo descriptivo.
- **Contenido típico**: Un UUID que representa el ID de usuario de la última persona que modificó la entrada, si procede.

### last_modified_on
- **Significado**: Marca de tiempo de la última modificación de la entrada de preferencia.
- **Función**: Campo técnico.
- **Contenido típico**: Una marca de tiempo con zona horaria que muestra la fecha y la hora de la última modificación.

### is_deleted
- **Significado**: Indicador que señala si la entrada de preferencia se ha marcado como eliminada.
- **Función**: Campo técnico.
- **Contenido típico**: Un valor booleano; `True` si la entrada está eliminada y `False` en caso contrario.

### deleted_by
- **Significado**: Identificador del usuario que marcó la entrada de preferencia como eliminada.
- **Función**: Campo descriptivo.
- **Contenido típico**: Un UUID que representa el ID del usuario que eliminó la entrada, si procede.

### deleted_on
- **Significado**: Marca de tiempo del momento en que la entrada de preferencia se marcó como eliminada.
- **Función**: Campo técnico.
- **Contenido típico**: Una marca de tiempo con zona horaria que indica cuándo se eliminó la entrada.

### supplier_id
- **Significado**: Identificador del proveedor asociado a la preferencia.
- **Función**: Clave externa.
- **Contenido típico**: Una cadena UUID que representa al proveedor vinculado a la preferencia.

Esta documentación ofrece una visión detallada de la finalidad y la estructura de la tabla `public.tfidf_preferences`, y ayuda a los desarrolladores a comprender cómo interactuar con estos datos y utilizarlos de forma eficaz.
```
