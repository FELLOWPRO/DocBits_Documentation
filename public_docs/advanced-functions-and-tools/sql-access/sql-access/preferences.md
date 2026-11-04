# Préférences

## Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `pref_key` : interne
* `pref_value` : texte
* `created_by` : integer
* `created_on` : horodatage avec fuseau horaire
* `last_modified_on` : horodatage avec fuseau horaire
* `deleted_on` : horodatage avec fuseau horaire
* `is_deleted` : boolean
* `user_id` : integer
* `sub_org_id` : interne

## Analyse et description

```markdown
# Documentation technique de la table `public.preferences`

## Introduction
La table `public.preferences` est conçue pour stocker les paramètres de configuration et les préférences de diverses entités organisationnelles au sein d'un système. Chaque entrée de la table représente une clé de préférence et sa valeur correspondante, associées à une organisation ou à une sous-organisation. Ces données de configuration peuvent inclure des paramètres relatifs aux numéros de TVA, à l'extraction, à l'activation de modules, etc.

## Description des colonnes

### id
- **Signification** : cette colonne stocke l'identifiant unique de chaque entrée de préférence.
- **Rôle** : clé primaire.
- **Contenu typique** : une chaîne UUID qui identifie de manière unique chaque ligne, par ex. `23f3d697-7411-4c95-981d-faf089d266be`.

### org_id
- **Signification** : cette colonne stocke l'identifiant de l'organisation à laquelle la préférence est associée.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID correspondant à une organisation, similaire à `23f3d697-7411-4c95-981d-faf089d266be`.

### pref_key
- **Signification** : cette colonne représente la clé ou le nom du paramètre de préférence.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaînes représentant des clés de configuration, comme `VAT_NUMBERS`, `TABLE_EXTRACTION_SETTING`.

### pref_value
- **Signification** : cette colonne contient la valeur de la préférence correspondant à `pref_key`.
- **Rôle** : champ descriptif.
- **Contenu typique** : varie selon `pref_key` ; par exemple des numéros de TVA séparés par des virgules ou des valeurs booléennes comme `true` ou `false`.

### created_by
- **Signification** : cette colonne indique l'ID utilisateur de la personne qui a créé l'entrée de préférence.
- **Rôle** : champ descriptif.
- **Contenu typique** : un entier représentant un ID utilisateur, par ex. `1`.

### created_on
- **Signification** : cette colonne enregistre l'horodatage de la création de la préférence.
- **Rôle** : champ technique.
- **Contenu typique** : un horodatage avec fuseau horaire, par ex. `2021-11-09 11:04:18+00`.

### last_modified_on
- **Signification** : cette colonne enregistre l'horodatage de la dernière modification de la préférence.
- **Rôle** : champ technique.
- **Contenu typique** : un horodatage avec fuseau horaire indiquant l'heure de la dernière mise à jour, comme `2023-12-04 10:10:26+00`.

### deleted_on
- **Signification** : cette colonne note l'horodatage du marquage de la préférence comme supprimée.
- **Rôle** : champ technique.
- **Contenu typique** : généralement `null`, sauf si la ligne est marquée pour suppression.

### is_deleted
- **Signification** : cette colonne indique si la préférence a été marquée comme supprimée.
- **Rôle** : champ technique.
- **Contenu typique** : une valeur booléenne, généralement `false`.

### user_id
- **Signification** : cette colonne stocke l'ID utilisateur associé à la préférence.
- **Rôle** : champ descriptif, éventuellement une clé étrangère.
- **Contenu typique** : un entier ou `null` si non applicable.

### sub_org_id
- **Signification** : cette colonne identifie la sous-organisation associée à la préférence.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID ou `null` si non applicable.

La table `public.preferences` offre un moyen souple et complet de gérer les paramètres de configuration de différentes entités organisationnelles, ce qui permet d'ajuster et de suivre les préférences de manière dynamique dans le temps.
```
