# Sales order

## Table `public.sales_order`

### Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `sub_org_id` : interne
* `location_id` : interne
* `order_number` : interne
* `customer_purchase_order` : interne
* `customer_id` : interne
* `customer_name` : interne
* `warehouse_id` : interne
* `warehouse_name` : interne
* `transportation_method` : interne
* `requested_delivery_date` : timestamp with time zone
* `order_date` : timestamp with time zone
* `sales_person_id` : interne
* `sales_person_name` : interne
* `ship_to_party_id` : interne
* `ship_to_party_name` : interne
* `ship_to_party_city` : interne
* `ship_to_party_state` : interne
* `ship_to_party_country` : interne
* `ship_to_party_zip` : interne
* `status` : interne
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean
* `deleted_on` : timestamp with time zone
* `preview_path` : interne
* `last_modified_by` : interne
* `deleted_by` : interne

### Analyse et description

## Documentation technique de la table `public.sales_order`

### Introduction

La table `public.sales_order` est conçue pour capturer et stocker les informations relatives aux commandes clients dans un contexte commercial. Cela comprend des détails sur la commande, le client, la logistique et diverses métadonnées associées au cycle de vie de la commande. La table sert de référentiel central pour suivre le statut et l'historique des transactions de vente.

### Description des colonnes

#### id

* **Signification** : identifiant unique de chaque commande client.
* **Rôle** : clé primaire.
* **Contenu typique** : une chaîne UUID (par ex. `'6ffe4673-7563-44dc-8e71-855e8f25534a'`).

#### org\_id

* **Signification** : identifiant de l'organisation qui a créé la commande client.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne UUID représentant l'organisation (par ex. `'23f3d697-7411-4c95-981d-faf089d266be'`).

#### sub\_org\_id

* **Signification** : identifiant d'une sous-organisation, le cas échéant.
* **Rôle** : clé étrangère.
* **Contenu typique** : peut être `NULL` si non applicable.

#### location\_id

* **Signification** : identifiant du site associé à la commande client.
* **Rôle** : clé étrangère.
* **Contenu typique** : un code sous forme de chaîne représentant un site (par ex. `'028'`).

#### order\_number

* **Signification** : numéro unique attribué à la commande client.
* **Rôle** : champ technique pour le suivi des commandes.
* **Contenu typique** : une chaîne (par ex. `'0010174175'`).

#### customer\_purchase\_order

* **Signification** : numéro de référence de la commande d'achat du client.
* **Rôle** : champ technique pour les références croisées.
* **Contenu typique** : une chaîne (par ex. `'1YFNC3'`).

#### customer\_id

* **Signification** : identifiant du client qui passe la commande.
* **Rôle** : clé étrangère.
* **Contenu typique** : un code sous forme de chaîne (par ex. `'35623000'`).

#### customer\_name

* **Signification** : nom du client.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne (par ex. `'DOLLAR GENERAL'`).

#### warehouse\_id

* **Signification** : identifiant de l'entrepôt chargé d'exécuter la commande.
* **Rôle** : clé étrangère.
* **Contenu typique** : un code sous forme de chaîne (par ex. `'028'`).

#### warehouse\_name

* **Signification** : nom de l'entrepôt.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne (par ex. `'USCS - DENTON, TX'`).

#### transportation\_method

* **Signification** : mode de transport pour la livraison de la commande.
* **Rôle** : champ descriptif.
* **Contenu typique** : un code sous forme de chaîne (par ex. `'001'`).

#### requested\_delivery\_date

* **Signification** : date de livraison demandée par le client.
* **Rôle** : champ descriptif.
* **Contenu typique** : un horodatage (par ex. `None`).

#### order\_date

* **Signification** : date de passation de la commande.
* **Rôle** : champ descriptif.
* **Contenu typique** : un horodatage (par ex. `datetime.datetime(2024, 1, 29, 0, 0, tzinfo=datetime.timezone.utc)`).

#### sales\_person\_id

* **Signification** : identifiant du commercial qui traite la commande.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne (par ex. `'ROBERTDOCK'`).

#### sales\_person\_name

* **Signification** : nom du commercial.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne (par ex. `'ROBERT DOCKINS'`).

#### ship\_to\_party\_id

* **Signification** : identifiant de la partie à laquelle la commande est expédiée.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne (par ex. `'35623000 009'`).

#### ship\_to\_party\_name

* **Signification** : nom de la partie à laquelle la commande est expédiée.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne (par ex. `'DOLLAR GENERAL DC 98061/96460'`).

#### ship\_to\_party\_city

* **Signification** : ville de l'adresse de livraison.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne (par ex. `'SAN ANTONIO'`).

#### ship\_to\_party\_state

* **Signification** : État de l'adresse de livraison.
* **Rôle** : champ descriptif.
* **Contenu typique** : peut être `NULL`.

#### ship\_to\_party\_country

* **Signification** : pays de l'adresse de livraison.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne (par ex. `'US'`).

#### ship\_to\_party\_zip

* **Signification** : code postal de l'adresse de livraison.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne (par ex. `'78218'`).

#### status

* **Signification** : statut actuel de la commande client.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne (par ex. `'Allocated'`).

#### created\_by

* **Signification** : identifiant de l'utilisateur qui a créé l'entrée.
* **Rôle** : champ technique.
* **Contenu typique** : un entier (par ex. `1`).

#### created\_on

* **Signification** : horodatage de la création de l'entrée.
* **Rôle** : champ technique.
* **Contenu typique** : un horodatage (par ex. `datetime.datetime(2024, 3, 6, 11, 48, 43, 237208, tzinfo=datetime.timezone.utc)`).

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification.
* **Rôle** : champ technique.
* **Contenu typique** : un horodatage (par ex. `datetime.datetime(2024, 9, 4, 8, 42, 32, 912247, tzinfo=datetime.timezone.utc)`).

#### is\_deleted

* **Signification** : indicateur précisant si la commande est marquée comme supprimée.
* **Rôle** : champ technique.
* **Contenu typique** : un booléen (par ex. `False`).

#### deleted\_on

* **Signification** : horodatage du marquage de la commande comme supprimée.
* **Rôle** : champ technique.
* **Contenu typique** : date par défaut si non supprimée (par ex. `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`).

#### preview\_path

* **Signification** : chemin d'un document d'aperçu de la commande client.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne représentant un chemin de fichier (par ex. `'previews/sales_order/23f3d697-7411-4c95-981d-faf089d266be/0010174175/0010174175_preview.pdf'`).

#### last\_modified\_by

* **Signification** : identifiant de l'utilisateur qui a modifié l'entrée en dernier.
* **Rôle** : champ technique.
* **Contenu typique** : peut être `NULL`.

#### deleted\_by

* **Signification** : identifiant de l'utilisateur qui a marqué l'entrée comme supprimée.
* **Rôle** : champ technique.
* **Contenu typique** : peut être `NULL`.
