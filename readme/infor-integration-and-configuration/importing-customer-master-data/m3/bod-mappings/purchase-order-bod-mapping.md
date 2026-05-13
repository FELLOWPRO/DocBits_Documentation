# Purchase Order BOD Mapping

Diese Seite dokumentiert, wie DocBits Infor M3 `SyncPurchaseOrder` BODs einliest und die Felder auf die internen Tabellen `PURCHASE_ORDER_HEADER` und Purchase Order Line abbildet.

{% file src="../../../../.gitbook/assets/Sync.PurchaseOrder.pdf" %}
Original BOD Mapping Referenz (PDF)
{% endfile %}

## Grundprinzipien

- **Keine Währungs-Konvertierung in DocBits.** Beträge werden genau so persistiert, wie M3 sie im BOD liefert, zusammen mit ihrer `@currencyID`. Drei Header-Beträge stehen zur Verfügung: `ExtendedAmount` (Transaktionswährung), `ExtendedBaseAmount` (Basiswährung des Mandanten), `ExtendedReportAmount` (Reportwährung).
- **Keine Maßeinheiten-Konvertierung in DocBits.** Mengen werden mit ihrer `@unitCode` gespeichert. `ReceivedBaseUOMQuantity` ist der von M3 vorberechnete Basis-UoM-Wert — DocBits speichert ihn unverändert.
- **Der Header-Status wird aus der SXE-Stage übernommen, sofern verfügbar.** DocBits liest `UserArea/Property[@name='poeh.stagecd']` (Werte `1..8` → Ordered / Entered / Released / Allocated / Picked / Delivered / Invoiced / Cancelled) und nutzt diesen Wert als maßgeblichen Header-Status. Das Standard-Feld `Status/Code` wird zusätzlich zur Referenz gespeichert.
- **Keine automatische Teilmengen-Status-Logik.** DocBits leitet keinen Status aus erhaltener vs. bestellter Menge ab; der von M3 gelieferte Status wird 1:1 übernommen.
- **`CONO`/`AccountingEntityID` ist nicht Bestandteil des PurchaseOrder-BODs.** Die Mandanten-Zuordnung über die Company-Number gilt für Stammdaten (siehe [Supplier BOD Mapping](supplier-bod-mapping.md)); Bestellungen werden über `LocationID` zugeordnet.

## Header-Mapping

→ DocBits Stammdaten-Tabelle: **PURCHASE\_ORDER\_HEADER**

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

### Header-Feldreferenz

| DocBits Feld | M3 Quelle | Beschreibung |
|---|---|---|
| `purchase_order_number` | `MPHEAD.IAPUNO` | M3-Bestellnummer, Primärschlüssel. |
| `warehouse_id` | — | Liest `ShipToParty/Location[@type='Warehouse']/ID`. Das Attribut `@type='Warehouse'` wird von M3 selten gesetzt; das Feld bleibt dann NULL. Nutzen Sie `location_id` für den M3-konformen Lagerort. |
| `location_id` | `MPHEAD.IAFACI` | M3-Division/-Werk (Lagerort), in dem der BOD erzeugt wurde. Wird zur Mandanten-/Werks-Zuordnung in DocBits verwendet, inkl. Matching mit Rechnungs-Werken. |
| `status` | `MPHEAD.IAPUSL` | Rohwert `Status/Code` aus dem BOD. Wird als Fallback verwendet, wenn `sxe_stage` leer ist. |
| `sxe_stage` | `MPHEAD.IAPUSL` | Der maßgebliche Header-Status, gelesen aus der UserArea-Property `poeh.stagecd`. Mappt M3 SXE-Stage-Codes 1..8 → Ordered, Entered, Released, Allocated, Picked, Delivered, Invoiced, Cancelled. Wenn gesetzt, überschreibt dieser Wert `status` für Workflow-Entscheidungen. Mit aktivierter Preference `UPDATE_DOCUMENT_PURCHASE_ORDER_STATUS` propagiert DocBits diesen Status auf verknüpfte Rechnungen. |
| `supplier_id` | `MPHEAD.IASUNO` | Lieferantennummer auf der Bestellung. |
| `supplier_name` | `CIDMAS.IDSUNM` | Anzeigename des Lieferanten. |
| `order_date` | `MPHEAD.IAPUDT` | Datum, an dem die Bestellung in M3 angelegt wurde. |
| `requested_shipment_date` | — | Lesen aus dem Header-`RequiredDeliveryDateTime`, falls vorhanden. Die meisten M3-Installationen führen dieses Feld nur auf Zeilenebene; in diesem Fall ist das zeilenbasierte `requested_ship_date` zu verwenden. |
| `total_amount` | `MPHEAD.IAOURR` | Bestellsumme in Transaktionswährung. 1:1 aus `ExtendedAmount` übernommen. |
| `extended_amount` | `MPHEAD.IAOURR` | Gleiche Quelle wie `total_amount`. Wird als separate Rohspalte erhalten — zur Nachvollziehbarkeit und für Downstream-Konsumenten, die den kanonischen BOD-Pfad erwarten. |
| `extended_base_amount` | `MPHEAD.IAOUVA` | Bestellsumme in der Basiswährung des Mandanten. Von M3 geliefert, sofern vorhanden. |
| `extended_report_amount` | `MPHEAD.IAOUVB` | Bestellsumme in der Reportwährung des Mandanten. |
| `canceled_amount` / `canceled_base_amount` / `canceled_reporting_amount` | — | Stornierte Beträge in Transaktions-/Basis-/Reportwährung. Wird von M3 nur nach Storno-Ereignissen befüllt. |
| `type_code` / `type_description` | — | Bestellart aus `Classification/Codes/Code[@listID='Purchase Order Types']` (und deren `Description`). Beispiele: `P10` Normale Bestellung, `P20` Lagerauffüllbestellung. Wird nur zur Anzeige gespeichert — keine Filterlogik. |
| `buyer_contact_id` / `buyer_contact_name` | `MPHEAD.IABUYE` / verknüpfter User | Der für die PO zuständige Käufer. |
| `order_last_modified_by` / `order_last_modified_on` | `MPHEAD.IACHID` / `MPHEAD.IALMDT` | Audit-Felder. |
| `disponent_id` / `disponent_name` | `MPHEAD.IARESP` / verknüpfter User | Disponenten-Referenz. |

