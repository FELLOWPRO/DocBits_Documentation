---
description: Spagna Facturae (3.2, 3.2.1, 3.2.2) – Supporto documenti elettronici in DocBits
---

# 🇪🇸 Spagna Facturae

| Proprietà | Valore |
|-----------|--------|
| **Paese / Regione** | Spagna |
| **Tipi di documento** | Fattura (Factura), Nota di credito |
| **Formato** | XML |
| **Standard** | Facturae 3.2 / 3.2.1 / 3.2.2 (Agencia Tributaria / AEAT) |
| **Locale** | `es_ES` |

Facturae è lo standard spagnolo obbligatorio per la fatturazione elettronica, gestito dall'Agencia Estatal de Administración Tributaria (AEAT) e dal Ministero delle Finanze. È obbligatorio per le fatture destinate agli enti del settore pubblico spagnolo e ampiamente utilizzato nelle transazioni B2B. L'elemento radice è `<fe:Facturae>` con un URL namespace versionato. DocBits rileva la versione tramite l'attributo `xsi:schemaLocation`, che fa riferimento a uno degli URL di schema ufficiali:

| Versione | URL schema |
|----------|-----------|
| Facturae 3.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2.xml` |
| Facturae 3.2.1 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_1.xml` |
| Facturae 3.2.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_2.xml` |

## Stato del supporto

| Componente | Stato |
|------------|-------|
| Anteprima | ✅ Supportato |
| Estrazione campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Anteprima predefinita

<figure><img src="spain-facturae-preview.png" alt="Anteprima fattura Spagna Facturae in DocBits"><figcaption><p>Anteprima predefinita di DocBits per una fattura Spagna Facturae 3.2.2</p></figcaption></figure>

## Mappatura dei campi

### Campi di intestazione

| Campo DocBits | Elemento XML sorgente | Note |
|---|---|---|
| `invoice_id` | `Invoices/Invoice/InvoiceHeader/InvoiceNumber` | Numero fattura |
| `invoice_date` | `Invoices/Invoice/InvoiceIssueData/IssueDate` | Data di emissione (AAAA-MM-GG) |
| `due_date` | `PaymentDetails/Installment/InstallmentDueDate` | Data di scadenza del pagamento |
| `invoice_type` | `Invoices/Invoice/InvoiceHeader/InvoiceDocumentType` | FC=Fattura, NC=Nota di credito |
| `currency` | `Invoices/Invoice/InvoiceIssueData/InvoiceCurrencyCode` | Sempre `EUR` |
| `purchase_order` | `Invoices/Invoice/InvoiceHeader/ReceiverContractReference` | Riferimento ordine/contratto acquirente |
| `net_amount` | `Invoices/Invoice/InvoiceTotals/TotalGrossAmountBeforeTaxes` | Importo netto IVA esclusa |
| `tax_amount` | `Invoices/Invoice/InvoiceTotals/TotalTaxOutputs` | Totale IVA |
| `total_amount` | `Invoices/Invoice/InvoiceTotals/InvoiceTotal` | Importo totale IVA inclusa |
| `tax_rate` | `TaxesOutputs/Tax/TaxRate` | Aliquota IVA in % (standard 21%) |
| `payment_terms` | `PaymentDetails/Installment/PaymentMeans` | Codice mezzo di pagamento |
| `supplier_name` | `Parties/SellerParty/LegalEntity/CorporateName` | Ragione sociale fornitore |
| `supplier_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF (es. `ES12345678A`) |
| `supplier_tax_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF o CIF spagnolo |
| `supplier_address` | `Parties/SellerParty/LegalEntity/AddressInSpain/Address` | Indirizzo fornitore |
| `supplier_city` | `Parties/SellerParty/LegalEntity/AddressInSpain/Town` | Città fornitore |
| `supplier_postal_code` | `Parties/SellerParty/LegalEntity/AddressInSpain/PostCode` | CAP fornitore |
| `supplier_country` | `Parties/SellerParty/LegalEntity/AddressInSpain/CountryCode` | Codice paese ISO (`ESP`) |
| `buyer_name` | `Parties/BuyerParty/LegalEntity/CorporateName` | Ragione sociale acquirente |
| `buyer_id` | `Parties/BuyerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF acquirente |
| `buyer_address` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Address` | Indirizzo acquirente |
| `buyer_city` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Town` | Città acquirente |
| `buyer_postal_code` | `Parties/BuyerParty/LegalEntity/AddressInSpain/PostCode` | CAP acquirente |
| `buyer_country` | `Parties/BuyerParty/LegalEntity/AddressInSpain/CountryCode` | Codice paese ISO (`ESP`) |
| `iban` | `PaymentDetails/Installment/AccountToBeCredited/IBAN` | IBAN beneficiario |

### Tabella righe (`INVOICE_TABLE`)

Percorso riga: `Invoices/Invoice/Items/InvoiceLine`

| Colonna | Elemento XML sorgente | Note |
|---|---|---|
| `POSITION` | `ItemDescription` | Sequenza / descrizione usata come identificatore |
| `DESCRIPTION` | `ItemDescription` | Descrizione articolo |
| `QUANTITY` | `Quantity` | Quantità fatturata |
| `UNIT` | `UnitOfMeasure` | Unità di misura (es. `units`) |
| `UNIT_PRICE` | `UnitPriceWithoutTax` | Prezzo unitario IVA esclusa |
| `VAT_RATE` | `TaxesOutputs/Tax/TaxRate` | Aliquota IVA in % (tipicamente 21%) |
| `VAT` | `TaxesOutputs/Tax/TaxAmount/TotalAmount` | Importo IVA per riga |
| `NET_AMOUNT` | `TotalCost` | Totale riga IVA esclusa |

## Regole di classificazione

DocBits rileva i documenti Facturae abbinando l'attributo `xsi:schemaLocation` sull'elemento radice `<fe:Facturae>`:

| Tipo documento elettronico | Pattern |
|---------------------------|---------|
| FACTURAE 3.2 | `xsi:schemaLocation` contiene `Facturaev3_2.xml` (non 3_2_1 o 3_2_2) |
| FACTURAE 3.2.1 | `xsi:schemaLocation` contiene `Facturaev3_2_1.xml` |
| FACTURAE 3.2.2 | `xsi:schemaLocation` contiene `Facturaev3_2_2.xml` |

L'elemento radice è `<fe:Facturae>` con namespace `http://www.facturae.es/Facturae/2014/v3.2.2/Facturae` (specifico per versione). La classificazione usa il principio **primo match vince**, con i pattern più specifici (3.2.2, 3.2.1) valutati prima del generico 3.2.

## Correlati

- [Standard e-fattura attualmente supportati](../../currently-supported-e-invoice-standards/)
- [Documenti elettronici supportati](./)
