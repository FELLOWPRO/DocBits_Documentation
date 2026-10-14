---
description: Prise en charge du document électronique ARGENTINA FACTURA ELECTRONICA dans DocBits
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

| Propriété            | Valeur                                                                  |
| -------------------- | ----------------------------------------------------------------------- |
| **Country / Region** | Argentine                                                               |
| **Document Types**   | Invoice                                                                 |
| **Format**           | XML                                                                     |
| **Standard**         | Argentina Factura Electrónica (types de comprobante AFIP autres que Factura A) |
| **Locale**           | `es_AR`                                                                 |

ARGENTINA FACTURA ELECTRONICA couvre l'ensemble plus large des documents électroniques AFIP argentins au-delà de la Factura A (type 001). Cela comprend d'autres types de comprobante tels que la Factura B (type 006), la Factura C (type 011), la Nota de Crédito (type 003) et d'autres variantes. DocBits détecte automatiquement le type de document à partir de `<tipoComprobante>` et applique l'extraction appropriée.

## Statut de la prise en charge

| Composant        | Statut      |
| ---------------- | ----------- |
| Preview          | ✅ Pris en charge |
| Field Extraction | ✅ Pris en charge |
| Transformation   | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/argentina-factura-electronica-preview.png" alt="Aperçu Argentina Factura Electronica dans DocBits"><figcaption><p>Aperçu DocBits par défaut d'un document ARGENTINA FACTURA ELECTRONICA</p></figcaption></figure>

## Mapping des champs

### Champs d'en-tête

| Champ DocBits    | Éléments XML sources                                                      | Remarques                                    |
| ---------------- | ------------------------------------------------------------------------- | -------------------------------------------- |
| `invoice_id`     | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber`           | Plusieurs XPath de repli pour les schémas variants |
| `invoice_date`   | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate`                |                                              |
| `due_date`       | `//fechaVencimiento`, `//fechaVtoPago`                                    |                                              |
| `currency`       | `//Moneda`, `//mon_id`, `//MonId`, repli : `ARS`                          |                                              |
| `total_amount`   | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount`              |                                              |
| `net_amount`     | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount`                   |                                              |
| `tax_amount`     | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount`                      |                                              |
| `supplier_name`  | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName`    |                                              |
| `supplier_id`    | `//CUITProveedor`, `//cuit`, `//Cuit`, `//SellerID`                       | CUIT = numéro d'identification fiscale argentin |
| `buyer_name`     | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` |                                              |
| `buyer_id`       | `//CUITComprador`, `//doc_nro`, `//DocNro`, `//BuyerID`                   |                                              |
| `iban`           | `//PAYMENT/IBAN`                                                          | Généralement vide                            |
| `bic`            | `//PAYMENT/BIC`                                                           | Généralement vide                            |
| `payment_terms`  | `//PAYMENT_TERMS`                                                         | Généralement vide                            |
| `purchase_order` | `//PURCHASE_ORDER`                                                        | Généralement vide                            |

### Tableau des lignes (`INVOICE_TABLE`)

Chemin de ligne : `<items>/<item>`, `<Items>/<Item>` ou `<Detalle>/<Linea>`

| Colonne       | Attribut / élément source               | Remarques            |
| ------------- | --------------------------------------- | -------------------- |
| `POSITION`    | `@numero`, `<numero>` ou `position()`   | Numéro de séquence de la ligne |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>`        |                      |
| `QUANTITY`    | `<cantidad>`, `<Cantidad>`              |                      |
| `UNIT_PRICE`  | `<precioUnitario>`, `<PrecioUnitario>`  |                      |
| `VAT_RATE`    | `<alicuotaIVA>`, `<AlicuotaIVA>`        | p. ex. `21.00`       |
| `VAT`         | `<importeIVA>`, `<ImporteIVA>`          |                      |
| `NET_AMOUNT`  | `<subtotal>`, `<Subtotal>`, `<importe>` | Total de la ligne    |

## Règle de classification

DocBits détecte les documents ARGENTINA FACTURA ELECTRONICA par l'absence du marqueur Factura A : les documents dont les valeurs `<tipoComprobante>` diffèrent de `001` (p. ex. `003`, `006`, `011`) sont dirigés vers ce standard.

## Voir aussi

* [ARGENTINA AFIP](argentina-afip.md)
* [Supported Electronic Documents](./)
