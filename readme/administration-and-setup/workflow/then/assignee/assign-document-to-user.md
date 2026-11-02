# Attribuer un document à un utilisateur

<figure><img src="../../../../.gitbook/assets/workflow_card_doc_user_assign_v1-fr-fr.png" alt="Attribuer un document à un utilisateur, Version 1" width="634"><figcaption><p>Version 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_doc_user_assign_v2-fr-fr.png" alt="Attribuer un document à un utilisateur, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_doc_user_assign_v3-fr-fr.png" alt="Attribuer un document à un utilisateur, Version 3" width="634"><figcaption><p>Version 3</p></figcaption></figure>

## **Objectif :**

La carte de workflow **« Assign Document to User »** permet aux utilisateurs d'assigner un document à un utilisateur spécifique, garantissant une gestion fluide du workflow en acheminant les documents vers la personne appropriée. La Version 3 ajoute la possibilité d'utiliser un arbre de décision pour déterminer dynamiquement l'attribution de l'utilisateur en fonction des conditions disponibles.

## **Composants de la carte :**

1. **Utilisateur**
   * **Descriptif :** spécifie l'utilisateur auquel le document sera assigné.
   * **Détail :** une liste déroulante de tous les utilisateurs disponibles est proposée pour la sélection. L'utilisateur sélectionné se verra attribuer le document pour une action complémentaire.

## **Composants supplémentaires dans la Version 3 :**

1. **Utiliser l'arbre de décision**
   * **Descriptif :** si elle est activée, la carte utilise un arbre de décision pour déterminer dynamiquement l'attribution de l'utilisateur.
   * **Possibilités :**
     * **True :** utilise l'arbre de décision pour l'attribution dynamique de l'utilisateur.
     * **False :** assigne le document à l'utilisateur sélectionné sans utiliser l'arbre de décision.

## **Fonctionnalité :**

* **Évaluation de la condition :**\
  La carte n'exécute son action que si les sections **« Quand »** et **« Et »** sont toutes deux évaluées comme vraies.
* **Attribution du document :**\
  La carte assigne le document à l'utilisateur sélectionné, garantissant que la tâche est acheminée vers la personne appropriée pour action. Cela favorise la responsabilité et une gestion efficace des documents.
* **Arbre de décision (Version 3) :**\
  Si l'arbre de décision est activé, la carte évalue les conditions définies dans l'arbre pour sélectionner dynamiquement l'utilisateur de l'attribution du document.

## **Mise en place et configuration :**

* **Sélectionner l'utilisateur :**\
  Choisissez l'**utilisateur** dans la liste déroulante auquel le document sera assigné.
* **Utiliser l'arbre de décision (Version 3) :**\
  Activez ou désactivez l'utilisation de l'arbre de décision pour sélectionner dynamiquement l'utilisateur.

## **Conclusion :**

La carte de workflow **« Assign Document to User »** facilite un acheminement efficace des documents en les assignant à l'utilisateur sélectionné, avec la flexibilité supplémentaire de la Version 3 de déterminer dynamiquement l'utilisateur à l'aide d'un arbre de décision. Cela garantit un processus de workflow plus adaptatif et efficace.

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Envoyez les factures nécessitant une révision manuelle à une personne responsable.

**Configuration :** Sélectionnez l'utilisateur configuré `Demo Reviewer A`.

**Résultat attendu et contre-exemple :** Le document est attribué à cet utilisateur. Confirmez l'affectation du document résultant ; cette carte ne crée pas en elle-même une tâche de révision distincte.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
