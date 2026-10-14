# Additional charge costing element

## Table `public.additional_charge_costing_element`

### Colonnes

* `id`: internal
* `org_id`: ID to organisation
* `costing_element`: internal
* `description`: internal
* `charge_type`: internal
* `distribution_method`: internal
* `distribution_type`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `sub_org_id`: internal
* `charge_count`: integer
* `charge_icon`: internal
* `charge_category`: internal
* `charge_sequence_number`: integer
* `charge_operator`: integer
* `last_modified_by`: internal
* `deleted_by`: internal

### Analyse et description

## Documentation de la table : `public.additional_charge_costing_element`

### Introduction

La table `public.additional_charge_costing_element` sert à gérer et à stocker des informations sur les différents éléments de coûts de frais supplémentaires au sein d'une organisation. Elle contient des données sur le type de frais, leur mode de répartition, ainsi que des métadonnées administratives telles que les détails de création et de modification. Cette table est vraisemblablement utilisée pour la gestion financière et opérationnelle d'une organisation, en se concentrant sur les coûts supplémentaires qui doivent être suivis et analysés.

### Description des colonnes

#### id

* **Signification** : cette colonne stocke un identifiant unique pour chaque enregistrement de la table.
* **Rôle** : clé primaire.
* **Contenu typique** : une chaîne alphanumérique unique qui identifie chaque enregistrement d'élément de coût.

#### org\_id

* **Signification** : l'identifiant de l'organisation à laquelle appartient cet élément de coût.
* **Rôle** : clé étrangère.
* **Contenu typique** : un UUID représentant l'organisation.

#### costing\_element

* **Signification** : un identifiant ou un code de l'élément de coût.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne alphanumérique qui représente l'élément de coût spécifique.

#### description

* **Signification** : une description textuelle de l'élément de coût.
* **Rôle** : champ descriptif.
* **Contenu typique** : une brève explication textuelle de l'élément de coût.

#### charge\_type

* **Signification** : le type de frais associé à cet élément de coût.
* **Rôle** : champ descriptif.
* **Contenu typique** : un code ou un court texte indiquant le type de frais.

#### distribution\_method

* **Signification** : la méthode selon laquelle les frais sont répartis.
* **Rôle** : champ descriptif.
* **Contenu typique** : un code ou un court texte indiquant la méthode de répartition.

#### distribution\_type

* **Signification** : le type de répartition des frais.
* **Rôle** : champ descriptif.
* **Contenu typique** : un code ou un court texte indiquant le type de répartition.

#### created\_by

* **Signification** : l'identifiant de l'utilisateur qui a créé l'enregistrement.
* **Rôle** : champ administratif.
* **Contenu typique** : un entier représentant l'ID de l'utilisateur.

#### created\_on

* **Signification** : l'horodatage indiquant quand l'enregistrement a été créé.
* **Rôle** : champ administratif.
* **Contenu typique** : un horodatage avec information de fuseau horaire.

#### last\_modified\_on

* **Signification** : l'horodatage de la dernière modification apportée à l'enregistrement.
* **Rôle** : champ administratif.
* **Contenu typique** : un horodatage avec information de fuseau horaire.

#### is\_deleted

* **Signification** : indique si l'enregistrement est marqué comme supprimé.
* **Rôle** : champ technique.
* **Contenu typique** : une valeur booléenne (`True` ou `False`).

#### deleted\_on

* **Signification** : l'horodatage du moment où l'enregistrement a été marqué comme supprimé.
* **Rôle** : champ administratif.
* **Contenu typique** : un horodatage avec information de fuseau horaire, ou `None` s'il n'est pas supprimé.

#### sub\_org\_id

* **Signification** : l'identifiant d'une sous-organisation liée à l'élément de coût.
* **Rôle** : clé étrangère.
* **Contenu typique** : un UUID représentant la sous-organisation.

#### charge\_count

* **Signification** : le nombre de frais associés à l'élément de coût.
* **Rôle** : champ descriptif.
* **Contenu typique** : un entier représentant le nombre de frais.

#### charge\_icon

* **Signification** : l'icône ou le symbole associé aux frais.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne représentant l'icône, vraisemblablement un chemin ou un identifiant.

#### charge\_category

* **Signification** : la catégorie à laquelle appartiennent les frais.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne représentant la catégorie de frais.

#### charge\_sequence\_number

* **Signification** : le numéro de séquence servant à ordonner les frais.
* **Rôle** : champ descriptif.
* **Contenu typique** : un entier utilisé pour séquencer les frais.

#### charge\_operator

* **Signification** : l'identifiant de l'opérateur responsable des frais.
* **Rôle** : champ descriptif.
* **Contenu typique** : un entier représentant l'ID de l'opérateur.

#### last\_modified\_by

* **Signification** : l'identifiant de l'utilisateur qui a modifié l'enregistrement en dernier.
* **Rôle** : champ administratif.
* **Contenu typique** : une chaîne représentant l'ID de l'utilisateur, éventuellement `None` si l'enregistrement n'a jamais été modifié.

#### deleted\_by

* **Signification** : l'identifiant de l'utilisateur qui a marqué l'enregistrement comme supprimé.
* **Rôle** : champ administratif.
* **Contenu typique** : une chaîne représentant l'ID de l'utilisateur, éventuellement `None` s'il n'est pas supprimé.
