---
description: Prise en charge des documents électroniques TEAPPSXML de Finlande dans DocBits
---

# 🇫🇮 Finlande TEAPPSXML

| Propriété | Valeur |
|----------|-------|
| **Pays / Région** | Finlande |
| **Types de documents** | Facture, Note de crédit |
| **Format** | XML |
| **Norme** | TEAPPSXML 3.0 (Tieto / Secteur bancaire finlandais) |
| **Paramètres régionaux** | `fi_FI` |

TEAPPSXML (Tietotekniikan ja viestinnän toimiala) est une norme de facture électronique finlandaise utilisée principalement dans le secteur bancaire et financier. L'élément racine est `<TEAPPSXML>` avec l'espace de noms `urn:TEAPPSXML:3.0`. DocBits détecte les documents TEAPPSXML par la présence de `xmlns="urn:TEAPPSXML:"` dans l'élément racine.

Le format TEAPPSXML utilise des noms d'éléments en majuscules et une structure plate avec des sections séparées `<SENDER>`, `<RECEIVER>`, `<INVOICE>` et `<PAYMENTINFO>`. Le format de l'identifiant d'entreprise finlandais (Y-tunnus) est `1234567-8`, et les numéros de TVA utilisent le préfixe `FI` (ex. `FI12345678`).

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="finland-teappsxml-preview.png" alt="Aperçu de facture TEAPPSXML de Finlande dans DocBits"><figcaption><p>Aperçu par défaut DocBits pour une facture TEAPPSXML de Finlande</p></figcaption></figure>

## Correspondance des champs

### Champs d'en-tête

| Champ DocBits | Élément XML source | Notes |
|---|---|---|
| `invoice_id` | `INVOICE/INVOICENUMBER` | Numéro de facture |
| `invoice_date` | `INVOICE/INVOICEDATE` | Date d'émission (AAAA-MM-JJ) |
| `due_date` | `INVOICE/DUEDATE` | Date d'échéance de paiement (AAAA-MM-JJ) |
| `invoice_type` | `INVOICE/INVOICE_TYPE` | Type de message (INVOICE) |
| `currency` | `INVOICE/CURRENCY` | Code devise (généralement `EUR`) |
| `purchase_order` | `INVOICE/REFERENCENUMBER` | Numéro de référence de paiement |
| `payment_reference` | `INVOICE/REFERENCENUMBER` | Référence de paiement finlandaise (viitenumero) |
| `net_amount` | `INVOICE/TOTALVATEXCLUDED` | Montant net HT |
| `tax_amount` | `INVOICE/TOTALVAT` | Montant total de TVA |
| `total_amount` | `INVOICE/TOTALAMOUNT` | Montant total TTC |
| `payment_terms` | `INVOICE/PAYMENT_TERMS` | Mode de paiement (ex. `BANKTRANSFER`) |
| `supplier_name` | `SENDER/NAME` | Nom de la société expéditrice |
| `supplier_id` | `SENDER/ID` | Identifiant d'entreprise finlandais (Y-tunnus, ex. `1234567-8`) |
| `supplier_tax_id` | `SENDER/VATNUMBER` | Numéro de TVA (ex. `FI12345678`) |
| `supplier_address` | `SENDER/ADDRESS/STREET` | Adresse de l'expéditeur |
| `supplier_city` | `SENDER/ADDRESS/CITY` | Ville de l'expéditeur |
| `supplier_postal_code` | `SENDER/ADDRESS/POSTCODE` | Code postal de l'expéditeur |
| `supplier_country` | `SENDER/ADDRESS/COUNTRY` | Code pays ISO (`FI`) |
| `supplier_bic` | `SENDER/BANK/BIC` | Code BIC de la banque de l'expéditeur |
| `buyer_name` | `INVOICE/BUYER/NAME` | Nom de la société acheteur |
| `buyer_id` | `INVOICE/BUYER/ID` | Identifiant d'entreprise finlandais de l'acheteur |
| `buyer_address` | `INVOICE/BUYER/ADDRESS_LINE_1` | Adresse de l'acheteur |
| `buyer_city` | `INVOICE/BUYER/CITY` | Ville de l'acheteur |
| `buyer_postal_code` | `INVOICE/BUYER/POSTAL_CODE` | Code postal de l'acheteur |
| `buyer_country` | `INVOICE/BUYER/COUNTRY` | Code pays ISO (`FI`) |
| `iban` | `PAYMENTINFO/BENEFICIARYACCOUNT/IBAN` | IBAN du bénéficiaire |
| `bic` | `PAYMENTINFO/BENEFICIARYACCOUNT/BIC` | Code BIC du bénéficiaire |

### Tableau des lignes (`INVOICE_TABLE`)

Chemin de ligne : `INVOICE/LINES/LINE`

| Colonne | Élément XML source | Notes |
|---|---|---|
| `POSITION` | `LINENUMBER` | Numéro de séquence de ligne |
| `DESCRIPTION` | `ARTICLENAME` | Nom / description de l'article |
| `QUANTITY` | `QUANTITY` | Quantité facturée |
| `UNIT` | `UNIT` | Unité de mesure (ex. `KPL` = pièce) |
| `UNIT_PRICE` | `UNITPRICE` | Prix unitaire HT |
| `VAT_RATE` | `VATRATE` | Taux de TVA en % (standard 25,5%) |
| `VAT` | Calculé | Montant de TVA par ligne |
| `NET_AMOUNT` | `LINEAMOUNT` | Total de ligne HT |

## Règle de classification

DocBits détecte les documents TEAPPSXML en faisant correspondre l'attribut `xmlns` sur l'élément racine `<TEAPPSXML>` :

| Type de document électronique | Motif |
|--------------------------|---------|
| TEAPPSXML | `xmlns` contient `urn:TEAPPSXML:` |

## Voir aussi

- [Normes de facturation électronique actuellement prises en charge](../../currently-supported-e-invoice-standards/)
- [Finlande Finvoice](./finland-finvoice.md)
- [Documents électroniques pris en charge](./)
