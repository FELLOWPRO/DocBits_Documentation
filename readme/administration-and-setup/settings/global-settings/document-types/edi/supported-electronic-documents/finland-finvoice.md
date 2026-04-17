---
description: Obsługa elektronicznych dokumentów Finvoice z Finlandii (1.3, 2.0, 2.01, 3.0) w DocBits
---

# 🇫🇮 Finlandia Finvoice

| Właściwość | Wartość |
|----------|-------|
| **Kraj / Region** | Finlandia |
| **Typy dokumentów** | Faktura (Lasku), Nota kredytowa (Hyvityslasku) |
| **Format** | XML |
| **Standard** | Finvoice 1.3 / 2.0 / 2.01 / 3.0 (Finance Finland / Finanssiala) |
| **Ustawienia regionalne** | `fi_FI` |

Finvoice to standard e-fakturowania fińskiego sektora bankowego, opracowany i utrzymywany przez Finance Finland (Finanssiala ry). Jest używany zarówno do fakturowania B2B, jak i B2G i jest przesyłany za pośrednictwem fińskiej infrastruktury bankowej. Elementem głównym jest `<Finvoice>` z wersjonowanym adresem URL przestrzeni nazw. DocBits wykrywa wersję za pomocą atrybutu `xmlns`:

| Wersja | Adres URL przestrzeni nazw |
|---------|--------------|
| Finvoice 1.3 | `http://www.finvoice.fi/schema/finvoice13` |
| Finvoice 2.0 | `http://www.finvoice.fi/schema/finvoice20` |
| Finvoice 2.01 | `http://www.finvoice.fi/schema/finvoice201` |
| Finvoice 3.0 | `http://www.finvoice.fi/schema/finvoice30` |

Format fińskiego identyfikatora firmy (Y-tunnus) to `1234567-8` (7 cyfr + cyfra kontrolna), używany jako identyfikator strony. Numer VAT ma prefiks `FI` po którym następuje 8 cyfr (np. `FI12345678`). Daty są kodowane w formacie `CCYYMMDD`.

