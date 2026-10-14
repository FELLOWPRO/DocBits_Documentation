# Custom classification document

## Table `public.custom_classification_document`

### Colonnes

* `id`: internal
* `org_id`: ID to organisation
* `first_page_content`: text
* `content`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse et description

## Documentation technique de la table `public.custom_classification_document`

### Introduction

La table `public.custom_classification_document` sert à stocker des informations détaillées sur les classifications de documents au sein d'une organisation. Cela comprend des métadonnées sur le document, telles que son contenu, les détails de sa création et son contexte organisationnel. La structure de la table suggère qu'elle est utilisée pour gérer des documents liés aux processus de l'organisation, probablement des factures ou des bons de commande, comme on peut le déduire des données d'exemple.

### Description des colonnes

#### id

* **Signification** : cette colonne stocke vraisemblablement un identifiant unique pour chaque entrée de document.
* **Rôle** : clé primaire
* **Contenu typique** : un UUID représentant un identifiant de document unique.

#### org\_id

* **Signification** : cette colonne stocke l'identifiant de l'organisation associée au document.
* **Rôle** : clé étrangère
* **Contenu typique** : un UUID qui relie le document à une organisation précise.

#### first\_page\_content

* **Signification** : cette colonne contient le contenu textuel de la première page du document.
* **Rôle** : champ de données
* **Contenu typique** : une représentation textuelle du document d'une organisation, comprenant éventuellement des en-têtes, des adresses et les premiers détails d'une facture ou d'une commande.

#### content

* **Signification** : cette colonne stocke le contenu textuel complet du document.
* **Rôle** : champ de données
* **Contenu typique** : le contenu textuel intégral du document, y compris tous les détails présents sur la première page et les pages suivantes.

#### created\_by

* **Signification** : cette colonne indique l'utilisateur qui a créé l'entrée du document.
* **Rôle** : champ de données
* **Contenu typique** : un entier représentant l'ID utilisateur du créateur.

#### created\_on

* **Signification** : cette colonne enregistre la date et l'heure de création de l'entrée du document.
* **Rôle** : champ technique
* **Contenu typique** : un horodatage avec information de fuseau horaire, indiquant la date et l'heure de création.

#### last\_modified\_on

* **Signification** : cette colonne stocke la date et l'heure de la dernière modification de l'entrée du document.
* **Rôle** : champ technique
* **Contenu typique** : un horodatage avec information de fuseau horaire, indiquant la date et l'heure de la dernière modification. Il vaut parfois `None` si aucune modification n'a eu lieu après la création.

#### is\_deleted

* **Signification** : cette colonne indique si l'entrée du document a été marquée comme supprimée.
* **Rôle** : champ technique
* **Contenu typique** : une valeur booléenne (`True` ou `False`) indiquant l'état de suppression de l'entrée du document.

Cette table fournit une structure robuste pour gérer les données de documents, garantissant que chaque document peut être identifié de manière unique, associé à une organisation et suivi tout au long de son cycle de vie, de la création aux modifications.
