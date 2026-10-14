# Document Report

## Colonnes

* `id`: internal
* `org_id`: ID to organisation
* `doc_id`: internal
* `doc_type`: DOC Type
* `sub_doc_type`: internal
* `time_spent`: internal
* `fields_total`: integer
* `fields_correct`: integer
* `checkbox_fields_total`: integer
* `checkbox_fields_correct`: integer
* `table_values_total`: integer
* `table_values_correct`: integer
* `detail_report`: text
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `validated_by`: integer
* `sub_org_id`: internal

## Analyse et description

```markdown
# Documentation de la table Document Report

## Introduction
La table `public.document_report` sert à stocker des informations détaillées sur les rapports de traitement des documents, en particulier ceux liés à la validation et à l'extraction de champs de documents tels que les factures. La table enregistre des métadonnées sur le document, des indicateurs de traitement et les résultats de la validation, qui peuvent être utilisés pour l'audit, le suivi et l'amélioration des workflows de traitement des documents.

## Description des colonnes

### id
- **Signification** : identifiant unique de chaque entrée de rapport de document.
- **Rôle** : clé primaire
- **Contenu typique** : un UUID représentant le rapport de document unique.

### org_id
- **Signification** : identifiant de l'organisation associée au document.
- **Rôle** : clé étrangère
- **Contenu typique** : un UUID renvoyant à une organisation.

### doc_id
- **Signification** : identifiant du document spécifique faisant l'objet du rapport.
- **Rôle** : clé étrangère
- **Contenu typique** : un UUID représentant le document unique.

### doc_type
- **Signification** : type du document traité, par exemple une facture.
- **Rôle** : champ descriptif
- **Contenu typique** : des valeurs comme `INVOICE`.

### sub_doc_type
- **Signification** : sous-type du document, offrant une catégorisation plus fine.
- **Rôle** : champ descriptif
- **Contenu typique** : peut être `null` ou des sous-types spécifiques comme « Cost Invoice ».

### time_spent
- **Signification** : temps passé à valider le document.
- **Rôle** : champ de mesure
- **Contenu typique** : généralement '0', le temps étant mesuré dans des unités prédéfinies.

### fields_total
- **Signification** : nombre total de champs extraits du document.
- **Rôle** : champ de mesure
- **Contenu typique** : un entier représentant le total des champs, par ex. 13.

### fields_correct
- **Signification** : nombre de champs correctement extraits et validés.
- **Rôle** : champ de mesure
- **Contenu typique** : un entier représentant les champs correctement traités, par ex. 12.

### checkbox_fields_total
- **Signification** : nombre total de champs de case à cocher traités.
- **Rôle** : champ de mesure
- **Contenu typique** : généralement `0`, indiquant les champs de case à cocher traités.

### checkbox_fields_correct
- **Signification** : nombre de champs de case à cocher correctement validés.
- **Rôle** : champ de mesure
- **Contenu typique** : généralement `0`, indiquant les champs de case à cocher correctement validés.

### table_values_total
- **Signification** : nombre total de valeurs de tableau extraites du document.
- **Rôle** : champ de mesure
- **Contenu typique** : généralement `0`, indiquant le total des valeurs de tableau traitées.

### table_values_correct
- **Signification** : nombre de valeurs de tableau correctement validées.
- **Rôle** : champ de mesure
- **Contenu typique** : généralement `0`, indiquant les valeurs de tableau correctement validées.

### detail_report
- **Signification** : contenu JSON fournissant un rapport détaillé des champs du document et de leur état de validation.
- **Rôle** : champ descriptif/technique
- **Contenu typique** : une chaîne JSON contenant des informations détaillées sur les champs.

### created_on
- **Signification** : horodatage de création de l'entrée du rapport de document.
- **Rôle** : champ technique
- **Contenu typique** : un horodatage en UTC, par ex. `2025-03-10 08:07:24+00`.

### last_modified_on
- **Signification** : horodatage de la dernière modification du rapport de document.
- **Rôle** : champ technique
- **Contenu typique** : un horodatage en UTC, indiquant l'heure de la dernière mise à jour.

### is_deleted
- **Signification** : indique si le rapport de document a été marqué comme supprimé.
- **Rôle** : champ technique
- **Contenu typique** : une valeur booléenne ; `False` s'il n'est pas supprimé.

### validated_by
- **Signification** : identifiant de l'utilisateur qui a validé le document.
- **Rôle** : clé étrangère
- **Contenu typique** : un entier représentant l'ID du validateur, par ex. `1`.

### sub_org_id
- **Signification** : identifiant d'une sous-organisation liée au document.
- **Rôle** : clé étrangère
- **Contenu typique** : un UUID renvoyant à une sous-organisation.
```
