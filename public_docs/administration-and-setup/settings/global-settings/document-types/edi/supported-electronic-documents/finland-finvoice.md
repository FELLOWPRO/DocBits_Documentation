---
description: Supporto per documenti elettronici Finvoice della Finlandia (1.3, 2.0, 2.01, 3.0) in DocBits
---

# 🇫🇮 Finlandia Finvoice

| Proprietà | Valore |
|----------|-------|
| **Paese / Regione** | Finlandia |
| **Tipi di documento** | Fattura (Lasku), Nota di credito (Hyvityslasku) |
| **Formato** | XML |
| **Standard** | Finvoice 1.3 / 2.0 / 2.01 / 3.0 (Finance Finland / Finanssiala) |
| **Impostazioni locali** | `fi_FI` |

Finvoice è lo standard di fatturazione elettronica del settore bancario finlandese, sviluppato e mantenuto da Finance Finland (Finanssiala ry). Viene utilizzato sia per la fatturazione B2B che B2G ed è trasmesso tramite l'infrastruttura bancaria finlandese. L'elemento radice è `<Finvoice>` con un URL di spazio dei nomi versionato. DocBits rileva la versione tramite l'attributo `xmlns`:

| Versione | URL spazio dei nomi |
|---------|--------------|
| Finvoice 1.3 | `http://www.finvoice.fi/schema/finvoice13` |
| Finvoice 2.0 | `http://www.finvoice.fi/schema/finvoice20` |
| Finvoice 2.01 | `http://www.finvoice.fi/schema/finvoice201` |
| Finvoice 3.0 | `http://www.finvoice.fi/schema/finvoice30` |

Il formato dell'ID aziendale finlandese (Y-tunnus) è `1234567-8` (7 cifre + cifra di controllo), utilizzato come identificatore di parte. Il numero di partita IVA ha il prefisso `FI` seguito da 8 cifre (es. `FI12345678`). Le date sono codificate nel formato `CCYYMMDD`.

## Stato del supporto

| Componente | Stato |
|-----------|--------|
| Anteprima | ✅ Supportato |
| Estrazione campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Anteprima predefinita

<figure><img src="finland-finvoice-preview.png" alt="Anteprima fattura Finvoice 3.0 della Finlandia in DocBits"><figcaption><p>Anteprima predefinita DocBits per una fattura Finvoice 3.0 della Finlandia (Lasku)</p></figcaption></figure>

## Mappatura dei campi

### Campi di intestazione

