# Single Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50 (1).png" alt="" width="552"><figcaption></figcaption></figure>

**Objectif**

Cette carte de workflow facilite les opérations fondées sur l'attribution d'une tâche ou d'un document à un seul utilisateur précis. Au moyen d'une approche de logique conditionnelle directe, elle gère les workflows qui nécessitent un engagement ciblé d'un utilisateur, garantissant la précision dans le traitement des tâches basées sur l'utilisateur.

**Composants de la carte**

1. **Operator**
   * **Description** : spécifie la logique à appliquer à l'attribution d'utilisateur.
   * **Options** :
     * **IS** : déclenche l'opération si l'utilisateur assigné au document ou à la tâche correspond à l'utilisateur spécifié.
     * **IS NOT** : déclenche l'opération si l'utilisateur assigné ne correspond pas à l'utilisateur spécifié.
2. **User**
   * **Description** : permet de sélectionner un seul utilisateur auquel l'utilisateur assigné sera comparé.
   * **Détail** : cela implique un simple menu déroulant ou un champ d'autocomplétion où un seul utilisateur peut être sélectionné à la fois.

**Fonctionnalité**

* **Identification de l'attribution d'utilisateur** : identifie l'utilisateur actuellement assigné à une tâche ou à un document spécifique.
* **Évaluation de la condition** :
  * Pour l'opérateur **IS**, la carte vérifie si l'utilisateur assigné est le même que l'utilisateur sélectionné.
  * Pour l'opérateur **IS NOT**, elle vérifie que l'utilisateur assigné est différent de l'utilisateur sélectionné.
* **Exécution de l'action** :
  * **Condition vraie** : si l'attribution satisfait la condition définie (IS ou IS NOT), elle déclenche des actions prédéfinies, qui peuvent inclure la poursuite des approbations, le lancement de tâches supplémentaires, l'envoi de notifications ou d'autres workflows associés.
  * **Condition fausse** : si la condition n'est pas remplie, le workflow ne se poursuit pas.

**Interactions utilisateur**

* **Mise en place et configuration** : les utilisateurs configurent la carte en choisissant un opérateur et en sélectionnant un utilisateur dans le champ utilisateur. Cette configuration doit être simple, garantissant une sélection et une configuration faciles de l'utilisateur.
* **Surveillance et reporting** : offre des outils pour surveiller les performances de la carte, comme le suivi des tâches déclenchées par des attributions d'utilisateurs spécifiques et de leurs résultats.
* **Gestion des erreurs et notifications** : fournit des mécanismes pour alerter les utilisateurs si des tâches sont mal assignées ou si des erreurs opérationnelles surviennent en raison de problèmes d'attribution.

#### Conclusion

La carte de workflow « Single Assigned User Condition » est essentielle pour une gestion précise et propre à l'utilisateur des documents et des tâches au sein d'un système ERP. Elle simplifie les workflows en se concentrant sur les attributions d'utilisateurs individuels, garantissant ainsi que les actions ne sont exécutées que lorsque cela est approprié, en fonction du rôle et des responsabilités de l'utilisateur. Documenter clairement cette carte aidera les utilisateurs à comprendre son application, leur permettant de la mettre en œuvre et de la gérer efficacement dans leurs opérations quotidiennes. Cette documentation garantit que tous les utilisateurs potentiels peuvent facilement saisir l'objectif de la carte et l'intégrer en toute fluidité dans leurs workflows.
