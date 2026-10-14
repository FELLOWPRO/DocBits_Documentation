# Organisation document type

## Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `document_type_id` : interne
* `document_type_key` : interne
* `document_locale` : interne
* `classification_method` : interne
* `is_active` : boolean
* `extraction_type` : interne
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean
* `sub_org_id` : interne

## Analyse et description

```markdown
# Documentation technique de la table `public.organisation_document_type`

## Introduction

La table `public.organisation_document_type` est conçue pour gérer et stocker des informations sur les différents types de documents associés aux organisations. Elle comprend des détails tels que la clé du type de document, les paramètres régionaux, les méthodes de classification et l'état du type de document (actif, supprimé, etc.). Elle semble servir de table de correspondance entre les organisations et les types de documents qu'elles utilisent ou gèrent, avec des métadonnées sur ces documents.

## Description des colonnes

### id
- **Signification** : identifiant unique de chaque enregistrement de la table.
- **Rôle** : clé primaire.
- **Contenu typique** : une chaîne UUID qui identifie de manière unique une entrée de type de document.
- **Remarque** : indispensable pour distinguer chaque enregistrement.

### org_id
- **Signification** : identifiant de l'organisation liée au type de document.
- **Rôle** : clé étrangère, référençant vraisemblablement une table d'organisations.
- **Contenu typique** : une chaîne UUID.
- **Remarque** : relie le type de document à une organisation précise.

### document_type_id
- **Signification** : identifiant du type de document.
- **Rôle** : clé étrangère, éventuellement liée à une table de référence des types de documents.
- **Contenu typique** : une chaîne UUID.
- **Remarque** : permet la correspondance avec des types de documents précis.

### document_type_key
- **Signification** : clé ou code représentant le type de document.
- **Rôle** : champ descriptif pour la classification du type de document.
- **Contenu typique** : une chaîne qui sert d'identifiant ou de libellé du type de document.
- **Remarque** : sert à identifier le type de document sous une forme lisible.

### document_locale
- **Signification** : paramètre régional ou de langue du type de document.
- **Rôle** : champ descriptif pour la spécification des paramètres régionaux.
- **Contenu typique** : une chaîne, souvent 'auto', indiquant une détermination automatique des paramètres régionaux.
- **Remarque** : utile pour l'internationalisation et la localisation.

### classification_method
- **Signification** : méthode utilisée pour classer le type de document.
- **Rôle** : champ descriptif indiquant comment le document est classé.
- **Contenu typique** : une chaîne, souvent 'auto', suggérant une classification automatique.
- **Remarque** : important pour comprendre le processus de classification.

### is_active
- **Signification** : état indiquant si le type de document est actif.
- **Rôle** : champ d'état booléen.
- **Contenu typique** : `True` ou `False`.
- **Remarque** : détermine si le type de document est actuellement utilisé.

### extraction_type
- **Signification** : type de méthode d'extraction utilisé pour le document.
- **Rôle** : champ descriptif du processus d'extraction.
- **Contenu typique** : chaînes comme 'FIX_COORDINATES', 'FLEX_COORDINATES' ou `None`.
- **Remarque** : donne un aperçu de la manière dont les données sont extraites des documents.

### created_by
- **Signification** : identifiant de l'utilisateur qui a créé l'enregistrement.
- **Rôle** : champ technique à des fins d'audit.
- **Contenu typique** : un entier représentant un ID utilisateur.
- **Remarque** : utile pour le suivi des modifications et la traçabilité des responsabilités.

### created_on
- **Signification** : horodatage de la création de l'enregistrement.
- **Rôle** : champ technique à des fins d'audit.
- **Contenu typique** : un horodatage avec fuseau horaire.
- **Remarque** : important pour suivre la date et l'heure de création de l'enregistrement.

### last_modified_on
- **Signification** : horodatage de la dernière modification de l'enregistrement.
- **Rôle** : champ technique à des fins d'audit.
- **Contenu typique** : un horodatage avec fuseau horaire.
- **Remarque** : utile pour suivre les mises à jour et les changements de l'enregistrement.

### is_deleted
- **Signification** : état indiquant si l'enregistrement a été marqué comme supprimé.
- **Rôle** : champ d'état booléen.
- **Contenu typique** : `True` ou `False`.
- **Remarque** : aide à mettre en œuvre la suppression logique.

### sub_org_id
- **Signification** : identifiant d'une sous-organisation liée au type de document.
- **Rôle** : clé étrangère possible, qui ajoute une structure hiérarchique d'organisation.
- **Contenu typique** : une chaîne UUID ou `None`.
- **Remarque** : apporte un contexte supplémentaire sur la structure de l'organisation.

```
