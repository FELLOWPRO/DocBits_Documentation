# Document Status Condition List

<figure><img src="../../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605 (1).png" alt="" width="521"><figcaption></figcaption></figure>

**Objectif**

Cette carte est conçue pour contrôler les actions du workflow en fonction du statut actuel d'un document, en utilisant une logique conditionnelle pour déclencher ou restreindre certains processus. Elle garantit que les documents ne progressent dans les workflows que lorsqu'ils satisfont des critères de statut prédéfinis.

**Composants de la carte**

1. **Operator**
   * **Description** : détermine comment le statut du document sera évalué par rapport à une condition spécifiée.
   * **Options** :
     * **is** : déclenche les actions associées si le statut actuel du document correspond à l'un des statuts spécifiés.
     * **is not** : déclenche les actions si le statut du document ne correspond à aucun des statuts spécifiés.
2. **Status ( List )**
   * **Description** : liste les statuts spécifiques auxquels le statut actuel du document sera comparé.
   * **Exemples** : « Error », « Export Error », « Ready in Validation », « Ready in Review », « Pending Approval », « Pending Second Approval ». Ils représentent les différentes étapes ou conditions dans lesquelles un document peut se trouver au sein d'un processus de workflow.

**Fonctionnalité**

* **Identification du statut** : identifie automatiquement le statut actuel d'un document à mesure qu'il progresse dans le workflow du système ERP.
* **Évaluation de la condition** : applique l'opérateur choisi (is ou is not) au statut du document par rapport aux statuts listés :
  * Si **is**, elle vérifie si le statut du document correspond à un statut de la liste.
  * Si **is not**, elle vérifie si le statut du document n'apparaît pas dans la liste.
* **Exécution de l'action** : selon le résultat de l'évaluation de la condition :
  * **True** : exécute des actions ou des workflows prédéfinis si la condition est satisfaite.
  * **False** : ignore ou déclenche des workflows alternatifs si la condition n'est pas satisfaite.
* **Intégration au workflow** : s'intègre en toute fluidité avec les autres composants du workflow, garantissant que le traitement des documents est coordonné dans l'ensemble du système.

**Interactions utilisateur**

* **Mise en place et configuration** : les utilisateurs configurent la carte en sélectionnant l'opérateur et en spécifiant les statuts concernés. Cette configuration peut faire appel à de simples menus déroulants ou cases à cocher pour sélectionner les statuts et les opérateurs.
* **Surveillance et gestion** : les utilisateurs peuvent suivre l'activité de la carte via un tableau de bord, qui donne un aperçu des conditions de statut surveillées et des actions effectuées en fonction de ces conditions.
* **Gestion des erreurs et alertes** : permet de configurer des alertes en cas d'échecs de processus ou d'incohérences dans les statuts de document attendus, permettant des réponses rapides aux problèmes opérationnels.

#### Conclusion

La carte de workflow « Document Status Condition » est essentielle pour garantir que les documents sont traités correctement selon leur statut actuel, renforçant le contrôle et l'efficacité au sein du système ERP. Documenter clairement cette carte dans le manuel du système aidera les utilisateurs à la mettre en œuvre et à la gérer efficacement, en exploitant sa fonctionnalité pour maintenir des workflows documentaires fluides et conformes. Cette carte est particulièrement utile pour gérer les cycles de vie des documents et garantir que seuls les documents satisfaisant des critères spécifiques passent aux étapes suivantes des processus métier.
