# Custom\_classification\_document\_label

## Table `public.custom_classification_document_label`

### Colonnes

* `id`: integer
* `org_id`: ID to organisation
* `doc_id`: internal
* `label_id`: integer
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse et description

## Documentation technique de la table `public.custom_classification_document_label`

### Introduction

La table `public.custom_classification_document_label` sert à gérer et à stocker les associations entre les documents et leurs libellés respectifs au sein d'une organisation. Cette table facilite la catégorisation et la recherche de documents à partir de libellés personnalisés, en offrant une manière structurée de gérer la classification des documents selon les besoins de l'organisation.

### Description des colonnes

#### id

* **Signification** : cette colonne sert d'identifiant unique pour chaque enregistrement de la table.
* **Rôle** : clé primaire
* **Contenu typique** : une valeur entière qui identifie chaque ligne de manière unique.
* **Remarque** : chaque entrée de la table possède un `id` distinct afin de garantir l'intégrité des données et de permettre un référencement efficace.

#### org\_id

* **Signification** : représente l'organisation à laquelle appartient l'association document-libellé.
* **Rôle** : clé étrangère
* **Contenu typique** : une chaîne de caractères, vraisemblablement un UUID, qui identifie une organisation de manière unique.
* **Remarque** : garantit que l'association entre documents et libellés est limitée au bon contexte organisationnel.

#### doc\_id

* **Signification** : identifie le document auquel un libellé est attribué.
* **Rôle** : clé étrangère
* **Contenu typique** : une chaîne de caractères, vraisemblablement un UUID, qui identifie un document de manière unique.
* **Remarque** : permet de lier des documents spécifiques à des libellés, ce qui rend possible la catégorisation des documents.

#### label\_id

* **Signification** : fait référence au libellé appliqué au document.
* **Rôle** : clé étrangère
* **Contenu typique** : un entier qui référence un libellé d'une table de libellés distincte.
* **Remarque** : facilite l'association entre les documents et leurs libellés respectifs.

#### created\_by

* **Signification** : identifie l'utilisateur qui a créé l'enregistrement.
* **Rôle** : clé étrangère (potentiellement vers une table d'utilisateurs)
* **Contenu typique** : un entier représentant l'ID de l'utilisateur.
* **Remarque** : permet de suivre l'origine de chaque association document-libellé à des fins d'audit et de responsabilité.

#### created\_on

* **Signification** : indique quand l'enregistrement a été créé.
* **Rôle** : champ technique
* **Contenu typique** : un horodatage avec information de fuseau horaire.
* **Remarque** : fournit un contexte temporel indiquant quand la relation document-libellé a été établie.

#### last\_modified\_on

* **Signification** : enregistre l'horodatage de la dernière modification de l'enregistrement.
* **Rôle** : champ technique
* **Contenu typique** : un horodatage avec information de fuseau horaire, pouvant valoir `None` si l'enregistrement n'a jamais été modifié.
* **Remarque** : utile pour suivre l'historique des modifications des associations document-libellé.

#### is\_deleted

* **Signification** : indique si l'enregistrement a été marqué comme supprimé.
* **Rôle** : champ technique
* **Contenu typique** : une valeur booléenne (`True` ou `False`).
* **Remarque** : prend en charge les pratiques de suppression logique, permettant de retirer logiquement des données sans les supprimer physiquement de la base de données.
