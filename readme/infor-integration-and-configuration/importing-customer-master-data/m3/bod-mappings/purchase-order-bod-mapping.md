# Purchase Order BOD Mapping

Deze pagina documenteert hoe DocBits Infor M3 `SyncPurchaseOrder` BODs inleest en de velden mapt naar de interne tabellen `PURCHASE_ORDER_HEADER` en Purchase Order Line.

{% file src="../../../../.gitbook/assets/Sync.PurchaseOrder.pdf" %}
Oorspronkelijke BOD mapping referentie (PDF)
{% endfile %}

## Kernprincipes

- **Geen valutaconversie in DocBits.** Bedragen worden precies opgeslagen zoals M3 ze in de BOD aanlevert, samen met hun `@currencyID`. Drie header-bedragen zijn beschikbaar: `ExtendedAmount` (transactievaluta), `ExtendedBaseAmount` (basisvaluta van de onderneming), `ExtendedReportAmount` (rapportagevaluta).
- **Geen conversie van meeteenheden in DocBits.** Hoeveelheden worden opgeslagen met hun `@unitCode`. `ReceivedBaseUOMQuantity` is de door M3 vooraf berekende basis-UoM-waarde — DocBits slaat die op zoals ze is.
- **De header-status wordt overgenomen uit de SXE-stage indien beschikbaar.** DocBits leest `UserArea/Property[@name='poeh.stagecd']` (waarden `1..8` → Ordered / Entered / Released / Allocated / Picked / Delivered / Invoiced / Cancelled) en gebruikt deze als de autoritatieve header-status. De standaard `Status/Code` wordt ook opgeslagen ter referentie.
- **Geen automatische statuslogica op deelhoeveelheden.** DocBits leidt geen status af uit ontvangen vs. bestelde hoeveelheden; de door M3 geleverde status wordt 1:1 overgenomen.
- **`CONO`/`AccountingEntityID` maakt geen deel uit van de PurchaseOrder-BOD.** Routering op bedrijfsnummer geldt voor leveranciers-stamgegevens (zie [Supplier BOD Mapping](supplier-bod-mapping.md)); inkooporders worden gekoppeld via `LocationID`.

## Header Mapping

→ DocBits Stamgegevenstabel: **PURCHASE\_ORDER\_HEADER**

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

### Header veld-referentie

| DocBits veld | M3 bron | Beschrijving |
|---|---|---|
| `purchase_order_number` | `MPHEAD.IAPUNO` | M3 inkoopordernummer, primaire sleutel. |
| `warehouse_id` | — | Leest `ShipToParty/Location[@type='Warehouse']/ID`. Het attribuut `@type='Warehouse'` wordt zelden door M3 gezet; het veld blijft dan NULL. Gebruik `location_id` als M3-native magazijn. |
| `location_id` | `MPHEAD.IAFACI` | M3-divisie/vestiging (magazijn) waar de BOD is gegenereerd. Wordt gebruikt voor organisatie-/vestigingsroutering binnen DocBits, inclusief matching tegen factuurvestigingen. |
| `status` | `MPHEAD.IAPUSL` | Ruwe `Status/Code` uit de BOD. Wordt gebruikt als fallback wanneer `sxe_stage` leeg is. |
| `sxe_stage` | `MPHEAD.IAPUSL` | De autoritatieve header-status, gelezen uit de UserArea-property `poeh.stagecd`. Mapt de M3 SXE-stage-codes 1..8 → Ordered, Entered, Released, Allocated, Picked, Delivered, Invoiced, Cancelled. Indien gezet, vervangt deze waarde `status` voor workflowbeslissingen. Met de preference `UPDATE_DOCUMENT_PURCHASE_ORDER_STATUS` ingeschakeld, propageert DocBits deze status naar gekoppelde facturen. |
| `supplier_id` | `MPHEAD.IASUNO` | Leveranciersnummer op de inkooporder. |
| `supplier_name` | `CIDMAS.IDSUNM` | Weergavenaam van de leverancier. |
| `order_date` | `MPHEAD.IAPUDT` | Datum waarop de inkooporder in M3 is aangemaakt. |
| `requested_shipment_date` | — | Wordt gelezen uit `RequiredDeliveryDateTime` op header-niveau indien aanwezig. De meeste M3-installaties hebben dit alleen op regel-niveau; gebruik in dat geval `requested_ship_date` op regel-niveau. |
| `total_amount` | `MPHEAD.IAOURR` | Ordertotaal in transactievaluta. Opgeslagen 1:1 uit `ExtendedAmount`. |
| `extended_amount` | `MPHEAD.IAOURR` | Zelfde bron als `total_amount`. Bewaard als separate ruwe kolom voor traceerbaarheid en downstream-consumenten die het canonieke BOD-pad verwachten. |
| `extended_base_amount` | `MPHEAD.IAOUVA` | Ordertotaal uitgedrukt in de basisvaluta van de onderneming. Door M3 gevuld indien beschikbaar. |
| `extended_report_amount` | `MPHEAD.IAOUVB` | Ordertotaal uitgedrukt in de rapportagevaluta. |
| `canceled_amount` / `canceled_base_amount` / `canceled_reporting_amount` | — | Annuleringsbedragen in transactie- / basis- / rapportagevaluta. Worden alleen door M3 gevuld na annuleringsgebeurtenissen. |
| `type_code` / `type_description` | — | Inkoopordertype uit `Classification/Codes/Code[@listID='Purchase Order Types']` (en bijbehorende `Description`). Voorbeelden: `P10` normale PO, `P20` voorraadaanvulling. Alleen opgeslagen voor weergave — geen filterlogica. |
| `buyer_contact_id` / `buyer_contact_name` | `MPHEAD.IABUYE` / gekoppelde gebruiker | Aan PO toegewezen inkoper. |
| `order_last_modified_by` / `order_last_modified_on` | `MPHEAD.IACHID` / `MPHEAD.IALMDT` | Auditvelden. |
| `disponent_id` / `disponent_name` | `MPHEAD.IARESP` / gekoppelde gebruiker | Plannerreferentie. |

