---
description: AUNZ PINT elektronisch document ondersteuning in DocBits
---

# 🇦🇺 AUNZ PINT

| Eigenschap | Waarde |
|----------|-------|
| **Land / Regio** | Australië / Nieuw-Zeeland |
| **Documenttypen** | Factuur, Creditnota |
| **Formaat** | UBL 2.1 XML |
| **Standaard** | PINT A-NZ (Peppol International Model for Australia-New Zealand) |
| **Locale** | `en_AU` |

AUNZ PINT is de Australische/Nieuw-Zeelandse implementatie van het Peppol International (PINT) factuurmodel. Het definieert een op UBL 2.1 gebaseerd factuurformaat afgestemd op de A-NZ regelgevende vereisten, waaronder ABN/NZBN-identificatie, GST-afhandeling en naleving van de A-NZ Peppol Authority-specificaties. DocBits ondersteunt zowel de standaard Factuur- en Creditnota-documenttypen onder het elektronische documenttype `PINT A-NZ`, als de Self-Billing-variant.

| Onderdeel | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaard voorbeeld

<figure><img src="aunz-pint-preview.png" alt="AUNZ PINT factuur voorbeeld in DocBits"><figcaption><p>Standaard DocBits voorbeeld voor een AUNZ PINT factuur</p></figcaption></figure>

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

## Classificatieregels

DocBits detecteert PINT A-NZ-documenten door het `CustomizationID`-element te matchen:

| Patroon | Regeltype | Elektronisch documenttype |
|---------|-----------|--------------------------|
| `urn:peppol.org:pint:billing-1@aunz` | STRING_CONTAINS | PINT A-NZ (Factuur) |
| `urn:peppol.org:pint:selfbilling-1@aunz` | STRING_CONTAINS | PINT A-NZ (Self-Billing Factuur) |

Beide patronen worden geclassificeerd onder het elektronische documenttype `PINT A-NZ`. Het rootelement is `<Invoice>` voor standaardfacturen en `<CreditNote>` voor creditnota's.

### A-NZ-specifieke functies

- **ABN/NZBN-identificatoren**: Gebruikt `schemeID="0151"` voor Australian Business Numbers en New Zealand Business Numbers
- **GST-belasting**: Gebruikt de belastingcategorie `S` (standaardtarief) met het GST-belastingschema
- **CustomizationID**: Moet het achtervoegsel `@aunz` bevatten om te worden geclassificeerd als PINT A-NZ (vs. globaal PINT)

## Zie ook

- [AUNZ PINT Self-Billing](aunz-pint-self-billing.md)
- [PINT A-NZ](pint-a-nz.md)
- [Ondersteunde elektronische documenten](./)