## Status obsługi

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="finland-finvoice-preview.png" alt="Podgląd faktury Finvoice 3.0 z Finlandii w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury Finvoice 3.0 z Finlandii (Lasku)</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | Źródłowy element XML | Uwagi |
|---|---|---|
| `invoice_id` | `InvoiceDetails/InvoiceNumber` | Numer faktury |
| `invoice_date` | `InvoiceDetails/InvoiceDate` | Data w formacie `CCYYMMDD`, konwertowana do ISO 8601 |
| `due_date` | `InvoiceDetails/PaymentTermsDetails/InvoiceDueDate` | Termin płatności (`CCYYMMDD`) |
| `invoice_type` | `InvoiceDetails/InvoiceTypeCode` | INV01=Faktura, CRE01=Nota kredytowa |
| `currency` | `InvoiceDetails/InvoiceTotalVatExcludedAmount/@AmountCurrencyIdentifier` | Kod waluty (zazwyczaj `EUR`) |
| `net_amount` | `InvoiceDetails/InvoiceTotalVatExcludedAmount` | Kwota netto bez VAT |
| `tax_amount` | `InvoiceDetails/InvoiceTotalVatAmount` | Łączna kwota VAT |
| `total_amount` | `InvoiceDetails/InvoiceTotalVatIncludedAmount` | Kwota całkowita z VAT |
| `tax_rate` | `InvoiceDetails/VatSpecificationDetails/VatRatePercent` | Stawka VAT w % (standardowo 25,5%) |
| `supplier_name` | `SellerPartyDetails/SellerOrganisationName` | Nazwa firmy dostawcy |
| `supplier_id` | `SellerPartyDetails/SellerPartyIdentifier` | Fiński identyfikator firmy (Y-tunnus, np. `1234567-8`) |
| `supplier_vat` | `SellerPartyDetails/SellerOrganisationTaxCode` | Numer VAT (np. `FI12345678`) |
| `supplier_address` | `SellerPartyDetails/SellerPostalAddressDetails/SellerStreetName` | Adres dostawcy |
| `supplier_city` | `SellerPartyDetails/SellerPostalAddressDetails/SellerTownName` | Miasto dostawcy |
| `supplier_postal_code` | `SellerPartyDetails/SellerPostalAddressDetails/SellerPostCodeIdentifier` | Kod pocztowy dostawcy |
| `supplier_country` | `SellerPartyDetails/SellerPostalAddressDetails/CountryCode` | Kod kraju ISO (`FI`) |
| `buyer_name` | `BuyerPartyDetails/BuyerOrganisationName` | Nazwa firmy kupującego |
| `buyer_id` | `BuyerPartyDetails/BuyerPartyIdentifier` | Fiński identyfikator firmy (Y-tunnus) |
| `buyer_address` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerStreetName` | Adres kupującego |
| `buyer_city` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerTownName` | Miasto kupującego |
| `buyer_postal_code` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerPostCodeIdentifier` | Kod pocztowy kupującego |
| `buyer_country` | `BuyerPartyDetails/BuyerPostalAddressDetails/CountryCode` | Kod kraju ISO (`FI`) |
| `iban` | `EpiDetails/EpiBfiPartyDetails/EpiBfiIdentifier` | IBAN odbiorcy (dane płatności EPI) |
| `bic` | `EpiDetails/EpiPaymentInstructionId` | Kod BIC/SWIFT |
| `payment_terms` | `InvoiceDetails/PaymentTermsDetails/PaymentTermsFreeText` | Warunki płatności w formie wolnego tekstu |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `InvoiceRow`

| Kolumna | Źródłowy element XML | Uwagi |
|---|---|---|
| `POSITION` | `InvoiceRow/ArticleIdentifier` | Kod artykułu / produktu |
| `DESCRIPTION` | `InvoiceRow/ArticleName` | Nazwa / opis artykułu |
| `QUANTITY` | `InvoiceRow/DeliveredQuantity` | Dostarczona ilość |
| `UNIT` | `InvoiceRow/DeliveredQuantity/@QuantityUnitCode` | Kod jednostki (np. `KPL` = sztuka) |
| `UNIT_PRICE` | `InvoiceRow/UnitPriceAmount` | Cena jednostkowa bez VAT |
| `VAT_RATE` | `InvoiceRow/RowVatRatePercent` | Stawka VAT w % na wiersz |
| `VAT` | `InvoiceRow/RowVatAmount` | Kwota VAT na wiersz |
| `NET_AMOUNT` | `InvoiceRow/RowAmount` | Suma wiersza bez VAT |

## Reguły klasyfikacji

DocBits wykrywa dokumenty Finvoice przez dopasowanie atrybutu `xmlns` na elemencie głównym `<Finvoice>`:

| Typ dokumentu elektronicznego | Wzorzec |
|--------------------------|---------|
| FINVOICE 1.3 | `xmlns` zawiera `http://www.finvoice.fi/schema/finvoice13` |
| FINVOICE 2.0 | `xmlns` zawiera `http://www.finvoice.fi/schema/finvoice20` (nie 2.01) |
| FINVOICE 2.01 | `xmlns` zawiera `http://www.finvoice.fi/schema/finvoice201` |
| FINVOICE 3.0 | `xmlns` zawiera `http://www.finvoice.fi/schema/finvoice30` |

Klasyfikacja stosuje zasadę **pierwszego dopasowania**, gdzie bardziej szczegółowe wzorce (2.01) są oceniane przed ogólnym 2.0.

## Powiązane

- [Aktualnie obsługiwane standardy e-fakturowania](../../currently-supported-e-invoice-standards/)
- [Finlandia TEAPPSXML](./finland-teappsxml.md)
- [Obsługiwane dokumenty elektroniczne](./)