| Campo DocBits | Elemento XML sorgente | Note |
|---|---|---|
| `invoice_id` | `InvoiceDetails/InvoiceNumber` | Numero fattura |
| `invoice_date` | `InvoiceDetails/InvoiceDate` | Data nel formato `CCYYMMDD`, convertita in ISO 8601 |
| `due_date` | `InvoiceDetails/PaymentTermsDetails/InvoiceDueDate` | Data di scadenza del pagamento (`CCYYMMDD`) |
| `invoice_type` | `InvoiceDetails/InvoiceTypeCode` | INV01=Fattura, CRE01=Nota di credito |
| `currency` | `InvoiceDetails/InvoiceTotalVatExcludedAmount/@AmountCurrencyIdentifier` | Codice valuta (tipicamente `EUR`) |
| `net_amount` | `InvoiceDetails/InvoiceTotalVatExcludedAmount` | Importo netto IVA esclusa |
| `tax_amount` | `InvoiceDetails/InvoiceTotalVatAmount` | Importo IVA totale |
| `total_amount` | `InvoiceDetails/InvoiceTotalVatIncludedAmount` | Importo totale IVA inclusa |
| `tax_rate` | `InvoiceDetails/VatSpecificationDetails/VatRatePercent` | Aliquota IVA in % (standard 25,5%) |
| `supplier_name` | `SellerPartyDetails/SellerOrganisationName` | Nome della società fornitrice |
| `supplier_id` | `SellerPartyDetails/SellerPartyIdentifier` | ID aziendale finlandese (Y-tunnus, es. `1234567-8`) |
| `supplier_vat` | `SellerPartyDetails/SellerOrganisationTaxCode` | Numero IVA (es. `FI12345678`) |
| `supplier_address` | `SellerPartyDetails/SellerPostalAddressDetails/SellerStreetName` | Indirizzo del fornitore |
| `supplier_city` | `SellerPartyDetails/SellerPostalAddressDetails/SellerTownName` | Città del fornitore |
| `supplier_postal_code` | `SellerPartyDetails/SellerPostalAddressDetails/SellerPostCodeIdentifier` | CAP del fornitore |
| `supplier_country` | `SellerPartyDetails/SellerPostalAddressDetails/CountryCode` | Codice paese ISO (`FI`) |
| `buyer_name` | `BuyerPartyDetails/BuyerOrganisationName` | Nome della società acquirente |
| `buyer_id` | `BuyerPartyDetails/BuyerPartyIdentifier` | ID aziendale finlandese (Y-tunnus) |
| `buyer_address` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerStreetName` | Indirizzo dell'acquirente |
| `buyer_city` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerTownName` | Città dell'acquirente |
| `buyer_postal_code` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerPostCodeIdentifier` | CAP dell'acquirente |
| `buyer_country` | `BuyerPartyDetails/BuyerPostalAddressDetails/CountryCode` | Codice paese ISO (`FI`) |
| `iban` | `EpiDetails/EpiBfiPartyDetails/EpiBfiIdentifier` | IBAN del beneficiario (dettagli pagamento EPI) |
| `bic` | `EpiDetails/EpiPaymentInstructionId` | Codice BIC/SWIFT |
| `payment_terms` | `InvoiceDetails/PaymentTermsDetails/PaymentTermsFreeText` | Condizioni di pagamento in testo libero |

### Tabella righe (`INVOICE_TABLE`)

Percorso riga: `InvoiceRow`

| Colonna | Elemento XML sorgente | Note |
|---|---|---|
| `POSITION` | `InvoiceRow/ArticleIdentifier` | Codice articolo / prodotto |
| `DESCRIPTION` | `InvoiceRow/ArticleName` | Nome / descrizione articolo |
| `QUANTITY` | `InvoiceRow/DeliveredQuantity` | Quantità consegnata |
| `UNIT` | `InvoiceRow/DeliveredQuantity/@QuantityUnitCode` | Codice unità (es. `KPL` = pezzo) |
| `UNIT_PRICE` | `InvoiceRow/UnitPriceAmount` | Prezzo unitario IVA esclusa |
| `VAT_RATE` | `InvoiceRow/RowVatRatePercent` | Aliquota IVA in % per riga |
| `VAT` | `InvoiceRow/RowVatAmount` | Importo IVA per riga |
| `NET_AMOUNT` | `InvoiceRow/RowAmount` | Totale riga IVA esclusa |

## Regole di classificazione

DocBits rileva i documenti Finvoice facendo corrispondere l'attributo `xmlns` sull'elemento radice `<Finvoice>`:

| Tipo documento elettronico | Schema |
|--------------------------|---------|
| FINVOICE 1.3 | `xmlns` contiene `http://www.finvoice.fi/schema/finvoice13` |
| FINVOICE 2.0 | `xmlns` contiene `http://www.finvoice.fi/schema/finvoice20` (non 2.01) |
| FINVOICE 2.01 | `xmlns` contiene `http://www.finvoice.fi/schema/finvoice201` |
| FINVOICE 3.0 | `xmlns` contiene `http://www.finvoice.fi/schema/finvoice30` |

La classificazione utilizza il principio **primo risultato vincente** con pattern più specifici (2.01) valutati prima del generico 2.0.

## Correlati

- [Standard di fatturazione elettronica attualmente supportati](../../currently-supported-e-invoice-standards/)
- [Finlandia TEAPPSXML](./finland-teappsxml.md)
- [Documenti elettronici supportati](./)
