# Purchase Order BOD Mapiranje

Ova stranica dokumentuje kako DocBits prima Infor M3 `SyncPurchaseOrder` BOD-ove i mapira polja na interne tabele `PURCHASE_ORDER_HEADER` i Purchase Order Line.

{% file src="../../../../.gitbook/assets/Sync.PurchaseOrder.pdf" %}
Originalna BOD referenca mapiranja (PDF)
{% endfile %}

## Ključni principi

- **Bez konverzije valuta u DocBits-u.** Iznosi se čuvaju tačno onako kako ih M3 dostavlja u BOD-u, zajedno sa svojim `@currencyID`. Tri iznosa zaglavlja su dostupna: `ExtendedAmount` (valuta transakcije), `ExtendedBaseAmount` (osnovna valuta kompanije), `ExtendedReportAmount` (valuta izveštavanja).
- **Bez konverzije jedinica mere u DocBits-u.** Količine se čuvaju sa svojim `@unitCode`. `ReceivedBaseUOMQuantity` je vrednost u osnovnoj UoM koju je M3 prethodno izračunao — DocBits je čuva onakvu kakva jeste.
- **Status zaglavlja se uzima iz SXE faze kada je dostupna.** DocBits čita `UserArea/Property[@name='poeh.stagecd']` (vrednosti `1..8` → Ordered / Entered / Released / Allocated / Picked / Delivered / Invoiced / Cancelled) i koristi je kao autoritativni status zaglavlja. Standardni `Status/Code` se takođe čuva radi reference.
- **Bez automatske logike statusa za delimične količine.** DocBits ne izvodi status iz primljenih vs. naručenih količina; status koji M3 dostavi uzima se 1:1.
- **`CONO`/`AccountingEntityID` nije deo PurchaseOrder BOD-a.** Rutiranje po broju kompanije važi za matične podatke dobavljača (vidi [Supplier BOD Mapiranje](supplier-bod-mapping.md)); narudžbenice se dodeljuju preko `LocationID`.

## Mapiranje Zaglavlja

→ DocBits Tabela Matičnih Podataka: **PURCHASE\_ORDER\_HEADER**

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

### Referenca polja zaglavlja

| DocBits polje | M3 izvor | Opis |
|---|---|---|
| `purchase_order_number` | `MPHEAD.IAPUNO` | M3 broj narudžbenice, primarni ključ. |
| `warehouse_id` | — | Čita `ShipToParty/Location[@type='Warehouse']/ID`. Atribut `@type='Warehouse'` retko postavlja M3; polje ostaje NULL u tom slučaju. Koristite `location_id` kao M3-nativno skladište. |
| `location_id` | `MPHEAD.IAFACI` | M3 divizija/postrojenje (skladište) gde je BOD generisan. Koristi se za usmeravanje organizacije/postrojenja unutar DocBits-a, uključujući uparivanje sa postrojenjima na fakturama. |
| `status` | `MPHEAD.IAPUSL` | Sirov `Status/Code` iz BOD-a. Koristi se kao fallback kada je `sxe_stage` prazan. |
| `sxe_stage` | `MPHEAD.IAPUSL` | Autoritativni status zaglavlja, čitan iz UserArea svojstva `poeh.stagecd`. Mapira M3 SXE kodove faze 1..8 → Ordered, Entered, Released, Allocated, Picked, Delivered, Invoiced, Cancelled. Kada je postavljen, ima prioritet nad `status` za odluke toka rada. Sa uključenom postavkom `UPDATE_DOCUMENT_PURCHASE_ORDER_STATUS`, DocBits propagira ovaj status na povezane fakture. |
| `supplier_id` | `MPHEAD.IASUNO` | Broj dobavljača na narudžbenici. |
| `supplier_name` | `CIDMAS.IDSUNM` | Prikazno ime dobavljača. |
| `order_date` | `MPHEAD.IAPUDT` | Datum kreiranja narudžbenice u M3. |
| `requested_shipment_date` | — | Čita se sa nivoa zaglavlja iz `RequiredDeliveryDateTime` ako postoji. Većina M3 podešavanja drži ovo polje samo na liniji; u tom slučaju koristite `requested_ship_date` sa linije. |
| `total_amount` | `MPHEAD.IAOURR` | Ukupan iznos narudžbenice u valuti transakcije. Čuvan 1:1 iz `ExtendedAmount`. |
| `extended_amount` | `MPHEAD.IAOURR` | Isti izvor kao `total_amount`. Drži se kao zasebna sirova kolona radi praćenja i nizvodnih potrošača koji očekuju kanonski BOD put. |
| `extended_base_amount` | `MPHEAD.IAOUVA` | Ukupan iznos izražen u osnovnoj valuti kompanije. Popunjava ga M3 kada je dostupno. |
| `extended_report_amount` | `MPHEAD.IAOUVB` | Ukupan iznos izražen u izveštajnoj valuti kompanije. |
| `canceled_amount` / `canceled_base_amount` / `canceled_reporting_amount` | — | Iznosi otkazivanja u valuti transakcije / osnovnoj / izveštajnoj. Popunjava ih M3 tek nakon događaja otkazivanja. |
| `type_code` / `type_description` | — | Tip narudžbenice iz `Classification/Codes/Code[@listID='Purchase Order Types']` (i njegovog `Description`). Primeri: `P10` normalna PO, `P20` PO popune zaliha. Čuva se samo za prikaz — bez logike filtriranja. |
| `buyer_contact_id` / `buyer_contact_name` | `MPHEAD.IABUYE` / povezani korisnik | Kupac dodeljen PO. |
| `order_last_modified_by` / `order_last_modified_on` | `MPHEAD.IACHID` / `MPHEAD.IALMDT` | Polja revizije. |
| `disponent_id` / `disponent_name` | `MPHEAD.IARESP` / povezani korisnik | Referenca planera. |

