# Above Max Amount

<figure><img src="../../../../.gitbook/assets/docbits_invoice_2.png" alt="DocBits Facture 2"><figcaption></figcaption></figure>

Ce titre indique que la règle est conçue pour gérer les cas où le total de la facture est supérieur au montant maximum qu'un approbateur est autorisé à traiter.

#### Configuration de la règle :

1. **When…**
   * **Document Type is Invoice** : Cette condition garantit que la règle ne s'applique qu'aux factures, ce qui est essentiel pour orienter correctement le flux de travail.
2. **And…**
   * **Document Status is Pending Approval** : La facture doit être au statut « Pending Approval ». Ce statut est crucial pour garantir que la règle s'applique aux factures qui sont encore en cours de traitement et qui n'ont pas encore été finalisées.
   * **Compare two fields: Total Amount Greater Than Approver Max Amount** : Cette condition vérifie si le montant total de la facture dépasse le montant maximum qu'un approbateur est autorisé à traiter. Cette comparaison peut également inclure un paramètre de tolérance, permettant des variations mineures selon des critères prédéfinis.

#### Action (Then…) :

* **Assign user from field Next Level Approver, use user User as fallback** : Si la facture dépasse le montant maximum spécifié, elle est automatiquement assignée à un approbateur de niveau supérieur, indiqué par le champ « Next Level Approver ». Si ce champ n'est pas renseigné ou si l'utilisateur spécifié n'est pas disponible, un utilisateur par défaut (vraisemblablement un administrateur ou un autre membre du personnel désigné) est utilisé en tant que solution de repli pour garantir que la facture est examinée sans délai.

#### Éléments d'interface :

* **Add Card** : Cette option permet d'ajouter des conditions ou des actions supplémentaires à la règle, offrant une flexibilité pour traiter des scénarios complexes.
* **Save** : Ce bouton enregistre la configuration de la règle dans le système.

#### Objectif de cette règle :

L'objectif de cette règle est de garantir que les factures qui dépassent certains seuils financiers sont examinées par des approbateurs disposant des niveaux d'autorisation appropriés. Cela contribue à maintenir le contrôle et la supervision financière, en garantissant que les dépenses sont examinées par du personnel disposant des limites d'approbation requises, protégeant ainsi l'organisation contre les dépenses non autorisées ou inappropriées.

Cette règle, comme la précédente, aide à automatiser le flux de travail, réduisant l'effort manuel et améliorant la conformité aux politiques financières de l'organisation. C'est un exemple de la manière dont l'automatisation des flux de travail peut être utilisée efficacement pour gérer des processus financiers complexes au sein d'une entreprise.
