# Facture d'achat - Exportation de la quantité de 2e approbation

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_6.png" alt="DocBits Achat Commande Exporter 6"><figcaption></figcaption></figure>

Ce titre indique que la règle est configurée pour gérer la deuxième phase d'approbation des factures d'achat en mettant l'accent sur les détails de quantité, en veillant à ce que les quantités sur la facture correspondent à celles de la commande d'achat d'origine.

#### Configuration de la règle :

1. **Quand…**
* **Le type de document est une facture** : Cette condition garantit que la règle n'est activée que pour les documents identifiés comme des factures, ce qui est crucial pour diriger le flux de travail de manière précise.
2. **Et…**
* **Le statut du document est En attente de la deuxième approbation** : Cela spécifie que la facture est actuellement en attente d'une deuxième approbation. Cette étape offre souvent une supervision supplémentaire pour garantir l'exactitude avant que la transaction ne soit finalisée.
* **Le sous-type de facture est Égal à la facture d'achat** : Cette condition précise en outre que la règle s'applique uniquement aux factures catégorisées spécifiquement comme "Factures d'achat", les différenciant des autres types de factures.
* **La quantité logique dans la confirmation de commande est égale à la commande d'achat** : Cette condition vérifie si la quantité indiquée dans la confirmation de commande correspond à la quantité dans la commande d'achat. Cela garantit que le traitement de la facture ne progresse que si les quantités sont cohérentes, ce qui est essentiel pour la gestion des stocks et la précision financière.

#### Action (Ensuite…):

* **Démarrer l'exportation** : Une fois que la facture répond aux conditions spécifiées (c'est-à-dire que les quantités correspondent entre la confirmation de commande et la commande d'achat), l'action "Démarrer l'exportation" est déclenchée. Cela implique probablement d'exporter les données de la facture pour un traitement ultérieur, éventuellement vers un autre système financier ou à des fins de reporting.

#### Objectif de cette règle :

* **Garantir l'exactitude et la cohérence** : En vérifiant que les quantités correspondent entre la confirmation de commande et la commande d'achat, le système aide à maintenir l'exactitude des stocks et à éviter les écarts qui pourraient affecter les rapports financiers ou la gestion des stocks.
* **Optimiser le traitement financier** : L'automatisation de l'exportation des données une fois que les quantités sont confirmées réduit la manipulation manuelle et accélère le cycle de traitement financier.
* **Améliorer la conformité et la supervision** : Exiger une deuxième approbation pour la vérification des quantités ajoute une couche supplémentaire de supervision, essentielle pour la conformité aux politiques financières et aux contrôles.

Cette règle est un exemple clair de la manière dont l'automatisation du flux de travail peut être utilisée de manière efficace pour garantir une manipulation précise et efficace des documents financiers au sein d'une organisation, en particulier dans le contexte des processus d'achat impliquant de gros volumes de transactions nécessitant une validation méticuleuse.
