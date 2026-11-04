# Facture d'achat - 2ème approbation du prix unitaire

<figure><img src="../../../.gitbook/assets/docbits_approval_invoice_3.png" alt="DocBits Approbation Facture 3"><figcaption></figcaption></figure>

Ce titre indique que la règle est configurée pour gérer la deuxième phase d'approbation d'une facture d'achat, en mettant l'accent sur la validation du prix unitaire.

#### Configuration de la règle :

1. **Quand…**
* **Le type de document est Facture** : Cette condition garantit que la règle n'est déclenchée que pour les documents identifiés comme des factures, filtrant les autres types de documents et maintenant la pertinence du flux de travail.
2. **Et…**
* **Le statut du document est En attente de la deuxième approbation** : Cela spécifie que la facture est dans la phase où elle attend une deuxième approbation. Il s'agit généralement d'une étape conçue pour assurer une surveillance supplémentaire avant le traitement final.
* **Le sous-type de facture est Égal à Facture d'achat** : Cela restreint davantage l'application de cette règle uniquement aux factures classées comme "Factures d'achat", les distinguant des autres sous-types de factures.
* **La logique du prix unitaire dans la confirmation de commande n'est pas égale à la commande d'achat** : Cette vérification logique est cruciale car elle compare le prix unitaire indiqué dans la confirmation de commande avec le prix unitaire dans la commande d'achat d'origine. L'action est déclenchée si ces valeurs ne correspondent pas, ce qui pourrait indiquer une divergence nécessitant une résolution.

#### Action (Ensuite…):

* **Attribuer un utilisateur à partir du champ Nom de l'acheteur, utiliser l'utilisateur Utilisateur en tant que solution de secours** : Si les conditions spécifiées sont remplies (c'est-à-dire s'il y a une incohérence dans les prix unitaires), la facture est automatiquement attribuée à un acheteur (le nom spécifié dans le champ 'Nom de l'acheteur') pour examen ultérieur. Si le champ 'Nom de l'acheteur' est vide ou non spécifié, un utilisateur par défaut (probablement un administrateur ou un autre membre du personnel désigné) est attribué en tant que solution de secours pour gérer l'approbation.

#### Objectif de cette règle :

* **Garantir l'exactitude et la conformité** : Cette règle est cruciale pour garantir que le processus de facturation est précis et conforme aux termes convenus. En déclenchant un examen en cas de divergence dans les prix unitaires, le système aide à prévenir les erreurs financières ou les fraudes potentielles.
* **Simplifier les approbations** : L'automatisation de l'attribution pour examen en fonction de divergences spécifiques aide à simplifier le processus d'approbation et garantit que les problèmes sont rapidement traités par le personnel approprié.
* **Surveillance financière** : Exiger une deuxième approbation, notamment basée sur la correspondance des prix, renforce les contrôles financiers et la responsabilité au sein de l'organisation.
