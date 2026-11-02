# Tabla de búsqueda

## Tabla `public.lookup_table`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `data_key`: interno
* `rec_id`: interno
* `prop_name`: interno
* `prop_value`: interno
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean
* `prop_value_clean`: interno
* `version`: integer
* `deleted_on`: marca de tiempo con zona horaria
* `sub_org_id`: interno

### Análisis y descripción

## Documentación técnica de `public.lookup_table`

### Introducción

La tabla `public.lookup_table` está diseñada para almacenar metadatos sobre diversas propiedades asociadas a los datos de la organización. Probablemente funciona como un almacén de clave-valor para distintos atributos relacionados con clientes u otras entidades de la organización. La tabla recoge información como los nombres de las propiedades, sus valores y el contexto (p. ej., la organización y la suborganización a las que pertenecen), junto con información de auditoría como las marcas de tiempo de creación y modificación.

### Descripción de las columnas

#### `id`

* **Significado**: Identificador único de cada registro de la tabla.
* **Función**: Clave primaria.
* **Contenido típico**: Una cadena UUID que identifica de forma única cada entrada.

#### `org_id`

* **Significado**: Identificador de la organización a la que pertenecen los datos.
* **Función**: Clave externa, que probablemente enlaza con una tabla de organizaciones.
* **Contenido típico**: Una cadena UUID que representa la organización.

#### `data_key`

* **Significado**: Una clave que representa un conjunto de datos o un contexto concreto dentro de la organización.
* **Función**: Identificador contextual para agrupar propiedades relacionadas.
* **Contenido típico**: Cadena alfanumérica que indica una categoría, como `customer_amier`.

#### `rec_id`

* **Significado**: Identificador de un registro concreto dentro del conjunto de datos.
* **Función**: Identificador contextual, posiblemente una clave externa a otra tabla.
* **Contenido típico**: Cadena alfanumérica o nulo en los registros sin un identificador específico.

#### `prop_name`

* **Significado**: Nombre de la propiedad o del atributo.
* **Función**: Campo descriptivo que indica qué representa el valor de la propiedad.
* **Contenido típico**: Cadenas como 'Kundennummer', 'Versandanschrift', 'Kundenname', etc.

#### `prop_value`

* **Significado**: Valor de la propiedad descrita por `prop_name`.
* **Función**: Campo descriptivo que contiene el dato o valor real.
* **Contenido típico**: Cadenas o números que representan el valor de la propiedad.

#### `created_by`

* **Significado**: Identificador del usuario o del sistema que creó el registro.
* **Función**: Campo técnico con fines de auditoría.
* **Contenido típico**: Un entero que representa un ID de usuario.

#### `created_on`

* **Significado**: Marca de tiempo que indica cuándo se creó el registro.
* **Función**: Campo técnico con fines de auditoría.
* **Contenido típico**: Fecha y hora con información de zona horaria.

#### `last_modified_on`

* **Significado**: Marca de tiempo que indica la última vez que se modificó el registro.
* **Función**: Campo técnico con fines de auditoría.
* **Contenido típico**: Fecha y hora con información de zona horaria; puede ser nulo si no se ha modificado.

#### `is_deleted`

* **Significado**: Indicador que señala si el registro está eliminado.
* **Función**: Campo técnico que indica la eliminación lógica.
* **Contenido típico**: Valor booleano (`True` o `False`).

#### `prop_value_clean`

* **Significado**: Versión limpia o procesada de `prop_value`.
* **Función**: Campo descriptivo para almacenar un valor normalizado o estandarizado.
* **Contenido típico**: Similar a `prop_value`; puede ser nulo si no procede.

#### `version`

* **Significado**: Número de versión del registro.
* **Función**: Campo técnico para el control de versiones.
* **Contenido típico**: Un entero que representa la versión del registro.

#### `deleted_on`

* **Significado**: Marca de tiempo que indica cuándo se marcó el registro como eliminado.
* **Función**: Campo técnico con fines de auditoría.
* **Contenido típico**: Fecha y hora con información de zona horaria; puede ser nulo si no se ha eliminado.

#### `sub_org_id`

* **Significado**: Identificador de una suborganización dentro de la organización principal.
* **Función**: Clave externa, que posiblemente enlaza con una tabla de suborganizaciones.
* **Contenido típico**: Una cadena UUID que representa la suborganización; puede ser nulo si no procede.
