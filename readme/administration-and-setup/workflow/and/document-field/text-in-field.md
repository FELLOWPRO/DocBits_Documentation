# Text in Field

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour automatiser des actions en fonction de la présence ou de l'absence d'un texte spécifique dans un champ de document spécifié. Elle garantit que les workflows peuvent s'adapter dynamiquement au contenu des documents, favorisant un traitement efficace et une prise de décision précise.

## **Composants de la carte :**

1. **Text**
   * **Description :** spécifie la chaîne de texte à rechercher dans le champ.
   * **Détail :** il peut s'agir d'un mot, d'une expression ou d'une suite de caractères pertinents pour le workflow.
2. **Operator**
   * **Description :** définit la condition de présence du texte dans le champ.
   * **Options :**
     * **Is :** déclenche le workflow si le texte spécifié est présent dans le champ.
     * **Is Not :** déclenche le workflow si le texte spécifié n'est pas présent dans le champ.
3. **Field Name**
   * **Description :** spécifie le nom du champ de document à évaluer.
   * **Détail :** il doit correspondre à l'identifiant exact du champ dans le document.

## **Fonctionnalité :**

1. **Évaluation de la condition :** le système vérifie si le texte spécifié existe dans le champ, en fonction de l'opérateur sélectionné (Is ou Is Not).
2. **Exécution de l'action :**
   * **Condition vraie :**\
     Si la présence du texte dans le champ correspond à la condition spécifiée, le système déclenche les actions associées. Celles-ci peuvent inclure le déclenchement d'alertes, la progression des workflows ou la mise à jour d'enregistrements.
   * **Condition fausse :**\
     Si la présence du texte dans le champ ne correspond pas à la condition, des actions alternatives ou aucune action peuvent être effectuées, selon la configuration du workflow.

## **Mise en place et configuration :**&#x20;

* L'utilisateur saisit le texte à rechercher. Il sélectionne ensuite le nom du champ du document concerné.

## **Conclusion :**

La carte de workflow « Text Presence in Field » est un outil simple mais puissant pour l'analyse du contenu des documents. En automatisant des actions en fonction de la détection de texte, cette carte facilite des workflows plus intelligents, améliore l'exactitude du traitement des documents et réduit l'effort manuel.
