# Purchase Order line

## Table `public.purchase_order_line`

### Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `purchase_order_id` : interne
* `purchase_order_number` : interne
* `line_number` : interne
* `item_id` : interne
* `supplier_item_id` : interne
* `description` : interne
* `quantity` : double precision
* `unit_code` : interne
* `unit_price` : double precision
* `total_amount` : double precision
* `currency` : interne
* `status` : interne
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `deleted_on` : timestamp with time zone
* `is_deleted` : boolean
* `open_quantity` : double precision
* `received_quantity` : double precision
* `confirmed_quantity` : double precision
* `note` : texte
* `sub_org_id` : interne
* `sub_line_number` : interne
* `unit_price_per` : double precision
* `buyer_id` : interne
* `buyer_name` : interne
* `unit_code_price` : interne
* `geo_code` : interne
* `promised_delivery_date` : timestamp with time zone
* `delivery_method` : interne
* `requested_ship_date` : date
* `received_base_mou_quantity` : double precision
* `extended_amount` : double precision

### Analyse et description

## Documentation technique de la table `public.purchase_order_line`

### Introduction

La table `public.purchase_order_line` est conçue pour stocker des informations détaillées sur chaque ligne d'une commande d'achat. Elle capture divers attributs d'une ligne de commande d'achat, tels que les détails de l'article, les quantités, les prix et les statuts. Cette table est essentielle pour gérer et suivre les commandes d'achat et leur état d'exécution dans un contexte organisationnel.

### Description des colonnes

#### id

* **Signification** : identifiant unique de chaque ligne de commande d'achat.
* **Rôle** : clé primaire.
* **Contenu typique** : une chaîne UUID identifiant de manière unique la ligne de commande d'achat.

#### org\_id

* **Signification** : identifiant de l'organisation associée à la commande d'achat.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne UUID faisant référence à une organisation.

#### purchase\_order\_id

* **Signification** : identifiant de la commande d'achat à laquelle appartient la ligne.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne UUID faisant référence à une commande d'achat.

#### purchase\_order\_number

* **Signification** : numéro attribué à la commande d'achat.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne représentant le numéro de la commande d'achat.

#### line\_number

* **Signification** : numéro de ligne de l'article dans la commande d'achat.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne indiquant la séquence de la ligne dans la commande d'achat.

#### item\_id

* **Signification** : identifiant de l'article commandé.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne représentant le code de l'article.

#### supplier\_item\_id

* **Signification** : identifiant de l'article propre au fournisseur.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne, pouvant être null si le fournisseur ne la fournit pas.

#### description

* **Signification** : description de l'article.
* **Rôle** : champ descriptif.
* **Contenu typique** : une description textuelle de l'article.

#### quantity

* **Signification** : nombre d'unités commandées.
* **Rôle** : champ descriptif.
* **Contenu typique** : une valeur numérique indiquant la quantité commandée.

#### unit\_code

* **Signification** : code représentant l'unité de mesure de l'article.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne représentant les unités, par ex. 'EA' pour l'unité (each).

#### unit\_price

* **Signification** : prix par unité de l'article.
* **Rôle** : champ descriptif.
* **Contenu typique** : une valeur numérique représentant le prix par unité.

#### total\_amount

* **Signification** : montant total de la ligne (quantité \* prix unitaire).
* **Rôle** : champ descriptif.
* **Contenu typique** : une valeur numérique représentant le montant total.

#### currency

* **Signification** : devise dans laquelle l'achat est effectué.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne représentant le code de la devise, par ex. 'USD'.

#### status

* **Signification** : statut actuel de la ligne de commande d'achat.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne indiquant le statut, par ex. 'Received', 'Invoiced'.

#### created\_by

* **Signification** : identifiant de l'utilisateur qui a créé l'entrée.
* **Rôle** : clé étrangère.
* **Contenu typique** : un entier représentant l'ID utilisateur.

#### created\_on

* **Signification** : horodatage de la création de l'entrée.
* **Rôle** : champ technique.
* **Contenu typique** : un horodatage avec information de fuseau horaire.

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification.
* **Rôle** : champ technique.
* **Contenu typique** : un horodatage avec information de fuseau horaire, pouvant être null si jamais modifiée.

#### deleted\_on

* **Signification** : horodatage du marquage de l'entrée comme supprimée.
* **Rôle** : champ technique.
* **Contenu typique** : un horodatage avec information de fuseau horaire, pouvant être null si non supprimée.

#### is\_deleted

* **Signification** : indique si l'entrée a été marquée comme supprimée.
* **Rôle** : champ technique.
* **Contenu typique** : valeur booléenne (true/false).

#### open\_quantity

* **Signification** : quantité pas encore reçue ni facturée.
* **Rôle** : champ descriptif.
* **Contenu typique** : une valeur numérique, généralement zéro si la ligne est entièrement reçue.

#### received\_quantity

* **Signification** : quantité qui a été reçue.
* **Rôle** : champ descriptif.
* **Contenu typique** : une valeur numérique indiquant la quantité reçue.

#### confirmed\_quantity

* **Signification** : quantité confirmée par le fournisseur.
* **Rôle** : champ descriptif.
* **Contenu typique** : une valeur numérique, pouvant être null si elle n'est pas confirmée.

#### note

* **Signification** : notes supplémentaires concernant la ligne de commande d'achat.
* **Rôle** : champ descriptif.
* **Contenu typique** : texte, pouvant inclure des instructions particulières ou des commentaires.

#### sub\_org\_id

* **Signification** : identifiant de la sous-organisation associée à la ligne de commande d'achat.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne, éventuellement null si non applicable.

#### sub\_line\_number

* **Signification** : numéro de sous-ligne dans la commande d'achat.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne représentant la séquence de la sous-ligne.

#### unit\_price\_per

* **Signification** : prix unitaire de base de l'article.
* **Rôle** : champ descriptif.
* **Contenu typique** : une valeur numérique représentant le prix unitaire de base.

#### buyer\_id

* **Signification** : identifiant de l'acheteur responsable de l'achat.
* **Rôle** : clé étrangère.
* **Contenu typique** : une chaîne représentant l'ID de l'acheteur.

#### buyer\_name

* **Signification** : nom de l'acheteur responsable.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne représentant le nom de l'acheteur.

#### unit\_code\_price

* **Signification** : code d'unité lié à la tarification.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne, similaire à unit\_code.

#### geo\_code

* **Signification** : code géographique de livraison.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne représentant un lieu géographique.

#### promised\_delivery\_date

* **Signification** : date promise pour la livraison.
* **Rôle** : champ descriptif.
* **Contenu typique** : un horodatage avec information de fuseau horaire.

#### delivery\_method

* **Signification** : mode de livraison de la ligne de commande d'achat.
* **Rôle** : champ descriptif.
* **Contenu typique** : une chaîne représentant le mode de livraison.

#### requested\_ship\_date

* **Signification** : date d'expédition demandée.
* **Rôle** : champ descriptif.
* **Contenu typique** : une valeur de type date.

#### received\_base\_mou\_quantity

* **Signification** : quantité reçue en unités de mesure de base.
* **Rôle** : champ descriptif.
* **Contenu typique** : une valeur numérique indiquant la quantité reçue en unités de mesure de base (MOU).

#### extended\_amount

* **Signification** : montant étendu de la ligne.
* **Rôle** : champ descriptif.
* **Contenu typique** : une valeur numérique représentant le montant étendu, qui peut être égal à total\_amount si aucune remise ni aucun frais supplémentaire ne s'applique.
