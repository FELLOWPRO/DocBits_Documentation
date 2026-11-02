# public.document\_log

## Table `public.document_log`

### Colonnes

* `id` : integer
* `org_id` : ID de l'organisation
* `doc_id` : interne
* `action_type` : interne
* `action_description` : texte
* `created_by` : integer
* `created_on` : horodatage avec fuseau horaire
* `last_modified_on` : horodatage avec fuseau horaire
* `is_deleted` : boolean
* `is_hidden` : boolean
* `previous_status` : interne
* `current_status` : interne

### Analyse et description

## Documentation technique : table `public.document_log`

### Introduction

La table `public.document_log` est conçue pour suivre l'historique et les changements de statut des documents au sein d'une organisation. Elle enregistre les actions effectuées sur les documents, comme les mises à jour de statut, ainsi que des détails sur l'utilisateur qui a effectué l'action et des horodatages indiquant quand ces actions ont eu lieu. Cette table est essentielle pour auditer les flux de traitement des documents et comprendre le cycle de vie de chaque document.

### Description des colonnes

#### id

* **Signification** : identifiant unique de chaque entrée du journal.
* **Rôle** : clé primaire. Cette colonne sert d'identifiant unique de chaque enregistrement de la table.
* **Contenu typique** : valeurs entières qui s'incrémentent à chaque nouvelle entrée.

#### org\_id

* **Signification** : identifiant de l'organisation associée au document.
* **Rôle** : clé étrangère. Renvoie à une entité d'organisation, bien que cela ne soit pas défini explicitement dans ce contexte.
* **Contenu typique** : chaînes de caractères, vraisemblablement des UUID, représentant des identifiants d'organisation.

#### doc\_id

* **Signification** : identifiant du document associé à l'entrée du journal.
* **Rôle** : clé étrangère. Cette colonne référence un document précis du système.
* **Contenu typique** : chaînes de caractères, vraisemblablement des UUID, représentant des identifiants de document.

#### action\_type

* **Signification** : type d'action consignée.
* **Rôle** : champ descriptif. Indique la catégorie de l'action effectuée.
* **Contenu typique** : chaînes telles que `STATUS_CHANGE`, indiquant la nature de l'action.

#### action\_description

* **Signification** : description détaillée de l'action effectuée.
* **Rôle** : champ descriptif. Fournit le contexte ou des détails sur l'action.
* **Contenu typique** : descriptions textuelles, par ex. « Data extraction started », « Error occurred processing document ».

#### created\_by

* **Signification** : identifiant de l'utilisateur qui a créé l'entrée du journal.
* **Rôle** : clé étrangère. Renvoie à une entité utilisateur et indique qui a effectué l'action.
* **Contenu typique** : valeurs entières représentant des identifiants d'utilisateur.

#### created\_on

* **Signification** : horodatage de la création de l'entrée du journal.
* **Rôle** : champ technique. Enregistre l'heure exacte à laquelle une action a été consignée.
* **Contenu typique** : horodatages avec information de fuseau horaire, par ex. `2025-04-01 13:07:51.291193 UTC`.

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification de l'entrée du journal.
* **Rôle** : champ technique. Indique l'heure de la dernière mise à jour de l'entrée du journal.
* **Contenu typique** : horodatages, éventuellement null si non modifiée après sa création.

#### is\_deleted

* **Signification** : indicateur précisant si l'entrée du journal est marquée comme supprimée.
* **Rôle** : champ technique. Sert à la suppression logique des entrées.
* **Contenu typique** : valeurs booléennes, `False` pour les entrées actives et `True` pour les entrées supprimées.

#### is\_hidden

* **Signification** : indicateur précisant si l'entrée du journal est masquée de l'affichage normal.
* **Rôle** : champ technique. Sert à contrôler la visibilité des entrées du journal.
* **Contenu typique** : valeurs booléennes, `False` pour les entrées visibles et `True` pour les entrées masquées.

#### previous\_status

* **Signification** : statut du document avant l'exécution de l'action.
* **Rôle** : champ descriptif. Indique l'état du document avant l'action consignée.
* **Contenu typique** : chaînes telles que `new`, `validating`, `running`, représentant des états de document.

#### current\_status

* **Signification** : statut du document après l'exécution de l'action.
* **Rôle** : champ descriptif. Indique l'état mis à jour du document à la suite de l'action.
* **Contenu typique** : chaînes telles que `running`, `ready_for_validation`, `error`, représentant des états de document.

Cette documentation offre un aperçu de la table `public.document_log`, en détaillant la finalité et la structure de chaque colonne, ce qui est essentiel pour les développeurs qui gèrent les flux de traitement des documents et assurent la traçabilité des audits.
