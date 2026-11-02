# Dépannage

## La nouvelle colonne n'apparaît pas sur l'écran de validation

* Le document a été traité avant l'ajout de la colonne. Les modifications s'appliquent aux documents importés ou redémarrés ensuite, **redémarrez le document** (Dashboard → menu du document → Restart).
* La colonne est **Hidden**. Vérifiez l'option dans la liste Table Columns.
* La colonne a été ajoutée à une **autre table** que celle affichée. L'écran de validation affiche les tables du type de document ; comparez la colonne *Table name*.
* Le document n'est pas du type de document que vous avez configuré.

## La colonne est là mais toujours vide

* Le fournisseur dispose de **règles entraînées** et la nouvelle colonne n'y est pas mappée. Ouvrez l'un des documents du fournisseur dans l'entraînement de tableau et mappez la colonne, ou activez *Use AI* sur la colonne.
* Avec l'extraction par IA, la valeur n'est pas reconnaissable sur le document (pas d'en-tête, abrégée, dans une autre langue). Ajoutez un [AI table tag](../../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) qui nomme la colonne, ou mappez-la dans l'entraînement.

## « Column name already exists »

Une colonne portant le même nom technique existe déjà dans la table. Si elle ne figure pas dans la liste, il s'agit d'une colonne par défaut masquée : le message indique *Please activate it in Table Column settings*. Désactivez *Hidden* sur cette colonne au lieu d'en créer une nouvelle.

## L'approbation est bloquée par une colonne obligatoire

Le message sur le tableau nomme la colonne. Renseignez la cellule dans chaque ligne ou (si la valeur n'existe pas sur ce document) décochez *Is Required* pour la colonne, redémarrez le document et réessayez. Demandez-vous si la colonne doit réellement être obligatoire (voir [Bonnes pratiques](best-practices-2.md)).

## L'IA renseigne une colonne avec une mauvaise valeur

Cas typique : `CHARGES` reçoit le total de la ligne, et chaque ligne échoue alors au contrôle du total avec *Line total does not match quantity x unit price (expected …, got …)*, car les frais font partie de la formule `quantité × prix unitaire + frais`.

* Décochez *Use AI* sur la colonne si les règles entraînées la saisissent correctement.
* Si le fournisseur n'a pas de règles, entraînez le tableau une fois (Table training) afin que la colonne soit liée à la bonne position, ou masquez la colonne si le fournisseur n'imprime jamais cette valeur.
* En dernier recours, *Skip table validation* dans les More Settings du type de document désactive tous les contrôles de tableau pour l'ensemble du type de document ; l'écart n'est alors plus détecté, pas plus que les colonnes obligatoires vides.

## PO matching : « Line Item Table is missing Mandatory column »

Le PO matching nécessite les colonnes par défaut numéro d'article, prix unitaire, quantité et montant total. L'une d'elles est masquée ou a été remplacée par une colonne personnalisée. Réaffichez la colonne par défaut, ou mappez la valeur sur celle-ci dans l'entraînement de tableau.

## Un script ou un export échoue après la suppression d'une colonne

Le script ou le mapping d'export fait toujours référence au *Column name* supprimé. Supprimez la référence, ou ajoutez à nouveau la colonne avec le même titre ; le nom technique est dérivé du titre et correspond de nouveau.

## Pour aller plus loin

* [Table Extraction Troubleshoot](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md) : qualité de l'extraction, OCR, E-Text
* [Champs de ligne de formation / Formation de table](../../../../setup/document-training/training-line-fields-table-training/README.md)
