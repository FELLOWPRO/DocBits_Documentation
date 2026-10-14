# Document Import log

## Colonnes

* `id`: integer
* `org_id`: ID to organisation
* `sub_org_id`: internal
* `original_filename`: internal
* `filename`: internal
* `imported_on`: internal
* `source_type`: internal
* `source`: internal
* `success`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `import_id`: text
* `extra_data`: text
* `doc_id`: internal
* `email_connection_id`: integer
* `subject`: internal
* `body`: text
* `sender`: internal
* `error_resp`: internal
* `source_received_on`: timestamp with time zone

## Analyse et description

```markdown
# Documentation technique de la table `public.document_import_log`

## Introduction

La table `public.document_import_log` sert à consigner les détails des imports de documents dans le système. Elle enregistre des informations sur chaque document, notamment son origine, l'état de l'import et les métadonnées associées. Cette table est essentielle pour suivre les activités d'import de documents et diagnostiquer les problèmes qui peuvent survenir pendant le processus d'import.

## Description des colonnes

### id
- **Signification** : un identifiant unique pour chaque entrée du journal d'import.
- **Rôle** : clé primaire
- **Contenu typique** : des valeurs entières séquentielles qui identifient chaque enregistrement de manière unique.

### org_id
- **Signification** : l'identifiant de l'organisation associée à l'import.
- **Rôle** : clé étrangère
- **Contenu typique** : un UUID ou un identifiant de chaîne unique similaire représentant l'organisation.

### sub_org_id
- **Signification** : l'identifiant d'une sous-organisation ou d'un département au sein de l'organisation principale.
- **Rôle** : clé étrangère
- **Contenu typique** : un UUID ou un identifiant de chaîne unique similaire ; peut être `None` si non applicable.

### original_filename
- **Signification** : le nom d'origine du fichier du document tel qu'il a été téléversé.
- **Rôle** : champ descriptif
- **Contenu typique** : une chaîne représentant le nom du fichier, par ex. `anton_invoice-1.pdf`.

### filename
- **Signification** : le nom du fichier du document après son traitement ou son stockage dans le système.
- **Rôle** : champ descriptif
- **Contenu typique** : une chaîne représentant le nom du fichier, souvent identique à `original_filename`.

### imported_on
- **Signification** : la date et l'heure auxquelles le document a été importé.
- **Rôle** : champ descriptif
- **Contenu typique** : un horodatage au format ISO 8601.

### source_type
- **Signification** : le type de source à partir de laquelle le document a été importé.
- **Rôle** : champ descriptif
- **Contenu typique** : une chaîne, par ex. `EMAIL`, indiquant le type de source.

### source
- **Signification** : des informations détaillées sur la source de l'import.
- **Rôle** : champ descriptif
- **Contenu typique** : une chaîne détaillant la source, par ex. `Email:O365:demo@fellow-digital.de:Tini Test`.

### success
- **Signification** : indique si l'import a réussi.
- **Rôle** : champ d'état
- **Contenu typique** : une valeur booléenne (`True` ou `False`).

### created_by
- **Signification** : l'identifiant de l'utilisateur qui a lancé l'import.
- **Rôle** : clé étrangère
- **Contenu typique** : un entier représentant l'ID de l'utilisateur.

### created_on
- **Signification** : la date et l'heure de création de l'entrée du journal d'import.
- **Rôle** : champ technique
- **Contenu typique** : un horodatage avec fuseau horaire.

### last_modified_on
- **Signification** : la date et l'heure de la dernière modification de l'entrée du journal d'import.
- **Rôle** : champ technique
- **Contenu typique** : un horodatage avec fuseau horaire ; peut être `None` si non modifié.

### is_deleted
- **Signification** : indique si l'entrée du journal d'import a été marquée comme supprimée.
- **Rôle** : champ d'état
- **Contenu typique** : une valeur booléenne (`True` ou `False`).

### import_id
- **Signification** : un identifiant unique du processus d'import.
- **Rôle** : champ technique
- **Contenu typique** : une chaîne ou un texte représentant un identifiant de processus unique.

### extra_data
- **Signification** : des métadonnées supplémentaires relatives à l'import.
- **Rôle** : champ descriptif
- **Contenu typique** : une chaîne JSON contenant des données supplémentaires, telles que la date, l'expéditeur, l'objet et le nombre.

### doc_id
- **Signification** : l'identifiant du document.
- **Rôle** : clé étrangère
- **Contenu typique** : un UUID ou un identifiant de chaîne unique similaire ; peut être `None`.

### email_connection_id
- **Signification** : l'identifiant de la connexion e-mail utilisée pour l'import.
- **Rôle** : clé étrangère
- **Contenu typique** : un entier représentant l'ID de la connexion e-mail ; peut être `None`.

### subject
- **Signification** : l'objet de l'e-mail à partir duquel le document a été importé.
- **Rôle** : champ descriptif
- **Contenu typique** : une chaîne représentant l'objet de l'e-mail.

### body
- **Signification** : le contenu du corps de l'e-mail à partir duquel le document a été importé.
- **Rôle** : champ descriptif
- **Contenu typique** : du texte contenant le corps de l'e-mail ; peut être `None`.

### sender
- **Signification** : l'adresse e-mail de l'expéditeur du document.
- **Rôle** : champ descriptif
- **Contenu typique** : une chaîne contenant l'adresse e-mail de l'expéditeur.

### error_resp
- **Signification** : la réponse ou le message d'erreur si l'import a échoué.
- **Rôle** : champ d'état
- **Contenu typique** : une chaîne contenant les détails de l'erreur ; peut être `None`.

### source_received_on
- **Signification** : la date et l'heure auxquelles le document a été reçu de la source.
- **Rôle** : champ descriptif
- **Contenu typique** : un horodatage avec fuseau horaire.

Cette documentation offre un aperçu détaillé de la table `public.document_import_log` et de ses colonnes, essentiel pour comprendre et gérer les imports de documents dans le système.
```
