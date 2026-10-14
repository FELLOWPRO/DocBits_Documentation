# Document Script activation status

## Table `public.document_script_activation_status`

### Colonnes

* `id`: internal
* `org_id`: ID to organisation
* `sort_order`: integer
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `script_id`: internal

### Analyse et description

## Documentation de la table : `public.document_script_activation_status`

### Introduction

La table `public.document_script_activation_status` sert à gérer l'état d'activation des scripts associés aux documents au sein d'une organisation. Chaque entrée de la table correspond à un script précis et à son état d'activation actuel, ce qui permet potentiellement aux organisations de contrôler et d'organiser l'exécution des scripts en lien avec leurs documents.

### Description des colonnes

#### id

* **Signification** : cette colonne stocke un identifiant unique pour chaque entrée de la table.
* **Rôle** : clé primaire.
* **Contenu typique** : un identifiant universellement unique (UUID) tel que `c599a3fa-a784-446a-a48e-cf37b95d93cd`.
* **Remarque** : garantit que chaque enregistrement est identifiable de manière unique.

#### org\_id

* **Signification** : représente l'identifiant d'une organisation.
* **Rôle** : clé étrangère, référençant vraisemblablement une table d'organisations.
* **Contenu typique** : un UUID qui identifie l'organisation, par ex. `23f3d697-7411-4c95-981d-faf089d266be`.
* **Remarque** : relie l'état d'activation du script à une organisation précise.

#### sort\_order

* **Signification** : indique l'ordre dans lequel les scripts doivent être exécutés ou affichés.
* **Rôle** : champ technique.
* **Contenu typique** : des valeurs entières représentant la séquence, comme `0`.
* **Remarque** : peut servir à prioriser ou à organiser les scripts.

#### is\_active

* **Signification** : indique si un script est actuellement actif.
* **Rôle** : champ technique.
* **Contenu typique** : des valeurs booléennes, `True` ou `False`.
* **Remarque** : détermine si le script associé doit être exécuté.

#### created\_by

* **Signification** : identifiant de l'utilisateur qui a créé l'enregistrement.
* **Rôle** : clé étrangère, référençant vraisemblablement une table d'utilisateurs.
* **Contenu typique** : une valeur entière représentant un ID d'utilisateur, comme `1`.
* **Remarque** : permet de suivre le créateur de l'enregistrement à des fins d'audit.

#### created\_on

* **Signification** : horodatage de création de l'enregistrement.
* **Rôle** : champ technique.
* **Contenu typique** : date et heure avec fuseau horaire, par ex. `2023-11-20 10:44:14.685170+00:00`.
* **Remarque** : fournit un horodatage de création pour la tenue des enregistrements.

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification de l'enregistrement.
* **Rôle** : champ technique.
* **Contenu typique** : date et heure avec fuseau horaire, ou `None` si jamais modifié.
* **Remarque** : utile pour suivre les changements au fil du temps.

#### is\_deleted

* **Signification** : indique si l'enregistrement est marqué comme supprimé.
* **Rôle** : champ technique.
* **Contenu typique** : des valeurs booléennes, `True` ou `False`.
* **Remarque** : permet la suppression logique des enregistrements sans suppression physique de la base de données.

#### script\_id

* **Signification** : identifiant du script associé à l'enregistrement.
* **Rôle** : clé étrangère, référençant vraisemblablement une table de scripts.
* **Contenu typique** : un UUID qui identifie le script, par ex. `4edc8cd7-e1bc-443a-9a23-dc490a09e80b`.
* **Remarque** : relie l'état d'activation à un script précis.
