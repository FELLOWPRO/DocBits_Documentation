---
description: ARGENTINA FACTURA ELECTRONICA elektronische Dokumentenunterstützung in DocBits
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Argentinien |
| **Dokumenttypen** | Rechnung |
| **Format** | XML |
| **Standard** | Argentina Factura Electrónica (AFIP Comprobante-Typen jenseits von Factura A) |
| **Sprache** | `es_AR` |

ARGENTINA FACTURA ELECTRONICA umfasst die erweiterte Menge argentinischer AFIP-Elektronikdokumente jenseits von Factura A (Typ 001). Dazu gehören Factura B (Typ 006), Factura C (Typ 011), Nota de Crédito (Typ 003) und andere Varianten. DocBits erkennt den Dokumenttyp automatisch aus `<tipoComprobante>`.

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standard-Vorschau

<figure><img src="argentina-factura-electronica-preview.png" alt="Argentina Factura Electronica Vorschau in DocBits"><figcaption><p>Standard DocBits-Vorschau für ein ARGENTINA FACTURA ELECTRONICA Dokument</p></figcaption></figure>

## Feldzuordnung

### Kopffelder

| DocBits-Feld | Quell-XML-Elemente | Hinweise |
|---|---|---|
| `invoice_id` | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber` | Mehrere XPath-Fallbacks |
| `invoice_date` | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate` | |
| `due_date` | `//fechaVencimiento`, `//fechaVtoPago` | |
| `currency` | `//Moneda`, `//mon_id`, `//MonId`, Fallback: `ARS` | |
| `total_amount` | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount` | |
| `net_amount` | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount` | |
| `tax_amount` | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount` | |
| `supplier_name` | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName` | |
| `supplier_id` | `//CUITProveedor`, `//cuit`, `//Cuit`, `//SellerID` | CUIT = argentinische Steuernummer |
| `buyer_name` | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` | |
| `buyer_id` | `//CUITComprador`, `//doc_nro`, `//DocNro`, `//BuyerID` | |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `<items>/<item>`, `<Items>/<Item>` oder `<Detalle>/<Linea>`

| Spalte | Quell-Attribut / Element | Hinweise |
|---|---|---|
| `POSITION` | `@numero`, `<numero>` oder `position()` | |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>` | |
| `QUANTITY` | `<cantidad>`, `<Cantidad>` | |
| `UNIT_PRICE` | `<precioUnitario>`, `<PrecioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>`, `<AlicuotaIVA>` | |
| `VAT` | `<importeIVA>`, `<ImporteIVA>` | |
| `NET_AMOUNT` | `<subtotal>`, `<Subtotal>`, `<importe>` | |

## Klassifizierungsregel

Dokumente mit `<tipoComprobante>`-Werten ungleich `001` (z.B. `003`, `006`, `011`) werden diesem Standard zugeordnet.

## Verwandte Seiten

- [ARGENTINA AFIP](argentina-afip.md)
- [Unterstützte elektronische Dokumente](./)
