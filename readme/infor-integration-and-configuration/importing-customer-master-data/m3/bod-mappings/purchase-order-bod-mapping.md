# Mapowanie BOD Purchase Order

Ta strona dokumentuje sposób, w jaki DocBits pobiera BOD-y `SyncPurchaseOrder` z Infor M3 i mapuje pola na wewnętrzne tabele `PURCHASE_ORDER_HEADER` oraz Purchase Order Line.

{% file src="../../../../.gitbook/assets/Sync.PurchaseOrder.pdf" %}
Oryginalna referencja mapowania BOD (PDF)
{% endfile %}

## Zasady kluczowe

- **Brak konwersji walut w DocBits.** Kwoty są zapisywane dokładnie tak, jak M3 dostarcza je w BOD, wraz z ich `@currencyID`. Dostępne są trzy kwoty nagłówka: `ExtendedAmount` (waluta transakcji), `ExtendedBaseAmount` (waluta bazowa firmy), `ExtendedReportAmount` (waluta raportowa).
- **Brak konwersji jednostek miary w DocBits.** Ilości są przechowywane z ich `@unitCode`. `ReceivedBaseUOMQuantity` to wartość w jednostce bazowej wstępnie obliczona przez M3 — DocBits zapisuje ją bez zmian.
- **Status nagłówka jest pobierany z etapu SXE, gdy jest dostępny.** DocBits czyta `UserArea/Property[@name='poeh.stagecd']` (wartości `1..8` → Ordered / Entered / Released / Allocated / Picked / Delivered / Invoiced / Cancelled) i używa ich jako miarodajnego statusu nagłówka. Standardowe `Status/Code` jest również przechowywane jako referencja.
- **Brak automatycznej logiki statusu dla częściowych ilości.** DocBits nie wyprowadza statusu z ilości otrzymanych vs. zamówionych; status dostarczony przez M3 jest przyjmowany 1:1.
- **`CONO`/`AccountingEntityID` nie jest częścią BOD PurchaseOrder.** Routing po numerze firmy dotyczy danych głównych dostawców (zob. [Supplier BOD Mapping](supplier-bod-mapping.md)); zamówienia zakupu są przypisywane przez `LocationID`.

## Mapowanie Nagłówka

→ Tabela danych głównych DocBits: **PURCHASE\_ORDER\_HEADER**

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

### Referencja pól nagłówka

