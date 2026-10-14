# Fichier de transformation et mappage

## 1. **Objet**

Ce fichier est responsable de l'extraction des données d'un fichier XML Peppol BIS Billing 3.0, de leur traitement et de la sauvegarde des informations pertinentes dans un format spécifié. Il est conçu pour permettre l'extraction de champs clés afin de faciliter le traitement ultérieur ou l'intégration dans DocBits.

## 2. **Aperçu**

* **Fichier source** : L'entrée est un fichier XML Peppol qui suit la norme Peppol BIS Billing 3.0.
* **Processus d'extraction** : Le fichier effectue une série d'étapes pour lire, analyser et extraire des éléments clés tels que les détails de la facture, les informations sur le fournisseur, les montants et les dates.
* **Sortie** : Les données extraites sont stockées dans un format structuré, dans un autre fichier XML.

## _**3.**_**&#x20;Téléchargement** **du fichier de transformation XML Peppol.**

* Exemple : _Ce fichier contient la logique de transformation XML Peppol pour extraire et sauvegarder des données dans un autre fichier XML._
* Si vous rencontrez des problèmes avec votre fichier actuel ou s'il devient inutilisable, téléchargez cette version de sauvegarde pour restaurer la fonctionnalité de transformation.

{% file src="../../../../../../.gitbook/assets/Transformation.xslt" %}

#### Voici le mappage :

<details>

<summary>Mappage des informations de l'AccountingSupplierParty</summary>



* **Adresse électronique du fournisseur**
  * **Source** : `//AccountingSupplierParty/Party/EndpointID/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS>`
  * **Peut apparaître plusieurs fois** : Non.
* **ID du schéma de l'adresse électronique du fournisseur**
  * **Source** : `//AccountingSupplierParty/Party/EndpointID/@schemeID`
  * **Mappé sur** : `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Peut apparaître several times** : Non.
* **Identification du fournisseur**
  * **Source** :`//AccountingSupplierParty/Party/PartyIdentification/ID/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID>`
  * **Peut apparaître several times** : Chaque élément `<PartyIdentification>` sous `Supplier` sera extrait.
* **ID du schéma d'identification du fournisseur**
  * **Source** :`//AccountingSupplierParty/Party/PartyIdentification/ID/@schemeID`
  * **Mappé sur** : `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Peut apparaître several times** : Chaque élément `<PartyIdentification>` aura son ID de schéma correspondant.
* **Nom du fournisseur**
  * **Source** : `//AccountingSupplierParty/Party/PartyName/Name/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><NAME>`
  * **Peut apparaître several times** : Non.
* **Ligne d'adresse du fournisseur 1**
  * **Source** :`//AccountingSupplierParty/Party/PostalAddress/StreetName/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><ADDRESS_LINE_1>`
  * **Peut apparaître several times** : Non.
* **Ligne d'adresse du fournisseur 2**
  * **Source** :`//AccountingSupplierParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><ADDRESS_LINE_2>`
  * **Peut apparaître several times** : Non.
* **Ligne d'adresse du fournisseur 3**
  * **Source** :`//AccountingSupplierParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Mappé sur** : `<InvoINVOICEice><SUPPLIER><ADDRESS_LINE_3>`
  * **Peut apparaître several times** : Non.
* **ID de TVA du fournisseur**
  * **Source** :`//AccountingSupplierParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><VAT_ID>`
  * **Peut apparaître several times** : Non.
* **Schéma fiscal du fournisseur**
  * **Source** :`//AccountingSupplierParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><TAX_SCHEME>`
  * **Peut apparaître several times** : Non.
* **Nom légal du fournisseur**
  * **Source** :`//AccountingSupplierParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><LEGAL_NAME>`
  * **Peut apparaître several times** : Non.
* **ID légal du fournisseur**
  * **Source** :`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><LEGAL_ID>`
  * **Peut apparaître several times** : Non.
