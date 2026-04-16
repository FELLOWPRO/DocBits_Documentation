---
description: Ondersteuning voor elektronisch document AUSTRIA EBINTERFACE 6.1 in DocBits
---

# 🇦🇹 AUSTRIA EBINTERFACE 6.1

| Eigenschap | Waarde |
|----------|-------|
| **Land/Regio** | Oostenrijk |
| **Documenttypen** | Factuur, Creditnota |
| **Formaat** | XML |
| **Standaard** | ebInterface 6.1 |
| **Locale** | `de_AT` |

ebInterface 6.1 is de nieuwste versie van de Oostenrijkse standaard voor elektronisch factureren. Het bevat bijgewerkte validatieregels, verbeterde ondersteuning voor creditnota's en uitgebreide compatibiliteit met het Peppol-netwerk voor grensoverschrijdende facturering. De namespace is `http://www.ebinterface.at/schema/6p1/`.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Preview | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaardvoorbeeld

<figure><img src="austria-ebinterface-preview.png" alt="Austria ebInterface 6.1 factuurvoorbeeld in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een AUSTRIA EBINTERFACE 6.1-factuur</p></figcaption></figure>

## Veldtoewijzing

### Koptekstvelden

| DocBits-veld | Bron XML-element | Opmerkingen |
|---|---|---|
| `invoice_id` | `eb:InvoiceNumber` | Factuurnummer |
| `invoice_date` | `eb:InvoiceDate` | ISO 8601-datum |
| `due_date` | `eb:PaymentConditions/eb:DueDate` | Betalingsvervaldatum |
| `delivery_date` | `eb:Delivery/eb:Date` | Leveringsdatum |
| `currency` | `@eb:InvoiceCurrency` | Root-attribuut, altijd `EUR` voor AT |
| `total_amount` | `eb:TotalGrossAmount` | Bruto totaal incl. btw |
| `net_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:TaxedAmount` | Netto belastbare grondslag |
| `tax_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:Amount` | Btw-bedrag |
| `purchase_order` | `eb:OrderReference/eb:OrderID` | Inkooporderreferentie |
| `payment_terms` | `eb:PaymentConditions/eb:Comment` | Vrije-tekst betalingsvoorwaarden |
| `supplier_name` | `eb:Biller/eb:Address/eb:Name` | Bedrijfsnaam factuuruitzender |
| `supplier_tax_id` | `eb:Biller/eb:VATIdentificationNumber` | Oostenrijkse UID (bijv. ATU12345678) |
| `supplier_street` | `eb:Biller/eb:Address/eb:Street` | Straat factuuruitzender |
| `supplier_city` | `eb:Biller/eb:Address/eb:Town` | Plaats factuuruitzender |
| `supplier_postal_code` | `eb:Biller/eb:Address/eb:ZIP` | Postcode factuuruitzender |
| `supplier_country` | `eb:Biller/eb:Address/eb:Country/@eb:CountryCode` | ISO-landcode |
| `supplier_email` | `eb:Biller/eb:Address/eb:Email` | E-mailadres factuuruitzender |
| `supplier_iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN factuuruitzender |
| `customer_name` | `eb:InvoiceRecipient/eb:Address/eb:Name` | Bedrijfsnaam ontvanger |
| `customer_tax_id` | `eb:InvoiceRecipient/eb:VATIdentificationNumber` | UID ontvanger |
| `customer_street` | `eb:InvoiceRecipient/eb:Address/eb:Street` | Straat ontvanger |
| `customer_city` | `eb:InvoiceRecipient/eb:Address/eb:Town` | Plaats ontvanger |
| `customer_postal_code` | `eb:InvoiceRecipient/eb:Address/eb:ZIP` | Postcode ontvanger |
| `customer_country` | `eb:InvoiceRecipient/eb:Address/eb:Country/@eb:CountryCode` | ISO-landcode |
| `iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | Betalings-IBAN |
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | Betalings-BIC/SWIFT |

### Regelitemtabel (`INVOICE_TABLE`)

Rijpad: `eb:Details/eb:ItemList/eb:ListLineItem`

| Kolom | Bron XML-element | Opmerkingen |
|---|---|---|
| `POSITION` | Sequentiele index | 1-gebaseerd regelnummer |
| `DESCRIPTION` | `eb:Description` | Product/dienstbeschrijving |
| `QUANTITY` | `eb:Quantity` | Numerieke hoeveelheid |
| `UNIT` | `eb:Quantity/@eb:Unit` | Eenheidscode (bijv. `STK` = stuk) |
| `UNIT_PRICE` | `eb:UnitPrice` | Eenheidsprijs excl. btw |
| `VAT_RATE` | `eb:VAT/eb:VATItem/eb:VATRate` | Btw-tarief in % |
| `VAT` | `eb:VAT/eb:VATItem/eb:TaxedAmount` | Btw-bedrag per regel |
| `NET_AMOUNT` | `eb:LineItemAmount` | Regeltotaal excl. btw |

## Classificatieregel

DocBits detecteert AUSTRIA EBINTERFACE 6.1-documenten aan de hand van de namespace-string:

```
http://www.ebinterface.at/schema/6p1/
```

## Gerelateerd

- [Ondersteunde elektronische documenten](./)
- [Austria ebInterface](austria-ebinterface.md)
- [Austria ebInterface 6.0](austria-ebinterface-6-0.md)