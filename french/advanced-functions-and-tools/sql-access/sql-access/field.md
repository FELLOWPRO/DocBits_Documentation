# Field

## Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `doc_type` : DOC Type
* `is_sub_doc_type_field` : boolean
* `profile` : interne
* `field_name` : interne
* `field_type` : interne
* `title` : interne
* `translation_key` : interne
* `hide_label` : boolean
* `input_type` : interne
* `input_size` : interne
* `icon_left` : interne
* `icon_right` : interne
* `icon_above` : interne
* `group_id` : interne
* `row_order` : integer
* `sort_order` : integer
* `fuzzy_name` : interne
* `fuzzy_field` : interne
* `fuzzy_primary_field` : boolean
* `label_align` : interne
* `calculation_formula` : texte
* `clean_field` : boolean
* `alphanumeric_field` : boolean
* `placeholder` : interne
* `coordinates` : interne
* `normalized_coordinates` : interne
* `threshold` : interne
* `reference_point` : interne
* `checkbox_group` : interne
* `list_of_values` : interne
* `enforce_list_of_values` : boolean
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean
* `costing_element` : interne
* `erp_field_name` : interne

## Analyse et description

```markdown
# Documentation technique de la table `public.field`

## Introduction

La table `public.field` semble conçue pour gérer les métadonnées et la configuration des différents champs associés aux documents, vraisemblablement dans le domaine de l'assurance. Chaque ligne de la table semble représenter la configuration d'un champ précis, y compris son type, son libellé, ses paramètres de visibilité et d'autres propriétés qui déterminent la manière dont le champ doit être présenté et traité.

## Colonnes

### id
- **Signification** : identifiant unique de chaque configuration de champ.
- **Rôle** : clé primaire.
- **Contenu typique** : une chaîne UUID qui identifie de manière unique chaque entrée de la table.

### org_id
- **Signification** : identifiant de l'organisation associée à la configuration du champ.
- **Rôle** : clé étrangère.
- **Contenu typique** : un UUID faisant référence à une organisation.

### doc_type
- **Signification** : précise le type de document auquel le champ est associé.
- **Rôle** : éventuellement une clé étrangère ou un identifiant catégoriel.
- **Contenu typique** : une chaîne au format `INSURANCE_DOCUMENTS_<UUID>` indiquant le type de document.

### is_sub_doc_type_field
- **Signification** : indique si le champ est un sous-type du type de document.
- **Rôle** : champ technique.
- **Contenu typique** : valeur booléenne (True ou False).

### profile
- **Signification** : définit éventuellement le profil ou la portée du champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : souvent vide ou une brève description textuelle.

### field_name
- **Signification** : nom interne du champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : une chaîne représentant le nom du champ dans un contexte technique (par ex. `Schadennummer`).

### field_type
- **Signification** : définit le type de données que contient le champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaînes descriptives comme `STRING`, `AMOUNT`.

### title
- **Signification** : titre d'affichage du champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaîne en majuscules utilisée pour afficher le libellé du champ.

### translation_key
- **Signification** : clé de traduction dans différentes langues.
- **Rôle** : champ technique.
- **Contenu typique** : chaîne en minuscules représentant la clé de traduction.

### hide_label
- **Signification** : indique si le libellé du champ doit être masqué dans l'interface.
- **Rôle** : champ technique.
- **Contenu typique** : valeur booléenne (True ou False).

### input_type
- **Signification** : précise la méthode de saisie du champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : peut être vide ou contenir des chaînes définissant le type de saisie.

### input_size
- **Signification** : détermine la taille du champ de saisie.
- **Rôle** : champ descriptif.
- **Contenu typique** : peut être vide ou contenir des chaînes définissant la taille de saisie.

### icon_left
- **Signification** : icône à afficher à gauche du champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : généralement vide ou contient des identifiants d'icône.

### icon_right
- **Signification** : icône à afficher à droite du champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : généralement vide ou contient des identifiants d'icône.

### icon_above
- **Signification** : icône à afficher au-dessus du champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : généralement vide ou contient des identifiants d'icône.

### group_id
- **Signification** : identifiant du groupe de champs auquel ce champ appartient.
- **Rôle** : clé étrangère.
- **Contenu typique** : un UUID faisant référence à un groupe de champs.

### row_order
- **Signification** : détermine l'ordre du champ dans une liste ou un formulaire.
- **Rôle** : champ technique.
- **Contenu typique** : entier indiquant la position.

### sort_order
- **Signification** : précise l'ordre de tri du champ.
- **Rôle** : champ technique.
- **Contenu typique** : entier qui définit la priorité de tri.

### fuzzy_name
- **Signification** : nom alternatif utilisé pour la correspondance approximative.
- **Rôle** : champ descriptif.
- **Contenu typique** : souvent vide ou contient une chaîne à des fins de correspondance.

### fuzzy_field
- **Signification** : précise si le champ est utilisé dans la correspondance approximative.
- **Rôle** : champ descriptif.
- **Contenu typique** : généralement vide ou contient une chaîne.

### fuzzy_primary_field
- **Signification** : indique s'il s'agit du champ principal pour la correspondance approximative.
- **Rôle** : champ technique.
- **Contenu typique** : valeur booléenne (True ou False).

### label_align
- **Signification** : paramètre d'alignement du libellé du champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : souvent vide ou contient une information d'alignement (par ex. gauche, droite, centre).

### calculation_formula
- **Signification** : formule utilisée pour les calculs impliquant le champ.
- **Rôle** : champ technique.
- **Contenu typique** : texte contenant une formule ou une logique de calcul.

### clean_field
- **Signification** : indique si le champ doit être soumis à un nettoyage des données.
- **Rôle** : champ technique.
- **Contenu typique** : valeur booléenne (True ou False).

### alphanumeric_field
- **Signification** : précise si le champ ne doit accepter que des caractères alphanumériques.
- **Rôle** : champ technique.
- **Contenu typique** : valeur booléenne (True ou False).

### placeholder
- **Signification** : texte indicatif du champ de saisie.
- **Rôle** : champ descriptif.
- **Contenu typique** : souvent vide ou contient un texte d'aide.

### coordinates
- **Signification** : données de coordonnées associées au champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : généralement vide ou contient des informations de coordonnées.

### normalized_coordinates
- **Signification** : version normalisée des coordonnées pour garantir la cohérence.
- **Rôle** : champ descriptif.
- **Contenu typique** : généralement vide ou contient des coordonnées normalisées.

### threshold
- **Signification** : valeur de seuil liée à la validation ou au traitement du champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : généralement vide ou contient des valeurs de seuil.

### reference_point
- **Signification** : point de référence utilisé dans les calculs ou le positionnement.
- **Rôle** : champ descriptif.
- **Contenu typique** : souvent vide ou contient des données de point de référence.

### checkbox_group
- **Signification** : identifiant de regroupement pour les champs de type case à cocher.
- **Rôle** : champ descriptif.
- **Contenu typique** : généralement vide ou contient des identifiants de groupe.

### list_of_values
- **Signification** : précise une liste de valeurs autorisées pour le champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : généralement vide ou contient une liste de valeurs.

### enforce_list_of_values
- **Signification** : indique si la liste de valeurs doit être strictement appliquée.
- **Rôle** : champ technique.
- **Contenu typique** : valeur booléenne (True ou False).

### created_by
- **Signification** : identifiant de l'utilisateur qui a créé l'entrée du champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : entier faisant référence à un ID utilisateur.

### created_on
- **Signification** : horodatage de la création du champ.
- **Rôle** : champ technique.
- **Contenu typique** : date et heure en UTC.

### last_modified_on
- **Signification** : horodatage de la dernière modification du champ.
- **Rôle** : champ technique.
- **Contenu typique** : date et heure en UTC.

### is_deleted
- **Signification** : indique si le champ a été marqué comme supprimé.
- **Rôle** : champ technique.
- **Contenu typique** : valeur booléenne (True ou False).

### costing_element
- **Signification** : élément de coût associé au champ.
- **Rôle** : champ descriptif.
- **Contenu typique** : généralement vide ou contient des identifiants d'élément de coût.

### erp_field_name
- **Signification** : nom du champ tel qu'utilisé dans les systèmes ERP.
- **Rôle** : champ descriptif.
- **Contenu typique** : généralement vide ou contient des noms de champs propres à l'ERP.

Cette documentation offre un aperçu détaillé de la structure et de la finalité de chaque colonne de la table `public.field`. Elle sert de guide aux développeurs pour comprendre le modèle de données et son application dans le système.
```
