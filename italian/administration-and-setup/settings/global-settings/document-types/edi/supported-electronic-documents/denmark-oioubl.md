---
description: Supporto per documenti elettronici Denmark OIOUBL 2.1 in DocBits
---

# 🇩🇰 Denmark OIOUBL 2.1

| Proprietà | Valore |
|----------|-------|
| **Paese / Regione** | Danimarca |
| **Tipi di Documento** | Invoice (Faktura), Credit Note |
| **Formato** | XML (UBL 2.1) |
| **Standard** | OIOUBL 2.1 (Offentlig Information Online UBL) |
| **Locale** | `da_DK` |

OIOUBL (Offentlig Information Online UBL) è lo standard danese per la fatturazione elettronica basato su UBL 2.1. È obbligatorio per le fatture destinate agli enti del settore pubblico danese ed è ampiamente utilizzato nelle transazioni B2B. DocBits rileva i documenti OIOUBL 2.1 tramite la presenza di `<cbc:CustomizationID>OIOUBL-2.1</cbc:CustomizationID>`. L'identificatore di profilo `urn:www.nesubl.eu:profiles:profile5:ver2.0` indica il profilo fattura NES (Northern European Subset).

## Stato del Supporto

| Componente | Stato |
|-----------|--------|
| Anteprima | ✅ Supportato |
| Estrazione Campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Anteprima Predefinita

<figure><img src="denmark-oioubl-preview.png" alt="Anteprima fattura Denmark OIOUBL 2.1 in DocBits"><figcaption><p>Anteprima predefinita DocBits per una fattura Denmark OIOUBL 2.1 (Faktura)</p></figcaption></figure>

## Mappatura dei Campi

### Campi di Intestazione

| Campo DocBits | Elemento XML Sorgente | Note |
|---|---|---|
| `invoice_id` | `cbc:ID` | Numero fattura |
| `invoice_date` | `cbc:IssueDate` | Data di emissione ISO 8601 |
| `due_date` | `cbc:DueDate` | Data di scadenza del pagamento |
| `invoice_type` | `cbc:InvoiceTypeCode` | Codice UNCL 1001 (380=Fattura, 381=Nota di Credito) |
| `currency` | `cbc:DocumentCurrencyCode` | Sempre `DKK` (Corona danese) |
| `purchase_order` | `cac:OrderReference/cbc:ID` | Numero di riferimento ordine dell'acquirente |
| `buyer_reference` | `cbc:BuyerReference` | Riferimento interno dell'acquirente / numero di ubicazione EAN |
| `note` | `cbc:Note` | Istruzioni di pagamento o note in testo libero |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Importo netto IVA esclusa |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Importo IVA totale (aliquota standard 25%) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Importo totale IVA inclusa |
| `tax_rate` | `cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` | Aliquota IVA in % |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Ragione sociale del fornitore |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` | Numero CVR (es. `DK12345678`) |
| `supplier_vat` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Numero IVA/CVR |
| `supplier_address` | `cac:AccountingSupplierParty/.../cbc:StreetName` | Indirizzo del fornitore |
| `supplier_city` | `cac:AccountingSupplierParty/.../cbc:CityName` | Città del fornitore |
| `supplier_postal_code` | `cac:AccountingSupplierParty/.../cbc:PostalZone` | CAP del fornitore |
| `supplier_country` | `cac:AccountingSupplierParty/.../cbc:IdentificationCode` | Codice paese ISO (`DK`) |
| `customer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Ragione sociale del cliente |
| `customer_id` | `cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` | Numero CVR |
| `customer_vat` | `cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Numero IVA/CVR |
| `customer_address` | `cac:AccountingCustomerParty/.../cbc:StreetName` | Indirizzo del cliente |
| `customer_city` | `cac:AccountingCustomerParty/.../cbc:CityName` | Città del cliente |
| `customer_postal_code` | `cac:AccountingCustomerParty/.../cbc:PostalZone` | CAP del cliente |
| `customer_country` | `cac:AccountingCustomerParty/.../cbc:IdentificationCode` | Codice paese ISO (`DK`) |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Conto bancario / IBAN |
| `bic` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID` | Codice BIC/SWIFT |

### Tabella Voci di Riga (`INVOICE_TABLE`)

Percorso riga: `cac:InvoiceLine`

| Colonna | Elemento XML Sorgente | Note |
|---|---|---|
| `POSITION` | `cbc:ID` | Numero di sequenza della riga |
| `DESCRIPTION` | `cac:Item/cbc:Name` | Nome / descrizione articolo |
| `QUANTITY` | `cbc:InvoicedQuantity` | Quantità fatturata |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Prezzo unitario IVA esclusa |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Totale riga IVA esclusa |

## Regola di Classificazione

DocBits rileva i documenti OIOUBL 2.1 facendo corrispondere l'elemento `CustomizationID`:

| Tipo Documento Elettronico | Pattern |
|--------------------------|---------|
| OIOUBL 2.1 | `<cbc:CustomizationID>OIOUBL-2\.1\s*</cbc:CustomizationID>` |

L'elemento radice è `<Invoice>` (o `<CreditNote>`) nel namespace UBL 2.1 `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`.

## Correlati

- [Standard E-Fattura Attualmente Supportati](../../currently-supported-e-invoice-standards/)
- [Documenti Elettronici Supportati](./)
