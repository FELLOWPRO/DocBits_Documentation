# La case est cochée

<figure><img src="../../../../.gitbook/assets/docbits_workflow_document_field.png" alt="Docbits Workflow Document Field" width="563"><figcaption></figcaption></figure>

## **Objet :**

Cette carte de flux de travail est conçue pour automatiser les actions basées sur l'état (coché ou décoché) d'une case à cocher dans votre système ERP. En évaluant la condition de la case à cocher, elle facilite le déclenchement de processus spécifiques ou l'application de certaines règles au sein de l'application.

## **Composants de la carte :**

* **Nom du champ**
  * **Description :** Spécifie le nom du champ de la case à cocher qui sera évalué.
  * **Détail :** Cela doit correspondre à l'identifiant exact du champ utilisé dans le système. Il détermine l'état de quelle case à cocher est surveillé.
* **Booléen**
  * **Description :** Définit la condition qui déclenche le flux de travail.
  * **Options :**
    * **Vrai :** Le flux de travail se déclenche si la case est cochée.
    * **Faux :** Le flux de travail se déclenche si la case est décochée.

#### **Fonctionnalité :**

* **Détection d'état :** La carte surveille en permanence l'état du champ de case à cocher spécifié.
* **Évaluation de la condition :** Le système vérifie si la case à cocher est dans l'état (coché ou décoché) spécifié par la condition booléenne.
* **Exécution de l'action :**
  * **Condition vraie :**
    Si l'état de la case à cocher correspond à la condition booléenne spécifiée (soit vrai pour coché, soit faux pour décoché), le système lance les actions associées. Celles-ci peuvent inclure l'activation ou la désactivation de champs de formulaire, le déclenchement de notifications, le démarrage de flux de travail ou la mise à jour d'enregistrements.
  * **Condition fausse :**
    Si l'état de la case à cocher ne correspond pas à la condition, des actions alternatives ou aucune action peuvent être entreprises, selon la configuration du flux de travail.

## **Configuration et paramétrage :**

* Les utilisateurs configurent la carte en sélectionnant le champ de la case à cocher dans une liste de champs disponibles et en définissant la condition booléenne.

## Conclusion :

La carte de flux de travail "Condition du champ de case à cocher" est un outil fondamental pour la gestion des formulaires et documents dynamiques au sein d'un système ERP, où les saisies des utilisateurs peuvent dicter les processus de données ultérieurs. En automatisant les actions basées sur l'état d'une case à cocher, cette carte améliore l'efficacité du flux de travail et garantit que les comportements du système s'alignent sur les saisies des utilisateurs. Une documentation claire de cette carte aidera les utilisateurs à l'implémenter efficacement au sein de leurs opérations, permettant un meilleur contrôle sur les comportements des formulaires et les automatisations de processus.


**Remarque : Tous les clients n'ont pas la case à cocher, mais elle peut être ajoutée si vous le souhaitez.**
