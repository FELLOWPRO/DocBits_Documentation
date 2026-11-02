# Table de recherche

## Table `public.lookup_table`

### Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `data_key` : interne
* `rec_id` : interne
* `prop_name` : interne
* `prop_value` : interne
* `created_by` : integer
* `created_on` : horodatage avec fuseau horaire
* `last_modified_on` : horodatage avec fuseau horaire
* `is_deleted` : boolean
* `prop_value_clean` : interne
* `version` : integer
* `deleted_on` : horodatage avec fuseau horaire
* `sub_org_id` : interne

### Analyse et description

## Documentation technique de `public.lookup_table`

### Introduction

La table `public.lookup_table` est conçue pour stocker des métadonnées sur diverses propriétés associées aux données de l'organisation. Elle sert vraisemblablement de magasin clé-valeur pour différents attributs liés aux clients ou à d'autres entités de l'organisation. La table enregistre des informations telles que les noms de propriétés, les valeurs et le contexte (par exemple l'organisation et la sous-organisation concernées), ainsi que des informations d'audit comme les horodatages de création et de modification.

### Description des colonnes

#### `id`

* **Signification** : identifiant unique de chaque enregistrement de la table.
* **Rôle** : clé primaire.
* **Contenu typique** : une chaîne UUID qui identifie de manière unique chaque entrée.

#### `org_id`

* **Signification** : identifiant de l'organisation à laquelle appartiennent les données.
* **Rôle** : clé étrangère, renvoyant vraisemblablement à une table d'organisations.
* **Contenu typique** : une chaîne UUID représentant l'organisation.

#### `data_key`

* **Signification** : clé représentant un jeu de données ou un contexte précis au sein de l'organisation.
* **Rôle** : identifiant contextuel servant à regrouper des propriétés liées.
* **Contenu typique** : chaîne alphanumérique indiquant une catégorie, comme `customer_amier`.

#### `rec_id`

* **Signification** : identifiant d'un enregistrement précis au sein du jeu de données.
* **Rôle** : identifiant contextuel, éventuellement une clé étrangère vers une autre table.
* **Contenu typique** : chaîne alphanumérique ou null pour les enregistrements sans identifiant précis.

#### `prop_name`

* **Signification** : nom de la propriété ou de l'attribut.
* **Rôle** : champ descriptif indiquant ce que représente la valeur de la propriété.
* **Contenu typique** : chaînes comme 'Kundennummer', 'Versandanschrift', 'Kundenname', etc.

#### `prop_value`

* **Signification** : valeur de la propriété décrite par `prop_name`.
* **Rôle** : champ descriptif contenant les données ou la valeur proprement dites.
* **Contenu typique** : chaînes ou nombres représentant la valeur de la propriété.

#### `created_by`

* **Signification** : identifiant de l'utilisateur ou du système qui a créé l'enregistrement.
* **Rôle** : champ technique à des fins d'audit.
* **Contenu typique** : entier représentant un ID utilisateur.

#### `created_on`

* **Signification** : horodatage indiquant quand l'enregistrement a été créé.
* **Rôle** : champ technique à des fins d'audit.
* **Contenu typique** : date et heure avec information de fuseau horaire.

#### `last_modified_on`

* **Signification** : horodatage indiquant la dernière modification de l'enregistrement.
* **Rôle** : champ technique à des fins d'audit.
* **Contenu typique** : date et heure avec information de fuseau horaire, éventuellement null si non modifié.

#### `is_deleted`

* **Signification** : indicateur précisant si l'enregistrement est supprimé.
* **Rôle** : champ technique indiquant une suppression logique.
* **Contenu typique** : valeur booléenne (`True` ou `False`).

#### `prop_value_clean`

* **Signification** : version nettoyée ou traitée de `prop_value`.
* **Rôle** : champ descriptif servant à stocker une valeur normalisée ou standardisée.
* **Contenu typique** : similaire à `prop_value`, éventuellement null si non applicable.

#### `version`

* **Signification** : numéro de version de l'enregistrement.
* **Rôle** : champ technique pour la gestion des versions.
* **Contenu typique** : entier représentant la version de l'enregistrement.

#### `deleted_on`

* **Signification** : horodatage indiquant quand l'enregistrement a été marqué comme supprimé.
* **Rôle** : champ technique à des fins d'audit.
* **Contenu typique** : date et heure avec information de fuseau horaire, éventuellement null si non supprimé.

#### `sub_org_id`

* **Signification** : identifiant d'une sous-organisation au sein de l'organisation principale.
* **Rôle** : clé étrangère, renvoyant éventuellement à une table de sous-organisations.
* **Contenu typique** : une chaîne UUID représentant la sous-organisation, éventuellement null si non applicable.
