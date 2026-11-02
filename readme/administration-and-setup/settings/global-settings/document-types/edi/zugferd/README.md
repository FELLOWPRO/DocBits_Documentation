# Aperçu de ZUGFeRD

## Introduction

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) est une norme allemande de facturation électronique basée sur la Cross Industry Invoice (CII) de l'UN/CEFACT et la norme ISO 19005-3 (PDF/A-3). Elle combine des données de facture structurées avec un fichier PDF.

DocBits extrait les champs des documents ZUGFeRD et les rapproche des systèmes ERP Infor (M3, LN) à l'aide des normes OAGIS BOD.

## Versions ZUGFeRD prises en charge

DocBits prend en charge plusieurs versions de la norme ZUGFeRD :

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Mappage complet des champs d'en-tête

### Identification de la facture

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Invoice number |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Invoice type code |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Date d'émission de la facture |
| `ExchangedDocument/IncludedNote` | `INVOICE_NOTE` | `Note` | STRING | Invoice notes |

### Type et sous-type de document (piloté par TRA)

> La même logique s'applique à **Factur-X** — Factur-X 1.x utilise le même vocabulaire CII que ZUGFeRD 2.x, donc le bloc dynamique ci-dessous est émis pour les deux.

En plus du `INVOICE_TYPE_CODE` brut, la XSLT TRANSFORMATION par défaut émet un arbre `<INVOICE>` canonique avec deux champs dérivés :

| Champ DocBits | Source | Logique |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `ExchangedDocument/TypeCode` (ou `HeaderExchangedDocument/TypeCode` pour ZUGFeRD 1.0) | UNCL 1001 `381` ou `261` → **Credit Note** ; tout autre code → **Invoice** |
| `INVOICE_SUB_TYPE` | Présence de `BuyerOrderReferencedDocument/IssuerAssignedID` (sous `ApplicableHeaderTradeAgreement` pour 2.x / `ApplicableSupplyChainTradeAgreement` pour 1.0) | Non vide → **Facture d'achat** ; vide/absent → **Facture de coûts** |

`INVOICE_SUB_TYPE` permet de distinguer les factures liées à un bon de commande des factures de coûts directs pour le routage AP.

### Références de documents

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Numéro de bon de commande |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Contract reference |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Référence du bon de livraison |

### Dates

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Invoice date |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualShipDateTime` | DATE | Date de livraison/expédition |
| `SpecifiedTradePaymentTerms/DueDateDateTime` | `DUE_DATE` | `PaymentDueDateTime` | DATE | Date d'échéance du paiement |
| `BillingSpecifiedPeriod/StartDateTime` | `BILLING_PERIOD_START` | `BillingPeriodStart` | DATE | Début de la période de facturation |
| `BillingSpecifiedPeriod/EndDateTime` | `BILLING_PERIOD_END` | `BillingPeriodEnd` | DATE | Fin de la période de facturation |

### Informations sur le fournisseur (vendeur)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | Supplier ID |
| `SellerTradeParty/GlobalID` | `VENDOR_GLN` | `SupplierPartyGLN` | STRING | Numéro d'emplacement mondial |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Supplier name |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Address line 1 |
| `SellerTradeParty/PostalTradeAddress/Line2` | `VENDOR_ADDRESS_2` | `SupplierAddress2` | STRING | Address line 2 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Postal code |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | City |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Country code |
| `SellerTradeParty/SpecifiedTaxRegistration/ID` | `VAT_NO_EXTRACTED` | `SupplierTaxID` | STRING | VAT registration number |
| `SellerTradeParty/DefinedTradeContact/EmailURIID` | `VENDOR_EMAIL` | `SupplierEmail` | STRING | Email |
| `SellerTradeParty/DefinedTradeContact/TelephoneUniversalCommunication` | `VENDOR_PHONE` | `SupplierPhone` | STRING | Phone |

### Informations sur l’acheteur

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerTradeParty/ID` | `COMPANY_ID` | `CustomerPartyID` | STRING | Customer ID |
| `BuyerTradeParty/GlobalID` | `COMPANY_GLN` | `CustomerPartyGLN` | STRING | Numéro d'emplacement mondial |
| `BuyerTradeParty/Name` | `COMPANY_NAME` | `CustomerPartyName` | STRING | Company name |
| `BuyerTradeParty/PostalTradeAddress/Line1` | `COMPANY_ADDRESS` | `CustomerAddress1` | STRING | Address line 1 |
| `BuyerTradeParty/PostalTradeAddress/PostcodeCode` | `COMPANY_POSTAL_CODE` | `CustomerPostalCode` | STRING | Postal code |
| `BuyerTradeParty/PostalTradeAddress/CityName` | `COMPANY_CITY` | `CustomerCity` | STRING | City |
| `BuyerTradeParty/PostalTradeAddress/CountryID` | `COMPANY_COUNTRY` | `CustomerCountryCode` | STRING | Country code |
| `BuyerTradeParty/SpecifiedTaxRegistration/ID` | `COMPANY_VAT_ID` | `CustomerTaxID` | STRING | VAT ID |

