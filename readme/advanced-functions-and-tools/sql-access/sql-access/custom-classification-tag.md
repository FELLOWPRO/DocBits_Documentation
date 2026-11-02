# Etiqueta de clasificación personalizada

## Tabla `public.custom_classification_tag`

### Columnas

* `id`: integer
* `org_id`: ID de la organización
* `name`: interno
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean

### Análisis y descripción

## Documentación técnica de la tabla `public.custom_classification_tag`

### Introducción

La tabla `public.custom_classification_tag` está diseñada para gestionar las etiquetas de clasificación personalizadas dentro de una organización. Recoge información esencial de cada etiqueta, incluida su asociación con una organización, los detalles de creación y modificación y su estado en el ciclo de vida.

### Descripción de las columnas

#### id

* **Significado**: Un identificador único para cada etiqueta de clasificación.
* **Función**: Clave primaria.
* **Contenido típico**: Un valor entero que identifica de forma única cada registro de la tabla.

#### org\_id

* **Significado**: El identificador de la organización a la que pertenece la etiqueta de clasificación.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena de caracteres, probablemente un UUID, que representa el ID único de la organización.

#### name

* **Significado**: El nombre o la etiqueta de la etiqueta de clasificación.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que indica el nombre o la descripción de la etiqueta. Puede ser una cadena vacía si no se proporciona el nombre.

#### created\_by

* **Significado**: El identificador del usuario que creó la etiqueta de clasificación.
* **Función**: Clave externa.
* **Contenido típico**: Un entero que representa el ID de usuario del creador.

#### created\_on

* **Significado**: La marca de tiempo que indica cuándo se creó la etiqueta de clasificación.
* **Función**: Campo técnico.
* **Contenido típico**: Una marca de tiempo con zona horaria que recoge la fecha y la hora exactas de creación.

#### last\_modified\_on

* **Significado**: La marca de tiempo de la última modificación realizada en la etiqueta de clasificación.
* **Función**: Campo técnico.
* **Contenido típico**: Una marca de tiempo con zona horaria, que puede ser `None` si no se ha producido ninguna modificación desde la creación.

#### is\_deleted

* **Significado**: Un indicador que señala si la etiqueta de clasificación se ha marcado como eliminada.
* **Función**: Campo técnico.
* **Contenido típico**: Un valor booleano (`True` o `False`), donde `False` significa que la etiqueta está activa y `True` indica que se ha eliminado o desactivado.