| Pole DocBits | Źródło M3 | Opis |
|---|---|---|
| `purchase_order_number` | `MPHEAD.IAPUNO` | Numer zamówienia zakupu M3, klucz podstawowy. |
| `warehouse_id` | — | Czyta `ShipToParty/Location[@type='Warehouse']/ID`. Atrybut `@type='Warehouse'` jest rzadko ustawiany przez M3; w takim przypadku pole pozostaje NULL. Używaj `location_id` jako natywnego magazynu M3. |
| `location_id` | `MPHEAD.IAFACI` | Dywizja/zakład (magazyn) M3, w którym wygenerowano BOD. Używany do routingu organizacja/zakład w DocBits, w tym do dopasowania do zakładów z faktur. |
| `status` | `MPHEAD.IAPUSL` | Surowy `Status/Code` z BOD. Używany jako fallback, gdy `sxe_stage` jest puste. |
| `sxe_stage` | `MPHEAD.IAPUSL` | Miarodajny status nagłówka, pobrany z właściwości UserArea `poeh.stagecd`. Mapuje kody SXE M3 1..8 → Ordered, Entered, Released, Allocated, Picked, Delivered, Invoiced, Cancelled. Gdy ustawiony, ma pierwszeństwo nad `status` dla decyzji workflow. Z włączoną preferencją `UPDATE_DOCUMENT_PURCHASE_ORDER_STATUS` DocBits propaguje ten status na powiązane faktury. |
| `supplier_id` | `MPHEAD.IASUNO` | Numer dostawcy na zamówieniu zakupu. |
| `supplier_name` | `CIDMAS.IDSUNM` | Nazwa wyświetlana dostawcy. |
| `order_date` | `MPHEAD.IAPUDT` | Data utworzenia zamówienia zakupu w M3. |
| `requested_shipment_date` | — | Czytane z `RequiredDeliveryDateTime` na poziomie nagłówka, jeśli istnieje. Większość konfiguracji M3 zawiera to pole tylko na poziomie linii; w takim przypadku użyj `requested_ship_date` z linii. |
| `total_amount` | `MPHEAD.IAOURR` | Suma zamówienia w walucie transakcji. Zapisywana 1:1 z `ExtendedAmount`. |
| `extended_amount` | `MPHEAD.IAOURR` | To samo źródło co `total_amount`. Zachowane jako osobna surowa kolumna dla śledzenia i konsumentów oczekujących kanonicznej ścieżki BOD. |
| `extended_base_amount` | `MPHEAD.IAOUVA` | Suma wyrażona w walucie bazowej firmy. Wypełniana przez M3, gdy jest dostępna. |
| `extended_report_amount` | `MPHEAD.IAOUVB` | Suma wyrażona w walucie raportowej firmy. |
| `canceled_amount` / `canceled_base_amount` / `canceled_reporting_amount` | — | Kwoty anulowania w walucie transakcji / bazowej / raportowej. Wypełniane przez M3 dopiero po zdarzeniach anulowania. |
| `type_code` / `type_description` | — | Typ zamówienia zakupu z `Classification/Codes/Code[@listID='Purchase Order Types']` (oraz jego `Description`). Przykłady: `P10` zwykłe PO, `P20` PO uzupełnienia magazynu. Zapisywane tylko do wyświetlania — bez logiki filtrowania. |
| `buyer_contact_id` / `buyer_contact_name` | `MPHEAD.IABUYE` / powiązany użytkownik | Kupiec przypisany do PO. |
| `order_last_modified_by` / `order_last_modified_on` | `MPHEAD.IACHID` / `MPHEAD.IALMDT` | Pola audytowe. |
| `disponent_id` / `disponent_name` | `MPHEAD.IARESP` / powiązany użytkownik | Referencja do planisty. |

## Mapowanie Linii

→ Tabela danych głównych DocBits: **Purchase Order**

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

### Referencja pól linii

| Pole DocBits | Źródło M3 | Opis |
|---|---|---|
| `item_id` | `MPLINE.IBITNO` | Numer artykułu M3. Fallback na `@schemeName='NonStock'` dla pozycji niemagazynowych. |
| `supplier_item_id` | `MPLINE.IBSITE` / Classification | Numer artykułu po stronie dostawcy. Rozwiązywany przez trzy fallbacki (w kolejności): `ID[@schemeName='Supplier']` → `Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']` → `Item/SupplierItemID/ID`. |
| `description` | `MPLINE.IBPITT` | Opis pozycji linii. |
| `note` | `MSYTXL.TLTX60` | Treść notatki linii. |
| `quantity` | `MPLINE.IBORQA` | Ilość zamówiona. Przechowywana z `unit_of_measure` (bez konwersji). |
| `open_quantity` | `CFQA - RVQA` | Ilość nadal otwarta (zamówiona minus otrzymana). Ta sama `unit_of_measure`. |
| `confirmed_quantity` | — | Ilość potwierdzona przez dostawcę. M3 pozostawia puste; wypełniane przez ERP-y emitujące `BackOrderedQuantity`. |
| `received_quantity` | `MPLINE.IBRVQA` | Ilość otrzymana. |
| `received_base_mou_quantity` | `MPLINE.IBRVQA` (jednostka bazowa) | Ilość otrzymana skonwertowana na jednostkę bazową przez sam M3. DocBits nie liczy — przechowuje to, co M3 przesyła. Przydatne do księgowości magazynowej. |
| `unit_of_measure` | `MPLINE.IBPUUN` | Jednostka transakcyjna. Dotyczy `quantity`, `open_quantity`, `received_quantity`. |
| `unit_price` | `MPLINE.IBPUPR` | Cena jednostkowa w walucie transakcji. |
| `unit_price_per` / `unit_code_price` | `MPLINE.IBCPUC` / `MPLINE.IBPPUN` | Cena za ilość i jej kod jednostki (modyfikator ceny, np. cena za 100 PCS). |
| `total_amount` | `LNAM + EXEP` | Suma linii. Rozwiązywana przez fallback `[TotalAmount, ExtendedAmount]` — gdy brak `TotalAmount`, `total_amount` jest równe `extended_amount`. Gdy oba są obecne, `TotalAmount` może zawierać podatki/rabaty, a `extended_amount` to `quantity × unit_price`. |
| `extended_amount` | `LNAM` / `LNA2` | Surowy `ExtendedAmount` (suma częściowa linii bez podatków/rabatów). |
| `currency` | `MPHEAD.IACUCD` | Waluta transakcji. Czytana z `TotalAmount/@currencyID`, z `ExtendedAmount/@currencyID` jako fallback. |
| `status` | `MPLINE.IBPUST` | Status linii. Przechowywany do raportowania; żadna logika workflow DocBits z niego nie wynika. |
| `buyer_id` / `buyer_name` | `MPLINE.IBBUYE` / powiązany użytkownik | Kupiec na poziomie linii. `buyer_name` jest rzadko wypełniane przez M3 na linii; referencja kupca dostawcy znajduje się w [Supplier BOD Mapping](supplier-bod-mapping.md). |
| `geo_code` | — | Kod geograficzny dla silników podatkowych US/CA. Wypełniany tylko przez ERP-y, które go emitują. |
| `delivery_method` | `MPLINE.IBMODL` | Metoda dostawy linii (kod `MODL` M3). |
| `promised_delivery_date` | `CODT, DWDT/TIHM` | Data dostawy potwierdzona przez dostawcę. |
| `requested_ship_date` | `MPLINE.IBDWDT` | Żądana data wysyłki na linii — operacyjnie istotna żądana data dostawy. |
| `sub_line_number` | — | Opcjonalny identyfikator podlinii. Przechowywany jeśli obecny; M3 zwykle pozostawia puste. |
| `schedule_line_number` | — | Opcjonalna referencja do linii harmonogramu dla PO z dostawami planowymi. |
| `order_multiple` / `standard_quantity` | `MPLINE.IBOMUL` / UserArea | Wielokrotność zamówienia linii (minimalna ilość) i standardowa ilość pakowania. |

