# Assign document to recipient

<figure><img src="../../../../.gitbook/assets/image (301).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow **« Assign Document to Disponent / Purchaser »** assigne un document soit à un **Disponent**, soit à un **Purchaser**. Si aucun utilisateur valide n'est trouvé, un utilisateur de repli est sélectionné pour garantir que le document est toujours assigné à quelqu'un.

## **Composants de la carte :**

1. **Disponent / Purchaser**
   * **Description :** spécifie si le document sera assigné à un Disponent ou à un Purchaser.
   * **Options :**
     * **Disponent :** assigne le document au Disponent.
     * **Purchaser :** assigne le document au Purchaser.
2. **Fallback User**
   * **Description :** spécifie un utilisateur de repli au cas où le document ne pourrait pas être assigné au Disponent ou au Purchaser sélectionné.
   * **Détail :** la liste déroulante des utilisateurs disponibles vous permet de choisir un utilisateur de repli pour garantir que le document est assigné même si l'utilisateur principal ne peut pas être déterminé.

## **Fonctionnalité :**

* **Évaluation de la condition :**\
  La carte n'exécute son action que si les sections **« Where »** et **« And »** sont toutes deux évaluées comme vraies.
* **Attribution du document :**\
  La carte assigne le document soit au **Disponent**, soit au **Purchaser** selon la sélection. Si la personne sélectionnée n'est pas disponible ou n'est pas valide, le document est assigné à l'utilisateur de repli.

## **Mise en place et configuration :**

* **Sélectionner Disponent / Purchaser :**\
  Choisissez d'assigner le document au **Disponent** ou au **Purchaser**.
* **Sélectionner l'utilisateur de repli :**\
  Choisissez un utilisateur de repli dans la liste déroulante qui recevra le document si l'attribution principale n'est pas possible.

## **Conclusion :**

La carte de workflow **« Assign Document to Disponent / Purchaser »** garantit que le document est toujours assigné, soit au Disponent/Purchaser sélectionné, soit, si nécessaire, à l'utilisateur de repli. Cela minimise les interruptions du workflow et garantit que le traitement des documents se poursuit en toute fluidité.