## Zeilen-Mapping

→ DocBits Stammdaten-Tabelle: **Purchase Order**

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

### Zeilen-Feldreferenz

| DocBits Feld | M3 Quelle | Beschreibung |
|---|---|---|
| `item_id` | `MPLINE.IBITNO` | M3-Artikelnummer. Fallback auf `@schemeName='NonStock'` für Nicht-Lager-Artikel. |
| `supplier_item_id` | `MPLINE.IBSITE` / Classification | Artikelnummer aus Lieferantensicht. Wird in drei Fallback-Stufen aufgelöst: `ID[@schemeName='Supplier']` → `Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']` → `Item/SupplierItemID/ID`. |
| `description` | `MPLINE.IBPITT` | Artikelbeschreibung der Zeile. |
| `note` | `MSYTXL.TLTX60` | Anmerkung zur Zeile. |
| `quantity` | `MPLINE.IBORQA` | Bestellte Menge. Wird mit `unit_of_measure` gespeichert (keine Konvertierung). |
| `open_quantity` | `CFQA - RVQA` | Noch offene Menge (bestellt minus erhalten). Gleiche `unit_of_measure`. |
| `confirmed_quantity` | — | Vom Lieferanten bestätigte Menge. M3 lässt das Feld leer; wird von ERPs befüllt, die `BackOrderedQuantity` emittieren. |
| `received_quantity` | `MPLINE.IBRVQA` | Wareneingangsmenge. |
| `received_base_mou_quantity` | `MPLINE.IBRVQA` (Basis-UoM) | Wareneingangsmenge konvertiert in die Basis-Mengeneinheit — von M3 selbst berechnet. DocBits konvertiert nicht, sondern speichert den von M3 gelieferten Wert. Relevant für die Lagerbuchhaltung. |
| `unit_of_measure` | `MPLINE.IBPUUN` | Transaktions-UoM. Gilt für `quantity`, `open_quantity`, `received_quantity`. |
| `unit_price` | `MPLINE.IBPUPR` | Einzelpreis in Transaktionswährung. |
| `unit_price_per` / `unit_code_price` | `MPLINE.IBCPUC` / `MPLINE.IBPPUN` | Preis-pro-Menge und zugehöriger Code (Preis-Modifikator, z. B. Preis je 100 Stück). |
| `total_amount` | `LNAM + EXEP` | Zeilensumme. Wird per Fallback `[TotalAmount, ExtendedAmount]` aufgelöst — wenn `TotalAmount` fehlt, ist `total_amount` gleich `extended_amount`. Wenn beide vorhanden sind, kann `TotalAmount` Steuern/Rabatte enthalten, während `extended_amount` `quantity × unit_price` entspricht. |
| `extended_amount` | `LNAM` / `LNA2` | Roher `ExtendedAmount` (Zeilensubtotal ohne Steuern/Rabatte). |
| `currency` | `MPHEAD.IACUCD` | Transaktionswährung. Gelesen aus `TotalAmount/@currencyID`, mit `ExtendedAmount/@currencyID` als Fallback. |
| `status` | `MPLINE.IBPUST` | Zeilenstatus. Wird für Reporting gespeichert; keine DocBits-Workflow-Logik leitet daraus etwas ab. |
| `buyer_id` / `buyer_name` | `MPLINE.IBBUYE` / verknüpfter User | Käufer auf Zeilenebene. `buyer_name` wird von M3 auf der Zeile selten befüllt; die Lieferanten-Käufer-Referenz steht in [Supplier BOD Mapping](supplier-bod-mapping.md). |
| `geo_code` | — | Geo-Code für US/CA-Steuer-Engines. Wird nur von ERPs befüllt, die ihn emittieren. |
| `delivery_method` | `MPLINE.IBMODL` | Liefermethode der Zeile (M3 `MODL`-Code). |
| `promised_delivery_date` | `CODT, DWDT/TIHM` | Vom Lieferanten bestätigtes Lieferdatum. |
| `requested_ship_date` | `MPLINE.IBDWDT` | Gewünschter Liefertermin auf Zeilenebene — operativ relevantes Wunsch-Lieferdatum. |
| `sub_line_number` | — | Optionale Sub-Zeilen-Kennung. Wird gespeichert, falls vorhanden; M3 lässt sie typischerweise leer. |
| `schedule_line_number` | — | Optionale Schedule-Line-Referenz für Liefertermin-geplante Bestellungen. |
| `order_multiple` / `standard_quantity` | `MPLINE.IBOMUL` / UserArea | Bestellschrittweite (Mindestbestellmenge) und Standard-Verpackungsmenge der Zeile. |