## Regel Mapping

→ DocBits Stamgegevenstabel: **Purchase Order**

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

### Regel veld-referentie

| DocBits veld | M3 bron | Beschrijving |
|---|---|---|
| `item_id` | `MPLINE.IBITNO` | M3-artikelnummer. Fallback naar `@schemeName='NonStock'` voor niet-voorraadartikelen. |
| `supplier_item_id` | `MPLINE.IBSITE` / Classification | Artikelnummer aan leverancierzijde. Opgelost via drie fallbacks (in volgorde): `ID[@schemeName='Supplier']` → `Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']` → `Item/SupplierItemID/ID`. |
| `description` | `MPLINE.IBPITT` | Regel-artikelomschrijving. |
| `note` | `MSYTXL.TLTX60` | Regelopmerking. |
| `quantity` | `MPLINE.IBORQA` | Bestelde hoeveelheid. Opgeslagen met `unit_of_measure` (geen conversie). |
| `open_quantity` | `CFQA - RVQA` | Nog openstaande hoeveelheid (besteld minus ontvangen). Zelfde `unit_of_measure`. |
| `confirmed_quantity` | — | Door leverancier bevestigde hoeveelheid. M3 laat dit leeg; gevuld door ERPs die `BackOrderedQuantity` emitteren. |
| `received_quantity` | `MPLINE.IBRVQA` | Ontvangen hoeveelheid. |
| `received_base_mou_quantity` | `MPLINE.IBRVQA` (basis-UoM) | Ontvangen hoeveelheid omgerekend naar de basismeeteenheid door M3 zelf. DocBits rekent niet — het slaat op wat M3 stuurt. Nuttig voor voorraadboekhouding. |
| `unit_of_measure` | `MPLINE.IBPUUN` | Transactie-UoM. Geldt voor `quantity`, `open_quantity`, `received_quantity`. |
| `unit_price` | `MPLINE.IBPUPR` | Eenheidsprijs in transactievaluta. |
| `unit_price_per` / `unit_code_price` | `MPLINE.IBCPUC` / `MPLINE.IBPPUN` | Prijs-per hoeveelheid en bijbehorende eenheidscode (prijsmodifier, bv. prijs per 100 stuks). |
| `total_amount` | `LNAM + EXEP` | Regeltotaal. Opgelost via fallback `[TotalAmount, ExtendedAmount]` — wanneer `TotalAmount` ontbreekt, is `total_amount` gelijk aan `extended_amount`. Wanneer beide aanwezig zijn, kan `TotalAmount` belastingen/kortingen bevatten terwijl `extended_amount` `quantity × unit_price` is. |
| `extended_amount` | `LNAM` / `LNA2` | Ruwe `ExtendedAmount` (regelsubtotaal zonder belasting/korting). |
| `currency` | `MPHEAD.IACUCD` | Transactievaluta. Gelezen uit `TotalAmount/@currencyID`, met `ExtendedAmount/@currencyID` als fallback. |
| `status` | `MPLINE.IBPUST` | Regelstatus. Opgeslagen voor rapportage; geen DocBits-workflowlogica leidt hieruit af. |
| `buyer_id` / `buyer_name` | `MPLINE.IBBUYE` / gekoppelde gebruiker | Inkoper op regelniveau. `buyer_name` wordt zelden door M3 op de regel gevuld; de leveranciers-inkoperreferentie staat in [Supplier BOD Mapping](supplier-bod-mapping.md). |
| `geo_code` | — | Geo-code voor US/CA tax-engines. Alleen gevuld door ERPs die het emitteren. |
| `delivery_method` | `MPLINE.IBMODL` | Regelafleveringsmethode (M3 `MODL`-code). |
| `promised_delivery_date` | `CODT, DWDT/TIHM` | Door leverancier bevestigde leveringsdatum. |
| `requested_ship_date` | `MPLINE.IBDWDT` | Gewenste verzenddatum op de regel — operationeel relevante gewenste leveringsdatum. |
| `sub_line_number` | — | Optionele sub-regel-identifier. Opgeslagen indien aanwezig; M3 laat hem doorgaans leeg. |
| `schedule_line_number` | — | Optionele schedule-line-referentie voor PO's met geplande leveringen. |
| `order_multiple` / `standard_quantity` | `MPLINE.IBOMUL` / UserArea | Bestelveelvoud op de regel (minimale bestelhoeveelheid) en standaard verpakkingshoeveelheid. |

