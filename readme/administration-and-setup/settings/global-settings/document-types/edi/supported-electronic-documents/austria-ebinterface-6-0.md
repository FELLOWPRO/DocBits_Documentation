---
description: Prise en charge du document électronique AUSTRIA EBINTERFACE 6.0 dans DocBits
---
# 🇦🇹 AUSTRIA EBINTERFACE 6.0
| Propriété | Valeur |
|-----------|--------|
| **Pays / Région** | Autriche |
| **Types de documents** | Facture, Note de crédit |
| **Format** | XML |
| **Norme** | ebInterface 6.0 |
| **Paramètres régionaux** | `de_AT` |

ebInterface 6.0 est la version de la norme autrichienne de facturation électronique alignée sur la norme européenne EN 16931. Maintenue par la Chambre économique fédérale autrichienne (WKÖ — Wirtschaftskammer Österreich), elle définit un format XML structuré pour les factures électroniques utilisées dans les transactions B2G et B2B en Autriche. DocBits prend en charge cette version via l'espace de noms XML dédié.

## Statut de prise en charge
| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut
<figure><img src="austria-ebinterface-preview.png" alt="Aperçu de la facture Austria ebInterface 6.0 dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour une facture AUSTRIA EBINTERFACE 6.0</p></figcaption></figure>

## Correspondance des champs
### Champs d'en-tête
| Champ DocBits | Élément XML source | Remarques |
|---|---|---|
| `invoice_id` | `eb:InvoiceNumber` | Numéro de facture |
| `invoice_date` | `eb:InvoiceDate` | Date au format ISO 8601 |
| `due_date` | `eb:PaymentConditions/eb:DueDate` | Date d'échéance du paiement |
| `delivery_date` | `eb:Delivery/eb:Date` | Date de livraison |
| `currency` | `@eb:InvoiceCurrency` | Attribut racine, toujours `EUR` pour AT |
| `total_amount` | `eb:TotalGrossAmount` | Total brut TVA comprise |
| `net_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:TaxedAmount` | Base imposable nette |
| `tax_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:Amount` | Montant de la TVA |
| `purchase_order` | `eb:OrderReference/eb:OrderID` | Référence du bon de commande |
| `payment_terms` | `eb:PaymentConditions/eb:Comment` | Conditions de paiement en texte libre |
| `supplier_name` | `eb:Biller/eb:Address/eb:Name` | Raison sociale du fournisseur |
| `supplier_tax_id` | `eb:Biller/eb:VATIdentificationNumber` | UID autrichien (ex. ATU12345678) |
| `supplier_street` | `eb:Biller/eb:Address/eb:Street` | Adresse du fournisseur |
| `supplier_city` | `eb:Biller/eb:Address/eb:Town` | Ville du fournisseur |
| `supplier_postal_code` | `eb:Biller/eb:Address/eb:ZIP` | Code postal du fournisseur |
| `supplier_country` | `eb:Biller/eb:Address/eb:Country/@eb:CountryCode` | Code pays ISO |
| `supplier_email` | `eb:Biller/eb:Address/eb:Email` | E-mail du fournisseur |
| `supplier_iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN du fournisseur |
| `customer_name` | `eb:InvoiceRecipient/eb:Address/eb:Name` | Raison sociale du destinataire |
| `customer_tax_id` | `eb:InvoiceRecipient/eb:VATIdentificationNumber` | UID du destinataire |
| `customer_street` | `eb:InvoiceRecipient/eb:Address/eb:Street` | Adresse du destinataire |
| `customer_city` | `eb:InvoiceRecipient/eb:Address/eb:Town` | Ville du destinataire |
| `customer_postal_code` | `eb:InvoiceRecipient/eb:Address/eb:ZIP` | Code postal du destinataire |
| `customer_country` | `eb:InvoiceRecipient/eb:Address/eb:Country/@eb:CountryCode` | Code pays ISO |
| `iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN de paiement |
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | BIC de paiement |

### Tableau des lignes de facturation (`INVOICE_TABLE`)
Chemin de la ligne : `eb:Details/eb:ItemList/eb:ListLineItem`
| Colonne | Élément XML source | Remarques |
|---|---|---|
| `POSITION` | Index séquentiel | Numéro de ligne (base 1) |
| `DESCRIPTION` | `eb:Description` | Description du produit/service |
| `QUANTITY` | `eb:Quantity` | Quantité numérique |
| `UNIT` | `eb:Quantity/@eb:Unit` | Code unité (ex. `STK` = pièce) |
| `UNIT_PRICE` | `eb:UnitPrice` | Prix unitaire hors TVA |
| `VAT_RATE` | `eb:VAT/eb:VATItem/eb:VATRate` | Taux de TVA en % |
| `VAT` | `eb:VAT/eb:VATItem/eb:TaxedAmount` | Montant de TVA par ligne |
| `NET_AMOUNT` | `eb:LineItemAmount` | Total de la ligne hors TVA |

## Règles de classification
| Version | Espace de noms |
|---------|----------------|
| ebInterface 6.0 | `http://www.ebinterface.at/schema/6p0/` |

L'élément racine est `<eb:Invoice>` avec l'URI d'espace de noms `http://www.ebinterface.at/schema/6p0/`.

## Voir aussi
- [Austria ebInterface](austria-ebinterface.md)
- [Austria ebInterface 6.1](austria-ebinterface-6-1.md)
- [Documents électroniques pris en charge](./)
