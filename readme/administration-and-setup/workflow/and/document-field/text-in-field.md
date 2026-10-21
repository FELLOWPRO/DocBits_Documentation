# Texte dans le champ

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-61d692604341-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour automatiser des actions en fonction de la présence ou de l'absence d'un texte spécifique dans un champ de document spécifié. Elle garantit que les workflows peuvent s'adapter dynamiquement au contenu des documents, favorisant un traitement efficace et une prise de décision précise.

## **Composants de la carte :**

1. **Texte**
   * **Descriptif :** spécifie la chaîne de texte à rechercher dans le champ.
   * **Détail :** il peut s'agir d'un mot, d'une expression ou d'une suite de caractères pertinents pour le workflow.
2. **Opérateur**
   * **Descriptif :** définit la condition de présence du texte dans le champ.
   * **Possibilités :**
     * **Is :** déclenche le workflow si le texte spécifié est présent dans le champ.
     * **N'est-ce pas :** déclenche le workflow si le texte spécifié n'est pas présent dans le champ.
3. **Nom du champ**
   * **Descriptif :** spécifie le nom du champ de document à évaluer.
   * **Détail :** il doit correspondre à l'identifiant exact du champ dans le document.

## **Fonctionnalité :**

1. **Évaluation de la condition :** le système vérifie si le texte spécifié existe dans le champ, en fonction de l'opérateur sélectionné (Is ou Is Not).
2. **Exécution de l'action :**
   * **Condition vraie :**\
     Si la présence du texte dans le champ correspond à la condition spécifiée, le système déclenche les actions associées. Celles-ci peuvent inclure le déclenchement d'alertes, la progression des workflows ou la mise à jour d'enregistrements.
   * **Condition fausse :**\
     Si la présence du texte dans le champ ne correspond pas à la condition, des actions alternatives ou aucune action peuvent être effectuées, selon la configuration du workflow.

## **Mise en place et configuration :**

* L'utilisateur saisit le texte à rechercher. Il sélectionne ensuite le nom du champ du document concerné.

## **Conclusion :**

La carte de workflow « Text Presence in Field » est un outil simple mais puissant pour l'analyse du contenu des documents. En automatisant des actions en fonction de la détection de texte, cette carte facilite des workflows plus intelligents, améliore l'exactitude du traitement des documents et réduit l'effort manuel.

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Recherchez des documents portant un marqueur de révision.

**Configuration :** Sélectionnez le champ de texte `review_note`, il contient l'opérateur et le texte `manual review`.

**Résultat attendu et contre-exemple :** `Please start manual review` réussit. `Ready for export` ne contient pas le texte sélectionné et échoue.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
