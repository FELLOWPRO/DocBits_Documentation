---
description: Ondersteuning voor Deens OIOUBL 2.1 elektronisch document in DocBits
---

# 🇩🇰 Denemarken OIOUBL 2.1

| Eigenschap | Waarde |
|----------|-------|
| **Land / Regio** | Denemarken |
| **Documenttypen** | Factuur (Faktura), Creditnota |
| **Formaat** | XML (UBL 2.1) |
| **Standaard** | OIOUBL 2.1 (Offentlig Information Online UBL) |
| **Landinstelling** | `da_DK` |

OIOUBL (Offentlig Information Online UBL) is de Deense e-factuurstandaard gebaseerd op UBL 2.1. Deze is verplicht voor facturen aan Deense overheidsinstanties en wordt veel gebruikt in B2B-transacties. DocBits detecteert OIOUBL 2.1-documenten aan de hand van de aanwezigheid van `<cbc:CustomizationID>OIOUBL-2.1</cbc:CustomizationID>`. De profielidentificatie `urn:www.nesubl.eu:profiles:profile5:ver2.0` geeft het NES (Northern European Subset) factuurprofiel aan.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaard voorbeeld

<figure><img src="denmark-oioubl-preview.png" alt="Denemarken OIOUBL 2.1 factuurvoorbeeld in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een Deense OIOUBL 2.1-factuur (Faktura)</p></figcaption></figure>

## Veldtoewijzing

### Headervelden

| DocBits-veld | Bron-XML-element | Opmerkingen |
|---|---|---|
| `invoice_id` | `cbc:ID` | Factuurnummer |
| `invoice_date` | `cbc:IssueDate` | ISO 8601 uitgiftedatum |
| `due_date` | `cbc:DueDate` | Vervaldatum betaling |
| `invoice_type` | `cbc:InvoiceTypeCode` | UNCL 1001-code (380=Factuur, 381=Creditnota) |
| `currency` | `cbc:DocumentCurrencyCode` | Altijd `DKK` (Deense kroon) |
| `purchase_order` | `cac:OrderReference/cbc:ID` | Ordernummer van de koper |
| `buyer_reference` | `cbc:BuyerReference` | Interne referentie van de koper / EAN-locatienummer |
| `note` | `cbc:Note` | Vrije tekst betalingsinstructies of opmerkingen |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Nettobedrag excl. btw |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Totaal btw-bedrag (25% standaardtarief) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Totaalbedrag incl. btw |
| `tax_rate` | `cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` | Btw-tarief in % |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Bedrijfsnaam leverancier |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` | CVR-nummer (bijv. `DK12345678`) |
| `supplier_vat` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | BTW/CVR-nummer |
| `supplier_address` | `cac:AccountingSupplierParty/.../cbc:StreetName` | Straatnaam leverancier |
| `supplier_city` | `cac:AccountingSupplierParty/.../cbc:CityName` | Stad leverancier |
| `supplier_postal_code` | `cac:AccountingSupplierParty/.../cbc:PostalZone` | Postcode leverancier |
| `supplier_country` | `cac:AccountingSupplierParty/.../cbc:IdentificationCode` | ISO-landcode (`DK`) |
| `customer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Bedrijfsnaam klant |
| `customer_id` | `cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` | CVR-nummer |
| `customer_vat` | `cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | BTW/CVR-nummer |
| `customer_address` | `cac:AccountingCustomerParty/.../cbc:StreetName` | Straatnaam klant |
| `customer_city` | `cac:AccountingCustomerParty/.../cbc:CityName` | Stad klant |
| `customer_postal_code` | `cac:AccountingCustomerParty/.../cbc:PostalZone` | Postcode klant |
| `customer_country` | `cac:AccountingCustomerParty/.../cbc:IdentificationCode` | ISO-landcode (`DK`) |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Bankrekening / IBAN |
| `bic` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID` | BIC/SWIFT-code |

### Regelitemtabel (`INVOICE_TABLE`)

Rijpad: `cac:InvoiceLine`

| Kolom | Bron-XML-element | Opmerkingen |
|---|---|---|
| `POSITION` | `cbc:ID` | Regelvolgorde nummer |
| `DESCRIPTION` | `cac:Item/cbc:Name` | Artikelnaam / omschrijving |
| `QUANTITY` | `cbc:InvoicedQuantity` | Gefactureerde hoeveelheid |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Eenheidsprijs excl. btw |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Regeltotaal excl. btw |

## Classificatieregel

DocBits detecteert OIOUBL 2.1-documenten door het `CustomizationID`-element te matchen:

| Elektronisch documenttype | Patroon |
|--------------------------|---------|
| OIOUBL 2.1 | `<cbc:CustomizationID>OIOUBL-2\.1\s*</cbc:CustomizationID>` |

Het rootelement is `<Invoice>` (of `<CreditNote>`) in de UBL 2.1-namespace `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`.

## Gerelateerd

- [Momenteel ondersteunde e-factuurstandaarden](../../currently-supported-e-invoice-standards/)
- [Ondersteunde elektronische documenten](./)
