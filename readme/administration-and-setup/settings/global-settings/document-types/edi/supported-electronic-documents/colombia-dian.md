---
description: Obsługa kolumbijskich dokumentów elektronicznych DIAN w DocBits (Factura Electrónica, Documento Soporte)
---

# 🇨🇴 Kolumbia DIAN

| Właściwość | Wartość |
|----------|-------|
| **Kraj / Region** | Colombia |
| **Typy dokumentów** | Faktura (Factura Electrónica), Nota kredytowa (Nota de Crédito), Documento Soporte |
| **Format** | XML (UBL 2.1) |
| **Standard** | DIAN 2.1 (Dirección de Impuestos y Aduanas Nacionales) |
| **Ustawienia regionalne** | `es_CO` |

Kolumbijski standard fakturowania elektronicznego jest regulowany przez **DIAN** (Dirección de Impuestos y Aduanas Nacionales). Opiera się na UBL 2.1 z rozszerzeniami specyficznymi dla DIAN (`sts:DianExtensions`). DocBits wykrywa dokumenty Colombia DIAN poprzez przestrzeń nazw DIAN i kieruje je na podstawie `CustomizationID`:

| CustomizationID | Typ dokumentu |
|-----------------|--------------|
| 10 | Factura Electrónica de Venta (FACTURA ELECTRONICA) |
| 20 | Nota de Crédito (Nota kredytowa) |
| 91 | Nota de Crédito por devolución |
| 92 | Nota de Débito |
| DS | Documento Soporte (DOCUMENTO SOPORTE) |

Identyfikator DIAN (**NIT** — Número de Identificación Tributaria) używa `schemeID="31"` w elemencie UBL `CompanyID`.

## Status obsługi

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="colombia-dian-preview.png" alt="Podgląd Colombia DIAN Factura Electrónica w DocBits"><figcaption><p>Domyślny podgląd DocBits dla COLOMBIA FACTURA ELECTRONICA (CustomizationID 10)</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | Źródłowy element XML | Uwagi |
|---|---|---|
| `invoice_id` | `cbc:ID` | Numer faktury z prefiksem (np. `SETP990000001`) |
| `invoice_date` | `cbc:IssueDate` | Data wystawienia (ISO 8601) |
| `due_date` | `cbc:DueDate` | Termin płatności |
| `currency` | `cbc:DocumentCurrencyCode` | Zawsze `COP` (peso kolumbijskie) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Łączna kwota do zapłaty z VAT |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Kwota netto bez VAT |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Łączna kwota VAT (standardowa stawka 19%) |
| `supplier_name` | `cac:AccountingSupplierParty//cbc:RegistrationName` | Nazwa prawna dostawcy |
| `supplier_id` | `cac:AccountingSupplierParty//cbc:CompanyID` | NIT dostawcy (schemeID=31) |
| `buyer_name` | `cac:AccountingCustomerParty//cbc:RegistrationName` | Nazwa prawna nabywcy |
| `buyer_id` | `cac:AccountingCustomerParty//cbc:CompanyID` | NIT nabywcy (schemeID=31) |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `cac:InvoiceLine` (lub `cac:CreditNoteLine`)

| Kolumna | Źródłowy element XML | Uwagi |
|---|---|---|
| `POSITION` | `cbc:ID` | Numer linii |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Opis produktu lub usługi |
| `QUANTITY` | `cbc:InvoicedQuantity` | Ilość z atrybutem kodu jednostki |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Cena jednostkowa bez VAT |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Suma linii bez VAT |

## Reguły klasyfikacji

DocBits wykrywa dokumenty Colombia DIAN na podstawie ciągu przestrzeni nazw DIAN:

| Typ dokumentu elektronicznego | Wzorzec |
|--------------------------|---------|
| COLOMBIA FACTURA ELECTRONICA | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `DianExtensions` |
| COLOMBIA DOCUMENTO SOPORTE | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `CustomizationID=DS` |

Element główny to `<Invoice>` (UBL 2.1) dla faktur, `<CreditNote>` dla not kredytowych. Wszystkie dokumenty zawierają blok `<sts:DianExtensions>` z danymi autoryzacji DIAN (`InvoiceAuthorization`, UUID `CUFE`/`CUDE`, kod QR).

## Powiązane

- [Aktualnie obsługiwane standardy faktur elektronicznych](../../currently-supported-e-invoice-standards/)
- [Obsługiwane dokumenty elektroniczne](./)
