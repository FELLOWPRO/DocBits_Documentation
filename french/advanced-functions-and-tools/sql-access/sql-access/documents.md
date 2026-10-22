# Documents

## Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `batch_id` : interne
* `doc_path` : interne
* `doc_type` : DOC Type
* `status` : interne
* `message` : texte
* `export_attempts` : integer
* `last_attempted_on` : horodatage avec fuseau horaire
* `next_attempt_on` : horodatage avec fuseau horaire
* `assigned_to` : integer
* `created_by` : integer
* `created_on` : horodatage avec fuseau horaire
* `last_modified_on` : horodatage avec fuseau horaire
* `is_deleted` : boolean
* `task_id` : interne
* `filename` : interne
* `assigned_on` : horodatage avec fuseau horaire
* `pages` : integer
* `auto_processed` : boolean
* `exception_info` : texte
* `doc_language` : Language
* `is_trimmed` : boolean
* `doc_origin` : Doc Origin
* `doc_locale` : Doc Locale
* `is_doc2landing_doc` : boolean
* `extraction_time` : double precision
* `export_time` : double precision
* `po_all_matched` : boolean
* `restart_allowed` : boolean
* `table_version` : interne
* `force_ocr` : boolean
* `locked_by` : integer
* `locked_on` : horodatage avec fuseau horaire
* `lock_renewed_on` : horodatage avec fuseau horaire
* `lock_key` : interne
* `last_saved_by` : integer
* `last_saved_on` : horodatage avec fuseau horaire
* `document_version` : integer
* `lock_session_key` : interne
* `sub_org_id` : interne
* `doc_source` : interne
* `sub_doc_type` : interne
* `assigned_to_group` : interne
* `status_changed_on` : horodatage avec fuseau horaire
* `improve_quality` : boolean
* `priority` : integer
* `metadata_field` : json
* `doc_classification_label` : interne
* `doc_start_page` : integer
* `doc_classification_class` : interne
* `celery_task_token` : interne
* `celery_task_attempt` : integer
* `celery_task_priority` : integer
* `has_zugferd` : boolean
* `has_peppol` : boolean
* `timestamp_for_validation` : horodatage avec fuseau horaire
* `exception_details` : texte
* `has_annotated_version` : boolean
* `po_match_status` : interne
* `tr_ocr_extracted_data` : texte
* `pending_workflow_execution` : boolean
* `extracted_document_id` : interne
* `extracted_supplier_id` : interne
* `classification_manually_corrected` : boolean
* `supplier_as_org_id` : interne
* `extracted_data_basic` : jsonb
* `celery_task_queue` : interne
* `extracted_data` : jsonb
* `extracted_data_jsonb` : jsonb
* `warnings` : jsonb

## Analyse et description

