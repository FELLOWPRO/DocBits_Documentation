# Comptabilisation automatique

## Table `public.auto_accounting`

### Colonnes

* `id`: internal
* `org_id`: ID to organisation
* `supplier_name`: Supplier Name
* `description`: internal
* `item_number`: internal
* `line_amount`: double precision
* `total_amount`: double precision
* `mapped_amount`: double precision
* `ledger_account`: internal
* `doc_id`: internal

### Analyse et description

## Documentation technique de la table `public.auto_accounting`

### Introduction

La table `public.auto_accounting` semble conçue pour gérer et stocker des données comptables relatives à divers fournisseurs et organisations. Elle enregistre des informations sur les transactions financières, notamment les montants et les comptes de grand livre, qui sont essentielles pour le reporting et l'analyse financiers.

### Description des colonnes

#### id

* **Signification** : un identifiant unique pour chaque enregistrement de la table.
* **Rôle** : clé primaire.
* **Contenu typique** : une chaîne UUID représentant chaque entrée de façon unique.
* **Remarque** : garantit que chaque enregistrement peut être identifié de manière distincte.

#### org\_id

* **Signification** : l'identifiant de l'organisation associée à l'écriture comptable.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne UUID renvoyant à une organisation dans une table parente.
* **Remarque** : sert à associer les écritures comptables à des organisations spécifiques.

#### supplier\_name

* **Signification** : le nom du fournisseur concerné par la transaction.
* **Rôle** : champ descriptif.
* **Contenu typique** : du texte représentant le nom du fournisseur, comme « Fellow Consulting AG ».
* **Remarque** : fournit des informations sur le fournisseur lié à la transaction.

#### description

* **Signification** : une courte description de la transaction ou de l'article.
* **Rôle** : champ descriptif.
* **Contenu typique** : du texte décrivant la transaction, par exemple le nom d'un article (« apple » ou « Peaches »).
* **Remarque** : utile pour comprendre la nature de la transaction.

#### item\_number

* **Signification** : l'identifiant d'un article précis concerné par la transaction.
* **Rôle** : champ descriptif.
* **Contenu typique** : peut être un identifiant de produit ou de SKU, bien qu'aucune donnée d'exemple ne soit fournie.
* **Remarque** : utile pour suivre ou référencer des articles spécifiques.

#### line\_amount

* **Signification** : le montant monétaire d'une ligne précise de la transaction.
* **Rôle** : champ financier.
* **Contenu typique** : une valeur décimale représentant le montant d'une ligne individuelle.
* **Remarque** : important pour l'analyse financière détaillée au niveau de la ligne.

#### total\_amount

* **Signification** : le montant monétaire total de la transaction.
* **Rôle** : champ financier.
* **Contenu typique** : une valeur décimale représentant le montant total de la transaction.
* **Remarque** : représente la somme de tous les montants de ligne d'une transaction.

#### mapped\_amount

* **Signification** : le montant qui a été alloué ou affecté à un compte précis.
* **Rôle** : champ financier.
* **Contenu typique** : une valeur décimale indiquant la part de la transaction qui a été allouée.
* **Remarque** : utile pour comprendre comment les fonds sont répartis entre les comptes.

#### ledger\_account

* **Signification** : le numéro du compte de grand livre dans lequel la transaction est enregistrée.
* **Rôle** : champ descriptif.
* **Contenu typique** : du texte représentant un numéro de compte, tel que « 2200 » ou « 2500 ».
* **Remarque** : essentiel en comptabilité pour suivre où les transactions sont comptabilisées.

#### doc\_id

* **Signification** : un identifiant d'un document ou d'un enregistrement associé.
* **Rôle** : clé étrangère ou référence.
* **Contenu typique** : une chaîne UUID ou un autre identifiant renvoyant à des documents associés.
* **Remarque** : permet d'associer les transactions à des documents ou enregistrements spécifiques pour assurer la traçabilité.

Cette documentation offre un aperçu détaillé de la table `public.auto_accounting`, en décrivant sa structure et le rôle de chaque colonne, afin d'aider les développeurs et les administrateurs de bases de données à comprendre et à exploiter efficacement les données.
