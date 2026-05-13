# Mapeo BOD de Purchase Order

Esta página documenta cómo DocBits ingiere los BODs `SyncPurchaseOrder` de Infor M3 y mapea los campos en las tablas internas `PURCHASE_ORDER_HEADER` y Purchase Order Line.

{% file src="../../../../.gitbook/assets/Sync.PurchaseOrder.pdf" %}
Referencia original del mapeo BOD (PDF)
{% endfile %}

## Principios clave

- **Sin conversión de moneda en DocBits.** Los importes se persisten exactamente como M3 los entrega en el BOD, junto con su `@currencyID`. Hay tres importes disponibles en la cabecera: `ExtendedAmount` (moneda de la transacción), `ExtendedBaseAmount` (moneda base de la empresa), `ExtendedReportAmount` (moneda de reporte).
- **Sin conversión de unidad de medida en DocBits.** Las cantidades se almacenan con su `@unitCode`. `ReceivedBaseUOMQuantity` es el valor de UoM base pre-calculado por M3 — DocBits lo almacena tal cual.
- **El estado de la cabecera proviene de la etapa SXE cuando está disponible.** DocBits lee `UserArea/Property[@name='poeh.stagecd']` (valores `1..8` → Ordered / Entered / Released / Allocated / Picked / Delivered / Invoiced / Cancelled) y lo utiliza como estado de cabecera autoritativo. El `Status/Code` estándar también se almacena para referencia.
- **Sin lógica automática de estado por cantidad parcial.** DocBits no deriva un estado a partir de las cantidades recibidas vs. ordenadas; el estado entregado por M3 se toma 1:1.
- **`CONO`/`AccountingEntityID` no forma parte del BOD de PurchaseOrder.** El enrutamiento por número de empresa aplica a los datos maestros de proveedores (ver [Supplier BOD Mapping](supplier-bod-mapping.md)); las órdenes de compra se asignan vía `LocationID`.

## Mapeo de Encabezado

→ Tabla de datos maestros de DocBits: **PURCHASE\_ORDER\_HEADER**

```python
header_mappings = {
            "purchase_order_number": "//DataArea/PurchaseOrder/PurchaseOrderHeader/DocumentID/ID",
            "warehouse_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ShipToParty/Location[@type='Warehouse']/ID",
            "location_id": "//DataArea/Sync/LocationID",
            "status": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Status/Code",
            "supplier_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/SupplierParty/PartyIDs/ID",
            "supplier_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/SupplierParty/Name",
            "order_date": "//DataArea/PurchaseOrder/PurchaseOrderHeader/OrderDateTime",
            "requested_shipment_date": "//DataArea/PurchaseOrder/PurchaseOrderHeader/RequiredDeliveryDateTime",
            "total_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedAmount",
            "buyer_contact_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CustomerParty/BuyerContact/ID",
            "buyer_contact_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CustomerParty/BuyerContact/Name",
            "order_last_modified_by": "//DataArea/PurchaseOrder/PurchaseOrderHeader/LastModificationPerson/IDs/ID",
            "order_last_modified_on": "//DataArea/PurchaseOrder/PurchaseOrderHeader/LastModificationDateTime",
            "disponent_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/PlannerReference/IDs/ID",
            "disponent_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/PlannerReference/Name",
            "extended_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedAmount",
            "extended_base_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedBaseAmount",
            "extended_report_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedReportAmount",
            "canceled_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledAmount",
            "canceled_base_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledBaseAmount",
            "canceled_reporting_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledReportingAmount",
            "type_code": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Classification/Codes/Code[@listID='Purchase Order Types']",
            "type_description": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Classification[Codes/Code[@listID='Purchase Order Types']]/Description",
            "sxe_stage": "//DataArea/PurchaseOrder/PurchaseOrderHeader/UserArea/Property/NameValue[@name='poeh.stagecd']/text()",
        }
```

### Referencia de campos de cabecera