* **ID du schéma de l'ID légal du fournisseur**
  * **Source** :`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Mappé sur** : `<INVOICE><SUPPLIER><LEGAL_ID_SCHEME_ID>`
  * **Peut apparaître several times** : Non.
* **Forme légale du fournisseur**
  * **Source** :`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><LEGAL_FORM>`
  * **Peut apparaître several times** : Non.
* **Code postal du fournisseur**
  * **Source** :`//AccountingSupplierParty/Party/PostalAddress/PostalZone/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><POST_CODE>`
  * **Peut apparaître several times** : Non.
* **Ville du fournisseur**
  * **Source** :`//AccountingSupplierParty/Party/PostalAddress/CityName/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><CITY>`
  * **Peut apparaître several times** : Non.
* **Sous-entité pays du fournisseur**
  * **Source** : `//AccountingSupplierParty/Party/PostalAddress/CountrySubentity/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><COUNTRY_SUBENTITY>`
  * **Peut apparaître several times** : Non.
* **Code pays du fournisseur**
  * **Source** : `//AccountingSupplierParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><COUNTRY_CODE>`
  * **Peut apparaître several times** : Non.
* **Nom du contact fournisseur**
  * **Source** : `//AccountingSupplierParty/Party/Contact/Name/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><CONTACT><NAME>`
  * **Peut apparaître several times** : Non.
* **Téléphone du contact fournisseur**
  * **Source** : `//AccountingSupplierParty/Party/Contact/Telephone/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><CONTACT><TELEPHONE>`
  * **Peut apparaître several times** : Non.
* **E-mail du contact fournisseur**
  * **Source** : `//AccountingSupplierParty/Party/Contact/ElectronicMail/text()`
  * **Mappé sur** : `<INVOICE><SUPPLIER><CONTACT><EMAIL>`
  * **Peut apparaître several times** : Non.

</details>

<details>

<summary>Mappage des informations de l'AccountingCustomerParty</summary>



* **Adresse électronique de l'acheteur**
  * **Source** : `//AccountingCustomerParty/Party/EndpointID/text()`
  * **Mappé sur** : `<INVOICE><BUYER><ELECTRONIC_ADDRESS>`
  * **Peut apparaître several times** : Non.
* **ID du schéma de l'adresse électronique de l'acheteur**
  * **Source** : `//AccountingCustomerParty/Party/EndpointID/@schemeID`
  * **Mappé sur** : `<INVOICE><BUYER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Peut apparaître several times** : Non.
* **Identification de l'acheteur**
  * **Source** : `//AccountingCustomerParty/Party/PartyIdentification/ID/text()`
  * **Mappé sur** : `<INVOICE><BUYER><PARTYIDENTIFICATION><ID>`
  * **Peut apparaître several times** : Chaque élément `<PartyIdentification>` sous `Buyer` sera extrait.
* **ID du schéma d'identification de l'acheteur**
  * **Source** :`//AccountingCustomerParty/Party/PartyIdentification/ID/@schemeID`
  * **Mappé sur** : `<INVOICE><BUYER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Peut apparaître several times** : Chaque élément `<PartyIdentification>` aura son ID de schéma correspondant.
* **Nom de l'acheteur**
  * **Source** : `//AccountingCustomerParty/Party/PartyName/Name/text()`
  * **Mappé sur** : `<INVOICE><BUYER><NAME>`
  * **Peut apparaître several times** : Non.
* **Ligne d'adresse de l'acheteur 1**
  * **Source** :`//AccountingCustomerParty/Party/PostalAddress/StreetName/text()`
  * **Mappé sur** : `<INVOICE><BUYER><ADDRESS_LINE_1>`
  * **Peut apparaître several times** : Non.
* **Ligne d'adresse de l'acheteur 2**
  * **Source** :`//AccountingCustomerParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Mappé sur** : `<INVOICE><BUYER><ADDRESS_LINE_2>`
  * **Peut apparaître several times** : Non.
* **Ligne d'adresse de l'acheteur 3**
  * **Source** :`//AccountingCustomerParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Mappé sur** : `<INVOICE><BUYER><ADDRESS_LINE_3>`
  * **Peut apparaître several times** : Non.
