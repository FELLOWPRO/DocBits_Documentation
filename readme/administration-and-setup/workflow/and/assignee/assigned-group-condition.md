# Condition de groupe assignée

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-bdcdca2a5488-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

**Objectif :**

Cette carte de workflow exécute des opérations selon qu'une tâche ou un document est assigné à un groupe particulier ou à un ensemble de groupes. Elle utilise une logique conditionnelle pour déclencher ou empêcher des actions spécifiques en fonction de l'attribution de groupe, ce qui la rend idéale pour les workflows nécessitant un traitement propre à un groupe.

**Composants de la carte :**

1. **Opérateur**
   * **Descriptif :** définit la condition logique à appliquer à l'attribution de groupe.
   * **Possibilités :**
     * **IS :** déclenche l'opération si le groupe assigné au document ou à la tâche correspond à l'un des groupes de la liste spécifiée.
     * **N'EST PAS :** déclenche l'opération si le groupe assigné au document ou à la tâche ne correspond à aucun des groupes de la liste spécifiée.
2. **Liste des groupes**
   * **Descriptif :** une liste ou une sélection de groupes à comparer au groupe assigné.
   * **Détail :** cette liste peut inclure un ou plusieurs groupes, permettant à la carte de gérer efficacement les conditions à un seul groupe comme à plusieurs groupes.

**Fonctionnalité :**

* **Identification de l'attribution de groupe :** identifie automatiquement le ou les groupes assignés à une tâche ou à un document particulier dans le système.
* **Évaluation de la condition :**
  * Avec l'opérateur **IS**, la carte vérifie si le groupe assigné fait partie des groupes répertoriés dans la Groups List.
  * Avec l'opérateur **N'EST PAS**, la carte s'assure que le groupe assigné ne fait pas partie des groupes répertoriés.
* **Exécution de l'action :**
  * **Condition vraie :** si l'attribution de groupe satisfait la condition (**IS** ou **N'EST PAS**), les actions pertinentes sont déclenchées, telles que des notifications, le lancement de tâches, des approbations ou d'autres étapes du workflow.
  * **Condition fausse :** si la condition n'est pas remplie, le workflow ne se poursuit pas.

**Interactions utilisateur :**

* **Mise en place et configuration :** les utilisateurs configurent la carte en sélectionnant un opérateur et en spécifiant les groupes concernés dans la Groups List. La configuration doit être conviviale et intuitive pour permettre des sélections à partir de bases de groupes potentiellement étendues.
* **Surveillance et reporting :**\
  Le système doit offrir la possibilité de surveiller et de rendre compte des opérations déclenchées par cette carte, donnant un aperçu de l'exactitude des attributions et de l'efficacité des processus.
* **Gestion des erreurs et notifications :**\
  Les utilisateurs doivent avoir la possibilité de recevoir des alertes ou des notifications en cas de problème d'attribution, comme des tâches non assignées ou des erreurs de sélection de groupe.

**Conclusion :**\
La carte de workflow « Assigned Group Condition » est essentielle pour gérer les workflows de documents et de tâches qui dépendent d'attributions de groupe. En autorisant des conditions basées sur l'attribution ou non d'une tâche ou d'un document à des groupes spécifiques, elle garantit que les workflows ne sont déclenchés que par les interactions de groupe appropriées, améliorant la responsabilité et la gestion des tâches entre les équipes.

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Appliquez la même règle à deux équipes de révision.

**Configuration :** Sélectionnez l'un des groupes configurés `Demo Finance` et `Demo Procurement`.

**Résultat attendu et contre-exemple :** Un document attribué à l'un ou l'autre des groupes sélectionnés est réussi. Un document attribué uniquement à `Demo Support` échoue.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
