# Assign user from field

<figure><img src="../../../../.gitbook/assets/image (299).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow **« Assign User from Field with Fallback »** assigne dynamiquement un utilisateur en fonction de la valeur trouvée dans un champ de document spécifié. Si le champ ne contient pas d'utilisateur valide, un utilisateur de repli est sélectionné dans une liste prédéfinie d'utilisateurs disponibles pour garantir que la tâche ou l'action est correctement assignée.

## **Composants de la carte :**

1. **Field Name**
   * **Description :** spécifie le **champ de document** qui contient les informations de l'utilisateur à assigner.
   * **Détail :** ce champ est évalué pour déterminer quel utilisateur doit être assigné. Si le champ contient un utilisateur valide, cet utilisateur se verra attribuer la tâche. Si le champ est vide ou invalide, l'utilisateur de repli sera assigné.
2. **User (Fallback)**
   * **Description :** spécifie l'**utilisateur de repli** à assigner si le champ de document ne contient pas d'utilisateur valide.
   * **Détail :** une liste déroulante de tous les utilisateurs disponibles est proposée pour la sélection. Cet utilisateur sera assigné si le champ de document est vide ou ne contient pas d'utilisateur valide.

## **Fonctionnalité :**

* **Évaluation de la condition :**\
  La carte n'exécute son action que si les sections **« Where »** et **« And »** sont toutes deux évaluées comme vraies.
* **Attribution d'utilisateur basée sur un champ :**\
  La carte tente d'abord d'assigner la tâche ou l'action à l'utilisateur identifié dans le **Field Name**.
* **Attribution d'utilisateur de repli :**\
  Si le champ ne contient pas d'utilisateur valide (ou est vide), la carte assigne la tâche à l'utilisateur de repli sélectionné dans la liste déroulante **User (Fallback)**.

## **Mise en place et configuration :**

* **Sélectionner le Field Name :**\
  Choisissez le **champ de document** qui spécifie l'utilisateur de l'attribution.
* **Sélectionner l'utilisateur de repli :**\
  Choisissez l'**utilisateur de repli** dans la liste déroulante. Cet utilisateur se verra attribuer la tâche si le champ de document ne contient pas d'utilisateur valide.

## **Conclusion :**

La carte de workflow **« Assign User from Field with Fallback »** garantit qu'une tâche ou une action est toujours assignée à un utilisateur valide. Si l'utilisateur du champ de document n'est pas disponible, l'utilisateur de repli est automatiquement assigné, offrant de la flexibilité et garantissant l'achèvement de la tâche.
