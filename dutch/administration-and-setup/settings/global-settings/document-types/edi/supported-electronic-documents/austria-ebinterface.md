---
description: Ondersteuning voor AUSTRIA EBINTERFACE elektronisch document in DocBits
---

# 🇦🇹 AUSTRIA EBINTERFACE

| Eigenschap | Waarde |
|------------|--------|
| **Land / Regio** | Austria |
| **Documenttypen** | Invoice, Credit Note |
| **Formaat** | XML |
| **Standaard** | ebInterface (versies 4.3 – 6.1) |
| **Taalinstelling** | `de_AT` |

ebInterface is de Oostenrijkse e-factuurstandaard die wordt beheerd door de Oostenrijkse Federale Economische Kamer (WKÖ — Wirtschaftskammer Österreich). Het definieert een gestructureerd XML-formaat voor elektronische facturen dat voornamelijk wordt gebruikt in B2G (business-to-government) en B2B-transacties in Oostenrijk. DocBits ondersteunt alle versies van 4.3 tot en met 6.1, elk geïdentificeerd door zijn eigen XML-naamruimte.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorvertoning | ✅ Supported |
| Veldextractie | ✅ Supported |
| Transformatie | ✅ Supported |

## Standaard voorvertoning

<figure><img src="austria-ebinterface-preview.png" alt="Voorvertoning van Austria ebInterface factuur in DocBits"><figcaption><p>Standaard DocBits-voorvertoning voor een AUSTRIA EBINTERFACE-factuur</p></figcaption></figure>

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
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | Betaling BIC |

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

## Classificatieregels

DocBits detecteert de ebInterface-versie door de XML-naamruimte te vergelijken:

| Versie | Naamruimte |
|--------|------------|
| ebInterface 4.3 | `http://www.ebinterface.at/schema/4p3/` |
| ebInterface 5.0 | `http://www.ebinterface.at/schema/5p0/` |
| ebInterface 6.0 | `http://www.ebinterface.at/schema/6p0/` |
| ebInterface 6.1 | `http://www.ebinterface.at/schema/6p1/` |

Alle versies delen het hoofdelement `<eb:Invoice>` met de bijbehorende naamruimte-URI.

## Gerelateerd

- [Austria ebInterface 6.0](austria-ebinterface-6-0.md)
- [Austria ebInterface 6.1](austria-ebinterface-6-1.md)
- [Ondersteunde elektronische documenten](./)
