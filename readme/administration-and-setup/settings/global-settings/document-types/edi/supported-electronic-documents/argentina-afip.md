---
description: Prise en charge du document électronique ARGENTINA AFIP dans DocBits
---

# 🇦🇷 ARGENTINA AFIP

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Argentine](countries/argentina.md). L’entrée de classification des avoirs ne possède pas d’ensemble d’extraction dédié dans l’état examiné. Vérifiez la correspondance effectivement utilisée et testez un véritable exemple d’avoir.
{% endhint %}

| Propriété            | Valeur                                                                     |
| -------------------- | -------------------------------------------------------------------------- |
| **Country / Region** | Argentine                                                                  |
| **Document Types**   | Invoice                                                                    |
| **Format**           | XML                                                                        |
| **Standard**         | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Locale**           | `es_AR`                                                                    |

Le standard ARGENTINA AFIP est le format de facture électronique de l'autorité fiscale fédérale argentine (AFIP). Les documents sont identifiés par `<tipoComprobante>`, p. ex. le type `001` = Factura A. Chaque facture comprend un numéro CAE (Código de Autorización Electrónica) et un code-barres pour la validation par l'AFIP.

## Statut de la prise en charge

| Composant              | Statut      |
| ---------------------- | ----------- |
| Preview                | ✅ Pris en charge |
| Field Extraction       | ✅ Pris en charge |
| Transformation         | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/argentina-afip-preview.png" alt="Aperçu d'une facture Argentina AFIP dans DocBits"><figcaption><p>Aperçu DocBits par défaut d'une facture ARGENTINA AFIP Factura A</p></figcaption></figure>

## Mapping des champs

### Champs d'en-tête

| Champ DocBits          | Élément XML source                                   | Remarques                                          |
| ---------------------- | ---------------------------------------------------- | -------------------------------------------------- |
| `invoice_id`           | `<puntoVenta>` + `<numeroComprobante>`               | Au format `PPPP-NNNNNNNN`                          |
| `invoice_date`         | `<cabecera>/<fechaEmision>`                          |                                                    |
| `due_date`             | `<cabecera>/<fechaVencimiento>`                      |                                                    |
| `currency`             | Fixe : `ARS`                                         | Toujours le peso argentin                          |
| `total_amount`         | `<totales>/<total>`                                  |                                                    |
| `net_amount`           | `<totales>/<netoGravado>` ou `<subtotal>`            |                                                    |
| `tax_amount`           | `<totales>/<totalIVA>`                               |                                                    |
| `supplier_name`        | `<emisor>/<razonSocial>`                             |                                                    |
| `supplier_id`          | `<emisor>/<CUIT>` ou `<cabecera>/<CUIT>`             | CUIT = numéro d'identification fiscale argentin    |
| `supplier_address`     | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` |                                                    |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>`       |                                                    |
| `supplier_city`        | `<emisor>/<domicilioComercial>/<localidad>`          |                                                    |
| `supplier_country`     | Fixe : `AR`                                          |                                                    |
| `buyer_name`           | `<receptor>/<razonSocial>`                           |                                                    |
| `buyer_id`             | `<receptor>/<CUIT>`                                  |                                                    |
| `buyer_address`        | `<receptor>/<domicilio>/<calle>` + `<numero>`        |                                                    |
| `buyer_postal_code`    | `<receptor>/<domicilio>/<codigoPostal>`              |                                                    |
| `buyer_city`           | `<receptor>/<domicilio>/<localidad>`                 |                                                    |
| `buyer_country`        | Fixe : `AR`                                          |                                                    |
| `iban`                 | `<PAYMENT/IBAN>`                                     | Généralement vide : les documents AFIP contiennent rarement des données bancaires |
| `bic`                  | `<PAYMENT/BIC>`                                      | Généralement vide                                  |
| `payment_terms`        | `<PAYMENT_TERMS>`                                    | Généralement vide                                  |
| `purchase_order`       | `<PURCHASE_ORDER>`                                   | Généralement vide                                  |

### Tableau des lignes (`INVOICE_TABLE`)

Chemin de ligne : `<items>/<item>`

| Colonne       | Attribut / élément source  | Remarques                               |
| ------------- | -------------------------- | --------------------------------------- |
| `POSITION`    | attribut `@numero`         | Numéro de séquence de la ligne          |
| `DESCRIPTION` | `<descripcion>`            |                                         |
| `QUANTITY`    | `<cantidad>`               |                                         |
| `UNIT`        | `<unidadMedida>`           | Code d'unité AFIP (p. ex. `7` = unité)  |
| `UNIT_PRICE`  | `<precioUnitario>`         |                                         |
| `VAT_RATE`    | `<alicuotaIVA>`            | p. ex. `21.00` pour la TVA argentine standard |
| `VAT`         | `<importeIVA>`             |                                         |
| `NET_AMOUNT`  | `<subtotal>`               | Total de la ligne avant taxe            |

## Règle de classification

DocBits détecte les documents ARGENTINA AFIP grâce au motif regex suivant :

```
<tipoComprobante>001\s*</tipoComprobante>
```

Le type `001` correspond à **Factura A** (facture destinée aux acheteurs assujettis à la TVA). Les autres types de comprobante sont traités par le standard ARGENTINA FACTURA ELECTRONICA.

## Voir aussi

* [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
* [Supported Electronic Documents](./)
