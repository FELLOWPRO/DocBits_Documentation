# Docfield is

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour automatiser des actions en comparant la valeur d'un champ de document spécifié à une valeur ou condition de référence. Elle garantit une prise de décision dynamique et précise dans les workflows, fondée sur la validation des données du document.

## **Composants de la carte :**

1. **Field Name**
   * **Description :** spécifie le nom du champ de document à évaluer.
   * **Détail :** il doit correspondre à l'identifiant exact du champ dans le document.
2. **Operators**
   * **Description :** définit le type de comparaison à effectuer entre la valeur du champ et la valeur de référence.
   * **Options :**
     * **Equals (=) :** vérifie si la valeur du champ correspond à la valeur de référence.
     * **Not Equals (≠) :** s'assure que la valeur du champ diffère de la valeur de référence.
     * **Greater Than (>) :** confirme que la valeur du champ est supérieure à la valeur de référence.
     * **Greater or Equals (≥) :** vérifie que la valeur du champ est égale ou supérieure à la valeur de référence.
     * **Lesser Than (<) :** vérifie si la valeur du champ est inférieure à la valeur de référence.
     * **Less or Equals (≤) :** s'assure que la valeur du champ est inférieure ou égale à la valeur de référence.

## **Fonctionnalité :**

* **Évaluation de la condition :** le système vérifie si la valeur du champ de document, par rapport à sa colonne associée, satisfait la condition de comparaison spécifiée par l'opérateur et la valeur de référence.
* **Exécution de l'action :**
  * **Condition vraie :**\
    Si la valeur du champ de document satisfait la condition spécifiée (par ex. égale la valeur de référence), le système déclenche les actions associées. Celles-ci peuvent inclure la mise à jour d'enregistrements, la progression du workflow ou la génération de notifications.
  * **Condition fausse :**\
    Si la valeur du champ de document ne satisfait pas la condition spécifiée, des actions alternatives ou aucune action sont exécutées, selon la configuration du workflow.

## **Mise en place et configuration :**

* L'utilisateur sélectionne le nom du champ du document concerné et choisit l'opérateur dans le menu déroulant. L'utilisateur spécifie ensuite la valeur de champ de référence pour finaliser la configuration.

## **Conclusion :**

La carte de workflow « DocField Comparison Validation » est un outil robuste pour le traitement dynamique des documents. En automatisant des actions en fonction des comparaisons de champs, cette carte rationalise les workflows, améliore la précision et facilite la prise de décision fondée sur les données.
