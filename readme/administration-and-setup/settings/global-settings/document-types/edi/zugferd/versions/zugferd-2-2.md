# Mappage des champs ZUGFeRD 2.2

## Aperçu

ZUGFeRD 2.2 était la version initiale du standard. Bien qu'elle soit ancienne, de nombreux documents utilisent encore ce format. DocBits offre un support complet pour l'extraction de données à partir des fichiers XML ZUGFeRD 2.2.

## Mappage des champs d'en-tête

### Identification de la facture

| Chemin ZUGFeRD CII | Champ DocBits | Champ Infor BOD | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Numéro de facture |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Code type de facture |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Date d'émission de la facture |

### Type et sous-type de document (piloté par TRA)

La XSLT TRANSFORMATION par défaut émet deux champs dérivés :

| Champ DocBits | Source | Logique |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryInvoice/ExchangedDocument/TypeCode` | UNCL 1001 `381` ou `261` → **Credit Note** ; tout autre code → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Non vide → **Purchase Invoice** ; vide/absent → **Cost Invoice** |

### Ventilation des taxes (classification par tranches)

Les blocs `ApplicableTradeTax` sont distribués sur trois tranches basées sur le taux (et non sur des index positionnels) : les champs au taux standard (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) capturent les taux ≥ 19 ; les champs au taux réduit (`*_2`) capturent 0 < taux < 19 ; les champs au taux zéro (`*_3`) capturent taux = 0. Voir [Ventilation des taxes ZUGFeRD](../README.md#tax-breakdown-tier-classified) pour la liste complète des champs.

### Références de documents

| Chemin ZUGFeRD CII | Champ DocBits | Champ Infor BOD | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Numéro de bon de commande |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Référence du contrat |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Référence du bon de livraison |

### Informations fournisseur (vendeur)

| Chemin ZUGFeRD CII | Champ DocBits | Champ Infor BOD | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | ID fournisseur |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Nom du fournisseur |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Ligne d'adresse 1 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Code postal |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | Ville |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Code pays |

## Mappage des lignes d'articles

| Chemin ZUGFeRD CII | Champ DocBits | Champ Infor BOD | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Numéro de ligne |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Numéro d'article de l'acheteur |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Description de l'article |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Quantité facturée |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Prix unitaire net |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Total de la ligne |
