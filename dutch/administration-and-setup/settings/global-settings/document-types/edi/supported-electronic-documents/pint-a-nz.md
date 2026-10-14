---
description: PINT A-NZ elektronisch document ondersteuning in DocBits
---

# 🇦🇺 PINT A-NZ

| Eigenschap | Waarde |
|----------|-------|
| **Land / Regio** | Australië / Nieuw-Zeeland |
| **Documenttypen** | Factuur, Creditnota |
| **Formaat** | UBL 2.1 XML |
| **Standaard** | PINT A-NZ (Peppol International Model for Australia-New Zealand) |
| **Locale** | `en_AU` |

PINT A-NZ (Peppol International Model for Australia-New Zealand) is de gelokaliseerde Peppol-factuurspecificatie voor de Australië/Nieuw-Zeeland-regio. Het breidt het globale PINT-model uit met A-NZ-specifieke bedrijfsregels, belastingcategorieën (GST) en identificatieschema's (ABN, NZBN). Dit is de technische referentiepagina met de volledige veldtoewijzing.

## Ondersteuningsstatus

| Onderdeel | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaard voorbeeld

<figure><img src="aunz-pint-preview.png" alt="PINT A-NZ factuur voorbeeld in DocBits"><figcaption><p>Standaard DocBits voorbeeld voor een PINT A-NZ factuur</p></figcaption></figure>

## Veldtoewijzing

### Koptekstvelden

| DocBits-veld | Bron-XPath (UBL 2.1) | Opmerkingen |
|---|---|---|
| `invoice_id` | `cbc:ID` | Factuurnummer |
| `invoice_date` | `cbc:IssueDate` | ISO 8601-datum |
| `due_date` | `cbc:DueDate` | Vervaldatum |
| `currency` | `cbc:DocumentCurrencyCode` | Meestal `AUD` of `NZD` |
| `total_amount` | `cbc:PayableAmount` (in `cac:LegalMonetaryTotal`) | Totaal incl. GST |
| `net_amount` | `cbc:TaxExclusiveAmount` (in `cac:LegalMonetaryTotal`) | Subtotaal excl. GST |
| `tax_amount` | `cbc:TaxAmount` (in `cac:TaxTotal`) | GST-bedrag |
| `purchase_order` | `cbc:BuyerReference` | Inkooporderreferentie koper |
| `payment_terms` | `cbc:Note` (in `cac:PaymentTerms`) | Betalingsvoorwaarden in vrije tekst |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Bedrijfsnaam leverancier |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID` | ABN (schemeID 0151) |
| `supplier_tax_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | ABN of GST-nummer |
| `supplier_street` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Straat leverancier |
| `supplier_city` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName` | Stad leverancier |
| `supplier_postal_code` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Postcode leverancier |
| `supplier_country` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | ISO-landcode (`AU` of `NZ`) |
| `buyer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Bedrijfsnaam koper |
| `buyer_id` | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID` | ABN/NZBN (schemeID 0151) |
| `buyer_street` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Straat koper |
| `buyer_city` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName` | Stad koper |
| `buyer_postal_code` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Postcode koper |
| `buyer_country` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | ISO-landcode |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Betalingsrekening-ID |

### Regeltabel (`INVOICE_TABLE`)

Regelpad: `cac:InvoiceLine`

| Kolom | Bron-XPath (UBL 2.1) | Opmerkingen |
|---|---|---|
| `POSITION` | `cbc:ID` | Regelnummer |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Product/dienstbeschrijving |
| `QUANTITY` | `cbc:InvoicedQuantity` | Hoeveelheid (eenheidcode in `@unitCode`) |
| `UNIT` | `cbc:InvoicedQuantity/@unitCode` | Eenheidcode (bijv. `C62` = stuk, `EA` = per stuk) |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Eenheidsprijs excl. GST |
| `VAT_RATE` | `cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` | GST-tarief in % |
| `VAT` | *(berekend uit belastingbedrag)* | GST-bedrag per regel |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Regeltotaal excl. GST |

## Classificatieregel

DocBits detecteert PINT A-NZ-documenten door het `CustomizationID`-element te matchen:

```
urn:peppol.org:pint:billing-1@aunz
```

Voor self-billing-documenten is het patroon:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Beide worden geclassificeerd onder het elektronische documenttype `PINT A-NZ`.

## Zie ook

- [AUNZ PINT](aunz-pint.md) — Overzicht en A-NZ-specifieke functies
- [AUNZ PINT Self-Billing](aunz-pint-self-billing.md) — Self-billing-variant
- [Ondersteunde elektronische documenten](./)
