# Compare two Fields

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour automatiser des actions en comparant les valeurs de deux champs de document spécifiés. Elle permet une prise de décision dynamique basée sur les données des champs et garantit que les workflows s'exécutent en fonction des comparaisons entre différentes valeurs de document.

## **Composants de la carte :**

1. **Field Name (1)**
   * **Description :** spécifie le premier champ de document à comparer.
   * **Détail :** il doit correspondre à l'identifiant exact du premier champ dans le document.
2. **Operator**
   * **Description :** définit le type de comparaison à effectuer entre les deux champs.
   * **Options :**
     * **Equals (=) :** vérifie si les valeurs des deux champs sont égales.
     * **Not Equals (≠) :** s'assure que les valeurs des deux champs sont différentes.
     * **Greater Than (>) :** confirme que la valeur du premier champ est supérieure à celle du second champ.
     * **Greater or Equals (≥) :** vérifie que la valeur du premier champ est égale ou supérieure à celle du second champ.
     * **Lesser Than (<) :** vérifie si la valeur du premier champ est inférieure à celle du second champ.
     * **Less or Equals (≤) :** s'assure que la valeur du premier champ est inférieure ou égale à celle du second champ.
3. **Field Name (2)**
   * **Description :** spécifie le second champ de document à comparer au premier champ.
   * **Détail :** il doit correspondre à l'identifiant exact du second champ dans le document.

## **Fonctionnalité :**

**Évaluation de la condition :** le système évalue si les valeurs des deux champs spécifiés satisfont la condition de comparaison définie par l'opérateur.

**Exécution de l'action :**

* **Condition vraie :**\
  Si les valeurs des deux champs correspondent à la condition de comparaison, le système déclenche les actions associées. Celles-ci peuvent inclure la mise à jour d'enregistrements ou le déclenchement d'alertes.
* **Condition fausse :**\
  Si les valeurs des deux champs ne correspondent pas à la condition spécifiée, des actions alternatives ou aucune action peuvent être exécutées, selon la configuration des workflows.

## **Mise en place et configuration :**&#x20;

* Les utilisateurs configurent la carte en sélectionnant les deux champs à comparer dans une liste de champs disponibles dans le système. L'opérateur est sélectionné dans une liste déroulante d'options de comparaison disponibles.

## **Conclusion :**

La carte de workflow « Compare Two Fields » est un outil essentiel pour comparer les données entre champs au sein de documents. En automatisant des actions en fonction des comparaisons de champs, cette carte aide à optimiser la prise de décision, facilite la validation des données et renforce l'automatisation du workflow.
