# Pedido de venta

## Tabla `public.sales_order`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `sub_org_id`: interno
* `location_id`: interno
* `order_number`: interno
* `customer_purchase_order`: interno
* `customer_id`: interno
* `customer_name`: interno
* `warehouse_id`: interno
* `warehouse_name`: interno
* `transportation_method`: interno
* `requested_delivery_date`: marca de tiempo con zona horaria
* `order_date`: marca de tiempo con zona horaria
* `sales_person_id`: interno
* `sales_person_name`: interno
* `ship_to_party_id`: interno
* `ship_to_party_name`: interno
* `ship_to_party_city`: interno
* `ship_to_party_state`: interno
* `ship_to_party_country`: interno
* `ship_to_party_zip`: interno
* `status`: interno
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean
* `deleted_on`: marca de tiempo con zona horaria
* `preview_path`: interno
* `last_modified_by`: interno
* `deleted_by`: interno

### Análisis y descripción

## Documentación técnica de la tabla `public.sales_order`

### Introducción

La tabla `public.sales_order` está diseñada para registrar y almacenar información relacionada con los pedidos de venta en un contexto empresarial. Incluye detalles del pedido, del cliente, de la logística y diversos metadatos asociados al ciclo de vida del pedido. La tabla sirve como repositorio central para el seguimiento del estado y del historial de las transacciones de venta.

### Descripción de las columnas

#### id

* **Significado**: Identificador único de cada pedido de venta.
* **Función**: Clave primaria.
* **Contenido típico**: Una cadena UUID (p. ej., `'6ffe4673-7563-44dc-8e71-855e8f25534a'`).

#### org\_id

* **Significado**: Identificador de la organización que creó el pedido de venta.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID que representa la organización (p. ej., `'23f3d697-7411-4c95-981d-faf089d266be'`).

#### sub\_org\_id

* **Significado**: Identificador de una suborganización, si procede.
* **Función**: Clave externa.
* **Contenido típico**: Puede ser `NULL` si no procede.

#### location\_id

* **Significado**: Identificador de la ubicación asociada al pedido de venta.
* **Función**: Clave externa.
* **Contenido típico**: Un código de cadena que representa una ubicación (p. ej., `'028'`).

#### order\_number

* **Significado**: Número único asignado al pedido de venta.
* **Función**: Campo técnico para el seguimiento del pedido.
* **Contenido típico**: Una cadena (p. ej., `'0010174175'`).

#### customer\_purchase\_order

* **Significado**: Número de referencia del pedido de compra del cliente.
* **Función**: Campo técnico para referencias cruzadas.
* **Contenido típico**: Una cadena (p. ej., `'1YFNC3'`).

#### customer\_id

* **Significado**: Identificador del cliente que realiza el pedido.
* **Función**: Clave externa.
* **Contenido típico**: Un código de cadena (p. ej., `'35623000'`).

#### customer\_name

* **Significado**: Nombre del cliente.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena (p. ej., `'DOLLAR GENERAL'`).

#### warehouse\_id

* **Significado**: Identificador del almacén responsable de preparar el pedido.
* **Función**: Clave externa.
* **Contenido típico**: Un código de cadena (p. ej., `'028'`).

#### warehouse\_name

* **Significado**: Nombre del almacén.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena (p. ej., `'USCS - DENTON, TX'`).

#### transportation\_method

* **Significado**: Método de transporte para entregar el pedido.
* **Función**: Campo descriptivo.
* **Contenido típico**: Un código de cadena (p. ej., `'001'`).

#### requested\_delivery\_date

* **Significado**: Fecha de entrega solicitada por el cliente.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una marca de tiempo (p. ej., `None`).

#### order\_date

* **Significado**: Fecha en la que se realizó el pedido.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una marca de tiempo (p. ej., `datetime.datetime(2024, 1, 29, 0, 0, tzinfo=datetime.timezone.utc)`).

#### sales\_person\_id

* **Significado**: Identificador del vendedor que gestiona el pedido.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena (p. ej., `'ROBERTDOCK'`).

#### sales\_person\_name

* **Significado**: Nombre del vendedor.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena (p. ej., `'ROBERT DOCKINS'`).

#### ship\_to\_party\_id

* **Significado**: Identificador de la parte a la que se envía el pedido.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena (p. ej., `'35623000 009'`).

#### ship\_to\_party\_name

* **Significado**: Nombre de la parte a la que se envía el pedido.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena (p. ej., `'DOLLAR GENERAL DC 98061/96460'`).

#### ship\_to\_party\_city

* **Significado**: Ciudad de la dirección de envío.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena (p. ej., `'SAN ANTONIO'`).

#### ship\_to\_party\_state

* **Significado**: Estado de la dirección de envío.
* **Función**: Campo descriptivo.
* **Contenido típico**: Puede ser `NULL`.

#### ship\_to\_party\_country

* **Significado**: País de la dirección de envío.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena (p. ej., `'US'`).

#### ship\_to\_party\_zip

* **Significado**: Código postal de la dirección de envío.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena (p. ej., `'78218'`).

#### status

* **Significado**: Estado actual del pedido de venta.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena (p. ej., `'Allocated'`).

#### created\_by

* **Significado**: Identificador del usuario que creó la entrada.
* **Función**: Campo técnico.
* **Contenido típico**: Un entero (p. ej., `1`).

#### created\_on

* **Significado**: Marca de tiempo de cuándo se creó la entrada.
* **Función**: Campo técnico.
* **Contenido típico**: Una marca de tiempo (p. ej., `datetime.datetime(2024, 3, 6, 11, 48, 43, 237208, tzinfo=datetime.timezone.utc)`).

#### last\_modified\_on

* **Significado**: Marca de tiempo de la última modificación.
* **Función**: Campo técnico.
* **Contenido típico**: Una marca de tiempo (p. ej., `datetime.datetime(2024, 9, 4, 8, 42, 32, 912247, tzinfo=datetime.timezone.utc)`).

#### is\_deleted

* **Significado**: Indicador que señala si el pedido está marcado como eliminado.
* **Función**: Campo técnico.
* **Contenido típico**: Un booleano (p. ej., `False`).

#### deleted\_on

* **Significado**: Marca de tiempo de cuándo se marcó el pedido como eliminado.
* **Función**: Campo técnico.
* **Contenido típico**: Fecha por defecto si no se ha eliminado (p. ej., `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`).

#### preview\_path

* **Significado**: Ruta a un documento de vista previa del pedido de venta.
* **Función**: Campo descriptivo.
* **Contenido típico**: Una cadena que representa una ruta de archivo (p. ej., `'previews/sales_order/23f3d697-7411-4c95-981d-faf089d266be/0010174175/0010174175_preview.pdf'`).

#### last\_modified\_by

* **Significado**: Identificador del usuario que modificó la entrada por última vez.
* **Función**: Campo técnico.
* **Contenido típico**: Puede ser `NULL`.

#### deleted\_by

* **Significado**: Identificador del usuario que marcó la entrada como eliminada.
* **Función**: Campo técnico.
* **Contenido típico**: Puede ser `NULL`.
