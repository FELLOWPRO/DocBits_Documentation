# Facture d'Achat - 2ème Approbation de Quantité

<figure><img src="../../../.gitbook/assets/docbits_approval_invoice_4.png" alt="DocBits Approbation Facture 4"><figcaption></figcaption></figure>

Ce titre indique que la règle concerne spécifiquement le traitement des factures d'achat lors d'une phase d'approbation secondaire, en mettant l'accent sur la vérification de l'exactitude des quantités répertoriées.

#### Configuration de la Règle :

1. **Quand…**
* **Le Type de Document est Facture** : Cette condition garantit que la règle n'est activée que pour les documents classés comme des factures. Cela est essentiel pour maintenir la spécificité et la pertinence dans le flux de travail.
2. **Et…**
* **Le Statut du Document est En Attente de Deuxième Approbation** : Cela spécifie que la facture est actuellement en attente d'une deuxième approbation. Cette étape est généralement destinée à fournir une surveillance supplémentaire avant de finaliser la facture.
* **Le Sous-Type de Facture est Égal à Facture d'Achat** : Cette condition affine davantage la règle pour s'appliquer exclusivement aux factures identifiées comme "Factures d'Achat". Cette catégorisation aide à les différencier des autres types de factures.
* **La Quantité Logique dans la Confirmation de Commande n'Est Pas Égale à la Commande d'Achat** : Cette condition critique vérifie si la quantité indiquée dans la confirmation de commande correspond à la quantité de la commande d'achat d'origine. L'action est déclenchée s'il y a une divergence, indiquant une erreur potentielle ou un problème nécessitant une résolution.

#### Action (Ensuite…):

* **Attribuer l'utilisateur du champ Nom de l'Acheteur, utiliser l'utilisateur Utilisateur en tant que solution de secours** : Si les conditions de la règle sont remplies (c'est-à-dire s'il y a une divergence dans les quantités), la facture est automatiquement attribuée à la personne répertoriée dans le champ 'Nom de l'Acheteur' pour une révision ultérieure. Si ce champ est vide ou si la personne spécifiée n'est pas disponible, un utilisateur par défaut (probablement un administrateur ou un autre membre du personnel désigné) prend le relais pour garantir une révision et une résolution rapides.

#### Objectif de Cette Règle :

* **Précision et Conformité** : La règle est essentielle pour garantir que le processus de facturation est précis et conforme aux termes convenus dans la commande d'achat. Elle aide à prévenir les divergences financières et les erreurs potentielles d'inventaire.
* **Approbations Rationalisées** : L'automatisation du processus de révision pour des divergences spécifiques aide à rationaliser les approbations et garantit que tout problème est rapidement traité par le personnel approprié.
* **Surveillance Financière Renforcée** : Exiger une approbation secondaire pour les vérifications de quantité renforce les contrôles financiers et la responsabilité au sein de l'organisation.

Cette configuration illustre comment l'automatisation du flux de travail peut être utilisée pour améliorer l'efficacité opérationnelle et garantir l'intégrité financière, en particulier dans la gestion des processus d'achat complexes au sein d'une entreprise.
