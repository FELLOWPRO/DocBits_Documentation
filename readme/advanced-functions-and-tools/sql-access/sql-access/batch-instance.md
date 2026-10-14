# Batch instance

## Table `public.batch_instance`

### Colonnes

* `id`: internal
* `org_id`: ID to organisation
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse et description

## Documentation de la table : `public.batch_instance`

### Introduction

La table `public.batch_instance` sert à stocker des informations sur les différentes instances de lot au sein d'une organisation. Elle contient des métadonnées clés sur chaque instance, notamment son identification unique, l'organisation à laquelle elle appartient, ainsi que les détails de sa création et de sa modification. Cette table est essentielle pour suivre le cycle de vie et la gestion des instances de lot, vraisemblablement dans une application logicielle de traitement par lots.

### Colonnes

#### `id`

* **Signification** : cette colonne stocke l'identifiant unique de chaque instance de lot.
* **Rôle** : clé primaire (`id`).
* **Contenu typique** : une chaîne UUID qui identifie chaque instance de lot de manière unique, par ex. `'e9aa9ad7-6c36-4d7c-b31c-6e10bb8fbd87'`.

#### `org_id`

* **Signification** : cette colonne stocke l'identifiant de l'organisation associée à l'instance de lot.
* **Rôle** : clé étrangère (`org_id`).
* **Contenu typique** : une chaîne UUID représentant l'organisation, par ex. `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### `created_by`

* **Signification** : cette colonne indique l'utilisateur ou l'entité système qui a créé l'instance de lot.
* **Rôle** : éventuellement une clé étrangère, référençant une table d'utilisateurs ou équivalente.
* **Contenu typique** : un entier représentant l'ID du créateur, par ex. `1`.

#### `created_on`

* **Signification** : cette colonne enregistre l'horodatage de création de l'instance de lot.
* **Rôle** : champ technique à des fins d'audit et de suivi.
* **Contenu typique** : un horodatage avec fuseau horaire, par ex. `2021-09-22 10:55:59.755627+00`.

#### `last_modified_on`

* **Signification** : cette colonne enregistre l'horodatage de la dernière modification apportée à l'instance de lot.
* **Rôle** : champ technique pour l'audit des modifications.
* **Contenu typique** : généralement null, ou un horodatage avec fuseau horaire si des modifications ont eu lieu.

#### `is_deleted`

* **Signification** : cette colonne indique si l'instance de lot est marquée comme supprimée.
* **Rôle** : champ technique pour la suppression logique.
* **Contenu typique** : une valeur booléenne, généralement `False` si l'instance est active, par ex. `False`.

Cette documentation offre un aperçu complet de la table `public.batch_instance`, en détaillant l'objectif et la structure de chaque colonne, ce qui est essentiel pour les développeurs travaillant avec ce modèle de données.
