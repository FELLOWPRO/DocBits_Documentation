---
description: ARGENTINA AFIP electronic document support in DocBits
---

# 🇦🇷 ARGENTINA AFIP

| Property | Value |
|----------|-------|
| **Country / Region** | Argentina |
| **Document Types** | Invoice |
| **Format** | XML |
| **Standard** | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Locale** | `es_AR` |

The ARGENTINA AFIP standard is the Argentine federal tax authority's (AFIP) electronic invoice format. Documents are identified by `<tipoComprobante>` — e.g. type `001` = Factura A. Each invoice includes a CAE (Código de Autorización Electrónica) number and barcode for AFIP validation.

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Default Preview

<figure><img src="argentina-afip-preview.png" alt="Argentina AFIP invoice preview in DocBits"><figcaption><p>Default DocBits preview for an ARGENTINA AFIP Factura A invoice</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field | Source XML Element | Notes |
|---|---|---|
| `invoice_id` | `<puntoVenta>` + `<numeroComprobante>` | Formatted as `PPPP-NNNNNNNN` |
| `invoice_date` | `<cabecera>/<fechaEmision>` | |
| `due_date` | `<cabecera>/<fechaVencimiento>` | |
| `currency` | Fixed: `ARS` | Always Argentine Peso |
| `total_amount` | `<totales>/<total>` | |
| `net_amount` | `<totales>/<netoGravado>` or `<subtotal>` | |
| `tax_amount` | `<totales>/<totalIVA>` | |
| `supplier_name` | `<emisor>/<razonSocial>` | |
| `supplier_id` | `<emisor>/<CUIT>` or `<cabecera>/<CUIT>` | CUIT = Argentine tax ID |
| `supplier_address` | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` | |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>` | |
| `supplier_city` | `<emisor>/<domicilioComercial>/<localidad>` | |
| `supplier_country` | Fixed: `AR` | |
| `buyer_name` | `<receptor>/<razonSocial>` | |
| `buyer_id` | `<receptor>/<CUIT>` | |
| `buyer_address` | `<receptor>/<domicilio>/<calle>` + `<numero>` | |
| `buyer_postal_code` | `<receptor>/<domicilio>/<codigoPostal>` | |
| `buyer_city` | `<receptor>/<domicilio>/<localidad>` | |
| `buyer_country` | Fixed: `AR` | |
| `iban` | `<PAYMENT/IBAN>` | Usually empty — AFIP docs rarely contain bank data |
| `bic` | `<PAYMENT/BIC>` | Usually empty |
| `payment_terms` | `<PAYMENT_TERMS>` | Usually empty |
| `purchase_order` | `<PURCHASE_ORDER>` | Usually empty |

### Line Item Table (`INVOICE_TABLE`)

Row path: `<items>/<item>`

| Column | Source Attribute / Element | Notes |
|---|---|---|
| `POSITION` | `@numero` attribute | Item sequence number |
| `DESCRIPTION` | `<descripcion>` | |
| `QUANTITY` | `<cantidad>` | |
| `UNIT` | `<unidadMedida>` | AFIP unit code (e.g. `7` = unit) |
| `UNIT_PRICE` | `<precioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>` | e.g. `21.00` for standard Argentine VAT |
| `VAT` | `<importeIVA>` | |
| `NET_AMOUNT` | `<subtotal>` | Line total before tax |

## Classification Rule

DocBits detects ARGENTINA AFIP documents via the regex pattern:

```
<tipoComprobante>001\s*</tipoComprobante>
```

Type `001` corresponds to **Factura A** (invoice to VAT-registered buyers). Other comprobante types are handled by the ARGENTINA FACTURA ELECTRONICA standard.

## Related

- [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
- [Supported Electronic Documents](./)