| Campo de DocBits | Origen en M3 | Descripción |
|---|---|---|
| `purchase_order_number` | `MPHEAD.IAPUNO` | Número de orden de compra de M3, clave primaria. |
| `warehouse_id` | — | Lee `ShipToParty/Location[@type='Warehouse']/ID`. El atributo `@type='Warehouse'` rara vez es establecido por M3; el campo queda NULL en ese caso. Use `location_id` como almacén nativo de M3. |
| `location_id` | `MPHEAD.IAFACI` | División/instalación (almacén) de M3 donde se originó el BOD. Se usa para enrutamiento organización/planta dentro de DocBits, incluido el emparejamiento con plantas de facturación. |
| `status` | `MPHEAD.IAPUSL` | `Status/Code` bruto del BOD. Se usa como respaldo cuando `sxe_stage` está vacío. |
| `sxe_stage` | `MPHEAD.IAPUSL` | Estado de cabecera autoritativo, tomado de la propiedad UserArea `poeh.stagecd`. Mapea los códigos M3 SXE 1..8 → Ordered, Entered, Released, Allocated, Picked, Delivered, Invoiced, Cancelled. Cuando está definido, prevalece sobre `status` en decisiones de flujo. Con la preferencia `UPDATE_DOCUMENT_PURCHASE_ORDER_STATUS` activada, DocBits propaga este estado a las facturas vinculadas. |
| `supplier_id` | `MPHEAD.IASUNO` | Número de proveedor en la orden de compra. |
| `supplier_name` | `CIDMAS.IDSUNM` | Nombre de visualización del proveedor. |
| `order_date` | `MPHEAD.IAPUDT` | Fecha de creación de la orden de compra en M3. |
| `requested_shipment_date` | — | Se lee de `RequiredDeliveryDateTime` a nivel cabecera si existe. La mayoría de M3 sólo lo lleva en la línea; en ese caso use el `requested_ship_date` de línea. |
| `total_amount` | `MPHEAD.IAOURR` | Total de la orden en moneda de transacción. Se almacena 1:1 desde `ExtendedAmount`. |
| `extended_amount` | `MPHEAD.IAOURR` | Mismo origen que `total_amount`. Se mantiene como columna en bruto para trazabilidad y consumidores que esperan la ruta BOD canónica. |
| `extended_base_amount` | `MPHEAD.IAOUVA` | Total expresado en la moneda base de la empresa. Lo entrega M3 cuando está disponible. |
| `extended_report_amount` | `MPHEAD.IAOUVB` | Total expresado en la moneda de reporte. |
| `canceled_amount` / `canceled_base_amount` / `canceled_reporting_amount` | — | Importes de cancelación en moneda de transacción / base / reporte. Sólo se llenan tras eventos de cancelación. |
| `type_code` / `type_description` | — | Tipo de orden de compra desde `Classification/Codes/Code[@listID='Purchase Order Types']` (y su `Description`). Ejemplos: `P10` PO normal, `P20` PO de reposición. Sólo se almacena para visualización — sin lógica de filtrado. |
| `buyer_contact_id` / `buyer_contact_name` | `MPHEAD.IABUYE` / usuario vinculado | Comprador asignado a la PO. |
| `order_last_modified_by` / `order_last_modified_on` | `MPHEAD.IACHID` / `MPHEAD.IALMDT` | Campos de auditoría. |
| `disponent_id` / `disponent_name` | `MPHEAD.IARESP` / usuario vinculado | Referencia del planificador. |

## Mapeo de Líneas

→ Tabla de datos maestros de DocBits: **Purchase Order**

