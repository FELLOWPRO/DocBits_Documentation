# Règles de validation des champs

## Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `field_id` : interne
* `doc_type` : DOC Type
* `is_sub_doc_type_field` : boolean
* `profile` : interne
* `field_name` : interne
* `field_length` : integer
* `field_label` : interne
* `is_required` : boolean
* `is_readonly` : boolean
* `is_hidden` : boolean
* `force_validation` : boolean
* `validation_pattern` : interne
* `confidence_threshold` : integer
* `match_score_threshold` : integer
* `created_by` : integer
* `created_on` : horodatage avec fuseau horaire
* `last_modified_on` : horodatage avec fuseau horaire
* `is_deleted` : boolean
* `additional_attributes` : texte

## Analyse et description

```markdown
# Documentation technique de la table `public.field_validation_rules`

## Introduction

La table `public.field_validation_rules` semble stocker les métadonnées et les règles de validation des champs associés aux différents types de documents d'une organisation. Elle sert vraisemblablement à garantir l'intégrité et la cohérence des données dans les formulaires ou les documents en précisant des exigences telles que le caractère obligatoire d'un champ, sa longueur, sa visibilité et les motifs de validation à appliquer.

## Description des colonnes

### id
- **Signification** : identifiant unique de chaque règle de validation de champ.
- **Rôle** : clé primaire.
- **Contenu typique** : une chaîne UUID qui identifie de manière unique un enregistrement.

### org_id
- **Signification** : identifiant de l'organisation à laquelle s'applique la règle de validation.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID faisant référence à une organisation précise.

### field_id
- **Signification** : identifiant du champ spécifique auquel la règle de validation est associée.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID faisant référence à un champ précis.

### doc_type
- **Signification** : précise le type de document auquel la règle de validation de champ est associée.
- **Rôle** : champ descriptif.
- **Contenu typique** : une chaîne indiquant le type de document (par ex. `PURCHASE_ORDER_FORM`).

### is_sub_doc_type_field
- **Signification** : indique si le champ fait partie d'un sous-type de document.
- **Rôle** : champ descriptif.
- **Contenu typique** : valeur booléenne (`True` ou `False`).

### profile
- **Signification** : représente le profil ou le contexte dans lequel la validation du champ est appliquée.
- **Rôle** : champ descriptif.
- **Contenu typique** : une chaîne telle que `DEFAULT`.

### field_name
- **Signification** : nom du champ pour lequel la règle de validation est définie.
- **Rôle** : champ descriptif.
- **Contenu typique** : une chaîne représentant le nom du champ (par ex. `Test`).

### field_length
- **Signification** : longueur maximale autorisée pour le contenu du champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : un entier précisant la limite de caractères.

### field_label
- **Signification** : libellé ou nom d'affichage du champ dans l'interface utilisateur.
- **Rôle** : champ descriptif.
- **Contenu typique** : généralement null dans les données d'exemple.

### is_required
- **Signification** : indique si le champ est obligatoire pour le document.
- **Rôle** : indicateur de contrainte.
- **Contenu typique** : valeur booléenne (`True` ou `False`).

### is_readonly
- **Signification** : précise si le champ est modifiable ou en lecture seule.
- **Rôle** : indicateur de contrainte.
- **Contenu typique** : valeur booléenne (`True` ou `False`).

### is_hidden
- **Signification** : indique si le champ doit être masqué dans l'interface utilisateur.
- **Rôle** : indicateur de contrainte.
- **Contenu typique** : valeur booléenne (`True` ou `False`).

### force_validation
- **Signification** : détermine si la validation doit être appliquée quelles que soient les autres conditions.
- **Rôle** : indicateur de contrainte.
- **Contenu typique** : valeur booléenne (`True` ou `False`).

### validation_pattern
- **Signification** : motif (vraisemblablement une regex) auquel le contenu du champ doit correspondre.
- **Rôle** : règle de validation.
- **Contenu typique** : généralement null dans les données d'exemple.

### confidence_threshold
- **Signification** : niveau de confiance minimal requis pour la validation du champ.
- **Rôle** : contrainte de validation.
- **Contenu typique** : une valeur entière représentant le seuil de confiance.

### match_score_threshold
- **Signification** : score de correspondance minimal requis pour valider le contenu du champ.
- **Rôle** : contrainte de validation.
- **Contenu typique** : une valeur entière représentant le seuil du score de correspondance.

### created_by
- **Signification** : identifiant de l'utilisateur qui a créé cette règle de validation.
- **Rôle** : champ descriptif.
- **Contenu typique** : un entier représentant l'ID utilisateur.

### created_on
- **Signification** : horodatage indiquant quand la règle de validation a été créée.
- **Rôle** : champ technique.
- **Contenu typique** : un horodatage avec fuseau horaire.

### last_modified_on
- **Signification** : horodatage indiquant la dernière modification de la règle de validation.
- **Rôle** : champ technique.
- **Contenu typique** : un horodatage avec fuseau horaire, peut être null si jamais modifiée.

### is_deleted
- **Signification** : indique si la règle de validation a été marquée comme supprimée.
- **Rôle** : indicateur de suppression logique.
- **Contenu typique** : valeur booléenne (`True` ou `False`).

### additional_attributes
- **Signification** : stocke des attributs ou métadonnées supplémentaires associés à la règle de validation de champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : texte, souvent null dans les données d'exemple.
```
