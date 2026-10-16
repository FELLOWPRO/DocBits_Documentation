---
description: Obsługa dokumentów elektronicznych AUNZ PINT w DocBits
---

# 🇦🇺 AUNZ PINT

| Właściwość | Wartość |
|----------|-------|
| **Kraj / Region** | Australia / Nowa Zelandia |
| **Typy dokumentów** | Faktura, Nota kredytowa |
| **Format** | UBL 2.1 XML |
| **Standard** | PINT A-NZ (Peppol International Model for Australia-New Zealand) |
| **Locale** | `en_AU` |

AUNZ PINT to australijska/nowozelandzka implementacja międzynarodowego modelu fakturowania Peppol (PINT). Definiuje format faktury oparty na UBL 2.1 dostosowany do wymogów regulacyjnych A-NZ, w tym identyfikację ABN/NZBN, obsługę GST i zgodność ze specyfikacjami organu Peppol A-NZ. DocBits obsługuje standardowe typy dokumentów Faktura i Nota kredytowa pod elektronicznym typem dokumentu `PINT A-NZ`, a także wariant Self-Billing.

## Status wsparcia

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwany |
| Ekstrakcja pól | ✅ Obsługiwany |
| Transformacja | ✅ Obsługiwany |

## Domyślny podgląd

<figure><img src="aunz-pint-preview.png" alt="Podgląd faktury AUNZ PINT w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury AUNZ PINT</p></figcaption></figure>

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

## Reguły klasyfikacji

DocBits wykrywa dokumenty PINT A-NZ poprzez dopasowanie elementu `CustomizationID`:

| Wzorzec | Typ reguły | Elektroniczny typ dokumentu |
|---------|-----------|--------------------------|
| `urn:peppol.org:pint:billing-1@aunz` | STRING_CONTAINS | PINT A-NZ (Faktura) |
| `urn:peppol.org:pint:selfbilling-1@aunz` | STRING_CONTAINS | PINT A-NZ (Faktura self-billing) |

Oba wzorce są klasyfikowane pod elektronicznym typem dokumentu `PINT A-NZ`. Element główny to `<Invoice>` dla standardowych faktur i `<CreditNote>` dla not kredytowych.

### Funkcje specyficzne dla A-NZ

- **Identyfikatory ABN/NZBN**: Używa `schemeID="0151"` dla Australian Business Numbers i New Zealand Business Numbers
- **Podatek GST**: Używa kategorii podatkowej `S` (stawka standardowa) ze schematem podatkowym GST
- **CustomizationID**: Musi zawierać przyrostek `@aunz`, aby zostać sklasyfikowany jako PINT A-NZ (vs. globalny PINT)

## Zobacz także

- [AUNZ PINT Self-Billing](aunz-pint-self-billing.md)
- [PINT A-NZ](pint-a-nz.md)
- [Obsługiwane dokumenty elektroniczne](./)