* **ID de TVA de l'acheteur**
  * **Source** :`//AccountingCustomerParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Mappé sur** : `<INVOICE><BUYER><VAT_ID>`
  * **Peut apparaître several times** : Non.
* **Schéma fiscal de l'acheteur**
  * **Source** :`//AccountingCustomerParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mappé sur** : `<INVOICE><BUYER><TAX_SCHEME>`
  * **Peut apparaître several times** : Non.
* **Nom légal de l'acheteur**
  * **Source** :`//AccountingCustomerParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Mappé sur** : `<INVOICE><BUYER><LEGAL_NAME>`
  * **Peut apparaître several times** : Non.
* **ID légal de l'acheteur**
  * **Source** :`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Mappé sur** : `<INVOICE><BUYER><LEGAL_ID>`
  * **Peut apparaître several times** : Non.
* **ID du schéma de l'ID légal de l'acheteur**
  * **Source** :`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Mappé sur** : `<INVOICE><BUYER><LEGAL_ID_SCHEME_ID>`
  * **Peut apparaître several times** : Non.
* **Forme légale de l'acheteur**
  * **Source** :`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Mappé sur** : `<INVOICE><BUYER><LEGAL_FORM>`
  * **Peut apparaître several times** : Non.
* **Code postal de l'acheteur**
  * **Source** :`//AccountingCustomerParty/Party/PostalAddress/PostalZone/text()`
  * **Mappé sur** : `<INVOICE><BUYER><POST_CODE>`
  * **Peut apparaître several times** : Non.
* **Ville de l'acheteur**
  * **Source** :`//AccountingCustomerParty/Party/PostalAddress/CityName/text()`
  * **Mappé sur** : `<INVOICE><BUYER><CITY>`
  * **Peut apparaître several times** : Non.
* **Sous-entité pays de l'acheteur**
  * **Source** :`//AccountingCustomerParty/Party/PostalAddress/CountrySubentity/text()`
  * **Mappé sur** : `<INVOICE><BUYER><COUNTRY_SUBENTITY>`
  * **Peut apparaître several times** : Non.
* **Code pays de l'acheteur**
  * **Source** :`//AccountingCustomerParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Mappé sur** : `<INVOICE><BUYER><COUNTRY_CODE>`
  * **Peut apparaître several times** : Non.
* **Nom du contact acheteur**
  * **Source** : `//AccountingCustomerParty/Party/Contact/Name/text()`
  * **Mappé sur** : `<INVOICE><BUYER><CONTACT><NAME>`
  * **Peut apparaître several times** : Non.
* **Téléphone du contact acheteur**
  * **Source** : `//AccountingCustomerParty/Party/Contact/Telephone/text()`
  * **Mappé sur** : `<INVOICE><BUYER><CONTACT><TELEPHONE>`
  * **Peut apparaître several times** : Non.
* **E-mail du contact acheteur**
  * **Source** : `//AccountingCustomerParty/Party/Contact/ElectronicMail/text()`
  * **Mappé sur** : `<INVOICE><BUYER><CONTACT><EMAIL>`
  * **Peut apparaître several times** : Non.

</details>

<details>

<summary>Mappage des informations de la PayeeParty</summary>



1. **Identification du bénéficiaire**
   * **Source** : `//PayeeParty/PartyIdentification/ID/text()`
   * **Mappé sur** : `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID>`
   * **Peut apparaître several times** : Chaque élément `<PartyIdentification>` sous `PayeeParty` sera extrait.
2. **ID du schéma d'identification du bénéficiaire**
   * **Source** : `//PayeeParty/PartyIdentification/ID/@schemeID`
   * **Mappé sur** : `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID_SCHEME_ID>`
   * **Peut apparaître several times** : Chaque élément `<PartyIdentification>` aura son ID de schéma correspondant.
3. **Nom du bénéficiaire**
   * **Source** : `//PayeeParty/PartyName/Name/text()`
   * **Mappé sur** : `<INVOICE><PAYEE><NAME>`
   * **Peut apparaître several times** : Non.