## Mapiranje Linija

→ DocBits Tabela Matičnih Podataka: **Purchase Order**

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

### Referenca polja linije

| DocBits polje | M3 izvor | Opis |
|---|---|---|
| `item_id` | `MPLINE.IBITNO` | M3 broj artikla. Fallback na `@schemeName='NonStock'` za neskladišne artikle. |
| `supplier_item_id` | `MPLINE.IBSITE` / Classification | Broj artikla sa strane dobavljača. Rešava se kroz tri fallback-a (po redosledu): `ID[@schemeName='Supplier']` → `Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']` → `Item/SupplierItemID/ID`. |
| `description` | `MPLINE.IBPITT` | Opis artikla na liniji. |
| `note` | `MSYTXL.TLTX60` | Tekst napomene linije. |
| `quantity` | `MPLINE.IBORQA` | Naručena količina. Čuva se sa `unit_of_measure` (bez konverzije). |
| `open_quantity` | `CFQA - RVQA` | Količina koja je još otvorena (naručeno minus primljeno). Ista `unit_of_measure`. |
| `confirmed_quantity` | — | Količina koju je potvrdio dobavljač. M3 ostavlja prazno; popunjavaju ERP-ovi koji emituju `BackOrderedQuantity`. |
| `received_quantity` | `MPLINE.IBRVQA` | Primljena količina. |
| `received_base_mou_quantity` | `MPLINE.IBRVQA` (osnovna UoM) | Primljena količina konvertovana u osnovnu jedinicu mere od strane samog M3. DocBits ne računa — čuva ono što M3 šalje. Korisno za skladišno knjigovodstvo. |
| `unit_of_measure` | `MPLINE.IBPUUN` | Transakciona UoM. Važi za `quantity`, `open_quantity`, `received_quantity`. |
| `unit_price` | `MPLINE.IBPUPR` | Jedinična cena u valuti transakcije. |
| `unit_price_per` / `unit_code_price` | `MPLINE.IBCPUC` / `MPLINE.IBPPUN` | Cena-po količini i njen kod jedinice (modifikator cene, npr. cena po 100 PCS). |
| `total_amount` | `LNAM + EXEP` | Ukupno linije. Rešava se kroz fallback `[TotalAmount, ExtendedAmount]` — kada `TotalAmount` nedostaje, `total_amount` je jednako `extended_amount`. Kada su oba prisutna, `TotalAmount` može sadržati poreze/popuste, dok `extended_amount` predstavlja `quantity × unit_price`. |
| `extended_amount` | `LNAM` / `LNA2` | Sirov `ExtendedAmount` (međuzbir linije bez poreza/popusta). |
| `currency` | `MPHEAD.IACUCD` | Valuta transakcije. Čita se sa `TotalAmount/@currencyID`, sa `ExtendedAmount/@currencyID` kao fallback. |
| `status` | `MPLINE.IBPUST` | Status linije. Čuva se za izveštavanje; nijedna logika toka rada DocBits-a ne izvodi se iz njega. |
| `buyer_id` / `buyer_name` | `MPLINE.IBBUYE` / povezani korisnik | Kupac na nivou linije. `buyer_name` M3 retko popunjava na liniji; referenca kupca dobavljača nalazi se u [Supplier BOD Mapiranje](supplier-bod-mapping.md). |
| `geo_code` | — | Geo kod za US/CA poreske motore. Popunjavaju ga samo ERP-ovi koji ga emituju. |
| `delivery_method` | `MPLINE.IBMODL` | Metoda isporuke linije (M3 `MODL` kod). |
| `promised_delivery_date` | `CODT, DWDT/TIHM` | Datum isporuke potvrđen od dobavljača. |
| `requested_ship_date` | `MPLINE.IBDWDT` | Tražen datum slanja na liniji — operativno relevantan željeni datum isporuke. |
| `sub_line_number` | — | Opcioni identifikator pod-linije. Čuva se ako je prisutan; M3 obično ostavlja prazno. |
| `schedule_line_number` | — | Opciona referenca na liniju rasporeda za PO sa planiranim isporukama. |
| `order_multiple` / `standard_quantity` | `MPLINE.IBOMUL` / UserArea | Višekratnik naručivanja na liniji (minimalna količina) i standardna količina pakovanja. |

