# Comparer le champ avec des tolérances

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objet :**

Cette carte de flux de travail est conçue pour comparer la valeur d'un champ à une valeur de référence spécifiée tout en autorisant des tolérances. Elle permet un traitement conditionnel précis dans les flux de travail où de légers écarts sont acceptables, ce qui la rend idéale pour des scénarios tels que l'assurance qualité, l'analyse financière ou les actions basées sur des seuils.

## **Composants de la carte :**

1. **Nom du champ**
   * **Description :** Le champ à évaluer lors de la comparaison.
   * **Détail :** Cela doit correspondre à l'identifiant exact du premier champ dans le document.
2. **Opérateur de comparaison**
   * **Description :** Spécifie comment la valeur du champ sélectionné sera comparée à la valeur de référence.
   * **Options :**
     * **Égal (=) :** Vérifie si la valeur du champ correspond exactement à la valeur de référence.
     * **Non égal (≠) :** Vérifie si la valeur du champ ne correspond pas à la valeur de référence.
     * **Supérieur à (>) :** Vérifie si la valeur du champ est supérieure à la valeur de référence.
     * **Supérieur ou égal (≥) :** Vérifie si la valeur du champ est supérieure ou égale à la valeur de référence.
     * **Inférieur à (<) :** Vérifie si la valeur du champ est inférieure à la valeur de référence.
     * **Inférieur ou égal (≤) :** Vérifie si la valeur du champ est inférieure ou égale à la valeur de référence.
3. **Valeur de référence**
   * **Description :** La valeur à laquelle le champ est comparé.
   * **Détail :** Cette valeur peut être numérique, textuelle ou basée sur une date, selon le contexte de la comparaison.
4. **Montant de la tolérance**
   * **Description :** Définit la marge d'erreur acceptable pour la comparaison.
   * **Détail :** Le montant de la tolérance est une valeur numérique qui indique la différence maximale autorisée entre les deux valeurs de champ pour que la comparaison soit considérée comme vraie.
5. **Type de tolérance**
   * **Description :** Spécifie l'unité de mesure pour le montant de la tolérance.
   * **Options :**
     * **Valeur :** La tolérance est une valeur absolue, ce qui signifie que les deux champs peuvent différer du montant de tolérance spécifié.
     * **Pourcentage :** La tolérance est calculée comme un pourcentage de la deuxième valeur du champ, ce qui permet une marge d'erreur relative.

## **Fonctionnalité :**

* **Évaluation de la condition :** Le système évalue la valeur du champ par rapport à la valeur de référence à l'aide de l'opérateur de comparaison sélectionné. Si une tolérance est configurée, le système considère la comparaison réussie si la valeur du champ se situe dans la plage de tolérance définie.
* **Exécution de l'action :**
  * **Dans la tolérance :** Si la valeur du champ satisfait à la condition dans la tolérance spécifiée, le flux de travail se poursuit, déclenchant les actions associées.
  * **Hors tolérance :** Si la valeur du champ ne remplit pas la condition ou tombe en dehors de la plage de tolérance, des actions alternatives peuvent être exécutées, telles que la journalisation, l'envoi d'alertes ou l'arrêt du flux de travail.

## **Configuration et paramétrage :**

* Les utilisateurs configurent la carte en sélectionnant le champ à évaluer dans une liste de champs disponibles et en choisissant l'opérateur de comparaison (par exemple, égal, supérieur à) dans une liste déroulante. Ils spécifient ensuite la valeur de référence à laquelle comparer et définissent le montant de la tolérance, puis ils sélectionnent le type de tolérance (par exemple, pourcentage ou valeur).&#x20;

## **Conclusion :**

La carte "Comparaison de champs avec tolérances" est un outil polyvalent pour les flux de travail nécessitant des évaluations flexibles. En permettant des comparaisons avec tolérances, elle garantit que les flux de travail restent efficaces et adaptables, en s'accommodant des variations du monde réel sans compromettre l'exactitude.
