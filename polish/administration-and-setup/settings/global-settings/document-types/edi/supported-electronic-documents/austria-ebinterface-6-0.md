---
description: Obsługa dokumentu elektronicznego AUSTRIA EBINTERFACE 6.0 w DocBits
---

# 🇦🇹 AUSTRIA EBINTERFACE 6.0

| Właściwość | Wartość |
|----------|-------|
| **Kraj/Region** | Austria |
| **Typy dokumentów** | Faktura, Nota kredytowa |
| **Format** | XML |
| **Standard** | ebInterface 6.0 |
| **Locale** | `de_AT` |

ebInterface 6.0 wprowadził zgodność z europejskim standardem EN 16931 przy jednoczesnym zachowaniu kompatybilności wstecznej z wymaganiami specyficznymi dla Austrii. Obsługuje strukturalną reprezentację danych faktury, w tym pozycje linii, szczegóły podatkowe i informacje o płatności. Przestrzeń nazw to `http://www.ebinterface.at/schema/6p0/`.

## Stan wsparcia

| Komponent | Status |
|-----------|--------|
| Podglad | ✅ Obslugiwany |
| Ekstrakcja pól | ✅ Obslugiwany |
| Transformacja | ✅ Obslugiwany |

## Domyślny podglad

<figure><img src="austria-ebinterface-preview.png" alt="Podglad faktury Austria ebInterface 6.0 w DocBits"><figcaption><p>Domyślny podglad DocBits dla faktury AUSTRIA EBINTERFACE 6.0</p></figcaption></figure>

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
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | BIC/SWIFT płatności |

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

DocBits wykrywa dokumenty AUSTRIA EBINTERFACE 6.0 na podstawie ciągu przestrzeni nazw:

```
http://www.ebinterface.at/schema/6p0/
```

## Powiązane

- [Obsługiwane dokumenty elektroniczne](./)
- [Austria ebInterface](austria-ebinterface.md)
- [Austria ebInterface 6.1](austria-ebinterface-6-1.md)