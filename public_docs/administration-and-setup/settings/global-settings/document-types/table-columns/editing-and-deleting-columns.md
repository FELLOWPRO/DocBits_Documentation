# Modifier et supprimer des colonnes

Les cases contrôlent les valeurs obligatoires, la modification et la visibilité. Use AI se règle séparément dans la liste à trois états expliquée ci-dessous.

Tout, à l'exception du titre, se modifie directement dans la liste ; il n'y a pas de boîte de dialogue de modification.

**Où :** Settings → Document Processing → Document Types → Table Columns

## Activer ou désactiver une option

Cochez ou décochez la case dans la ligne. La modification est enregistrée immédiatement (*Successfully saved*).

| Option | Activée | Désactivée |
|---|---|---|
| **Is Required** | L'approbation est bloquée tant que la colonne est vide dans une ligne quelconque ; l'écran de validation marque la cellule. | Les cellules vides sont autorisées. |
| **Read Only** | La valeur est affichée mais ne peut pas être écrasée. À utiliser pour les valeurs provenant d'une recherche ou d'un script. | Les utilisateurs peuvent modifier la cellule. |
| **Hidden** | La colonne disparaît de l'écran de validation et de l'export. Ses données sont conservées. | La colonne est affichée et exportée. |


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

## Use AI : Par défaut, Oui ou Non

Ouvrez les [colonnes de tableau](README.md) du bon type de document et du bon tableau. **Utiliser l'IA (Use AI)** est une liste à trois états, pas une case à cocher. Le choix est enregistré immédiatement.

| Choix actuel | Effet sur le schéma de base |
| --- | --- |
| **Default · demandé** ou **Default · non demandé** | Applique la sélection DocBits pour ce type et ce nom de colonne. Par défaut ne signifie ni toujours activé ni toujours désactivé. |
| **Yes · demandé** | Demande explicitement cette colonne configurée à l'IA. |
| **No · non demandé** | L'exclut du schéma de base, même si elle est normalement demandée. |

Revenir à **Default** supprime le choix explicite. Une nouvelle colonne personnalisée n'appartient normalement pas à la sélection IA par défaut : choisissez **Yes** pour la demander. Les colonnes IA par défaut ne correspondent pas à toutes les colonnes fournies. Vérifiez l'effet affiché et l'aperçu.

**Required**, **Read Only** et **Hidden** concernent les contrôles de complétude, la modification et la visibilité ; ils ne remplacent pas le choix IA. **No** ne supprime ni la colonne ni ses valeurs et n'empêche pas des règles, scripts ou autres sources de la renseigner. L'apprentissage fournisseur et les tags IA peuvent étendre la demande effective : résolvez aussi leurs contradictions. Le commutateur ne remplace pas automatiquement un résultat purement issu de règles.

[Structured Output pour les tableaux](../../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
