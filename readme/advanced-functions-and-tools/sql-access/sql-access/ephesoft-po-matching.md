# Ephesoft PO matching

## Table `public.ephesoft_po_matching`

### Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `doc_id` : interne
* `doc_type` : DOC Type
* `ephesoft_doc_id` : interne
* `extracted_data` : texte
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean

### Analyse et description

## Documentation technique de la table `public.ephesoft_po_matching`

### Introduction

La table `public.ephesoft_po_matching` est conçue pour stocker et gérer les données relatives au rapprochement des commandes d'achat avec les documents, tels que les factures, traités par le système Ephesoft. Cette table enregistre divers détails sur les documents, leur processus d'extraction et l'état de leur rapprochement avec les commandes d'achat.

### Description des colonnes

#### id

* **Signification** : identifiant unique de chaque enregistrement de la table, représentant vraisemblablement un document ou une transaction traité.
* **Rôle** : clé primaire.
* **Contenu typique** : identifiant universel unique (UUID) au format chaîne, par ex. `ea587c89-0d4f-4a47-a3ac-89cfb2bed9cb`.

#### org\_id

* **Signification** : identifiant de l'organisation associée au document ou à la transaction.
* **Rôle** : clé étrangère, pouvant renvoyer à une table d'organisations.
* **Contenu typique** : UUID au format chaîne, par ex. `23f3d697-7411-4c95-981d-faf089d266be`.

#### doc\_id

* **Signification** : identifiant du document traité par le système.
* **Rôle** : clé étrangère, renvoyant à une table de documents ou équivalente.
* **Contenu typique** : UUID au format chaîne, par ex. `f46c6c90-568b-42ee-ae71-c5a3c22211de`.

#### doc\_type

* **Signification** : type du document traité, indiquant la nature du document (par ex. INVOICE).
* **Rôle** : champ descriptif.
* **Contenu typique** : chaîne indiquant le type de document, par ex. `INVOICE`.

#### ephesoft\_doc\_id

* **Signification** : identifiant utilisé par le système Ephesoft pour suivre le document.
* **Rôle** : champ descriptif.
* **Contenu typique** : chaîne courte, éventuellement un identifiant, par ex. `DOC1`.

#### extracted\_data

* **Signification** : données JSON contenant les informations extraites du document, y compris les champs, les tableaux et les métadonnées.
* **Rôle** : champ de stockage du contenu extrait du document.
* **Contenu typique** : structure JSON avec des détails comme le type de document, les champs, les tableaux et les métadonnées.

#### created\_by

* **Signification** : identifiant de l'utilisateur ou du système qui a créé l'enregistrement.
* **Rôle** : clé étrangère, pouvant renvoyer à une table d'utilisateurs.
* **Contenu typique** : entier représentant l'ID utilisateur, par ex. `1`.

#### created\_on

* **Signification** : horodatage de la création de l'enregistrement.
* **Rôle** : champ technique de suivi de l'enregistrement.
* **Contenu typique** : horodatage avec fuseau horaire, par ex. `2022-02-19 10:43:37 UTC`.

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification de l'enregistrement.
* **Rôle** : champ technique de suivi de l'enregistrement.
* **Contenu typique** : horodatage avec fuseau horaire, peut être null si non modifié depuis la création.

#### is\_deleted

* **Signification** : indicateur précisant si l'enregistrement est marqué comme supprimé.
* **Rôle** : champ technique pour la suppression logique.
* **Contenu typique** : booléen, `true` si l'enregistrement est supprimé, `false` sinon.
