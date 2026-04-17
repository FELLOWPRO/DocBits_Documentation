---
description: Prise en charge des documents électroniques Finvoice de Finlande (1.3, 2.0, 2.01, 3.0) dans DocBits
---

# 🇫🇮 Finlande Finvoice

| Propriété | Valeur |
|----------|-------|
| **Pays / Région** | Finlande |
| **Types de documents** | Facture (Lasku), Note de crédit (Hyvityslasku) |
| **Format** | XML |
| **Norme** | Finvoice 1.3 / 2.0 / 2.01 / 3.0 (Finance Finland / Finanssiala) |
| **Paramètres régionaux** | `fi_FI` |

Finvoice est la norme de facturation électronique du secteur bancaire finlandais, développée et maintenue par Finance Finland (Finanssiala ry). Elle est utilisée aussi bien pour la facturation B2B que B2G et est transmise via l'infrastructure bancaire finlandaise. L'élément racine est `<Finvoice>` avec une URL d'espace de noms versionnée. DocBits détecte la version via l'attribut `xmlns` :

| Version | URL d'espace de noms |
|---------|--------------|
| Finvoice 1.3 | `http://www.finvoice.fi/schema/finvoice13` |
| Finvoice 2.0 | `http://www.finvoice.fi/schema/finvoice20` |
| Finvoice 2.01 | `http://www.finvoice.fi/schema/finvoice201` |
| Finvoice 3.0 | `http://www.finvoice.fi/schema/finvoice30` |

Le format de l'identifiant d'entreprise finlandais (Y-tunnus) est `1234567-8` (7 chiffres + chiffre de contrôle), utilisé comme identifiant de partie. Le numéro de TVA a le préfixe `FI` suivi de 8 chiffres (ex. `FI12345678`). Les dates sont encodées au format `CCYYMMDD`.

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="finland-finvoice-preview.png" alt="Aperçu de facture Finvoice 3.0 de Finlande dans DocBits"><figcaption><p>Aperçu par défaut DocBits pour une facture Finvoice 3.0 de Finlande (Lasku)</p></figcaption></figure>

## Correspondance des champs

### Champs d'en-tête

| Champ DocBits | Élément XML source | Notes |
|---|---|---|
| `invoice_id` | `InvoiceDetails/InvoiceNumber` | Numéro de facture |
| `invoice_date` | `InvoiceDetails/InvoiceDate` | Date au format `CCYYMMDD`, convertie en ISO 8601 |
| `due_date` | `InvoiceDetails/PaymentTermsDetails/InvoiceDueDate` | Date d'échéance de paiement (`CCYYMMDD`) |
| `invoice_type` | `InvoiceDetails/InvoiceTypeCode` | INV01=Facture, CRE01=Note de crédit |
| `currency` | `InvoiceDetails/InvoiceTotalVatExcludedAmount/@AmountCurrencyIdentifier` | Code devise (généralement `EUR`) |
| `net_amount` | `InvoiceDetails/InvoiceTotalVatExcludedAmount` | Montant net HT |
| `tax_amount` | `InvoiceDetails/InvoiceTotalVatAmount` | Montant total de TVA |
| `total_amount` | `InvoiceDetails/InvoiceTotalVatIncludedAmount` | Montant total TTC |
| `tax_rate` | `InvoiceDetails/VatSpecificationDetails/VatRatePercent` | Taux de TVA en % (standard 25,5%) |
| `supplier_name` | `SellerPartyDetails/SellerOrganisationName` | Nom de la société fournisseur |
| `supplier_id` | `SellerPartyDetails/SellerPartyIdentifier` | Identifiant d'entreprise finlandais (Y-tunnus, ex. `1234567-8`) |
| `supplier_vat` | `SellerPartyDetails/SellerOrganisationTaxCode` | Numéro de TVA (ex. `FI12345678`) |
| `supplier_address` | `SellerPartyDetails/SellerPostalAddressDetails/SellerStreetName` | Adresse du fournisseur |
| `supplier_city` | `SellerPartyDetails/SellerPostalAddressDetails/SellerTownName` | Ville du fournisseur |
| `supplier_postal_code` | `SellerPartyDetails/SellerPostalAddressDetails/SellerPostCodeIdentifier` | Code postal du fournisseur |
| `supplier_country` | `SellerPartyDetails/SellerPostalAddressDetails/CountryCode` | Code pays ISO (`FI`) |
| `buyer_name` | `BuyerPartyDetails/BuyerOrganisationName` | Nom de la société acheteur |
| `buyer_id` | `BuyerPartyDetails/BuyerPartyIdentifier` | Identifiant d'entreprise finlandais (Y-tunnus) |
| `buyer_address` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerStreetName` | Adresse de l'acheteur |
| `buyer_city` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerTownName` | Ville de l'acheteur |
| `buyer_postal_code` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerPostCodeIdentifier` | Code postal de l'acheteur |
| `buyer_country` | `BuyerPartyDetails/BuyerPostalAddressDetails/CountryCode` | Code pays ISO (`FI`) |
| `iban` | `EpiDetails/EpiBfiPartyDetails/EpiBfiIdentifier` | IBAN du bénéficiaire (détails de paiement EPI) |
| `bic` | `EpiDetails/EpiPaymentInstructionId` | Code BIC/SWIFT |
| `payment_terms` | `InvoiceDetails/PaymentTermsDetails/PaymentTermsFreeText` | Conditions de paiement en texte libre |

### Tableau des lignes (`INVOICE_TABLE`)

Chemin de ligne : `InvoiceRow`

| Colonne | Élément XML source | Notes |
|---|---|---|
| `POSITION` | `InvoiceRow/ArticleIdentifier` | Code article / produit |
| `DESCRIPTION` | `InvoiceRow/ArticleName` | Nom / description de l'article |
| `QUANTITY` | `InvoiceRow/DeliveredQuantity` | Quantité livrée |
| `UNIT` | `InvoiceRow/DeliveredQuantity/@QuantityUnitCode` | Code unité (ex. `KPL` = pièce) |
| `UNIT_PRICE` | `InvoiceRow/UnitPriceAmount` | Prix unitaire HT |
| `VAT_RATE` | `InvoiceRow/RowVatRatePercent` | Taux de TVA en % par ligne |
| `VAT` | `InvoiceRow/RowVatAmount` | Montant de TVA par ligne |
| `NET_AMOUNT` | `InvoiceRow/RowAmount` | Total de ligne HT |

## Règles de classification

DocBits détecte les documents Finvoice en faisant correspondre l'attribut `xmlns` sur l'élément racine `<Finvoice>` :

| Type de document électronique | Motif |
|--------------------------|---------|
| FINVOICE 1.3 | `xmlns` contient `http://www.finvoice.fi/schema/finvoice13` |
| FINVOICE 2.0 | `xmlns` contient `http://www.finvoice.fi/schema/finvoice20` (pas 2.01) |
| FINVOICE 2.01 | `xmlns` contient `http://www.finvoice.fi/schema/finvoice201` |
| FINVOICE 3.0 | `xmlns` contient `http://www.finvoice.fi/schema/finvoice30` |

La classification utilise le principe **premier résultat gagnant** avec des motifs plus spécifiques (2.01) évalués avant le générique 2.0.

## Voir aussi

- [Normes de facturation électronique actuellement prises en charge](../../currently-supported-e-invoice-standards/)
- [Finlande TEAPPSXML](./finland-teappsxml.md)
- [Documents électroniques pris en charge](./)