```python
line_mappings = {
        "sub_line_number": "SubLineNumber",
        "item_id": [
            "Item/ItemID/ID[not(@schemeName)]",
            "Item/ItemID/ID[@schemeName='NonStock']",
        ],
        "supplier_item_id": [
            "Item/ItemID/ID[@schemeName='Supplier']",
            "Item/Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']",
            "Item/SupplierItemID/ID",
        ],
        "schedule_line_number ": "DocumentReference/ScheduleLineNumber",
        "description": "Item/Description",
        "note": "Note",
        "quantity": "Quantity",
        "open_quantity": "OpenQuantity",
        "confirmed_quantity": "BackOrderedQuantity",
        "received_quantity": "ReceivedQuantity",
        "received_base_mou_quantity": "ReceivedBaseUOMQuantity",
        "unit_of_measure": "Quantity/@unitCode",
        "unit_price": "UnitPrice/Amount",
        "unit_price_per": "UnitPrice/PerQuantity",
        "unit_code_price": "UnitPrice/PerQuantity/@unitCode",
        "total_amount": ["TotalAmount", "ExtendedAmount"],
        "extended_amount": "ExtendedAmount",
        "currency": ["TotalAmount/@currencyID", "ExtendedAmount/@currencyID"],
        "buyer_id": "BuyerParty/PartyIDs/ID",
        "buyer_name": "BuyerParty/Name",
        "status": "Status/Code",
        "geo_code": "UserArea/Property/NameValue[@name='GeoCode']",
        "delivery_method": "UserArea/Property/NameValue[@name='m3.DeliveryMethod']",
        "order_multiple": "Classification/Codes/Code[@listID='Order multiple']",
        "standard_quantity": "UserArea/Property/NameValue[@name='StandardQuantity']",
        "promised_delivery_date": "PromisedDeliveryDateTime",
        "requested_ship_date": "RequiredDeliveryDateTime",
    }
```

### Referencia de campos de línea

| Campo de DocBits | Origen en M3 | Descripción |
|---|---|---|
| `item_id` | `MPLINE.IBITNO` | Número de artículo de M3. Recurre a `@schemeName='NonStock'` para artículos no inventariados. |
| `supplier_item_id` | `MPLINE.IBSITE` / Classification | Número de artículo del proveedor. Se resuelve mediante tres reintentos (en orden): `ID[@schemeName='Supplier']` → `Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']` → `Item/SupplierItemID/ID`. |
| `description` | `MPLINE.IBPITT` | Descripción del artículo de línea. |
| `note` | `MSYTXL.TLTX60` | Texto de nota de la línea. |
| `quantity` | `MPLINE.IBORQA` | Cantidad ordenada. Se almacena con `unit_of_measure` (sin conversión). |
| `open_quantity` | `CFQA - RVQA` | Cantidad aún pendiente (ordenada menos recibida). Misma `unit_of_measure`. |
| `confirmed_quantity` | — | Cantidad confirmada por el proveedor. M3 lo deja vacío; lo llenan ERPs que emiten `BackOrderedQuantity`. |
| `received_quantity` | `MPLINE.IBRVQA` | Cantidad recibida. |
| `received_base_mou_quantity` | `MPLINE.IBRVQA` (UoM base) | Cantidad recibida convertida a la unidad de medida base por el propio M3. DocBits no calcula esto — almacena lo que M3 envía. Útil para contabilidad de inventario. |
| `unit_of_measure` | `MPLINE.IBPUUN` | UoM de transacción. Aplica a `quantity`, `open_quantity`, `received_quantity`. |
| `unit_price` | `MPLINE.IBPUPR` | Precio unitario en moneda de transacción. |
| `unit_price_per` / `unit_code_price` | `MPLINE.IBCPUC` / `MPLINE.IBPPUN` | Precio-por cantidad y su código de unidad (modificador de precio, p. ej. precio por 100 PCS). |
| `total_amount` | `LNAM + EXEP` | Total de línea. Se resuelve mediante el respaldo `[TotalAmount, ExtendedAmount]` — cuando `TotalAmount` falta, `total_amount` es igual a `extended_amount`. Cuando ambos están presentes, `TotalAmount` puede incluir impuestos/descuentos mientras que `extended_amount` es `quantity × unit_price`. |
| `extended_amount` | `LNAM` / `LNA2` | `ExtendedAmount` bruto (subtotal de línea sin impuestos/descuentos). |
| `currency` | `MPHEAD.IACUCD` | Moneda de transacción. Se lee de `TotalAmount/@currencyID`, con `ExtendedAmount/@currencyID` como respaldo. |
| `status` | `MPLINE.IBPUST` | Estado de línea. Se almacena para reporting; ninguna lógica de flujo de DocBits deriva de él. |
| `buyer_id` / `buyer_name` | `MPLINE.IBBUYE` / usuario vinculado | Comprador a nivel línea. `buyer_name` rara vez es llenado por M3 en la línea; la referencia del comprador del proveedor está en [Supplier BOD Mapping](supplier-bod-mapping.md). |
| `geo_code` | — | Código geográfico para motores fiscales US/CA. Sólo lo llenan ERPs que lo emiten. |
| `delivery_method` | `MPLINE.IBMODL` | Método de entrega de la línea (código `MODL` de M3). |
| `promised_delivery_date` | `CODT, DWDT/TIHM` | Fecha de entrega confirmada por el proveedor. |
| `requested_ship_date` | `MPLINE.IBDWDT` | Fecha de envío solicitada en la línea — fecha de entrega solicitada operativamente relevante. |
| `sub_line_number` | — | Identificador opcional de sub-línea. Se almacena si está presente; M3 normalmente lo deja vacío. |
| `schedule_line_number` | — | Referencia opcional a línea de planificación para POs con entregas programadas. |
| `order_multiple` / `standard_quantity` | `MPLINE.IBOMUL` / UserArea | Múltiplo de pedido de línea (cantidad mínima) y cantidad estándar de empaquetado. |

