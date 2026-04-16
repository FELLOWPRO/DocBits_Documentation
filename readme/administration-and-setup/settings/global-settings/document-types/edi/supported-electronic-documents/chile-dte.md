---
description: Obsługa elektronicznych dokumentów CHILE DTE w DocBits
---

# 🇨🇱 CHILE DTE

| Właściwość | Wartość |
|----------|-------|
| **Kraj / Region** | Chile |
| **Typy dokumentów** | Faktura (Factura), Nota kredytowa, Nota debetowa, Przewodnik wysyłki |
| **Format** | XML |
| **Standard** | DTE (Documento Tributario Electrónico), SII |
| **Ustawienia regionalne** | `es_CL` |

DTE (Documento Tributario Electrónico) to chilijski standard elektronicznych dokumentów podatkowych regulowany przez Servicio de Impuestos Internos (SII). Wszystkie dokumenty DTE współdzielą przestrzeń nazw `http://www.sii.cl/SiiDte`. DocBits automatycznie wykrywa kod typu DTE (`TipoDTE`) i kieruje do odpowiednich reguł ekstrakcji:

| Kod typu | Typ dokumentu |
|-----------|--------------|
| 33 | Factura Electrónica (Invoice) |
| 34 | Factura No Afecta o Exenta (Tax-exempt invoice) |
| 52 | Guía de Despacho (Dispatch Guide) |
| 56 | Nota de Débito (Debit Note) |
| 61 | Nota de Crédito (Credit Note) |

## Status wsparcia

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwany |
| Ekstrakcja pól | ✅ Obsługiwana |
| Transformacja | ✅ Obsługiwana |

## Domyślny podgląd

<figure><img src="chile-dte-preview.png" alt="Podgląd Chile DTE Factura w DocBits"><figcaption><p>Domyślny podgląd DocBits dla CHILE DTE FACTURA (typ 33)</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | Źródłowy element XML | Uwagi |
|---|---|---|
| `invoice_id` | `Folio` | Numer folio dokumentu |
| `invoice_date` | `FchEmis` | Data emisji ISO 8601 |
| `due_date` | `FchVenc` | Termin płatności |
| `currency` | Stały: `CLP` | Zawsze peso chilijskie |
| `total_amount` | `MntTotal` | Kwota całkowita z VAT |
| `net_amount` | `MntNeto` | Netto kwota podlegająca opodatkowaniu |
| `tax_amount` | `IVA` | Kwota VAT (standardowa stawka 19%) |
| `supplier_name` | `RznSoc` (Emisor) | Nazwa firmy wystawcy |
| `supplier_id` | `RUTEmisor` | RUT wystawcy (np. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Adres uliczny wystawcy |
| `supplier_city` | `CiudadOrigen` | Miasto wystawcy |
| `supplier_country` | Stały: `CL` | Zawsze Chile |
| `buyer_name` | `RznSocRecep` | Nazwa firmy odbiorcy |
| `buyer_id` | `RUTRecep` | RUT odbiorcy |
| `buyer_address` | `DirRecep` | Adres uliczny odbiorcy |
| `buyer_city` | `CiudadRecep` | Miasto odbiorcy |
| `buyer_country` | Stały: `CL` | Zawsze Chile |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `Detalle`

| Kolumna | Źródłowy element XML | Uwagi |
|---|---|---|
| `POSITION` | `NroLinDet` | Numer kolejny wiersza |
| `DESCRIPTION` | `NmbItem` | Nazwa pozycji |
| `QUANTITY` | `QtyItem` | Ilość |
| `UNIT` | `UnmdItem` | Jednostka miary |
| `UNIT_PRICE` | `PrcItem` | Cena jednostkowa bez VAT |
| `VAT_RATE` | `TasaIVA` (z nagłówka) | Stawka VAT w % (zazwyczaj 19%) |
| `VAT` | Obliczony | VAT na wiersz |
| `NET_AMOUNT` | `MontoItem` | Suma wiersza |

## Reguły klasyfikacji

DocBits wykrywa dokumenty Chile DTE przez dopasowanie przestrzeni nazw XML i `TipoDTE`:

| Typ dokumentu elektronicznego | Wzorzec |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

Element obwiedni to `<EnvioDTE>`, a każde DTE jest opakowane w `<DTE><Documento>`.

## Powiązane

- [Aktualnie obsługiwane standardy e-faktur](../../currently-supported-e-invoice-standards/)
- [Obsługiwane dokumenty elektroniczne](./)
