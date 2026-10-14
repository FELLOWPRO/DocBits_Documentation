# Purchase Invoice - 2nd Approval Unit Price

<figure><img src="../../../../.gitbook/assets/docbits_approval_invoice_3.png" alt="DocBits Approbation Facture 3"><figcaption></figcaption></figure>

Ce titre indique que la règle est mise en place pour gérer la seconde phase d'approbation d'une facture d'achat, en mettant spécifiquement l'accent sur la validation du prix unitaire.

#### Configuration de la règle :

1. **When…**
   * **Document Type is Invoice** : Cette condition garantit que la règle n'est déclenchée que pour les documents identifiés comme factures, filtrant les autres types de documents et maintenant la pertinence du flux de travail.
2. **And…**
   * **Document Status is Pending Second Approval** : Cela précise que la facture se trouve dans la phase où elle est en attente d'une seconde approbation. Il s'agit généralement d'une étape conçue pour garantir une supervision supplémentaire avant le traitement final.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice** : Cela restreint encore l'application de cette règle aux seules factures classées comme « Purchase Invoices », les distinguant des autres sous-types de factures.
   * **Logic Unit Price in order confirmation Not Equals purchase order** : Cette vérification logique est cruciale car elle compare le prix unitaire indiqué dans la confirmation de commande au prix unitaire de la commande d'achat d'origine. L'action est déclenchée si ces valeurs ne correspondent pas, ce qui pourrait indiquer une divergence nécessitant une résolution.

#### Action (Then…) :

* **Assign user from field Buyer Name, use user User as fallback** : Si les conditions spécifiées sont remplies (c.-à-d. qu'il existe une non-correspondance dans les prix unitaires), la facture est automatiquement assignée à un acheteur (le nom spécifié dans le champ « Buyer Name ») pour examen complémentaire. Si le champ « Buyer Name » est vide ou non spécifié, un utilisateur par défaut (vraisemblablement un administrateur ou un autre membre du personnel désigné) est assigné en tant que solution de repli pour gérer l'approbation.

#### Objectif de cette règle :

* **Garantir l'exactitude et la conformité** : Cette règle est essentielle pour garantir que le processus de facturation est exact et conforme aux conditions convenues. En déclenchant un examen lorsqu'il existe une divergence dans les prix unitaires, le système aide à prévenir les erreurs financières ou la fraude potentielle.
* **Rationaliser les approbations** : L'automatisation de l'assignation pour examen en fonction de divergences spécifiques aide à rationaliser le processus d'approbation et garantit que les problèmes sont rapidement traités par le personnel approprié.
* **Supervision financière** : Exiger une seconde approbation, en particulier basée sur la correspondance des prix, renforce les contrôles financiers et la responsabilité au sein de l'organisation.
