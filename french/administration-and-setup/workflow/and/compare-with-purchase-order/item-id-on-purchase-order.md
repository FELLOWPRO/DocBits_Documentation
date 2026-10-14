# Item Id on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour comparer les identifiants d'article (item ID) entre un bon de commande et un document associé afin de garantir que les bons articles sont inclus. La carte évalue si l'item ID du bon de commande correspond à l'item ID du document. Cette comparaison peut déclencher des actions en cas d'écarts, garantissant que les articles du document sont alignés sur le bon de commande.

## **Composants de la carte :**

1. **Any / All :**
   * **Description** : définit si la condition s'applique à une ou à toutes les occurrences de comparaison d'item ID.
   * **Options** :
     * **Any** : la condition est satisfaite si un quelconque item ID du bon de commande correspond à l'item ID du document.
     * **All** : la condition n'est satisfaite que si tous les item ID du bon de commande correspondent aux item ID du document.
2. **Operator :**
   * **Description** : définit la condition de comparaison de l'item ID du bon de commande à l'item ID du document.
   * **Options** :
     * **Equals (=)** : vérifie si l'item ID du bon de commande correspond exactement à l'item ID du document.
     * **Not Equals (≠)** : s'assure que l'item ID du bon de commande ne correspond pas à l'item ID du document.

## **Fonctionnalité :**

* **Évaluation de la condition :** le système compare l'item ID du bon de commande à l'item ID du document en fonction de l'opérateur sélectionné. Si la condition de comparaison est vraie (par ex. les item ID correspondent ou ne correspondent pas), le workflow se poursuit en conséquence.
* **Exécution de l'action :**
  * **Condition vraie** : si la condition est évaluée comme vraie (par ex. l'item ID du bon de commande est égal à l'item ID du document), le workflow se poursuit avec l'action vraie (par ex. approbation ou traitement complémentaire).
  * **Condition fausse** : si la condition est évaluée comme fausse (par ex. l'item ID du bon de commande ne correspond pas à l'item ID du document), le workflow ne se poursuit pas.

## **Mise en place et configuration :**

* Les utilisateurs configurent la carte en sélectionnant l'item ID à la fois dans le bon de commande et dans le document. Ils choisissent ensuite l'opérateur approprié (Equals ou Not Equals) pour définir comment les item ID seront comparés. Enfin, les utilisateurs indiquent si la condition s'applique à une ou à toutes les occurrences des item ID de la comparaison.

## **Scénario d'exemple :**

* Une facture liste un article portant l'ID « ABC123 » et le bon de commande associé inclut également un article portant l'ID « ABC123 ». À l'aide de l'opérateur « Equals », la carte compare l'item ID du document à l'item ID du bon de commande. Puisque les item ID correspondent, le workflow se poursuit sans problème.

## **Conclusion :**

La carte de workflow « Item ID Comparison » garantit que les item ID des documents sont alignés sur ceux des bons de commande. Cela aide à prévenir les écarts dans les listes d'articles et garantit que les bons articles sont traités conformément au bon de commande. La possibilité de comparer en fonction d'une ou de toutes les occurrences offre de la flexibilité dans différents cas d'usage, améliorant l'exactitude et l'efficacité des workflows d'approvisionnement.
