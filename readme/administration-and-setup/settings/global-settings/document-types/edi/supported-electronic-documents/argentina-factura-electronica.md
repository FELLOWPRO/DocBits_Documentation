---
description: ARGENTINA FACTURA ELECTRONICA electronic document support in DocBits
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

| Property | Value |
|----------|-------|
| **Country / Region** | Argentina |
| **Document Types** | Invoice |
| **Format** | XML |
| **Standard** | Argentina Factura Electrónica (AFIP comprobante types beyond Factura A) |
| **Locale** | `es_AR` |

ARGENTINA FACTURA ELECTRONICA covers the broader set of Argentine AFIP electronic documents beyond Factura A (type 001). This includes other comprobante types such as Factura B (type 006), Factura C (type 011), Nota de Crédito (type 003), and other variants. DocBits auto-detects the document type from `<tipoComprobante>` and applies the appropriate extraction.

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Default Preview

<figure><img src="argentina-factura-electronica-preview.png" alt="Argentina Factura Electronica preview in DocBits"><figcaption><p>Default DocBits preview for an ARGENTINA FACTURA ELECTRONICA document</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field | Source XML Elements | Notes |
|---|---|---|
| `invoice_id` | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber` | Multiple XPath fallbacks for variant schemas |
| `invoice_date` | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate` | |
| `due_date` | `//fechaVencimiento`, `//fechaVtoPago` | |
| `currency` | `//Moneda`, `//mon_id`, `//MonId`, fallback: `ARS` | |
| `total_amount` | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount` | |
| `net_amount` | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount` | |
| `tax_amount` | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount` | |
| `supplier_name` | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName` | |
| `supplier_id` | `//CUITProveedor`, `//cuit`, `//Cuit`, `//SellerID` | CUIT = Argentine tax ID |
| `buyer_name` | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` | |
| `buyer_id` | `//CUITComprador`, `//doc_nro`, `//DocNro`, `//BuyerID` | |
| `iban` | `//PAYMENT/IBAN` | Usually empty |
| `bic` | `//PAYMENT/BIC` | Usually empty |
| `payment_terms` | `//PAYMENT_TERMS` | Usually empty |
| `purchase_order` | `//PURCHASE_ORDER` | Usually empty |

### Line Item Table (`INVOICE_TABLE`)

Row path: `<items>/<item>`, `<Items>/<Item>`, or `<Detalle>/<Linea>`

| Column | Source Attribute / Element | Notes |
|---|---|---|
| `POSITION` | `@numero`, `<numero>`, or `position()` | Item sequence number |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>` | |
| `QUANTITY` | `<cantidad>`, `<Cantidad>` | |
| `UNIT_PRICE` | `<precioUnitario>`, `<PrecioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>`, `<AlicuotaIVA>` | e.g. `21.00` |
| `VAT` | `<importeIVA>`, `<ImporteIVA>` | |
| `NET_AMOUNT` | `<subtotal>`, `<Subtotal>`, `<importe>` | Line total |

## Classification Rule

DocBits detects ARGENTINA FACTURA ELECTRONICA documents via the absence of the Factura A marker — documents with `<tipoComprobante>` values other than `001` (e.g. `003`, `006`, `011`) are routed to this standard.

## Related

- [ARGENTINA AFIP](argentina-afip.md)
- [Supported Electronic Documents](./)
