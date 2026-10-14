# Bonnes pratiques

## Conserver les colonnes par défaut pour les montants et les quantités

Les contrôles des lignes (*quantité × prix unitaire = total de la ligne*) et le PO matching recherchent les colonnes par défaut `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. Si vous créez vos propres colonnes pour ces valeurs, les contrôles ne s'exécutent pas et le PO matching signale des colonnes obligatoires manquantes. Renommez le *titre* si la formulation ne vous convient pas ; conservez la colonne.

## Masquer plutôt que supprimer

Les colonnes par défaut dont vous n'avez pas besoin sont masquées, non supprimées ; elles ne peuvent de toute façon pas être supprimées. Pour vos propres colonnes, le masquage est également le choix le plus sûr tant que vous ne savez pas si un script ou un mapping d'export fait encore référence à la colonne.

## Ne marquer comme obligatoire que ce qui bloque l'export

Chaque colonne obligatoire doit être renseignée dans chaque ligne avant qu'un utilisateur puisse approuver le document. Utilisez cette option pour les valeurs que l'ERP rejette lorsqu'elles manquent (par exemple le centre de coûts dans un export comptable), et non pour des valeurs simplement utiles.

## Utiliser *Read Only* pour les valeurs issues d'une recherche

Les valeurs qu'un script ou une recherche dans les données de base écrit dans la table (description de l'article issue de la fiche article, code de taxe issu du fournisseur) doivent être en lecture seule, afin que les utilisateurs corrigent la source plutôt que la copie.

## Utiliser l'IA par colonne, pas par fournisseur

Pour un fournisseur disposant de règles entraînées, la plupart des colonnes sont correctement extraites grâce à ces règles. Si une colonne n'est pas fiable (longues descriptions sur plusieurs lignes, remise parfois située à un autre endroit), activez *Use AI* uniquement sur cette colonne. Les règles gèrent le reste.

## Nommer les colonnes pour l'ERP, pas pour le document

Le *Column name* se retrouve dans les mappings d'export et dans les scripts. `COST_CENTRE` est plus facile à mapper que `KST` et ne change pas lorsqu'un fournisseur l'imprime différemment.

## Tester sur un document redémarré

Après une modification, redémarrez un document existant du type de document et ouvrez-le : la nouvelle colonne apparaît, la colonne masquée a disparu, les cellules obligatoires sont marquées. Ce n'est qu'ensuite qu'il faut déployer la modification auprès des utilisateurs.

## Une table par structure de lignes

Ne créez une seconde table que si un type de document comporte réellement deux tables indépendantes (par exemple des lignes d'articles et une table distincte de frais). Les tables vides supplémentaires apparaissent sur chaque document du type.
