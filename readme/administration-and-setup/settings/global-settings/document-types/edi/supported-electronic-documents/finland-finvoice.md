---
description: Podrška za elektronske dokumente Finska Finvoice (1.3, 2.0, 2.01, 3.0) u DocBits-u
---

# 🇫🇮 Finska Finvoice

| Svojstvo | Vrednost |
|----------|-------|
| **Zemlja / Region** | Finska |
| **Tipovi dokumenata** | Faktura (Lasku), Kreditna nota (Hyvityslasku) |
| **Format** | XML |
| **Standard** | Finvoice 1.3 / 2.0 / 2.01 / 3.0 (Finance Finland / Finanssiala) |
| **Lokalizacija** | `fi_FI` |

Finvoice je standard e-fakturisanja finskog bankarskog sektora, razvijen i održavan od strane Finance Finland (Finanssiala ry). Koristi se za B2B i B2G fakturisanje i prenosi se putem finske bankarske infrastrukture. Koreni element je `<Finvoice>` sa verzioniranim URL-om imenskog prostora. DocBits detektuje verziju putem atributa `xmlns`:

| Verzija | URL imenskog prostora |
|---------|--------------|
| Finvoice 1.3 | `http://www.finvoice.fi/schema/finvoice13` |
| Finvoice 2.0 | `http://www.finvoice.fi/schema/finvoice20` |
| Finvoice 2.01 | `http://www.finvoice.fi/schema/finvoice201` |
| Finvoice 3.0 | `http://www.finvoice.fi/schema/finvoice30` |

Format finskog poslovnog ID-ja (Y-tunnus) je `1234567-8` (7 cifara + kontrolna cifra), koji se koristi kao identifikator strane. PDV broj ima prefiks `FI` praćen sa 8 cifara (npr. `FI12345678`). Datumi su kodirani u formatu `CCYYMMDD`.

## Status podrške

| Komponenta | Status |
|-----------|--------|
| Pregled | ✅ Podržano |
| Ekstrakcija polja | ✅ Podržano |
| Transformacija | ✅ Podržano |

## Podrazumevani pregled

<figure><img src="finland-finvoice-preview.png" alt="Pregled fakture Finska Finvoice 3.0 u DocBits-u"><figcaption><p>Podrazumevani pregled u DocBits-u za finsku Finvoice 3.0 fakturu (Lasku)</p></figcaption></figure>

## Mapiranje polja

### Polja zaglavlja

