---
description: CHILE DTE electronic document support in DocBits
---

# 🇨🇱 CHILE DTE

| Property | Value |
|----------|-------|
| **Country / Region** | Chile |
| **Document Types** | Invoice (Factura), Credit Note, Debit Note, Dispatch Guide |
| **Format** | XML |
| **Standard** | DTE (Documento Tributario Electrónico), SII |
| **Locale** | `es_CL` |

DTE (Documento Tributario Electrónico) is the Chilean electronic tax document standard regulated by the Servicio de Impuestos Internos (SII). All DTE documents share the `http://www.sii.cl/SiiDte` namespace. DocBits auto-detects the DTE type code (`TipoDTE`) and routes to the appropriate extraction rules:

| Type Code | Document Type |
|-----------|--------------|
| 33 | Factura Electrónica (Invoice) |
| 34 | Factura No Afecta o Exenta (Tax-exempt invoice) |
| 52 | Guía de Despacho (Dispatch Guide) |
| 56 | Nota de Débito (Debit Note) |
| 61 | Nota de Crédito (Credit Note) |

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Default Preview

<figure><img src="chile-dte-preview.png" alt="Chile DTE Factura preview in DocBits"><figcaption><p>Default DocBits preview for a CHILE DTE FACTURA (type 33)</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field | Source XML Element | Notes |
|---|---|---|
| `invoice_id` | `Folio` | Document folio number |
| `invoice_date` | `FchEmis` | ISO 8601 emission date |
| `due_date` | `FchVenc` | Payment due date |
| `currency` | Fixed: `CLP` | Always Chilean Peso |
| `total_amount` | `MntTotal` | Total amount incl. VAT |
| `net_amount` | `MntNeto` | Net taxable amount |
| `tax_amount` | `IVA` | VAT amount (19% standard rate) |
| `supplier_name` | `RznSoc` (Emisor) | Issuer company name |
| `supplier_id` | `RUTEmisor` | Issuer RUT (e.g. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Issuer street address |
| `supplier_city` | `CiudadOrigen` | Issuer city |
| `supplier_country` | Fixed: `CL` | Always Chile |
| `buyer_name` | `RznSocRecep` | Recipient company name |
| `buyer_id` | `RUTRecep` | Recipient RUT |
| `buyer_address` | `DirRecep` | Recipient street address |
| `buyer_city` | `CiudadRecep` | Recipient city |
| `buyer_country` | Fixed: `CL` | Always Chile |

### Line Item Table (`INVOICE_TABLE`)

Row path: `Detalle`

| Column | Source XML Element | Notes |
|---|---|---|
| `POSITION` | `NroLinDet` | Line sequence number |
| `DESCRIPTION` | `NmbItem` | Item name |
| `QUANTITY` | `QtyItem` | Quantity |
| `UNIT` | `UnmdItem` | Unit of measure |
| `UNIT_PRICE` | `PrcItem` | Unit price excl. VAT |
| `VAT_RATE` | `TasaIVA` (from header) | IVA rate in % (typically 19%) |
| `VAT` | Calculated | VAT per line |
| `NET_AMOUNT` | `MontoItem` | Line total |

## Classification Rules

DocBits detects Chile DTE documents by matching the XML namespace and `TipoDTE`:

| Electronic Document Type | Pattern |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

The envelope element is `<EnvioDTE>` and each DTE is wrapped in `<DTE><Documento>`.

## Related

- [Currently Supported E-Invoice Standards](../../currently-supported-e-invoice-standards/)
- [Supported Electronic Documents](./)
