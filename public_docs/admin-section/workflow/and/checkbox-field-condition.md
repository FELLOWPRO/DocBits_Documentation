# Condition du champ de case à cocher

<figure><img src="../../../.gitbook/assets/userlmn_b689c7ce31284b4635be85f674a90917.png" alt=""><figcaption></figcaption></figure>

**Objectif**

Cette carte de workflow est conçue pour automatiser des actions en fonction de l'état (coché ou décoché) d'une case à cocher dans votre système ERP. En évaluant la condition de la case à cocher, elle facilite le déclenchement de processus spécifiques ou l'application de certaines règles au sein de l'application.

**Composants de la carte**

1. **Nom du champ**
* **Description** : Spécifie le nom du champ de case à cocher qui sera évalué.
* **Détail** : Cela doit correspondre à l'étiquette exacte du champ ou à l'identifiant utilisé dans le système. Cela détermine l'état de la case à cocher qui est surveillé.
2. **Booléen**
* **Description** : Définit la condition qui déclenche le workflow.
* **Options** :
* **Vrai** : Le workflow se déclenche si la case à cocher est cochée.
* **Faux** : Le workflow se déclenche si la case à cocher est décochée.

**Fonctionnalités**

* **Détection de l'état** : La carte surveille en continu l'état du champ de case à cocher spécifié.
* **Évaluation de la condition** :
* Le système vérifie si la case à cocher est dans l'état (coché ou décoché) spécifié par la condition Booléenne.
* **Exécution de l'action** :
* **Condition Vraie** : Si l'état de la case à cocher correspond à la condition Booléenne spécifiée (vrai pour cochée ou faux pour décochée), le système lance les actions associées. Celles-ci pourraient inclure l'activation ou la désactivation de champs de formulaire, le déclenchement de notifications, le démarrage de workflows ou la mise à jour d'enregistrements.
* **Condition Fausse** : Si l'état de la case à cocher ne correspond pas à la condition, des actions alternatives ou aucune action peuvent être prises, selon la configuration du workflow.

**Interactions Utilisateur**

* **Configuration et Paramétrage** : Les utilisateurs configurent la carte en sélectionnant le champ de case à cocher dans une liste de champs disponibles et en définissant la condition Booléenne. Ce processus de configuration devrait être intuitif, impliquant généralement un simple menu déroulant pour la sélection du champ et un interrupteur pour la condition Booléenne.
* **Surveillance et Rapports** : Fournit des fonctionnalités aux utilisateurs pour surveiller l'état de cette condition, éventuellement via un tableau de bord montrant des mises à jour en temps réel sur les conditions actives ou déclenchées.
* **Gestion des Erreurs et Notifications** : Veille à ce que les utilisateurs soient notifiés en cas de divergences ou d'erreurs dans le processus de vérification de la condition, telles que des échecs du système à lire l'état de la case à cocher.

#### Conclusion

La carte de workflow "Condition du champ de case à cocher" est un outil fondamental pour gérer des formulaires dynamiques et des documents au sein d'un système ERP, où les entrées des utilisateurs peuvent dicter les processus de données ultérieurs. En automatisant des actions en fonction de l'état d'une case à cocher, cette carte améliore l'efficacité du workflow et garantit que les comportements du système sont alignés sur les entrées des utilisateurs. Une documentation claire de cette carte aidera les utilisateurs à l'implémenter efficacement dans leurs opérations, permettant un meilleur contrôle sur les comportements des formulaires et les automatisations des processus.
