---
description: Prise en charge de la facture électronique GST indienne dans DocBits
---

# 🇮🇳 India GST E-Invoice

| Propriété | Valeur |
|----------|-------|
| **Pays / Région** | Inde |
| **Types de documents** | Facture (INV), Note de crédit (CRN), Note de débit (DBN) |
| **Format** | XML (`<SignedInvoice>`) |
| **Standard** | GST E-Invoice (GSTN Invoice Registration Portal) |
| **Locale** | `en_IN` |

La facture électronique GST indienne est le standard de facturation électronique obligatoire dans le cadre du régime de taxe sur les biens et services (GST) de l'Inde, géré par le GSTN (GST Network). Les entreprises dépassant le seuil de chiffre d'affaires prescrit doivent générer des e-Factures via le portail d'enregistrement des factures (IRP), qui signe la facture et retourne un **IRN** (Invoice Reference Number — un hash SHA-256 de 64 caractères) et un code QR.

DocBits détecte les documents GST E-Invoice par la présence de `<SignedInvoice>` comme élément racine. Le format inclut trois composantes fiscales GST :

| Composante fiscale | Description |
|--------------|-------------|
| IGST | GST intégré — appliqué aux transactions entre États |
| CGST | GST central — appliqué aux transactions intra-État (composante centrale) |
| SGST | GST d'État — appliqué aux transactions intra-État (composante d'État) |

L'identifiant du contribuable est le **GSTIN** (Goods and Services Tax Identification Number), un code alphanumérique de 15 caractères au format `29AABCU9603R1ZM` (code d'État sur 2 chiffres + PAN sur 10 chiffres + numéro d'entité + chiffre de contrôle). Les dates utilisent le format `JJ/MM/AAAA`.

## Statut de support

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction de champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="india-gst-e-invoice-preview.png" alt="India GST E-Invoice preview in DocBits"><figcaption><p>Aperçu DocBits par défaut pour une facture électronique GST indienne</p></figcaption></figure>

## Correspondance des champs

### Champs d'en-tête

| Champ DocBits | Élément XML source | Notes |
|---|---|---|
| `invoice_id` | `Invoice/DocDtls/No` | Numéro de facture |
| `invoice_date` | `Invoice/DocDtls/Dt` | Date d'émission (`JJ/MM/AAAA`) |
| `invoice_type` | `Invoice/DocDtls/Typ` | INV=Facture, CRN=Note de crédit, DBN=Note de débit |
| `currency` | Fixe : `INR` | Toujours en roupie indienne |
| `net_amount` | `Invoice/ValDtls/AssVal` | Valeur imposable / taxable |
| `tax_amount` | `Invoice/ValDtls/IgstVal` + `CgstVal` + `SgstVal` | Montant total de la GST |
| `total_amount` | `Invoice/ValDtls/TotInvVal` | Valeur totale de la facture incl. GST |
| `igst_amount` | `Invoice/ValDtls/IgstVal` | Montant de la GST intégrée |
| `cgst_amount` | `Invoice/ValDtls/CgstVal` | Montant de la GST centrale |
| `sgst_amount` | `Invoice/ValDtls/SgstVal` | Montant de la GST d'État |
| `cess_amount` | `Invoice/ValDtls/CesVal` | Montant de la taxe supplémentaire (le cas échéant) |
| `supplier_name` | `Invoice/SellerDtls/LglNm` | Nom légal du vendeur |
| `supplier_id` | `Invoice/SellerDtls/Gstin` | GSTIN du vendeur (15 caractères, ex. `29AABCU9603R1ZM`) |
| `supplier_trade_name` | `Invoice/SellerDtls/TrdNm` | Nom commercial du vendeur |
| `supplier_address` | `Invoice/SellerDtls/Addr1` | Adresse du vendeur ligne 1 |
| `supplier_city` | `Invoice/SellerDtls/Loc` | Ville / localisation du vendeur |
| `supplier_postal_code` | `Invoice/SellerDtls/Pin` | Code PIN du vendeur |
| `supplier_state_code` | `Invoice/SellerDtls/Stcd` | Code d'État du vendeur (2 chiffres) |
| `buyer_name` | `Invoice/BuyerDtls/LglNm` | Nom légal de l'acheteur |
| `buyer_id` | `Invoice/BuyerDtls/Gstin` | GSTIN de l'acheteur |
| `buyer_trade_name` | `Invoice/BuyerDtls/TrdNm` | Nom commercial de l'acheteur |
| `buyer_address` | `Invoice/BuyerDtls/Addr1` | Adresse de l'acheteur ligne 1 |
| `buyer_city` | `Invoice/BuyerDtls/Loc` | Ville / localisation de l'acheteur |
| `buyer_postal_code` | `Invoice/BuyerDtls/Pin` | Code PIN de l'acheteur |
| `buyer_state_code` | `Invoice/BuyerDtls/Stcd` | Code d'État de l'acheteur |
| `irn` | `Irn` | Numéro de référence de facture (hash SHA-256 de 64 caractères) |
| `ack_number` | `AckNo` | Numéro d'accusé de réception IRP |
| `ack_date` | `AckDt` | Date d'accusé de réception IRP |

### Tableau des lignes (`INVOICE_TABLE`)

Chemin de ligne : `Invoice/ItemList/Item`

| Colonne | Élément XML source | Notes |
|---|---|---|
| `POSITION` | `SlNo` | Numéro de séquence de ligne |
| `DESCRIPTION` | `PrdDesc` | Description du produit / service |
| `QUANTITY` | `Qty` | Quantité facturée |
| `UNIT` | `Unit` | Unité de mesure (ex. `OTH`, `NOS`, `KGS`) |
| `UNIT_PRICE` | `UnitPrice` | Prix unitaire |
| `VAT_RATE` | `GstRt` | Taux de GST en % (ex. 18%) |
| `VAT` | `IgstAmt` (ou `CgstAmt` + `SgstAmt`) | Montant de la GST par ligne |
| `NET_AMOUNT` | `AssAmt` | Montant imposable par ligne |

## Règle de classification

DocBits détecte les documents India GST E-Invoice en faisant correspondre l'élément racine :

| Type de document électronique | Modèle |
|--------------------------|---------|
| INDIA GST E-INVOICE | L'élément racine contient `<SignedInvoice` |

## Voir aussi

- [Standards de facture électronique actuellement pris en charge](../../currently-supported-e-invoice-standards/)
- [Documents électroniques pris en charge](./)
