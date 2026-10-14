# Checkbox is checked

<figure><img src="../../../../.gitbook/assets/image (20) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour automatiser des actions en fonction de l'état (cochée ou décochée) d'une case à cocher dans votre système ERP. En évaluant l'état de la case à cocher, elle facilite le déclenchement de processus spécifiques ou l'application de certaines règles au sein de l'application.

## **Composants de la carte :**

* **Field Name**
  * **Description :** spécifie le nom du champ de type case à cocher qui sera évalué.
  * **Détail :** il doit correspondre à l'identifiant exact du champ utilisé dans le système. Il détermine l'état de quelle case à cocher est surveillé.
* **Boolean**
  * **Description :** définit la condition qui déclenche le workflow.
  * **Options :**
    * **True :** le workflow se déclenche si la case est cochée.
    * **False :** le workflow se déclenche si la case est décochée.

#### **Fonctionnalité :**

* **Détection de l'état :** la carte surveille en continu l'état du champ de case à cocher spécifié.
* **Évaluation de la condition :** le système vérifie si la case à cocher est dans l'état (cochée ou décochée) spécifié par la condition booléenne.
* **Exécution de l'action :**
  * **Condition vraie :**\
    Si l'état de la case à cocher correspond à la condition booléenne spécifiée (true pour cochée ou false pour décochée), le système déclenche les actions associées. Celles-ci peuvent inclure l'activation ou la désactivation de champs de formulaire, le déclenchement de notifications, le démarrage de workflows ou la mise à jour d'enregistrements.
  * **Condition fausse :**\
    Si l'état de la case à cocher ne correspond pas à la condition, des actions alternatives ou aucune action peuvent être effectuées, selon la configuration du workflow.

## **Mise en place et configuration :**

* Les utilisateurs configurent la carte en sélectionnant le champ de case à cocher dans une liste de champs disponibles et en définissant la condition booléenne.&#x20;

## Conclusion :

La carte de workflow « Checkbox Field Condition » est un outil fondamental pour gérer les formulaires et documents dynamiques au sein d'un système ERP, où les saisies de l'utilisateur peuvent dicter les processus de données ultérieurs. En automatisant des actions en fonction de l'état d'une case à cocher, cette carte améliore l'efficacité du workflow et garantit que les comportements du système sont alignés sur les saisies de l'utilisateur. Une documentation claire de cette carte aidera les utilisateurs à la mettre en œuvre efficacement dans leurs opérations, permettant un meilleur contrôle des comportements des formulaires et des automatisations de processus.



**Note : tous les clients ne disposent pas de la case à cocher, mais elle peut être ajoutée si souhaité.**
