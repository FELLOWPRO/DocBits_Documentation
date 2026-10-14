# Lookup field configuration

## Table `public.lookup_field_configuration`

### Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `lookup_rec_id` : interne
* `field_id` : interne
* `lookup_field` : interne
* `is_searchable` : boolean
* `parent_field_id` : interne
* `auto_trigger` : boolean
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean
* `deleted_on` : timestamp with time zone
* `search_operator` : interne
* `last_modified_by` : interne
* `deleted_by` : interne

### Analyse et description

## Documentation de la table `public.lookup_field_configuration`

### Introduction

La table `public.lookup_field_configuration` semble être une table de configuration servant à définir et à gérer les champs de lookup au sein d'une application. Elle contient des métadonnées sur chaque champ, comme son identifiant, l'organisation associée, sa capacité de recherche et des informations d'audit. Cette table fait vraisemblablement partie d'un système plus vaste de gestion de champs dynamiques ou définis par l'utilisateur, qui permet des requêtes et des configurations complexes.

### Description des colonnes

#### `id`

* **Signification** : identifiant unique de chaque enregistrement de la table.
* **Rôle** : clé primaire.
* **Contenu typique** : une chaîne UUID qui identifie de manière unique chaque entrée de configuration.

#### `org_id`

* **Signification** : identifiant de l'organisation à laquelle cette configuration est associée.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne UUID représentant l'organisation.

#### `lookup_rec_id`

* **Signification** : identifiant de l'enregistrement de lookup précis auquel cette configuration s'applique.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne UUID faisant référence à un enregistrement de lookup précis.

#### `field_id`

* **Signification** : identifiant du champ en cours de configuration.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne UUID faisant référence à un champ particulier.

#### `lookup_field`

* **Signification** : nom ou libellé du champ en cours de configuration.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne représentant le nom du champ, comme "address\_1" ou "taxratefree".

#### `is_searchable`

* **Signification** : indique si le champ peut être inclus dans les opérations de recherche.
* **Rôle** : indicateur de configuration.
* **Contenu typique** : une valeur booléenne (`True` ou `False`).

#### `parent_field_id`

* **Signification** : identifiant du champ parent, le cas échéant.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne UUID ou `None` s'il n'existe aucun champ parent.

#### `auto_trigger`

* **Signification** : précise si la configuration du champ doit déclencher automatiquement certaines actions.
* **Rôle** : indicateur de configuration.
* **Contenu typique** : une valeur booléenne (`True` ou `False`).

#### `created_by`

* **Signification** : identifiant de l'utilisateur qui a créé l'entrée de configuration.
* **Rôle** : champ d'audit.
* **Contenu typique** : un entier représentant l'ID utilisateur.

#### `created_on`

* **Signification** : horodatage de la création de l'entrée de configuration.
* **Rôle** : champ d'audit.
* **Contenu typique** : un horodatage avec information de fuseau horaire.

#### `last_modified_on`

* **Signification** : horodatage de la modification la plus récente de l'entrée de configuration.
* **Rôle** : champ d'audit.
* **Contenu typique** : un horodatage avec information de fuseau horaire, ou `None` si jamais modifiée.

#### `is_deleted`

* **Signification** : indique si l'entrée de configuration a été marquée comme supprimée.
* **Rôle** : indicateur de suppression logique.
* **Contenu typique** : une valeur booléenne (`True` ou `False`).

#### `deleted_on`

* **Signification** : horodatage du marquage de l'entrée de configuration comme supprimée.
* **Rôle** : champ d'audit.
* **Contenu typique** : un horodatage avec information de fuseau horaire, ou `None` si non supprimée.

#### `search_operator`

* **Signification** : définit l'opérateur de recherche utilisé pour le champ.
* **Rôle** : champ de configuration.
* **Contenu typique** : une chaîne telle que "contains" indiquant le type d'opération de recherche.

#### `last_modified_by`

* **Signification** : identifiant de l'utilisateur qui a modifié l'entrée de configuration en dernier.
* **Rôle** : champ d'audit.
* **Contenu typique** : une chaîne UUID ou `None` si jamais modifiée.

#### `deleted_by`

* **Signification** : identifiant de l'utilisateur qui a marqué l'entrée comme supprimée.
* **Rôle** : champ d'audit.
* **Contenu typique** : une chaîne UUID ou `None` si non supprimée.

Cette documentation offre une vue détaillée de la structure et de la finalité de chaque colonne de la table `public.lookup_field_configuration` et donne aux développeurs une compréhension complète de la manière dont les champs de lookup sont configurés et gérés dans le système.
