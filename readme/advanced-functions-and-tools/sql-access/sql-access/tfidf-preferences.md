# Tfidf preferences

## Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `tfidf_id` : interne
* `pref_key` : interne
* `pref_value` : text
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_by` : interne
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean
* `deleted_by` : interne
* `deleted_on` : timestamp with time zone
* `supplier_id` : interne

## Analyse et description

```markdown
# Documentation technique de la table `public.tfidf_preferences`

## Introduction

La table `public.tfidf_preferences` semble conçue pour stocker les préférences liées aux configurations ou aux modèles TF-IDF (Term Frequency-Inverse Document Frequency). Cette table contient des informations sur des préférences définies par les organisations, notamment les clés de préférence et leurs valeurs correspondantes, ainsi que des métadonnées sur les actions de création, de modification et de suppression.

## Description des colonnes

### id
- **Signification** : identifiant unique de chaque enregistrement de la table.
- **Rôle** : clé primaire.
- **Contenu typique** : une chaîne UUID représentant l'ID unique d'une entrée de préférence.

### org_id
- **Signification** : identifiant de l'organisation associée à la préférence.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID qui relie la préférence à une organisation donnée.

### tfidf_id
- **Signification** : identifiant de la configuration ou du modèle TF-IDF concerné.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID représentant la configuration TF-IDF liée.

### pref_key
- **Signification** : clé ou nom du paramètre de préférence.
- **Rôle** : champ descriptif.
- **Contenu typique** : une chaîne représentant le nom de la préférence, par exemple « USE_ETEXT_IF_AVAILABLE » ou « AI_MODEL ».

### pref_value
- **Signification** : valeur associée à la clé de préférence.
- **Rôle** : champ descriptif.
- **Contenu typique** : une chaîne ou un texte correspondant à la clé de préférence, par ex. « true », « false » ou « Full ».

### created_by
- **Signification** : identifiant de l'utilisateur qui a créé l'entrée de préférence.
- **Rôle** : champ descriptif.
- **Contenu typique** : un entier représentant l'ID d'utilisateur du créateur.

### created_on
- **Signification** : horodatage de la création de l'entrée de préférence.
- **Rôle** : champ technique.
- **Contenu typique** : un horodatage avec fuseau horaire indiquant la date et l'heure de création.

### last_modified_by
- **Signification** : identifiant de l'utilisateur qui a modifié l'entrée de préférence en dernier.
- **Rôle** : champ descriptif.
- **Contenu typique** : un UUID représentant l'ID d'utilisateur de la dernière personne ayant modifié l'entrée, le cas échéant.

### last_modified_on
- **Signification** : horodatage de la dernière modification de l'entrée de préférence.
- **Rôle** : champ technique.
- **Contenu typique** : un horodatage avec fuseau horaire indiquant la date et l'heure de la dernière modification.

### is_deleted
- **Signification** : indicateur précisant si l'entrée de préférence a été marquée comme supprimée.
- **Rôle** : champ technique.
- **Contenu typique** : une valeur booléenne ; `True` si l'entrée est supprimée, sinon `False`.

### deleted_by
- **Signification** : identifiant de l'utilisateur qui a marqué l'entrée de préférence comme supprimée.
- **Rôle** : champ descriptif.
- **Contenu typique** : un UUID représentant l'ID d'utilisateur de la personne ayant supprimé l'entrée, le cas échéant.

### deleted_on
- **Signification** : horodatage du moment où l'entrée de préférence a été marquée comme supprimée.
- **Rôle** : champ technique.
- **Contenu typique** : un horodatage avec fuseau horaire indiquant quand l'entrée a été supprimée.

### supplier_id
- **Signification** : identifiant du fournisseur associé à la préférence.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID représentant le fournisseur lié à la préférence.

Cette documentation offre un aperçu détaillé de l'objectif et de la structure de la table `public.tfidf_preferences`, afin d'aider les développeurs à comprendre comment interagir avec ces données et les utiliser efficacement.
```
