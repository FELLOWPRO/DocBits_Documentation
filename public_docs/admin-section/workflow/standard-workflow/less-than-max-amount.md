# Moins que le montant maximal

<figure><img src="../../../.gitbook/assets/docbits_invoice.png" alt="DocBits Facture"><figcaption></figcaption></figure>

Ce titre suggère que la règle ou la condition mise en place est conçue pour gérer les factures dont le montant total est inférieur ou égal à un montant maximal spécifié.

#### Configuration de la règle :

1. **Quand…**
* **Le type de document est Facture** : Cette condition vérifie si le document en cours de traitement est une facture. Cela est crucial pour garantir que la règle s'applique uniquement aux factures et non à d'autres types de documents.
2. **Et…**
* **Le statut du document est En attente d'approbation** : Cela spécifie que la facture doit être dans un statut "En attente d'approbation". Cette vérification de statut garantit que la règle s'applique uniquement aux factures en attente d'approbation.
* **Comparer deux champs : Montant total inférieur ou égal au montant maximal de l'approbateur** : Cette condition compare le montant total de la facture au montant maximal autorisé par l'approbateur. Si le montant total de la facture est inférieur ou égal à ce montant maximal, la règle passe à l'étape suivante. Cela inclut probablement un niveau de tolérance permettant des écarts mineurs dans des limites spécifiées.

#### Action (Alors…):

* **Attribuer l'utilisateur du champ Nom de l'approbateur, utiliser l'utilisateur Utilisateur en cas de secours** : Si les conditions spécifiées sont remplies, la facture est automatiquement attribuée à un approbateur dont le nom est spécifié dans un champ. Si ce champ est vide ou non disponible, un utilisateur par défaut (probablement un administrateur ou un autre membre du personnel désigné) est attribué en secours pour gérer l'approbation.

#### Éléments de l'interface :

* **Ajouter une carte** : Ce bouton permet probablement aux utilisateurs d'ajouter plus de conditions ou d'actions à la règle, améliorant ainsi la flexibilité et la spécificité du flux de travail.
* **Enregistrer** : Enregistre la règle configurée dans le système.

#### Objectif de cette règle :

Cette configuration est conçue pour rationaliser le processus d'approbation des factures en dirigeant automatiquement les factures vers l'approbateur approprié en fonction du montant et en garantissant que seules celles se situant dans une certaine plage sont traitées de cette manière automatisée. Cela aide à gérer les contrôles financiers et à accélérer le flux de travail en réduisant les vérifications manuelles pour chaque facture.
