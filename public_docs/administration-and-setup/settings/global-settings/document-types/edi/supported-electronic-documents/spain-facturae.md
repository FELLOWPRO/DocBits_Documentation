---
description: Hiszpania Facturae (3.2, 3.2.1, 3.2.2) – Obsługa dokumentów elektronicznych w DocBits
---

# 🇪🇸 Hiszpania Facturae

| Właściwość | Wartość |
|------------|---------|
| **Kraj / Region** | Hiszpania |
| **Typy dokumentów** | Faktura (Factura), Nota kredytowa |
| **Format** | XML |
| **Standard** | Facturae 3.2 / 3.2.1 / 3.2.2 (Agencia Tributaria / AEAT) |
| **Ustawienia regionalne** | `es_ES` |

Facturae to obowiązkowy hiszpański standard fakturowania elektronicznego, zarządzany przez Agencia Estatal de Administración Tributaria (AEAT) i Ministerstwo Finansów. Jest wymagany do faktur kierowanych do hiszpańskich podmiotów sektora publicznego i szeroko stosowany w transakcjach B2B. Element główny to `<fe:Facturae>` z wersjonowanym adresem URL przestrzeni nazw. DocBits wykrywa wersję za pomocą atrybutu `xsi:schemaLocation`, który odwołuje się do jednego z oficjalnych adresów URL schematu:

| Wersja | Adres URL schematu |
|--------|-------------------|
| Facturae 3.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2.xml` |
| Facturae 3.2.1 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_1.xml` |
| Facturae 3.2.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_2.xml` |

## Status obsługi

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="spain-facturae-preview.png" alt="Podgląd faktury Hiszpania Facturae w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury Hiszpania Facturae 3.2.2</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | Źródłowy element XML | Uwagi |
|---|---|---|
| `invoice_id` | `Invoices/Invoice/InvoiceHeader/InvoiceNumber` | Numer faktury |
| `invoice_date` | `Invoices/Invoice/InvoiceIssueData/IssueDate` | Data wystawienia (RRRR-MM-DD) |
| `due_date` | `PaymentDetails/Installment/InstallmentDueDate` | Termin płatności |
| `invoice_type` | `Invoices/Invoice/InvoiceHeader/InvoiceDocumentType` | FC=Faktura, NC=Nota kredytowa |
| `currency` | `Invoices/Invoice/InvoiceIssueData/InvoiceCurrencyCode` | Zawsze `EUR` |
| `purchase_order` | `Invoices/Invoice/InvoiceHeader/ReceiverContractReference` | Referencja zamówienia / umowy kupującego |
| `net_amount` | `Invoices/Invoice/InvoiceTotals/TotalGrossAmountBeforeTaxes` | Kwota netto bez VAT |
| `tax_amount` | `Invoices/Invoice/InvoiceTotals/TotalTaxOutputs` | Łączna kwota VAT |
| `total_amount` | `Invoices/Invoice/InvoiceTotals/InvoiceTotal` | Kwota całkowita z VAT |
| `tax_rate` | `TaxesOutputs/Tax/TaxRate` | Stawka VAT w % (standardowa 21%) |
| `payment_terms` | `PaymentDetails/Installment/PaymentMeans` | Kod formy płatności |
| `supplier_name` | `Parties/SellerParty/LegalEntity/CorporateName` | Nazwa dostawcy |
| `supplier_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF (np. `ES12345678A`) |
| `supplier_tax_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | Hiszpański NIF lub CIF |
| `supplier_address` | `Parties/SellerParty/LegalEntity/AddressInSpain/Address` | Adres dostawcy |
| `supplier_city` | `Parties/SellerParty/LegalEntity/AddressInSpain/Town` | Miasto dostawcy |
| `supplier_postal_code` | `Parties/SellerParty/LegalEntity/AddressInSpain/PostCode` | Kod pocztowy dostawcy |
| `supplier_country` | `Parties/SellerParty/LegalEntity/AddressInSpain/CountryCode` | Kod kraju ISO (`ESP`) |
| `buyer_name` | `Parties/BuyerParty/LegalEntity/CorporateName` | Nazwa kupującego |
| `buyer_id` | `Parties/BuyerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF kupującego |
| `buyer_address` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Address` | Adres kupującego |
| `buyer_city` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Town` | Miasto kupującego |
| `buyer_postal_code` | `Parties/BuyerParty/LegalEntity/AddressInSpain/PostCode` | Kod pocztowy kupującego |
| `buyer_country` | `Parties/BuyerParty/LegalEntity/AddressInSpain/CountryCode` | Kod kraju ISO (`ESP`) |
| `iban` | `PaymentDetails/Installment/AccountToBeCredited/IBAN` | IBAN beneficjenta |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `Invoices/Invoice/Items/InvoiceLine`

| Kolumna | Źródłowy element XML | Uwagi |
|---|---|---|
| `POSITION` | `ItemDescription` | Sekwencja / opis jako identyfikator |
| `DESCRIPTION` | `ItemDescription` | Opis artykułu |
| `QUANTITY` | `Quantity` | Ilość na fakturze |
| `UNIT` | `UnitOfMeasure` | Jednostka miary (np. `units`) |
| `UNIT_PRICE` | `UnitPriceWithoutTax` | Cena jednostkowa bez VAT |
| `VAT_RATE` | `TaxesOutputs/Tax/TaxRate` | Stawka VAT w % (zazwyczaj 21%) |
| `VAT` | `TaxesOutputs/Tax/TaxAmount/TotalAmount` | Kwota VAT na pozycję |
| `NET_AMOUNT` | `TotalCost` | Suma pozycji bez VAT |

## Reguły klasyfikacji

DocBits wykrywa dokumenty Facturae, dopasowując atrybut `xsi:schemaLocation` na głównym elemencie `<fe:Facturae>`:

| Typ dokumentu elektronicznego | Wzorzec |
|------------------------------|---------|
| FACTURAE 3.2 | `xsi:schemaLocation` zawiera `Facturaev3_2.xml` (nie 3_2_1 ani 3_2_2) |
| FACTURAE 3.2.1 | `xsi:schemaLocation` zawiera `Facturaev3_2_1.xml` |
| FACTURAE 3.2.2 | `xsi:schemaLocation` zawiera `Facturaev3_2_2.xml` |

Element główny to `<fe:Facturae>` z przestrzenią nazw `http://www.facturae.es/Facturae/2014/v3.2.2/Facturae` (specyficzna dla wersji). Klasyfikacja używa zasady **pierwsze dopasowanie wygrywa**, przy czym bardziej szczegółowe wzorce (3.2.2, 3.2.1) są sprawdzane przed ogólnym 3.2.

## Powiązane

- [Aktualnie obsługiwane standardy e-faktur](../../currently-supported-e-invoice-standards/)
- [Obsługiwane dokumenty elektroniczne](./)
