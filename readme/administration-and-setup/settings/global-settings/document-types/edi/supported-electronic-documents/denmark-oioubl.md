---
description: Prise en charge des documents électroniques Denmark OIOUBL 2.1 dans DocBits
---

# 🇩🇰 Denmark OIOUBL 2.1

| Propriété | Valeur |
|----------|-------|
| **Pays / Région** | Danemark |
| **Types de documents** | Invoice (Faktura), Credit Note |
| **Format** | XML (UBL 2.1) |
| **Standard** | OIOUBL 2.1 (Offentlig Information Online UBL) |
| **Locale** | `da_DK` |

OIOUBL (Offentlig Information Online UBL) est le standard danois de facturation électronique basé sur UBL 2.1. Il est obligatoire pour les factures destinées aux entités du secteur public danois et largement utilisé dans les transactions B2B. DocBits détecte les documents OIOUBL 2.1 par la présence de `<cbc:CustomizationID>OIOUBL-2.1</cbc:CustomizationID>`. L'identifiant de profil `urn:www.nesubl.eu:profiles:profile5:ver2.0` indique le profil de facture NES (Northern European Subset).

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction de champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="denmark-oioubl-preview.png" alt="Aperçu de la facture Denmark OIOUBL 2.1 dans DocBits"><figcaption><p>Aperçu par défaut DocBits pour une facture Denmark OIOUBL 2.1 (Faktura)</p></figcaption></figure>

## Correspondance des champs

### Champs d'en-tête

| Champ DocBits | Élément XML source | Notes |
|---|---|---|
| `invoice_id` | `cbc:ID` | Numéro de facture |
| `invoice_date` | `cbc:IssueDate` | Date d'émission ISO 8601 |
| `due_date` | `cbc:DueDate` | Date d'échéance de paiement |
| `invoice_type` | `cbc:InvoiceTypeCode` | Code UNCL 1001 (380=Facture, 381=Note de crédit) |
| `currency` | `cbc:DocumentCurrencyCode` | Toujours `DKK` (Couronne danoise) |
| `purchase_order` | `cac:OrderReference/cbc:ID` | Numéro de référence de commande de l'acheteur |
| `buyer_reference` | `cbc:BuyerReference` | Référence interne de l'acheteur / numéro de localisation EAN |
| `note` | `cbc:Note` | Instructions de paiement ou notes en texte libre |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Montant net hors TVA |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Montant total de TVA (taux standard 25%) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Montant total TVA incluse |
| `tax_rate` | `cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` | Taux de TVA en % |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Nom de la société fournisseur |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` | Numéro CVR (ex. `DK12345678`) |
| `supplier_vat` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Numéro TVA/CVR |
| `supplier_address` | `cac:AccountingSupplierParty/.../cbc:StreetName` | Adresse du fournisseur |
| `supplier_city` | `cac:AccountingSupplierParty/.../cbc:CityName` | Ville du fournisseur |
| `supplier_postal_code` | `cac:AccountingSupplierParty/.../cbc:PostalZone` | Code postal du fournisseur |
| `supplier_country` | `cac:AccountingSupplierParty/.../cbc:IdentificationCode` | Code pays ISO (`DK`) |
| `customer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Nom de la société client |
| `customer_id` | `cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` | Numéro CVR |
| `customer_vat` | `cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Numéro TVA/CVR |
| `customer_address` | `cac:AccountingCustomerParty/.../cbc:StreetName` | Adresse du client |
| `customer_city` | `cac:AccountingCustomerParty/.../cbc:CityName` | Ville du client |
| `customer_postal_code` | `cac:AccountingCustomerParty/.../cbc:PostalZone` | Code postal du client |
| `customer_country` | `cac:AccountingCustomerParty/.../cbc:IdentificationCode` | Code pays ISO (`DK`) |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Compte bancaire / IBAN |
| `bic` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID` | Code BIC/SWIFT |

### Tableau des lignes (`INVOICE_TABLE`)

Chemin de ligne : `cac:InvoiceLine`

| Colonne | Élément XML source | Notes |
|---|---|---|
| `POSITION` | `cbc:ID` | Numéro de séquence de ligne |
| `DESCRIPTION` | `cac:Item/cbc:Name` | Nom / description de l'article |
| `QUANTITY` | `cbc:InvoicedQuantity` | Quantité facturée |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Prix unitaire hors TVA |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Total de ligne hors TVA |

## Règle de classification

DocBits détecte les documents OIOUBL 2.1 en faisant correspondre l'élément `CustomizationID` :

| Type de document électronique | Modèle |
|--------------------------|---------|
| OIOUBL 2.1 | `<cbc:CustomizationID>OIOUBL-2\.1\s*</cbc:CustomizationID>` |

L'élément racine est `<Invoice>` (ou `<CreditNote>`) dans l'espace de noms UBL 2.1 `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`.

## Liens connexes

- [Standards de facturation électronique actuellement pris en charge](../../currently-supported-e-invoice-standards/)
- [Documents électroniques pris en charge](./)