| Polje DocBits | Izvorni XML element | Napomene |
|---|---|---|
| `invoice_id` | `InvoiceDetails/InvoiceNumber` | Broj fakture |
| `invoice_date` | `InvoiceDetails/InvoiceDate` | Datum u formatu `CCYYMMDD`, konvertovan u ISO 8601 |
| `due_date` | `InvoiceDetails/PaymentTermsDetails/InvoiceDueDate` | Rok plaćanja (`CCYYMMDD`) |
| `invoice_type` | `InvoiceDetails/InvoiceTypeCode` | INV01=Faktura, CRE01=Kreditna nota |
| `currency` | `InvoiceDetails/InvoiceTotalVatExcludedAmount/@AmountCurrencyIdentifier` | Kod valute (obično `EUR`) |
| `net_amount` | `InvoiceDetails/InvoiceTotalVatExcludedAmount` | Neto iznos bez PDV-a |
| `tax_amount` | `InvoiceDetails/InvoiceTotalVatAmount` | Ukupan iznos PDV-a |
| `total_amount` | `InvoiceDetails/InvoiceTotalVatIncludedAmount` | Ukupan iznos sa PDV-om |
| `tax_rate` | `InvoiceDetails/VatSpecificationDetails/VatRatePercent` | Stopa PDV-a u % (standardno 25,5%) |
| `supplier_name` | `SellerPartyDetails/SellerOrganisationName` | Naziv kompanije dobavljača |
| `supplier_id` | `SellerPartyDetails/SellerPartyIdentifier` | Finski poslovni ID (Y-tunnus, npr. `1234567-8`) |
| `supplier_vat` | `SellerPartyDetails/SellerOrganisationTaxCode` | PDV broj (npr. `FI12345678`) |
| `supplier_address` | `SellerPartyDetails/SellerPostalAddressDetails/SellerStreetName` | Adresa dobavljača |
| `supplier_city` | `SellerPartyDetails/SellerPostalAddressDetails/SellerTownName` | Grad dobavljača |
| `supplier_postal_code` | `SellerPartyDetails/SellerPostalAddressDetails/SellerPostCodeIdentifier` | Poštanski broj dobavljača |
| `supplier_country` | `SellerPartyDetails/SellerPostalAddressDetails/CountryCode` | ISO kod države (`FI`) |
| `buyer_name` | `BuyerPartyDetails/BuyerOrganisationName` | Naziv kompanije kupca |
| `buyer_id` | `BuyerPartyDetails/BuyerPartyIdentifier` | Finski poslovni ID (Y-tunnus) |
| `buyer_address` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerStreetName` | Adresa kupca |
| `buyer_city` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerTownName` | Grad kupca |
| `buyer_postal_code` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerPostCodeIdentifier` | Poštanski broj kupca |
| `buyer_country` | `BuyerPartyDetails/BuyerPostalAddressDetails/CountryCode` | ISO kod države (`FI`) |
| `iban` | `EpiDetails/EpiBfiPartyDetails/EpiBfiIdentifier` | IBAN primaoca (EPI detalji plaćanja) |
| `bic` | `EpiDetails/EpiPaymentInstructionId` | BIC/SWIFT kod |
| `payment_terms` | `InvoiceDetails/PaymentTermsDetails/PaymentTermsFreeText` | Uslovi plaćanja u slobodnom tekstu |

### Tabela stavki (`INVOICE_TABLE`)

Putanja reda: `InvoiceRow`

| Kolona | Izvorni XML element | Napomene |
|---|---|---|
| `POSITION` | `InvoiceRow/ArticleIdentifier` | Kod artikla / proizvoda |
| `DESCRIPTION` | `InvoiceRow/ArticleName` | Naziv / opis artikla |
| `QUANTITY` | `InvoiceRow/DeliveredQuantity` | Isporučena količina |
| `UNIT` | `InvoiceRow/DeliveredQuantity/@QuantityUnitCode` | Kod jedinice (npr. `KPL` = komad) |
| `UNIT_PRICE` | `InvoiceRow/UnitPriceAmount` | Jedinična cena bez PDV-a |
| `VAT_RATE` | `InvoiceRow/RowVatRatePercent` | Stopa PDV-a u % po redu |
| `VAT` | `InvoiceRow/RowVatAmount` | Iznos PDV-a po redu |
| `NET_AMOUNT` | `InvoiceRow/RowAmount` | Ukupan iznos reda bez PDV-a |

## Pravila klasifikacije

DocBits detektuje Finvoice dokumente podudaranjem atributa `xmlns` na korenom elementu `<Finvoice>`:

| Tip elektronskog dokumenta | Obrazac |
|--------------------------|---------|
| FINVOICE 1.3 | `xmlns` sadrži `http://www.finvoice.fi/schema/finvoice13` |
| FINVOICE 2.0 | `xmlns` sadrži `http://www.finvoice.fi/schema/finvoice20` (ne 2.01) |
| FINVOICE 2.01 | `xmlns` sadrži `http://www.finvoice.fi/schema/finvoice201` |
| FINVOICE 3.0 | `xmlns` sadrži `http://www.finvoice.fi/schema/finvoice30` |

Klasifikacija koristi princip **prvo podudaranje pobeđuje**, gde se specifičniji obrasci (2.01) evaluiraju pre generičkog 2.0.

## Srodni sadržaji

- [Trenutno podržani standardi e-fakturisanja](../../currently-supported-e-invoice-standards/)
- [Finska TEAPPSXML](./finland-teappsxml.md)
- [Podržani elektronski dokumenti](./)
