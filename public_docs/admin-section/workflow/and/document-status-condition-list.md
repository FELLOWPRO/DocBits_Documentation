# Liste des conditions d'état du document

<figure><img src="../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605.png" alt=""><figcaption></figcaption></figure>

**Objectif**

Cette carte est conçue pour contrôler les actions du flux de travail en fonction de l'état actuel d'un document, en utilisant une logique conditionnelle pour déclencher ou restreindre certains processus. Elle garantit que les documents ne progressent que dans les flux de travail lorsqu'ils répondent à des critères d'état prédéfinis.

**Composants de la carte**

1. **Opérateur**
* **Description** : Détermine comment l'état du document sera évalué par rapport à une condition spécifiée.
* **Options** :
* **est** : Déclenche les actions associées si l'état actuel du document correspond à l'un des états spécifiés.
* **n'est pas** : Déclenche les actions si l'état du document ne correspond à aucun des états spécifiés.
2. **État (Liste)**
* **Description** : Répertorie les états spécifiques par rapport auxquels l'état actuel du document sera comparé.
* **Exemples** : "Erreur", "Erreur d'exportation", "Prêt à valider", "Prêt à réviser", "Approbation en attente", "Deuxième approbation en attente". Ces états représentent les différentes étapes ou conditions dans lesquelles un document peut se trouver dans un processus de flux de travail.

**Fonctionnalités**

* **Identification de l'état** : Identifie automatiquement l'état actuel d'un document lors de son passage à travers le flux de travail du système ERP.
* **Évaluation de la condition** : Applique l'opérateur choisi (est ou n'est pas) à l'état du document par rapport aux états répertoriés :
* Si **est**, vérifie si l'état du document correspond à l'un des états de la liste.
* Si **n'est pas**, vérifie si l'état du document n'apparaît pas dans la liste.
* **Exécution de l'action** : En fonction du résultat de l'évaluation de la condition :
* **Vrai** : Exécute des actions prédéfinies ou des flux de travail si la condition est remplie.
* **Faux** : Passe ou déclenche des flux de travail alternatifs si la condition n'est pas remplie.
* **Intégration au flux de travail** : S'intègre parfaitement avec d'autres composants du flux de travail, garantissant que la gestion des documents est coordonnée dans l'ensemble du système.

**Interactions utilisateur**

* **Configuration et paramétrage** : Les utilisateurs configurent la carte en sélectionnant l'opérateur et en spécifiant les états pertinents. Cette configuration peut impliquer des menus déroulants simples ou des cases à cocher pour sélectionner les états et les opérateurs.
* **Surveillance et gestion** : Les utilisateurs peuvent suivre l'activité de la carte via un tableau de bord, qui fournit des informations sur les conditions d'état surveillées et les actions prises en fonction de ces conditions.
* **Gestion des erreurs et alertes** : Prise en charge de la configuration d'alertes pour les échecs de processus ou les incohérences dans les états de document attendus, permettant des réponses rapides aux problèmes opérationnels.

#### Conclusion

La carte de flux de travail "Condition d'état du document" est essentielle pour garantir que les documents sont traités correctement en fonction de leur état actuel, améliorant le contrôle et l'efficacité au sein du système ERP. Documenter clairement cette carte dans le manuel du système aidera les utilisateurs à implémenter et à gérer efficacement, en tirant parti de sa fonctionnalité pour maintenir des flux de travail de documents fluides et conformes. Cette carte est particulièrement utile pour gérer les cycles de vie des documents et garantir que seuls les documents répondant à des critères spécifiques avancent aux étapes suivantes des processus métier.
