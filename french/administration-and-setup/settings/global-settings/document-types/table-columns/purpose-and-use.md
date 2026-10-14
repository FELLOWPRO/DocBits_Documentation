# Objectif et utilisation

Une colonne de table est un champ du tableau des lignes d'articles. Tout ce que DocBits fait avec un tableau (extraction, validation, PO matching, export) repose sur les colonnes configurées ici.

## Où une colonne intervient

| Endroit | Rôle de la colonne à cet endroit |
|---|---|
| **Validation screen** | Une colonne du tableau des lignes d'articles. Le *Title* est l'en-tête, le *Column Type* détermine l'éditeur (montant, date, texte, oui/non). Les colonnes masquées ne sont pas affichées. |
| **Table training** | Lorsque vous entraînez le tableau d'un fournisseur, vous associez chaque colonne détectée à l'une de ces colonnes configurées. Seules les colonnes configurées peuvent être mappées. |
| **AI table extraction** | L'IA renseigne les colonnes configurées. Une colonne marquée *Use AI* est renseignée par l'IA même pour les fournisseurs disposant de règles entraînées. |
| **Validation rules** | Les contrôles des lignes tels que *quantité × prix unitaire = total de la ligne* s'appliquent aux colonnes par défaut `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **PO matching** | Nécessite les colonnes par défaut numéro d'article, prix unitaire, quantité et montant total. Sans elles, le document affiche *Line Item Table is missing Mandatory column for PO*. |
| **Export** | Chaque colonne non masquée fait partie des données de lignes envoyées à l'ERP. Le mapping d'export fait référence au *Column name*. |
| **Scripts** | Les scripts lisent et écrivent les colonnes par *Column name*, par exemple `row["TOTAL_AMOUNT"]`. |

## Portée

* Les colonnes de table sont configurées **par table**, et une table appartient à un **type de document**. Les colonnes des factures n'ont aucun effet sur les bons de livraison.
* La configuration est **par organisation**. Les sous-organisations en héritent.
* Les colonnes qui sont *renseignées* pour un fournisseur donné sont déterminées par l'entraînement de ce fournisseur ou par l'IA ; la configuration des colonnes indique uniquement quelles colonnes existent.

## Raisons typiques de modifier la configuration

* Une valeur propre à un client doit être saisie pour chaque ligne (centre de coûts, numéro de projet, numéro d'article interne) → ajoutez une colonne.
* Une colonne par défaut n'est jamais utilisée et encombre l'écran de validation → masquez-la.
* Une colonne doit toujours être renseignée avant l'export → marquez-la *Required*.
* Une valeur provient de la recherche dans l'ERP et ne doit pas être modifiée par les utilisateurs → marquez-la *Read Only*.
* L'IA saisit mieux une colonne que les règles entraînées (par exemple les descriptions en texte libre) → marquez-la *Use AI*.

## Pages associées

* [Ajouter une nouvelle colonne](adding-a-new-column.md)
* [Modifier et supprimer des colonnes](editing-and-deleting-columns.md)
* [Table Extraction Troubleshoot](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md)
