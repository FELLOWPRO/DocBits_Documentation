# Peppol BIS Billing 3.0

### Aperçu

Cette section décrit le plan de mise en œuvre pour l'importation et le mappage des données à partir de fichiers XML utilisant le schéma Peppol BIS Billing 3.0. Peppol BIS Billing 3.0 a été développé pour standardiser les processus de facturation électronique et assurer la conformité aux normes européennes.

### Objectifs

* Assurer une conformité totale avec les spécifications Peppol BIS Billing 3.0.
* Intégration transparente des données de facture électronique dans notre système de comptes fournisseurs à l'aide de DocBits.
* Améliorer la qualité des données et l'efficacité du traitement.

### Portée

La portée de ce projet est de mapper les éléments clés du schéma Peppol BIS Billing 3.0 à nos structures de données internes. En particulier, le mappage couvrira les domaines suivants :

* Détails du fournisseur et de l'acheteur
* Détails de la facture
* Lignes de facture
* Instructions de paiement
* Informations fiscales et juridiques

### Éléments clés et mappage

**Informations sur le fournisseur :**

* cac:AccountingSupplierParty
  * cbc:EndpointID : Adresse électronique du fournisseur
  * cbc:Name : Nom commercial du fournisseur
  * cbc:CompanyID : Numéro d'enregistrement légal du fournisseur
  * cbc:StreetName, cbc:CityName, cbc:PostalZone : Détails de l'adresse du fournisseur

**Informations sur l'acheteur :**

* cac:AccountingCustomerParty
  * cbc:EndpointID : Adresse électronique de l'acheteur
  * cbc:Name : Nom commercial de l'acheteur
  * cbc:CompanyID : Numéro d'enregistrement légal de l'acheteur
  * cbc:StreetName, cbc:CityName, cbc:PostalZone : Détails de l'adresse de l'acheteur

**Détails de la facture :**

* cbc:ID : Numéro de facture
* cbc:IssueDate : Date d'émission de la facture
* cbc:DueDate : Date d'échéance de la facture
* cbc:InvoiceTypeCode : Type de facture

**Lignes de facture :**

* cac:InvoiceLine
  * cbc:ID : Numéro de ligne de facture
  * cbc:InvoicedQuantity : Quantité facturée
  * cbc:LineExtensionAmount : Montant de l'extension de ligne
  * cbc:Description : Description du poste de facturation
  * cac:Item
    * cbc:Name : Nom de l'article
    * cbc:SellerItemIdentification/cbc:ID : Numéro d'article du fournisseur
  * cac:Price
    * cbc:PriceAmount : Prix unitaire
    * cbc:BaseQuantity : Quantité de base pour le prix

**Instructions de paiement :**

* cac:PaymentMeans
  * cbc:PaymentMeansCode : Code pour identifier le mode de paiement
  * cbc:PaymentID : Identifiant de paiement

**Informations fiscales :**

* cac:TaxTotal
  * cbc:TaxAmount : Montant total de la taxe
  * cac:TaxSubtotal : Détails pour chaque montant de taxe intermédiaire

### Aperçu PDF pour la facture électronique

Un document PDF est généré selon une mise en page standard avec les champs importés afin de fournir à l'utilisateur un aperçu à titre de référence. Une personnalisation plus poussée de la mise en page de l'aperçu PDF est possible mais nécessite un effort supplémentaire.
