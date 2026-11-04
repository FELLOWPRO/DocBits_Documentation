# Condition d'Utilisateur Unique Assigné

<figure><img src="../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50.png" alt=""><figcaption></figcaption></figure>

**Objectif**

Cette carte de workflow facilite les opérations basées sur l'assignation d'une tâche ou d'un document à un utilisateur spécifique unique. En utilisant une approche logique conditionnelle directe, elle gère les workflows nécessitant l'engagement ciblé de l'utilisateur, assurant ainsi une précision dans la gestion des tâches basées sur l'utilisateur.

**Composants de la Carte**

1. **Opérateur**
* **Description** : Spécifie la logique à appliquer à l'assignation de l'utilisateur.
* **Options** :
* **EST** : Déclenche l'opération si l'utilisateur assigné du document ou de la tâche correspond à l'utilisateur spécifié.
* **N'EST PAS** : Déclenche l'opération si l'utilisateur assigné ne correspond pas à l'utilisateur spécifié.
2. **Utilisateur**
* **Description** : Permet la sélection d'un seul utilisateur par rapport auquel l'utilisateur assigné sera comparé.
* **Détail** : Il s'agit d'un simple menu déroulant ou champ d'autocomplétion où un utilisateur peut être sélectionné à la fois.

**Fonctionnalité**

* **Identification de l'Assignation de l'Utilisateur** : Identifie l'utilisateur actuellement assigné à une tâche ou un document spécifique.
* **Évaluation de la Condition** :
* Pour l'opérateur **EST**, la carte vérifie si l'utilisateur assigné est le même que l'utilisateur sélectionné.
* Pour l'opérateur **N'EST PAS**, elle vérifie que l'utilisateur assigné est différent de l'utilisateur sélectionné.
* **Exécution de l'Action** :
* **Condition Vraie** : Si l'assignation répond à la condition définie (EST ou N'EST PAS), cela déclenche des actions prédéfinies, qui pourraient inclure la progression des approbations, le lancement de tâches supplémentaires, l'envoi de notifications ou d'autres workflows connexes.
* **Condition Fausse** : Si la condition échoue, le système peut réorienter la tâche, la mettre en attente pour révision, ou déclencher d'autres actions prédéfinies alternatives.

**Interactions Utilisateur**

* **Configuration et Configuration** : Les utilisateurs configurent la carte en choisissant un opérateur et en sélectionnant un utilisateur dans le champ utilisateur. Cette configuration devrait être simple, garantissant une sélection et une configuration faciles pour l'utilisateur.
* **Surveillance et Rapports** : Offre des outils pour surveiller les performances de la carte, comme le suivi des tâches déclenchées par des assignations d'utilisateurs spécifiques et les résultats de ces déclenchements.
* **Gestion des Erreurs et Notifications** : Fournit des mécanismes pour alerter les utilisateurs si les tâches sont incorrectement assignées ou si des erreurs opérationnelles surviennent en raison de problèmes d'assignation.

#### Conclusion

La carte de workflow "Condition d'Utilisateur Unique Assigné" est essentielle pour la gestion précise des documents et tâches spécifiques à un utilisateur au sein d'un système ERP. Elle simplifie les workflows en se concentrant sur les assignations individuelles d'utilisateurs, garantissant ainsi que les actions ne sont exécutées que lorsque c'est approprié, en fonction du rôle et des responsabilités de l'utilisateur. Documenter clairement cette carte aidera les utilisateurs à comprendre son application, leur permettant de l'implémenter et de la gérer efficacement dans leurs opérations quotidiennes. Cette documentation garantit que tous les utilisateurs potentiels peuvent facilement saisir le but de la carte et l'intégrer de manière transparente dans leurs workflows.
