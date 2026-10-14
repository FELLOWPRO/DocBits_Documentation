# Purchase Order line

## Tabla `public.purchase_order_line`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `purchase_order_id`: interno
* `purchase_order_number`: interno
* `line_number`: interno
* `item_id`: interno
* `supplier_item_id`: interno
* `description`: interno
* `quantity`: double precision
* `unit_code`: interno
* `unit_price`: double precision
* `total_amount`: double precision
* `currency`: interno
* `status`: interno
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `deleted_on`: timestamp with time zone
* `is_deleted`: boolean
* `open_quantity`: double precision
* `received_quantity`: double precision
* `confirmed_quantity`: double precision
* `note`: text
* `sub_org_id`: interno
* `sub_line_number`: interno
* `unit_price_per`: double precision
* `buyer_id`: interno
* `buyer_name`: interno
* `unit_code_price`: interno
* `geo_code`: interno
* `promised_delivery_date`: timestamp with time zone
* `delivery_method`: interno
* `requested_ship_date`: date
* `received_base_mou_quantity`: double precision
* `extended_amount`: double precision

### Análisis y descripción

## Documentación técnica de la tabla `public.purchase_order_line`

### Introducción

La tabla `public.purchase_order_line` está diseñada para almacenar información detallada de cada línea de un pedido de compra. Recoge diversos atributos de la línea del pedido, como los datos del artículo, las cantidades, los precios y los estados. Esta tabla es fundamental para gestionar y realizar el seguimiento de los pedidos de compra y de su estado de cumplimiento en el contexto de una organización.

### Descripción de las columnas

#### id

* **Significado**: Identificador único de cada línea de artículo del pedido de compra.
* **Función**: Clave primaria.
* **Contenido típico**: Una cadena UUID que identifica de forma única la línea del pedido de compra.

#### org\_id

* **Significado**: Identificador de la organización asociada al pedido de compra.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID que hace referencia a una organización.

#### purchase\_order\_id

* **Significado**: Identificador del pedido de compra al que pertenece la línea de artículo.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID que hace referencia a un pedido de compra.

#### purchase\_order\_number

* **Significado**: El número asignado al pedido de compra.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que representa el número del pedido de compra.

#### line\_number

* **Significado**: El número de línea del artículo dentro del pedido de compra.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que indica la secuencia de la línea en el pedido de compra.

#### item\_id

* **Significado**: Identificador del artículo pedido.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena que representa el código del artículo.

#### supplier\_item\_id

* **Significado**: Identificador del artículo específico del proveedor.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena; puede ser nula si el proveedor no la facilita.

#### description

* **Significado**: Descripción del artículo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una descripción de texto del artículo.

#### quantity

* **Significado**: El número de unidades pedidas.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un valor numérico que indica la cantidad pedida.

#### unit\_code

* **Significado**: Código que representa la unidad de medida del artículo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que representa unidades, p. ej., 'EA' para unidad.

#### unit\_price

* **Significado**: Precio por unidad del artículo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un valor numérico que representa el precio por unidad.

#### total\_amount

* **Significado**: Importe total de la línea de artículo (cantidad \* precio unitario).
* **Función**: Campo descriptivo.
* **Contenido típico**: Un valor numérico que representa el importe total.

#### currency

* **Significado**: Moneda en la que se realiza la compra.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que representa el código de moneda, p. ej., 'USD'.

#### status

* **Significado**: Estado actual de la línea del pedido de compra.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que indica el estado, p. ej., 'Received', 'Invoiced'.

#### created\_by

* **Significado**: Identificador del usuario que creó la entrada.
* **Función**: Clave externa.
* **Contenido típico**: Un entero que representa el ID de usuario.

#### created\_on

* **Significado**: Marca de tiempo de cuándo se creó la entrada.
* **Función**: Campo técnico.
* **Contenido típico**: Una marca de tiempo con información de zona horaria.

#### last\_modified\_on

* **Significado**: Marca de tiempo de la última modificación.
* **Función**: Campo técnico.
* **Contenido típico**: Una marca de tiempo con información de zona horaria; puede ser nula si nunca se ha modificado.

#### deleted\_on

* **Significado**: Marca de tiempo de cuándo se marcó la entrada como eliminada.
* **Función**: Campo técnico.
* **Contenido típico**: Una marca de tiempo con información de zona horaria; puede ser nula si no se ha eliminado.

#### is\_deleted

* **Significado**: Indica si la entrada se ha marcado como eliminada.
* **Función**: Campo técnico.
* **Contenido típico**: Valor booleano (true/false).

#### open\_quantity

* **Significado**: Cantidad aún no recibida ni facturada.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un valor numérico, normalmente cero si se ha recibido por completo.

#### received\_quantity

* **Significado**: Cantidad que se ha recibido.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un valor numérico que indica la cantidad recibida.

#### confirmed\_quantity

* **Significado**: Cantidad confirmada por el proveedor.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un valor numérico; puede ser nulo si no se ha confirmado.

#### note

* **Significado**: Notas adicionales sobre la línea del pedido de compra.
* **Función**: Campo descriptivo.
* **Contenido típico**: Texto; puede incluir instrucciones especiales o comentarios.

#### sub\_org\_id

* **Significado**: Identificador de la suborganización asociada a la línea del pedido de compra.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena; puede ser nula si no procede.

#### sub\_line\_number

* **Significado**: Número de sublínea dentro del pedido de compra.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que representa la secuencia de la sublínea.

#### unit\_price\_per

* **Significado**: Precio unitario base del artículo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un valor numérico que representa el precio unitario base.

#### buyer\_id

* **Significado**: Identificador del comprador responsable de la compra.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena que representa el ID del comprador.

#### buyer\_name

* **Significado**: Nombre del comprador responsable.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que representa el nombre del comprador.

#### unit\_code\_price

* **Significado**: Código de unidad relacionado con el precio.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena, similar a unit\_code.

#### geo\_code

* **Significado**: Código geográfico de la entrega.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que representa una ubicación geográfica.

#### promised\_delivery\_date

* **Significado**: Fecha prometida para la entrega.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una marca de tiempo con información de zona horaria.

#### delivery\_method

* **Significado**: Método de entrega de la línea del pedido de compra.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que representa el método de entrega.

#### requested\_ship\_date

* **Significado**: Fecha solicitada para el envío.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un valor de fecha.

#### received\_base\_mou\_quantity

* **Significado**: Cantidad recibida en unidades de medida base.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un valor numérico que indica la cantidad recibida en unidades de medida base (MOU).

#### extended\_amount

* **Significado**: Importe ampliado de la línea de artículo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un valor numérico que representa el importe ampliado, que puede ser igual a total\_amount si no se aplican descuentos ni cargos adicionales.
