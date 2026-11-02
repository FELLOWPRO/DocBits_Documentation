# Données extraites du document

## Colonnes

* `id`: internal
* `org_id`: ID to organisation
* `doc_id`: internal
* `field_name`: internal
* `field_value`: internal
* `created_by`: integer
* `created_on` : horodatage avec fuseau horaire
* `last_modified_on` : horodatage avec fuseau horaire
* `is_deleted`: boolean
* `field_type`: internal

## Analyse et description

```markdown
# Documentation technique de la table `public.document_extracted_data`

## Introduction

La table `public.document_extracted_data` sert à stocker les données extraites de différents documents, vraisemblablement à des fins de traitement et d'analyse de documents. Chaque entrée de la table correspond à un champ précis extrait d'un document, par exemple une facture, et comprend des métadonnées sur le processus d'extraction. La table facilite le suivi et la gestion des données de documents en les associant à des organisations et à des documents spécifiques.

## Description des colonnes

### id
- **Signification** : un identifiant unique pour chaque entrée de données extraites.
- **Rôle** : clé primaire.
- **Contenu typique** : une chaîne au format UUID identifiant de façon unique l'enregistrement de données extraites.

### org_id
- **Signification** : l'identifiant de l'organisation associée aux données du document.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne au format UUID représentant l'organisation.

### doc_id
- **Signification** : l'identifiant du document dont les données ont été extraites.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne au format UUID représentant le document.

### field_name
- **Signification** : le nom du champ extrait du document.
- **Rôle** : champ descriptif.
- **Contenu typique** : des chaînes comme 'invoice_id', 'invoice_date', etc., indiquant le type de donnée extraite.

### field_value
- **Signification** : la valeur associée au champ extrait.
- **Rôle** : champ descriptif.
- **Contenu typique** : des chaînes représentant divers types de données, comme des numéros de facture, des dates ou des montants.

### created_by
- **Signification** : l'identifiant de l'utilisateur ou du processus qui a créé l'entrée de données.
- **Rôle** : champ technique.
- **Contenu typique** : un entier représentant un ID d'utilisateur ou de processus.

### created_on
- **Signification** : l'horodatage de création de l'entrée de données.
- **Rôle** : champ technique.
- **Contenu typique** : un horodatage avec fuseau horaire indiquant la date et l'heure de création.

### last_modified_on
- **Signification** : l'horodatage de la dernière modification apportée à l'entrée de données.
- **Rôle** : champ technique.
- **Contenu typique** : un horodatage avec fuseau horaire indiquant la date et l'heure de la dernière modification (peut être null si jamais modifié).

### is_deleted
- **Signification** : un indicateur précisant si l'entrée de données a été marquée comme supprimée.
- **Rôle** : champ technique.
- **Contenu typique** : une valeur booléenne, où `False` indique des entrées actives et `True` des entrées supprimées.

### field_type
- **Signification** : le type de données stocké dans la colonne `field_value`.
- **Rôle** : champ descriptif.
- **Contenu typique** : des chaînes comme 'date', 'AMOUNT', ou null si le type n'est pas spécifié.

Ce modèle de données structuré permet un stockage et une récupération efficaces des données liées aux documents, et prend en charge un large éventail d'applications, du traitement des factures à la gestion de la conformité.
```
