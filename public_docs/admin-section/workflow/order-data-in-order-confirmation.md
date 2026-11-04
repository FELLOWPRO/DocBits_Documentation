# Données de commande dans la confirmation de commande

<figure><img src="../../../../.gitbook/assets/image (265).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objet**

Cette carte de flux de travail est conçue pour comparer des champs spécifiques — **Prix unitaire**, **Remise** ou **Quantité** — entre une confirmation de commande et un bon de commande. Elle assure la cohérence et la conformité avec les conditions convenues. En fonction du résultat de la comparaison, la carte permet aux utilisateurs d'écrire un texte spécifié dans un champ choisi lorsque la condition est évaluée comme **vraie** ou **fausse**, simplifiant ainsi le traitement des documents et réduisant l'intervention manuelle.

## **Composants de la carte**

1. **Données de commande**
   * **Description :** Spécifie le champ à comparer entre la confirmation de commande et le bon de commande.
   * **Options :**
     * **Prix unitaire** : Compare le prix unitaire dans les deux documents.
     * **Remise** : Compare le pourcentage ou la valeur de la remise.
     * **Quantité** : Compare la quantité commandée.
2. **Opérateur**
   * **Description :** Définit la condition appliquée lors de la comparaison.
   * **Options :**
     * **Égal (=) :** Vérifie si la valeur du champ sélectionné correspond entre la confirmation de commande et le bon de commande.
     * **Non égal (≠) :** Garantit que la valeur du champ sélectionné diffère entre les deux documents.
3. **Texte**
   * **Description :** Spécifie le texte à écrire dans le champ cible lors de l'évaluation de la condition.
   * **Détail :** Ce texte peut inclure des notes personnalisées, des mises à jour de statut ou des valeurs prédéfinies.
4. **Nom du champ**
   * **Description :** Spécifie le champ où le texte sera écrit.
   * **Détail :** Le champ cible est sélectionné parmi les champs modifiables disponibles dans le système.
5. **Résultat de la condition**
   * **Description :** Détermine quand le texte doit être écrit, en fonction du résultat de la comparaison.
   * **Options :**
     * **Vrai :** Écrit le texte si la condition de comparaison est remplie.
     * **Faux :** Écrit le texte si la condition de comparaison n'est pas remplie.

## **Fonctionnalité**

* **Évaluation de la comparaison :** Le système compare le champ sélectionné entre la confirmation de commande et le bon de commande à l'aide de l'opérateur spécifié.
* **Exécution de l'action :** Si la condition est évaluée comme **vraie** ou **fausse**, le texte spécifié est écrit dans le champ désigné.

## **Configuration et paramétrage**

* Pour configurer cette carte, les utilisateurs sélectionnent d'abord le champ à comparer — **Prix unitaire**, **Remise** ou **Quantité**. Ensuite, ils choisissent un opérateur pour définir la condition de comparaison, telle que **égal** ou **non égal**. Les utilisateurs spécifient le texte à écrire dans un champ cible et sélectionnent quand cette action doit se produire, en fonction du résultat de la condition (**vrai** ou **faux**).

## **Exemple de scénario**

* Une confirmation de commande indique un prix unitaire de 50 $ pour un produit, tandis que le bon de commande spécifie un prix de 45 $. En utilisant l'opérateur **Non égal (≠)**, la carte identifie la divergence et écrit le texte "Écart de prix" dans un champ désigné lorsque la condition est évaluée comme **vraie**.

## **Conclusion**

La carte de flux de travail "[Prix unitaire/Remise/Quantité] dans la confirmation de commande" offre une solution pratique pour assurer la cohérence des documents. En signalant automatiquement les divergences et en écrivant le texte pertinent dans des champs spécifiés, elle améliore l'efficacité et réduit les erreurs dans les processus de gestion des commandes.
