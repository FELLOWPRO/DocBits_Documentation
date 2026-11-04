# Comparer deux champs avec tolérance

<figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objet :**

Cette carte de flux de travail est conçue pour automatiser des actions en comparant les valeurs de deux champs de document spécifiés, avec la possibilité supplémentaire d'appliquer une valeur de tolérance. Cette fonction permet au système de prendre en compte une marge d'erreur (tolérance) lors de la comparaison des valeurs de champs, permettant ainsi une prise de décision plus flexible au sein des flux de travail.

## **Composants de la carte :**

1. **Nom du champ (1)**
   * **Description :** Spécifie le premier champ du document à comparer.
   * **Détail :** Cela doit correspondre à l'identifiant exact du premier champ dans le document.
2. **Opérateur**
   * **Description :** Définit le type de comparaison à effectuer entre les deux champs.
   * **Options :**
     * **Égal (=) :** Vérifie si les valeurs des deux champs sont égales.
     * **Non égal (≠) :** Garantit que les valeurs des deux champs sont différentes.
     * **Supérieur à (>) :** Confirme que la valeur du premier champ est supérieure à celle du second.
     * **Supérieur ou égal (≥) :** Valide que la valeur du premier champ est supérieure ou égale à celle du second.
     * **Inférieur à (<) :** Vérifie si la valeur du premier champ est inférieure à celle du second.
     * **Inférieur ou égal (≤) :** Garantit que la valeur du premier champ est inférieure ou égale à celle du second.
3. **Nom du champ (2)**
   * **Description :** Spécifie le second champ du document à comparer au premier.
   * **Détail :** Cela doit correspondre à l'identifiant exact du second champ dans le document.
4. **Montant de la tolérance**
   * **Description :** Définit la marge d'erreur acceptable pour la comparaison.
   * **Détail :** Le montant de la tolérance est une valeur numérique qui indique la différence maximale autorisée entre les deux valeurs de champ pour que la comparaison soit considérée comme vraie.
5. **Type de tolérance**
   * **Description :** Spécifie l'unité de mesure pour le montant de la tolérance.
   * **Options :**
     * **Valeur :** La tolérance est une valeur absolue, ce qui signifie que les deux champs peuvent différer du montant de tolérance spécifié.
     * **Pourcentage :** La tolérance est calculée comme un pourcentage de la deuxième valeur du champ, ce qui permet une marge d'erreur relative.

## **Fonctionnalité :**

* **Évaluation de la condition :** Le système évalue si les valeurs des deux champs spécifiés satisfont à la condition de comparaison, en tenant compte de la tolérance définie. Si la différence absolue ou relative entre les deux champs se situe dans la plage de tolérance, la condition est considérée comme vraie.
* **Exécution de l'action :**
  * **Condition vraie :**
    Si les valeurs des deux champs, après prise en compte de la tolérance, correspondent à la condition de comparaison, le système lance les actions associées. Ces actions peuvent inclure la progression du flux de travail, la mise à jour d'enregistrements, le déclenchement d'alertes ou l'activation de certaines opérations.
  * **Condition fausse :**
    Si les valeurs des deux champs, après prise en compte de la tolérance, ne correspondent pas à la condition spécifiée, des actions alternatives ou aucune action peuvent être exécutées, selon la configuration du flux de travail.

## **Configuration et paramétrage :**

* Les utilisateurs configurent la carte en sélectionnant les deux champs à comparer dans une liste de champs disponibles dans le système. L'opérateur est sélectionné dans une liste déroulante des options de comparaison disponibles. Les utilisateurs saisissent le montant de la tolérance et choisissent le type de tolérance (valeur ou pourcentage).

## **Conclusion :**

La carte de flux de travail "Comparer deux champs avec tolérance" est un outil puissant pour comparer des champs de document tout en tenant compte des écarts autorisés dans les données. En appliquant une tolérance aux comparaisons de champs, cette carte ajoute de la flexibilité au flux de travail, lui permettant de gérer les variations de données du monde réel. Elle améliore la prise de décision, prend en charge la validation des données et renforce l'automatisation globale du flux de travail.
