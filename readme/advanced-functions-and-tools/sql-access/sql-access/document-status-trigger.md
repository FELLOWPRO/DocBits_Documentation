# Document status trigger

## Table `public.document_status_trigger`

### Colonnes

* `id`: internal
* `org_id`: ID to organisation
* `trigger_doc_type`: internal
* `trigger_doc_status`: internal
* `trigger_url`: internal
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse et description

## Documentation technique de la table `public.document_status_trigger`

### Introduction

La table `public.document_status_trigger` sert à gérer et à suivre le statut des documents au sein d'une organisation. Cette table semble gérer les déclencheurs liés au traitement des documents, vraisemblablement dans un système de workflow. Elle enregistre des informations sur les types de documents et leurs changements de statut, pouvant déclencher des actions ou des workflows via des URL spécifiées.

### Description des colonnes

#### id

* **Signification** : cette colonne stocke un identifiant unique pour chaque enregistrement de la table.
* **Rôle** : clé primaire.
* **Contenu typique** : une chaîne UUID, par ex. `8103b700-c03c-40cb-9322-e9e1ddbe0cb1`.

#### org\_id

* **Signification** : représente l'identifiant unique d'une organisation.
* **Rôle** : clé étrangère, reliée à une entité organisation.
* **Contenu typique** : une chaîne UUID, par ex. `23f3d697-7411-4c95-981d-faf089d266be`.

#### trigger\_doc\_type

* **Signification** : précise le type de document associé au déclencheur.
* **Rôle** : champ descriptif indiquant le type de document.
* **Contenu typique** : des noms de types de documents, tels que `INVOICE`.

#### trigger\_doc\_status

* **Signification** : désigne le statut précis du document qui active le déclencheur.
* **Rôle** : champ descriptif détaillant le statut du document.
* **Contenu typique** : des descriptions de statut, comme `approved_pending_second_approval`.

#### trigger\_url

* **Signification** : URL appelée lorsque le statut du document remplit certaines conditions.
* **Rôle** : champ technique pour l'automatisation des workflows.
* **Contenu typique** : des URL, par ex. `https://test-wf-stage.workflow.polydocs.io/webhook/3c3ab41b-a1d9-40a9-8e33-2968d33c989e/webhook`.

#### is\_active

* **Signification** : indique si le déclencheur est actuellement actif.
* **Rôle** : champ technique pour gérer les états des déclencheurs.
* **Contenu typique** : des valeurs booléennes, `True` ou `False`.

#### created\_by

* **Signification** : identifie l'utilisateur qui a créé l'enregistrement.
* **Rôle** : clé étrangère vers une entité utilisateur.
* **Contenu typique** : des ID d'utilisateur entiers, par ex. `1`.

#### created\_on

* **Signification** : horodatage de création de l'enregistrement.
* **Rôle** : champ technique pour l'audit et le suivi des modifications.
* **Contenu typique** : des horodatages avec fuseau horaire, par ex. `2022-09-16 07:26:55 UTC`.

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification de l'enregistrement.
* **Rôle** : champ technique pour l'audit et le suivi des modifications.
* **Contenu typique** : des horodatages avec fuseau horaire, peut être `None` si non modifié.

#### is\_deleted

* **Signification** : indique si l'enregistrement est considéré comme supprimé ou inactif.
* **Rôle** : champ technique pour la suppression logique.
* **Contenu typique** : des valeurs booléennes, `True` ou `False`.

Cette table offre une approche structurée de la gestion des statuts de documents et des déclencheurs associés dans le système de workflow d'une organisation, garantissant que des actions peuvent être exécutées automatiquement à mesure que les documents progressent dans leurs différents états.
