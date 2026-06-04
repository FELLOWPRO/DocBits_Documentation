# Confirmed Delivery Date

<figure><img src="../../../../.gitbook/assets/image (266).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif**

Cette carte de workflow est conçue pour vérifier que les dates de livraison confirmées sur les factures ou les documents d'expédition sont alignées sur les dates de livraison acceptées définies dans une table de données de référence. En comparant ces dates, elle aide à garantir le respect des calendriers de livraison convenus et améliore la fiabilité de la chaîne d'approvisionnement.

## **Composants de la carte**

1. **Operator**
   * **Description :** définit la condition de comparaison de la date de livraison confirmée à la date de livraison acceptée.
   * **Options :**
     * **Is :** confirme que la date de livraison correspond à la date de livraison acceptée dans les données de référence.
     * **Is Not :** s'assure que la date de livraison ne correspond pas à la date de livraison acceptée dans les données de référence.
2. **Master Data Table Lookup**
   * **Description :** spécifie la table de référence contenant les dates de livraison acceptées pour la comparaison.
   * **Détail :** la table est définie par le paramètre **Master Data Table** et peut inclure des métadonnées supplémentaires telles que des numéros de commande ou des régions de livraison.



## **Fonctionnalité**

* **Comparaison de dates :** le système compare la date de livraison confirmée de la facture ou du document d'expédition à la date de livraison acceptée dans la table de données de référence spécifiée.
* **Exécution de l'action :** selon le résultat de la comparaison, la carte peut déclencher des actions de suivi telles que des notifications.

## **Mise en place et configuration**

* Pour configurer cette carte, les utilisateurs sélectionnent le champ représentant la date de livraison confirmée dans le document et spécifient la table de données de référence contenant les dates de livraison acceptées. Un opérateur est ensuite choisi pour définir comment les deux dates doivent être comparées (par ex. **Is** ou **Is Not**).

## **Scénario d'exemple**

* Une facture indique une date de livraison confirmée du 10 juin, tandis que la table de données de référence spécifie une date de livraison acceptée du 15 juin. À l'aide de l'opérateur **Is Not**, la carte signale l'écart pour examen, permettant à l'équipe logistique d'en étudier la cause et d'ajuster les calendriers en conséquence.

## **Conclusion**

La carte de workflow **« Confirmed Delivery Date vs. Accepted Delivery Date »** aide les organisations à respecter les calendriers de livraison convenus en automatisant la comparaison des dates de livraison confirmées et acceptées. Cette approche proactive de la gestion des livraisons améliore l'efficacité opérationnelle, réduit les retards et favorise une meilleure collaboration tout au long de la chaîne d'approvisionnement.
