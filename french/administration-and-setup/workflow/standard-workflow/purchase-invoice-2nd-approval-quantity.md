# Purchase Invoice - 2nd Approval Quantity

<figure><img src="../../../../.gitbook/assets/docbits_approval_invoice_4.png" alt="DocBits Approbation Facture 4"><figcaption></figcaption></figure>

Ce titre indique que la règle concerne spécifiquement le traitement des factures d'achat lors d'une phase d'approbation secondaire, en mettant l'accent sur la vérification de l'exactitude des quantités indiquées.

#### Configuration de la règle :

1. **When…**
   * **Document Type is Invoice** : Cette condition garantit que la règle n'est activée que pour les documents classés comme factures. Ceci est essentiel pour maintenir la spécificité et la pertinence du flux de travail.
2. **And…**
   * **Document Status is Pending Second Approval** : Cela précise que la facture est actuellement en attente d'une seconde approbation. Cette étape vise généralement à fournir une supervision supplémentaire avant de finaliser la facture.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice** : Cette condition affine encore la règle pour qu'elle s'applique exclusivement aux factures identifiées comme « Purchase Invoices ». Cette catégorisation aide à les différencier des autres types de factures.
   * **Logic Quantity in order confirmation Not Equals purchase order** : Cette condition critique vérifie si la quantité indiquée dans la confirmation de commande correspond à la quantité de la commande d'achat d'origine. L'action est déclenchée en cas de divergence, signalant une erreur ou un problème potentiel nécessitant une résolution.

#### Action (Then…) :

* **Assign user from field Buyer Name, use user User as fallback** : Si les conditions de la règle sont remplies (c.-à-d. qu'il existe une divergence dans les quantités), la facture est automatiquement assignée à la personne indiquée dans le champ « Buyer Name » pour examen complémentaire. Si ce champ est vide ou si la personne spécifiée n'est pas disponible, un utilisateur par défaut (vraisemblablement un administrateur ou un autre membre du personnel désigné) prend le relais pour garantir un examen et une résolution en temps voulu.

#### Objectif de cette règle :

* **Exactitude et conformité** : La règle est essentielle pour garantir que le processus de facturation est exact et conforme aux conditions convenues dans la commande d'achat. Elle aide à prévenir les divergences financières et les éventuelles erreurs d'inventaire.
* **Approbations rationalisées** : L'automatisation du processus d'examen pour des divergences spécifiques aide à rationaliser les approbations et garantit que tout problème est rapidement traité par le personnel approprié.
* **Supervision financière renforcée** : Exiger une approbation secondaire pour les vérifications de quantité renforce les contrôles financiers et la responsabilité au sein de l'organisation.

Cette configuration illustre comment l'automatisation des flux de travail peut être utilisée pour améliorer l'efficacité opérationnelle et garantir l'intégrité financière, en particulier dans la gestion de processus d'achat complexes au sein d'une entreprise.