## Preguntas frecuentes

### ¿Cómo gestiona DocBits las órdenes de compra en moneda extranjera?

DocBits no convierte monedas. El importe de transacción (`total_amount`, `extended_amount`, `unit_price`) se almacena junto con su `@currencyID`. Cuando la empresa usa una moneda base o de reporte distinta, M3 entrega valores pre-convertidos vía `extended_base_amount` y `extended_report_amount` — se almacenan como columnas adicionales en la cabecera.

### ¿Cómo deriva DocBits el estado de recepción parcial?

No lo hace. El estado de cabecera refleja la etapa SXE de M3 (`poeh.stagecd`) en el momento de la emisión del BOD. Si necesita un indicador de recepción parcial, derívelo de `open_quantity` vs. `quantity` en la tabla de líneas.

### ¿Cuál es la diferencia entre `total_amount` y `extended_amount` en la línea?

Ambas columnas existen por compatibilidad histórica/UI. `total_amount` se resuelve mediante `[TotalAmount, ExtendedAmount]`, por lo que es igual a `extended_amount` siempre que `TotalAmount` esté ausente. Cuando M3 emite ambos, `TotalAmount` puede incluir impuestos o descuentos por encima del valor `quantity × unit_price` guardado en `extended_amount`.

### ¿Por qué el almacén mapea a dos rutas diferentes?

`warehouse_id` lee `ShipToParty/Location[@type='Warehouse']/ID`, que la mayoría de las instalaciones M3 dejan vacío (el atributo `@type` rara vez se establece). `location_id` lee `DataArea/Sync/LocationID`, siempre llenado por M3 y correspondiente a la división/instalación a la que pertenece la PO. Trate `location_id` como el identificador de almacén nativo de M3.

### Algunos campos están documentados pero siempre vacíos (`buyer_name`, `geo_code`, `confirmed_quantity`, `sub_line_number`, …). ¿Por qué están mapeados?

Estos mapeos son defensivos: el esquema BOD permite los campos y otros ERPs o extensiones M3 personalizadas pueden llenarlos. Cuando M3 los deja vacíos, las columnas son simplemente NULL en DocBits.