## Häufige Fragen

### Wie behandelt DocBits Bestellungen in Fremdwährung?

DocBits konvertiert keine Währungen. Der Transaktionsbetrag (`total_amount`, `extended_amount`, `unit_price`) wird zusammen mit seiner `@currencyID` gespeichert. Wenn der Mandant eine andere Basis- oder Reportwährung verwendet, liefert M3 vorab konvertierte Werte über `extended_base_amount` und `extended_report_amount` — diese werden als zusätzliche Spalten im Header gespeichert.

### Wie leitet DocBits den Teilmengen-Status ab?

Gar nicht. Der Header-Status spiegelt die M3 SXE-Stage (`poeh.stagecd`) zum Zeitpunkt der BOD-Erzeugung wider. Wenn Sie einen Teilmengen-Indikator brauchen, leiten Sie ihn aus `open_quantity` vs. `quantity` auf der Zeilen-Tabelle ab.

### Wo ist der Unterschied zwischen `total_amount` und `extended_amount` auf der Zeile?

Beide Spalten existieren aus historischen/UI-Kompatibilitätsgründen. `total_amount` wird per Fallback `[TotalAmount, ExtendedAmount]` aufgelöst, ist also gleich `extended_amount`, wann immer `TotalAmount` fehlt. Wenn M3 beide emittiert, kann `TotalAmount` Steuern oder Rabatte oberhalb von `quantity × unit_price` enthalten — dieser Wert steht in `extended_amount`.

### Warum wird der Lagerort auf zwei verschiedene Pfade gemappt?

`warehouse_id` liest `ShipToParty/Location[@type='Warehouse']/ID`, was die meisten M3-Installationen leer lassen (das `@type`-Attribut wird selten gesetzt). `location_id` liest `DataArea/Sync/LocationID` und wird von M3 immer befüllt; es entspricht der Division/dem Werk, zu der/dem die Bestellung gehört. Behandeln Sie `location_id` als M3-nativen Lagerort-Identifier.

### Einige Felder sind dokumentiert, aber immer leer (`buyer_name`, `geo_code`, `confirmed_quantity`, `sub_line_number`, …). Warum sind sie gemappt?

Die Mappings sind defensiv: das BOD-Schema erlaubt diese Felder, und andere ERPs oder individuelle M3-Erweiterungen können sie befüllen. Wenn M3 sie leer lässt, sind die Spalten in DocBits einfach NULL.
