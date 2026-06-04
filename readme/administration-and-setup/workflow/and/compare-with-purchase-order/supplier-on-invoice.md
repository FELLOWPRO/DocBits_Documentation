# Supplier on Invoice

<figure><img src="../../../../.gitbook/assets/image (276).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour comparer les informations du fournisseur d'une facture aux informations du fournisseur du bon de commande associé. La carte garantit que le fournisseur de la facture correspond au fournisseur du bon de commande. Cette comparaison aide à vérifier que le bon fournisseur facture la commande et peut déclencher des actions en cas d'écarts.

## **Composants de la carte :**

1. **Operator :**
   * **Description** : définit la condition de comparaison du fournisseur de la facture au fournisseur du bon de commande.
   * **Options** :
     * **Is** : vérifie si le fournisseur de la facture correspond au fournisseur du bon de commande.
     * **Is Not** : s'assure que le fournisseur de la facture ne correspond pas au fournisseur du bon de commande.

## **Fonctionnalité :**

* **Évaluation de la condition :** le système compare le fournisseur de la facture au fournisseur du bon de commande en fonction de l'opérateur sélectionné. Si la condition de comparaison est vraie (par ex. le fournisseur est identique ou différent selon ce qui est requis), le workflow se poursuit en conséquence.
* **Exécution de l'action :**
  * **Condition vraie** : si la condition est évaluée comme vraie (par ex. le fournisseur de la facture correspond au fournisseur du bon de commande), le workflow se poursuit sans déclencher d'erreurs.
  * **Condition fausse** : si la condition est évaluée comme fausse (par ex. le fournisseur de la facture ne correspond pas au fournisseur du bon de commande), le workflow ne se poursuit pas.

## **Mise en place et configuration :**

* Les utilisateurs choisissent l'opérateur approprié (« Is » ou « Is Not ») pour définir comment les fournisseurs seront comparés.

## **Scénario d'exemple :**

* Une facture liste un fournisseur portant l'ID « SUP123 » et le bon de commande associé indique également « SUP123 » comme fournisseur. À l'aide de l'opérateur « Is », la carte compare les fournisseurs et les trouve identiques, de sorte que le workflow se poursuit sans problème.

## **Conclusion :**

La carte de workflow « Supplier Comparison » garantit que le bon fournisseur facture le bon de commande, contribuant à prévenir les écarts et les erreurs dans le processus d'approvisionnement. En vérifiant automatiquement les informations du fournisseur, les organisations peuvent rationaliser leur processus d'approbation des factures et réduire le risque de fraude ou d'erreurs dans la facturation fournisseur.
