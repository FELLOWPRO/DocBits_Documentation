# Condition sur un groupe assigné unique

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-d12f96578747-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

**Objectif :**\
Cette carte de workflow exécute des opérations selon qu'une tâche ou un document est assigné à un groupe particulier. Elle utilise une condition simple pour déclencher ou empêcher des actions en fonction de l'attribution de groupe.

**Composants de la carte :**

1. **Opérateur**
   * **Descriptif :** définit la condition logique à appliquer à l'attribution de groupe.
   * **Possibilités :**
     * **IS :** déclenche l'opération si le groupe assigné au document ou à la tâche correspond au groupe spécifié.
     * **N'EST PAS :** déclenche l'opération si le groupe assigné au document ou à la tâche ne correspond pas au groupe spécifié.
2. **Groupe**
   * **Descriptif :** spécifie le groupe à comparer au groupe assigné.
   * **Détail :** ce champ vous permet de sélectionner un seul groupe pour comparer l'attribution.

**Fonctionnalité :**

* **Identification de l'attribution de groupe :** identifie automatiquement le groupe assigné à une tâche ou à un document particulier.
* **Évaluation de la condition :**
  * Avec l'opérateur **IS**, la carte vérifie si le groupe assigné correspond au groupe spécifié.
  * Avec l'opérateur **N'EST PAS**, la carte s'assure que le groupe assigné ne correspond pas au groupe spécifié.
* **Exécution de l'action :**
  * **Condition vraie :** si l'attribution de groupe satisfait la condition (**IS** ou **N'EST PAS**), les actions pertinentes sont déclenchées, telles que des notifications, le lancement de tâches, des approbations ou d'autres étapes du workflow.
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

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Appliquer une règle à la file d'attente de révision financière.

**Configuration :** Sélectionnez l'opérateur égal et le groupe `Demo Finance`.

**Résultat attendu et contre-exemple :** Un document attribué à `Demo Finance` est réussi. L'attribution à un utilisateur individuel n'établit pas à elle seule l'appartenance à ce groupe d'attribution de documents sélectionné.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
