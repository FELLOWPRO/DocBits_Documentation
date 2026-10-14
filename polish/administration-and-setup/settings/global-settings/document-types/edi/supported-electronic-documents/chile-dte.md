---
description: Obsługa dokumentów elektronicznych CHILE DTE w DocBits
---

# 🇨🇱 CHILE DTE

| Właściwość | Wartość |
|----------|-------|
| **Kraj / Region** | Chile |
| **Typy dokumentów** | Faktura, Nota korygująca, Nota obciążeniowa, List przewozowy |
| **Format** | XML |
| **Standard** | DTE (Documento Tributario Electrónico), SII |
| **Locale** | `es_CL` |

DTE (Documento Tributario Electrónico) to chilijski standard elektronicznych dokumentów fiskalnych regulowany przez Servicio de Impuestos Internos (SII). Wszystkie dokumenty DTE współdzielą przestrzeń nazw `http://www.sii.cl/SiiDte`. DocBits automatycznie wykrywa kod typu DTE (`TipoDTE`) i kieruje do odpowiednich reguł ekstrakcji:

| Kod typu | Typ dokumentu |
|-----------|--------------|
| 33 | Factura Electrónica (Faktura) |
| 34 | Factura No Afecta o Exenta (Faktura zwolniona) |
| 52 | Guía de Despacho (List przewozowy) |
| 56 | Nota de Débito (Nota obciążeniowa) |
| 61 | Nota de Crédito (Nota korygująca) |

## Status obsługi

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwany |
| Ekstrakcja pól | ✅ Obsługiwany |
| Transformacja | ✅ Obsługiwany |

## Domyślny podgląd

<figure><img src="chile-dte-preview.png" alt="Podgląd faktury Chile DTE w DocBits"><figcaption><p>Domyślny podgląd DocBits dla CHILE DTE FACTURA (typ 33)</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | Element XML źródła | Uwagi |
|---|---|---|
| `invoice_id` | `Folio` | Numer folio dokumentu |
| `invoice_date` | `FchEmis` | Data wystawienia ISO 8601 |
| `due_date` | `FchVenc` | Data płatności |
| `currency` | Stałe: `CLP` | Zawsze peso chilijskie |
| `total_amount` | `MntTotal` | Kwota brutto z VAT |
| `net_amount` | `MntNeto` | Kwota netto opodatkowana |
| `tax_amount` | `IVA` | Kwota VAT (stawka standardowa 19%) |
| `supplier_name` | `RznSoc` (Emisor) | Nazwa firmy wystawcy |
| `supplier_id` | `RUTEmisor` | RUT wystawcy (np. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Adres wystawcy |
| `supplier_city` | `CiudadOrigen` | Miasto wystawcy |
| `supplier_country` | Stałe: `CL` | Zawsze Chile |
| `buyer_name` | `RznSocRecep` | Nazwa firmy nabywcy |
| `buyer_id` | `RUTRecep` | RUT nabywcy |
| `buyer_address` | `DirRecep` | Adres nabywcy |
| `buyer_city` | `CiudadRecep` | Miasto nabywcy |
| `buyer_country` | Stałe: `CL` | Zawsze Chile |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka pozycji: `Detalle`

| Kolumna | Element XML źródła | Uwagi |
|---|---|---|
| `POSITION` | `NroLinDet` | Numer pozycji |
| `DESCRIPTION` | `NmbItem` | Opis pozycji |
| `QUANTITY` | `QtyItem` | Ilość |
| `UNIT` | `UnmdItem` | Jednostka miary |
| `UNIT_PRICE` | `PrcItem` | Cena jednostkowa netto |
| `VAT_RATE` | `TasaIVA` (z nagłówka) | Stawka VAT w % (zazwyczaj 19%) |
| `VAT` | Obliczone | VAT na pozycję |
| `NET_AMOUNT` | `MontoItem` | Wartość pozycji |

## Reguły klasyfikacji

DocBits wykrywa dokumenty Chile DTE poprzez dopasowanie przestrzeni nazw XML i `TipoDTE`:

| Typ dokumentu elektronicznego | Wzorzec |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

Element koperty to `<EnvioDTE>`, a każdy DTE jest opakowany w `<DTE><Documento>`.

## Zobacz również

- [Obecnie obsługiwane standardy e-faktur](../../currently-supported-e-invoice-standards/)
- [Obsługiwane dokumenty elektroniczne](./)
