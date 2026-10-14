# Document type

## Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `document_key` : interne
* `document_name` : interne
* `title` : interne
* `translation_key` : interne
* `extraction_type` : interne
* `document_type_category` : interne
* `has_table` : boolean
* `sort_order` : integer
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean

## Analyse et description

```markdown
# Table : public.document_type

## Introduction
La table `public.document_type` est conçue pour stocker des informations relatives aux différents types de documents au sein d'une organisation. Elle contient des identifiants et des métadonnées pour la catégorisation, la gestion et le traitement des documents, tels que les clés de document, les noms, les titres, les clés de traduction et d'autres attributs qui facilitent la manipulation et la recherche des documents. La table suit également la création et la modification de ces entrées, et prend en charge les états actif et supprimé.

## Description des colonnes

### id
- **Signification** : identifiant unique de chaque entrée de type de document.
- **Rôle** : clé primaire.
- **Contenu typique** : une chaîne UUID qui identifie de manière unique une entrée de type de document.

### org_id
- **Signification** : identifiant de l'organisation à laquelle appartient le type de document.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID faisant référence à une organisation.

### document_key
- **Signification** : clé unique d'identification du type de document, éventuellement utilisée dans les systèmes de stockage ou de traitement des documents.
- **Rôle** : identifiant.
- **Contenu typique** : une chaîne qui combine les informations du type de document avec l'ID de l'organisation.

### document_name
- **Signification** : nom interne du type de document.
- **Rôle** : champ descriptif.
- **Contenu typique** : une chaîne en majuscules représentant le nom du type de document.

### title
- **Signification** : titre d'affichage du type de document dans les interfaces utilisateur.
- **Rôle** : champ descriptif.
- **Contenu typique** : une chaîne en casse de titre, lisible et descriptive du type de document.

### translation_key
- **Signification** : clé utilisée pour localiser le titre ou le nom du document dans différentes langues.
- **Rôle** : prise en charge de l'internationalisation.
- **Contenu typique** : une chaîne en minuscules qui sert de référence pour les systèmes de traduction.

### extraction_type
- **Signification** : indique la méthode ou le processus par lequel les données sont extraites du document.
- **Rôle** : champ de métadonnées.
- **Contenu typique** : actuellement non renseigné dans les données d'exemple.

### document_type_category
- **Signification** : classe le type de document dans des catégories ou classifications plus larges.
- **Rôle** : champ de catégorisation.
- **Contenu typique** : actuellement non renseigné dans les données d'exemple.

### has_table
- **Signification** : indique si le type de document comporte des données tabulaires.
- **Rôle** : champ de métadonnées.
- **Contenu typique** : valeur booléenne (`True` ou `False`) indiquant la présence de données tabulaires.

### sort_order
- **Signification** : définit l'ordre dans lequel les types de document sont triés ou affichés.
- **Rôle** : champ de tri.
- **Contenu typique** : un entier représentant la séquence de tri.

### created_by
- **Signification** : identifiant de l'utilisateur qui a créé l'entrée de type de document.
- **Rôle** : champ de métadonnées.
- **Contenu typique** : un entier faisant référence à un ID utilisateur.

### created_on
- **Signification** : horodatage indiquant quand l'entrée de type de document a été créée.
- **Rôle** : champ d'audit.
- **Contenu typique** : date et heure avec information de fuseau horaire.

### last_modified_on
- **Signification** : horodatage indiquant la date de dernière modification de l'entrée de type de document.
- **Rôle** : champ d'audit.
- **Contenu typique** : date et heure avec information de fuseau horaire, `None` si jamais modifiée.

### is_deleted
- **Signification** : indique si l'entrée de type de document est marquée comme supprimée.
- **Rôle** : champ d'état.
- **Contenu typique** : valeur booléenne (`True` ou `False`) indiquant l'état de suppression.
```
