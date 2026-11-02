# Mappage ZUGFeRD 2.3

## Aperçu

ZUGFeRD 2.3 est la dernière version majeure. Elle intègre des améliorations pour une meilleure interopérabilité et une meilleure conformité aux exigences modernes de la facturation électronique.

## Mapping des champs d'en-tête

### Identification de la facture

| Chemin ZUGFeRD CII                | Champ DocBits    | Champ Infor BOD    | Type   | Description                   |
| --------------------------------- | ---------------- | ------------------ | ------ | ----------------------------- |
| `ExchangedDocument/ID`            | `INVOICE_NUMBER` | `DocumentID`       | STRING | Numéro de facture             |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE`   | `DocumentDateTime` | DATE   | Date d'émission de la facture |

### Type et sous-type de document (piloté par TRA)

Le XSLT TRANSFORMATION par défaut produit deux champs dérivés :

| Champ DocBits      | Source                                                                                                     | Logique                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `INVOICE_TYPE`     | `CrossIndustryInvoice/ExchangedDocument/TypeCode`                                                          | UNCL 1001 `381` ou `261` → **Credit Note** ; tout autre code → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Non vide → **Purchase Invoice** ; vide/absent → **Cost Invoice**           |

### Informations de paiement

| Chemin ZUGFeRD CII                                 | Champ DocBits    | Champ Infor BOD | Type   | Description    |
| -------------------------------------------------- | ---------------- | --------------- | ------ | -------------- |
| `PayeePartyCreditorFinancialAccount/IBANID`        | `IBAN_EXTRACTED` | `PayeeIBAN`     | STRING | IBAN           |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC`            | `PayeeBIC`      | STRING | Code BIC/SWIFT |

### Ventilation des taxes (classée par niveaux)

Les blocs `ApplicableTradeTax` sont répartis sur trois niveaux basés sur le taux (et non sur des index positionnels) : les champs au taux normal (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) capturent un taux ≥ 19 ; les champs au taux réduit (`*_2`) capturent 0 < taux < 19 ; les champs au taux zéro (`*_3`) capturent un taux = 0. Consultez [ZUGFeRD Tax Breakdown](./#ventilation-des-taxes-classification-par-tranches) pour la liste complète des champs.

## Mapping des lignes d'articles

| Chemin ZUGFeRD CII                       | Champ DocBits  | Champ Infor BOD    | Type   | Description              |
| ---------------------------------------- | -------------- | ------------------ | ------ | ------------------------ |
| `AssociatedDocumentLineDocument/LineID`  | `POSITION`     | `LineNumber`       | STRING | Numéro de ligne          |
| `SpecifiedTradeProduct/Name`             | `DESCRIPTION`  | `ItemDescription`  | STRING | Description de l'article |
| `BilledQuantity`                         | `QUANTITY`     | `InvoicedQuantity` | NUMBER | Quantité facturée        |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE`   | `UnitPrice`        | AMOUNT | Prix unitaire net        |
| `LineTotalAmount`                        | `TOTAL_AMOUNT` | `ExtendedAmount`   | AMOUNT | Total de la ligne        |
