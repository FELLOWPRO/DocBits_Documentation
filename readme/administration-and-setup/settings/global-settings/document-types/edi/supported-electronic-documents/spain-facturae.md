---
description: Spanje Facturae (3.2, 3.2.1, 3.2.2) – Ondersteuning voor elektronische documenten in DocBits
---

# 🇪🇸 Spanje Facturae

| Eigenschap | Waarde |
|------------|--------|
| **Land / Regio** | Spanje |
| **Documenttypen** | Factuur (Factura), Creditnota |
| **Formaat** | XML |
| **Standaard** | Facturae 3.2 / 3.2.1 / 3.2.2 (Agencia Tributaria / AEAT) |
| **Locale** | `es_ES` |

Facturae is de verplichte Spaanse standaard voor elektronisch factureren, beheerd door de Agencia Estatal de Administración Tributaria (AEAT) en het Ministerie van Financiën. Het is verplicht voor facturen aan Spaanse overheidsinstanties en wordt veel gebruikt in B2B-transacties. Het hoofdelement is `<fe:Facturae>` met een versioned namespace-URL. DocBits detecteert de versie via het attribuut `xsi:schemaLocation`, dat verwijst naar een van de officiële schema-URL's:

| Versie | Schema-URL |
|--------|-----------|
| Facturae 3.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2.xml` |
| Facturae 3.2.1 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_1.xml` |
| Facturae 3.2.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_2.xml` |

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaardvoorbeeld

<figure><img src="spain-facturae-preview.png" alt="Voorbeeld Spanje Facturae factuur in DocBits"><figcaption><p>Standaardvoorbeeld in DocBits voor een Spanje Facturae 3.2.2 factuur</p></figcaption></figure>

## Veldtoewijzing

### Kopvelden

| DocBits-veld | XML-bronelement | Opmerkingen |
|---|---|---|
| `invoice_id` | `Invoices/Invoice/InvoiceHeader/InvoiceNumber` | Factuurnummer |
| `invoice_date` | `Invoices/Invoice/InvoiceIssueData/IssueDate` | Uitgiiftedatum (JJJJ-MM-DD) |
| `due_date` | `PaymentDetails/Installment/InstallmentDueDate` | Betalingsvervaldatum |
| `invoice_type` | `Invoices/Invoice/InvoiceHeader/InvoiceDocumentType` | FC=Factuur, NC=Creditnota |
| `currency` | `Invoices/Invoice/InvoiceIssueData/InvoiceCurrencyCode` | Altijd `EUR` |
| `purchase_order` | `Invoices/Invoice/InvoiceHeader/ReceiverContractReference` | Bestelreferentie / contractreferentie koper |
| `net_amount` | `Invoices/Invoice/InvoiceTotals/TotalGrossAmountBeforeTaxes` | Nettobedrag excl. btw |
| `tax_amount` | `Invoices/Invoice/InvoiceTotals/TotalTaxOutputs` | Totaal btw-bedrag |
| `total_amount` | `Invoices/Invoice/InvoiceTotals/InvoiceTotal` | Totaalbedrag incl. btw |
| `tax_rate` | `TaxesOutputs/Tax/TaxRate` | Btw-tarief in % (standaard 21%) |
| `payment_terms` | `PaymentDetails/Installment/PaymentMeans` | Code betalingsmiddel |
| `supplier_name` | `Parties/SellerParty/LegalEntity/CorporateName` | Naam leverancier |
| `supplier_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF (bijv. `ES12345678A`) |
| `supplier_tax_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | Spaans NIF of CIF btw-nummer |
| `supplier_address` | `Parties/SellerParty/LegalEntity/AddressInSpain/Address` | Adres leverancier |
| `supplier_city` | `Parties/SellerParty/LegalEntity/AddressInSpain/Town` | Stad leverancier |
| `supplier_postal_code` | `Parties/SellerParty/LegalEntity/AddressInSpain/PostCode` | Postcode leverancier |
| `supplier_country` | `Parties/SellerParty/LegalEntity/AddressInSpain/CountryCode` | ISO-landcode (`ESP`) |
| `buyer_name` | `Parties/BuyerParty/LegalEntity/CorporateName` | Naam koper |
| `buyer_id` | `Parties/BuyerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF koper |
| `buyer_address` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Address` | Adres koper |
| `buyer_city` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Town` | Stad koper |
| `buyer_postal_code` | `Parties/BuyerParty/LegalEntity/AddressInSpain/PostCode` | Postcode koper |
| `buyer_country` | `Parties/BuyerParty/LegalEntity/AddressInSpain/CountryCode` | ISO-landcode (`ESP`) |
| `iban` | `PaymentDetails/Installment/AccountToBeCredited/IBAN` | IBAN begunstigde |

### Regeltabel (`INVOICE_TABLE`)

Regelpad: `Invoices/Invoice/Items/InvoiceLine`

| Kolom | XML-bronelement | Opmerkingen |
|---|---|---|
| `POSITION` | `ItemDescription` | Regelvolgnummer / beschrijving als identifier |
| `DESCRIPTION` | `ItemDescription` | Artikelomschrijving |
| `QUANTITY` | `Quantity` | Gefactureerde hoeveelheid |
| `UNIT` | `UnitOfMeasure` | Meeteenheid (bijv. `units`) |
| `UNIT_PRICE` | `UnitPriceWithoutTax` | Eenheidsprijs excl. btw |
| `VAT_RATE` | `TaxesOutputs/Tax/TaxRate` | Btw-tarief in % (typisch 21%) |
| `VAT` | `TaxesOutputs/Tax/TaxAmount/TotalAmount` | Btw-bedrag per regel |
| `NET_AMOUNT` | `TotalCost` | Regeltotaal excl. btw |

## Classificatieregels

DocBits detecteert Facturae-documenten door het `xsi:schemaLocation`-attribuut op het hoofdelement `<fe:Facturae>` te matchen:

| Type elektronisch document | Patroon |
|--------------------------|---------|
| FACTURAE 3.2 | `xsi:schemaLocation` bevat `Facturaev3_2.xml` (niet 3_2_1 of 3_2_2) |
| FACTURAE 3.2.1 | `xsi:schemaLocation` bevat `Facturaev3_2_1.xml` |
| FACTURAE 3.2.2 | `xsi:schemaLocation` bevat `Facturaev3_2_2.xml` |

Het hoofdelement is `<fe:Facturae>` met namespace `http://www.facturae.es/Facturae/2014/v3.2.2/Facturae` (versiespecifiek). Classificatie gebruikt het principe **eerste overeenkomst wint**, waarbij meer specifieke patronen (3.2.2, 3.2.1) vóór het generieke 3.2 worden geëvalueerd.

## Gerelateerd

- [Momenteel ondersteunde e-factuurstandaarden](../../currently-supported-e-invoice-standards/)
- [Ondersteunde elektronische documenten](./)
