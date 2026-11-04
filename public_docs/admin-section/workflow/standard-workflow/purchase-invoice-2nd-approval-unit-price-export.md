# Facture d'achat - Exportation du prix unitaire de la 2ème approbation

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_5.png" alt="DocBits Achat Commande Exporter 5"><figcaption></figcaption></figure>

Ce titre indique que la règle est configurée pour gérer la deuxième phase d'approbation des factures d'achat en mettant l'accent sur le prix unitaire, en veillant à ce qu'il corresponde aux termes convenus.

#### Configuration de la règle :

1. **Quand…**
* **Le type de document est une facture** : Cette condition garantit que la règle n'est activée que pour les documents identifiés comme des factures, ce qui est crucial pour diriger le flux de travail de manière précise.
2. **Et…**
* **Le statut du document est En attente de la deuxième approbation** : Cela spécifie que la facture est en attente d'une deuxième approbation. Cette étape offre souvent une supervision supplémentaire pour garantir l'exactitude avant de finaliser la transaction.
* **Le sous-type de facture est égal à Facture d'achat** : Cette condition spécifie en outre que la règle s'applique uniquement aux factures catégorisées spécifiquement comme "Factures d'achat", les différenciant des autres types de factures.
* **La logique du prix unitaire dans la confirmation de commande est égale à la commande d'achat** : Cette condition vérifie si le prix unitaire indiqué dans la confirmation de commande correspond au prix unitaire dans la commande d'achat. Cela garantit que le traitement de la facture ne progresse que s'il y a une cohérence dans les prix, ce qui est essentiel pour la budgétisation et les rapports financiers.

#### Action (Ensuite…):

* **Démarrer l'exportation** : Une fois que la facture répond aux conditions spécifiées (c'est-à-dire que les prix unitaires correspondent entre la confirmation de commande et la commande d'achat), l'action "Démarrer l'exportation" est déclenchée. Cela implique probablement l'exportation des données de la facture pour un traitement ultérieur, éventuellement vers un autre système financier ou à des fins de reporting.

#### Objectif de cette règle :

* **Garantir l'exactitude et la cohérence** : En vérifiant que les prix unitaires correspondent entre la confirmation de commande et la commande d'achat, le système aide à maintenir l'exactitude financière et à éviter les surcharges ou les sous-charges.
* **Optimiser le traitement financier** : L'automatisation de l'exportation des données une fois les prix confirmés réduit la manipulation manuelle et accélère le cycle de traitement financier.
* **Améliorer la conformité et la supervision** : Exiger une deuxième approbation pour la vérification des prix ajoute une couche supplémentaire de supervision, ce qui est crucial pour la conformité aux politiques et aux contrôles financiers.

Cette règle est un exemple de la manière dont l'automatisation du flux de travail peut être utilisée de manière efficace pour garantir une manipulation précise et efficace des documents financiers au sein d'une organisation, en particulier dans le contexte de grands volumes de transactions nécessitant une validation méticuleuse.
