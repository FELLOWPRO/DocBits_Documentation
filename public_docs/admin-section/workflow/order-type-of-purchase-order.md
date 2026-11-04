# Type de commande du bon de commande

<figure><img src="../../../../.gitbook/assets/image (277).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objet :**

Cette carte de flux de travail est conçue pour comparer le type de commande d'un bon de commande à une valeur spécifiée. La carte vérifie si le type de commande du bon de commande remplit la condition spécifiée (par exemple, s'il est égal, n'est pas égal, est supérieur à, ou remplit une autre condition) afin de s'assurer que le bon de commande est classé correctement. Cette comparaison peut déclencher des actions basées sur des conditions spécifiques, comme l'envoi de la commande pour un examen plus approfondi ou une approbation si des divergences sont constatées.

## **Composants de la carte :**

1. **N'importe quel / Tous (Any / All) :**
   * **Description :** Définit si la condition s'applique à n'importe lequel ou à tous les bons de commande en cours d'évaluation dans le flux de travail.
   * **Options :**
     * **N'importe quel (Any) :** La condition est remplie si l'un des bons de commande correspond à la condition spécifiée.
     * **Tous (All) :** La condition n'est remplie que si tous les bons de commande remplissent la condition spécifiée.
2. **Opérateur :**
   * **Description :** Définit la condition qui sera appliquée pour comparer le type de commande à une valeur spécifiée.
   * **Options :**
     * **Égal (=) :** Vérifie si le type de commande correspond à la valeur spécifiée.
     * **Non égal (≠) :** Garantit que le type de commande est différent de la valeur spécifiée.
3. **Type de commande :**
   * **Description :** Spécifie la valeur à laquelle le type de commande du bon de commande sera comparé.
   * **Détail :** La valeur doit correspondre au type de commande ou à la classification dans le système.

## **Fonctionnalité :**

* **Évaluation de la condition :** Le système évalue le type de commande du bon de commande par rapport à la condition spécifiée à l'aide de l'opérateur sélectionné. Si le type de commande correspond (ou ne correspond pas) à la valeur spécifiée, le flux de travail se poursuit en conséquence.
* **Exécution de l'action :**
  * **Condition vraie :** Si la condition est évaluée comme vraie (par exemple, le type de commande correspond à la valeur spécifiée), le flux de travail continuera, déclenchant éventuellement des actions ou des étapes de traitement supplémentaires.
  * **Condition fausse :** Si la condition est évaluée comme fausse (par exemple, le type de commande ne correspond pas à la valeur spécifiée), le flux de travail ne continuera pas.

## **Configuration et paramétrage :**

* Les utilisateurs configurent la carte en sélectionnant le champ du type de commande du bon de commande et en choisissant l'opérateur qui définit comment le type de commande sera comparé. Ensuite, ils définissent la valeur spécifiée et décident d'appliquer la condition à n'importe laquelle ou à toutes les lignes du bon de commande.

## **Exemple de scénario :**

* Un bon de commande a pour type de commande "Standard". Le flux de travail est configuré pour vérifier si le type de commande est "Urgent". En utilisant l'opérateur "Égal", la carte compare le type de commande et constate qu'il ne correspond pas à la valeur spécifiée, déclenchant le flux de travail pour envoyer la commande pour examen en raison de la discordance.

## **Conclusion :**

La carte de flux de travail "Type de commande du bon de commande" garantit que les bons de commande sont classés correctement selon leur type de commande spécifié. En automatisant la comparaison des types de commande, les organisations peuvent s'assurer que les bons de commande sont traités conformément à leurs classifications attendues, ce qui aide à faire respecter la conformité et à simplifier les flux de travail d'achat.
