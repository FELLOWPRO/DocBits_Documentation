---
description: Support des documents électroniques ARGENTINA FACTURA ELECTRONICA dans DocBits
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

| Propriété | Valeur |
|-----------|--------|
| **Pays / Région** | Argentine |
| **Types de documents** | Facture |
| **Format** | XML |
| **Standard** | Argentina Factura Electrónica (types de comprobante AFIP au-delà de Factura A) |
| **Langue** | `es_AR` |

ARGENTINA FACTURA ELECTRONICA couvre l'ensemble plus large des documents électroniques AFIP argentins au-delà de la Factura A (type 001). Cela inclut la Factura B (type 006), la Factura C (type 011), la Nota de Crédito (type 003) et d'autres variantes.

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="argentina-factura-electronica-preview.png" alt="Aperçu Argentina Factura Electronica dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour un document ARGENTINA FACTURA ELECTRONICA</p></figcaption></figure>

## Correspondance des champs

### Champs d'en-tête

| Champ DocBits | Éléments XML sources | Notes |
|---|---|---|
| `invoice_id` | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber` | Plusieurs chemins XPath de repli |
| `invoice_date` | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate` | |
| `due_date` | `//fechaVencimiento`, `//fechaVtoPago` | |
| `currency` | `//Moneda`, `//mon_id`, `//MonId`, repli : `ARS` | |
| `total_amount` | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount` | |
| `net_amount` | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount` | |
| `tax_amount` | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount` | |
| `supplier_name` | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName` | |
| `supplier_id` | `//CUITProveedor`, `//cuit`, `//Cuit`, `//SellerID` | |
| `buyer_name` | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` | |
| `buyer_id` | `//CUITComprador`, `//doc_nro`, `//DocNro`, `//BuyerID` | |

### Tableau des lignes (`INVOICE_TABLE`)

Chemin de ligne : `<items>/<item>`, `<Items>/<Item>` ou `<Detalle>/<Linea>`

| Colonne | Attribut / Élément source | Notes |
|---|---|---|
| `POSITION` | `@numero`, `<numero>` ou `position()` | |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>` | |
| `QUANTITY` | `<cantidad>`, `<Cantidad>` | |
| `UNIT_PRICE` | `<precioUnitario>`, `<PrecioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>`, `<AlicuotaIVA>` | |
| `VAT` | `<importeIVA>`, `<ImporteIVA>` | |
| `NET_AMOUNT` | `<subtotal>`, `<Subtotal>`, `<importe>` | |

## Règle de classification

Les documents avec des valeurs `<tipoComprobante>` autres que `001` sont routés vers ce standard.

## Pages liées

- [ARGENTINA AFIP](argentina-afip.md)
- [Documents électroniques pris en charge](./)
