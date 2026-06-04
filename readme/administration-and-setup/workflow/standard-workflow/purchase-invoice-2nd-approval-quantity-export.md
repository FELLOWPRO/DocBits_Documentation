# Purchase Invoice - 2nd Approval Quantity Export

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_export_6.png" alt="DocBits Achat Commande Exporter 6"><figcaption></figcaption></figure>

Ce titre indique que la règle est mise en place pour gérer la seconde phase d'approbation des factures d'achat en mettant l'accent sur les détails de quantité, garantissant que les quantités figurant sur la facture correspondent à celles de la commande d'achat d'origine.

#### Configuration de la règle :

1. **When…**
   * **Document Type is Invoice** : Cette condition garantit que la règle n'est activée que pour les documents identifiés comme factures, ce qui est crucial pour orienter le flux de travail avec précision.
2. **And…**
   * **Document Status is Pending Second Approval** : Cela précise que la facture est actuellement en attente d'une seconde approbation. Cette étape fournit souvent une supervision supplémentaire pour garantir l'exactitude avant que la transaction ne soit finalisée.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice** : Cette condition précise en outre que la règle ne s'applique qu'aux factures catégorisées spécifiquement comme « Purchase Invoices », les différenciant des autres types de factures.
   * **Logic Quantity in order confirmation Equals purchase order** : Cette condition vérifie si la quantité indiquée dans la confirmation de commande correspond à la quantité de la commande d'achat. Elle garantit que le traitement de la facture ne se poursuit que si les quantités sont cohérentes, ce qui est essentiel pour la gestion des stocks et l'exactitude financière.

#### Action (Then…) :

* **Start Export** : Une fois que la facture remplit les conditions spécifiées (c.-à-d. que les quantités correspondent entre la confirmation de commande et la commande d'achat), l'action « Start Export » est déclenchée. Cela implique vraisemblablement l'exportation des données de la facture pour un traitement ultérieur, possiblement vers un autre système financier ou à des fins de reporting.

#### Objectif de cette règle :

* **Garantir l'exactitude et la cohérence** : En vérifiant que les quantités correspondent entre la confirmation de commande et la commande d'achat, le système aide à maintenir l'exactitude des stocks et prévient les divergences qui pourraient affecter le reporting financier ou la gestion des stocks.
* **Rationaliser le traitement financier** : L'automatisation de l'exportation des données une fois les quantités confirmées réduit le traitement manuel et accélère le cycle de traitement financier.
* **Renforcer la conformité et la supervision** : Exiger une seconde approbation pour la vérification des quantités ajoute une couche supplémentaire de supervision, essentielle pour la conformité aux politiques et contrôles financiers.

Cette règle est un exemple clair de la manière dont l'automatisation des flux de travail peut être utilisée efficacement pour garantir un traitement précis et efficient des documents financiers au sein d'une organisation, en particulier dans le contexte de processus d'achat impliquant de grands volumes de transactions nécessitant une validation méticuleuse.
