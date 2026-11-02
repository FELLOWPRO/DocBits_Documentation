# Alerte d’état du document

## Table `public.document_status_alert`

### Colonnes

* `id`: internal
* `org_id`: ID to organisation
* `doc_type_id`: internal
* `doc_type_key`: internal
* `doc_status`: internal
* `email_address`: text
* `send_to_assigned_user`: boolean
* `delay_delta`: integer
* `delay_delta_type`: internal
* `created_by`: integer
* `created_on` : horodatage avec fuseau horaire
* `last_modified_on` : horodatage avec fuseau horaire
* `is_deleted`: boolean
* `name`: internal
* `is_recursive`: boolean
* `is_active`: boolean
* `priority`: internal
* `email_template_id`: internal

### Analyse et description

## Documentation de la table : `public.document_status_alert`

### Introduction

La table `public.document_status_alert` semble conçue pour gérer les alertes liées aux statuts des documents au sein d'une organisation. D'après les noms de colonnes, la table stocke des informations sur divers types de documents et leurs statuts, y compris des détails sur les notifications et le calendrier des alertes. Cette table sert vraisemblablement à déclencher des alertes en fonction de certains statuts et conditions de documents, éventuellement pour notifier des utilisateurs ou escalader des processus.

### Description des colonnes

#### `id`

* **Signification** : identifiant unique de chaque enregistrement d'alerte.
* **Rôle** : clé primaire.
* **Contenu typique** : une chaîne UUID qui identifie chaque ligne de la table de manière unique.

#### `org_id`

* **Signification** : identifiant de l'organisation associée à l'alerte.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne UUID renvoyant à un enregistrement d'organisation.

#### `doc_type_id`

* **Signification** : identifiant du type de document.
* **Rôle** : clé étrangère (supposée).
* **Contenu typique** : généralement un UUID, bien que les données d'exemple affichent `None`, ce qui indique que ce champ peut être facultatif.

#### `doc_type_key`

* **Signification** : clé représentant le type de document.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne telle que 'INVOICE' ou 'XML\_INVOICE'.

#### `doc_status`

* **Signification** : statut actuel du document.
* **Rôle** : champ descriptif.
* **Contenu typique** : des chaînes de statut descriptives comme 'validated\_pending\_approval' ou 'error'.

#### `email_address`

* **Signification** : adresse e-mail à laquelle les alertes sont envoyées.
* **Rôle** : champ de notification.
* **Contenu typique** : une adresse e-mail ; peut être `None` si aucune adresse n'est indiquée.

#### `send_to_assigned_user`

* **Signification** : indique si l'alerte doit être envoyée à l'utilisateur affecté au document.
* **Rôle** : champ booléen.
* **Contenu typique** : `True` ou `False`.

#### `delay_delta`

* **Signification** : durée du délai avant l'envoi de l'alerte.
* **Rôle** : champ de temporisation.
* **Contenu typique** : un entier représentant la durée du délai.

#### `delay_delta_type`

* **Signification** : unité de temps de `delay_delta`.
* **Rôle** : champ de temporisation.
* **Contenu typique** : généralement 'minutes'.

#### `created_by`

* **Signification** : identifiant de l'utilisateur qui a créé l'enregistrement d'alerte.
* **Rôle** : clé étrangère (supposée).
* **Contenu typique** : un entier représentant un ID d'utilisateur.

#### `created_on`

* **Signification** : horodatage de création de l'enregistrement d'alerte.
* **Rôle** : champ technique.
* **Contenu typique** : date et heure avec information de fuseau horaire.

#### `last_modified_on`

* **Signification** : horodatage de la dernière modification de l'enregistrement d'alerte.
* **Rôle** : champ technique.
* **Contenu typique** : date et heure avec information de fuseau horaire ; peut être `None` si non modifié.

#### `is_deleted`

* **Signification** : indique si l'enregistrement d'alerte est marqué comme supprimé.
* **Rôle** : champ booléen.
* **Contenu typique** : `True` ou `False`.

#### `name`

* **Signification** : nom ou libellé de l'alerte.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne représentant le nom de l'alerte.

#### `is_recursive`

* **Signification** : indique si l'alerte doit se répéter à intervalles définis.
* **Rôle** : champ booléen.
* **Contenu typique** : `True` ou `False`.

#### `is_active`

* **Signification** : indique si l'alerte est actuellement active.
* **Rôle** : champ booléen.
* **Contenu typique** : `True` ou `False`.

#### `priority`

* **Signification** : niveau de priorité de l'alerte.
* **Rôle** : champ descriptif.
* **Contenu typique** : peut être des chaînes comme 'High', 'Medium', 'Low' ; les données d'exemple affichent `None`.

#### `email_template_id`

* **Signification** : identifiant du modèle d'e-mail utilisé pour l'alerte.
* **Rôle** : clé étrangère (supposée).
* **Contenu typique** : généralement un UUID ; les données d'exemple affichent `None`, ce qui indique que ce champ peut être facultatif.
