# Tabla po\_match\_tolerance

## Tabla `public.po_match_tolerance`

### Columnas

* `id`: internal
* `org_id`: ID to organisation
* `item_number`: internal
* `supplier_item_number`: internal
* `description`: internal
* `unit_price_tolerance`: double precision
* `quantity_tolerance`: double precision
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `unit_price_tolerance_type`: internal
* `quantity_tolerance_type`: internal

### Análisis y descripción

## Documentación técnica de la tabla `public.po_match_tolerance`

### Introducción

La tabla `public.po_match_tolerance` está diseñada para gestionar y almacenar los niveles de tolerancia asociados a los procesos de conciliación de pedidos de compra (PO). Normalmente se trata de las discrepancias admisibles en los precios unitarios y las cantidades entre las mercancías pedidas y las recibidas. Cada entrada de la tabla representa la configuración de tolerancia de un artículo concreto, lo que puede ayudar a las organizaciones a garantizar la coherencia y la precisión en sus procesos de compras.

### Descripción de las columnas

#### id

* **Significado**: Un identificador único para cada entrada de la tabla.
* **Función**: Clave primaria.
* **Contenido típico**: Una cadena UUID que identifica de forma única cada registro de configuración de tolerancia.

#### org\_id

* **Significado**: Identificador de la organización asociada a la configuración de tolerancia.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID que enlaza con la organización dentro del sistema.

#### item\_number

* **Significado**: El número de artículo para el que se define la configuración de tolerancia.
* **Función**: Identificador de negocio.
* **Contenido típico**: Una cadena que representa el código o número del artículo en el inventario de la organización.

#### supplier\_item\_number

* **Significado**: El número de artículo tal como lo proporciona el proveedor.
* **Función**: Identificador de negocio.
* **Contenido típico**: Una cadena que puede ser `None` si no se ha proporcionado y que representa el código o número del artículo para el proveedor.

#### description

* **Significado**: Una descripción textual del artículo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que ofrece detalles sobre el artículo, que puede ser `None`.

#### unit\_price\_tolerance

* **Significado**: La variación admisible en el precio unitario del artículo.
* **Función**: Regla de negocio.
* **Contenido típico**: Un valor numérico que indica la tolerancia del precio unitario como porcentaje o como valor absoluto.

#### quantity\_tolerance

* **Significado**: La variación admisible en la cantidad del artículo.
* **Función**: Regla de negocio.
* **Contenido típico**: Un valor numérico que indica la tolerancia de la cantidad como porcentaje o como valor absoluto.

#### created\_by

* **Significado**: Identificador del usuario que creó la entrada.
* **Función**: Campo de auditoría/registro.
* **Contenido típico**: Un entero que normalmente hace referencia a un ID de usuario del sistema.

#### created\_on

* **Significado**: La marca de tiempo del momento en que se creó la entrada.
* **Función**: Campo de auditoría/registro.
* **Contenido típico**: Un valor de fecha y hora con zona horaria que indica la fecha y la hora de creación.

#### last\_modified\_on

* **Significado**: La marca de tiempo de la última modificación de la entrada.
* **Función**: Campo de auditoría/registro.
* **Contenido típico**: Un valor de fecha y hora con zona horaria que indica cuándo se actualizó el registro por última vez, que puede ser `None` si no se ha modificado.

#### is\_deleted

* **Significado**: Indica si la entrada está eliminada de forma lógica.
* **Función**: Indicador técnico/de eliminación lógica (soft delete).
* **Contenido típico**: Un valor booleano donde `False` significa activa y `True` significa eliminada de forma lógica.

#### unit\_price\_tolerance\_type

* **Significado**: Define el tipo de tolerancia del precio unitario (por ejemplo, porcentaje o valor absoluto).
* **Función**: Regla de negocio.
* **Contenido típico**: Una cadena, a menudo 'value', que indica el tipo de medida de tolerancia.

#### quantity\_tolerance\_type

* **Significado**: Define el tipo de tolerancia de la cantidad (por ejemplo, porcentaje o valor absoluto).
* **Función**: Regla de negocio.
* **Contenido típico**: Una cadena, a menudo 'value', que indica el tipo de medida de tolerancia.

Esta documentación ofrece una visión detallada de cada campo de la tabla `public.po_match_tolerance` y aporta información sobre su posible contenido y su función en el contexto de la gestión de pedidos de compra.
