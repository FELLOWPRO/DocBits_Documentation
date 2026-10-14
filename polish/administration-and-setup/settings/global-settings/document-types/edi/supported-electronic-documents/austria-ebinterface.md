---
description: Obsługa dokumentu elektronicznego AUSTRIA EBINTERFACE w DocBits
---

# 🇦🇹 AUSTRIA EBINTERFACE

| Właściwość | Wartość |
|----------|-------|
| **Kraj/Region** | Austria |
| **Typy dokumentów** | Faktura, Nota kredytowa |
| **Format** | XML |
| **Standard** | ebInterface (wersje 4.3 – 6.1) |
| **Locale** | `de_AT` |

ebInterface to austriacki standard e-fakturowania utrzymywany przez Austriacką Federalną Izbę Gospodarczą (WKO — Wirtschaftskammer Osterreich). Definiuje strukturalny format XML dla faktur elektronicznych uzywanych glownie w transakcjach B2G (biznes-rzad) i B2B w Austrii. DocBits obsluguje wszystkie wersje od 4.3 do 6.1, z kazda identyfikowana przez wlasna przestrzen nazw XML.

## Stan wsparcia

| Komponent | Status |
|-----------|--------|
| Podglad | ✅ Obslugiwany |
| Ekstrakcja pol | ✅ Obslugiwany |
| Transformacja | ✅ Obslugiwany |

## Domyślny podglad

<figure><img src="austria-ebinterface-preview.png" alt="Podglad faktury Austria ebInterface w DocBits"><figcaption><p>Domyślny podglad DocBits dla faktury AUSTRIA EBINTERFACE</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | Element źródłowy XML | Uwagi |
|---|---|---|
| `invoice_id` | `eb:InvoiceNumber` | Numer faktury |
| `invoice_date` | `eb:InvoiceDate` | Data ISO 8601 |
| `due_date` | `eb:PaymentConditions/eb:DueDate` | Termin płatności |
| `delivery_date` | `eb:Delivery/eb:Date` | Data dostawy |
| `currency` | `@eb:InvoiceCurrency` | Atrybut główny, zawsze `EUR` dla AT |
| `total_amount` | `eb:TotalGrossAmount` | Kwota brutto z VAT |
| `net_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:TaxedAmount` | Podstawa netto opodatkowana |
| `tax_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:Amount` | Kwota VAT |
| `purchase_order` | `eb:OrderReference/eb:OrderID` | Referencja zamówienia zakupu |
| `payment_terms` | `eb:PaymentConditions/eb:Comment` | Warunki płatności (tekst wolny) |
| `supplier_name` | `eb:Biller/eb:Address/eb:Name` | Nazwa firmy wystawcy |
| `supplier_tax_id` | `eb:Biller/eb:VATIdentificationNumber` | Austriacki UID (np. ATU12345678) |
| `supplier_street` | `eb:Biller/eb:Address/eb:Street` | Ulica wystawcy |
| `supplier_city` | `eb:Biller/eb:Address/eb:Town` | Miasto wystawcy |
| `supplier_postal_code` | `eb:Biller/eb:Address/eb:ZIP` | Kod pocztowy wystawcy |
| `supplier_country` | `eb:Biller/eb:Address/eb:Country/@eb:CountryCode` | Kod kraju ISO |
| `supplier_email` | `eb:Biller/eb:Address/eb:Email` | E-mail wystawcy |
| `supplier_iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN wystawcy |
| `customer_name` | `eb:InvoiceRecipient/eb:Address/eb:Name` | Nazwa firmy odbiorcy |
| `customer_tax_id` | `eb:InvoiceRecipient/eb:VATIdentificationNumber` | UID odbiorcy |
| `customer_street` | `eb:InvoiceRecipient/eb:Address/eb:Street` | Ulica odbiorcy |
| `customer_city` | `eb:InvoiceRecipient/eb:Address/eb:Town` | Miasto odbiorcy |
| `customer_postal_code` | `eb:InvoiceRecipient/eb:Address/eb:ZIP` | Kod pocztowy odbiorcy |
| `customer_country` | `eb:InvoiceRecipient/eb:Address/eb:Country/@eb:CountryCode` | Kod kraju ISO |
| `iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN płatności |
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | BIC płatności |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wierszy: `eb:Details/eb:ItemList/eb:ListLineItem`

| Kolumna | Element źródłowy XML | Uwagi |
|---|---|---|
| `POSITION` | Indeks sekwencyjny | Numer wiersza od 1 |
| `DESCRIPTION` | `eb:Description` | Opis produktu/usługi |
| `QUANTITY` | `eb:Quantity` | Ilość numeryczna |
| `UNIT` | `eb:Quantity/@eb:Unit` | Kod jednostki (np. `STK` = sztuka) |
| `UNIT_PRICE` | `eb:UnitPrice` | Cena jednostkowa bez VAT |
| `VAT_RATE` | `eb:VAT/eb:VATItem/eb:VATRate` | Stawka VAT w % |
| `VAT` | `eb:VAT/eb:VATItem/eb:TaxedAmount` | Kwota VAT na wiersz |
| `NET_AMOUNT` | `eb:LineItemAmount` | Wartość wiersza bez VAT |

## Reguła klasyfikacji

DocBits wykrywa wersję ebInterface poprzez dopasowanie przestrzeni nazw XML:

| Wersja | Przestrzeń nazw |
|---------|-----------|
| ebInterface 4.3 | `http://www.ebinterface.at/schema/4p3/` |
| ebInterface 5.0 | `http://www.ebinterface.at/schema/5p0/` |
| ebInterface 6.0 | `http://www.ebinterface.at/schema/6p0/` |
| ebInterface 6.1 | `http://www.ebinterface.at/schema/6p1/` |

Wszystkie wersje współdzielą element główny `<eb:Invoice>` z odpowiednim URI przestrzeni nazw.

## Powiązane

- [Austria ebInterface 6.0](austria-ebinterface-6-0.md)
- [Austria ebInterface 6.1](austria-ebinterface-6-1.md)
- [Obsługiwane dokumenty elektroniczne](./)