4. **ID légal du bénéficiaire**
   * **Source** : `//PayeeParty/PartyLegalEntity/CompanyID/text()`
   * **Mappé sur** : `<INVOICE><PAYEE><LEGAL_ID>`
   * **Peut apparaître several times** : Non.
5. **ID du schéma de l'ID légal du bénéficiaire**
   * **Source** : `//PayeeParty/PartyLegalEntity/CompanyID/@schemeID`
   * **Mappé sur** : `<INVOICE><PAYEE><LEGAL_ID_SCHEME_ID>`
   * **Peut apparaître several times** : Non.

</details>

<details>

<summary>Mappage des informations de la TaxRepresentativeParty</summary>



* **Nom du représentant fiscal**
  * **Source** : `//TaxRepresentativeParty/PartyName/Name/text()`
  * **Mappé sur** : `<INVOICE><TAX_REPRESENTATIVE_PARTY><NAME>`
  * **Peut apparaître several times** : Non.
* **Ligne d'adresse du représentant fiscal 1**
  * **Source** : `//TaxRepresentativeParty/PostalAddress/StreetName/text()`
  * **Mappé sur** : `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_1>`
  * **Peut apparaître several times** : Non.
* **Ligne d'adresse du représentant fiscal 2**
  * **Source** :`//TaxRepresentativeParty/PostalAddress/AdditionalStreetName/text()`
  * **Mappé sur** : `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_2>`
  * **Peut apparaître several times** : Non.
* **Ligne d'adresse du représentant fiscal 3**
  * **Source** :`//TaxRepresentativeParty/PostalAddress/AddressLine/Line/text()`
  * **Mappé sur** : `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_3>`
  * **Peut apparaître several times** : Non.
* **ID de TVA du représentant fiscal**
  * **Source** : `//TaxRepresentativeParty/PartyTaxScheme/CompanyID/text()`
  * **Mappé sur** : `<INVOICE><TAX_REPRESENTATIVE_PARTY><VAT_ID>`
  * **Peut apparaître several times** : Non.
* **Schéma fiscal du représentant fiscal**
  * **Source** :`//TaxRepresentativeParty/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mappé sur** : `<INVOICE><TAX_REPRESENTATIVE_PARTY><TAX_SCHEME>`
  * **Peut apparaître several times** : Non.
* **Ville du représentant fiscal**
  * **Source** : `//TaxRepresentativeParty/PostalAddress/CityName/text()`
  * **Mappé sur** : `<INVOICE><TAX_REPRESENTATIVE_PARTY><CITY>`
  * **Peut apparaître several times** : Non.
* **Code postal du représentant fiscal**
  * **Source** : `//TaxRepresentativeParty/PostalAddress/PostalZone/text()`
  * **Mappé sur** : `<INVOICE><TAX_REPRESENTATIVE_PARTY><POST_CODE>`
  * **Peut apparaître several times** : Non.
* **Sous-entité pays du représentant fiscal**
  * **Source** :`//TaxRepresentativeParty/PostalAddress/CountrySubentity/text()`
  * **Mappé sur** : `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_SUBENTITY>`
  * **Peut apparaître several times** : Non.
* **Code pays du représentant fiscal**
  * **Source** :`//TaxRepresentativeParty/PostalAddress/Country/IdentificationCode/text()`
  * **Mappé sur** : `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_CODE>`
  * **Peut apparaître several times** : Non.

</details>

<details>

<summary>Informations générales sur la facture</summary>



1. **Type de facture**
   * **Source** : `"Invoice"`
   * **Mappé sur** : `<INVOICE><INVOICE_TYPE>`
   * **Peut apparaître several times** : Non.
2. **Sous-type de facture**
   * **Source** : `"Purchase Invoice"`
   * **Mappé sur** : `<INVOICE><INVOICE_SUB_TYPE>`
   * **Peut apparaître several times** : Non.
3. **ID de facture**
   * **Source** : `//ID/text()`
   * **Mappé sur** : `<INVOICE><INVOICE_ID>`
   * **Peut apparaître several times** : Non.
