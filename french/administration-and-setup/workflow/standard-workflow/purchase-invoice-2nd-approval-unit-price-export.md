# Purchase Invoice - 2nd Approval Unit Price Export

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_export_5.png" alt="DocBits Achat Commande Exporter 5"><figcaption></figcaption></figure>

Ce titre indique que la règle est mise en place pour gérer la seconde phase d'approbation des factures d'achat en mettant l'accent sur le prix unitaire, garantissant qu'il correspond aux conditions convenues.

#### Configuration de la règle :

1. **When…**
   * **Document Type is Invoice** : Cette condition garantit que la règle n'est activée que pour les documents identifiés comme factures, ce qui est crucial pour orienter le flux de travail avec précision.
2. **And…**
   * **Document Status is Pending Second Approval** : Cela précise que la facture est en attente d'une seconde approbation. Cette étape fournit souvent une supervision supplémentaire pour garantir l'exactitude avant de finaliser la transaction.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice** : Cette condition précise en outre que la règle ne s'applique qu'aux factures catégorisées spécifiquement comme « Purchase Invoices », les différenciant des autres types de factures.
   * **Logic Unit Price in order confirmation Equals purchase order** : Cette condition vérifie si le prix unitaire indiqué dans la confirmation de commande correspond au prix unitaire de la commande d'achat. Elle garantit que le traitement de la facture ne se poursuit que s'il y a cohérence dans la tarification, ce qui est essentiel pour la budgétisation et le reporting financier.

#### Action (Then…) :

* **Start Export** : Une fois que la facture remplit les conditions spécifiées (c.-à-d. que les prix unitaires correspondent entre la confirmation de commande et la commande d'achat), l'action « Start Export » est déclenchée. Cela implique vraisemblablement l'exportation des données de la facture pour un traitement ultérieur, possiblement vers un autre système financier ou à des fins de reporting.

#### Objectif de cette règle :

* **Garantir l'exactitude et la cohérence** : En vérifiant que les prix unitaires correspondent entre la confirmation de commande et la commande d'achat, le système aide à maintenir l'exactitude financière et prévient les surfacturations ou sous-facturations.
* **Rationaliser le traitement financier** : L'automatisation de l'exportation des données une fois les prix confirmés réduit le traitement manuel et accélère le cycle de traitement financier.
* **Renforcer la conformité et la supervision** : Exiger une seconde approbation pour la vérification des prix ajoute une couche supplémentaire de supervision, ce qui est essentiel pour la conformité aux politiques et contrôles financiers.

Cette règle est un exemple de la manière dont l'automatisation des flux de travail peut être utilisée efficacement pour garantir un traitement précis et efficient des documents financiers au sein d'une organisation, en particulier dans le contexte de grands volumes de transactions nécessitant une validation méticuleuse.
