---
description: Ondersteuning voor elektronische documenten Finland Finvoice (1.3, 2.0, 2.01, 3.0) in DocBits
---

# 🇫🇮 Finland Finvoice

| Eigenschap | Waarde |
|----------|-------|
| **Land / Regio** | Finland |
| **Documenttypen** | Factuur (Lasku), Creditnota (Hyvityslasku) |
| **Formaat** | XML |
| **Standaard** | Finvoice 1.3 / 2.0 / 2.01 / 3.0 (Finance Finland / Finanssiala) |
| **Landinstelling** | `fi_FI` |

Finvoice is de e-factuurstandaard van de Finse banksector, ontwikkeld en beheerd door Finance Finland (Finanssiala ry). Het wordt gebruikt voor zowel B2B- als B2G-facturering en wordt verzonden via de Finse bankinfrastructuur. Het rootelement is `<Finvoice>` met een versie-specifieke naamruimte-URL. DocBits detecteert de versie via het `xmlns`-attribuut:

| Versie | Naamruimte-URL |
|---------|--------------|
| Finvoice 1.3 | `http://www.finvoice.fi/schema/finvoice13` |
| Finvoice 2.0 | `http://www.finvoice.fi/schema/finvoice20` |
| Finvoice 2.01 | `http://www.finvoice.fi/schema/finvoice201` |
| Finvoice 3.0 | `http://www.finvoice.fi/schema/finvoice30` |

Het Finse bedrijfs-ID-formaat (Y-tunnus) is `1234567-8` (7 cijfers + controlegetal), gebruikt als partij-identificator. Het btw-nummer heeft het voorvoegsel `FI` gevolgd door 8 cijfers (bijv. `FI12345678`). Datums worden gecodeerd in het formaat `CCYYMMDD`.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaardvoorbeeld

<figure><img src="finland-finvoice-preview.png" alt="Finland Finvoice 3.0 factuurvoorbeeld in DocBits"><figcaption><p>Standaardvoorbeeld in DocBits voor een Finland Finvoice 3.0-factuur (Lasku)</p></figcaption></figure>

## Veldtoewijzing

### Kopvelden

| DocBits-veld | Bron-XML-element | Opmerkingen |
|---|---|---|
| `invoice_id` | `InvoiceDetails/InvoiceNumber` | Factuurnummer |
| `invoice_date` | `InvoiceDetails/InvoiceDate` | Datum in formaat `CCYYMMDD`, omgezet naar ISO 8601 |
| `due_date` | `InvoiceDetails/PaymentTermsDetails/InvoiceDueDate` | Vervaldatum betaling (`CCYYMMDD`) |
| `invoice_type` | `InvoiceDetails/InvoiceTypeCode` | INV01=Factuur, CRE01=Creditnota |
| `currency` | `InvoiceDetails/InvoiceTotalVatExcludedAmount/@AmountCurrencyIdentifier` | Valutacode (doorgaans `EUR`) |
| `net_amount` | `InvoiceDetails/InvoiceTotalVatExcludedAmount` | Nettobedrag excl. btw |
| `tax_amount` | `InvoiceDetails/InvoiceTotalVatAmount` | Totaal btw-bedrag |
| `total_amount` | `InvoiceDetails/InvoiceTotalVatIncludedAmount` | Totaalbedrag incl. btw |
| `tax_rate` | `InvoiceDetails/VatSpecificationDetails/VatRatePercent` | Btw-tarief in % (standaard 25,5%) |
| `supplier_name` | `SellerPartyDetails/SellerOrganisationName` | Naam leveranciersbedrijf |
| `supplier_id` | `SellerPartyDetails/SellerPartyIdentifier` | Fins bedrijfs-ID (Y-tunnus, bijv. `1234567-8`) |
| `supplier_vat` | `SellerPartyDetails/SellerOrganisationTaxCode` | Btw-nummer (bijv. `FI12345678`) |
| `supplier_address` | `SellerPartyDetails/SellerPostalAddressDetails/SellerStreetName` | Leveranciersadres |
| `supplier_city` | `SellerPartyDetails/SellerPostalAddressDetails/SellerTownName` | Stad van leverancier |
| `supplier_postal_code` | `SellerPartyDetails/SellerPostalAddressDetails/SellerPostCodeIdentifier` | Postcode leverancier |
| `supplier_country` | `SellerPartyDetails/SellerPostalAddressDetails/CountryCode` | ISO-landcode (`FI`) |
| `buyer_name` | `BuyerPartyDetails/BuyerOrganisationName` | Naam kopersbedrijf |
| `buyer_id` | `BuyerPartyDetails/BuyerPartyIdentifier` | Fins bedrijfs-ID (Y-tunnus) |
| `buyer_address` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerStreetName` | Kopersadres |
| `buyer_city` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerTownName` | Stad van koper |
| `buyer_postal_code` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerPostCodeIdentifier` | Postcode koper |
| `buyer_country` | `BuyerPartyDetails/BuyerPostalAddressDetails/CountryCode` | ISO-landcode (`FI`) |
| `iban` | `EpiDetails/EpiBfiPartyDetails/EpiBfiIdentifier` | IBAN begunstigde (EPI-betalingsgegevens) |
| `bic` | `EpiDetails/EpiPaymentInstructionId` | BIC/SWIFT-code |
| `payment_terms` | `InvoiceDetails/PaymentTermsDetails/PaymentTermsFreeText` | Betalingsvoorwaarden in vrije tekst |

### Regeltabel (`INVOICE_TABLE`)

Rijpad: `InvoiceRow`

| Kolom | Bron-XML-element | Opmerkingen |
|---|---|---|
| `POSITION` | `InvoiceRow/ArticleIdentifier` | Artikel- / productcode |
| `DESCRIPTION` | `InvoiceRow/ArticleName` | Artikelnaam / -omschrijving |
| `QUANTITY` | `InvoiceRow/DeliveredQuantity` | Geleverde hoeveelheid |
| `UNIT` | `InvoiceRow/DeliveredQuantity/@QuantityUnitCode` | Eenheidscode (bijv. `KPL` = stuk) |
| `UNIT_PRICE` | `InvoiceRow/UnitPriceAmount` | Stukprijs excl. btw |
| `VAT_RATE` | `InvoiceRow/RowVatRatePercent` | Btw-tarief in % per regel |
| `VAT` | `InvoiceRow/RowVatAmount` | Btw-bedrag per regel |
| `NET_AMOUNT` | `InvoiceRow/RowAmount` | Regeltotaal excl. btw |

## Classificatieregels

DocBits detecteert Finvoice-documenten door het `xmlns`-attribuut op het rootelement `<Finvoice>` te matchen:

| Type elektronisch document | Patroon |
|--------------------------|---------|
| FINVOICE 1.3 | `xmlns` bevat `http://www.finvoice.fi/schema/finvoice13` |
| FINVOICE 2.0 | `xmlns` bevat `http://www.finvoice.fi/schema/finvoice20` (niet 2.01) |
| FINVOICE 2.01 | `xmlns` bevat `http://www.finvoice.fi/schema/finvoice201` |
| FINVOICE 3.0 | `xmlns` bevat `http://www.finvoice.fi/schema/finvoice30` |

Classificatie gebruikt het principe **eerste overeenkomst wint**, waarbij specifiekere patronen (2.01) voor het generieke 2.0 worden geëvalueerd.

## Gerelateerd

- [Momenteel ondersteunde e-factuurstandaarden](../../currently-supported-e-invoice-standards/)
- [Finland TEAPPSXML](./finland-teappsxml.md)
- [Ondersteunde elektronische documenten](./)
