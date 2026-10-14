# Compare two Fields with Tolerance

<figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour automatiser des actions en comparant les valeurs de deux champs de document spécifiés, avec la possibilité supplémentaire d'appliquer une valeur de tolérance. Cette fonctionnalité permet au système de tenir compte d'une marge d'erreur (tolérance) lors de la comparaison des valeurs de champs, autorisant une prise de décision plus flexible au sein des workflows.

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
   * **Détail :** il doit correspondre à l'identifiant exact du second champ dans le document.&#x20;
4. **Tolerance Amount**
   * **Description :** définit la marge d'erreur acceptable pour la comparaison.
   * **Détail :** le montant de tolérance est une valeur numérique qui indique l'écart maximal autorisé entre les deux valeurs de champ pour que la comparaison soit considérée comme vraie.
5. **Tolerance Type**
   * **Description :** spécifie l'unité de mesure du montant de tolérance.
   * **Options :**
     * **Value :** la tolérance est une valeur absolue, ce qui signifie que les deux champs peuvent différer du montant de tolérance spécifié.
     * **Percent :** la tolérance est calculée en pourcentage de la valeur du second champ, autorisant une marge d'erreur relative.

## **Fonctionnalité :**

* **Évaluation de la condition :** le système évalue si les valeurs des deux champs spécifiés satisfont la condition de comparaison, en tenant compte de la tolérance définie. Si l'écart absolu ou relatif entre les deux champs se situe dans la tolérance, la condition est considérée comme vraie.
* **Exécution de l'action :**
  * **Condition vraie :**\
    Si les valeurs des deux champs, après prise en compte de la tolérance, correspondent à la condition de comparaison, le système déclenche les actions associées. Celles-ci peuvent inclure la progression du workflow, la mise à jour d'enregistrements, le déclenchement d'alertes ou l'activation de certaines opérations.
  * **Condition fausse :**\
    Si les valeurs des deux champs, après prise en compte de la tolérance, ne correspondent pas à la condition spécifiée, des actions alternatives ou aucune action peuvent être exécutées, selon la configuration du workflow.

## **Mise en place et configuration :**

* Les utilisateurs configurent la carte en sélectionnant les deux champs à comparer dans une liste de champs disponibles dans le système. L'opérateur est sélectionné dans une liste déroulante d'options de comparaison disponibles. Les utilisateurs saisissent le montant de tolérance et choisissent le type de tolérance (value ou percent).&#x20;

## **Conclusion :**

La carte de workflow « Compare Two Fields with Tolerance » est un outil puissant pour comparer des champs de document tout en tenant compte des écarts admissibles dans les données. En appliquant une tolérance aux comparaisons de champs, cette carte apporte de la flexibilité au workflow, lui permettant de gérer les variations de données du monde réel. Elle améliore la prise de décision, facilite la validation des données et renforce l'automatisation globale du workflow.
