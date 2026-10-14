---
description: Ondersteuning voor AUSTRIA EBINTERFACE 6.1 elektronisch document in DocBits
---

# 🇦🇹 AUSTRIA EBINTERFACE 6.1

| Eigenschap | Waarde |
|------------|--------|
| **Land / Regio** | Austria |
| **Documenttypen** | Invoice, Credit Note |
| **Formaat** | XML |
| **Standaard** | ebInterface 6.1 |
| **Taalinstelling** | `de_AT` |

ebInterface 6.1 is de nieuwste versie van de Oostenrijkse e-factuurstandaard. Het bevat bijgewerkte validatieregels, verbeterde ondersteuning voor creditnota's en verbeterde compatibiliteit met het Peppol-netwerk voor grensoverschrijdende facturering. De naamruimte is `http://www.ebinterface.at/schema/6p1/`.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorvertoning | ✅ Supported |
| Veldextractie | ✅ Supported |
| Transformatie | ✅ Supported |

## Standaard voorvertoning

<figure><img src="austria-ebinterface-preview.png" alt="Voorvertoning van Austria ebInterface 6.1 factuur in DocBits"><figcaption><p>Standaard DocBits-voorvertoning voor een AUSTRIA EBINTERFACE 6.1-factuur</p></figcaption></figure>

## Veldtoewijzing

### Headergebieden

| DocBits-veld | Bron-XML-element | Notities |
|---|---|---|
| `invoice_id` | `eb:InvoiceNumber` | Factuurnummer |
| `invoice_date` | `eb:InvoiceDate` | ISO 8601-datum |
| `due_date` | `eb:PaymentConditions/eb:DueDate` | Vervaldatum betaling |
| `delivery_date` | `eb:Delivery/eb:Date` | Leverdatum |
| `currency` | `@eb:InvoiceCurrency` | Hoofdattribuut, altijd `EUR` voor AT |
| `total_amount` | `eb:TotalGrossAmount` | Bruto totaal incl. btw |
| `net_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:TaxedAmount` | Netto belastbare grondslag |
| `tax_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:Amount` | Btw-bedrag |
| `purchase_order` | `eb:OrderReference/eb:OrderID` | Referentie inkooporder |
| `payment_terms` | `eb:PaymentConditions/eb:Comment` | Betalingsvoorwaarden in vrije tekst |
| `supplier_name` | `eb:Biller/eb:Address/eb:Name` | Naam facturerende onderneming |
| `supplier_tax_id` | `eb:Biller/eb:VATIdentificationNumber` | Oostenrijks UID (bijv. ATU12345678) |
| `supplier_street` | `eb:Biller/eb:Address/eb:Street` | Straatnaam facturerende partij |
| `supplier_city` | `eb:Biller/eb:Address/eb:Town` | Stad facturerende partij |
| `supplier_postal_code` | `eb:Biller/eb:Address/eb:ZIP` | Postcode facturerende partij |
| `supplier_country` | `eb:Biller/eb:Address/eb:Country/@eb:CountryCode` | ISO-landcode |
| `supplier_email` | `eb:Biller/eb:Address/eb:Email` | E-mailadres facturerende partij |
| `supplier_iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN facturerende partij |
| `customer_name` | `eb:InvoiceRecipient/eb:Address/eb:Name` | Naam ontvangend bedrijf |
| `customer_tax_id` | `eb:InvoiceRecipient/eb:VATIdentificationNumber` | UID ontvanger |
| `customer_street` | `eb:InvoiceRecipient/eb:Address/eb:Street` | Straatnaam ontvanger |
| `customer_city` | `eb:InvoiceRecipient/eb:Address/eb:Town` | Stad ontvanger |
| `customer_postal_code` | `eb:InvoiceRecipient/eb:Address/eb:ZIP` | Postcode ontvanger |
| `customer_country` | `eb:InvoiceRecipient/eb:Address/eb:Country/@eb:CountryCode` | ISO-landcode |
| `iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | Betaling IBAN |
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | Betaling BIC/SWIFT |

### Regelitemtabel (`INVOICE_TABLE`)

Regelpad: `eb:Details/eb:ItemList/eb:ListLineItem`

| Kolom | Bron-XML-element | Notities |
|---|---|---|
| `POSITION` | Opeenvolgend index | Regelnummer op basis van 1 |
| `DESCRIPTION` | `eb:Description` | Product-/dienstomschrijving |
| `QUANTITY` | `eb:Quantity` | Numerieke hoeveelheid |
| `UNIT` | `eb:Quantity/@eb:Unit` | Eenheidscode (bijv. `STK` = stuk) |
| `UNIT_PRICE` | `eb:UnitPrice` | Eenheidsprijs excl. btw |
| `VAT_RATE` | `eb:VAT/eb:VATItem/eb:VATRate` | Btw-tarief in % |
| `VAT` | `eb:VAT/eb:VATItem/eb:TaxedAmount` | Btw-bedrag per regel |
| `NET_AMOUNT` | `eb:LineItemAmount` | Regeltotaal excl. btw |

## Classificatieregel

DocBits detecteert AUSTRIA EBINTERFACE 6.1-documenten via de naamruimtestring:

```
http://www.ebinterface.at/schema/6p1/
```

## Gerelateerd

- [Ondersteunde elektronische documenten](./)
- [Austria ebInterface](austria-ebinterface.md)
- [Austria ebInterface 6.0](austria-ebinterface-6-0.md)
