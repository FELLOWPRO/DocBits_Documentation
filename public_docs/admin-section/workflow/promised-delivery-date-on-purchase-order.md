# Date de livraison promise sur le bon de commande

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objet**

Cette carte DocBits est conçue pour faciliter la comparaison précise des dates de livraison promises sur les bons de commande avec les dates de livraison spécifiées pour les articles dans un tableau. En intégrant une valeur de tolérance, la carte assure une flexibilité dans le suivi des délais de livraison, aidant à maintenir l'exactitude de la planification des stocks et la satisfaction des clients.

## **Composants de la carte**

1. **Opérateur**
   * **Description :** Définit la condition appliquée pour comparer les dates de livraison.
   * **Options :**
     * **Égal (=) :** Vérifie si la date de livraison promise sur l'article correspond à la date de livraison du bon de commande.
     * **Non égal (≠) :** Garantit que la date de livraison promise sur l'article ne correspond pas à la date sur le bon de commande.
     * **Supérieur à (>) :** Vérifie si la date de livraison promise de l'article est postérieure à la date de livraison du bon de commande.
     * **Supérieur ou égal (≥) :** Vérifie si la date de livraison promise de l'article est égale ou postérieure à la date de livraison du bon de commande.
     * **Inférieur à (<) :** Confirme si la date de livraison promise de l'article est antérieure à la date de livraison du bon de commande.
     * **Inférieur ou égal (≤) :** Valide si la date de livraison promise de l'article est égale ou antérieure à la date de livraison du bon de commande.
2. **Valeur**
   * **Description :** Spécifie une marge d'erreur admissible dans la comparaison des dates de livraison.
   * **Détail :** Les utilisateurs définissent le nombre de jours pendant lesquels la date de livraison de l'article peut différer de la date de livraison promise.

## **Fonctionnalité**

* **Évaluation de la condition :**
  La carte calcule la différence entre la date de livraison promise du bon de commande et les dates de livraison des articles dans le tableau. L'opérateur sélectionné est ensuite appliqué pour déterminer si la condition est remplie.
* **Exécution de l'action :**
  * **Condition vraie :** Si la différence de date de livraison se situe dans la plage de tolérance et correspond à la condition définie par l'opérateur, le flux de travail se poursuit.
  * **Condition fausse :** Si la condition n'est pas remplie, le flux de travail ne continuera pas.

## **Configuration et paramétrage**

* L'opérateur est sélectionné pour définir la condition de comparaison souhaitée, telle qu'égal à, supérieur à ou inférieur à. Enfin, les utilisateurs spécifient une valeur de tolérance en jours, ce qui permet de légères variations dans la comparaison sans déclencher d'alertes.

## **Exemple de scénario**

* Un bon de commande spécifie une date de livraison promise au 1er décembre. Un article dans le tableau a une date de livraison promise au 3 décembre. Avec une valeur de tolérance fixée à 2 jours et l'opérateur **Supérieur ou égal (≥)** sélectionné, la carte considère que la date de livraison se situe dans la plage acceptable. Aucune alerte n'est déclenchée, garantissant que les écarts mineurs sont tolérés sans perturber les opérations.

## **Conclusion**

La carte "Comparaison de la date de livraison promise" aide à simplifier les opérations de la chaîne d'approvisionnement en permettant un suivi précis des délais de livraison. Grâce à sa capacité à intégrer des tolérances et des opérateurs de comparaison flexibles, elle garantit le respect des attentes de livraison tout en évitant les alertes inutiles pour des écarts mineurs. Cela améliore la gestion des fournisseurs et l'efficacité globale du flux de travail.