### Informations de paiement

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `PayeePartyCreditorFinancialAccount/IBANID` | `IBAN_EXTRACTED` | `PayeeIBAN` | STRING | IBAN |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC` | `PayeeBIC` | STRING | BIC/SWIFT code |
| `SpecifiedTradePaymentTerms/Description` | `PAYMENT_TERMS` | `PaymentTerms` | STRING | Description des conditions de paiement |
| `SpecifiedTradeSettlementPaymentMeans/TypeCode` | `PAYMENT_METHOD` | `PaymentMethod` | STRING | Payment method code |

### Devise et montants (en-tête)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceCurrencyCode` | `CURRENCY` | `CurrencyCode` | STRING | Invoice currency |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Montant net total |
| `TaxTotalAmount` | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount` | AMOUNT | Montant total de la taxe |
| `GrandTotalAmount` | `TOTAL_AMOUNT` | `GrandTotalAmount` | AMOUNT | Grand total |
| `DuePayableAmount` | `AMOUNT_DUE` | `DuePayableAmount` | AMOUNT | Amount due |
| `TotalPrepaidAmount` | `PREPAID_AMOUNT` | `TotalPrepaidAmount` | AMOUNT | Prepaid amount |
| `AllowanceTotalAmount` | `NEGATIVE_AMOUNT` | `AllowanceTotalAmount` | AMOUNT | Total allowances |
| `ChargeTotalAmount` | `CHARGES` | `ChargeTotalAmount` | AMOUNT | Total charges |

### Ventilation des taxes (classification par tranches)

La XSLT TRANSFORMATION par défaut distribue les blocs `ApplicableTradeTax` sur trois tranches basées sur le taux plutôt que d'utiliser des index positionnels. Chaque bloc est associé à une tranche par son `RateApplicablePercent` :

| Tranche | Champs DocBits | Règle de sélection |
| :--- | :--- | :--- |
| Tranche 1 (Standard) | `TAX_RATE`, `NET_AMOUNT`, `TAX_AMOUNT` | taux ≥ 19 |
| Tranche 2 (Réduit) | `TAX_RATE_2`, `NET_AMOUNT_2`, `TAX_AMOUNT_2` | 0 < taux < 19 |
| Tranche 3 (Zéro) | `TAX_RATE_3`, `NET_AMOUNT_3`, `TAX_AMOUNT_3` | taux = 0 |

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` (tranche 1) | `TAX_RATE` | `TaxPercent` | NUMBER | Pourcentage de TVA au taux standard |
| `ApplicableTradeTax/BasisAmount` (tranche 1) | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Montant net au taux standard |
| `ApplicableTradeTax/CalculatedAmount` (tranche 1) | `TAX_AMOUNT` | `TaxAmount` | AMOUNT | Montant de taxe au taux standard |
| `ApplicableTradeTax/RateApplicablePercent` (tranche 2) | `TAX_RATE_2` | `TaxPercent2` | NUMBER | Pourcentage de TVA au taux réduit |
| `ApplicableTradeTax/BasisAmount` (tranche 2) | `NET_AMOUNT_2` | `TaxableAmount2` | AMOUNT | Montant net au taux réduit |
| `ApplicableTradeTax/CalculatedAmount` (tranche 2) | `TAX_AMOUNT_2` | `TaxAmount2` | AMOUNT | Montant de taxe au taux réduit |
| `ApplicableTradeTax/RateApplicablePercent` (tranche 3) | `TAX_RATE_3` | `TaxPercent3` | NUMBER | Pourcentage de TVA au taux zéro |
| `ApplicableTradeTax/BasisAmount` (tranche 3) | `NET_AMOUNT_3` | `TaxableAmount3` | AMOUNT | Montant net au taux zéro |
| `ApplicableTradeTax/CalculatedAmount` (tranche 3) | `TAX_AMOUNT_3` | `TaxAmount3` | AMOUNT | Montant de taxe au taux zéro |

