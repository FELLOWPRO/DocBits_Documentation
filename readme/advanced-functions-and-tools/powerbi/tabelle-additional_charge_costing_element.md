# Tabla additional\_charge\_costing\_element

## Tabla `public.additional_charge_costing_element`

### Columnas

* `id`: internal
* `org_id`: ID to organisation
* `costing_element`: internal
* `description`: internal
* `charge_type`: internal
* `distribution_method`: internal
* `distribution_type`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `sub_org_id`: internal
* `charge_count`: integer
* `charge_icon`: internal
* `charge_category`: internal
* `charge_sequence_number`: integer
* `charge_operator`: integer
* `last_modified_by`: internal
* `deleted_by`: internal

### Análisis y descripción

## Documentación de la tabla: `public.additional_charge_costing_element`

### Introducción

La tabla `public.additional_charge_costing_element` está diseñada para gestionar y almacenar información sobre diversos elementos de coste de cargos adicionales dentro de una organización. Esto incluye datos sobre el tipo de cargos, cómo se distribuyen y metadatos administrativos como los detalles de creación y modificación. Es probable que esta tabla se utilice para la gestión financiera y operativa de una organización, centrándose en los costes adicionales que deben registrarse y analizarse.

### Descripción de las columnas

#### id

* **Significado**: Esta columna almacena un identificador único para cada registro de la tabla.
* **Función**: Clave primaria.
* **Contenido típico**: Una cadena alfanumérica única que identifica cada registro de elemento de coste.

#### org\_id

* **Significado**: El identificador de la organización a la que pertenece este elemento de coste.
* **Función**: Clave externa.
* **Contenido típico**: Un UUID que representa la organización.

#### costing\_element

* **Significado**: Un identificador o código del elemento de coste.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena alfanumérica que representa el elemento de coste específico.

#### description

* **Significado**: Una descripción textual del elemento de coste.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una breve explicación textual del elemento de coste.

#### charge\_type

* **Significado**: El tipo de cargo asociado a este elemento de coste.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un código o texto breve que indica el tipo de cargo.

#### distribution\_method

* **Significado**: Método mediante el cual se distribuye el cargo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un código o texto breve que indica el método de distribución.

#### distribution\_type

* **Significado**: Tipo de distribución del cargo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un código o texto breve que indica el tipo de distribución.

#### created\_by

* **Significado**: Identificador del usuario que creó el registro.
* **Función**: Campo administrativo.
* **Contenido típico**: Un entero que representa el ID del usuario.

#### created\_on

* **Significado**: Marca de tiempo que indica cuándo se creó el registro.
* **Función**: Campo administrativo.
* **Contenido típico**: Una marca de tiempo con información de zona horaria.

#### last\_modified\_on

* **Significado**: Marca de tiempo de la última modificación realizada en el registro.
* **Función**: Campo administrativo.
* **Contenido típico**: Una marca de tiempo con información de zona horaria.

#### is\_deleted

* **Significado**: Indica si el registro está marcado como eliminado.
* **Función**: Campo técnico.
* **Contenido típico**: Valor booleano (`True` o `False`).

#### deleted\_on

* **Significado**: Marca de tiempo del momento en que el registro se marcó como eliminado.
* **Función**: Campo administrativo.
* **Contenido típico**: Una marca de tiempo con información de zona horaria o `None` si no se ha eliminado.

#### sub\_org\_id

* **Significado**: Identificador de una suborganización relacionada con el elemento de coste.
* **Función**: Clave externa.
* **Contenido típico**: Un UUID que representa la suborganización.

#### charge\_count

* **Significado**: El número de cargos asociados al elemento de coste.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un entero que representa el recuento de cargos.

#### charge\_icon

* **Significado**: Icono o símbolo asociado al cargo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que representa el icono, probablemente una ruta o un identificador.

#### charge\_category

* **Significado**: La categoría a la que pertenece el cargo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que representa la categoría del cargo.

#### charge\_sequence\_number

* **Significado**: Número de secuencia para ordenar los cargos.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un entero utilizado para secuenciar los cargos.

#### charge\_operator

* **Significado**: Identificador del operador responsable del cargo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un entero que representa el ID del operador.

#### last\_modified\_by

* **Significado**: Identificador del usuario que modificó el registro por última vez.
* **Función**: Campo administrativo.
* **Contenido típico**: Una cadena que representa el ID del usuario, posiblemente `None` si nunca se ha modificado.

#### deleted\_by

* **Significado**: Identificador del usuario que marcó el registro como eliminado.
* **Función**: Campo administrativo.
* **Contenido típico**: Una cadena que representa el ID del usuario, posiblemente `None` si no se ha eliminado.