```markdown
# Documentation technique de la table `public.documents`

## Introduction

La table `public.documents` est conçue pour stocker et gérer les métadonnées et les informations de traitement relatives à la gestion des documents au sein d'une organisation. Cela comprend le suivi du statut des documents, des tentatives de traitement, de la langue et d'autres détails administratifs. La table est structurée pour prendre en charge la classification des documents, le flux de traitement et les affectations aux utilisateurs, ce qui en fait un élément essentiel du système de gestion documentaire.

## Description des colonnes

### id
- **Signification** : identifiant unique de chaque document.
- **Rôle** : clé primaire.
- **Contenu typique** : une chaîne UUID représentant le document.

### org_id
- **Signification** : identifiant de l'organisation associée au document.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID représentant l'organisation.

### batch_id
- **Signification** : identifiant du lot dans lequel le document a été traité.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID représentant le lot.

### doc_path
- **Signification** : chemin du fichier où le document est stocké.
- **Rôle** : champ technique.
- **Contenu typique** : chemin vers le fichier du document, par ex. `documents/{id}/{id}.pdf`.

### doc_type
- **Signification** : type du document stocké (par ex. facture).
- **Rôle** : classification du document.
- **Contenu typique** : une chaîne telle que `INVOICE`.

### status
- **Signification** : statut de traitement actuel du document.
- **Rôle** : indicateur de flux de traitement.
- **Contenu typique** : une chaîne indiquant le statut, par ex. `ready_for_validation`.

### message
- **Signification** : informations sur l'état de traitement du document ou sur les erreurs.
- **Rôle** : champ descriptif.
- **Contenu typique** : texte décrivant les erreurs ou les messages liés au traitement du document.

### export_attempts
- **Signification** : nombre de tentatives d'export effectuées pour le document.
- **Rôle** : suivi du traitement.
- **Contenu typique** : nombre entier de tentatives d'export.

### last_attempted_on
- **Signification** : horodatage de la dernière tentative de traitement ou d'export du document.
- **Rôle** : champ d'horodatage.
- **Contenu typique** : date et heure avec fuseau horaire.

### next_attempt_on
- **Signification** : horodatage planifié de la prochaine tentative de traitement ou d'export du document.
- **Rôle** : champ de planification.
- **Contenu typique** : date et heure avec fuseau horaire.

### assigned_to
- **Signification** : identifiant de l'utilisateur auquel ce document est affecté.
- **Rôle** : clé étrangère.
- **Contenu typique** : entier représentant l'ID utilisateur.

### created_by
- **Signification** : identifiant de l'utilisateur qui a créé ou téléversé le document.
- **Rôle** : clé étrangère.
- **Contenu typique** : entier représentant l'ID utilisateur.

### created_on
- **Signification** : horodatage de la création ou du téléversement du document.
- **Rôle** : champ d'horodatage.
- **Contenu typique** : date et heure avec fuseau horaire.

### last_modified_on
- **Signification** : horodatage de la dernière modification apportée à l'enregistrement du document.
- **Rôle** : champ d'horodatage.
- **Contenu typique** : date et heure avec fuseau horaire.

### is_deleted
- **Signification** : indique si le document est marqué comme supprimé.
- **Rôle** : indicateur de suppression logique.
- **Contenu typique** : valeur booléenne (True ou False).

### task_id
- **Signification** : identifiant de la tâche associée au traitement du document.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID représentant la tâche.

### filename
- **Signification** : nom de fichier d'origine du document.
- **Rôle** : champ descriptif.
- **Contenu typique** : nom du fichier, par ex. `document.pdf`.

### assigned_on
- **Signification** : horodatage de l'affectation du document à un utilisateur.
- **Rôle** : champ d'horodatage.
- **Contenu typique** : date et heure avec fuseau horaire.

### pages
- **Signification** : nombre de pages du document.
- **Rôle** : champ descriptif.
- **Contenu typique** : entier indiquant le nombre de pages.

### auto_processed
- **Signification** : indique si le document a été traité automatiquement.
- **Rôle** : indicateur d'état de traitement.
- **Contenu typique** : valeur booléenne (True ou False).

### exception_info
- **Signification** : informations sur les exceptions éventuelles rencontrées pendant le traitement.
- **Rôle** : champ descriptif.
- **Contenu typique** : texte décrivant les exceptions de traitement.

### doc_language
- **Signification** : langue du contenu du document.
- **Rôle** : classification par langue.
- **Contenu typique** : code de langue ISO, par ex. `en`, `de`.

### is_trimmed
- **Signification** : indique si le document a été rogné ou recadré.
- **Rôle** : indicateur de modification du document.
- **Contenu typique** : valeur booléenne (True ou False).

### doc_origin
- **Signification** : origine du document, pouvant indiquer le pays ou le système source.
- **Rôle** : champ descriptif.
- **Contenu typique** : code pays ou identifiant d'origine, par ex. `DE`.

### doc_locale
- **Signification** : paramètres régionaux du document, indiquant la langue et la région.
- **Rôle** : classification des paramètres régionaux.
- **Contenu typique** : chaîne de paramètres régionaux, par ex. `de_DE.ISO8859-1`.

### is_doc2landing_doc
- **Signification** : indique si le document est lié à un flux de traitement spécifique (Doc2Landing).
- **Rôle** : indicateur de flux de traitement.
- **Contenu typique** : valeur booléenne (True ou False).

### extraction_time
- **Signification** : temps nécessaire pour extraire les données du document.
- **Rôle** : indicateur de performance.
- **Contenu typique** : valeur en double précision représentant la durée d'extraction.

### export_time
- **Signification** : temps nécessaire pour exporter le document.
- **Rôle** : indicateur de performance.
- **Contenu typique** : valeur en double précision représentant la durée d'export.

### po_all_matched
- **Signification** : indique si toutes les commandes d'achat liées au document ont été rapprochées.
- **Rôle** : indicateur d'état de rapprochement.
- **Contenu typique** : valeur booléenne (True ou False).

### restart_allowed
- **Signification** : indique si le traitement du document peut être relancé.
- **Rôle** : indicateur de contrôle du flux de traitement.
- **Contenu typique** : valeur booléenne (True ou False).

### table_version
- **Signification** : version de la structure de table utilisée pour le document.
- **Rôle** : gestion des versions.
- **Contenu typique** : chaîne indiquant la version, par ex. `v3`.

### force_ocr
- **Signification** : indique si le traitement OCR est forcé pour le document.
- **Rôle** : indicateur de contrôle du traitement.
- **Contenu typique** : valeur booléenne (True ou False).

### locked_by
- **Signification** : identifiant de l'utilisateur qui a verrouillé le document pour modification.
- **Rôle** : clé étrangère.
- **Contenu typique** : entier représentant l'ID utilisateur.

### locked_on
- **Signification** : horodatage du verrouillage du document pour modification.
- **Rôle** : champ d'horodatage.
- **Contenu typique** : date et heure avec fuseau horaire.

### lock_renewed_on
- **Signification** : horodatage du dernier renouvellement du verrou du document.
- **Rôle** : champ d'horodatage.
- **Contenu typique** : date et heure avec fuseau horaire.

### lock_key
- **Signification** : clé associée au verrou du document.
- **Rôle** : contrôle du verrou.
- **Contenu typique** : chaîne représentant la clé de verrouillage.

### last_saved_by
- **Signification** : identifiant de l'utilisateur qui a enregistré le document en dernier.
- **Rôle** : clé étrangère.
- **Contenu typique** : entier représentant l'ID utilisateur.

### last_saved_on
- **Signification** : horodatage du dernier enregistrement du document.
- **Rôle** : champ d'horodatage.
- **Contenu typique** : date et heure avec fuseau horaire.

### document_version
- **Signification** : numéro de version du document.
- **Rôle** : suivi des versions.
- **Contenu typique** : entier représentant la version du document.

### lock_session_key
- **Signification** : clé de session associée au verrou du document.
- **Rôle** : contrôle du verrou.
- **Contenu typique** : chaîne représentant la clé de session.

### sub_org_id
- **Signification** : identifiant d'une sous-organisation associée au document.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID représentant la sous-organisation.

### doc_source
- **Signification** : système source ou origine du document.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaîne indiquant la source, par ex. `doc2app`.

### sub_doc_type
- **Signification** : classification du sous-type du document.
- **Rôle** : classification du document.
- **Contenu typique** : chaîne indiquant le sous-type.

### assigned_to_group
- **Signification** : identifiant du groupe auquel le document est affecté.
- **Rôle** : suivi des affectations.
- **Contenu typique** : une chaîne UUID représentant le groupe.

### status_changed_on
- **Signification** : horodatage du dernier changement de statut du document.
- **Rôle** : champ d'horodatage.
- **Contenu typique** : date et heure avec fuseau horaire.

### improve_quality
- **Signification** : indique si des processus d'amélioration de la qualité sont appliqués au document.
- **Rôle** : indicateur de contrôle qualité.
- **Contenu typique** : valeur booléenne (True ou False).

### priority
- **Signification** : priorité de traitement du document.
- **Rôle** : contrôle du flux de traitement.
- **Contenu typique** : entier indiquant le niveau de priorité.

### metadata_field
- **Signification** : champ JSON contenant les métadonnées relatives au document.
- **Rôle** : stockage de métadonnées.
- **Contenu typique** : structure JSON avec divers champs de métadonnées.

### doc_classification_label
- **Signification** : libellé indiquant la classification du document.
- **Rôle** : libellé de classification.
- **Contenu typique** : chaîne indiquant la classification, par ex. `INVOICE`.

### doc_start_page
- **Signification** : numéro de la page où commence le contenu du document.
- **Rôle** : champ descriptif.
- **Contenu typique** : entier indiquant la page de départ.

### doc_classification_class
- **Signification** : classe indiquant la classification détaillée du document.
- **Rôle** : détail de classification.
- **Contenu typique** : chaîne indiquant la classe de classification.

### celery_task_token
- **Signification** : jeton de suivi de la tâche Celery associée au document.
- **Rôle** : suivi des tâches.
- **Contenu typique** : chaîne représentant le jeton de la tâche.

### celery_task_attempt
- **Signification** : nombre de tentatives effectuées pour la tâche Celery.
- **Rôle** : suivi des tâches.
- **Contenu typique** : nombre entier de tentatives de la tâche.

### celery_task_priority
- **Signification** : niveau de priorité de la tâche Celery.
- **Rôle** : contrôle des tâches.
- **Contenu typique** : entier indiquant la priorité de la tâche.

### has_zugferd
- **Signification** : indique si le document est au format ZUGFeRD.
- **Rôle** : indicateur de format.
- **Contenu typique** : valeur booléenne (True ou False).

### has_peppol
- **Signification** : indique si le document est au format PEPPOL.
- **Rôle** : indicateur de format.
- **Contenu typique** : valeur booléenne (True ou False).

### timestamp_for_validation
- **Signification** : horodatage de la validation du document.
- **Rôle** : suivi de la validation.
- **Contenu typique** : date et heure avec fuseau horaire.

### exception_details
- **Signification** : informations détaillées sur les exceptions survenues pendant le traitement.
- **Rôle** : champ descriptif.
- **Contenu typique** : texte avec les détails de l'exception.

### has_annotated_version
- **Signification** : indique s'il existe une version annotée du document.
- **Rôle** : indicateur de version.
- **Contenu typique** : valeur booléenne (True ou False).

### po_match_status
- **Signification** : statut du rapprochement des commandes d'achat.
- **Rôle** : indicateur d'état de rapprochement.
- **Contenu typique** : chaîne indiquant le statut de rapprochement.

### tr_ocr_extracted_data
- **Signification** : données extraites du document par OCR.
- **Rôle** : stockage de données.
- **Contenu typique** : texte contenant les données extraites.

### pending_workflow_execution
- **Signification** : indique s'il existe des exécutions de workflow en attente.
- **Rôle** : indicateur d'état du workflow.
- **Contenu typique** : valeur booléenne (True ou False).

### extracted_document_id
- **Signification** : identifiant du document extrait.
- **Rôle** : suivi de l'extraction.
- **Contenu typique** : une chaîne UUID représentant le document extrait.

### extracted_supplier_id
- **Signification** : identifiant du fournisseur extrait.
- **Rôle** : suivi de l'extraction.
- **Contenu typique** : une chaîne UUID représentant le fournisseur extrait.

### classification_manually_corrected
- **Signification** : indique si la classification du document a été corrigée manuellement.
- **Rôle** : indicateur d'état de classification.
- **Contenu typique** : valeur booléenne (True ou False).

### supplier_as_org_id
- **Signification** : identifiant du fournisseur traité comme une organisation.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID représentant l'organisation du fournisseur.

### extracted_data_basic
- **Signification** : données extraites de base au format JSONB.
- **Rôle** : stockage de données.
- **Contenu typique** : structure JSONB avec les champs de données extraites.

### celery_task_queue
- **Signification** : nom de la file d'attente des tâches Celery.
- **Rôle** : gestion des tâches.
- **Contenu typique** : chaîne indiquant le nom de la file d'attente.

### extracted_data
- **Signification** : données extraites du document au format JSONB.
- **Rôle** : stockage de données.
- **Contenu typique** : structure JSONB avec les champs de données extraites.

### extracted_data_jsonb
- **Signification** : champ JSONB contenant les données extraites détaillées.
- **Rôle** : stockage de données.
- **Contenu typique** : structure JSONB avec les champs de données extraites.

### warnings
- **Signification** : avertissements liés au traitement du document, stockés au format JSONB.
- **Rôle** : stockage des avertissements.
- **Contenu typique** : structure JSONB avec les messages d'avertissement.
```
