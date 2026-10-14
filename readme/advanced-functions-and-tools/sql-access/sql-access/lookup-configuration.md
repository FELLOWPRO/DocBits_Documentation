# Lookup Configuration

## Table `public.lookup_configuration`

### Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `doc_type` : DOC Type
* `lookup_dataset_name` : interne
* `lookup_name` : interne
* `conflict_handle` : interne
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean
* `deleted_on` : timestamp with time zone
* `match_all` : boolean
* `last_modified_by` : interne
* `deleted_by` : interne
* `context` : interne
* `context_detail` : interne

### Analyse et description

## Documentation technique de la table `public.lookup_configuration`

### Introduction

La table `public.lookup_configuration` est conçue pour stocker les paramètres de configuration de diverses opérations de recherche de données (lookup) au sein d'une organisation. Elle contient des informations sur l'organisation, le type de documents concernés ainsi que les jeux de données et les noms utilisés pour les recherches. La table suit également la création et la modification de ces configurations, ainsi que leur état actuel (active ou supprimée).

### Description des colonnes

#### id

* **Signification** : identifiant unique de chaque entrée de configuration de lookup dans la table.
* **Rôle** : clé primaire qui identifie chaque ligne de manière unique.
* **Contenu typique** : valeurs UUID, par ex. `'68454d10-e045-4d64-8dd3-774bcb5b6013'`.

#### org\_id

* **Signification** : représente l'organisation associée à la configuration de lookup.
* **Rôle** : clé étrangère, renvoyant à une organisation dans une autre table.
* **Contenu typique** : valeurs UUID indiquant des identifiants d'organisation, par ex. `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### doc\_type

* **Signification** : précise le type de document auquel s'applique la configuration de lookup.
* **Rôle** : champ descriptif indiquant le contexte de la configuration.
* **Contenu typique** : chaînes comme `'MEDI_ORDER'`, `'INVOICE'`, etc.

#### lookup\_dataset\_name

* **Signification** : nom du jeu de données utilisé pour effectuer les recherches.
* **Rôle** : champ descriptif servant à identifier les jeux de données.
* **Contenu typique** : chaînes descriptives telles que `'customer_tini'`, `'supplier'`.

#### lookup\_name

* **Signification** : nom spécifique ou alias utilisé pour l'opération de lookup.
* **Rôle** : champ descriptif indiquant le nom opérationnel.
* **Contenu typique** : chaînes comme `'customer_tini'`, `'supplier (copy)'`.

#### conflict\_handle

* **Signification** : indique la stratégie de gestion des conflits lors des recherches.
* **Rôle** : champ descriptif de la stratégie de résolution des conflits.
* **Contenu typique** : valeurs telles que `'BEST_SCORE'`, `'RETURN_NONE'`.

#### created\_by

* **Signification** : ID de l'utilisateur qui a créé la configuration de lookup.
* **Rôle** : champ technique pour suivre le créateur de l'entrée.
* **Contenu typique** : valeurs entières représentant des ID utilisateur, par ex. `1`.

#### created\_on

* **Signification** : horodatage de la création de la configuration de lookup.
* **Rôle** : champ technique pour suivre l'heure de création.
* **Contenu typique** : horodatages, par ex. `2024-02-08 11:24:14 UTC`.

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification apportée à la configuration de lookup.
* **Rôle** : champ technique pour suivre l'heure de la dernière mise à jour.
* **Contenu typique** : horodatages, généralement `None` si non modifiée.

#### is\_deleted

* **Signification** : indique si la configuration de lookup a été marquée comme supprimée.
* **Rôle** : champ booléen de suivi de l'état.
* **Contenu typique** : valeurs booléennes, `False` pour les entrées actives.

#### deleted\_on

* **Signification** : horodatage du marquage de la configuration de lookup comme supprimée.
* **Rôle** : champ technique pour suivre l'heure de suppression.
* **Contenu typique** : souvent une date de remplacement par défaut, par ex. `0002-01-01 11:00:00 UTC`.

#### match\_all

* **Signification** : précise si le lookup doit satisfaire toutes les conditions.
* **Rôle** : champ booléen pour les paramètres de configuration.
* **Contenu typique** : valeurs booléennes, généralement `False`.

#### last\_modified\_by

* **Signification** : ID de l'utilisateur qui a modifié la configuration de lookup en dernier.
* **Rôle** : champ technique pour suivre l'utilisateur ayant effectué la dernière mise à jour de l'entrée.
* **Contenu typique** : UUID ou identifiant de l'utilisateur ayant effectué la modification, souvent `None`.

#### deleted\_by

* **Signification** : ID de l'utilisateur qui a marqué la configuration de lookup comme supprimée.
* **Rôle** : champ technique pour suivre l'utilisateur responsable de la suppression.
* **Contenu typique** : UUID ou identifiant, souvent `None`.

#### context

* **Signification** : contexte dans lequel le lookup est appliqué, par exemple une section d'un document.
* **Rôle** : champ descriptif du contexte opérationnel.
* **Contenu typique** : chaînes comme `'header'`.

#### context\_detail

* **Signification** : détails supplémentaires sur le contexte du lookup.
* **Rôle** : champ descriptif pour des informations de contexte étendues.
* **Contenu typique** : souvent `None`, utilisé pour une description de contexte supplémentaire.
