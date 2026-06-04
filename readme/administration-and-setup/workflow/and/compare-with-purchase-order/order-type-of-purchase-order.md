# Order Type of Purchase Order

<figure><img src="../../../../.gitbook/assets/image (277).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour comparer le type de commande d'un bon de commande à une valeur spécifiée. La carte vérifie si le type de commande du bon de commande satisfait la condition spécifiée (par ex. égal, différent, supérieur, ou une autre condition) afin de garantir que le bon de commande est classé correctement. Cette comparaison peut déclencher des actions selon des conditions spécifiques, comme acheminer la commande vers un examen ou une approbation complémentaire si des écarts sont détectés.

## **Composants de la carte :**

1. **Any/All :**
   * **Description** : définit si la condition s'applique à un ou à tous les bons de commande évalués dans le workflow.
   * **Options** :
     * **Any** : la condition est satisfaite si l'un des bons de commande correspond à la condition spécifiée.
     * **All** : la condition n'est satisfaite que si tous les bons de commande satisfont la condition spécifiée.
2. **Operator :**
   * **Description** : définit la condition qui sera appliquée pour comparer le type de commande à une valeur spécifiée.
   * **Options** :
     * **Equals (=)** : vérifie si le type de commande correspond à la valeur spécifiée.
     * **Not Equals (≠)** : s'assure que le type de commande diffère de la valeur spécifiée.
3. **Order Type :**
   * **Description** : spécifie la valeur à laquelle le type de commande du bon de commande sera comparé.
   * **Détail** : la valeur doit correspondre au type de commande ou à la classification dans le système.

## **Fonctionnalité :**

* **Évaluation de la condition :** le système évalue le type de commande du bon de commande par rapport à la condition spécifiée à l'aide de l'opérateur sélectionné. Si le type de commande correspond (ou ne correspond pas) à la valeur spécifiée, le workflow se poursuit en conséquence.
* **Exécution de l'action :**
  * **Condition vraie** : si la condition est évaluée comme vraie (par ex. le type de commande correspond à la valeur spécifiée), le workflow se poursuit, déclenchant éventuellement des actions ou des étapes de traitement supplémentaires.
  * **Condition fausse** : si la condition est évaluée comme fausse (par ex. le type de commande ne correspond pas à la valeur spécifiée), le workflow ne se poursuit pas.

## **Mise en place et configuration :**

* Les utilisateurs configurent la carte en sélectionnant le champ de type de commande du bon de commande et en choisissant l'opérateur qui définit comment le type de commande sera comparé. Ils définissent ensuite la valeur spécifiée et décident d'appliquer la condition à une ou à toutes les lignes du bon de commande.

## **Scénario d'exemple :**

* Un bon de commande a le type de commande « Standard ». Le workflow est configuré pour vérifier si le type de commande est « Urgent ». À l'aide de l'opérateur « Equals », la carte compare le type de commande et constate qu'il ne correspond pas à la valeur spécifiée, déclenchant l'envoi de la commande pour examen en raison de l'écart.

## **Conclusion :**

La carte de workflow « Order Type of Purchase Order » garantit que les bons de commande sont classés correctement selon leur type de commande spécifié. En automatisant la comparaison des types de commande, les organisations peuvent garantir que les bons de commande sont traités selon leurs classifications attendues, contribuant à faire respecter la conformité et à rationaliser les workflows d'approvisionnement.
