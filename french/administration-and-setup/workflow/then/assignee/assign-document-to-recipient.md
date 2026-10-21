# Attribuer un document au destinataire

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-1b1b68dfdcad-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

## **Objectif :**

La carte de workflow **« Attribuer le document au fournisseur/acheteur »** assigne un document soit à un **Disponent**, soit à un **Acheteur**. Si aucun utilisateur valide n'est trouvé, un utilisateur de repli est sélectionné pour garantir que le document est toujours assigné à quelqu'un.

## **Composants de la carte :**

1. **Disposant / Acheteur**
   * **Descriptif :** spécifie si le document sera assigné à un Disponent ou à un Purchaser.
   * **Possibilités :**
     * **Disponent :** assigne le document au Disponent.
     * **Acheteur :** assigne le document à l'Acheteur.
2. **Utilisateur de secours**
   * **Descriptif :** spécifie un utilisateur de repli au cas où le document ne pourrait pas être assigné au Disponent ou au Purchaser sélectionné.
   * **Détail :** la liste déroulante des utilisateurs disponibles vous permet de choisir un utilisateur de repli pour garantir que le document est assigné même si l'utilisateur principal ne peut pas être déterminé.

## **Fonctionnalité :**

* **Évaluation de la condition :**\
  La carte n'exécute son action que si les sections **« Quand »** et **« Et »** sont toutes deux évaluées comme vraies.
* **Attribution du document :**\
  La carte assigne le document soit au **Disponent**, soit au **Acheteur** selon la sélection. Si la personne sélectionnée n'est pas disponible ou n'est pas valide, le document est assigné à l'utilisateur de repli.

## **Mise en place et configuration :**

* **Sélectionner Disponent / Acheteur :**\
  Choisissez d'assigner le document au **Disponent** ou au **Acheteur**.
* **Sélectionner l'utilisateur de repli :**\
  Choisissez un utilisateur de repli dans la liste déroulante qui recevra le document si l'attribution principale n'est pas possible.

## **Conclusion :**

La carte de workflow **« Attribuer le document au fournisseur/acheteur »** garantit que le document est toujours assigné, soit au Disponent/Purchaser sélectionné, soit, si nécessaire, à l'utilisateur de repli. Cela minimise les interruptions du workflow et garantit que le traitement des documents se poursuit en toute fluidité.

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Attribuez un document à son destinataire résolu, avec une solution de secours sécurisée.

**Configuration :** Sélectionnez la source du destinataire et l'utilisateur de secours `Demo Reviewer A`.

**Résultat attendu et contre-exemple :** Un destinataire résoluble reçoit la mission. Si le destinataire ne peut pas être résolu, la solution de secours configurée est utilisée. Vérifiez les deux chemins.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
