---
description: Supporto documenti elettronici AUNZ PINT in DocBits
---

# 🇦🇺 AUNZ PINT

| Proprietà | Valore |
|----------|-------|
| **Paese / Regione** | Australia / Nuova Zelanda |
| **Tipi di documento** | Fattura, Nota di credito |
| **Formato** | UBL 2.1 XML |
| **Standard** | PINT A-NZ (Peppol International Model for Australia-New Zealand) |
| **Locale** | `en_AU` |

AUNZ PINT è l'implementazione australiana/neozelandese del modello di fatturazione Peppol International (PINT). Definisce un formato di fattura basato su UBL 2.1 adattato ai requisiti normativi A-NZ, inclusa l'identificazione ABN/NZBN, la gestione della GST e la conformità alle specifiche dell'autorità Peppol A-NZ. DocBits supporta sia i tipi di documento Fattura standard e Nota di credito sotto il tipo di documento elettronico `PINT A-NZ`, nonché la variante Self-Billing.

## Stato del supporto

| Componente | Stato |
|-----------|--------|
| Anteprima | ✅ Supportato |
| Estrazione campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Anteprima predefinita

<figure><img src="aunz-pint-preview.png" alt="Anteprima fattura AUNZ PINT in DocBits"><figcaption><p>Anteprima predefinita DocBits per una fattura AUNZ PINT</p></figcaption></figure>

## Mappatura dei campi

### Campi di intestazione

| Campo DocBits | XPath sorgente (UBL 2.1) | Note |
|---|---|---|
| `invoice_id` | `cbc:ID` | Numero fattura |
| `invoice_date` | `cbc:IssueDate` | Data ISO 8601 |
| `due_date` | `cbc:DueDate` | Data di scadenza |
| `currency` | `cbc:DocumentCurrencyCode` | Tipicamente `AUD` o `NZD` |
| `total_amount` | `cbc:PayableAmount` (in `cac:LegalMonetaryTotal`) | Totale incl. GST |
| `net_amount` | `cbc:TaxExclusiveAmount` (in `cac:LegalMonetaryTotal`) | Subtotale excl. GST |
| `tax_amount` | `cbc:TaxAmount` (in `cac:TaxTotal`) | Importo GST |
| `purchase_order` | `cbc:BuyerReference` | Riferimento ordine acquirente |
| `payment_terms` | `cbc:Note` (in `cac:PaymentTerms`) | Termini di pagamento in testo libero |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Nome società fornitore |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID` | ABN (schemeID 0151) |
| `supplier_tax_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | ABN o numero GST |
| `supplier_street` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Via del fornitore |
| `supplier_city` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName` | Città del fornitore |
| `supplier_postal_code` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | CAP del fornitore |
| `supplier_country` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | Codice paese ISO (`AU` o `NZ`) |
| `buyer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Nome società acquirente |
| `buyer_id` | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID` | ABN/NZBN (schemeID 0151) |
| `buyer_street` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Via dell'acquirente |
| `buyer_city` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName` | Città dell'acquirente |
| `buyer_postal_code` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | CAP dell'acquirente |
| `buyer_country` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | Codice paese ISO |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | ID conto di pagamento |

### Tabella delle righe (`INVOICE_TABLE`)

Percorso riga: `cac:InvoiceLine`

| Colonna | XPath sorgente (UBL 2.1) | Note |
|---|---|---|
| `POSITION` | `cbc:ID` | Numero riga |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Descrizione prodotto/servizio |
| `QUANTITY` | `cbc:InvoicedQuantity` | Quantità (codice unità in `@unitCode`) |
| `UNIT` | `cbc:InvoicedQuantity/@unitCode` | Codice unità (es. `C62` = pezzo, `EA` = ciascuno) |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Prezzo unitario excl. GST |
| `VAT_RATE` | `cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` | Aliquota GST in % |
| `VAT` | *(calcolato dall'importo tassa)* | Importo GST per riga |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Totale riga excl. GST |

## Regole di classificazione

DocBits rileva i documenti PINT A-NZ corrispondendo l'elemento `CustomizationID`:

| Pattern | Tipo di regola | Tipo di documento elettronico |
|---------|-----------|--------------------------|
| `urn:peppol.org:pint:billing-1@aunz` | STRING_CONTAINS | PINT A-NZ (Fattura) |
| `urn:peppol.org:pint:selfbilling-1@aunz` | STRING_CONTAINS | PINT A-NZ (Fattura di autofatturazione) |

Entrambi i pattern sono classificati sotto il tipo di documento elettronico `PINT A-NZ`. L'elemento radice è `<Invoice>` per le fatture standard e `<CreditNote>` per le note di credito.

### Funzionalità specifiche A-NZ

- **Identificatori ABN/NZBN**: Utilizza `schemeID="0151"` per gli Australian Business Numbers e i New Zealand Business Numbers
- **Tassa GST**: Utilizza la categoria fiscale `S` (aliquota standard) con lo schema fiscale GST
- **CustomizationID**: Deve contenere il suffisso `@aunz` per essere classificato come PINT A-NZ (vs. PINT globale)

## Vedi anche

- [AUNZ PINT Self-Billing](aunz-pint-self-billing.md)
- [PINT A-NZ](pint-a-nz.md)
- [Documenti elettronici supportati](./)
