---
description: Obsługa elektronicznych dokumentów TEAPPSXML z Finlandii w DocBits
---

# 🇫🇮 Finlandia TEAPPSXML

| Właściwość | Wartość |
|----------|-------|
| **Kraj / Region** | Finlandia |
| **Typy dokumentów** | Faktura, Nota kredytowa |
| **Format** | XML |
| **Standard** | TEAPPSXML 3.0 (Tieto / Fiński sektor bankowy) |
| **Ustawienia regionalne** | `fi_FI` |

TEAPPSXML (Tietotekniikan ja viestinnän toimiala) to fiński standard faktury elektronicznej stosowany głównie w sektorze bankowym i finansowym. Elementem głównym jest `<TEAPPSXML>` z przestrzenią nazw `urn:TEAPPSXML:3.0`. DocBits wykrywa dokumenty TEAPPSXML przez obecność `xmlns="urn:TEAPPSXML:"` w elemencie głównym.

Format TEAPPSXML używa nazw elementów pisanych wielkimi literami i płaskiej struktury z oddzielnymi sekcjami `<SENDER>`, `<RECEIVER>`, `<INVOICE>` i `<PAYMENTINFO>`. Format fińskiego identyfikatora firmy (Y-tunnus) to `1234567-8`, a numery VAT używają prefiksu `FI` (np. `FI12345678`).

## Status obsługi

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="finland-teappsxml-preview.png" alt="Podgląd faktury TEAPPSXML z Finlandii w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury TEAPPSXML z Finlandii</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | Źródłowy element XML | Uwagi |
|---|---|---|
| `invoice_id` | `INVOICE/INVOICENUMBER` | Numer faktury |
| `invoice_date` | `INVOICE/INVOICEDATE` | Data wystawienia (RRRR-MM-DD) |
| `due_date` | `INVOICE/DUEDATE` | Termin płatności (RRRR-MM-DD) |
| `invoice_type` | `INVOICE/INVOICE_TYPE` | Typ wiadomości (INVOICE) |
| `currency` | `INVOICE/CURRENCY` | Kod waluty (zazwyczaj `EUR`) |
| `purchase_order` | `INVOICE/REFERENCENUMBER` | Numer referencyjny płatności |
| `payment_reference` | `INVOICE/REFERENCENUMBER` | Fińska referencja płatności (viitenumero) |
| `net_amount` | `INVOICE/TOTALVATEXCLUDED` | Kwota netto bez VAT |
| `tax_amount` | `INVOICE/TOTALVAT` | Łączna kwota VAT |
| `total_amount` | `INVOICE/TOTALAMOUNT` | Kwota całkowita z VAT |
| `payment_terms` | `INVOICE/PAYMENT_TERMS` | Metoda płatności (np. `BANKTRANSFER`) |
| `supplier_name` | `SENDER/NAME` | Nazwa firmy nadawcy |
| `supplier_id` | `SENDER/ID` | Fiński identyfikator firmy (Y-tunnus, np. `1234567-8`) |
| `supplier_tax_id` | `SENDER/VATNUMBER` | Numer VAT (np. `FI12345678`) |
| `supplier_address` | `SENDER/ADDRESS/STREET` | Adres nadawcy |
| `supplier_city` | `SENDER/ADDRESS/CITY` | Miasto nadawcy |
| `supplier_postal_code` | `SENDER/ADDRESS/POSTCODE` | Kod pocztowy nadawcy |
| `supplier_country` | `SENDER/ADDRESS/COUNTRY` | Kod kraju ISO (`FI`) |
| `supplier_bic` | `SENDER/BANK/BIC` | Kod BIC banku nadawcy |
| `buyer_name` | `INVOICE/BUYER/NAME` | Nazwa firmy kupującego |
| `buyer_id` | `INVOICE/BUYER/ID` | Fiński identyfikator firmy kupującego |
| `buyer_address` | `INVOICE/BUYER/ADDRESS_LINE_1` | Adres kupującego |
| `buyer_city` | `INVOICE/BUYER/CITY` | Miasto kupującego |
| `buyer_postal_code` | `INVOICE/BUYER/POSTAL_CODE` | Kod pocztowy kupującego |
| `buyer_country` | `INVOICE/BUYER/COUNTRY` | Kod kraju ISO (`FI`) |
| `iban` | `PAYMENTINFO/BENEFICIARYACCOUNT/IBAN` | IBAN odbiorcy |
| `bic` | `PAYMENTINFO/BENEFICIARYACCOUNT/BIC` | Kod BIC odbiorcy |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `INVOICE/LINES/LINE`

| Kolumna | Źródłowy element XML | Uwagi |
|---|---|---|
| `POSITION` | `LINENUMBER` | Numer kolejny wiersza |
| `DESCRIPTION` | `ARTICLENAME` | Nazwa / opis artykułu |
| `QUANTITY` | `QUANTITY` | Zafakturowana ilość |
| `UNIT` | `UNIT` | Jednostka miary (np. `KPL` = sztuka) |
| `UNIT_PRICE` | `UNITPRICE` | Cena jednostkowa bez VAT |
| `VAT_RATE` | `VATRATE` | Stawka VAT w % (standardowo 25,5%) |
| `VAT` | Wyliczone | Kwota VAT na wiersz |
| `NET_AMOUNT` | `LINEAMOUNT` | Suma wiersza bez VAT |

## Reguła klasyfikacji

DocBits wykrywa dokumenty TEAPPSXML przez dopasowanie atrybutu `xmlns` na elemencie głównym `<TEAPPSXML>`:

| Typ dokumentu elektronicznego | Wzorzec |
|--------------------------|---------|
| TEAPPSXML | `xmlns` zawiera `urn:TEAPPSXML:` |

## Powiązane

- [Aktualnie obsługiwane standardy e-fakturowania](../../currently-supported-e-invoice-standards/)
- [Finlandia Finvoice](./finland-finvoice.md)
- [Obsługiwane dokumenty elektroniczne](./)
