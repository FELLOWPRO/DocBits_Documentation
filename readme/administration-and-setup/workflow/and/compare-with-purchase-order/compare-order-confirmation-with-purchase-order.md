# Compare Order Confirmation with Purchase order

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (267).png" alt="" width="563"><figcaption></figcaption></figure>

## Objectif :

Cette carte DocBits est conçue pour comparer un champ de données de commande spécifique — comme la quantité, la remise ou le prix unitaire — entre une confirmation de commande et un bon de commande. En permettant une comparaison ciblée d'un champ à la fois, elle garantit la précision dans la validation des points de données clés, préservant l'exactitude des commandes. La **Version 4** étend cette fonctionnalité en permettant des comparaisons entre différentes entités telles que le bon de commande, les quantités reçues et le document lui-même, ajoutant davantage de flexibilité et de contrôle au workflow.

## Composants de la carte :

1. **Any/All**&#x20;
   * **Description :** détermine si la condition s'applique à une ou à toutes les lignes de la confirmation de commande.\
     **Options :**
     * **Any** : la comparaison se déclenche si la valeur du champ sélectionné dans une quelconque ligne de la confirmation de commande correspond à la valeur correspondante du bon de commande.
     * **All** : la comparaison ne se déclenche que si la valeur du champ sélectionné dans toutes les lignes de la confirmation de commande correspond à la valeur correspondante du bon de commande.
2. **Order Data Field**
   * **Description** : spécifie le champ de données à comparer entre la confirmation de commande et le bon de commande.
   * **Détail** : les utilisateurs peuvent sélectionner l'un des champs suivants pour la comparaison :
     * **Quantity** : compare la quantité commandée à la quantité confirmée.
     * **Discount** : vérifie que la remise de la confirmation correspond au bon de commande.
     * **Unit Price** : garantit que le prix unitaire de la confirmation est aligné sur le bon de commande.
3. **Operator**
   * **Description** : définit la condition appliquée à la comparaison du champ de données sélectionné.
   * **Options** :
     * **Equals (=)** : confirme que la valeur correspond au bon de commande.
     * **Not Equals (≠)** : s'assure que la valeur diffère du bon de commande.
     * **Greater Than (>)** : vérifie que la valeur dépasse celle du bon de commande.
     * **Greater or Equals (≥)** : confirme que la valeur est égale ou supérieure à celle du bon de commande.
     * **Less Than (<)** : vérifie que la valeur est inférieure à celle du bon de commande.
     * **Less or Equals (≤)** : confirme que la valeur est inférieure ou égale à celle du bon de commande.

## **Composants supplémentaires dans la Version 4** :

* **Comparison Type** : sélectionne les entités à comparer. Les options incluent :
  * **Purchase Order to Document** : compare les données du bon de commande au document associé.
  * **Received to Document** : compare les données reçues (par ex. les quantités reçues) au document.
  * **Purchase Order to Received** : compare les données du bon de commande aux quantités reçues.

## Fonctionnalité :

* **Comparaison de champ** : le système compare le champ de données de commande sélectionné (Unit Price, Discount ou Quantity) de la confirmation de commande à la valeur correspondante du bon de commande.
* **Exécution de l'action** : selon le résultat de la comparaison et la condition de l'opérateur, la carte peut déclencher des actions de suivi, telles que des notifications ou des alertes.

## Scénario d'exemple :

* Une confirmation de commande spécifie un **prix unitaire** de 50 $, tandis que le bon de commande indique 45 $. À l'aide de l'opérateur « Greater Than », la carte signale l'écart, permettant à l'équipe d'approvisionnement de le traiter avant le traitement.

## Conclusion :

Cette carte simplifie la validation des champs de données de commande individuels, garantissant la conformité aux conditions du bon de commande. En isolant un champ à la fois pour la comparaison, elle facilite les examens ciblés et la prévention des erreurs dans le traitement des commandes.
