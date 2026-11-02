---
hidden: true
noIndex: true
---

# M3\_OLD

## Importer un modèle de connexion API dans Infor M3

Ce guide explique comment importer un modèle de connexion API (API Connection Template) afin de configurer rapidement les principaux paramètres d'intégration avec Infor M3. L'utilisation d'un modèle permet d'établir une configuration de connexion prédéfinie, ce qui simplifie le processus et garantit la cohérence.

<mark style="color:red;">**Remarque**</mark> : pour la configuration détaillée de domaines spécifiques tels que Auto Accounting, l'intégration des fournisseurs, les bons de commande ou l'extraction de tableaux pour les éléments de coût, consultez la documentation correspondante :

* [Auto Accounting](m3/auto-accounting.md)
* [Fournisseurs et bons de commande](m3/suppliers-and-purchase-orders.md)
* [Comment importer tous les fournisseurs](m3/how-to-import-all-suppliers.md)
* [Extraction de tableaux pour les éléments de coût](m3/table-extraction-for-costing-element.md)

### **Télécharger le modèle**

Avant l'importation, téléchargez le modèle de connexion requis à l'aide du fichier ci-dessous :

{% file src="../../.gitbook/assets/DocBits-Dev-Import-Template (1).xml" %}

### Importer le modèle

#### Étapes pour importer un modèle de connexion

1. **Accéder à Infor ION Desk :**
   *   Accédez à **InforOS** → **ION Desk** → **Connect** → **Connection Points**.

       ![Menu de navigation d'Infor ION Desk avec les entrées Home, Data Flows, API Flows et Mappings](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)
2. **Importer le modèle :**
   *   Cliquez sur le bouton **Import**.

       <figure><img src="../../.gitbook/assets/m3_import_2.png" alt="Page Connect d'Infor ION Desk montrant la vue Connection Points avec sa recherche et sa barre d'outils"><figcaption></figcaption></figure>
   * Sélectionnez le **Template File** approprié sur votre système local.
   *   Cliquez sur **OK** pour lancer le processus d'importation.

       <figure><img src="../../.gitbook/assets/m3_import_3.png" alt="Boîte de dialogue Upload Local File dans Infor ION Desk avec le fichier DocBits-Dev-Prod-Import-Template sélectionné pour le chargement" width="327"><figcaption></figcaption></figure>
3. **Confirmation :**
   *   Si l'importation réussit, un message de confirmation s'affiche.

       <figure><img src="../../.gitbook/assets/m3_import_4.png" alt="Confirmation d'importation dans Infor ION Desk indiquant que l'importation de DocBits-Dev-Prod-Import-Template a réussi"><figcaption></figcaption></figure>
4. **Configuration après l'importation :**
   * Une fois le modèle importé, vous pouvez personnaliser certains paramètres de connexion selon vos besoins.
   * N'oubliez pas d'importer ou de configurer votre **Service Account** pour l'authentification et le contrôle d'accès.

<figure><img src="../../.gitbook/assets/m3_import_5.png" alt="Page API Connection Point de DocBits-Dev-Prod-Import-Template avec son nom, son ID logique et ses détails d'authentification"><figcaption></figcaption></figure>
