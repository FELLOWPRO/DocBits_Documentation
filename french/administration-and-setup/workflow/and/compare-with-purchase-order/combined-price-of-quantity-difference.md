# Combined Price of Quantity Difference

<figure><img src="../../../../.gitbook/assets/image (17) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (21) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif** :

Cette carte de workflow évalue le prix combiné d'un écart de quantité, en le comparant à une valeur spécifiée. Elle aide à automatiser des actions en fonction des écarts de prix et de quantité entre documents associés, améliorant les workflows d'approvisionnement et de réception. La **Version 4** étend cette fonctionnalité en permettant des comparaisons entre différentes entités telles que le bon de commande, les quantités reçues et le document lui-même, ajoutant davantage de flexibilité et de contrôle au workflow.

## **Composants de la carte** :

1. **Operator** :&#x20;
   * **Description :** la condition de comparaison du prix combiné à une valeur spécifiée.
   * **Options :**
     * **Equals (=)** : vérifie si le prix combiné correspond à la valeur spécifiée.
     * **Not Equals (≠)** : s'assure que le prix combiné diffère de la valeur spécifiée.
     * **Greater Than (>)** : vérifie si le prix combiné est supérieur à la valeur spécifiée.
     * **Greater or Equals (≥)** : vérifie si le prix combiné est supérieur ou égal à la valeur spécifiée.
     * **Lesser Than (<)** : vérifie si le prix combiné est inférieur à la valeur spécifiée.
     * **Lesser or Equals (≤)** : vérifie si le prix combiné est inférieur ou égal à la valeur spécifiée.
2. **Value** :&#x20;
   * **Description :** spécifie la valeur à laquelle le prix combiné de la valeur de quantité sera comparé.
   * **Détail :** la valeur doit être une valeur numérique.

## **Composants supplémentaires dans la Version 4** :

* **Comparison Type** : sélectionne les entités à comparer. Les options incluent :
  * **Purchase Order to Document** : compare les quantités et les prix entre le bon de commande et le document associé.
  * **Received to Document** : compare les quantités reçues aux quantités du document.
  * **Purchase Order to Received** : compare les quantités du bon de commande aux quantités reçues.

## **Fonctionnalité** :

* **Évaluation de la condition** : calcule le prix combiné en multipliant l'écart de quantité par le prix unitaire et le compare à la valeur spécifiée à l'aide de l'opérateur sélectionné.\
  La **Version 4** ajoute la possibilité de comparer des entités supplémentaires en fonction de la configuration de l'utilisateur, comme bon de commande vers reçu ou bon de commande vers document.
* **Exécution de l'action** : selon que le prix combiné satisfait ou non la condition spécifiée, le workflow se poursuit avec des conditions vraies ou fausses pour déclencher des actions ou interrompre le workflow. La **Version 4** permet également une exécution d'action plus dynamique, où le type de condition (par ex. bon de commande vers reçu) influence l'étape suivante.

## **Mise en place et configuration** :

* **Version 3** : les utilisateurs configurent la carte en sélectionnant les champs de document pour l'écart de quantité et le prix unitaire. L'opérateur est ensuite choisi pour définir comment le prix combiné sera comparé à la valeur spécifiée. Enfin, les utilisateurs définissent la condition de poursuite (vraie ou fausse), qui dicte l'étape suivante du workflow.
* **Version 4** : en plus de la configuration de la **Version 3**, les utilisateurs disposent d'une option supplémentaire pour configurer le **Comparison Type**. Celui-ci définit quelles entités seront comparées, telles que **Purchase Order to Document**, **Received to Document** ou **Purchase Order to Received**.

## **Scénario d'exemple** :

* Une facture indique 50 unités d'un produit à 100 $ chacune, soit un total de 5000 $. Le bon de commande associé autorisait un achat de 4500 $ pour 45 unités. L'écart de quantité est de 5 unités, et le prix combiné de l'écart est de 500 $. La carte compare la quantité du bon de commande (45 unités) à la quantité reçue (50 unités) et vérifie si le prix combiné est supérieur à 400 $ (la valeur spécifiée). À l'aide de l'opérateur **Greater Than (>)**, la carte identifie l'écart et le signale pour examen par l'équipe financière.

## **Conclusion** :

La **Version 3** de la carte de workflow « Combined Price of Quantity Difference » offre une approche simple pour comparer les écarts de quantité et déclencher des actions en fonction de seuils de prix.\
La **Version 4** étend cette fonctionnalité en permettant des comparaisons entre différentes entités (bon de commande, reçu, document), offrant plus de flexibilité et de contrôle sur le workflow. Les organisations peuvent désormais automatiser des scénarios plus complexes et appliquer un contrôle plus strict sur leurs processus d'approvisionnement et de réception.