## Częste pytania

### Jak DocBits obsługuje zamówienia zakupu w obcej walucie?

DocBits nie konwertuje walut. Kwota transakcyjna (`total_amount`, `extended_amount`, `unit_price`) jest przechowywana wraz z jej `@currencyID`. Gdy firma używa innej waluty bazowej lub raportowej, M3 dostarcza wstępnie skonwertowane wartości przez `extended_base_amount` i `extended_report_amount` — przechowywane jako dodatkowe kolumny na nagłówku.

### Jak DocBits wyprowadza status częściowego odbioru?

Nie wyprowadza. Status nagłówka odzwierciedla etap SXE M3 (`poeh.stagecd`) w momencie emisji BOD. Jeśli potrzebujesz wskaźnika częściowego odbioru, wyprowadź go z `open_quantity` vs. `quantity` na tabeli linii.

### Jaka jest różnica między `total_amount` a `extended_amount` na linii?

Obie kolumny istnieją ze względów historycznych/UI. `total_amount` jest rozwiązywane przez `[TotalAmount, ExtendedAmount]`, więc równa się `extended_amount`, gdy `TotalAmount` jest nieobecne. Gdy M3 emituje oba, `TotalAmount` może zawierać podatki lub rabaty powyżej wartości `quantity × unit_price` zapisanej w `extended_amount`.

### Dlaczego magazyn jest mapowany na dwie różne ścieżki?

`warehouse_id` czyta `ShipToParty/Location[@type='Warehouse']/ID`, co większość instalacji M3 pozostawia puste (atrybut `@type` jest rzadko ustawiany). `location_id` czyta `DataArea/Sync/LocationID`, zawsze wypełniane przez M3 i odpowiadające dywizji/zakładowi, do którego należy PO. Traktuj `location_id` jako natywny identyfikator magazynu M3.

### Niektóre pola są udokumentowane, ale zawsze puste (`buyer_name`, `geo_code`, `confirmed_quantity`, `sub_line_number`, …). Dlaczego są zmapowane?

Te mapowania są defensywne: schemat BOD pozwala na te pola, a inne ERP-y lub niestandardowe rozszerzenia M3 mogą je wypełniać. Gdy M3 pozostawia je puste, kolumny w DocBits są po prostu NULL.
