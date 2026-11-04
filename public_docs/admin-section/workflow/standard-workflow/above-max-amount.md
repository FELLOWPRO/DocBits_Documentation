# Au-dessus du montant maximum

<figure><img src="../../../.gitbook/assets/docbits_invoice_2.png" alt="DocBits Facture 2"><figcaption></figcaption></figure>

Ce titre indique que la règle est conçue pour gérer les cas où le total de la facture est supérieur au montant maximum qu'un approbateur est autorisé à gérer.

#### Configuration de la règle :

1. **Quand…**
* **Le type de document est une facture** : Cette condition garantit que la règle s'applique uniquement aux factures, ce qui est essentiel pour diriger correctement le flux de travail.
2. **Et…**
* **Le statut du document est En attente d'approbation** : La facture doit être dans un statut "En attente d'approbation". Ce statut est crucial pour garantir que la règle s'applique aux factures qui sont encore en cours de traitement et n'ont pas encore été finalisées.
* **Comparer deux champs : Montant total supérieur au montant maximum de l'approbateur** : Cette condition vérifie si le montant total de la facture dépasse le montant maximum qu'un approbateur est autorisé à gérer. Cette comparaison peut également inclure un paramètre de tolérance, permettant des variations mineures en fonction de critères prédéfinis.

#### Action (Alors…):

* **Attribuer un utilisateur à partir du champ Approbateur de niveau suivant, utiliser l'utilisateur Utilisateur en cas de secours** : Si la facture dépasse le montant maximum spécifié, elle est automatiquement attribuée à un approbateur de niveau supérieur, indiqué par le champ 'Approbateur de niveau suivant'. Si ce champ n'est pas rempli ou si l'utilisateur spécifié n'est pas disponible, un utilisateur par défaut (probablement un administrateur ou un autre membre du personnel désigné) est utilisé en tant que secours pour garantir que la facture est examinée sans délai.

#### Éléments de l'interface :

* **Ajouter une carte** : Cette option permet d'ajouter des conditions ou des actions supplémentaires à la règle, offrant ainsi la flexibilité nécessaire pour traiter des scénarios complexes.
* **Enregistrer** : Ce bouton enregistre la configuration de la règle dans le système.

#### Objectif de cette règle :

Le but de cette règle est de garantir que les factures dépassant certains seuils financiers sont examinées par des approbateurs ayant les niveaux d'autorisation appropriés. Cela contribue à maintenir le contrôle financier et la supervision, en veillant à ce que les dépenses soient examinées par le personnel ayant les limites d'approbation requises, protégeant ainsi l'organisation contre des dépenses non autorisées ou inappropriées.

Cette règle, comme la précédente, contribue à automatiser le flux de travail, réduisant les efforts manuels et améliorant la conformité avec les politiques financières de l'organisation. C'est un exemple de la manière dont l'automatisation du flux de travail peut être utilisée efficacement pour gérer des processus financiers complexes au sein d'une entreprise.
