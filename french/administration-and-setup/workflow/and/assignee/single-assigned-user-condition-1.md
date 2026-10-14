# Single Assigned User Condition

<figure><img src="../../../../.gitbook/assets/image (16) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Objectif :**\
Cette carte de workflow exécute des opérations selon qu'une tâche ou un document est assigné à un groupe particulier. Elle utilise une condition simple pour déclencher ou empêcher des actions en fonction de l'attribution de groupe.

**Composants de la carte :**

1. **Operator**
   * **Description :** définit la condition logique à appliquer à l'attribution de groupe.
   * **Options :**
     * **IS :** déclenche l'opération si le groupe assigné au document ou à la tâche correspond au groupe spécifié.
     * **IS NOT :** déclenche l'opération si le groupe assigné au document ou à la tâche ne correspond pas au groupe spécifié.
2. **Group**
   * **Description :** spécifie le groupe à comparer au groupe assigné.
   * **Détail :** ce champ vous permet de sélectionner un seul groupe pour comparer l'attribution.

**Fonctionnalité :**

* **Identification de l'attribution de groupe :** identifie automatiquement le groupe assigné à une tâche ou à un document particulier.
* **Évaluation de la condition :**
  * Avec l'opérateur **IS**, la carte vérifie si le groupe assigné correspond au groupe spécifié.
  * Avec l'opérateur **IS NOT**, la carte s'assure que le groupe assigné ne correspond pas au groupe spécifié.
* **Exécution de l'action :**
  * **Condition vraie :** si l'attribution de groupe satisfait la condition (**IS** ou **IS NOT**), les actions pertinentes sont déclenchées, telles que des notifications, le lancement de tâches, des approbations ou d'autres étapes du workflow.
  * **Condition fausse :** si la condition n'est pas remplie, le document ou la tâche peut suivre un routage différent, ou des actions alternatives peuvent être spécifiées.

**Interactions utilisateur :**

* **Mise en place et configuration :**\
  Les utilisateurs configurent la carte en sélectionnant un opérateur et en spécifiant le groupe concerné. La configuration doit être simple et intuitive.
* **Surveillance et reporting :**\
  Le système doit offrir la possibilité de surveiller et de rendre compte des opérations déclenchées par cette carte, donnant un aperçu de l'exactitude des attributions et de l'efficacité des processus.
* **Gestion des erreurs et notifications :**\
  Les utilisateurs doivent avoir la possibilité de recevoir des alertes ou des notifications en cas de problème d'attribution, comme des tâches non assignées ou des erreurs de sélection de groupe.

**Conclusion :**\
La carte de workflow « Assigned Group Condition » est essentielle pour gérer les workflows de documents et de tâches basés sur des attributions de groupe. En autorisant des conditions basées sur l'attribution ou non d'une tâche ou d'un document à un groupe spécifique, elle garantit que les workflows ne sont déclenchés que par les interactions de groupe appropriées, améliorant la gestion des tâches et l'efficacité du workflow.
