---
description: Obsługa indyjskiej faktury elektronicznej GST w DocBits
---

# 🇮🇳 India GST E-Invoice

| Właściwość | Wartość |
|----------|-------|
| **Kraj / Region** | Indie |
| **Typy dokumentów** | Faktura (INV), Nota kredytowa (CRN), Nota debetowa (DBN) |
| **Format** | XML (`<SignedInvoice>`) |
| **Standard** | GST E-Invoice (GSTN Invoice Registration Portal) |
| **Locale** | `en_IN` |

Indyjska faktura elektroniczna GST jest obowiązkowym standardem fakturowania elektronicznego w ramach indyjskiego systemu GST (Goods and Services Tax), obsługiwanym przez GSTN (GST Network). Firmy przekraczające określony próg obrotów muszą generować e-faktury za pośrednictwem portalu IRP (Invoice Registration Portal), który podpisuje fakturę i zwraca **IRN** (Invoice Reference Number — 64-znakowy hash SHA-256) oraz kod QR.

DocBits wykrywa dokumenty GST E-Invoice przez obecność `<SignedInvoice>` jako elementu głównego. Format obejmuje trzy komponenty podatkowe GST:

| Komponent podatkowy | Opis |
|--------------|-------------|
| IGST | Zintegrowany GST — stosowany w transakcjach między stanami |
| CGST | Centralny GST — stosowany w transakcjach wewnątrz stanu (komponent centralny) |
| SGST | Stanowy GST — stosowany w transakcjach wewnątrz stanu (komponent stanowy) |

Identyfikatorem podatnika jest **GSTIN** (Goods and Services Tax Identification Number), 15-znakowy kod alfanumeryczny w formacie `29AABCU9603R1ZM` (2-cyfrowy kod stanu + 10-cyfrowy PAN + numer podmiotu + cyfra kontrolna). Daty używają formatu `DD/MM/RRRR`.

## Status wsparcia

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwany |
| Ekstrakcja pól | ✅ Obsługiwany |
| Transformacja | ✅ Obsługiwany |

## Domyślny podgląd

<figure><img src="india-gst-e-invoice-preview.png" alt="India GST E-Invoice preview in DocBits"><figcaption><p>Domyślny podgląd DocBits dla indyjskiej faktury elektronicznej GST</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | Źródłowy element XML | Uwagi |
|---|---|---|
| `invoice_id` | `Invoice/DocDtls/No` | Numer faktury |
| `invoice_date` | `Invoice/DocDtls/Dt` | Data wystawienia (`DD/MM/RRRR`) |
| `invoice_type` | `Invoice/DocDtls/Typ` | INV=Faktura, CRN=Nota kredytowa, DBN=Nota debetowa |
| `currency` | Stałe: `INR` | Zawsze rupia indyjska |
| `net_amount` | `Invoice/ValDtls/AssVal` | Wartość podlegająca opodatkowaniu |
| `tax_amount` | `Invoice/ValDtls/IgstVal` + `CgstVal` + `SgstVal` | Łączna kwota GST |
| `total_amount` | `Invoice/ValDtls/TotInvVal` | Całkowita wartość faktury z GST |
| `igst_amount` | `Invoice/ValDtls/IgstVal` | Kwota zintegrowanego GST |
| `cgst_amount` | `Invoice/ValDtls/CgstVal` | Kwota centralnego GST |
| `sgst_amount` | `Invoice/ValDtls/SgstVal` | Kwota stanowego GST |
| `cess_amount` | `Invoice/ValDtls/CesVal` | Kwota cess (jeśli dotyczy) |
| `supplier_name` | `Invoice/SellerDtls/LglNm` | Prawna nazwa sprzedawcy |
| `supplier_id` | `Invoice/SellerDtls/Gstin` | GSTIN sprzedawcy (15 znaków, np. `29AABCU9603R1ZM`) |
| `supplier_trade_name` | `Invoice/SellerDtls/TrdNm` | Nazwa handlowa sprzedawcy |
| `supplier_address` | `Invoice/SellerDtls/Addr1` | Adres sprzedawcy wiersz 1 |
| `supplier_city` | `Invoice/SellerDtls/Loc` | Miasto / lokalizacja sprzedawcy |
| `supplier_postal_code` | `Invoice/SellerDtls/Pin` | Kod PIN sprzedawcy |
| `supplier_state_code` | `Invoice/SellerDtls/Stcd` | Kod stanu sprzedawcy (2 cyfry) |
| `buyer_name` | `Invoice/BuyerDtls/LglNm` | Prawna nazwa nabywcy |
| `buyer_id` | `Invoice/BuyerDtls/Gstin` | GSTIN nabywcy |
| `buyer_trade_name` | `Invoice/BuyerDtls/TrdNm` | Nazwa handlowa nabywcy |
| `buyer_address` | `Invoice/BuyerDtls/Addr1` | Adres nabywcy wiersz 1 |
| `buyer_city` | `Invoice/BuyerDtls/Loc` | Miasto / lokalizacja nabywcy |
| `buyer_postal_code` | `Invoice/BuyerDtls/Pin` | Kod PIN nabywcy |
| `buyer_state_code` | `Invoice/BuyerDtls/Stcd` | Kod stanu nabywcy |
| `irn` | `Irn` | Numer referencyjny faktury (64-znakowy hash SHA-256) |
| `ack_number` | `AckNo` | Numer potwierdzenia IRP |
| `ack_date` | `AckDt` | Data potwierdzenia IRP |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `Invoice/ItemList/Item`

| Kolumna | Źródłowy element XML | Uwagi |
|---|---|---|
| `POSITION` | `SlNo` | Numer sekwencyjny wiersza |
| `DESCRIPTION` | `PrdDesc` | Opis produktu / usługi |
| `QUANTITY` | `Qty` | Zafakturowana ilość |
| `UNIT` | `Unit` | Jednostka miary (np. `OTH`, `NOS`, `KGS`) |
| `UNIT_PRICE` | `UnitPrice` | Cena jednostkowa |
| `VAT_RATE` | `GstRt` | Stawka GST w % (np. 18%) |
| `VAT` | `IgstAmt` (lub `CgstAmt` + `SgstAmt`) | Kwota GST na wiersz |
| `NET_AMOUNT` | `AssAmt` | Kwota podlegająca opodatkowaniu na wiersz |

## Reguła klasyfikacji

DocBits wykrywa dokumenty India GST E-Invoice przez dopasowanie elementu głównego:

| Typ dokumentu elektronicznego | Wzorzec |
|--------------------------|---------|
| INDIA GST E-INVOICE | Element główny zawiera `<SignedInvoice` |

## Powiązane

- [Aktualnie obsługiwane standardy e-faktur](../../currently-supported-e-invoice-standards/)
- [Obsługiwane dokumenty elektroniczne](./)
