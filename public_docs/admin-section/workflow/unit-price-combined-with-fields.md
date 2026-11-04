# Prix unitaire combiné avec des champs

<figure><img src="../../../../.gitbook/assets/image (26) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objet :**

Cette carte de flux de travail est conçue pour évaluer si le prix unitaire, lorsqu'il est combiné à une valeur de champ spécifiée (telle que la quantité, la remise ou des frais supplémentaires), remplit une condition définie. La carte compare le prix unitaire et la valeur du champ à un seuil spécifié pour aider à s'assurer que la tarification correspond aux attentes. Cette comparaison peut déclencher des actions basées sur des conditions spécifiques, comme le signalement de divergences ou l'automatisation des processus d'approbation dans les flux de travail d'achat ou de réception.

## **Composants de la carte :**

1. **Nom du champ**
   * **Description :** Spécifie le champ du document qui contient la valeur à combiner avec le prix unitaire.
   * **Détail :** Cela doit correspondre à l'identifiant exact du premier champ dans le document.
2. **Opérateur**
   * **Description :** Définit la condition qui sera appliquée à la comparaison entre la valeur combinée et la valeur spécifiée.
   * **Options :**
     * **Égal (=) :** Vérifie si la valeur combinée du prix unitaire et du champ correspond à la valeur spécifiée.
     * **Non égal (≠) :** Garantit que la valeur combinée du prix unitaire et du champ est différente de la valeur spécifiée.
     * **Supérieur à (>) :** Vérifie si la valeur combinée est supérieure à la valeur spécifiée.
     * **Supérieur ou égal (≥) :** Vérifie si la valeur combinée est supérieure ou égale à la valeur spécifiée.
     * **Inférieur à (<) :** Vérifie si la valeur combinée est inférieure à la valeur spécifiée.
     * **Inférieur ou égal (≤) :** Vérifie si la valeur combinée est inférieure ou égale à la valeur spécifiée.
3. **Valeur**
   * **Description :** Spécifie la valeur à laquelle la valeur combinée du prix unitaire et du champ sera comparée.
   * **Détail :** La valeur doit être une valeur numérique.

## **Fonctionnalité :**

* **Évaluation de la condition :** Le système évalue le prix unitaire combiné et la valeur du champ en fonction de l'opérateur sélectionné et le compare à la valeur spécifiée. Le résultat de cette évaluation détermine si la condition est vraie ou fausse.
* **Exécution de l'action :**
  * **Condition vraie :** Si la comparaison donne un résultat vrai (par exemple, la valeur combinée dépasse la valeur spécifiée), le flux de travail se poursuit avec la condition vraie. Cela peut déclencher des actions telles que l'approbation, l'acheminement du document ou l'application de règles de traitement.
  * **Condition fausse :** Si la comparaison donne un résultat faux (par exemple, la valeur combinée ne remplit pas la condition), le flux de travail se poursuit avec la condition fausse. Cela pourrait déclencher une notification, envoyer le document pour examen manuel ou arrêter le flux de travail.

## **Configuration et paramétrage :**

* Les utilisateurs commencent par sélectionner le ou les champs du document contenant la ou les valeurs à combiner avec le prix unitaire. Après avoir sélectionné le champ, ils choisissent ensuite l'opérateur approprié pour définir comment la valeur combinée sera comparée à la valeur spécifiée. Ils peuvent ensuite définir la valeur.

## **Exemple de scénario :**

* Une facture répertorie 50 unités d'un produit à 20 $ chacune, pour un total de 1 000 $. Le document associé contient un champ de quantité avec une valeur de 10. En utilisant l'opérateur « Supérieur à », la carte compare la valeur combinée du prix unitaire (20 $) et de la quantité (10), qui est égale à 200 $. La carte vérifie si la valeur combinée est supérieure à 150 $ (la valeur spécifiée). Comme la valeur combinée de 200 $ est supérieure au seuil de 150 $, le flux de travail se poursuit pour déclencher une approbation pour le document.

## **Conclusion :**

La carte de flux de travail "Prix unitaire combiné avec des champs" permet de s'assurer que les conditions tarifaires sont remplies en évaluant la valeur combinée du prix unitaire et d'un champ spécifié. En automatisant cette comparaison, les organisations peuvent assurer la cohérence et signaler les divergences de prix ou de quantités avant de procéder à l'approbation, ce qui aide à simplifier les processus d'achat et financiers.
