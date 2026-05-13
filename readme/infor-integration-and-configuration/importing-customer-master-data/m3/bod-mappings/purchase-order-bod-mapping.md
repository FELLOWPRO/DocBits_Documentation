# Purchase Order BOD Mapping

This page documents how DocBits ingests Infor M3 `SyncPurchaseOrder` BODs and maps fields onto the internal `PURCHASE_ORDER_HEADER` and Purchase Order Line tables.

{% file src="../../../../.gitbook/assets/Sync.PurchaseOrder.pdf" %}
Original BOD mapping reference (PDF)
{% endfile %}

## Key principles

- **No currency conversion in DocBits.** Amounts are persisted exactly as M3 delivers them in the BOD, together with their `@currencyID`. Three header amounts are available: `ExtendedAmount` (transaction currency), `ExtendedBaseAmount` (company base currency), `ExtendedReportAmount` (reporting currency).
- **No unit-of-measure conversion in DocBits.** Quantities are stored with their `@unitCode`. `ReceivedBaseUOMQuantity` is the base-UOM value pre-computed by M3 — DocBits stores it as-is.
- **Header status is taken from the SXE stage when available.** DocBits reads `UserArea/Property[@name='poeh.stagecd']` (values `1..8` → Ordered / Entered / Released / Allocated / Picked / Delivered / Invoiced / Cancelled) and uses it as the authoritative header status. The standard `Status/Code` is also stored for reference.
- **No automatic partial-quantity status logic.** DocBits does not derive a status from received vs. ordered quantities; the status delivered by M3 is taken 1:1.
- **`CONO`/`AccountingEntityID` is not part of the PurchaseOrder BOD.** Company-number routing applies to supplier master data (see [Supplier BOD Mapping](supplier-bod-mapping.md)); purchase orders are scoped via `LocationID`.

## Header mapping

→ DocBits Master Data Lookup Table: **PURCHASE\_ORDER\_HEADER**

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

### Header field reference

| DocBits field | M3 source | Description |
|---|---|---|
| `purchase_order_number` | `MPHEAD.IAPUNO` | M3 purchase order number, primary key. |
| `warehouse_id` | — | Reads `ShipToParty/Location[@type='Warehouse']/ID`. The `@type='Warehouse'` attribute is rarely set by M3; the field stays NULL in that case. Use `location_id` for the M3-native warehouse. |
| `location_id` | `MPHEAD.IAFACI` | M3 division/facility (warehouse) where the BOD originated. Used for org/plant routing inside DocBits, including matching with invoice plants. |
| `status` | `MPHEAD.IAPUSL` | Raw `Status/Code` from the BOD. Used as a fallback when `sxe_stage` is empty. |
| `sxe_stage` | `MPHEAD.IAPUSL` | The authoritative header status, taken from `poeh.stagecd` user-area property. Maps M3 SXE stage codes 1..8 → Ordered, Entered, Released, Allocated, Picked, Delivered, Invoiced, Cancelled. When set, this overrides `status` for workflow decisions. With the preference `UPDATE_DOCUMENT_PURCHASE_ORDER_STATUS` enabled, DocBits propagates this status onto linked invoices. |
| `supplier_id` | `MPHEAD.IASUNO` | Supplier number on the purchase order. |
| `supplier_name` | `CIDMAS.IDSUNM` | Supplier display name. |
| `order_date` | `MPHEAD.IAPUDT` | Date the purchase order was created in M3. |
| `requested_shipment_date` | — | Read from header-level `RequiredDeliveryDateTime` if present. Most M3 setups carry this only on the line; in that case use the line-level `requested_ship_date`. |
| `total_amount` | `MPHEAD.IAOURR` | Order total in transaction currency. Stored 1:1 from `ExtendedAmount`. |
| `extended_amount` | `MPHEAD.IAOURR` | Same source as `total_amount`. Kept as a separate raw column for traceability and downstream consumers that expect the canonical BOD path. |
| `extended_base_amount` | `MPHEAD.IAOUVA` | Order total expressed in the company base currency. Filled by M3 when available. |
| `extended_report_amount` | `MPHEAD.IAOUVB` | Order total expressed in the company reporting currency. |
| `canceled_amount` / `canceled_base_amount` / `canceled_reporting_amount` | — | Cancellation amounts in transaction / base / reporting currency. Populated by M3 only after cancellation events. |
| `type_code` / `type_description` | — | Purchase order type from `Classification/Codes/Code[@listID='Purchase Order Types']` (and its `Description`). Examples: `P10` Normal PO, `P20` Stock-replenishment PO. Stored for display only — no filtering logic. |
| `buyer_contact_id` / `buyer_contact_name` | `MPHEAD.IABUYE` / linked user | Buyer assigned to the PO. |
| `order_last_modified_by` / `order_last_modified_on` | `MPHEAD.IACHID` / `MPHEAD.IALMDT` | Audit fields. |
| `disponent_id` / `disponent_name` | `MPHEAD.IARESP` / linked user | Planner reference. |

## Line mapping

→ DocBits Master Data Lookup Table: **Purchase Order**

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

### Line field reference

