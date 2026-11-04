# Prix unitaire hors tolérance

<figure><img src="../../../../.gitbook/assets/image (272).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objet :**

Cette carte de flux de travail est conçue pour évaluer si la valeur combinée des prix unitaires et d'un champ spécifié dépasse ou est inférieure à un seuil défini. Elle aide à identifier toute divergence où les prix unitaires, lorsqu'ils sont combinés à d'autres champs, sont hors tolérance, garantissant que les conditions de prix répondent aux attentes et signalant tout problème pour examen ou action ultérieure.

## **Composants de la carte :**

1. **Nom du champ :**
   * **Description :** Spécifie le champ du document qui contient la valeur à combiner avec le prix unitaire.
   * **Détail :** La valeur de ce champ sera combinée au prix unitaire pour créer la valeur combinée totale aux fins de comparaison.
2. **Opérateur :**
   * **Description :** Définit la condition de comparaison de la valeur combinée du prix unitaire et de la valeur du champ par rapport à la valeur spécifiée.
   * **Options :**
     * **Égal (=) :** Vérifie si la valeur combinée du prix unitaire et du champ correspond à la valeur spécifiée.
     * **Non égal (≠) :** Garantit que la valeur combinée du prix unitaire et du champ est différente de la valeur spécifiée.
     * **Supérieur à (>) :** Vérifie si la valeur combinée du prix unitaire et du champ dépasse la valeur spécifiée.
     * **Supérieur ou égal (≥) :** Vérifie si la valeur combinée du prix unitaire et du champ est supérieure ou égale à la valeur spécifiée.
     * **Inférieur à (<) :** Vérifie si la valeur combinée du prix unitaire et du champ est inférieure à la valeur spécifiée.
     * **Inférieur ou égal (≤) :** Vérifie si la valeur combinée du prix unitaire et du champ est inférieure ou égale à la valeur spécifiée.
3. **Valeur :**
   * **Description :** Spécifie la valeur à laquelle la valeur combinée du prix unitaire et du champ sera comparée.
   * **Détail :** Cette valeur numérique représente le seuil de comparaison. Si la valeur combinée du prix unitaire et du champ dépasse ou est inférieure à cette valeur (selon l'opérateur sélectionné), la condition déclenchera les actions spécifiées.

## **Fonctionnalité :**

* **Évaluation de la condition :** Le système calcule la valeur combinée en multipliant ou en ajoutant le prix unitaire à la valeur du champ, selon la configuration. Le résultat est ensuite comparé à la valeur spécifiée à l'aide de l'opérateur sélectionné. Si la condition est remplie (c'est-à-dire que la valeur combinée est hors tolérance), le flux de travail passe à l'étape suivante, qu'il s'agisse d'une approbation, d'un rejet ou d'un examen plus approfondi.
* **Exécution de l'action :**
  * **Condition vraie :** Si la comparaison donne un résultat vrai (c'est-à-dire que la valeur combinée remplit la condition), le flux de travail déclenche l'action associée à la condition vraie (par exemple, approbation ou notification).
  * **Condition fausse :** Si la comparaison donne un résultat faux (c'est-à-dire que la valeur combinée ne remplit pas la condition), le flux de travail ne se poursuivra pas.

## **Configuration et paramétrage :**

* Les utilisateurs sélectionnent le champ qui contient la valeur à combiner avec le prix unitaire. Ensuite, ils choisissent l'opérateur approprié pour déterminer comment la valeur combinée sera comparée à la valeur spécifiée. Enfin, l'utilisateur définit la valeur à laquelle le prix combiné sera comparé.

## **Exemple de scénario :**

* Une facture répertorie 50 unités d'un produit à 30 $ chacune, pour un total de 1 500 $. Le document associé contient un champ de quantité avec une valeur de 10. Le prix combiné est calculé en multipliant le prix unitaire (30 $) et la quantité (10), ce qui donne 300 $. La carte compare ensuite cette valeur combinée à un seuil de 250 $. En utilisant l'opérateur « Supérieur à », la carte identifie que 300 $ est supérieur à 250 $, déclenchant un processus d'approbation pour le document.

## **Conclusion :**

La carte de flux de travail "Prix unitaires hors tolérance combinés aux champs" permet de s'assurer que les prix et les valeurs des champs sont en adéquation avec les règles métier. En automatisant ce contrôle, les organisations peuvent identifier les divergences tôt dans le processus, garantissant que tout prix unitaire hors tolérance est signalé pour examen ou action nécessaire.
