# PO match tolerance

## Table `public.po_match_tolerance`

### Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `item_number` : interne
* `supplier_item_number` : interne
* `description` : interne
* `unit_price_tolerance` : double precision
* `quantity_tolerance` : double precision
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean
* `unit_price_tolerance_type` : interne
* `quantity_tolerance_type` : interne

### Analyse et description

## Documentation technique de la table `public.po_match_tolerance`

### Introduction

La table `public.po_match_tolerance` est conçue pour gérer et stocker les niveaux de tolérance associés aux processus de rapprochement des commandes d'achat (PO). Il s'agit généralement des écarts admissibles sur les prix unitaires et les quantités entre les marchandises commandées et reçues. Chaque entrée de la table représente les paramètres de tolérance d'articles précis, ce qui peut aider les organisations à garantir la cohérence et l'exactitude de leurs processus d'achat.

### Description des colonnes

#### id

* **Signification** : identifiant unique de chaque entrée de la table.
* **Rôle** : clé primaire.
* **Contenu typique** : une chaîne UUID qui identifie de manière unique chaque enregistrement de paramètre de tolérance.

#### org\_id

* **Signification** : identifiant de l'organisation associée aux paramètres de tolérance.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne UUID reliée à l'organisation dans le système.

#### item\_number

* **Signification** : numéro d'article pour lequel les paramètres de tolérance sont définis.
* **Rôle** : identifiant métier.
* **Contenu typique** : une chaîne représentant le code ou le numéro de l'article dans le stock de l'organisation.

#### supplier\_item\_number

* **Signification** : numéro d'article tel que fourni par le fournisseur.
* **Rôle** : identifiant métier.
* **Contenu typique** : une chaîne pouvant être `None` si elle n'est pas fournie, représentant le code ou le numéro de l'article chez le fournisseur.

#### description

* **Signification** : description textuelle de l'article.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne fournissant des détails sur l'article, pouvant être `None`.

#### unit\_price\_tolerance

* **Signification** : écart admissible sur le prix unitaire de l'article.
* **Rôle** : règle métier.
* **Contenu typique** : une valeur numérique indiquant la tolérance en pourcentage ou en valeur absolue sur le prix unitaire.

#### quantity\_tolerance

* **Signification** : écart admissible sur la quantité de l'article.
* **Rôle** : règle métier.
* **Contenu typique** : une valeur numérique indiquant la tolérance en pourcentage ou en valeur absolue sur la quantité.

#### created\_by

* **Signification** : identifiant de l'utilisateur qui a créé l'entrée.
* **Rôle** : champ d'audit/de journalisation.
* **Contenu typique** : un entier faisant généralement référence à un ID utilisateur du système.

#### created\_on

* **Signification** : horodatage de la création de l'entrée.
* **Rôle** : champ d'audit/de journalisation.
* **Contenu typique** : une valeur datetime avec fuseau horaire indiquant la date et l'heure de création.

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification de l'entrée.
* **Rôle** : champ d'audit/de journalisation.
* **Contenu typique** : une valeur datetime avec fuseau horaire indiquant la dernière mise à jour de l'enregistrement, pouvant être `None` si non modifié.

#### is\_deleted

* **Signification** : indique si l'entrée est supprimée logiquement.
* **Rôle** : indicateur technique de suppression logique.
* **Contenu typique** : une valeur booléenne où `False` signifie active et `True` signifie supprimée logiquement.

#### unit\_price\_tolerance\_type

* **Signification** : définit le type de tolérance sur le prix unitaire (par ex. pourcentage ou valeur absolue).
* **Rôle** : règle métier.
* **Contenu typique** : une chaîne, souvent 'value', indiquant le type de mesure de la tolérance.

#### quantity\_tolerance\_type

* **Signification** : définit le type de tolérance sur la quantité (par ex. pourcentage ou valeur absolue).
* **Rôle** : règle métier.
* **Contenu typique** : une chaîne, souvent 'value', indiquant le type de mesure de la tolérance.

Cette documentation offre un aperçu détaillé de chaque champ de la table `public.po_match_tolerance` et éclaire leur contenu possible ainsi que leur rôle dans le contexte de la gestion des commandes d'achat.
