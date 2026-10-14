# Document table column

## Colonnes

* `id`: internal
* `document_table_id`: internal
* `table_name`: internal
* `org_id`: ID to organisation
* `column_name`: internal
* `column_type`: internal
* `title`: internal
* `translation_key`: internal
* `sort_order`: integer
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

## Analyse et description

```markdown
# Documentation technique de `public.document_table_column`

## Introduction

La table `public.document_table_column` semble conçue pour stocker des métadonnées sur les colonnes de diverses tables liées aux documents, telles que les tables de factures ou de bons de livraison. Ces métadonnées comprennent des informations sur le nom, le type et les propriétés de chaque colonne, ainsi que des identifiants organisationnels et techniques. La table prend en charge la génération et la gestion dynamiques des schémas de documents dans le système.

## Description des colonnes

### id
- **Signification** : un identifiant unique pour chaque entrée de colonne de la table.
- **Rôle** : clé primaire.
- **Remarque** : généralement une chaîne UUID qui identifie de manière unique une ligne de cette table.

### document_table_id
- **Signification** : fait référence à la table qui contient le document dont cette colonne fait partie.
- **Rôle** : clé étrangère.
- **Remarque** : vraisemblablement un UUID qui renvoie à une autre table où les tables de documents sont définies.

### table_name
- **Signification** : le nom de la table de document à laquelle appartient cette colonne.
- **Rôle** : champ descriptif.
- **Contenu typique** : des noms comme `INVOICE_TABLE`, `DELIVERY_NOTE_TABLE`.
- **Remarque** : facilite la compréhension de la structure de document à laquelle appartient la colonne.

### org_id
- **Signification** : identifiant de l'organisation qui possède ou gère la table de document.
- **Rôle** : clé étrangère.
- **Remarque** : généralement un UUID reliant à une entité organisation.

### column_name
- **Signification** : le nom technique de la colonne dans sa table de document.
- **Rôle** : champ descriptif.
- **Contenu typique** : des noms tels que `COUNTRY_ORIGIN`, `ORDERED_QUANTITY`.
- **Remarque** : représente le nom réel du champ dans la table de document.

### column_type
- **Signification** : décrit le type de données de la colonne.
- **Rôle** : champ descriptif.
- **Contenu typique** : `STRING`, `DATE`.
- **Remarque** : indique le type de données stockées dans la colonne.

### title
- **Signification** : un titre ou libellé lisible par l'humain pour la colonne.
- **Rôle** : champ descriptif.
- **Contenu typique** : `COUNTRY_ORIGIN`, `Ordered Quantity`.
- **Remarque** : sert à afficher les noms de colonnes de manière conviviale.

### translation_key
- **Signification** : clé utilisée pour l'internationalisation et la localisation du titre de la colonne.
- **Rôle** : champ technique.
- **Remarque** : actuellement vide dans les données d'exemple, ce qui suggère un usage facultatif.

### sort_order
- **Signification** : définit l'ordre des colonnes à l'affichage.
- **Rôle** : champ descriptif.
- **Contenu typique** : des entiers comme `16`, `5`.
- **Remarque** : détermine la séquence des colonnes dans la vue de la table de document.

### clean_field
- **Signification** : indique si la colonne contient des données nettoyées.
- **Rôle** : indicateur booléen.
- **Contenu typique** : `True` ou `False`.
- **Remarque** : utilisé pour la validation des données ou l'état de nettoyage.

### alphanumeric_field
- **Signification** : précise si la colonne doit être traitée comme un champ alphanumérique.
- **Rôle** : indicateur booléen.
- **Contenu typique** : `True` ou `False`.
- **Remarque** : utile pour la validation des saisies ou la mise en forme.

### created_by
- **Signification** : identifiant de l'utilisateur qui a créé cette entrée de colonne.
- **Rôle** : clé étrangère.
- **Contenu typique** : des valeurs entières comme `1`, `8`.
- **Remarque** : renvoie à un utilisateur ou à une entité système responsable de la création.

### created_on
- **Signification** : horodatage de création de l'entrée de colonne.
- **Rôle** : champ technique.
- **Contenu typique** : des valeurs de date et d'heure en UTC.
- **Remarque** : utile pour l'audit et le suivi des modifications.

### last_modified_on
- **Signification** : horodatage de la dernière modification apportée à l'entrée de colonne.
- **Rôle** : champ technique.
- **Remarque** : actuellement `None` dans les données d'exemple, ce qui indique qu'aucune modification n'a eu lieu après la création.

### is_deleted
- **Signification** : indique si l'entrée de colonne a été logiquement supprimée.
- **Rôle** : indicateur booléen.
- **Contenu typique** : `True` ou `False`.
- **Remarque** : aide à gérer les suppressions logiques sans supprimer physiquement les données.

```
