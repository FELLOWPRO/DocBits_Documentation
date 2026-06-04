# Out of Tolerance Unit Price

<figure><img src="../../../../.gitbook/assets/image (272).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour évaluer si la valeur combinée des prix unitaires et d'un champ spécifié dépasse ou n'atteint pas un seuil défini. Elle aide à identifier les écarts où les prix unitaires, combinés à d'autres champs, sont hors tolérance, garantissant que les conditions de prix respectent les attentes et signalant tout problème pour examen ou action complémentaire.

## **Composants de la carte :**

1. **Field Name :**
   * **Description** : spécifie le champ de document qui contient la valeur à combiner avec le prix unitaire.
   * **Détail** : la valeur de ce champ sera combinée au prix unitaire pour créer la valeur combinée totale à comparer.
2. **Operator :**
   * **Description** : définit la condition de comparaison de la valeur combinée du prix unitaire et de la valeur du champ par rapport à la valeur spécifiée.
   * **Options** :
     * **Equals (=)** : vérifie si la valeur combinée du prix unitaire et du champ correspond à la valeur spécifiée.
     * **Not Equals (≠)** : s'assure que la valeur combinée du prix unitaire et du champ diffère de la valeur spécifiée.
     * **Greater Than (>)** : vérifie si la valeur combinée du prix unitaire et du champ dépasse la valeur spécifiée.
     * **Greater or Equals (≥)** : vérifie si la valeur combinée du prix unitaire et du champ est supérieure ou égale à la valeur spécifiée.
     * **Lesser Than (<)** : vérifie si la valeur combinée du prix unitaire et du champ est inférieure à la valeur spécifiée.
     * **Lesser or Equals (≤)** : vérifie si la valeur combinée du prix unitaire et du champ est inférieure ou égale à la valeur spécifiée.
3. **Value :**
   * **Description** : spécifie la valeur à laquelle la valeur combinée du prix unitaire et du champ sera comparée.
   * **Détail** : cette valeur numérique représente le seuil de comparaison. Si la valeur combinée du prix unitaire et du champ dépasse ou n'atteint pas cette valeur (selon l'opérateur sélectionné), la condition déclenchera les actions spécifiées.

## **Fonctionnalité :**

* &#x20;**Évaluation de la condition :** le système calcule la valeur combinée en multipliant ou en additionnant le prix unitaire avec la valeur du champ, selon la configuration. Le résultat est ensuite comparé à la valeur spécifiée à l'aide de l'opérateur sélectionné. Si la condition est satisfaite (c.-à-d. que la valeur combinée est hors tolérance), le workflow poursuit avec l'étape suivante, qu'il s'agisse d'une approbation, d'un rejet ou d'un examen complémentaire.
* **Exécution de l'action :**
  * **Condition vraie** : si la comparaison renvoie vrai (c.-à-d. que la valeur combinée satisfait la condition), le workflow déclenche l'action associée à la condition vraie (par ex. approbation ou notification).
  * **Condition fausse** : si la comparaison renvoie faux (c.-à-d. que la valeur combinée ne satisfait pas la condition), le workflow ne se poursuit pas.

## **Mise en place et configuration :**

* Les utilisateurs sélectionnent le champ qui contient la valeur à combiner avec le prix unitaire. Ils choisissent ensuite l'opérateur approprié pour déterminer comment la valeur combinée sera comparée à la valeur spécifiée. Enfin, l'utilisateur définit la valeur à laquelle le prix combiné sera comparé.

## **Scénario d'exemple :**

* Une facture liste 50 unités d'un produit à 30 $ chacune, soit un total de 1500 $. Le document associé possède un champ de quantité d'une valeur de 10. Le prix combiné est calculé en multipliant le prix unitaire (30 $) par la quantité (10), ce qui donne 300 $. La carte compare ensuite cette valeur combinée à un seuil de 250 $. À l'aide de l'opérateur « Greater Than », la carte constate que 300 $ est supérieur à 250 $, déclenchant un processus d'approbation pour le document.

## **Conclusion :**

La carte de workflow « Out of Tolerance Unit Prices Combined with Fields » aide à garantir que les valeurs de prix et de champs sont alignées sur les règles métier. En automatisant cette vérification, les organisations peuvent identifier les écarts en amont du processus, garantissant que tout prix unitaire hors tolérance est signalé pour examen ou action nécessaire.
