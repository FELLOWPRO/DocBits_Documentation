# public.receive\_delivery\_line

## Tabla `public.receive_delivery_line`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `receive_delivery_id`: interno
* `delivery_number`: interno
* `line_number`: interno
* `item_id`: interno
* `description`: interno
* `shipped_quantity`: double precision
* `status`: interno
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `deleted_on`: timestamp with time zone
* `is_deleted`: boolean
* `purchase_order`: interno
* `sequence_number`: interno
* `sub_org_id`: interno
* `shipped_quantity_unit_code`: interno
* `packing_slip_quantity`: double precision
* `packing_slip_quantity_unit_code`: interno
* `received_quantity`: double precision
* `received_quantity_unit_code`: interno
* `purchase_order_line_number`: interno
* `status_effective_from`: timestamp with time zone
* `purchase_order_sub_line_number`: interno
* `invoiced_quantity`: double precision
* `invoice_matching_status`: interno
* `open_quantity`: double precision
* `last_modified_by`: interno
* `deleted_by`: interno

### Análisis y descripción

## Documentación de la tabla: `public.receive_delivery_line`

### Introducción

La tabla `public.receive_delivery_line` parece ser un registro detallado de las líneas de entrega y recepción asociadas con las operaciones de logística y cadena de suministro de una organización. Cada fila de la tabla representa una línea concreta de una entrega y recoge detalles como la descripción del artículo, las cantidades enviadas y recibidas y diversos campos de estado. La tabla es un componente vital para el seguimiento del movimiento de las mercancías desde el envío hasta la recepción, incluida la facturación y la gestión de pedidos.

### Descripción de las columnas

#### id

* **Significado**: Identificador único de cada línea de artículo de la entrega.
* **Función**: Clave primaria.
* **Contenido típico**: Un identificador único universal (UUID).

#### org\_id

* **Significado**: Identificador de la organización asociada con la entrega.
* **Función**: Clave externa.
* **Contenido típico**: Un UUID que representa la organización.

#### receive\_delivery\_id

* **Significado**: Identificador que enlaza con la transacción de entrega global.
* **Función**: Clave externa.
* **Contenido típico**: Un UUID asociado con una transacción de entrega específica.

#### delivery\_number

* **Significado**: Número único asignado a la entrega.
* **Función**: Campo de referencia.
* **Contenido típico**: Una cadena que representa el número de entrega.

#### line\_number

* **Significado**: Número de línea específico dentro de una entrega.
* **Función**: Campo de referencia.
* **Contenido típico**: Cadena numérica que indica la secuencia de la línea.

#### item\_id

* **Significado**: Identificador del artículo que se envía.
* **Función**: Campo de referencia.
* **Contenido típico**: Una cadena numérica correspondiente a un artículo.

#### description

* **Significado**: Descripción del artículo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Descripción textual del artículo, p. ej., "FLOUR, WHEAT, UN-BLEACHED ENRICHED, BULK".

#### shipped\_quantity

* **Significado**: Cantidad del artículo que se envió.
* **Función**: Campo cuantitativo.
* **Contenido típico**: Un número decimal que indica la cantidad enviada.

#### status

* **Significado**: Estado actual de la línea de artículo de la entrega.
* **Función**: Campo de estado.
* **Contenido típico**: Texto como "Received".

#### created\_by

* **Significado**: Identificador del usuario o del sistema que creó el registro.
* **Función**: Campo de auditoría.
* **Contenido típico**: Un entero que representa un ID de usuario.

#### created\_on

* **Significado**: Marca de tiempo de cuándo se creó el registro.
* **Función**: Campo de auditoría.
* **Contenido típico**: Fecha y hora con zona horaria.

#### last\_modified\_on

* **Significado**: Marca de tiempo de la última modificación.
* **Función**: Campo de auditoría.
* **Contenido típico**: Fecha y hora con zona horaria.

#### deleted\_on

* **Significado**: Marca de tiempo de cuándo se marcó el registro como eliminado.
* **Función**: Campo de auditoría.
* **Contenido típico**: Fecha y hora con zona horaria, a menudo nulo salvo que se haya eliminado.

#### is\_deleted

* **Significado**: Indica si el registro está marcado como eliminado.
* **Función**: Campo técnico.
* **Contenido típico**: Valor booleano, true o false.

#### purchase\_order

* **Significado**: Referencia al pedido de compra asociado.
* **Función**: Campo de referencia.
* **Contenido típico**: Cadena alfanumérica que representa un número de pedido de compra.

#### sequence\_number

* **Significado**: Número de secuencia de la línea de entrega.
* **Función**: Campo de referencia.
* **Contenido típico**: Cadena numérica, a menudo nula.

#### sub\_org\_id

* **Significado**: Identificador de una suborganización implicada.
* **Función**: Clave externa.
* **Contenido típico**: UUID, a menudo nulo.

#### shipped\_quantity\_unit\_code

* **Significado**: Unidad de medida de la cantidad enviada.
* **Función**: Campo de referencia.
* **Contenido típico**: Código que representa unidades, p. ej., "LBP".

#### packing\_slip\_quantity

* **Significado**: Cantidad según el albarán.
* **Función**: Campo cuantitativo.
* **Contenido típico**: Número decimal, a menudo nulo.

#### packing\_slip\_quantity\_unit\_code

* **Significado**: Código de unidad de la cantidad del albarán.
* **Función**: Campo de referencia.
* **Contenido típico**: Código que representa unidades, a menudo nulo.

#### received\_quantity

* **Significado**: Cantidad de artículos realmente recibida.
* **Función**: Campo cuantitativo.
* **Contenido típico**: Número decimal que indica la cantidad recibida.

#### received\_quantity\_unit\_code

* **Significado**: Código de unidad de la cantidad recibida.
* **Función**: Campo de referencia.
* **Contenido típico**: Código que representa unidades, p. ej., "LBP".

#### purchase\_order\_line\_number

* **Significado**: Número de línea dentro del pedido de compra.
* **Función**: Campo de referencia.
* **Contenido típico**: Cadena numérica.

#### status\_effective\_from

* **Significado**: La fecha y la hora a partir de las cuales el estado es efectivo.
* **Función**: Campo de estado.
* **Contenido típico**: Fecha y hora con zona horaria, a menudo nulo.

#### purchase\_order\_sub\_line\_number

* **Significado**: Número de sublínea dentro del pedido de compra.
* **Función**: Campo de referencia.
* **Contenido típico**: Cadena numérica, a menudo "000".

#### invoiced\_quantity

* **Significado**: Cantidad que se ha facturado.
* **Función**: Campo cuantitativo.
* **Contenido típico**: Número decimal.

#### invoice\_matching\_status

* **Significado**: Estado del proceso de conciliación de facturas.
* **Función**: Campo de estado.
* **Contenido típico**: Código de estado textual, p. ej., "9.0".

#### open\_quantity

* **Significado**: Cantidad que permanece abierta o aún no procesada.
* **Función**: Campo cuantitativo.
* **Contenido típico**: Número decimal.

#### last\_modified\_by

* **Significado**: Identificador del usuario que modificó el registro por última vez.
* **Función**: Campo de auditoría.
* **Contenido típico**: UUID del usuario, a menudo nulo.

#### deleted\_by

* **Significado**: Identificador del usuario que marcó el registro como eliminado.
* **Función**: Campo de auditoría.
* **Contenido típico**: UUID del usuario, a menudo nulo.
