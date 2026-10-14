# Sub document type

## Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `doc_type_key` : interne
* `sub_doc_type_key` : interne
* `name` : interne
* `title` : interne
* `translation_key` : interne
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean

## Analyse et description

```markdown
# Table `public.sub_document_type`

## Introduction

La table `sub_document_type` est conçue pour stocker des informations détaillées sur les différents sous-types de documents au sein d'une organisation. Elle comprend des identifiants uniques, des associations organisationnelles, des noms descriptifs et des métadonnées relatives à la création et à la modification de ces sous-types de documents. La table conserve également l'état de suppression logique des enregistrements.

## Description des colonnes

### id
- **Signification** : cette colonne stocke l'identifiant unique de chaque sous-type de document.
- **Rôle** : clé primaire.
- **Contenu typique** : une chaîne UUID qui identifie de manière unique un enregistrement de sous-type de document (par ex. `'c2cc2d62-e4be-491b-a43e-c4123dff5aa6'`).

### org_id
- **Signification** : cette colonne indique l'organisation à laquelle appartient le sous-type de document.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID qui référence une organisation (par ex. `'23f3d697-7411-4c95-981d-faf089d266be'`).

### doc_type_key
- **Signification** : représente la clé du type de document associé au sous-type de document.
- **Rôle** : clé étrangère (implicite d'après la convention de nommage).
- **Contenu typique** : une clé sous forme de chaîne qui renvoie à un type de document plus général (par ex. `'TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### sub_doc_type_key
- **Signification** : désigne une clé spécifique du sous-type de document au sein d'une catégorie de documents.
- **Rôle** : identifiant unique du sous-type de document dans le périmètre d'un type de document.
- **Contenu typique** : une clé sous forme de chaîne qui identifie de manière unique un sous-type de document (par ex. `'TEST_SUB_TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### name
- **Signification** : stocke un nom court ou un code du sous-type de document.
- **Rôle** : descriptif.
- **Contenu typique** : un identifiant ou code concis (par ex. `'TEST_SUB_TEST'`).

### title
- **Signification** : contient un titre lisible du sous-type de document.
- **Rôle** : descriptif.
- **Contenu typique** : un titre descriptif pour les interfaces utilisateur ou les rapports (par ex. `'Test Sub Test'`).

### translation_key
- **Signification** : clé utilisée pour l'internationalisation et la localisation afin de traduire le nom du sous-type de document.
- **Rôle** : technique.
- **Contenu typique** : une chaîne utilisée dans les fichiers de traduction (par ex. `'test_sub_test'`).

### created_by
- **Signification** : identifie l'utilisateur qui a créé l'entrée de sous-type de document.
- **Rôle** : technique.
- **Contenu typique** : un entier représentant l'ID utilisateur (par ex. `8`).

### created_on
- **Signification** : horodatage indiquant quand le sous-type de document a été créé.
- **Rôle** : technique.
- **Contenu typique** : un horodatage avec fuseau horaire (par ex. `2022-12-13 08:34:13.932893+00:00`).

### last_modified_on
- **Signification** : horodatage indiquant quand le sous-type de document a été modifié en dernier.
- **Rôle** : technique.
- **Contenu typique** : un horodatage avec fuseau horaire, éventuellement `None` si jamais modifié après sa création.

### is_deleted
- **Signification** : indicateur booléen précisant si le sous-type de document a fait l'objet d'une suppression logique.
- **Rôle** : technique.
- **Contenu typique** : `True` ou `False` indiquant l'état de suppression (par ex. `False`).
```
