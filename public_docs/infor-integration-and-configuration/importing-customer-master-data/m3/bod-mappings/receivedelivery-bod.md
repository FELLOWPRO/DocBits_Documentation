# Mapeo BOD de ReceiveDelivery

```python
purchase_order_exists = True
when "//DataArea//PurchaseOrderReference/DocumentID/ID" exists
```

```python
delivery_number =
"//DataArea/ReceiveDelivery/ReceiveDeliveryHeader/DisplayID"
OR
"//DataArea/ReceiveDelivery/ReceiveDeliveryHeader/DocumentID/ID"
```

<mark style="color:red;">Nota</mark>: Si el `DisplayID` no está disponible, se utilizará el XPath alternativo `DocumentID/ID`.

```python
ship_from_party_id = "//DataArea/ReceiveDelivery/ReceiveDeliveryHeader/ShipFromParty/PartyIDs/ID"
ship_from_party_name= "//DataArea/ReceiveDelivery/ReceiveDeliveryHeader/ShipFromParty/Name"
warehouse_id = "//DataArea/ReceiveDelivery/ReceiveDeliveryHeader/WarehouseLocation/ID"
location_id = "//DataArea/Sync/LocationID"
packing_slip_number = "//DataArea/Sync/LocationID""//DataArea/ReceiveDelivery/ReceiveDeliveryHeader/PackingSlip"
actual_delivery_date_time = "//DataArea/ReceiveDelivery/ReceiveDeliveryHeader/ActualDeliveryDateTime"
status = "//DataArea/ReceiveDelivery/ReceiveDeliveryHeader/Status/Code"
status_effective_from = "//DataArea/ReceiveDelivery/ReceiveDeliveryHeader/Status/EffectiveDateTime"
```

## **Artículos de línea**

```python
line_number = "//ReceiveDeliveryItem[{index}]/LineNumber"
sequence_number = "//ReceiveDeliveryItem[{index}]/CountSequence"
item_id = "//ReceiveDeliveryItem[{index}]/ItemID/ID[not(@schemeName)]"
description = "//ReceiveDeliveryItem[{index}]/Description"
purchase_order = "//ReceiveDeliveryItem[{index}]/PurchaseOrderReference/DocumentID/ID"
shipped_quantity = "//ReceiveDeliveryItem[{index}]/ShippedQuantity"
shipped_quantity_unit_code = "//ReceiveDeliveryItem[{index}]/ShippedQuantity/@unitCode"
packing_slip_quantity = "//ReceiveDeliveryItem[{index}]/PackingSlipQuantity"
packing_slip_quantity_unit_code = "//ReceiveDeliveryItem[{index}]/PackingSlipQuantity/@unitCode"
received_quantity = "//ReceiveDeliveryItem[{index}]/ReceivedQuantity"
received_quantity_unit_code = "//ReceiveDeliveryItem[{index}]/ReceivedQuantity/@unitCode"
purchase_order_line_number = "//ReceiveDeliveryItem[{index}]/PurchaseOrderReference/LineNumber"
status = "//ReceiveDeliveryItem[{index}]/Status/Code"
status_effective_from = "//ReceiveDeliveryItem[{index}]/Status/EffectiveDateTime"
```

```python
invoiced_quantity = "//ns:ReceiveDeliveryItem[{index}]/ns:UserArea/ns:Property/ns:NameValue[@name='InvoicedQuantity']"
```

<mark style="color:red;">**Nota**</mark>: La cantidad facturada solo se utilizará si el nodo existe en UserArea con el nombre InvoicedQuantity.

```python
purchase_order_sub_line_number =
"//ns:ReceiveDeliveryItem[{index}]//ns:DataArea/ns:ReceiveDelivery/ns:ReceiveDeliveryHeader/ns:UserArea/ns:Property/ns:NameValue[@name='PO LineSubNumber']"
OR
"//ns:ReceiveDeliveryItem[{index}]/ns:PurchaseOrderReference/ns:SubLineNumber"
OR
"//ns:ReceiveDeliveryItem[{index}]/ns:PurchaseOrderReference/ns:ScheduleLineNumber"
```

<mark style="color:red;">**Nota**</mark>: Si el XPath no está disponible, se utilizará el XPath alternativo.
