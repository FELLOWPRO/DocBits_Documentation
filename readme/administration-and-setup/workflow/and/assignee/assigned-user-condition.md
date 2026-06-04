# Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513 (1).png" alt="" width="552"><figcaption></figcaption></figure>

**Objectif**

Cette carte de workflow gère l'exécution d'opérations selon qu'une tâche ou un document est assigné à un utilisateur particulier ou à un ensemble d'utilisateurs. Elle emploie une logique conditionnelle pour déclencher ou empêcher des actions spécifiques, ce qui la rend idéale pour les workflows nécessitant un traitement propre à un utilisateur.

**Composants de la carte**

1. **Operator**
   * **Description** : définit la condition logique à appliquer à l'attribution d'utilisateur.
   * **Options** :
     * **IS** : déclenche l'opération si l'utilisateur assigné au document ou à la tâche correspond à l'un des utilisateurs de la liste spécifiée.
     * **IS NOT** : déclenche l'opération si l'utilisateur assigné au document ou à la tâche ne correspond à aucun des utilisateurs de la liste spécifiée.
2. **User List**
   * **Description** : une liste ou une sélection d'utilisateurs à comparer à l'utilisateur assigné.
   * **Détail** : cette liste peut inclure un ou plusieurs utilisateurs, permettant à la carte de gérer efficacement les conditions à un seul utilisateur comme à plusieurs utilisateurs. La sélection peut se faire au moyen de cases à cocher, d'une liste déroulante à sélection multiple ou d'éléments d'interface similaires.

**Fonctionnalité**

* **Identification de l'attribution d'utilisateur** : identifie automatiquement le ou les utilisateurs assignés à une tâche ou à un document particulier dans le système ERP.
* **Évaluation de la condition** :
  * Avec l'opérateur **IS**, la carte vérifie si l'utilisateur assigné fait partie de ceux répertoriés dans la User List.
  * Avec l'opérateur **IS NOT**, la carte s'assure que l'utilisateur assigné ne fait pas partie de ceux répertoriés.
* **Exécution de l'action** :
  * **Condition vraie** : si l'attribution d'utilisateur satisfait la condition (IS ou IS NOT), les actions pertinentes sont déclenchées, telles que des notifications, le lancement de tâches, des approbations ou d'autres étapes du workflow.
  * **Condition fausse** : si la condition n'est pas remplie, le workflow ne se poursuit pas.

**Interactions utilisateur**

* **Mise en place et configuration** : les utilisateurs configurent la carte en sélectionnant un opérateur et en spécifiant les utilisateurs concernés dans la User List. La configuration doit être conviviale et intuitive pour permettre des sélections à partir de bases d'utilisateurs potentiellement étendues.
* **Surveillance et reporting** : le système ERP doit offrir la possibilité de surveiller et de rendre compte des opérations déclenchées par cette carte, donnant un aperçu de l'exactitude des attributions et de l'efficacité des processus.
* **Gestion des erreurs et notifications** : les utilisateurs doivent avoir la possibilité de recevoir des alertes ou des notifications en cas de problème d'attribution, comme des tâches non assignées ou des erreurs de sélection d'utilisateur.

#### Conclusion

La carte de workflow « Assigned User Condition » est un outil essentiel pour gérer les workflows de documents et de tâches qui dépendent d'attributions d'utilisateurs. En autorisant des conditions basées sur l'attribution ou non d'une tâche ou d'un document à des utilisateurs spécifiques, elle garantit que les workflows ne sont déclenchés que par les interactions utilisateur appropriées, renforçant à la fois la responsabilité et l'alignement des tâches au sein des équipes. Documenter clairement cette carte aidera les utilisateurs à comprendre son importance et à l'intégrer efficacement dans leurs workflows, garantissant des opérations fluides et efficaces, adaptées aux rôles et responsabilités des utilisateurs.
