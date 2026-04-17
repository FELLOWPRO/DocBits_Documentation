---
description: Prise en charge des documents électroniques CHINA FAPIAO dans DocBits
---

# 🇨🇳 CHINA FAPIAO

| Propriété | Valeur |
|----------|-------|
| **Pays / Région** | Chine |
| **Types de documents** | Facture TVA générale, Facture TVA spéciale, E-Fapiao |
| **Format** | XML |
| **Norme** | Fapiao (发票), State Taxation Administration |
| **Locale** | `zh_CN` |
| **Namespace XML** | `urn:china:tax:fapiao:1.0` |

Fapiao (发票) est le système chinois de facturation fiscale électronique réglementé par la State Taxation Administration (国家税务总局). Tous les documents Fapiao partagent le namespace XML `urn:china:tax:fapiao:1.0`. DocBits détecte automatiquement le type de Fapiao et achemine vers les règles d'extraction appropriées :

| Type de Fapiao | Code | Description |
|-----------|------|-------------|
| 普通发票 | General VAT Invoice | Facture TVA générale (普通发票) |
| 专用发票 | Special VAT Invoice | Facture TVA spéciale (专用发票) — déductible |

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="china-fapiao-preview.png" alt="Aperçu de facture China Fapiao dans DocBits"><figcaption><p>Aperçu par défaut DocBits pour une CHINA GENERAL VAT INVOICE (普通发票)</p></figcaption></figure>

## Mappage des champs

### Champs d'en-tête

| Champ DocBits | Élément XML source | Remarques |
|---|---|---|
| `invoice_id` | `fapiao_number` | Numéro de facture (8 chiffres) |
| `invoice_code` | `fapiao_code` | Code de facture (10-12 chiffres) |
| `invoice_date` | `issue_date` | Date d'émission ISO 8601 |
| `fapiao_type` | `fapiao_type` | Type : 普通发票 ou 专用发票 |
| `check_code` | `check_code` | Code de vérification (20 chiffres) |
| `machine_code` | `machine_code` | Numéro de machine fiscale |
| `currency` | Fixe : `CNY` | Toujours yuan chinois |
| `total_amount` | `total_with_tax` | Montant total TTC (价税合计) |
| `net_amount` | `total_amount` | Montant net HT (金额) |
| `tax_amount` | `total_tax` | Montant de la TVA (税额) |
| `amount_in_words` | `amount_in_words` | Montant en caractères chinois (大写) |
| `supplier_name` | `seller/name` | Nom de l'entreprise émettrice (销售方) |
| `supplier_id` | `seller/taxpayer_id` | Identifiant fiscal de l'émetteur (18 caractères) |
| `supplier_address` | `seller/address` | Adresse de l'émetteur |
| `supplier_telephone` | `seller/telephone` | Téléphone de l'émetteur |
| `supplier_bank_name` | `seller/bank_name` | Banque de l'émetteur |
| `supplier_bank_account` | `seller/bank_account` | Compte bancaire de l'émetteur |
| `buyer_name` | `buyer/name` | Nom de l'entreprise destinataire (购买方) |
| `buyer_id` | `buyer/taxpayer_id` | Identifiant fiscal du destinataire |
| `buyer_address` | `buyer/address` | Adresse du destinataire |
| `buyer_telephone` | `buyer/telephone` | Téléphone du destinataire |
| `remarks` | `remarks` | Remarques (备注) |
| `issuer` | `issuer` | Émetteur (开票人) |
| `tax_authority` | `tax_authority` | Autorité fiscale (税务机关) |

### Tableau des lignes (`INVOICE_TABLE`)

Chemin de la ligne : `items/item`

| Colonne | Élément XML source | Remarques |
|---|---|---|
| `SEQ` | `seq` | Numéro de ligne |
| `ITEM_NAME` | `name` | Désignation de l'article |
| `SPEC` | `spec` | Spécification / modèle |
| `UNIT` | `unit` | Unité de mesure |
| `QUANTITY` | `quantity` | Quantité |
| `UNIT_PRICE` | `unit_price` | Prix unitaire HT |
| `AMOUNT` | `amount` | Total de la ligne HT |
| `TAX_RATE` | `tax_rate` | Taux de TVA en % (13% ou 9%) |
| `TAX_AMOUNT` | `tax_amount` | TVA par ligne |

## Règles de classification

DocBits détecte les documents China Fapiao en faisant correspondre le namespace XML et le type de Fapiao :

| Type de document électronique | Modèle |
|--------------------------|---------|
| CHINA GENERAL VAT INVOICE | `<fapiao xmlns="urn:china:tax:fapiao:1.0" version="1.0">` |
| CHINA SPECIAL VAT INVOICE | `<fapiao xmlns="urn:china:tax:fapiao:1.0"` + `<fapiao_type>专用发票</fapiao_type>` |
| CHINA FAPIAO | `<fapiao` (correspondance générique) |
| CHINA FAPIAO | `税务总局` (correspondance texte) |
| CHINA VAT INVOICE | `<VATInvoice` (format hérité) |

La classification utilise le principe **FIRST MATCH WINS** trié par longueur de motif (le plus long d'abord). L'élément racine est `<fapiao>` avec le namespace `urn:china:tax:fapiao:1.0`.

## Voir aussi

- [Normes de e-facturation actuellement prises en charge](../../currently-supported-e-invoice-standards/)
- [Documents électroniques pris en charge](./)
