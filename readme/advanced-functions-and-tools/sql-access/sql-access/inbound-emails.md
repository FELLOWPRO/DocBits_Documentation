# Inbound Emails

## Table `public.inbound_emails`

### Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `is_active` : boolean
* `email_senders` : interne
* `email_receiver` : interne
* `token` : interne
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_by` : interne
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean
* `deleted_by` : interne
* `deleted_on` : timestamp with time zone

### Analyse et description

## Documentation technique : table `public.inbound_emails`

### Introduction

La table `public.inbound_emails` est conçue pour stocker et gérer les informations sur les e-mails reçus par une organisation. Elle conserve les détails de l'expéditeur et du destinataire, l'état de l'e-mail et diverses métadonnées relatives à la création, à la modification et à la suppression des enregistrements. Elle semble faire partie d'un système de gestion des e-mails au sein d'une organisation, éventuellement utilisé pour suivre les communications par e-mail entrantes.

### Description des colonnes

#### id

* **Signification** : identifiant unique de chaque enregistrement de la table.
* **Rôle** : clé primaire.
* **Contenu typique** : une chaîne unique, vraisemblablement un UUID, comme `'42bf9383-73bf-4b46-9862-3c3a1d97ac80'`.

#### org\_id

* **Signification** : identifiant de l'organisation associée à l'e-mail entrant.
* **Rôle** : clé étrangère, renvoyant à une autre table qui contient les détails de l'organisation.
* **Contenu typique** : une chaîne unique, vraisemblablement un UUID, comme `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### is\_active

* **Signification** : indique si l'enregistrement de l'e-mail est actuellement actif.
* **Rôle** : indicateur d'état.
* **Contenu typique** : une valeur booléenne, `True` ou `False`.

#### email\_senders

* **Signification** : stocke les informations sur le ou les expéditeurs de l'e-mail.
* **Rôle** : champ de données.
* **Contenu typique** : une chaîne de type JSON contenant les détails des expéditeurs, par ex. `"[{'email': '', 'sub_org': ''}]"`.

#### email\_receiver

* **Signification** : adresse e-mail du destinataire principal.
* **Rôle** : champ de données.
* **Contenu typique** : une chaîne contenant une adresse e-mail. Dans l'exemple, elle est vide, ce qui suggère un usage facultatif ou variable.

#### token

* **Signification** : jeton associé à l'e-mail, éventuellement pour l'authentification ou l'identification.
* **Rôle** : champ d'authentification ou de suivi.
* **Contenu typique** : une longue chaîne générée de manière aléatoire.

#### created\_by

* **Signification** : identifiant de l'utilisateur qui a créé l'enregistrement.
* **Rôle** : clé étrangère, renvoyant à une table d'utilisateurs ou d'employés.
* **Contenu typique** : un entier représentant un ID utilisateur, comme `1`.

#### created\_on

* **Signification** : horodatage de la création de l'enregistrement.
* **Rôle** : champ de métadonnées.
* **Contenu typique** : une valeur datetime avec information de fuseau horaire, par ex. `datetime.datetime(2024, 11, 25, 7, 43, 54, 266771, tzinfo=datetime.timezone.utc)`.

#### last\_modified\_by

* **Signification** : identifiant de l'utilisateur qui a modifié l'enregistrement en dernier.
* **Rôle** : clé étrangère, renvoyant à une table d'utilisateurs ou d'employés.
* **Contenu typique** : peut être un ID utilisateur ou null si aucune modification n'a été effectuée.

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification de l'enregistrement.
* **Rôle** : champ de métadonnées.
* **Contenu typique** : une valeur datetime indiquant l'heure de la dernière modification, par ex. `datetime.datetime(2024, 11, 25, 7, 44, 48, 505384, tzinfo=datetime.timezone.utc)`.

#### is\_deleted

* **Signification** : indique si l'enregistrement de l'e-mail a été marqué comme supprimé.
* **Rôle** : indicateur d'état.
* **Contenu typique** : une valeur booléenne, `True` ou `False`.

#### deleted\_by

* **Signification** : identifiant de l'utilisateur qui a marqué l'enregistrement comme supprimé.
* **Rôle** : clé étrangère, renvoyant à une table d'utilisateurs ou d'employés.
* **Contenu typique** : peut être un ID utilisateur ou null si l'enregistrement n'est pas supprimé.

#### deleted\_on

* **Signification** : horodatage du marquage de l'enregistrement comme supprimé.
* **Rôle** : champ de métadonnées.
* **Contenu typique** : une valeur datetime indiquant l'heure de suppression, ou une date par défaut si non applicable, par ex. `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`.
