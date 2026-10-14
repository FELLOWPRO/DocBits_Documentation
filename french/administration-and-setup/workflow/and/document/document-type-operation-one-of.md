# Document Type Operation one of

<figure><img src="../../../../.gitbook/assets/userlmn_14ab8ac5e693d9bbe68d178795d12a9f (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte est conçue pour gérer des actions sur les documents en fonction de leur type, en employant une logique conditionnelle simple (is/is not) pour déclencher ou empêcher des workflows spécifiques. Cela permet un contrôle précis de la manière dont les différents types de documents sont traités au sein du système ERP.

## **Composants de la carte :**

1. **Operator**
   * **Description** : détermine la logique conditionnelle appliquée aux types de documents.
   * **Options** :
     * **is** : l'opération se déclenche si le type du document correspond à l'un des types spécifiés dans la liste.
     * **is not** : l'opération se déclenche si le type du document ne correspond à aucun des types listés.
2. **Document Types List**
   * **Description** : spécifie une liste de types de documents auxquels la condition s'appliquera.
   * **Détail** : elle inclut divers types de documents tels que « Invoice », « Purchase Order », etc., en fonction desquels la condition (is/is not) sera évaluée.

## Fonctionnalité :

* **Évaluation de la condition :** le système vérifie si le type de document satisfait la condition de l'opérateur (is ou is not) par rapport à la liste de types de documents spécifiée.
* **Exécution de l'action :**
  * **Condition vraie :**\
    Si le type de document satisfait la condition spécifiée (présent ou non dans la liste), le workflow se poursuit. Cela peut déclencher des processus tels que des approbations de documents, des validations spécifiques ou des actions d'acheminement.
  * **Condition fausse :**\
    Si le type de document ne satisfait pas la condition, des actions alternatives sont exécutées, comme le rejet du document ou l'arrêt du workflow.

## Mise en place et configuration :

* Les utilisateurs configurent la carte en sélectionnant le champ de type de document et en définissant l'opérateur (is ou is not). Ils spécifient ensuite la liste des types de documents à vérifier. La configuration est simple, faisant appel à des menus déroulants pour la sélection du champ et de l'opérateur, ainsi qu'à un champ pour saisir la liste des types de documents.

## Conclusion :

La carte de workflow « Document Type Condition » joue un rôle crucial dans la gestion des opérations basées sur les documents, avec précision et flexibilité. En utilisant une logique conditionnelle simple, elle aide à garantir que les documents sont traités de manière appropriée, améliorant l'efficacité et la conformité. Documenter clairement cette carte aidera les utilisateurs à comprendre comment la mettre en œuvre et l'exploiter efficacement, en faisant un élément précieux de la documentation de votre système ERP.
