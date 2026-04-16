---
description: Support des documents électroniques ARGENTINA AFIP dans DocBits
---

# 🇦🇷 ARGENTINA AFIP

| Propriété | Valeur |
|-----------|--------|
| **Pays / Région** | Argentine |
| **Types de documents** | Facture |
| **Format** | XML |
| **Standard** | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Langue** | `es_AR` |

Le standard ARGENTINA AFIP est le format de facture électronique de l'administration fiscale fédérale argentine (AFIP). Les documents sont identifiés par `<tipoComprobante>` — par exemple, le type `001` = Factura A. Chaque facture inclut un numéro CAE (Código de Autorización Electrónica) et un code-barres pour la validation AFIP.

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="argentina-afip-preview.png" alt="Aperçu de facture ARGENTINA AFIP dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour une facture ARGENTINA AFIP Factura A</p></figcaption></figure>

## Correspondance des champs

### Champs d'en-tête

| Champ DocBits | Élément XML source | Notes |
|---|---|---|
| `invoice_id` | `<puntoVenta>` + `<numeroComprobante>` | Format : `PPPP-NNNNNNNN` |
| `invoice_date` | `<cabecera>/<fechaEmision>` | |
| `due_date` | `<cabecera>/<fechaVencimiento>` | |
| `currency` | Fixe : `ARS` | Toujours Peso argentin |
| `total_amount` | `<totales>/<total>` | |
| `net_amount` | `<totales>/<netoGravado>` ou `<subtotal>` | |
| `tax_amount` | `<totales>/<totalIVA>` | |
| `supplier_name` | `<emisor>/<razonSocial>` | |
| `supplier_id` | `<emisor>/<CUIT>` ou `<cabecera>/<CUIT>` | CUIT = numéro fiscal argentin |
| `supplier_address` | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` | |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>` | |
| `supplier_city` | `<emisor>/<domicilioComercial>/<localidad>` | |
| `supplier_country` | Fixe : `AR` | |
| `buyer_name` | `<receptor>/<razonSocial>` | |
| `buyer_id` | `<receptor>/<CUIT>` | |
| `buyer_address` | `<receptor>/<domicilio>/<calle>` + `<numero>` | |
| `buyer_postal_code` | `<receptor>/<domicilio>/<codigoPostal>` | |
| `buyer_city` | `<receptor>/<domicilio>/<localidad>` | |
| `buyer_country` | Fixe : `AR` | |
| `iban` | `<PAYMENT/IBAN>` | Généralement vide |
| `bic` | `<PAYMENT/BIC>` | Généralement vide |
| `payment_terms` | `<PAYMENT_TERMS>` | Généralement vide |
| `purchase_order` | `<PURCHASE_ORDER>` | Généralement vide |

### Tableau des lignes (`INVOICE_TABLE`)

Chemin de ligne : `<items>/<item>`

| Colonne | Attribut / Élément source | Notes |
|---|---|---|
| `POSITION` | Attribut `@numero` | Numéro de position |
| `DESCRIPTION` | `<descripcion>` | |
| `QUANTITY` | `<cantidad>` | |
| `UNIT` | `<unidadMedida>` | Code unité AFIP (ex. `7` = unité) |
| `UNIT_PRICE` | `<precioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>` | ex. `21.00` pour la TVA standard argentine |
| `VAT` | `<importeIVA>` | |
| `NET_AMOUNT` | `<subtotal>` | Total de ligne avant taxe |

## Règle de classification

DocBits détecte les documents ARGENTINA AFIP via le motif regex :

```
<tipoComprobante>001\s*</tipoComprobante>
```

## Pages liées

- [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
- [Documents électroniques pris en charge](./)