## Veelgestelde vragen

### Hoe behandelt DocBits inkooporders in vreemde valuta?

DocBits converteert geen valuta. Het transactiebedrag (`total_amount`, `extended_amount`, `unit_price`) wordt opgeslagen samen met zijn `@currencyID`. Wanneer de onderneming een andere basis- of rapportagevaluta gebruikt, levert M3 vooraf geconverteerde waarden via `extended_base_amount` en `extended_report_amount` — opgeslagen als aanvullende kolommen op de header.

### Hoe leidt DocBits de status van een gedeeltelijke ontvangst af?

Niet. De header-status weerspiegelt de M3 SXE-stage (`poeh.stagecd`) op het moment van de BOD-emissie. Als je een gedeeltelijke-ontvangst-indicator nodig hebt, leid die dan af uit `open_quantity` vs. `quantity` op de regeltabel.

### Wat is het verschil tussen `total_amount` en `extended_amount` op de regel?

Beide kolommen bestaan om historische/UI-redenen. `total_amount` wordt opgelost via `[TotalAmount, ExtendedAmount]`, dus is gelijk aan `extended_amount` zodra `TotalAmount` ontbreekt. Wanneer M3 beide emitteert, kan `TotalAmount` belastingen of kortingen bevatten bovenop de `quantity × unit_price`-waarde die in `extended_amount` staat.

### Waarom wordt het magazijn naar twee verschillende paden gemapt?

`warehouse_id` leest `ShipToParty/Location[@type='Warehouse']/ID`, dat de meeste M3-installaties leeg laten (het `@type`-attribuut wordt zelden gezet). `location_id` leest `DataArea/Sync/LocationID`, dat altijd door M3 wordt gevuld en correspondeert met de divisie/vestiging waar de PO bij hoort. Behandel `location_id` als M3-native magazijn-identifier.

### Sommige velden zijn gedocumenteerd maar altijd leeg (`buyer_name`, `geo_code`, `confirmed_quantity`, `sub_line_number`, …). Waarom zijn ze gemapt?

Deze mappings zijn defensief: het BOD-schema staat de velden toe, en andere ERPs of M3-uitbreidingen op maat kunnen ze vullen. Wanneer M3 ze leeg laat, zijn de kolommen eenvoudigweg NULL in DocBits.
