---
description: Obsługa dokumentów elektronicznych Ecuador SRI (Factura Electrónica, SRI 1.0.0 – 2.1.0) w DocBits
---

# 🇪🇨 Ecuador SRI

| Właściwość | Wartość |
|-----------|---------|
| **Kraj / Region** | Ekwador |
| **Typy dokumentów** | Factura (Faktura), Nota de Crédito, Nota de Débito, Guía de Remisión, Comprobante de Retención |
| **Format** | XML |
| **Standard** | SRI (Servicio de Rentas Internas) |
| **Ustawienia regionalne** | `es_EC` |

Standard faktury elektronicznej Ecuador SRI jest wydawany pod nadzorem Servicio de Rentas Internas (SRI), ekwadorskiego organu podatkowego. Dokumenty używają własnego formatu XML z elementem głównym `<factura id="comprobante" version="X.X.X">`. DocBits automatycznie wykrywa wersję na podstawie atrybutu `version` i typ dokumentu na podstawie `codDoc`:

| Atrybut version | Typ dokumentu |
|----------------|---------------|
| `1.0.0` | SRI 1.0.0 |
| `1.1.0` | SRI 1.1.0 |
| `2.0.0` | SRI 2.0.0 |
| `2.1.0` | SRI 2.1.0 / FACTURA ELECTRONICA |

Numer faktury jest złożeniem trzech pól: `estab-ptoEmi-secuencial` (np. `001-001-000000001`). `claveAcceso` to 49-cyfrowy klucz dostępu wydawany przez SRI do uwierzytelniania dokumentów. Ekwador używa **Dolara Amerykańskiego (USD)** jako oficjalnej waluty.

## Status obsługi

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="ecuador-sri-preview.png" alt="Podgląd Ecuador SRI Factura w DocBits"><figcaption><p>Domyślny podgląd DocBits dla Factura Electrónica Ecuador SRI (wersja 2.1.0)</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | Źródłowy element XML | Uwagi |
|---|---|---|
| `invoice_id` | `estab` + `ptoEmi` + `secuencial` | Złożone: `001-001-000000001` |
| `invoice_date` | `infoFactura/fechaEmision` | Format daty `DD/MM/YYYY` |
| `due_date` | `infoFactura/pagos/pago/plazo` + `unidadTiempo` | Termin płatności (np. `30 dias`) |
| `currency` | Stałe: `USD` | Zawsze Dolar Amerykański (oficjalna waluta Ekwadoru) |
| `invoice_type` | Stałe: `Factura` | Etykieta typu dokumentu |
| `net_amount` | `infoFactura/totalSinImpuestos` | Kwota netto bez VAT |
| `tax_amount` | `infoFactura/totalConImpuestos/totalImpuesto/valor` | Kwota VAT (IVA) |
| `total_amount` | `infoFactura/importeTotal` | Kwota całkowita z VAT |
| `supplier_name` | `infoTributaria/razonSocial` | Nazwa firmy wystawcy |
| `supplier_id` | `infoTributaria/ruc` | RUC — 13-cyfrowy numer identyfikacji podatkowej |
| `supplier_tax_id` | `infoTributaria/ruc` | RUC (taki sam jak supplier_id) |
| `supplier_address` | `infoTributaria/dirMatriz` | Adres siedziby głównej wystawcy |
| `payment_terms` | `infoFactura/pagos/pago/formaPago` | Kod metody płatności SRI |
| `buyer_name` | `infoFactura/razonSocialComprador` | Nazwa firmy nabywcy |
| `buyer_id` | `infoFactura/identificacionComprador` | RUC lub CI nabywcy |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `detalles/detalle`

| Kolumna | Źródłowy element XML | Uwagi |
|---|---|---|
| `POSITION` | Indeks sekwencyjny | Numer wiersza od 1 |
| `DESCRIPTION` | `descripcion` | Opis pozycji |
| `QUANTITY` | `cantidad` | Ilość |
| `UNIT_PRICE` | `precioUnitario` | Cena jednostkowa bez VAT |
| `VAT_RATE` | `impuestos/impuesto/tarifa` | Stawka VAT w % (np. 15%) |
| `VAT` | `impuestos/impuesto/valor` | Kwota VAT na wiersz |
| `NET_AMOUNT` | `precioTotalSinImpuesto` | Suma wiersza bez VAT |

## Reguły klasyfikacji

DocBits wykrywa dokumenty Ecuador SRI dopasowując element główny i atrybut wersji:

| Typ dokumentu elektronicznego | Wzorzec |
|------------------------------|---------|
| ECUADOR SRI / FACTURA ELECTRONICA | `<factura id="comprobante"` (dowolna wersja) |
| ECUADOR SRI 1.0.0 | `<factura id="comprobante" version="1.0.0">` |
| ECUADOR SRI 1.1.0 | `<factura id="comprobante" version="1.1.0">` |
| ECUADOR SRI 2.0.0 | `<factura id="comprobante" version="2.0.0">` |
| ECUADOR SRI 2.1.0 | `<factura id="comprobante" version="2.1.0">` |

Elementem głównym jest `<factura>` z `id="comprobante"`. Atrybut `version` określa konkretną wersję SRI. Klasyfikacja używa zasady **pierwsze dopasowanie wygrywa**, posortowanej według długości wzorca (najdłuższy/najbardziej szczegółowy jako pierwszy).

## Powiązane

- [Aktualnie obsługiwane standardy e-faktur](../../currently-supported-e-invoice-standards/)
- [Obsługiwane dokumenty elektroniczne](./)