4. **Code de type de facture**
   * **Source** : `//InvoiceTypeCode/text()`
   * **Mappé sur** : `<INVOICE><INVOICE_TYPE_CODE>`
   * **Peut apparaître several times** : Non.
5. **Date de facture**
   * **Source** : `normalize-space(//IssueDate/text())`
   * **Mappé sur** : `<INVOICE><INVOICE_DATE>`
   * **Peut apparaître several times** : Non.
   * **Traitement** : Utilise le modèle `DateTimeString` pour le formatage.
6. **Date d'échéance**
   * **Source** : `normalize-space(//DueDate/text())`
   * **Mappé sur** : `<INVOICE><DUE_DATE>`
   * **Peut apparaître several times** : Non.
   * **Traitement** : Utilise le modèle `DateTimeString` pour le formatage.
7. **Date de point fiscal**
   * **Source** : `normalize-space(//TaxPointDate/text())`
   * **Mappé sur** : `<INVOICE><TAX_POINT_DATE>`
   * **Peut apparaître several times** : Non.
   * **Traitement** : Utilise le modèle `DateTimeString` pour le formatage.
8. **Note de facture**
   * **Source** : `//Note/text()`
   * **Mappé sur** : `<INVOICE><INVOICE_NOTE>`
   * **Peut apparaître several times** : Non.
9. **Code devise du document**
   * **Source** : `//DocumentCurrencyCode/text()`
   * **Mappé sur** : `<INVOICE><DOCUMENT_CURRENCY_CODE>`
   * **Peut apparaître several times** : Non.
10. **Code devise fiscale**
    * **Source** : `//TaxCurrencyCode/text()`
    * **Mappé sur** : `<INVOICE><TAX_CURRENCY_CODE>`
    * **Peut apparaître several times** : Non.
11. **Coût comptable**
    * **Source** : `//AccountingCost/text()`
    * **Mappé sur** : `<INVOICE><ACCOUNTING_COST>`
    * **Peut apparaître several times** : Non.
12. **Date de début de période de facture**
    * **Source** : `normalize-space(//InvoicePeriod/StartDate/text())`
    * **Mappé sur** : `<INVOICE><INVOCICE_PERIOD><START_DATE>`
    * **Peut apparaître several times** : Non.
    * **Traitement** : Utilise le modèle `DateTimeString` pour le formatage.
13. **Date de fin de période de facture**
    * **Source** : `normalize-space(//InvoicePeriod/EndDate/text())`
    * **Mappé sur** : `<INVOICE><INVOCICE_PERIOD><END_DATE>`
    * **Peut apparaître several times** : Non.
    * **Traitement** : Utilise le modèle `DateTimeString` pour le formatage.
14. **Code de description de période de facture**
    * **Source** : `//InvoicePeriod/DescriptionCode/text()`
    * **Mappé sur** : `<INVOICE><INVOCICE_PERIOD><DESCRIPTION_CODE>`
    * **Peut apparaître several times** : Non.
15. **Référence de bon de commande**
    * **Source** : `//OrderReference/ID/text()`
    * **Mappé sur** : `<INVOICE><PURCHASE_ORDER>`
    * **Peut apparaître several times** : Non.
16. **Référence de commande client**
    * **Source** : `//OrderReference/SalesOrderID/text()`
    * **Mappé sur** : `<INVOICE><SALES_ORDER>`
    * **Peut apparaître several times** : Non.

</details>

<details>

<summary>Mappage des références de documents et détails supplémentaires du document</summary>

1. **Référence de l'acheteur**
   * **Source** : `//BuyerReference/text()`
   * **Mappé sur** : `<INVOICE><BUYER_REFERENCE>`
   * **Peut apparaître several times** : Non.

