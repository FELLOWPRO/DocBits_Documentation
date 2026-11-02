# Configurations d’importation FTP

## Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `sub_org_id` : interne
* `server_url` : interne
* `username` : interne
* `password` : interne
* `is_active` : boolean
* `created_by` : integer
* `created_on` : horodatage avec fuseau horaire
* `last_modified_on` : horodatage avec fuseau horaire
* `is_deleted` : boolean
* `deleted_on` : horodatage avec fuseau horaire
* `port` : integer
* `default_directory` : interne
* `ftp_type` : interne
* `token` : interne
* `file_name_matching_patterns` : interne
* `last_mtime` : interne
* `auth_failed_count` : integer
* `auth_message` : texte
* `ignore_certificate` : boolean
* `move_after_import` : boolean
* `destination_directory` : interne
* `import_directory` : interne
* `include_subfolder_content` : boolean

## Analyse et description

```markdown
# Documentation de la table FTP Import Configurations

## Introduction

La table `public.ftp_import_configurations` est conçue pour stocker les détails de configuration des processus d'import FTP. Cette table contient les informations nécessaires pour se connecter aux serveurs FTP, gérer l'authentification et traiter les imports de fichiers. Elle prend en charge les protocoles FTP et SFTP et comprend des champs pour les détails du serveur FTP, les identifiants d'authentification et les paramètres opérationnels, par exemple le déplacement des fichiers après l'import et l'inclusion du contenu des sous-dossiers.

## Description des colonnes

### id
- **Signification** : identifiant unique de chaque enregistrement de configuration d'import FTP.
- **Rôle** : clé primaire.
- **Contenu typique** : format UUID, par ex. `9862d8c6-bb61-4373-9616-d5f8c125eeb8`.

### org_id
- **Signification** : identifiant de l'organisation associée à cette configuration.
- **Rôle** : clé étrangère.
- **Contenu typique** : format UUID.

### sub_org_id
- **Signification** : identifiant d'une sous-organisation, le cas échéant.
- **Rôle** : clé étrangère.
- **Contenu typique** : format UUID ou `null` si non applicable.

### server_url
- **Signification** : URL ou adresse IP du serveur FTP.
- **Rôle** : champ descriptif.
- **Contenu typique** : nom de domaine ou adresse IP, par ex. `sftp.it.doxee.com`.

### username
- **Signification** : nom d'utilisateur utilisé pour l'authentification auprès du serveur FTP.
- **Rôle** : champ descriptif.
- **Contenu typique** : nom d'utilisateur en texte brut.

### password
- **Signification** : mot de passe utilisé pour l'authentification auprès du serveur FTP.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaîne de mot de passe chiffrée.

### is_active
- **Signification** : indique si la configuration est actuellement active.
- **Rôle** : indicateur d'état.
- **Contenu typique** : `True` ou `False`.

### created_by
- **Signification** : identifiant de l'utilisateur qui a créé la configuration.
- **Rôle** : clé étrangère.
- **Contenu typique** : entier représentant l'ID utilisateur.

### created_on
- **Signification** : horodatage de la création de la configuration.
- **Rôle** : champ d'audit.
- **Contenu typique** : date et heure avec information de fuseau horaire.

### last_modified_on
- **Signification** : horodatage de la dernière modification de la configuration.
- **Rôle** : champ d'audit.
- **Contenu typique** : date et heure avec information de fuseau horaire.

### is_deleted
- **Signification** : indique si la configuration a été marquée comme supprimée.
- **Rôle** : indicateur d'état.
- **Contenu typique** : `True` ou `False`.

### deleted_on
- **Signification** : horodatage du marquage de la configuration comme supprimée.
- **Rôle** : champ d'audit.
- **Contenu typique** : date et heure avec information de fuseau horaire, ou une date par défaut pour les enregistrements non supprimés.

### port
- **Signification** : numéro de port utilisé pour se connecter au serveur FTP.
- **Rôle** : champ descriptif.
- **Contenu typique** : entier, par ex. `22` pour SFTP.

### default_directory
- **Signification** : chemin du répertoire par défaut sur le serveur FTP.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaîne de chemin de répertoire.

### ftp_type
- **Signification** : type de protocole FTP utilisé (par ex. FTP, SFTP).
- **Rôle** : champ descriptif.
- **Contenu typique** : `FTP` ou `SFTP`.

### token
- **Signification** : jeton de sécurité pour une authentification ou une identification supplémentaire.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaîne chiffrée ou encodée.

### file_name_matching_patterns
- **Signification** : motifs utilisés pour faire correspondre les noms de fichiers à importer.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaînes de motifs ou `null`.

### last_mtime
- **Signification** : dernière heure de modification des fichiers, utilisée pour filtrer les imports.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaîne représentant un horodatage ou `null`.

### auth_failed_count
- **Signification** : compteur des tentatives d'authentification échouées.
- **Rôle** : champ descriptif.
- **Contenu typique** : entier, par ex. `0` ou `5`.

### auth_message
- **Signification** : message décrivant le résultat de la dernière tentative d'authentification.
- **Rôle** : champ descriptif.
- **Contenu typique** : message texte ou `null`.

### ignore_certificate
- **Signification** : indique si la validation du certificat SSL doit être ignorée.
- **Rôle** : indicateur d'état.
- **Contenu typique** : `True` ou `False`.

### move_after_import
- **Signification** : indique si les fichiers doivent être déplacés une fois l'import terminé.
- **Rôle** : indicateur d'état.
- **Contenu typique** : `True` ou `False`.

### destination_directory
- **Signification** : chemin du répertoire vers lequel les fichiers doivent être déplacés après l'import.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaîne de chemin de répertoire ou `null`.

### import_directory
- **Signification** : chemin du répertoire à partir duquel les fichiers sont importés.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaîne de chemin de répertoire ou `null`.

### include_subfolder_content
- **Signification** : indique si le contenu des sous-dossiers doit être inclus dans l'import.
- **Rôle** : indicateur d'état.
- **Contenu typique** : `True` ou `False`.
```

Cette documentation permet de comprendre l'ensemble des colonnes de la table `public.ftp_import_configurations` en expliquant leur finalité, leur rôle et leur contenu typique, à partir des données fournies et des noms de colonnes.
