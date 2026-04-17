---
description: Ecuador SRI (Factura Electrónica, SRI 1.0.0 – 2.1.0) electronic document support in DocBits
---

# 🇪🇨 Ecuador SRI

| Property | Value |
|----------|-------|
| **Country / Region** | Ecuador |
| **Document Types** | Factura (Invoice), Nota de Crédito, Nota de Débito, Guía de Remisión, Comprobante de Retención |
| **Format** | XML |
| **Standard** | SRI (Servicio de Rentas Internas) |
| **Locale** | `es_EC` |

The Ecuador SRI electronic invoice standard is issued under the authority of the Servicio de Rentas Internas (SRI), Ecuador's tax authority. Documents use a proprietary XML format with a `<factura id="comprobante" version="X.X.X">` root element. DocBits auto-detects the version from the `version` attribute and the document type from `codDoc`:

| version attribute | Document Type |
|-------------------|---------------|
| `1.0.0` | SRI 1.0.0 |
| `1.1.0` | SRI 1.1.0 |
| `2.0.0` | SRI 2.0.0 |
| `2.1.0` | SRI 2.1.0 / FACTURA ELECTRONICA |

The invoice number is a composite of three fields: `estab-ptoEmi-secuencial` (e.g. `001-001-000000001`). The `claveAcceso` is a 49-digit access key issued by SRI for document authentication. Ecuador uses the **US Dollar (USD)** as its official currency.

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Default Preview

<figure><img src="ecuador-sri-preview.png" alt="Ecuador SRI Factura preview in DocBits"><figcaption><p>Default DocBits preview for an Ecuador SRI Factura Electrónica (version 2.1.0)</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field | Source XML Element | Notes |
|---|---|---|
| `invoice_id` | `estab` + `ptoEmi` + `secuencial` | Composite: `001-001-000000001` |
| `invoice_date` | `infoFactura/fechaEmision` | Date format `DD/MM/YYYY` |
| `due_date` | `infoFactura/pagos/pago/plazo` + `unidadTiempo` | Payment term (e.g. `30 dias`) |
| `currency` | Fixed: `USD` | Always US Dollar (Ecuador's official currency) |
| `invoice_type` | Fixed: `Factura` | Document type label |
| `net_amount` | `infoFactura/totalSinImpuestos` | Net total excl. VAT |
| `tax_amount` | `infoFactura/totalConImpuestos/totalImpuesto/valor` | VAT amount (IVA) |
| `total_amount` | `infoFactura/importeTotal` | Total amount incl. VAT |
| `supplier_name` | `infoTributaria/razonSocial` | Issuer company name |
| `supplier_id` | `infoTributaria/ruc` | RUC — 13-digit taxpayer ID |
| `supplier_tax_id` | `infoTributaria/ruc` | RUC (same as supplier_id) |
| `supplier_address` | `infoTributaria/dirMatriz` | Issuer headquarters address |
| `payment_terms` | `infoFactura/pagos/pago/formaPago` | SRI payment method code |
| `buyer_name` | `infoFactura/razonSocialComprador` | Buyer company name |
| `buyer_id` | `infoFactura/identificacionComprador` | Buyer RUC or CI |

### Line Item Table (`INVOICE_TABLE`)

Row path: `detalles/detalle`

| Column | Source XML Element | Notes |
|---|---|---|
| `POSITION` | Sequential index | 1-based line number |
| `DESCRIPTION` | `descripcion` | Item description |
| `QUANTITY` | `cantidad` | Quantity |
| `UNIT_PRICE` | `precioUnitario` | Unit price excl. VAT |
| `VAT_RATE` | `impuestos/impuesto/tarifa` | VAT rate in % (e.g. 15%) |
| `VAT` | `impuestos/impuesto/valor` | VAT amount per line |
| `NET_AMOUNT` | `precioTotalSinImpuesto` | Line total excl. VAT |

## Classification Rules

DocBits detects Ecuador SRI documents by matching the root element and version attribute:

| Electronic Document Type | Pattern |
|--------------------------|---------|
| ECUADOR SRI / FACTURA ELECTRONICA | `<factura id="comprobante"` (any version) |
| ECUADOR SRI 1.0.0 | `<factura id="comprobante" version="1.0.0">` |
| ECUADOR SRI 1.1.0 | `<factura id="comprobante" version="1.1.0">` |
| ECUADOR SRI 2.0.0 | `<factura id="comprobante" version="2.0.0">` |
| ECUADOR SRI 2.1.0 | `<factura id="comprobante" version="2.1.0">` |

The root element is `<factura>` with `id="comprobante"`. The `version` attribute determines the specific SRI version. Classification uses the **first-match-wins** principle, sorted by pattern length (longest/most-specific first).

## Related

- [Currently Supported E-Invoice Standards](../../currently-supported-e-invoice-standards/)
- [Supported Electronic Documents](./)
