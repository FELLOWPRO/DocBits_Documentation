# Tolerancia de conciliación con órdenes de compra

## Tabla `public.po_match_tolerance`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `item_number`: interno
* `supplier_item_number`: interno
* `description`: interno
* `unit_price_tolerance`: double precision
* `quantity_tolerance`: double precision
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean
* `unit_price_tolerance_type`: interno
* `quantity_tolerance_type`: interno

### Análisis y descripción

## Documentación técnica de la tabla `public.po_match_tolerance`

### Introducción

La tabla `public.po_match_tolerance` está diseñada para gestionar y almacenar los niveles de tolerancia asociados a los procesos de PO matching (conciliación de pedidos de compra). Normalmente se trata de las discrepancias admisibles en los precios unitarios y las cantidades entre las mercancías pedidas y las recibidas. Cada entrada de la tabla representa los ajustes de tolerancia de artículos concretos y puede ayudar a las organizaciones a garantizar la coherencia y la precisión de sus procesos de compras.

### Descripción de las columnas

#### id

* **Significado**: Un identificador único de cada entrada de la tabla.
* **Función**: Clave primaria.
* **Contenido típico**: Una cadena UUID que identifica de forma única cada registro de ajustes de tolerancia.

#### org\_id

* **Significado**: Identificador de la organización asociada a los ajustes de tolerancia.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID que enlaza con la organización dentro del sistema.

#### item\_number

* **Significado**: El número de artículo concreto para el que se definen los ajustes de tolerancia.
* **Función**: Identificador de negocio.
* **Contenido típico**: Una cadena que representa el código o número del artículo en el inventario de la organización.

#### supplier\_item\_number

* **Significado**: El número de artículo tal como lo facilita el proveedor.
* **Función**: Identificador de negocio.
* **Contenido típico**: Una cadena que puede ser `None` si no se facilita y que representa el código o número del artículo del proveedor.

#### description

* **Significado**: Una descripción textual del artículo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena con detalles sobre el artículo, que puede ser `None`.

#### unit\_price\_tolerance

* **Significado**: La variación admisible en el precio unitario del artículo.
* **Función**: Regla de negocio.
* **Contenido típico**: Un valor numérico que indica la tolerancia porcentual o en valor absoluto del precio unitario.

#### quantity\_tolerance

* **Significado**: La variación admisible en la cantidad del artículo.
* **Función**: Regla de negocio.
* **Contenido típico**: Un valor numérico que indica la tolerancia porcentual o en valor absoluto de la cantidad.

#### created\_by

* **Significado**: Identificador del usuario que creó la entrada.
* **Función**: Campo de auditoría y registro.
* **Contenido típico**: Un entero que normalmente hace referencia a un ID de usuario del sistema.

#### created\_on

* **Significado**: La marca de tiempo de cuándo se creó la entrada.
* **Función**: Campo de auditoría y registro.
* **Contenido típico**: Un valor de fecha y hora con zona horaria que indica la fecha y la hora de creación.

#### last\_modified\_on

* **Significado**: La marca de tiempo de la última modificación de la entrada.
* **Función**: Campo de auditoría y registro.
* **Contenido típico**: Un valor de fecha y hora con zona horaria que indica cuándo se actualizó el registro por última vez; puede ser `None` si no se ha modificado.

#### is\_deleted

* **Significado**: Indica si la entrada está eliminada lógicamente.
* **Función**: Indicador técnico de eliminación lógica.
* **Contenido típico**: Un valor booleano en el que `False` significa activa y `True` significa eliminada lógicamente.

#### unit\_price\_tolerance\_type

* **Significado**: Define el tipo de tolerancia del precio unitario (p. ej., porcentaje o valor absoluto).
* **Función**: Regla de negocio.
* **Contenido típico**: Una cadena, a menudo 'value', que indica el tipo de medida de tolerancia.

#### quantity\_tolerance\_type

* **Significado**: Define el tipo de tolerancia de la cantidad (p. ej., porcentaje o valor absoluto).
* **Función**: Regla de negocio.
* **Contenido típico**: Una cadena, a menudo 'value', que indica el tipo de medida de tolerancia.

Esta documentación ofrece una visión detallada de cada campo de la tabla `public.po_match_tolerance` y de su posible contenido y función en el contexto de la gestión de pedidos de compra.
