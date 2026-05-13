# Mappatura BOD Purchase Order

Questa pagina documenta come DocBits ingerisce i BOD `SyncPurchaseOrder` di Infor M3 e mappa i campi sulle tabelle interne `PURCHASE_ORDER_HEADER` e Purchase Order Line.

{% file src="../../../../.gitbook/assets/Sync.PurchaseOrder.pdf" %}
Riferimento originale della mappatura BOD (PDF)
{% endfile %}

## Principi chiave

- **Nessuna conversione di valuta in DocBits.** Gli importi vengono persistiti esattamente come M3 li consegna nel BOD, insieme al loro `@currencyID`. Tre importi di intestazione sono disponibili: `ExtendedAmount` (valuta di transazione), `ExtendedBaseAmount` (valuta base della società), `ExtendedReportAmount` (valuta di reporting).
- **Nessuna conversione di unità di misura in DocBits.** Le quantità vengono salvate con il loro `@unitCode`. `ReceivedBaseUOMQuantity` è il valore in UoM base pre-calcolato da M3 — DocBits lo salva così com'è.
- **Lo stato dell'intestazione viene preso dallo stage SXE quando disponibile.** DocBits legge `UserArea/Property[@name='poeh.stagecd']` (valori `1..8` → Ordered / Entered / Released / Allocated / Picked / Delivered / Invoiced / Cancelled) e lo usa come stato di intestazione autoritativo. Lo `Status/Code` standard viene comunque salvato come riferimento.
- **Nessuna logica automatica di stato per quantità parziale.** DocBits non deriva uno stato dalle quantità ricevute vs. ordinate; lo stato consegnato da M3 viene preso 1:1.
- **`CONO`/`AccountingEntityID` non fa parte del BOD PurchaseOrder.** Il routing per numero azienda si applica ai dati anagrafici fornitori (vedi [Supplier BOD Mapping](supplier-bod-mapping.md)); gli ordini d'acquisto sono assegnati tramite `LocationID`.

## Mappatura dell'Intestazione

→ Tabella dati anagrafici DocBits: **PURCHASE\_ORDER\_HEADER**

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

### Riferimento campi di intestazione

| Campo DocBits | Origine M3 | Descrizione |
|---|---|---|
| `purchase_order_number` | `MPHEAD.IAPUNO` | Numero d'ordine d'acquisto M3, chiave primaria. |
| `warehouse_id` | — | Legge `ShipToParty/Location[@type='Warehouse']/ID`. L'attributo `@type='Warehouse'` viene impostato raramente da M3; il campo rimane NULL in tal caso. Usa `location_id` come magazzino nativo M3. |
| `location_id` | `MPHEAD.IAFACI` | Divisione/stabilimento (magazzino) M3 dove il BOD è stato generato. Usato per il routing organizzazione/stabilimento all'interno di DocBits, incluso il matching con gli stabilimenti delle fatture. |
| `status` | `MPHEAD.IAPUSL` | `Status/Code` grezzo dal BOD. Usato come fallback quando `sxe_stage` è vuoto. |
| `sxe_stage` | `MPHEAD.IAPUSL` | Stato di intestazione autoritativo, preso dalla proprietà UserArea `poeh.stagecd`. Mappa i codici SXE M3 1..8 → Ordered, Entered, Released, Allocated, Picked, Delivered, Invoiced, Cancelled. Quando impostato, prevale su `status` per le decisioni di workflow. Con la preference `UPDATE_DOCUMENT_PURCHASE_ORDER_STATUS` attivata, DocBits propaga questo stato sulle fatture collegate. |
| `supplier_id` | `MPHEAD.IASUNO` | Numero fornitore sull'ordine d'acquisto. |
| `supplier_name` | `CIDMAS.IDSUNM` | Nome di visualizzazione del fornitore. |
| `order_date` | `MPHEAD.IAPUDT` | Data di creazione dell'ordine d'acquisto in M3. |
| `requested_shipment_date` | — | Letto da `RequiredDeliveryDateTime` a livello intestazione se presente. La maggior parte delle installazioni M3 lo gestisce solo a livello riga; in tal caso usare `requested_ship_date` a livello riga. |
| `total_amount` | `MPHEAD.IAOURR` | Totale ordine in valuta di transazione. Salvato 1:1 da `ExtendedAmount`. |
| `extended_amount` | `MPHEAD.IAOURR` | Stessa origine di `total_amount`. Mantenuto come colonna grezza separata per tracciabilità e consumatori downstream che si aspettano il percorso BOD canonico. |
| `extended_base_amount` | `MPHEAD.IAOUVA` | Totale espresso nella valuta base aziendale. Riempito da M3 quando disponibile. |
| `extended_report_amount` | `MPHEAD.IAOUVB` | Totale espresso nella valuta di reporting aziendale. |
| `canceled_amount` / `canceled_base_amount` / `canceled_reporting_amount` | — | Importi di cancellazione in valuta di transazione / base / reporting. Riempiti da M3 solo dopo eventi di cancellazione. |
| `type_code` / `type_description` | — | Tipologia di ordine d'acquisto da `Classification/Codes/Code[@listID='Purchase Order Types']` (e sua `Description`). Esempi: `P10` PO normale, `P20` PO di riapprovvigionamento. Salvato solo per visualizzazione — nessuna logica di filtraggio. |
| `buyer_contact_id` / `buyer_contact_name` | `MPHEAD.IABUYE` / utente collegato | Buyer assegnato alla PO. |
| `order_last_modified_by` / `order_last_modified_on` | `MPHEAD.IACHID` / `MPHEAD.IALMDT` | Campi di audit. |
| `disponent_id` / `disponent_name` | `MPHEAD.IARESP` / utente collegato | Riferimento del pianificatore. |

