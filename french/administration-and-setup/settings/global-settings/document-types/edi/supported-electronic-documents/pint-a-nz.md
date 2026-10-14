---
description: Prise en charge des documents électroniques PINT A-NZ dans DocBits
---

# 🇦🇺 PINT A-NZ

| Propriété | Valeur |
|----------|-------|
| **Pays / Région** | Australie / Nouvelle-Zélande |
| **Types de document** | Facture, Note de crédit |
| **Format** | UBL 2.1 XML |
| **Norme** | PINT A-NZ (Modèle Peppol International pour l'Australie-Nouvelle-Zélande) |
| **Paramètre régional** | `en_AU` |

PINT A-NZ (Modèle Peppol International pour l'Australie-Nouvelle-Zélande) est la spécification de facturation Peppol localisée pour la région Australie/Nouvelle-Zélande. Il étend le modèle PINT global avec des règles métier spécifiques à l'A-NZ, des catégories fiscales (GST) et des schémas d'identifiants (ABN, NZBN). Il s'agit de la page de référence technique avec le mappage complet des champs.

## État de la prise en charge

| Composant | État |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="aunz-pint-preview.png" alt="Aperçu de facture PINT A-NZ dans DocBits"><figcaption><p>Aperçu par défaut de DocBits pour une facture PINT A-NZ</p></figcaption></figure>

## Mappage des champs

### Champs d'en-tête

| Champ DocBits | XPath source (UBL 2.1) | Remarques |
|---|---|---|
| `invoice_id` | `cbc:ID` | Numéro de facture |
| `invoice_date` | `cbc:IssueDate` | Date ISO 8601 |
| `due_date` | `cbc:DueDate` | Date d'échéance |
| `currency` | `cbc:DocumentCurrencyCode` | Généralement `AUD` ou `NZD` |
| `total_amount` | `cbc:PayableAmount` (dans `cac:LegalMonetaryTotal`) | Total TTC (incl. GST) |
| `net_amount` | `cbc:TaxExclusiveAmount` (dans `cac:LegalMonetaryTotal`) | Sous-total HT (excl. GST) |
| `tax_amount` | `cbc:TaxAmount` (dans `cac:TaxTotal`) | Montant de la GST |
| `purchase_order` | `cbc:BuyerReference` | Référence BC de l'acheteur |
| `payment_terms` | `cbc:Note` (dans `cac:PaymentTerms`) | Conditions de paiement en texte libre |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Nom du fournisseur |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID` | ABN (schemeID 0151) |
| `supplier_tax_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | ABN ou numéro GST |
| `supplier_street` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Rue du fournisseur |
| `supplier_city` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName` | Ville du fournisseur |
| `supplier_postal_code` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Code postal du fournisseur |
| `supplier_country` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | Code pays ISO (`AU` ou `NZ`) |
| `buyer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Nom de l'acheteur |
| `buyer_id` | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID` | ABN/NZBN (schemeID 0151) |
| `buyer_street` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Rue de l'acheteur |
| `buyer_city` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName` | Ville de l'acheteur |
| `buyer_postal_code` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Code postal de l'acheteur |
| `buyer_country` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | Code pays ISO |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | ID du compte de paiement |

### Tableau des lignes d'article (`INVOICE_TABLE`)

Chemin des lignes : `cac:InvoiceLine`

| Colonne | XPath source (UBL 2.1) | Remarques |
|---|---|---|
| `POSITION` | `cbc:ID` | Numéro de ligne |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Description du produit/service |
| `QUANTITY` | `cbc:InvoicedQuantity` | Quantité (code d'unité dans `@unitCode`) |
| `UNIT` | `cbc:InvoicedQuantity/@unitCode` | Code d'unité (ex. `C62` = pièce, `EA` = chacun) |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Prix unitaire HT (excl. GST) |
| `VAT_RATE` | `cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` | Taux de GST en % |
| `VAT` | *(calculé à partir du montant des taxes)* | Montant de GST par ligne |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Total de ligne HT (excl. GST) |

## Règle de classification

DocBits détecte les documents PINT A-NZ en faisant correspondre l'élément `CustomizationID` :

```
urn:peppol.org:pint:billing-1@aunz
```

Pour les documents d'autofacturation, le motif est :

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Les deux sont classés sous le type de document électronique `PINT A-NZ`.

## Voir aussi

- [AUNZ PINT](aunz-pint.md) — Aperçu et fonctionnalités spécifiques à l'A-NZ
- [AUNZ PINT Self-Billing](aunz-pint-self-billing.md) — Variante d'autofacturation
- [Documents électroniques pris en charge](./)