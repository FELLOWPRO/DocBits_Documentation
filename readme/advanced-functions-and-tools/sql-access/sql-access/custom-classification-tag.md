# Étiquette de classification personnalisée

## Table `public.custom_classification_tag`

### Colonnes

* `id`: integer
* `org_id`: ID to organisation
* `name`: internal
* `created_by`: integer
* `created_on` : horodatage avec fuseau horaire
* `last_modified_on` : horodatage avec fuseau horaire
* `is_deleted`: boolean

### Analyse et description

## Documentation technique de la table `public.custom_classification_tag`

### Introduction

La table `public.custom_classification_tag` sert à gérer les balises de classification personnalisées au sein d'une organisation. Elle enregistre les informations essentielles sur chaque balise, notamment son association à une organisation, les détails de sa création et de sa modification, ainsi que son état dans le cycle de vie.

### Description des colonnes

#### id

* **Signification** : un identifiant unique pour chaque balise de classification.
* **Rôle** : clé primaire.
* **Contenu typique** : une valeur entière qui identifie chaque enregistrement de la table de manière unique.

#### org\_id

* **Signification** : l'identifiant de l'organisation à laquelle appartient la balise de classification.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne de caractères, vraisemblablement un UUID, représentant l'ID unique de l'organisation.

#### name

* **Signification** : le nom ou le libellé de la balise de classification.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne désignant le nom ou la description de la balise. Elle peut être vide si le nom n'est pas renseigné.

#### created\_by

* **Signification** : l'identifiant de l'utilisateur qui a créé la balise de classification.
* **Rôle** : clé étrangère.
* **Contenu typique** : un entier représentant l'ID utilisateur du créateur.

#### created\_on

* **Signification** : l'horodatage indiquant quand la balise de classification a été créée.
* **Rôle** : champ technique.
* **Contenu typique** : un horodatage avec fuseau horaire, indiquant la date et l'heure exactes de création.

#### last\_modified\_on

* **Signification** : l'horodatage de la dernière modification apportée à la balise de classification.
* **Rôle** : champ technique.
* **Contenu typique** : un horodatage avec fuseau horaire, qui peut valoir `None` si aucune modification n'a eu lieu depuis la création.

#### is\_deleted

* **Signification** : un indicateur précisant si la balise de classification a été marquée comme supprimée.
* **Rôle** : champ technique.
* **Contenu typique** : une valeur booléenne (`True` ou `False`), où `False` signifie que la balise est active et `True` qu'elle a été supprimée ou désactivée.
