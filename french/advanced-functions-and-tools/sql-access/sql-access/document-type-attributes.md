# Attributs du type de document

## Colonnes

* `id`: internal
* `org_id`: ID to organisation
* `doc_type_key`: internal
* `sub_doc_type_key`: internal
* `attribute_key`: internal
* `attribute_value`: text
* `created_by`: integer
* `created_on` : horodatage avec fuseau horaire
* `last_modified_on` : horodatage avec fuseau horaire
* `is_deleted`: boolean
* `sub_org_id`: internal

## Analyse et description

```markdown
# Documentation technique de la table `public.document_type_attributes`

## Introduction

La table `public.document_type_attributes` semble conçue pour gérer les attributs liés à divers types de documents dans un contexte organisationnel. Cette table prend vraisemblablement en charge la configuration ou la gestion des métadonnées pour différents types de documents, tels que les factures ou les bons de livraison, en associant des attributs spécifiques à chaque type de document.

## Description des colonnes

### id
- **Signification** : un identifiant unique pour chaque enregistrement de la table.
- **Rôle** : clé primaire.
- **Contenu typique** : une chaîne UUID qui identifie une ligne de la table de manière unique.

### org_id
- **Signification** : représente l'organisation à laquelle appartient l'attribut du type de document.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID référençant une organisation.

### doc_type_key
- **Signification** : le type de document auquel l'attribut s'applique (par ex. INVOICE, DELIVERY_NOTE).
- **Rôle** : champ descriptif.
- **Contenu typique** : une chaîne représentant un type de document.

### sub_doc_type_key
- **Signification** : une catégorisation plus précise au sein du type de document, le cas échéant.
- **Rôle** : champ descriptif.
- **Contenu typique** : généralement `None`, ce qui indique qu'il n'est pas toujours utilisé.

### attribute_key
- **Signification** : la clé de l'attribut ou de la propriété spécifique liée au type de document.
- **Rôle** : champ descriptif.
- **Contenu typique** : une chaîne représentant une clé d'attribut, telle que `SECOND_APPROVAL_BEFORE_EXPORT`.

### attribute_value
- **Signification** : la valeur associée à la clé d'attribut pour le type de document.
- **Rôle** : champ descriptif.
- **Contenu typique** : une chaîne ou une valeur numérique qui fournit la valeur de l'attribut, par ex. `true`, `123`.

### created_by
- **Signification** : l'identifiant de l'utilisateur qui a créé l'enregistrement.
- **Rôle** : champ descriptif.
- **Contenu typique** : un entier représentant un ID d'utilisateur.

### created_on
- **Signification** : l'horodatage de création de l'enregistrement.
- **Rôle** : champ technique.
- **Contenu typique** : un horodatage avec fuseau horaire indiquant quand l'enregistrement a été créé.

### last_modified_on
- **Signification** : l'horodatage de la dernière modification apportée à l'enregistrement.
- **Rôle** : champ technique.
- **Contenu typique** : un horodatage avec fuseau horaire indiquant l'heure de la dernière mise à jour.

### is_deleted
- **Signification** : indique si l'enregistrement est marqué comme supprimé.
- **Rôle** : champ technique.
- **Contenu typique** : une valeur booléenne, `false` impliquant que l'enregistrement est actif.

### sub_org_id
- **Signification** : représente une sous-organisation au sein de l'organisation principale, le cas échéant.
- **Rôle** : clé étrangère.
- **Contenu typique** : généralement `None`, ce qui indique qu'il n'est pas toujours utilisé.
```

Cette documentation offre un aperçu structuré de la table `public.document_type_attributes`, permettant aux développeurs de comprendre l'objectif et l'usage de chaque colonne.
