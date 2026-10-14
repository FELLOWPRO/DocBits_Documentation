# Electronic document extraction attributes

## Table `public.electronic_document_extraction_attributes`

### Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `doc_type_key` : interne
* `sub_doc_type_key` : interne
* `electronic_document_type` : interne
* `attribute_name` : interne
* `attribute_type` : interne
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean
* `deleted_on` : timestamp with time zone
* `last_modified_by` : interne
* `deleted_by` : interne

### Analyse et description

## Documentation technique de `public.electronic_document_extraction_attributes`

### Introduction

La table `public.electronic_document_extraction_attributes` semble gérer les attributs liés à l'extraction de documents électroniques. Elle stocke diverses caractéristiques et métadonnées sur les types de documents électroniques, leurs méthodes de traitement et les organisations associées. La table semble prendre en charge des fonctions telles que l'identification du type de document, les transformations, les aperçus et les descriptions de structure, indispensables pour traiter efficacement les documents électroniques.

### Description des colonnes

#### id

* **Signification** : identifiant unique de chaque enregistrement de la table.
* **Rôle** : clé primaire.
* **Contenu typique** : une chaîne UUID qui identifie de manière unique chaque entrée d'attribut d'extraction de document.
* **Remarque** : sert de référence unique pour chaque ligne.

#### org\_id

* **Signification** : identifiant de l'organisation liée aux attributs du document.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne UUID qui renvoie à l'organisation associée.
* **Remarque** : relie les attributs d'extraction de document à une organisation précise.

#### doc\_type\_key

* **Signification** : clé représentant le type de document.
* **Rôle** : identifiant pour la catégorisation des documents.
* **Contenu typique** : une chaîne qui indique le type de document, comme 'INVOICE' ou 'ORDER\_CONFIRMATION'.
* **Remarque** : sert à déterminer la catégorie du document.

#### sub\_doc\_type\_key

* **Signification** : représente une sous-catégorie du type de document principal.
* **Rôle** : identifiant pour une classification plus fine.
* **Contenu typique** : Null ou une chaîne de sous-type spécifique.
* **Remarque** : utile pour une granularité supplémentaire dans la classification des documents.

#### electronic\_document\_type

* **Signification** : format ou norme du document électronique.
* **Rôle** : champ descriptif du format du document.
* **Contenu typique** : chaînes comme 'EDI' ou 'FACTURX'.
* **Remarque** : indique la norme ou le format du document.

#### attribute\_name

* **Signification** : nom de l'attribut lié au processus d'extraction du document.
* **Rôle** : champ descriptif.
* **Contenu typique** : chaînes comme 'PREVIEW' ou 'TRANSFORMATION'.
* **Remarque** : décrit l'attribut spécifique lié au traitement du document.

#### attribute\_type

* **Signification** : type de l'attribut lié à l'extraction du document.
* **Rôle** : champ descriptif.
* **Contenu typique** : chaînes telles que 'XSLT' ou 'JSON'.
* **Remarque** : précise le format de données ou la méthode utilisée pour l'attribut.

#### created\_by

* **Signification** : ID de l'utilisateur qui a créé l'enregistrement.
* **Rôle** : clé étrangère.
* **Contenu typique** : entier représentant un ID utilisateur.
* **Remarque** : permet de savoir qui a créé l'enregistrement à l'origine.

#### created\_on

* **Signification** : horodatage de la création de l'enregistrement.
* **Rôle** : champ technique.
* **Contenu typique** : date et heure en UTC.
* **Remarque** : indique l'heure de création de l'enregistrement.

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification de l'enregistrement.
* **Rôle** : champ technique.
* **Contenu typique** : date et heure en UTC, ou null si non modifié.
* **Remarque** : permet de suivre la mise à jour la plus récente de l'enregistrement.

#### is\_deleted

* **Signification** : indique si l'enregistrement est marqué comme supprimé.
* **Rôle** : champ technique.
* **Contenu typique** : valeur booléenne, `True` ou `False`.
* **Remarque** : facilite la gestion de la suppression logique.

#### deleted\_on

* **Signification** : horodatage du marquage de l'enregistrement comme supprimé.
* **Rôle** : champ technique.
* **Contenu typique** : date et heure en UTC, ou date ancienne par défaut si non supprimé.
* **Remarque** : sert à suivre quand l'enregistrement a été supprimé.

#### last\_modified\_by

* **Signification** : ID de l'utilisateur qui a modifié l'enregistrement en dernier.
* **Rôle** : clé étrangère.
* **Contenu typique** : chaîne UUID, ou null si non modifié.
* **Remarque** : identifie l'utilisateur responsable de la dernière modification.

#### deleted\_by

* **Signification** : ID de l'utilisateur qui a marqué l'enregistrement comme supprimé.
* **Rôle** : clé étrangère.
* **Contenu typique** : chaîne UUID, ou null si non supprimé.
* **Remarque** : permet de savoir qui a effectué la suppression.

Cette documentation offre un aperçu détaillé de la structure de la table et de ses colonnes, afin de faciliter la compréhension et l'utilisation par les développeurs et les administrateurs de bases de données.