| DocBits field | M3 source | Description |
|---|---|---|
| `item_id` | `MPLINE.IBITNO` | M3 item number. Falls back to `@schemeName='NonStock'` for non-stock items. |
| `supplier_item_id` | `MPLINE.IBSITE` / Classification | Supplier-side item number. Resolved through three fallbacks (in order): `ID[@schemeName='Supplier']` → `Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']` → `Item/SupplierItemID/ID`. |
| `description` | `MPLINE.IBPITT` | Line item description. |
| `note` | `MSYTXL.TLTX60` | Line note text. |
| `quantity` | `MPLINE.IBORQA` | Ordered quantity. Stored with `unit_of_measure` (no conversion). |
| `open_quantity` | `CFQA - RVQA` | Quantity still open (ordered minus received). Same `unit_of_measure`. |
| `confirmed_quantity` | — | Supplier-confirmed quantity. M3 leaves this empty; populated by ERPs that emit `BackOrderedQuantity`. |
| `received_quantity` | `MPLINE.IBRVQA` | Goods received quantity. |
| `received_base_mou_quantity` | `MPLINE.IBRVQA` (base UoM) | Received quantity converted to the base unit of measure by M3 itself. DocBits does not compute this — it stores what M3 sends. Useful for inventory accounting. |
| `unit_of_measure` | `MPLINE.IBPUUN` | Transaction UoM. Applies to `quantity`, `open_quantity`, `received_quantity`. |
| `unit_price` | `MPLINE.IBPUPR` | Unit price in transaction currency. |
| `unit_price_per` / `unit_code_price` | `MPLINE.IBCPUC` / `MPLINE.IBPPUN` | Price-per quantity and its unit code (price modifier, e.g. price per 100 PCS). |
| `total_amount` | `LNAM + EXEP` | Line total. Resolved through fallback `[TotalAmount, ExtendedAmount]` — when `TotalAmount` is missing, `total_amount` equals `extended_amount`. When both are present, `TotalAmount` may include taxes/discounts while `extended_amount` is `quantity × unit_price`. |
| `extended_amount` | `LNAM` / `LNA2` | Raw `ExtendedAmount` (line subtotal without tax/discount). |
| `currency` | `MPHEAD.IACUCD` | Transaction currency. Read from `TotalAmount/@currencyID` with `ExtendedAmount/@currencyID` as fallback. |
| `status` | `MPLINE.IBPUST` | Line status. Stored for reporting; no DocBits workflow logic derives from it. |
| `buyer_id` / `buyer_name` | `MPLINE.IBBUYE` / linked user | Line-level buyer. `buyer_name` is rarely populated by M3 on the line; the supplier-level buyer reference is in [Supplier BOD Mapping](supplier-bod-mapping.md). |
| `geo_code` | — | US/CA tax-engine geo code. Populated only by ERPs that emit it. |
| `delivery_method` | `MPLINE.IBMODL` | Line delivery method (M3 `MODL` code). |
| `promised_delivery_date` | `CODT, DWDT/TIHM` | Supplier-confirmed delivery date. |
| `requested_ship_date` | `MPLINE.IBDWDT` | Requested ship date on the line — this is the operationally relevant requested delivery date. |
| `sub_line_number` | — | Optional sub-line identifier. Stored if present; M3 typically leaves it empty. |
| `schedule_line_number` | — | Optional schedule-line reference for scheduled-delivery POs. |
| `order_multiple` / `standard_quantity` | `MPLINE.IBOMUL` / UserArea | Line ordering quantum (minimum order multiple) and standard packaging quantity. |

## Common questions

### How does DocBits handle foreign-currency purchase orders?

DocBits does not convert currencies. The transaction amount (`total_amount`, `extended_amount`, `unit_price`) is stored together with its `@currencyID`. When the company uses a different base or reporting currency, M3 supplies pre-converted values via `extended_base_amount` and `extended_report_amount` — those are stored as additional columns on the header.

### How does DocBits derive the partial-receipt status?

It does not. The header status reflects the M3 SXE stage (`poeh.stagecd`) at the time the BOD was emitted. If you need a partial-receipt indicator, derive it from `open_quantity` vs. `quantity` on the line table.

### What is the difference between `total_amount` and `extended_amount` on the line?

Both columns exist for historical/UI compatibility. `total_amount` resolves through `[TotalAmount, ExtendedAmount]`, so it equals `extended_amount` whenever `TotalAmount` is absent. When M3 emits both, `TotalAmount` may include taxes or discounts on top of the `quantity × unit_price` value held in `extended_amount`.

### Why does the warehouse map to two different paths?

`warehouse_id` reads `ShipToParty/Location[@type='Warehouse']/ID`, which most M3 installations leave empty (the `@type` attribute is rarely set). `location_id` reads `DataArea/Sync/LocationID`, which is always populated by M3 and corresponds to the division/facility the PO belongs to. Treat `location_id` as the M3-native warehouse identifier.

### Some fields are documented but always empty (`buyer_name`, `geo_code`, `confirmed_quantity`, `sub_line_number`, …). Why are they mapped?

These mappings are defensive: the BOD schema allows the fields, and other ERPs or custom M3 extensions can populate them. When M3 leaves them empty, the columns are simply NULL in DocBits.
