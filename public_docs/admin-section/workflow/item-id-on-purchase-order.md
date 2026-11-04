# ID de l'article sur le bon de commande

<figure><img src="../../../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objet :**

Cette carte de flux de travail est conçue pour comparer les identifiants (ID) d'articles entre un bon de commande et un document associé afin de s'assurer que les bons articles sont inclus. La carte évalue si l'ID de l'article dans le bon de commande correspond à l'ID de l'article dans le document. Cette comparaison peut déclencher des actions si des divergences sont constatées, garantissant que les articles du document s'alignent sur le bon de commande.

## **Composants de la carte :**

1. **N'importe quel / Tous (Any / All) :**
   * **Description :** Définit si la condition s'applique à n'importe quelle instance ou à toutes les instances de comparaison d'ID d'article.
   * **Options :**
     * **N'importe quel (Any) :** La condition est remplie si n'importe quel ID d'article dans le bon de commande correspond à l'ID de l'article dans le document.
     * **Tous (All) :** La condition n'est remplie que si tous les ID d'article du bon de commande correspondent aux ID d'article du document.
2. **Opérateur :**
   * **Description :** Définit la condition de comparaison de l'ID de l'article sur le bon de commande à l'ID de l'article sur le document.
   * **Options :**
     * **Égal (=) :** Vérifie si l'ID de l'article dans le bon de commande correspond exactement à l'ID de l'article dans le document.
     * **Non égal (≠) :** Garantit que l'ID de l'article dans le bon de commande ne correspond pas à l'ID de l'article dans le document.

## **Fonctionnalité :**

* **Évaluation de la condition :** Le système compare l'ID de l'article dans le bon de commande à l'ID de l'article dans le document en fonction de l'opérateur sélectionné. Si la condition de comparaison est vraie (par exemple, les ID d'article correspondent ou ne correspondent pas), le flux de travail se poursuivra en conséquence.
* **Exécution de l'action :**
  * **Condition vraie :** Si la condition est évaluée comme vraie (par exemple, l'ID de l'article dans le bon de commande est égal à l'ID de l'article dans le document), le flux de travail se poursuivra avec l'action vraie (par exemple, approbation ou traitement ultérieur).
  * **Condition fausse :** Si la condition est évaluée comme fausse (par exemple, l'ID de l'article dans le bon de commande ne correspond pas à l'ID de l'article dans le document), le flux de travail ne se poursuivra pas.

## **Configuration et paramétrage :**

* Les utilisateurs configurent la carte en sélectionnant l'ID de l'article à la fois dans le bon de commande et dans le document. Ils choisissent ensuite l'opérateur approprié (Égal ou Non égal) pour définir la manière dont les ID d'article seront comparés. Enfin, les utilisateurs choisissent si la condition s'applique à n'importe lequel ou à tous les ID d'article de la comparaison.

## **Exemple de scénario :**

* Une facture répertorie un article avec l'ID "ABC123" et le bon de commande associé comprend également un article avec l'ID "ABC123". En utilisant l'opérateur "Égal", la carte compare l'ID de l'article dans le document avec l'ID de l'article dans le bon de commande. Comme les ID d'article correspondent, le flux de travail continue sans problème.

## **Conclusion :**

La carte de flux de travail "Comparaison d'ID d'article" garantit que les ID d'article dans les documents correspondent à ceux des bons de commande. Cela permet d'éviter les divergences dans les listes d'articles et garantit que les bons articles sont traités conformément au bon de commande. La possibilité de comparer sur la base de n'importe quelle instance ou de toutes les instances offre une flexibilité pour différents cas d'utilisation, améliorant l'exactitude et l'efficacité des flux de travail d'achat.