## Mappatura delle Righe

→ Tabella dati anagrafici DocBits: **Purchase Order**

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

### Riferimento campi di riga

| Campo DocBits | Origine M3 | Descrizione |
|---|---|---|
| `item_id` | `MPLINE.IBITNO` | Numero articolo M3. Fallback su `@schemeName='NonStock'` per articoli non a magazzino. |
| `supplier_item_id` | `MPLINE.IBSITE` / Classification | Numero articolo lato fornitore. Risolto tramite tre fallback (in ordine): `ID[@schemeName='Supplier']` → `Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']` → `Item/SupplierItemID/ID`. |
| `description` | `MPLINE.IBPITT` | Descrizione articolo di riga. |
| `note` | `MSYTXL.TLTX60` | Testo nota di riga. |
| `quantity` | `MPLINE.IBORQA` | Quantità ordinata. Salvata con `unit_of_measure` (nessuna conversione). |
| `open_quantity` | `CFQA - RVQA` | Quantità ancora aperta (ordinata meno ricevuta). Stessa `unit_of_measure`. |
| `confirmed_quantity` | — | Quantità confermata dal fornitore. M3 lo lascia vuoto; riempito da ERP che emettono `BackOrderedQuantity`. |
| `received_quantity` | `MPLINE.IBRVQA` | Quantità ricevuta. |
| `received_base_mou_quantity` | `MPLINE.IBRVQA` (UoM base) | Quantità ricevuta convertita nell'unità di misura base da M3 stesso. DocBits non calcola — salva ciò che M3 invia. Utile per la contabilità di magazzino. |
| `unit_of_measure` | `MPLINE.IBPUUN` | UoM di transazione. Si applica a `quantity`, `open_quantity`, `received_quantity`. |
| `unit_price` | `MPLINE.IBPUPR` | Prezzo unitario in valuta di transazione. |
| `unit_price_per` / `unit_code_price` | `MPLINE.IBCPUC` / `MPLINE.IBPPUN` | Prezzo-per quantità e relativo codice unità (modificatore di prezzo, es. prezzo per 100 PCS). |
| `total_amount` | `LNAM + EXEP` | Totale di riga. Risolto tramite fallback `[TotalAmount, ExtendedAmount]` — quando `TotalAmount` manca, `total_amount` è uguale a `extended_amount`. Quando entrambi sono presenti, `TotalAmount` può includere tasse/sconti mentre `extended_amount` vale `quantity × unit_price`. |
| `extended_amount` | `LNAM` / `LNA2` | `ExtendedAmount` grezzo (subtotale riga senza tasse/sconti). |
| `currency` | `MPHEAD.IACUCD` | Valuta di transazione. Letta da `TotalAmount/@currencyID`, con `ExtendedAmount/@currencyID` come fallback. |
| `status` | `MPLINE.IBPUST` | Stato di riga. Salvato per reporting; nessuna logica di workflow DocBits ne deriva. |
| `buyer_id` / `buyer_name` | `MPLINE.IBBUYE` / utente collegato | Buyer a livello riga. `buyer_name` è raramente riempito da M3 sulla riga; il riferimento buyer fornitore è in [Supplier BOD Mapping](supplier-bod-mapping.md). |
| `geo_code` | — | Codice geografico per motori fiscali US/CA. Riempito solo da ERP che lo emettono. |
| `delivery_method` | `MPLINE.IBMODL` | Metodo di consegna della riga (codice `MODL` M3). |
| `promised_delivery_date` | `CODT, DWDT/TIHM` | Data di consegna confermata dal fornitore. |
| `requested_ship_date` | `MPLINE.IBDWDT` | Data di spedizione richiesta sulla riga — data di consegna desiderata operativamente rilevante. |
| `sub_line_number` | — | Identificatore opzionale di sub-riga. Salvato se presente; M3 lo lascia tipicamente vuoto. |
| `schedule_line_number` | — | Riferimento opzionale a riga di pianificazione per PO con consegne pianificate. |
| `order_multiple` / `standard_quantity` | `MPLINE.IBOMUL` / UserArea | Multiplo d'ordine della riga (quantità minima) e quantità standard di imballaggio. |

