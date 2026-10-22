# Configuration des recherches par API REST

## Table `public.rest_api_lookup_configurations`

### Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `sub_org_id` : interne
* `data_key` : interne
* `url` : interne
* `method` : interne
* `params` : texte
* `headers` : texte
* `body` : texte
* `body_type` : interne
* `authentication_type` : interne
* `authentication_json` : texte
* `data_base_path` : interne
* `column_paths` : texte
* `created_by` : integer
* `created_on` : horodatage avec fuseau horaire
* `last_modified_on` : horodatage avec fuseau horaire
* `is_deleted` : boolean
* `deleted_on` : horodatage avec fuseau horaire
* `is_template` : boolean
* `is_dynamic` : boolean

### Analyse et description

## Documentation technique : table `public.rest_api_lookup_configurations`

### Introduction

La table `public.rest_api_lookup_configurations` est conçue pour stocker les configurations des recherches (lookups) par API REST au sein d'une organisation. Elle contient les informations essentielles pour effectuer des requêtes API, notamment les détails sur les points de terminaison, les méthodes d'authentification et les configurations de requête et de réponse. Elle semble servir à construire dynamiquement des appels API et à analyser leurs résultats.

### Description des colonnes

#### id

* **Signification** : identifiant unique de chaque entrée de configuration.
* **Rôle** : clé primaire.
* **Contenu typique** : chaînes UUID comme `5e9b3637-79a1-4535-99cf-9247dfa48960`.
* **Remarque** : il s'agit de la clé unique permettant d'identifier une configuration de lookup API précise.

#### org\_id

* **Signification** : identifiant de l'organisation propriétaire de la configuration.
* **Rôle** : clé étrangère.
* **Contenu typique** : chaînes UUID représentant des ID d'organisation.
* **Remarque** : relie la configuration à une organisation.

#### sub\_org\_id

* **Signification** : identifiant d'une sous-organisation au sein de l'organisation principale.
* **Rôle** : clé étrangère.
* **Contenu typique** : chaînes UUID représentant des ID de sous-organisation.
* **Remarque** : permet une granularité supplémentaire au sein des organisations.

#### data\_key

* **Signification** : libellé ou clé servant à identifier les données ou le point de terminaison de l'API.
* **Rôle** : champ descriptif.
* **Contenu typique** : texte descriptif comme `bank_codes`.
* **Remarque** : sert à distinguer différents types de données ou de points de terminaison.

#### url

* **Signification** : URL du point de terminaison de l'API à appeler.
* **Rôle** : champ descriptif.
* **Contenu typique** : chaînes d'URL comme `/M3/m3api-rest/v2/execute/CRS692MI/LstByID`.
* **Remarque** : représente le point de terminaison auquel la requête HTTP est envoyée.

#### method

* **Signification** : méthode HTTP utilisée pour la requête API.
* **Rôle** : champ descriptif.
* **Contenu typique** : méthodes HTTP courantes comme `GET`.
* **Remarque** : détermine le type de requête HTTP à effectuer.

#### params

* **Signification** : paramètres à inclure dans la requête API.
* **Rôle** : champ de configuration.
* **Contenu typique** : JSON ou paires clé-valeur (souvent `None` si inutilisé).
* **Remarque** : contient les paramètres dynamiques de la requête.

#### headers

* **Signification** : en-têtes HTTP à inclure dans la requête.
* **Rôle** : champ de configuration.
* **Contenu typique** : données JSON ou texte (souvent `None` si inutilisé).
* **Remarque** : sert à inclure des métadonnées supplémentaires dans la requête.

#### body

* **Signification** : corps de la requête HTTP.
* **Rôle** : champ de configuration.
* **Contenu typique** : données JSON ou autres données sérialisées (souvent `None` si inutilisé).
* **Remarque** : contient la charge utile des requêtes POST/PUT.

#### body\_type

* **Signification** : précise le format du corps de la requête.
* **Rôle** : champ descriptif.
* **Contenu typique** : types MIME comme `application/json`.
* **Remarque** : indique le type de contenu du corps.

#### authentication\_type

* **Signification** : type d'authentification utilisé pour la requête API.
* **Rôle** : champ descriptif.
* **Contenu typique** : méthodes d'authentification comme `ionapi`.
* **Remarque** : détermine comment la requête sera authentifiée.

#### authentication\_json

* **Signification** : détails de la configuration d'authentification au format JSON.
* **Rôle** : champ de configuration.
* **Contenu typique** : chaînes JSON contenant les informations d'authentification.
* **Remarque** : contient les identifiants et les détails du point de terminaison pour l'authentification.

#### data\_base\_path

* **Signification** : chemin dans la réponse de l'API à partir duquel extraire les données.
* **Rôle** : champ de configuration.
* **Contenu typique** : expressions de chemin JSON comme `$[results][0][records]`.
* **Remarque** : sert à analyser les données de la réponse de l'API.

#### column\_paths

* **Signification** : associe les champs de données aux colonnes pour l'extraction.
* **Rôle** : champ de configuration.
* **Contenu typique** : chaînes JSON associant les champs de la réponse de l'API à des noms de colonnes.
* **Remarque** : facilite l'extraction des données de la réponse de l'API.

#### created\_by

* **Signification** : identifiant de l'utilisateur qui a créé la configuration.
* **Rôle** : champ technique.
* **Contenu typique** : ID entiers comme `1`.
* **Remarque** : permet de savoir qui a créé l'entrée de configuration.

#### created\_on

* **Signification** : horodatage de la création de la configuration.
* **Rôle** : champ technique.
* **Contenu typique** : horodatages comme `2024-01-24T09:14:24.788788Z`.
* **Remarque** : indique la date et l'heure de création.

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification.
* **Rôle** : champ technique.
* **Contenu typique** : horodatages (souvent `None` si non modifiée).
* **Remarque** : enregistre l'heure de la dernière mise à jour.

#### is\_deleted

* **Signification** : indicateur précisant si une configuration est marquée comme supprimée.
* **Rôle** : champ technique.
* **Contenu typique** : valeurs booléennes comme `False`.
* **Remarque** : sert à la suppression logique des configurations.

#### deleted\_on

* **Signification** : horodatage du marquage de la configuration comme supprimée.
* **Rôle** : champ technique.
* **Contenu typique** : horodatages (souvent une valeur de remplacement si non supprimée).
* **Remarque** : enregistre le moment où la configuration a été marquée comme supprimée.

#### is\_template

* **Signification** : indique si la configuration sert de modèle.
* **Rôle** : champ descriptif.
* **Contenu typique** : valeurs booléennes comme `True`.
* **Remarque** : identifie les modèles réutilisables.

#### is\_dynamic

* **Signification** : précise si la configuration est dynamique.
* **Rôle** : champ descriptif.
* **Contenu typique** : valeurs booléennes comme `False`.
* **Remarque** : détermine si la configuration s'adapte à l'évolution des données.