## Mappage complet des lignes d'articles (tableau)

### Identification de la ligne

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Line number |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Numéro d'article de l'acheteur |
| `SpecifiedTradeProduct/SellerAssignedID` | `SUPPLIER_ITEM_NUMBER` | `SellerItemID` | STRING | Numéro d'article du vendeur |
| `SpecifiedTradeProduct/GlobalID` | `ITEM_CODE` | `ItemCode` | STRING | Global ID (GTIN/EAN) |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Item description |

### Références de la ligne

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Numéro PO au niveau de la ligne |
| `BuyerOrderReferencedDocument/LineID` | `PO_LINE_NUMBER` | `CustomerOrderLineNumber` | STRING | PO line number |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Delivery note |
| `DespatchAdviceReferencedDocument/LineID` | `DELIVERY_LINE` | `ShipmentLineNumber` | STRING | Delivery line |

### Quantités et unités

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Billed quantity |
| `BilledQuantity/@unitCode` | `UNIT` | `UnitCode` | STRING | Code d'unité de mesure |
| `PackageQuantity` | `PACKAGE_QUANTITY` | `PackageQuantity` | NUMBER | Nombre de colis |

### Tarification

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Prix unitaire net |
| `GrossPriceProductTradePrice/ChargeAmount` | `GROSS_PRICE` | `GrossUnitPrice` | AMOUNT | Prix unitaire brut |
| `NetPriceProductTradePrice/BasisQuantity` | `UNIT_PRICE_PER_QUANTITY` | `PricePerQuantity` | NUMBER | Quantité de base de prix |

### Montants de la ligne

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Line total |
| `TotalAllowanceChargeAmount` | `NET_AMOUNT` | `NetAmount` | AMOUNT | Montant net de la ligne |

### Taxes de la ligne

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` | `VAT` | `TaxPercent` | NUMBER | VAT rate |
| `ApplicableTradeTax/TypeCode` | `TAX_CODE` | `TaxCode` | STRING | Code du type de taxe |
| `ApplicableTradeTax/CategoryCode` | `TAX_CATEGORY` | `TaxCategoryCode` | STRING | Tax category |

### Remises et frais (ligne)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AppliedTradeAllowanceCharge/ActualAmount` | `DISCOUNT` | `AllowanceAmount` | AMOUNT | Discount amount |
| `AppliedTradeAllowanceCharge/CalculationPercent` | `DISCOUNT_PERCENT` | `AllowancePercent` | NUMBER | Discount percentage |
| `AppliedTradeAllowanceCharge/ActualAmount` | `SURCHARGE` | `ChargeAmount` | AMOUNT | Surcharge amount |
| `AppliedTradeAllowanceCharge/Reason` | `ALLOWANCE_REASON` | `AllowanceReason` | STRING | Motif de la remise |

### Champs de ligne supplémentaires

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SpecifiedTradeProduct/OriginTradeCountry/ID` | `COUNTRY_OF_ORIGIN` | `CountryOfOrigin` | STRING | Pays d'origine |
| `SpecifiedTradeProduct/ApplicableProductCharacteristic/Value` | `PRODUCT_CHARACTERISTIC` | `ProductCharacteristic` | STRING | Product characteristic |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualDeliveryDate` | DATE | Date de livraison de la ligne |

## Règles effectivement utilisées et activation

Si un avoir électronique apparaît comme Invoice, suivez le [guide de diagnostic de la classification](../credit-note-recognized-as-invoice.md). Il couvre la source personnalisée ou par défaut effectivement utilisée, les codes de type, Extraction Paths et l’activation en toute sécurité.

## Guides par pays

Consultez les guides par pays pour connaître les libellés exacts des formats, la syntaxe, les limites de version et l’état de configuration examiné. [Formats eDocs, versions et guides par pays](../supported-electronic-documents/README.md).