## Domande frequenti

### Come gestisce DocBits gli ordini d'acquisto in valuta estera?

DocBits non converte le valute. L'importo di transazione (`total_amount`, `extended_amount`, `unit_price`) viene salvato insieme al suo `@currencyID`. Quando l'azienda usa una valuta base o di reporting diversa, M3 fornisce valori pre-convertiti tramite `extended_base_amount` e `extended_report_amount` — salvati come colonne aggiuntive sull'intestazione.

### Come deriva DocBits lo stato di ricezione parziale?

Non lo fa. Lo stato di intestazione riflette lo stage SXE M3 (`poeh.stagecd`) al momento dell'emissione del BOD. Se serve un indicatore di ricezione parziale, derivalo da `open_quantity` vs. `quantity` sulla tabella delle righe.

### Qual è la differenza tra `total_amount` e `extended_amount` sulla riga?

Entrambe le colonne esistono per compatibilità storica/UI. `total_amount` viene risolto tramite `[TotalAmount, ExtendedAmount]`, quindi è uguale a `extended_amount` ogni volta che `TotalAmount` è assente. Quando M3 emette entrambi, `TotalAmount` può includere tasse o sconti sopra il valore `quantity × unit_price` conservato in `extended_amount`.

### Perché il magazzino è mappato su due percorsi diversi?

`warehouse_id` legge `ShipToParty/Location[@type='Warehouse']/ID`, che la maggior parte delle installazioni M3 lasciano vuoto (l'attributo `@type` è raramente impostato). `location_id` legge `DataArea/Sync/LocationID`, sempre riempito da M3 e corrispondente alla divisione/stabilimento a cui la PO appartiene. Trattate `location_id` come identificatore di magazzino nativo M3.

### Alcuni campi sono documentati ma sempre vuoti (`buyer_name`, `geo_code`, `confirmed_quantity`, `sub_line_number`, …). Perché sono mappati?

Queste mappature sono difensive: lo schema BOD consente i campi e altri ERP o estensioni M3 personalizzate possono riempirli. Quando M3 li lascia vuoti, le colonne sono semplicemente NULL in DocBits.
