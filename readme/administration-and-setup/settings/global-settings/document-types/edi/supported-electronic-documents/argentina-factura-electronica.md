---
description: Obsługa dokumentów elektronicznych ARGENTINA FACTURA ELECTRONICA w DocBits
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

| Właściwość | Wartość |
|------------|---------|
| **Kraj / Region** | Argentyna |
| **Typy dokumentów** | Faktura |
| **Format** | XML |
| **Standard** | Argentina Factura Electrónica (typy comprobanteAFIP poza Factura A) |
| **Język** | `es_AR` |

ARGENTINA FACTURA ELECTRONICA obejmuje szerszy zestaw argentyńskich dokumentów elektronicznych AFIP poza Factura A (typ 001). Obejmuje to Factura B (typ 006), Factura C (typ 011), Nota de Crédito (typ 003) i inne warianty.

## Status obsługi

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwane |
| Ekstrakcja pól | ✅ Obsługiwane |
| Transformacja | ✅ Obsługiwane |

## Domyślny podgląd

<figure><img src="argentina-factura-electronica-preview.png" alt="Podgląd Argentina Factura Electronica w DocBits"><figcaption><p>Domyślny podgląd DocBits dla dokumentu ARGENTINA FACTURA ELECTRONICA</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits | Źródłowe elementy XML | Uwagi |
|---|---|---|
| `invoice_id` | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber` | Wiele ścieżek XPath zapasowych |
| `invoice_date` | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate` | |
| `currency` | `//Moneda`, `//mon_id`, `//MonId`, zapasowy: `ARS` | |
| `total_amount` | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount` | |
| `net_amount` | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount` | |
| `tax_amount` | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount` | |
| `supplier_name` | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName` | |
| `buyer_name` | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` | |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `<items>/<item>`, `<Items>/<Item>` lub `<Detalle>/<Linea>`

| Kolumna | Źródło | Uwagi |
|---|---|---|
| `POSITION` | `@numero`, `<numero>` lub `position()` | |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>` | |
| `QUANTITY` | `<cantidad>`, `<Cantidad>` | |
| `UNIT_PRICE` | `<precioUnitario>`, `<PrecioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>`, `<AlicuotaIVA>` | |
| `NET_AMOUNT` | `<subtotal>`, `<Subtotal>`, `<importe>` | |

## Reguła klasyfikacji

Dokumenty z wartościami `<tipoComprobante>` innymi niż `001` są kierowane do tego standardu.

## Powiązane

- [ARGENTINA AFIP](argentina-afip.md)
- [Obsługiwane dokumenty elektroniczne](./)
