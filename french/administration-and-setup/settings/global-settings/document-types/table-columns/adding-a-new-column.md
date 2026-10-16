# Ajouter une nouvelle colonne

Ajoutez une colonne lorsqu'une valeur doit être saisie pour chaque ligne et que les colonnes par défaut ne la couvrent pas : un centre de coûts, un numéro de projet, un numéro d'article interne.

## Avant de commencer

* Décidez à quelle **table** appartient la colonne. La plupart des types de document ont une seule table (par exemple `INVOICE_TABLE`). Si la liste est vide, cliquez d'abord sur **Create new table** ; la boîte de dialogue demande uniquement un nom de table.
* Décidez du **type** : `AMOUNT` pour les montants, `NUMBER` pour les quantités, `DATE`, `BOOLEAN` pour oui/non, `CURRENCY` pour un code de devise ISO, `STRING` pour tout le reste. Le type ne peut plus être modifié après l'enregistrement.
* Vérifiez si une **colonne par défaut** de même signification existe déjà mais est masquée. Les colonnes masquées apparaissent dans la liste avec l'indicateur _Hidden_ activé ; réaffichez-la au lieu de créer un doublon.

## Étapes

1. Ouvrez **Settings → Global Settings → Document Types → Table Columns**.
2. Cliquez sur **Add new table column**.

<figure><img src="../../../../../.gitbook/assets/table-columns_add-dialog.png" alt="Boîte de dialogue Add new table column avec Title, Is column required, Select column type et Select Table"><figcaption><p>Add new table column</p></figcaption></figure>

3. Remplissez la boîte de dialogue :

| Champ                   | Ce qu'il faut saisir                                                                                                                                                               |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Title**               | Libellé que l'utilisateur voit sur l'écran de validation, par exemple `Cost Centre`. Lettres et chiffres uniquement. DocBits en déduit le _Column name_ technique (`COST_CENTRE`). |
| **Is column required?** | Cochez si le document ne doit pas être approuvé tant que la colonne est vide dans une ligne quelconque.                                                                            |
| **Select column type**  | Voir la liste des types ci-dessus.                                                                                                                                                 |
| **Select Table**        | La table qui reçoit la colonne.                                                                                                                                                    |

4. Cliquez sur **Proceed**. La colonne apparaît dans la liste avec _Read Only_, _Hidden_ et _Use AI_ désactivés. Modifiez ces indicateurs dans la liste si nécessaire, voir [Modifier et supprimer des colonnes](editing-and-deleting-columns.md).

## Après l'ajout

* La colonne est **vide sur les documents existants**. Elle est remplie sur les documents téléversés ou redémarrés après la modification.
* Pour les fournisseurs avec des **règles entraînées**, ouvrez l'un de leurs documents dans l'entraînement de tableau et associez la nouvelle colonne, sinon la colonne reste vide pour ce fournisseur. Voir [Defining tables and columns](../../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* Avec l'**extraction de tableau par IA**, l'IA remplit la colonne si la valeur est reconnaissable sur le document. Cochez _Use AI_ pour la colonne si le fournisseur a des règles entraînées mais que cette colonne doit tout de même provenir de l'IA.
* Ajoutez la colonne au **mapping d'export** si l'ERP doit la recevoir, voir [Export](../../../document-processing/export/).

## Messages

| Message                                                                    | Signification                                                                                                    |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| _Column name already exists_                                               | Une colonne portant ce nom technique existe déjà dans la table. Choisissez un autre titre.                       |
| _Column name already exists – Please activate it in Table Column settings_ | Une colonne par défaut masquée porte ce nom. Désactivez son indicateur _Hidden_ au lieu d'en créer une nouvelle. |
| _No table exists. Please create table before creating columns._            | Le type de document n'a pas encore de table : cliquez d'abord sur **Create new table**.                          |
