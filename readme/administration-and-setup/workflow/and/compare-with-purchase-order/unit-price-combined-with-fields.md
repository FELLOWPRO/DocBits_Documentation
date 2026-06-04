# Unit Price Combined with Fields

<figure><img src="../../../../.gitbook/assets/image (26) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour évaluer si le prix unitaire, combiné à la valeur d'un champ spécifié (comme la quantité, la remise ou des frais supplémentaires), satisfait une condition définie. La carte compare le prix unitaire et la valeur du champ à un seuil spécifié afin de garantir que la tarification est conforme aux attentes. Cette comparaison peut déclencher des actions selon des conditions spécifiques, comme signaler des écarts ou automatiser les processus d'approbation dans les workflows d'approvisionnement ou de réception.

## **Composants de la carte :**

1. **Field Name**
   * **Description :** spécifie le champ de document qui contient la valeur à combiner avec le prix unitaire.
   * **Détail :** il doit correspondre à l'identifiant exact du premier champ dans le document.
2. **Operator**
   * **Description :** définit la condition qui sera appliquée à la comparaison entre la valeur combinée et la valeur spécifiée.
   * **Options :**
     * **Equals (=) :** vérifie si la valeur combinée du prix unitaire et du champ correspond à la valeur spécifiée.
     * **Not Equals (≠) :** s'assure que la valeur combinée du prix unitaire et du champ diffère de la valeur spécifiée.
     * **Greater Than (>) :** vérifie si la valeur combinée est supérieure à la valeur spécifiée.
     * **Greater or Equals (≥) :** vérifie si la valeur combinée est supérieure ou égale à la valeur spécifiée.
     * **Lesser Than (<) :** vérifie si la valeur combinée est inférieure à la valeur spécifiée.
     * **Lesser or Equals (≤) :** vérifie si la valeur combinée est inférieure ou égale à la valeur spécifiée.
3. **Value**
   * **Description :** spécifie la valeur à laquelle la valeur combinée du prix unitaire et du champ sera comparée.
   * **Détail :** la valeur doit être une valeur numérique.

## **Fonctionnalité :**

* **Évaluation de la condition :** le système évalue la valeur combinée du prix unitaire et du champ en fonction de l'opérateur sélectionné et la compare à la valeur spécifiée. Le résultat de cette évaluation détermine si la condition est vraie ou fausse.
* **Exécution de l'action :**
  * **Condition vraie :** si la comparaison renvoie vrai (par ex. la valeur combinée dépasse la valeur spécifiée), le workflow se poursuit avec la condition vraie. Cela peut déclencher des actions telles que l'approbation, l'acheminement du document ou l'application de règles de traitement.
  * **Condition fausse :** si la comparaison renvoie faux (par ex. la valeur combinée ne satisfait pas la condition), le workflow se poursuit avec la condition fausse. Cela peut déclencher une notification, envoyer le document pour un examen manuel ou arrêter le workflow.

## **Mise en place et configuration :**

* Les utilisateurs commencent par sélectionner le ou les champs de document qui contiennent la ou les valeurs à combiner avec le prix unitaire. Après avoir sélectionné le champ, ils choisissent l'opérateur approprié pour définir comment la valeur combinée sera comparée à la valeur spécifiée. Ils peuvent ensuite définir la valeur.

## **Scénario d'exemple :**

* Une facture liste 50 unités d'un produit à 20 $ chacune, soit un total de 1000 $. Le document associé possède un champ de quantité d'une valeur de 10. À l'aide de l'opérateur « Greater Than », la carte compare la valeur combinée du prix unitaire (20 $) et de la quantité (10), qui équivaut à 200 $. La carte vérifie si la valeur combinée est supérieure à 150 $ (la valeur spécifiée). Puisque la valeur combinée de 200 $ est supérieure au seuil de 150 $, le workflow se poursuit en déclenchant une approbation pour le document.

## **Conclusion :**

La carte de workflow « Unit Price Combined with Fields » garantit que les conditions de tarification sont satisfaites en évaluant la valeur combinée du prix unitaire et d'un champ spécifié. En automatisant cette comparaison, les organisations peuvent garantir la cohérence et signaler les écarts de prix ou de quantité avant de procéder à l'approbation, contribuant à rationaliser les processus d'approvisionnement et financiers.
