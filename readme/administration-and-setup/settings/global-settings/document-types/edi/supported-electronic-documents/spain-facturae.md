---
description: Espagne Facturae (3.2, 3.2.1, 3.2.2) – Prise en charge des documents électroniques dans DocBits
---

# 🇪🇸 Espagne Facturae

| Propriété | Valeur |
|-----------|--------|
| **Pays / Région** | Espagne |
| **Types de documents** | Facture (Factura), Note de crédit |
| **Format** | XML |
| **Norme** | Facturae 3.2 / 3.2.1 / 3.2.2 (Agencia Tributaria / AEAT) |
| **Locale** | `es_ES` |

Facturae est la norme espagnole obligatoire de facturation électronique, régie par l'Agencia Estatal de Administración Tributaria (AEAT) et le Ministère des Finances. Elle est obligatoire pour les factures adressées aux entités du secteur public espagnol et largement utilisée dans les transactions B2B. L'élément racine est `<fe:Facturae>` avec une URL d'espace de noms versionnée. DocBits détecte la version via l'attribut `xsi:schemaLocation`, qui référence l'une des URL de schéma officielles :

| Version | URL du schéma |
|---------|--------------|
| Facturae 3.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2.xml` |
| Facturae 3.2.1 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_1.xml` |
| Facturae 3.2.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_2.xml` |

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="spain-facturae-preview.png" alt="Aperçu de la facture Espagne Facturae dans DocBits"><figcaption><p>Aperçu par défaut de DocBits pour une facture Espagne Facturae 3.2.2</p></figcaption></figure>

## Correspondance des champs

### Champs d'en-tête

| Champ DocBits | Élément XML source | Notes |
|---|---|---|
| `invoice_id` | `Invoices/Invoice/InvoiceHeader/InvoiceNumber` | Numéro de facture |
| `invoice_date` | `Invoices/Invoice/InvoiceIssueData/IssueDate` | Date d'émission (AAAA-MM-JJ) |
| `due_date` | `PaymentDetails/Installment/InstallmentDueDate` | Date d'échéance du paiement |
| `invoice_type` | `Invoices/Invoice/InvoiceHeader/InvoiceDocumentType` | FC=Facture, NC=Note de crédit |
| `currency` | `Invoices/Invoice/InvoiceIssueData/InvoiceCurrencyCode` | Toujours `EUR` |
| `purchase_order` | `Invoices/Invoice/InvoiceHeader/ReceiverContractReference` | Référence commande / contrat de l'acheteur |
| `net_amount` | `Invoices/Invoice/InvoiceTotals/TotalGrossAmountBeforeTaxes` | Montant net HT |
| `tax_amount` | `Invoices/Invoice/InvoiceTotals/TotalTaxOutputs` | Montant total de TVA |
| `total_amount` | `Invoices/Invoice/InvoiceTotals/InvoiceTotal` | Montant total TTC |
| `tax_rate` | `TaxesOutputs/Tax/TaxRate` | Taux de TVA en % (standard 21%) |
| `payment_terms` | `PaymentDetails/Installment/PaymentMeans` | Code du moyen de paiement |
| `supplier_name` | `Parties/SellerParty/LegalEntity/CorporateName` | Nom du fournisseur |
| `supplier_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF (ex. `ES12345678A`) |
| `supplier_tax_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF ou CIF espagnol |
| `supplier_address` | `Parties/SellerParty/LegalEntity/AddressInSpain/Address` | Adresse du fournisseur |
| `supplier_city` | `Parties/SellerParty/LegalEntity/AddressInSpain/Town` | Ville du fournisseur |
| `supplier_postal_code` | `Parties/SellerParty/LegalEntity/AddressInSpain/PostCode` | Code postal du fournisseur |
| `supplier_country` | `Parties/SellerParty/LegalEntity/AddressInSpain/CountryCode` | Code pays ISO (`ESP`) |
| `buyer_name` | `Parties/BuyerParty/LegalEntity/CorporateName` | Nom de l'acheteur |
| `buyer_id` | `Parties/BuyerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF de l'acheteur |
| `buyer_address` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Address` | Adresse de l'acheteur |
| `buyer_city` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Town` | Ville de l'acheteur |
| `buyer_postal_code` | `Parties/BuyerParty/LegalEntity/AddressInSpain/PostCode` | Code postal de l'acheteur |
| `buyer_country` | `Parties/BuyerParty/LegalEntity/AddressInSpain/CountryCode` | Code pays ISO (`ESP`) |
| `iban` | `PaymentDetails/Installment/AccountToBeCredited/IBAN` | IBAN du bénéficiaire |

### Tableau des lignes (`INVOICE_TABLE`)

Chemin de ligne : `Invoices/Invoice/Items/InvoiceLine`

| Colonne | Élément XML source | Notes |
|---|---|---|
| `POSITION` | `ItemDescription` | Séquence / description utilisée comme identifiant |
| `DESCRIPTION` | `ItemDescription` | Description de l'article |
| `QUANTITY` | `Quantity` | Quantité facturée |
| `UNIT` | `UnitOfMeasure` | Unité de mesure (ex. `units`) |
| `UNIT_PRICE` | `UnitPriceWithoutTax` | Prix unitaire HT |
| `VAT_RATE` | `TaxesOutputs/Tax/TaxRate` | Taux de TVA en % (généralement 21%) |
| `VAT` | `TaxesOutputs/Tax/TaxAmount/TotalAmount` | Montant de TVA par ligne |
| `NET_AMOUNT` | `TotalCost` | Total de la ligne HT |

## Règles de classification

DocBits détecte les documents Facturae en faisant correspondre l'attribut `xsi:schemaLocation` sur l'élément racine `<fe:Facturae>` :

| Type de document électronique | Motif |
|------------------------------|-------|
| FACTURAE 3.2 | `xsi:schemaLocation` contient `Facturaev3_2.xml` (pas 3_2_1 ou 3_2_2) |
| FACTURAE 3.2.1 | `xsi:schemaLocation` contient `Facturaev3_2_1.xml` |
| FACTURAE 3.2.2 | `xsi:schemaLocation` contient `Facturaev3_2_2.xml` |

L'élément racine est `<fe:Facturae>` avec l'espace de noms `http://www.facturae.es/Facturae/2014/v3.2.2/Facturae` (spécifique à la version). La classification utilise le principe **premier correspondant gagne**, avec les motifs plus spécifiques (3.2.2, 3.2.1) évalués avant le générique 3.2.

## Voir aussi

- [Normes e-facture actuellement prises en charge](../../currently-supported-e-invoice-standards/)
- [Documents électroniques pris en charge](./)