## Često postavljana pitanja

### Kako DocBits obrađuje narudžbenice u stranoj valuti?

DocBits ne konvertuje valute. Iznos transakcije (`total_amount`, `extended_amount`, `unit_price`) čuva se zajedno sa svojim `@currencyID`. Kada kompanija koristi različitu osnovnu ili izveštajnu valutu, M3 dostavlja unapred konvertovane vrednosti preko `extended_base_amount` i `extended_report_amount` — čuvaju se kao dodatne kolone na zaglavlju.

### Kako DocBits izvodi status delimičnog prijema?

Ne izvodi ga. Status zaglavlja odražava M3 SXE fazu (`poeh.stagecd`) u trenutku emisije BOD-a. Ako vam je potreban indikator delimičnog prijema, izvedite ga iz `open_quantity` vs. `quantity` na tabeli linija.

### Koja je razlika između `total_amount` i `extended_amount` na liniji?

Obe kolone postoje radi istorijske/UI kompatibilnosti. `total_amount` se rešava kroz `[TotalAmount, ExtendedAmount]`, pa je jednak `extended_amount` uvek kada nedostaje `TotalAmount`. Kada M3 emituje oba, `TotalAmount` može uključivati poreze ili popuste iznad vrednosti `quantity × unit_price` koja se čuva u `extended_amount`.

### Zašto se skladište mapira na dve različite putanje?

`warehouse_id` čita `ShipToParty/Location[@type='Warehouse']/ID`, što većina M3 instalacija ostavlja praznim (atribut `@type` se retko postavlja). `location_id` čita `DataArea/Sync/LocationID`, koji M3 uvek popunjava i koji odgovara diviziji/postrojenju kojem PO pripada. Tretirajte `location_id` kao M3-nativni identifikator skladišta.

### Neka polja su dokumentovana ali uvek prazna (`buyer_name`, `geo_code`, `confirmed_quantity`, `sub_line_number`, …). Zašto su mapirana?

Ova mapiranja su defanzivna: BOD šema dozvoljava polja, a drugi ERP-ovi ili prilagođena M3 proširenja mogu ih popunjavati. Kada ih M3 ostavi prazna, kolone su jednostavno NULL u DocBits-u.
