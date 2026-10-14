# Modifier et supprimer des colonnes

Tout, à l'exception du titre, se modifie directement dans la liste ; il n'y a pas de boîte de dialogue de modification.

**Où :** Settings → Global Settings → Document Types → Table Columns

## Activer ou désactiver une option

Cochez ou décochez la case dans la ligne. La modification est enregistrée immédiatement (*Successfully saved*).

| Option | Activée | Désactivée |
|---|---|---|
| **Is Required** | L'approbation est bloquée tant que la colonne est vide dans une ligne quelconque ; l'écran de validation marque la cellule. | Les cellules vides sont autorisées. |
| **Read Only** | La valeur est affichée mais ne peut pas être écrasée. À utiliser pour les valeurs provenant d'une recherche ou d'un script. | Les utilisateurs peuvent modifier la cellule. |
| **Hidden** | La colonne disparaît de l'écran de validation et de l'export. Ses données sont conservées. | La colonne est affichée et exportée. |
| **Use AI** | L'extraction de tableau par IA renseigne cette colonne, y compris pour les fournisseurs disposant de règles entraînées. | La colonne est renseignée par les règles entraînées, ou par l'IA lorsqu'aucune règle n'existe. |

{% hint style="info" %}
Les options prennent effet sur les documents importés ou redémarrés **après** la modification. Les documents ouverts conservent leur tableau actuel jusqu'à leur redémarrage.
{% endhint %}

## Renommer le titre

Cliquez sur l'icône de traduction dans la colonne *Actions* (*Update translation key*), saisissez le nouveau libellé et confirmez. L'icône d'information à côté indique quel libellé est actuellement en vigueur et d'où il provient. Seul le libellé change ; le *Column name* technique reste le même, de sorte que les scripts, les mappings d'export et les règles entraînées continuent de fonctionner.

## Modifier le type ou la table

Impossible. Masquez la colonne (ou supprimez-la s'il s'agit de la vôtre) et ajoutez-en une nouvelle avec le bon type.

## Supprimer une colonne

L'action de suppression n'est proposée que pour les colonnes créées par votre organisation. Les colonnes par défaut ne peuvent pas être supprimées, masquez-les.

1. Ouvrez le menu à trois points dans la colonne *Actions* et choisissez **Delete**. L'entrée est absente pour les colonnes par défaut.
2. Confirmez.

Ce qui se passe :

* La colonne est retirée de la configuration. Les documents traités **à partir de maintenant** ne l'ont plus.
* Les documents déjà extraits conservent la colonne et ses valeurs jusqu'à leur redémarrage.
* Les règles entraînées qui mappaient cette colonne continuent de fonctionner pour les autres colonnes ; le mapping de la colonne supprimée est ignoré.
* Si la colonne est référencée dans un mapping d'export ou dans un script, supprimez cette référence ; sinon l'export ou le script échoue avec une erreur de colonne manquante.

## Annuler une suppression

Une colonne supprimée ne peut pas être restaurée depuis la liste. Ajoutez-la à nouveau avec le même titre : le nom technique est dérivé du titre, donc une colonne créée avec le même titre reçoit le même *Column name* et les mappings existants correspondent de nouveau.
