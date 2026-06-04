# Any Value of

<figure><img src="../../../../.gitbook/assets/image (46).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte DocBits sert à valider si une quelconque valeur d'une colonne spécifique d'un tableau correspond à un motif regex fourni. Si une seule entrée de la colonne correspond au motif, le workflow se poursuit, ce qui la rend idéale pour les cas d'usage où l'identification d'une seule correspondance déclenche les étapes suivantes du processus.

## **Fonctionnalité :**

* **Validation par motif regex :** cette carte vérifie si une quelconque valeur d'une colonne donnée d'un tableau correspond au motif d'expression régulière fourni. La carte se déclenche et permet la poursuite du workflow si au moins une entrée de la colonne satisfait la condition.
* **Operator :** les utilisateurs définissent la colonne et spécifient le motif regex. La condition disponible inclut :
  * **Matches Regex Pattern :** vérifie qu'au moins une valeur de la colonne spécifiée correspond au motif regex.
* **Sélection de la table et de la colonne :** les utilisateurs spécifient la table et la colonne qu'ils souhaitent vérifier pour des correspondances au motif regex.

## **Utilisation :**

Cette carte est particulièrement utile dans les scénarios où un tableau contient des données pouvant nécessiter des correspondances spécifiques, comme la validation d'adresses e-mail, de numéros de facture ou d'identifiants de produit. Elle garantit que les workflows se poursuivent lorsqu'une entrée pertinente correspond au motif défini, sans avoir à vérifier chaque entrée.

## **Scénario d'exemple :**

* Un utilisateur configure la carte pour vérifier les entrées de la colonne « Email Address » de la table « Customers », à l'aide d'un motif regex pour les formats d'e-mail valides. Si au moins une adresse e-mail de la colonne correspond au motif, la carte déclenche l'étape suivante du workflow, garantissant que le système traite l'entrée valide.

En utilisant la carte « Regex Pattern Matching », les organisations peuvent automatiser des workflows fondés sur des validations dynamiques basées sur des motifs, rationalisant les processus et garantissant que seules les entrées pertinentes déclenchent des actions supplémentaires.
