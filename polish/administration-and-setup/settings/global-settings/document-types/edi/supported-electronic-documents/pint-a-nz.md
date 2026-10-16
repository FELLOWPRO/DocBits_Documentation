---
description: Obsługa dokumentów elektronicznych PINT A-NZ w DocBits
---

# 🇦🇺 PINT A-NZ

| Właściwość | Wartość |
|----------|-------|
| **Kraj / Region** | Australia / Nowa Zelandia |
| **Typy dokumentów** | Faktura, Nota kredytowa |
| **Format** | UBL 2.1 XML |
| **Standard** | PINT A-NZ (Peppol International Model for Australia-New Zealand) |
| **Locale** | `en_AU` |

PINT A-NZ (Peppol International Model for Australia-New Zealand) to zlokalizowana specyfikacja fakturowania Peppol dla regionu Australii/Nowej Zelandii. Rozszerza globalny model PINT o reguły biznesowe specyficzne dla A-NZ, kategorie podatkowe (GST) i schematy identyfikacji (ABN, NZBN). To jest strona referencyjna techniczna z pełnym mapowaniem pól.

## Status wsparcia

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwany |
| Ekstrakcja pól | ✅ Obsługiwany |
| Transformacja | ✅ Obsługiwany |

## Domyślny podgląd

<figure><img src="aunz-pint-preview.png" alt="Podgląd faktury PINT A-NZ w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury PINT A-NZ</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | XPath źródłowy (UBL 2.1) | Uwagi |
|---|---|---|
| `invoice_id` | `cbc:ID` | Numer faktury |
| `invoice_date` | `cbc:IssueDate` | Data ISO 8601 |
| `due_date` | `cbc:DueDate` | Termin płatności |
| `currency` | `cbc:DocumentCurrencyCode` | Zazwyczaj `AUD` lub `NZD` |
| `total_amount` | `cbc:PayableAmount` (w `cac:LegalMonetaryTotal`) | Razem z GST |
| `net_amount` | `cbc:TaxExclusiveAmount` (w `cac:LegalMonetaryTotal`) | Podsuma bez GST |
| `tax_amount` | `cbc:TaxAmount` (w `cac:TaxTotal`) | Kwota GST |
| `purchase_order` | `cbc:BuyerReference` | Referencja zamówienia kupującego |
| `payment_terms` | `cbc:Note` (w `cac:PaymentTerms`) | Warunki płatności w dowolnym tekście |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Nazwa firmy dostawcy |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID` | ABN (schemeID 0151) |
| `supplier_tax_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | ABN lub numer GST |
| `supplier_street` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Ulica dostawcy |
| `supplier_city` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName` | Miasto dostawcy |
| `supplier_postal_code` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Kod pocztowy dostawcy |
| `supplier_country` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | Kod kraju ISO (`AU` lub `NZ`) |
| `buyer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Nazwa firmy kupującego |
| `buyer_id` | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID` | ABN/NZBN (schemeID 0151) |
| `buyer_street` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Ulica kupującego |
| `buyer_city` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName` | Miasto kupującego |
| `buyer_postal_code` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Kod pocztowy kupującego |
| `buyer_country` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | Kod kraju ISO |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Identyfikator konta płatności |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `cac:InvoiceLine`

| Kolumna | XPath źródłowy (UBL 2.1) | Uwagi |
|---|---|---|
| `POSITION` | `cbc:ID` | Numer wiersza |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Opis produktu/usługi |
| `QUANTITY` | `cbc:InvoicedQuantity` | Ilość (kod jednostki w `@unitCode`) |
| `UNIT` | `cbc:InvoicedQuantity/@unitCode` | Kod jednostki (np. `C62` = sztuka, `EA` = każda) |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Cena jednostkowa bez GST |
| `VAT_RATE` | `cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` | Stawka GST w % |
| `VAT` | *(obliczona z kwoty podatku)* | Kwota GST za wiersz |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Suma wiersza bez GST |

## Reguła klasyfikacji

DocBits wykrywa dokumenty PINT A-NZ poprzez dopasowanie elementu `CustomizationID`:

```
urn:peppol.org:pint:billing-1@aunz
```

Dla dokumentów self-billing wzorzec to:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Oba są klasyfikowane pod elektronicznym typem dokumentu `PINT A-NZ`.

## Zobacz także

- [AUNZ PINT](aunz-pint.md) — Przegląd i funkcje specyficzne dla A-NZ
- [AUNZ PINT Self-Billing](aunz-pint-self-billing.md) — Wariant self-billing
- [Obsługiwane dokumenty elektroniczne](./)
