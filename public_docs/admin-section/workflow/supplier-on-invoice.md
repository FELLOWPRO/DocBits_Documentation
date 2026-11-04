# Fournisseur sur la facture

<figure><img src="../../../../.gitbook/assets/image (276).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objet :**

Cette carte de flux de travail est conçue pour comparer les informations sur le fournisseur figurant sur une facture avec les informations sur le fournisseur figurant sur le bon de commande associé. La carte garantit que le fournisseur figurant sur la facture correspond au fournisseur figurant sur le bon de commande. Cette comparaison aide à vérifier que le bon fournisseur facture la commande et peut déclencher des actions en cas de divergences.

## **Composants de la carte :**

1. **Opérateur :**
   * **Description :** Définit la condition de comparaison du fournisseur sur la facture au fournisseur sur le bon de commande.
   * **Options :**
     * **Est (Is) :** Vérifie si le fournisseur sur la facture correspond au fournisseur sur le bon de commande.
     * **N'est pas (Is Not) :** Garantit que le fournisseur sur la facture ne correspond pas au fournisseur sur le bon de commande.

## **Fonctionnalité :**

* **Évaluation de la condition :** Le système compare le fournisseur sur la facture au fournisseur sur le bon de commande en fonction de l'opérateur sélectionné. Si la condition de comparaison est vraie (par exemple, le fournisseur est le même ou différent comme requis), le flux de travail se poursuivra en conséquence.
* **Exécution de l'action :**
  * **Condition vraie :** Si la condition est évaluée comme vraie (par exemple, le fournisseur sur la facture correspond au fournisseur sur le bon de commande), le flux de travail continue sans déclencher d'erreurs.
  * **Condition fausse :** Si la condition est évaluée comme fausse (par exemple, le fournisseur sur la facture ne correspond pas au fournisseur sur le bon de commande), le flux de travail ne continuera pas.

## **Configuration et paramétrage :**

* Les utilisateurs choisissent l'opérateur approprié (« Est » ou « N'est pas ») pour définir la manière dont les fournisseurs seront comparés.

## **Exemple de scénario :**

* Une facture indique un fournisseur avec l'ID "SUP123" et le bon de commande associé indique également "SUP123" comme fournisseur. En utilisant l'opérateur "Est", la carte compare les fournisseurs et constate qu'ils sont identiques, le flux de travail se poursuit donc sans aucun problème.

## **Conclusion :**

La carte de flux de travail "Comparaison de fournisseurs" garantit que le bon fournisseur facture le bon de commande, aidant ainsi à prévenir les divergences et les erreurs dans le processus d'achat. En vérifiant automatiquement les informations sur le fournisseur, les organisations peuvent simplifier leur processus d'approbation des factures et réduire le risque de fraude ou d'erreurs dans la facturation des fournisseurs.