2)  **Référence de facturation**

    * **Source** : `//BillingReference`
    * **Mappé sur** : `<INVOICE><BILLING_REFERENCE>`
    * **Peut apparaître several times** : Oui. Chaque élément `<BillingReference>` de la source de données générera un élément `<BILLING_REFERENCE>`.

    **Pour chaque référence de facturation :**

    * **NUMÉRO\_FACTURE\_PRÉCÉDENTE**
      * **Source** : `InvoiceDocumentReference/ID/text()`
      * **Mappé sur** : `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOCIE_NUMBER>`
      * **Peut apparaître several times** : Non.
    * **DATE\_ÉMISSION\_FACTURE\_PRÉCÉDENTE**
      * **Source** : `InvoiceDocumentReference/IssueDate/text()`
      * **Mappé sur** : `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOICE_ISSUE_DATE>`
      * **Peut apparaître several times** : Non.

3. **Référence du document d'expédition**
   * **Source** : `//DespatchDocumentReference/ID/text()`
   * **Mappé sur** : `<INVOICE><DESPATCH_DOCUMENT_REFERENCE>`
   * **Peut apparaître several times** : Non.

4) **Référence du document de réception**
   * **Source** : `//ReceiptDocumentReference/ID/text()`
   * **Mappé sur** : `<INVOICE><RECEIPT_DOCUMENT_REFERENCE>`
   * **Peut apparaître several times** : Non.

5. **Référence du document d'origine**
   1. **Source** : `//OriginatorDocumentReference/ID/text()`
   2. **Mappé sur** : `<INVOICE><ORIGINATOR_DOCUMENT_REFERENCE>`
   3. **Peut apparaître several times** : Non.

#### Référence du document de contrat

* **Source** : `//ContractDocumentReference/ID/text()`
* **Mappé sur** : `<INVOICE><CONTRACT_DOCUMENT_REFERENCE>`
* **Peut apparaître several times** : Non.

#### Référence du projet

* **Source** : `//ProjectReference/ID/text()`
* **Mappé sur** : `<INVOICE><PROJECT_REFERENCE>`
* **Peut apparaître several times** : Non.

#### Référence de document supplémentaire

* **Source** : `//AdditionalDocumentReference`
* **Mappé sur** : `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE>`
* **Peut apparaître several times** : Oui. Chaque élément `<AdditionalDocumentReference>` de la source de données générera un élément `<ADDITIONAL_DOCUMENT_REFERENCE>`.

**Pour chaque référence de document supplémentaire :**

* **ID**
  * **Source** : `ID/text()`
  * **Mappé sur** : `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ID>`
  * **Peut apparaître several times** : Non.
* **ID\_SCHÉMA**
  * **Source** : `ID/@schemeID`
  * **Mappé sur** : `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><SCHEME_ID>`
  * **Peut apparaître several times** : Non.
* **CODE\_TYPE\_DOCUMENT**
  * **Source** : `DocumentTypeCode/text()`
  * **Mappé sur** : `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_TYPE_CODE>`
  * **Peut apparaître several times** : Non.
* **DESCRIPTION\_DOCUMENT**
  * **Source** : `DocumentDescription/text()`
  * **Mappé sur** : `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_DESCRIPTION>`
  * **Peut apparaître several times** : Non.

**Informations sur les pièces jointes (pour chaque référence de document supplémentaire) :**

* **OBJET\_BINAIRE\_DOCUMENT\_INTÉGRÉ**
  * **Source** : `Attachment/EmbeddedDocumentBinaryObject/text()`
  * **Mappé sur** : `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EMBEDDED_DOCUMENT_BINARY_OBJECT>`
  * **Peut apparaître several times** : Non.
* **CODE\_MIME**
  * **Source** : `Attachment/EmbeddedDocumentBinaryObject/@mimeCode`
  * **Mappé sur** : `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><MIME_CODE>`
  * **Peut apparaître several times** : Non.
* **NOM\_DE\_FICHIER**
  * **Source** : `Attachment/EmbeddedDocumentBinaryObject/@filename`
  * **Mappé sur** : `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><FILENAME>`
  * **Peut apparaître several times** : Non.
* **URL\_RÉFÉRENCE\_EXTERNE**
  * **Source** : `Attachment/ExternalReference/URI/text()`
  * **Mappé sur** : `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EXTERNAL_REFERENCE_URL>`
  * **Peut apparaître several times** : Non.

</details>
