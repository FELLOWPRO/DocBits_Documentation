---
description: ARGENTINA FACTURA ELECTRONICA ondersteuning voor elektronische documenten in DocBits
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

| Eigenschap | Waarde |
|------------|--------|
| **Land / Regio** | Argentinië |
| **Documenttypen** | Factuur |
| **Formaat** | XML |
| **Standaard** | Argentina Factura Electrónica (AFIP comprobante-typen buiten Factura A) |
| **Taal** | `es_AR` |

ARGENTINA FACTURA ELECTRONICA omvat de bredere set Argentijnse AFIP elektronische documenten buiten Factura A (type 001). Dit omvat Factura B (type 006), Factura C (type 011), Nota de Crédito (type 003) en andere varianten.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaard voorbeeld

<figure><img src="argentina-factura-electronica-preview.png" alt="Argentina Factura Electronica voorbeeld in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een ARGENTINA FACTURA ELECTRONICA document</p></figcaption></figure>

## Veldtoewijzing

### Kopvelden

| DocBits-veld | Bron-XML-elementen | Opmerkingen |
|---|---|---|
| `invoice_id` | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber` | Meerdere XPath-fallbacks |
| `invoice_date` | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate` | |
| `currency` | `//Moneda`, `//mon_id`, `//MonId`, fallback: `ARS` | |
| `total_amount` | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount` | |
| `net_amount` | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount` | |
| `tax_amount` | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount` | |
| `supplier_name` | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName` | |
| `buyer_name` | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` | |

### Regeltabel (`INVOICE_TABLE`)

Rijpad: `<items>/<item>`, `<Items>/<Item>` of `<Detalle>/<Linea>`

| Kolom | Bron | Opmerkingen |
|---|---|---|
| `POSITION` | `@numero`, `<numero>` of `position()` | |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>` | |
| `QUANTITY` | `<cantidad>`, `<Cantidad>` | |
| `UNIT_PRICE` | `<precioUnitario>`, `<PrecioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>`, `<AlicuotaIVA>` | |
| `NET_AMOUNT` | `<subtotal>`, `<Subtotal>`, `<importe>` | |

## Classificatieregel

Documenten met `<tipoComprobante>`-waarden anders dan `001` worden naar deze standaard gerouteerd.

## Gerelateerd

- [ARGENTINA AFIP](argentina-afip.md)
- [Ondersteunde elektronische documenten](./)
