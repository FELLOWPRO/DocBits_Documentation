# Assign document to User

<figure><img src="../../../../.gitbook/assets/image (300).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow **« Assign Document to User »** permet aux utilisateurs d'assigner un document à un utilisateur spécifique, garantissant une gestion fluide du workflow en acheminant les documents vers la personne appropriée. La Version 3 ajoute la possibilité d'utiliser un arbre de décision pour déterminer dynamiquement l'attribution de l'utilisateur en fonction des conditions disponibles.

## **Composants de la carte :**

1. **User**
   * **Description :** spécifie l'utilisateur auquel le document sera assigné.
   * **Détail :** une liste déroulante de tous les utilisateurs disponibles est proposée pour la sélection. L'utilisateur sélectionné se verra attribuer le document pour une action complémentaire.

## **Composants supplémentaires dans la Version 3 :**

1. **Use Decision Tree**
   * **Description :** si elle est activée, la carte utilise un arbre de décision pour déterminer dynamiquement l'attribution de l'utilisateur.
   * **Options :**
     * **True :** utilise l'arbre de décision pour l'attribution dynamique de l'utilisateur.
     * **False :** assigne le document à l'utilisateur sélectionné sans utiliser l'arbre de décision.

## **Fonctionnalité :**

* **Évaluation de la condition :**\
  La carte n'exécute son action que si les sections **« Where »** et **« And »** sont toutes deux évaluées comme vraies.
* **Attribution du document :**\
  La carte assigne le document à l'utilisateur sélectionné, garantissant que la tâche est acheminée vers la personne appropriée pour action. Cela favorise la responsabilité et une gestion efficace des documents.
* **Arbre de décision (Version 3) :**\
  Si l'arbre de décision est activé, la carte évalue les conditions définies dans l'arbre pour sélectionner dynamiquement l'utilisateur de l'attribution du document.

## **Mise en place et configuration :**

* **Sélectionner l'utilisateur :**\
  Choisissez l'**utilisateur** dans la liste déroulante auquel le document sera assigné.
* **Use Decision Tree (Version 3) :**\
  Activez ou désactivez l'utilisation de l'arbre de décision pour sélectionner dynamiquement l'utilisateur.

## **Conclusion :**

La carte de workflow **« Assign Document to User »** facilite un acheminement efficace des documents en les assignant à l'utilisateur sélectionné, avec la flexibilité supplémentaire de la Version 3 de déterminer dynamiquement l'utilisateur à l'aide d'un arbre de décision. Cela garantit un processus de workflow plus adaptatif et efficace.
