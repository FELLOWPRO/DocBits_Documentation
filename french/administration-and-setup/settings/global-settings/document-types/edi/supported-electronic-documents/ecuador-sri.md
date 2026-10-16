---
description: Prise en charge des documents électroniques Ecuador SRI (Factura Electrónica, SRI 1.0.0 – 2.1.0) dans DocBits
---

# 🇪🇨 Ecuador SRI

| Propriété | Valeur |
|-----------|--------|
| **Pays / Région** | Équateur |
| **Types de documents** | Factura (Facture), Nota de Crédito, Nota de Débito, Guía de Remisión, Comprobante de Retención |
| **Format** | XML |
| **Norme** | SRI (Servicio de Rentas Internas) |
| **Paramètres régionaux** | `es_EC` |

La norme de facturation électronique Ecuador SRI est émise sous l'autorité du Servicio de Rentas Internas (SRI), l'autorité fiscale équatorienne. Les documents utilisent un format XML propriétaire avec un élément racine `<factura id="comprobante" version="X.X.X">`. DocBits détecte automatiquement la version à partir de l'attribut `version` et le type de document à partir de `codDoc` :

| Attribut version | Type de document |
|------------------|-----------------|
| `1.0.0` | SRI 1.0.0 |
| `1.1.0` | SRI 1.1.0 |
| `2.0.0` | SRI 2.0.0 |
| `2.1.0` | SRI 2.1.0 / FACTURA ELECTRONICA |

Le numéro de facture est un composite de trois champs : `estab-ptoEmi-secuencial` (ex. `001-001-000000001`). La `claveAcceso` est une clé d'accès à 49 chiffres émise par le SRI pour l'authentification des documents. L'Équateur utilise le **dollar américain (USD)** comme monnaie officielle.

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction de champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="ecuador-sri-preview.png" alt="Aperçu de la Factura Ecuador SRI dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour une Factura Electrónica Ecuador SRI (version 2.1.0)</p></figcaption></figure>

## Correspondance des champs

### Champs d'en-tête

| Champ DocBits | Élément XML source | Notes |
|---|---|---|
| `invoice_id` | `estab` + `ptoEmi` + `secuencial` | Composite : `001-001-000000001` |
| `invoice_date` | `infoFactura/fechaEmision` | Format de date `DD/MM/YYYY` |
| `due_date` | `infoFactura/pagos/pago/plazo` + `unidadTiempo` | Conditions de paiement (ex. `30 dias`) |
| `currency` | Fixe : `USD` | Toujours dollar américain (monnaie officielle de l'Équateur) |
| `invoice_type` | Fixe : `Factura` | Libellé du type de document |
| `net_amount` | `infoFactura/totalSinImpuestos` | Total net hors TVA |
| `tax_amount` | `infoFactura/totalConImpuestos/totalImpuesto/valor` | Montant de la TVA (IVA) |
| `total_amount` | `infoFactura/importeTotal` | Montant total TVA incluse |
| `supplier_name` | `infoTributaria/razonSocial` | Raison sociale de l'émetteur |
| `supplier_id` | `infoTributaria/ruc` | RUC — identifiant fiscal à 13 chiffres |
| `supplier_tax_id` | `infoTributaria/ruc` | RUC (identique à supplier_id) |
| `supplier_address` | `infoTributaria/dirMatriz` | Adresse du siège social de l'émetteur |
| `payment_terms` | `infoFactura/pagos/pago/formaPago` | Code du mode de paiement SRI |
| `buyer_name` | `infoFactura/razonSocialComprador` | Raison sociale de l'acheteur |
| `buyer_id` | `infoFactura/identificacionComprador` | RUC ou CI de l'acheteur |

### Tableau des lignes de commande (`INVOICE_TABLE`)

Chemin de ligne : `detalles/detalle`

| Colonne | Élément XML source | Notes |
|---|---|---|
| `POSITION` | Index séquentiel | Numéro de ligne à base 1 |
| `DESCRIPTION` | `descripcion` | Description de l'article |
| `QUANTITY` | `cantidad` | Quantité |
| `UNIT_PRICE` | `precioUnitario` | Prix unitaire hors TVA |
| `VAT_RATE` | `impuestos/impuesto/tarifa` | Taux de TVA en % (ex. 15%) |
| `VAT` | `impuestos/impuesto/valor` | Montant de la TVA par ligne |
| `NET_AMOUNT` | `precioTotalSinImpuesto` | Total de la ligne hors TVA |

## Règles de classification

DocBits détecte les documents Ecuador SRI en faisant correspondre l'élément racine et l'attribut de version :

| Type de document électronique | Modèle |
|-------------------------------|--------|
| ECUADOR SRI / FACTURA ELECTRONICA | `<factura id="comprobante"` (toute version) |
| ECUADOR SRI 1.0.0 | `<factura id="comprobante" version="1.0.0">` |
| ECUADOR SRI 1.1.0 | `<factura id="comprobante" version="1.1.0">` |
| ECUADOR SRI 2.0.0 | `<factura id="comprobante" version="2.0.0">` |
| ECUADOR SRI 2.1.0 | `<factura id="comprobante" version="2.1.0">` |

L'élément racine est `<factura>` avec `id="comprobante"`. L'attribut `version` détermine la version SRI spécifique. La classification utilise le principe du **premier modèle correspondant**, trié par longueur de modèle (du plus long/spécifique au plus court).

## Liens connexes

- [Normes e-Facture actuellement prises en charge](../../currently-supported-e-invoice-standards/)
- [Documents électroniques pris en charge](./)
