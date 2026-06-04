# Less than Max Amount

<figure><img src="../../../../.gitbook/assets/docbits_invoice.png" alt="DocBits Facture"><figcaption></figcaption></figure>

Ce titre suggère que la règle ou la condition mise en place est conçue pour gérer les factures dont le montant total est inférieur ou égal à un montant maximum spécifié.

#### Configuration de la règle :

1. **When…**
   * **Document Type is Invoice** : Cette condition vérifie si le document en cours de traitement est une facture. Ceci est crucial pour garantir que la règle ne s'applique qu'aux factures et non à d'autres types de documents.
2. **And…**
   * **Document Status is Pending Approval** : Cela précise que la facture doit être au statut « Pending Approval ». Cette vérification de statut garantit que la règle ne s'applique qu'aux factures en attente d'approbation.
   * **Compare two fields: Total Amount Less Or Equals Approver Max Amount** : Cette condition compare le montant total de la facture au montant maximum autorisé d'un approbateur. Si le montant total de la facture est inférieur ou égal à ce montant maximum, la règle passe à l'étape suivante. Cela inclut vraisemblablement un niveau de tolérance permettant des écarts mineurs dans des limites spécifiées.

#### Action (Then…) :

* **Assign user from field Approver Name, use user User as fallback** : Si les conditions spécifiées sont remplies, la facture est automatiquement assignée à un approbateur dont le nom est spécifié dans un champ. Si ce champ est vide ou indisponible, un utilisateur par défaut (vraisemblablement un administrateur ou un autre membre du personnel désigné) est assigné en tant que solution de repli pour gérer l'approbation.

#### Éléments d'interface :

* **Add Card** : Ce bouton permet vraisemblablement aux utilisateurs d'ajouter davantage de conditions ou d'actions à la règle, améliorant la flexibilité et la spécificité du flux de travail.
* **Save** : Enregistre la règle configurée dans le système.

#### Objectif de cette règle :

Cette configuration est conçue pour rationaliser le processus d'approbation des factures en dirigeant automatiquement les factures vers l'approbateur approprié en fonction du montant et en garantissant que seules celles situées dans un certain seuil sont traitées de cette manière automatisée. Elle aide à gérer les contrôles financiers et accélère le flux de travail en réduisant les vérifications manuelles pour chaque facture.

\
