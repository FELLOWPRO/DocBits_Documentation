# Condition de l'utilisateur assigné

<figure><img src="../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513.png" alt=""><figcaption></figcaption></figure>

**Objectif**

Cette carte de workflow gère l'exécution des opérations en fonction de savoir si une tâche ou un document est assigné à un utilisateur particulier ou à un ensemble d'utilisateurs. Elle utilise une logique conditionnelle pour déclencher ou empêcher des actions spécifiques, ce qui la rend idéale pour les workflows nécessitant une gestion spécifique des utilisateurs.

**Composants de la carte**

1. **Opérateur**
* **Description** : Définit la condition logique à appliquer à l'assignation de l'utilisateur.
* **Options** :
* **EST** : Déclenche l'opération si l'utilisateur assigné au document ou à la tâche correspond à un utilisateur de la liste spécifiée.
* **N'EST PAS** : Déclenche l'opération si l'utilisateur assigné au document ou à la tâche ne correspond à aucun utilisateur de la liste spécifiée.
2. **Liste d'utilisateurs**
* **Description** : Une liste ou une sélection d'utilisateurs à comparer avec l'utilisateur assigné.
* **Détail** : Cette liste peut inclure un ou plusieurs utilisateurs, permettant à la carte de gérer efficacement les conditions d'utilisateur unique et multiple. La sélection peut se faire via des cases à cocher, un menu déroulant multi-sélection ou des éléments d'interface utilisateur similaires.

**Fonctionnalités**

* **Identification de l'assignation d'utilisateur** : Identifie automatiquement l'utilisateur ou les utilisateurs assignés à une tâche ou un document particulier dans le système ERP.
* **Évaluation de la condition** :
* En utilisant l'opérateur **EST**, la carte vérifie si l'utilisateur assigné figure parmi ceux répertoriés dans la Liste d'utilisateurs.
* En utilisant l'opérateur **N'EST PAS**, la carte s'assure que l'utilisateur assigné ne figure pas parmi ceux répertoriés.
* **Exécution de l'action** :
* **Condition vraie** : Si l'assignation de l'utilisateur répond à la condition (soit EST soit N'EST PAS), des actions pertinentes sont déclenchées, telles que des notifications, des déclenchements de tâches, des approbations ou d'autres étapes du workflow.
* **Condition fausse** : Si la condition n'est pas remplie, le document ou la tâche peut suivre un cheminement différent, ou des actions alternatives peuvent être spécifiées.

**Interactions utilisateur**

* **Configuration et paramétrage** : Les utilisateurs configurent la carte en sélectionnant un opérateur et en spécifiant les utilisateurs pertinents de la Liste d'utilisateurs. La configuration doit être conviviale et intuitive pour permettre des sélections parmi des bases d'utilisateurs potentiellement importantes.
* **Surveillance et rapports** : Le système ERP doit fournir des fonctionnalités pour surveiller et rapporter sur les opérations déclenchées par cette carte, offrant des informations sur la précision de l'assignation et l'efficacité du processus.
* **Gestion des erreurs et notifications** : Les utilisateurs doivent avoir la possibilité de recevoir des alertes ou des notifications en cas de problèmes avec les assignations, tels que des tâches non assignées ou des erreurs dans la sélection des utilisateurs.

#### Conclusion

La carte de workflow "Condition de l'utilisateur assigné" est un outil essentiel pour gérer les workflows de documents et de tâches qui dépendent des assignations d'utilisateurs. En permettant des conditions basées sur le fait qu'une tâche ou un document est assigné à des utilisateurs spécifiques, elle garantit que les workflows ne sont déclenchés que par des interactions utilisateur appropriées, améliorant à la fois la responsabilité et l'alignement des tâches au sein des équipes. Documenter clairement cette carte aidera les utilisateurs à comprendre sa signification et à l'intégrer efficacement dans leurs workflows, garantissant des opérations fluides et efficaces adaptées aux rôles et responsabilités des utilisateurs.
