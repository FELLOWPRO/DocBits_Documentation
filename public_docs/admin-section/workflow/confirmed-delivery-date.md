# Date de livraison confirmée

<figure><img src="../../../../.gitbook/assets/image (266).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objet**

Cette carte de flux de travail est conçue pour vérifier que les dates de livraison confirmées sur les factures ou les documents d'expédition correspondent aux dates de livraison acceptées définies dans une table de recherche de données de référence. En comparant ces dates, elle aide à garantir le respect des calendriers de livraison convenus et renforce la fiabilité de la chaîne d'approvisionnement.

## **Composants de la carte**

1. **Opérateur**
   * **Description :** Définit la condition de comparaison entre la date de livraison confirmée et la date de livraison acceptée.
   * **Options :**
     * **Est (Is) :** Confirme que la date de livraison correspond à la date de livraison acceptée dans les données de référence.
     * **N'est pas (Is Not) :** Garantit que la date de livraison ne correspond pas à la date de livraison acceptée dans les données de référence.
2. **Recherche dans la table de données de référence**
   * **Description :** Spécifie la table de référence contenant les dates de livraison acceptées pour la comparaison.
   * **Détail :** La table est définie par le paramètre **Table de données de référence** et peut inclure des métadonnées supplémentaires telles que les numéros de commande ou les régions de livraison.



## **Fonctionnalité**

* **Comparaison de dates :** Le système compare la date de livraison confirmée de la facture ou du document d'expédition à la date de livraison acceptée dans la table de recherche de données de référence spécifiée.
* **Exécution de l'action :** En fonction du résultat de la comparaison, la carte peut déclencher des actions de suivi telles que des notifications.

## **Configuration et paramétrage**

* Pour configurer cette carte, les utilisateurs sélectionnent le champ représentant la date de livraison confirmée dans le document et spécifient la table de recherche de données de référence contenant les dates de livraison acceptées. Un opérateur est ensuite choisi pour définir comment les deux dates doivent être comparées (par exemple, **Est** ou **N'est pas**).

## **Exemple de scénario**

* Une facture indique une date de livraison confirmée au 10 juin, tandis que la table de recherche de données de référence spécifie une date de livraison acceptée au 15 juin. En utilisant l'opérateur **N'est pas**, la carte signale la divergence pour examen, permettant à l'équipe logistique d'enquêter sur la cause et d'ajuster les calendriers en conséquence.

## **Conclusion**

La carte de flux de travail **"Date de livraison confirmée vs Date de livraison acceptée"** aide les organisations à maintenir le respect des calendriers de livraison convenus en automatisant la comparaison des dates de livraison confirmées et acceptées. Cette approche proactive de la gestion des livraisons améliore l'efficacité opérationnelle, réduit les retards et favorise une meilleure collaboration tout au long de la chaîne d'approvisionnement.
