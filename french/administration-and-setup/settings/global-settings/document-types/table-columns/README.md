# Table Columns

Les Table Columns définissent les colonnes du tableau des lignes d'un type de document : ce que DocBits extrait dans chaque colonne, ce que l'utilisateur voit sur l'écran de validation et ce qui est envoyé à l'ERP lors de l'export.

**Où :** Settings → Global Settings → Document Types → Table Columns

<figure><img src="../../../../../.gitbook/assets/table-columns_list.png" alt="Liste des Table Columns avec les indicateurs Required, Read Only, Hidden et Use AI pour chaque colonne"><figcaption><p>Table Columns : une ligne par colonne, les indicateurs se modifient directement dans la liste</p></figcaption></figure>

## Ce que vous voyez

Chaque ligne correspond à une colonne d'une table. La liste affiche :

| Colonne | Signification |
|---|---|
| **Column name** | Nom technique, généré à partir du titre (majuscules, tirets bas). Utilisé dans les scripts, les mappings d'export et l'API. Ne peut pas être modifié par la suite. |
| **Title** | Libellé affiché sur l'écran de validation. Modifiez-le avec l'icône de traduction dans la colonne *Actions* (*Update translation key*). |
| **Column Type** | `AMOUNT`, `STRING`, `DATE`, `NUMBER`, `BOOLEAN` ou `CURRENCY`. Détermine la validation et le formatage. |
| **Table name** | La table à laquelle appartient la colonne, par exemple `INVOICE_TABLE`. |
| **Is Required** | Le document ne peut pas être approuvé tant que cette colonne est vide dans une ligne quelconque. |
| **Read Only** | Les utilisateurs voient la valeur mais ne peuvent pas la modifier. |
| **Hidden** | La colonne n'est ni affichée ni exportée. Sert à désactiver les colonnes par défaut dont vous n'avez pas besoin. |
| **Use AI** | L'extraction de tableau par IA remplit cette colonne, même lorsqu'un fournisseur a des règles entraînées. |
| **Actions** | Icône de traduction : renommer le titre. Icône d'information : origine du libellé affiché (votre traduction, la valeur par défaut, la clé). Menu à trois points : *Delete*, uniquement pour les colonnes créées par votre organisation ; les colonnes par défaut peuvent seulement être masquées. |

Deux boutons au-dessus de la liste :

* **Create new table** : un second tableau de lignes pour le type de document (par exemple un tableau de frais à côté du tableau des articles).
* **Add new table column** : ouvre la boîte de dialogue décrite dans [Ajouter une nouvelle colonne](adding-a-new-column.md).

## Colonnes par défaut et colonnes personnalisées

Chaque type de document est fourni avec un ensemble de colonnes par défaut (pour les factures : numéro d'article, description, quantité, prix unitaire, montant total, taxe, …). Elles appartiennent à DocBits et non à votre organisation ; elles ne peuvent donc pas être supprimées, masquez-les plutôt. Les colonnes que vous ajoutez vous-même appartiennent à votre organisation et peuvent être supprimées.

{% hint style="info" %}
**Les modifications ne s'appliquent qu'aux nouveaux documents.** Une colonne que vous ajoutez, masquez ou supprimez apparaît sur les documents téléversés ou redémarrés après la modification. Les documents déjà présents dans le tableau de bord conservent leur tableau tel qu'il a été extrait. Redémarrez un document pour prendre en compte la nouvelle configuration.
{% endhint %}

## Pages associées

* [Objectif et utilisation](purpose-and-use.md) : où apparaissent les colonnes de tableau
* [Ajouter une nouvelle colonne](adding-a-new-column.md)
* [Modifier et supprimer des colonnes](editing-and-deleting-columns.md)
* [Bonnes pratiques](best-practices-2.md)
* [Dépannage](troubleshooting-1.md)
* [Training Line Fields / Table Training](../../../../setup/document-training/training-line-fields-table-training/README.md) : indiquez à DocBits où se trouve le tableau d'un fournisseur
* [AI Table](../../../../../end-user-and-partner-section/end-user-section/ai-table/README.md) : ce que l'utilisateur voit sur l'écran de validation
