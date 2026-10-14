# Training data

## Table `public.training_data`

### Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `doc_type` : type de document
* `doc_origin` : origine du document
* `doc_locale` : locale du document
* `doc_language` : langue
* `first_page_content` : text
* `supplier_name` : nom du fournisseur
* `supplier_vat` : interne
* `doc_created_on` : timestamp with time zone
* `is_training_sample` : boolean
* `sample_doc_id` : interne
* `sample_file_name` : interne
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean
* `is_table_training_sample` : boolean

### Analyse et description

## Documentation technique de la table `public.training_data`

### Introduction

La table `public.training_data` semble conçue pour stocker diverses données relatives aux documents, vraisemblablement utilisées pour entraîner des modèles ou des systèmes qui traitent et analysent le contenu des documents. La table contient des informations sur le type de document, son origine, sa langue, les détails du fournisseur et des horodatages liés à la création et à la modification des enregistrements, entre autres attributs. Elle semble particulièrement axée sur les factures et les justificatifs médicaux, ce qui suggère une utilisation dans des applications de traitement de données financières ou de santé.

### Description des colonnes

#### id

* **Signification** : identifiant unique de chaque enregistrement de la table.
* **Rôle** : clé primaire.
* **Contenu typique** : un identifiant unique universel (UUID) au format caractères.
* **Remarque** : indispensable pour identifier chaque entrée de manière unique.

#### org\_id

* **Signification** : identifiant de l'organisation associée au document.
* **Rôle** : clé étrangère qui renvoie à un enregistrement d'organisation.
* **Contenu typique** : un UUID représentant une organisation.
* **Remarque** : permet d'associer les documents à des organisations précises.

#### doc\_type

* **Signification** : type de document stocké dans l'enregistrement.
* **Rôle** : champ descriptif.
* **Contenu typique** : des valeurs telles que « INVOICE » ou « MEDICAL\_RECEIPT ».
* **Remarque** : utile pour catégoriser les documents.

#### doc\_origin

* **Signification** : origine du document, sous la forme du code du pays source.
* **Rôle** : champ descriptif.
* **Contenu typique** : un code pays tel que « DE » pour l'Allemagne.
* **Remarque** : indique l'origine géographique du document.

#### doc\_locale

* **Signification** : informations de locale du document.
* **Rôle** : champ descriptif.
* **Contenu typique** : un code de locale tel que « en\_DE ».
* **Remarque** : combine la langue et la région à des fins de localisation.

#### doc\_language

* **Signification** : langue dans laquelle le document est rédigé.
* **Rôle** : champ descriptif.
* **Contenu typique** : un code de langue tel que « en » ou « de ».
* **Remarque** : indique la langue principale utilisée dans le document.

#### first\_page\_content

* **Signification** : contenu de la première page du document.
* **Rôle** : champ descriptif.
* **Contenu typique** : des données textuelles contenant le contenu de la première page du document.
* **Remarque** : peut être utilisé pour l'analyse ou le traitement de texte.

#### supplier\_name

* **Signification** : nom du fournisseur associé au document.
* **Rôle** : champ descriptif.
* **Contenu typique** : le nom du fournisseur sous forme de texte.
* **Remarque** : important pour identifier la source ou l'émetteur du document.

#### supplier\_vat

* **Signification** : numéro d'identification TVA du fournisseur.
* **Rôle** : champ descriptif.
* **Contenu typique** : un numéro de TVA, par ex. « DE 129375678 ».
* **Remarque** : utile pour les processus fiscaux.

#### doc\_created\_on

* **Signification** : horodatage de la création du document.
* **Rôle** : champ descriptif.
* **Contenu typique** : date et heure au format UTC.
* **Remarque** : fournit le contexte temporel de la création du document.

#### is\_training\_sample

* **Signification** : indicateur précisant si l'enregistrement est utilisé comme échantillon d'entraînement.
* **Rôle** : champ technique.
* **Contenu typique** : une valeur booléenne (`True` ou `False`).
* **Remarque** : identifie les enregistrements spécifiquement marqués à des fins d'entraînement.

#### sample\_doc\_id

* **Signification** : identifiant du document échantillon.
* **Rôle** : champ descriptif ou clé étrangère possible.
* **Contenu typique** : un UUID renvoyant à un autre document.
* **Remarque** : peut faire référence à un document associé ou d'origine utilisé pour l'échantillonnage.

#### sample\_file\_name

* **Signification** : nom du fichier associé à l'échantillon de document.
* **Rôle** : champ descriptif.
* **Contenu typique** : un nom de fichier sous forme de texte.
* **Remarque** : utile pour la gestion ou la récupération des fichiers.

#### created\_on

* **Signification** : horodatage de la création de l'enregistrement.
* **Rôle** : champ technique.
* **Contenu typique** : date et heure au format UTC.
* **Remarque** : indique quand l'enregistrement a été ajouté à la base de données.

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification de l'enregistrement.
* **Rôle** : champ technique.
* **Contenu typique** : date et heure au format UTC.
* **Remarque** : permet de suivre la dernière mise à jour de l'enregistrement.

#### is\_deleted

* **Signification** : indicateur précisant si l'enregistrement a été marqué comme supprimé.
* **Rôle** : champ technique.
* **Contenu typique** : une valeur booléenne (`True` ou `False`).
* **Remarque** : prend en charge la fonctionnalité de suppression logique.

#### is\_table\_training\_sample

* **Signification** : indicateur précisant si l'enregistrement est un échantillon d'entraînement propre aux tableaux.
* **Rôle** : champ technique.
* **Contenu typique** : une valeur booléenne (`True` ou `False`).
* **Remarque** : se distingue des échantillons d'entraînement généraux en se concentrant sur les données de tableau.
