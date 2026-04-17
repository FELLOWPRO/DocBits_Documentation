---
description: Obsługa elektronicznych dokumentów Denmark OIOUBL 2.1 w DocBits
---

# 🇩🇰 Denmark OIOUBL 2.1

| Właściwość | Wartość |
|----------|-------|
| **Kraj / Region** | Dania |
| **Typy dokumentów** | Faktura (Faktura), Nota kredytowa |
| **Format** | XML (UBL 2.1) |
| **Standard** | OIOUBL 2.1 (Offentlig Information Online UBL) |
| **Ustawienia regionalne** | `da_DK` |

OIOUBL (Offentlig Information Online UBL) to duński standard e-fakturowania oparty na UBL 2.1. Jest obowiązkowy dla faktur wystawianych duńskim podmiotom sektora publicznego i powszechnie stosowany w transakcjach B2B. DocBits wykrywa dokumenty OIOUBL 2.1 na podstawie obecności `<cbc:CustomizationID>OIOUBL-2.1</cbc:CustomizationID>`. Identyfikator profilu `urn:www.nesubl.eu:profiles:profile5:ver2.0` wskazuje profil faktury NES (Northern European Subset).

## Status wsparcia

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwany |
| Ekstrakcja pól | ✅ Obsługiwana |
| Transformacja | ✅ Obsługiwana |

## Domyślny podgląd

<figure><img src="denmark-oioubl-preview.png" alt="Podgląd faktury Denmark OIOUBL 2.1 w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury Denmark OIOUBL 2.1 (Faktura)</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | Źródłowy element XML | Uwagi |
|---|---|---|
| `invoice_id` | `cbc:ID` | Numer faktury |
| `invoice_date` | `cbc:IssueDate` | Data wystawienia w formacie ISO 8601 |
| `due_date` | `cbc:DueDate` | Termin płatności |
| `invoice_type` | `cbc:InvoiceTypeCode` | Kod UNCL 1001 (380=Faktura, 381=Nota kredytowa) |
| `currency` | `cbc:DocumentCurrencyCode` | Zawsze `DKK` (korona duńska) |
| `purchase_order` | `cac:OrderReference/cbc:ID` | Numer referencyjny zamówienia kupującego |
| `buyer_reference` | `cbc:BuyerReference` | Wewnętrzny numer referencyjny kupującego / numer lokalizacji EAN |
| `note` | `cbc:Note` | Dowolne instrukcje płatności lub notatki |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Kwota netto bez VAT |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Łączna kwota VAT (standardowa stawka 25%) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Kwota całkowita z VAT |
| `tax_rate` | `cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` | Stawka VAT w % |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Nazwa firmy dostawcy |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` | Numer CVR (np. `DK12345678`) |
| `supplier_vat` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Numer VAT/CVR |
| `supplier_address` | `cac:AccountingSupplierParty/.../cbc:StreetName` | Adres ulicy dostawcy |
| `supplier_city` | `cac:AccountingSupplierParty/.../cbc:CityName` | Miasto dostawcy |
| `supplier_postal_code` | `cac:AccountingSupplierParty/.../cbc:PostalZone` | Kod pocztowy dostawcy |
| `supplier_country` | `cac:AccountingSupplierParty/.../cbc:IdentificationCode` | Kod kraju ISO (`DK`) |
| `customer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Nazwa firmy klienta |
| `customer_id` | `cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` | Numer CVR |
| `customer_vat` | `cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Numer VAT/CVR |
| `customer_address` | `cac:AccountingCustomerParty/.../cbc:StreetName` | Adres ulicy klienta |
| `customer_city` | `cac:AccountingCustomerParty/.../cbc:CityName` | Miasto klienta |
| `customer_postal_code` | `cac:AccountingCustomerParty/.../cbc:PostalZone` | Kod pocztowy klienta |
| `customer_country` | `cac:AccountingCustomerParty/.../cbc:IdentificationCode` | Kod kraju ISO (`DK`) |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Numer rachunku bankowego / IBAN |
| `bic` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID` | Kod BIC/SWIFT |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `cac:InvoiceLine`

| Kolumna | Źródłowy element XML | Uwagi |
|---|---|---|
| `POSITION` | `cbc:ID` | Numer kolejny pozycji |
| `DESCRIPTION` | `cac:Item/cbc:Name` | Nazwa / opis towaru |
| `QUANTITY` | `cbc:InvoicedQuantity` | Zafakturowana ilość |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Cena jednostkowa bez VAT |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Suma wiersza bez VAT |

## Reguła klasyfikacji

DocBits wykrywa dokumenty OIOUBL 2.1 przez dopasowanie elementu `CustomizationID`:

| Typ dokumentu elektronicznego | Wzorzec |
|--------------------------|---------|
| OIOUBL 2.1 | `<cbc:CustomizationID>OIOUBL-2\.1\s*</cbc:CustomizationID>` |

Elementem głównym jest `<Invoice>` (lub `<CreditNote>`) w przestrzeni nazw UBL 2.1 `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`.

## Powiązane

- [Aktualnie obsługiwane standardy e-faktur](../../currently-supported-e-invoice-standards/)
- [Obsługiwane dokumenty elektroniczne](./)
