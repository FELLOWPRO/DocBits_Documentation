# Identifiants API

## Colonnes

* `id`: internal
* `org_id`: ID to organisation
* `sub_org_id`: internal
* `title`: internal
* `credentials_type`: internal
* `credentials_json`: text
* `created_by`: integer
* `created_on` : horodatage avec fuseau horaire
* `last_modified_on` : horodatage avec fuseau horaire
* `is_deleted`: boolean
* `deleted_on` : horodatage avec fuseau horaire
* `last_modified_by`: internal
* `deleted_by`: internal

## Analyse et description

```markdown
# Documentation de la table : `public.api_credentials`

## Introduction

La table `public.api_credentials` sert à stocker et à gérer les informations d'identification d'API. Cette table est essentielle pour que les organisations gèrent de manière sécurisée leurs informations d'authentification d'API, afin que les différents services puissent interagir entre eux avec les bons identifiants. Elle contient des informations sur le type d'identifiants, l'organisation à laquelle ils appartiennent, ainsi que des métadonnées sur leur création et leur modification.

## Description des colonnes

### id
- **Signification** : un identifiant unique pour chaque entrée de la table.
- **Rôle** : clé primaire.
- **Contenu typique** : un identifiant universellement unique (UUID) représentant un ensemble spécifique d'identifiants d'API.

### org_id
- **Signification** : l'identifiant de l'organisation propriétaire des identifiants.
- **Rôle** : clé étrangère.
- **Contenu typique** : un UUID qui renvoie à l'enregistrement de l'organisation dans une autre table.

### sub_org_id
- **Signification** : l'identifiant d'une sous-organisation au sein de l'organisation principale.
- **Rôle** : clé étrangère (facultative).
- **Contenu typique** : peut contenir un UUID renvoyant à une sous-organisation, ou `None`.

### title
- **Signification** : un titre descriptif pour les identifiants d'API.
- **Rôle** : champ descriptif.
- **Contenu typique** : une chaîne telle que « supplier_auth » indiquant l'objectif ou l'usage des identifiants.

### credentials_type
- **Signification** : précise le type d'identifiants stockés.
- **Rôle** : champ descriptif.
- **Contenu typique** : une chaîne comme « ionapi » indiquant le format ou le protocole utilisé par les identifiants.

### credentials_json
- **Signification** : un objet JSON contenant les informations d'identification détaillées.
- **Rôle** : champ technique.
- **Contenu typique** : une chaîne JSON avec diverses paires clé-valeur décrivant les paramètres d'authentification.

### created_by
- **Signification** : l'ID de l'utilisateur qui a créé l'enregistrement d'identifiants.
- **Rôle** : champ technique.
- **Contenu typique** : un entier représentant l'ID de l'utilisateur.

### created_on
- **Signification** : l'horodatage indiquant quand les identifiants ont été créés.
- **Rôle** : champ technique.
- **Contenu typique** : une valeur date-heure avec fuseau horaire, par ex. `2024-04-08 11:54:55 UTC`.

### last_modified_on
- **Signification** : l'horodatage indiquant la dernière modification des identifiants.
- **Rôle** : champ technique.
- **Contenu typique** : une valeur date-heure avec fuseau horaire, ou `None` si jamais modifiés.

### is_deleted
- **Signification** : un indicateur précisant si les identifiants sont marqués comme supprimés.
- **Rôle** : champ technique.
- **Contenu typique** : une valeur booléenne, où `False` indique des identifiants actifs.

### deleted_on
- **Signification** : l'horodatage indiquant quand les identifiants ont été marqués comme supprimés.
- **Rôle** : champ technique.
- **Contenu typique** : une valeur date-heure avec fuseau horaire, ou `None` s'ils ne sont pas supprimés.

### last_modified_by
- **Signification** : l'identifiant de l'utilisateur qui a modifié les identifiants en dernier.
- **Rôle** : champ technique.
- **Contenu typique** : une chaîne de caractères représentant l'ID de l'utilisateur, ou `None`.

### deleted_by
- **Signification** : l'identifiant de l'utilisateur qui a marqué les identifiants comme supprimés.
- **Rôle** : champ technique.
- **Contenu typique** : une chaîne de caractères représentant l'ID de l'utilisateur, ou `None`.
```
