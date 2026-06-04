# Any / All Unit Price is

<figure><img src="../../../../.gitbook/assets/image (274).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (273).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow sert à comparer le prix unitaire d'un document au prix unitaire d'un bon de commande, en garantissant que les prix correspondent dans les niveaux de tolérance définis. La comparaison peut déclencher des actions si le prix unitaire ne répond pas aux attentes. La **Version 4** ajoute davantage de flexibilité en permettant aux utilisateurs de choisir différentes entités à comparer, offrant un niveau de contrôle plus poussé sur les processus de tarification et d'approvisionnement.

## **Composants de la carte :**

1. **Any / All :**
   * **Description** : définit si la condition s'applique à une ou à toutes les occurrences où le prix unitaire est comparé.
   * **Options** :
     * **Any** : la condition est satisfaite si un quelconque prix unitaire satisfait la condition de comparaison spécifiée.
     * **All** : la condition n'est satisfaite que si tous les prix unitaires satisfont la condition de comparaison spécifiée.
2. **Operator :**
   * **Description** : définit la condition de comparaison du prix unitaire à la valeur spécifiée.
   * **Options** :
     * **Equals (=)** : vérifie si le prix unitaire correspond à la valeur spécifiée.
     * **Not Equals (≠)** : s'assure que le prix unitaire diffère de la valeur spécifiée.
     * **Greater Than (>)** : vérifie si le prix unitaire est supérieur à la valeur spécifiée.
     * **Greater or Equals (≥)** : vérifie si le prix unitaire est supérieur ou égal à la valeur spécifiée.
     * **Lesser Than (<)** : vérifie si le prix unitaire est inférieur à la valeur spécifiée.
     * **Lesser or Equals (≤)** : vérifie si le prix unitaire est inférieur ou égal à la valeur spécifiée.

## **Composants supplémentaires dans la Version 4 :**

**Comparison Type :**

* **Description** : permet aux utilisateurs de choisir quelles entités seront comparées en plus du prix unitaire.
* **Options** :
  * **Purchase Order to Document** : compare le prix unitaire du bon de commande au prix unitaire du document.
  * **Received to Document** : compare la quantité reçue au prix unitaire du document.
  * **Purchase Order to Received** : compare le prix unitaire du bon de commande à la quantité reçue.

## **Fonctionnalité :**

* **Évaluation de la condition :** le système compare le prix unitaire du document au prix unitaire du bon de commande (ou à une autre entité sélectionnée, dans la Version 4) en fonction de l'opérateur sélectionné. Si la comparaison est vraie, le workflow se poursuit selon les étapes suivantes, en déclenchant l'approbation ou en arrêtant le processus.
* **Exécution de l'action :**
  * **Condition vraie** : si la condition est évaluée comme vraie (par ex. le prix unitaire du document est supérieur à la valeur spécifiée), le workflow se poursuit avec l'action vraie (par ex. approbation, traitement du document).
  * **Condition fausse** : si la condition est évaluée comme fausse (par ex. le prix unitaire du document ne satisfait pas la comparaison), le workflow ne se poursuit pas.

## **Mise en place et configuration :**

* **Configuration de la Version 3 :** les utilisateurs configurent la carte en sélectionnant le prix unitaire du document, en choisissant l'opérateur approprié pour définir comment le prix unitaire sera comparé à la valeur spécifiée, et en définissant la valeur de comparaison. De plus, les utilisateurs indiquent si la condition s'applique à une ou à toutes les occurrences de la comparaison de prix unitaire.
* **Configuration de la Version 4 :** dans la Version 4, les utilisateurs disposent de l'option supplémentaire de sélectionner le Comparison Type. Cela leur permet de définir les entités à comparer, telles que Purchase Order to Document, Received to Document ou Purchase Order to Received. Cela accroît la flexibilité de la carte pour comparer les prix unitaires dans des scénarios plus complexes.

## **Scénario d'exemple :**

*   **Exemple Version 3 :**&#x20;

    Une facture indique un prix unitaire de 50 $. Le bon de commande associé a un prix unitaire de 45 $. La carte compare les deux prix unitaires à l'aide de l'opérateur « Greater Than ». Puisque le prix unitaire du document (50 $) est supérieur au prix unitaire du bon de commande (45 $), le workflow déclenche la condition vraie (par ex. envoyer le document pour examen).
* **Exemple Version 4 :**\
  Une facture indique un prix unitaire de 50 $, et le bon de commande associé autorisait un prix unitaire de 45 $. De plus, la quantité reçue est de 60 unités. La carte compare la quantité reçue au prix unitaire du document à l'aide de l'opérateur « Greater Than ». Puisque la quantité reçue (60) est supérieure au prix unitaire (50 $), le workflow déclenche la condition vraie et le document est signalé pour un examen complémentaire.

## **Conclusion :**

La Version 3 de la carte de workflow « Unit Price Comparison » est conçue pour garantir que les prix unitaires des documents correspondent à ceux des bons de commande, en déclenchant des actions selon des conditions définies. La Version 4 étend cette fonctionnalité en introduisant des options de comparaison plus complexes, comme la comparaison de bons de commande à des documents, de quantités reçues à des documents, et de bons de commande à des quantités reçues. Cette flexibilité supplémentaire permet aux organisations de gérer des scénarios de tarification et d'approvisionnement plus sophistiqués, améliorant le contrôle et la précision de leurs workflows.
