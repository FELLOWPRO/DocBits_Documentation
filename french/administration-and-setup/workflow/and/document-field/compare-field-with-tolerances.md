# Compare Field with tolerances

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour comparer la valeur d'un champ à une valeur de référence spécifiée tout en autorisant des tolérances. Elle permet un traitement conditionnel précis dans les workflows où de petits écarts sont acceptables, ce qui la rend idéale pour des scénarios tels que l'assurance qualité, l'analyse financière ou les actions basées sur des seuils.

## **Composants de la carte :**

1. **Field Name**
   * **Description :** le champ à évaluer dans la comparaison.
   * **Détail :** il doit correspondre à l'identifiant exact du premier champ dans le document.
2. **Comparison Operator**
   * **Description :** spécifie comment la valeur du champ sélectionné sera comparée à la valeur de référence.
   * **Options :**
     * **Equals (=) :** vérifie si la valeur du champ correspond exactement à la valeur de référence.
     * **Not Equals (≠) :** vérifie si la valeur du champ ne correspond pas à la valeur de référence.
     * **Greater Than (>) :** vérifie si la valeur du champ est supérieure à la valeur de référence.
     * **Greater or Equals (≥) :** vérifie si la valeur du champ est supérieure ou égale à la valeur de référence.
     * **Lesser Than (<) :** vérifie si la valeur du champ est inférieure à la valeur de référence.
     * **Lesser or Equals (≤) :** vérifie si la valeur du champ est inférieure ou égale à la valeur de référence.
3. **Reference Value**
   * **Description :** la valeur à laquelle le champ est comparé.
   * **Détail :** cette valeur peut être numérique, textuelle ou de type date, selon le contexte de la comparaison.
4. **Tolerance Amount**
   * **Description :** définit la marge d'erreur acceptable pour la comparaison.
   * **Détail :** le montant de tolérance est une valeur numérique qui indique l'écart maximal autorisé entre les deux valeurs de champ pour que la comparaison soit considérée comme vraie.
5. **Tolerance Type**
   * **Description :** spécifie l'unité de mesure du montant de tolérance.
   * **Options :**
     * **Value :** la tolérance est une valeur absolue, ce qui signifie que les deux champs peuvent différer du montant de tolérance spécifié.
     * **Percent :** la tolérance est calculée en pourcentage de la valeur du second champ, autorisant une marge d'erreur relative.

## **Fonctionnalité :**

* **Évaluation de la condition :** le système évalue la valeur du champ par rapport à la valeur de référence à l'aide de l'opérateur de comparaison sélectionné. Si une tolérance est configurée, le système considère la comparaison réussie si la valeur du champ se situe dans la plage de tolérance définie.
* **Exécution de l'action :**
  * **Dans la tolérance :** si la valeur du champ satisfait la condition dans la tolérance spécifiée, le workflow se poursuit en déclenchant les actions associées.
  * **Hors tolérance :** si la valeur du champ ne satisfait pas la condition ou se situe en dehors de la plage de tolérance, des actions alternatives peuvent être exécutées, comme la journalisation, l'envoi d'alertes ou l'arrêt du workflow.

## **Mise en place et configuration :**

* Les utilisateurs configurent la carte en sélectionnant le champ à évaluer dans une liste de champs disponibles et en choisissant l'opérateur de comparaison (par ex. equals, greater than) dans une liste déroulante. Ils spécifient ensuite la valeur de référence à laquelle comparer et définissent le montant de tolérance, puis sélectionnent le type de tolérance (par ex. percent ou value).&#x20;

## **Conclusion :**

La carte « Field Comparison with Tolerances » est un outil polyvalent pour les workflows nécessitant des évaluations flexibles. En permettant des comparaisons avec tolérances, elle garantit que les workflows restent efficaces et adaptables, tenant compte des variations du monde réel sans compromettre la précision.
