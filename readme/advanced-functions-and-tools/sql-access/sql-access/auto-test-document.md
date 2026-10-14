# Auto test document

## Colonnes

* `id`: internal
* `org_id`: ID to organisation
* `doc_id`: internal
* `doc_type`: DOC Type
* `extracted_data`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `filename`: internal

## Analyse et description

```markdown
# Documentation de la table : `public.auto_test_document`

## Introduction

La table `public.auto_test_document` sert à stocker les métadonnées et les résultats d'extraction issus du traitement de documents au sein d'une organisation. La table enregistre des informations sur les documents, leurs types et les données qui en sont extraites. Elle comprend des champs d'identification des documents, des métadonnées de traitement et des indicateurs d'état, essentiels pour gérer les workflows documentaires et garantir l'intégrité des données.

## Description des colonnes

### id
- **Signification** : identifiant unique de chaque entrée de document dans la table.
- **Rôle** : clé primaire.
- **Contenu typique** : chaîne UUID.
- **Remarque** : sert d'identifiant unique pour les enregistrements, garantissant que chaque entrée est distincte.

### org_id
- **Signification** : identifiant de l'organisation associée au document.
- **Rôle** : clé étrangère.
- **Contenu typique** : chaîne UUID.
- **Remarque** : relie le document à une organisation précise du système.

### doc_id
- **Signification** : identifiant du document en cours de traitement.
- **Rôle** : clé étrangère.
- **Contenu typique** : chaîne UUID.
- **Remarque** : sert à associer les données extraites au document d'origine.

### doc_type
- **Signification** : type ou catégorie du document.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaîne telle que « MEDI_ORDER ».
- **Remarque** : aide à catégoriser les documents pour le traitement et l'analyse.

### extracted_data
- **Signification** : structure JSON contenant les données détaillées extraites du document.
- **Rôle** : champ de données.
- **Contenu typique** : texte JSON avec des champs, des valeurs et des métadonnées d'extraction.
- **Remarque** : stocke les résultats du processus d'extraction de données du document.

### created_by
- **Signification** : identifiant de l'utilisateur qui a créé l'enregistrement du document.
- **Rôle** : champ descriptif.
- **Contenu typique** : entier représentant un ID d'utilisateur.
- **Remarque** : permet de savoir quel utilisateur a initié l'entrée du document dans le système.

### created_on
- **Signification** : horodatage indiquant quand l'enregistrement du document a été créé.
- **Rôle** : champ technique.
- **Contenu typique** : date et heure avec information de fuseau horaire.
- **Remarque** : utile pour l'audit et le suivi du cycle de vie du document.

### last_modified_on
- **Signification** : horodatage indiquant la dernière modification apportée à l'enregistrement du document.
- **Rôle** : champ technique.
- **Contenu typique** : date et heure avec information de fuseau horaire.
- **Remarque** : aide à suivre les changements et mises à jour de l'enregistrement du document.

### is_deleted
- **Signification** : indicateur précisant si l'enregistrement du document a été marqué comme supprimé.
- **Rôle** : champ d'état.
- **Contenu typique** : valeur booléenne.
- **Remarque** : facilite la suppression logique des enregistrements, ce qui permet une récupération si nécessaire.

### filename
- **Signification** : nom du fichier associé au document.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaîne, par ex. « 7.pdf ».
- **Remarque** : fournit une référence au fichier physique associé à l'entrée du document.

```
