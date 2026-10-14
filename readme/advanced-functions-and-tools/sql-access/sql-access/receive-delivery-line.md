# Receive delivery line

## Table `public.receive_delivery_line`

### Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `receive_delivery_id` : interne
* `delivery_number` : interne
* `line_number` : interne
* `item_id` : interne
* `description` : interne
* `shipped_quantity` : double precision
* `status` : interne
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `deleted_on` : timestamp with time zone
* `is_deleted` : boolean
* `purchase_order` : interne
* `sequence_number` : interne
* `sub_org_id` : interne
* `shipped_quantity_unit_code` : interne
* `packing_slip_quantity` : double precision
* `packing_slip_quantity_unit_code` : interne
* `received_quantity` : double precision
* `received_quantity_unit_code` : interne
* `purchase_order_line_number` : interne
* `status_effective_from` : timestamp with time zone
* `purchase_order_sub_line_number` : interne
* `invoiced_quantity` : double precision
* `invoice_matching_status` : interne
* `open_quantity` : double precision
* `last_modified_by` : interne
* `deleted_by` : interne

### Analyse et description

## Documentation de la table `public.receive_delivery_line`

### Introduction

La table `public.receive_delivery_line` semble être un enregistrement détaillé des lignes de livraison et de réception associées aux opérations logistiques et de chaîne d'approvisionnement d'une organisation. Chaque ligne de la table représente une ligne précise d'une livraison et capture des détails tels que la description de l'article, les quantités expédiées et reçues et divers champs de statut. La table est un élément essentiel pour suivre le mouvement des marchandises de l'expédition à la réception, y compris la facturation et la gestion des commandes.

### Description des colonnes

#### id

* **Signification** : identifiant unique de chaque ligne de livraison.
* **Rôle** : clé primaire.
* **Contenu typique** : un identifiant universel unique (UUID).

#### org\_id

* **Signification** : identifiant de l'organisation associée à la livraison.
* **Rôle** : clé étrangère.
* **Contenu typique** : un UUID représentant l'organisation.

#### receive\_delivery\_id

* **Signification** : identifiant reliant la ligne à la transaction de livraison globale.
* **Rôle** : clé étrangère.
* **Contenu typique** : un UUID associé à une transaction de livraison précise.

#### delivery\_number

* **Signification** : numéro unique attribué à la livraison.
* **Rôle** : champ de référence.
* **Contenu typique** : une chaîne représentant le numéro de livraison.

#### line\_number

* **Signification** : numéro de ligne précis au sein d'une livraison.
* **Rôle** : champ de référence.
* **Contenu typique** : chaîne numérique indiquant la séquence de la ligne.

#### item\_id

* **Signification** : identifiant de l'article expédié.
* **Rôle** : champ de référence.
* **Contenu typique** : une chaîne numérique correspondant à un article.

#### description

* **Signification** : description de l'article.
* **Rôle** : champ descriptif.
* **Contenu typique** : description textuelle de l'article, par ex. "FLOUR, WHEAT, UN-BLEACHED ENRICHED, BULK".

#### shipped\_quantity

* **Signification** : quantité de l'article qui a été expédiée.
* **Rôle** : champ quantitatif.
* **Contenu typique** : un nombre décimal indiquant la quantité expédiée.

#### status

* **Signification** : statut actuel de la ligne de livraison.
* **Rôle** : champ de statut.
* **Contenu typique** : texte tel que "Received".

#### created\_by

* **Signification** : identifiant de l'utilisateur ou du système qui a créé l'enregistrement.
* **Rôle** : champ d'audit.
* **Contenu typique** : entier représentant un ID utilisateur.

#### created\_on

* **Signification** : horodatage de la création de l'enregistrement.
* **Rôle** : champ d'audit.
* **Contenu typique** : date et heure avec fuseau horaire.

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification.
* **Rôle** : champ d'audit.
* **Contenu typique** : date et heure avec fuseau horaire.

#### deleted\_on

* **Signification** : horodatage du marquage de l'enregistrement comme supprimé.
* **Rôle** : champ d'audit.
* **Contenu typique** : date et heure avec fuseau horaire, souvent null sauf en cas de suppression.

#### is\_deleted

* **Signification** : indique si l'enregistrement est marqué comme supprimé.
* **Rôle** : champ technique.
* **Contenu typique** : valeur booléenne, true ou false.

#### purchase\_order

* **Signification** : référence à la commande d'achat associée.
* **Rôle** : champ de référence.
* **Contenu typique** : chaîne alphanumérique représentant un numéro de commande d'achat.

#### sequence\_number

* **Signification** : numéro de séquence de la ligne de livraison.
* **Rôle** : champ de référence.
* **Contenu typique** : chaîne numérique, souvent null.

#### sub\_org\_id

* **Signification** : identifiant d'une sous-organisation concernée.
* **Rôle** : clé étrangère.
* **Contenu typique** : UUID, souvent null.

#### shipped\_quantity\_unit\_code

* **Signification** : unité de mesure de la quantité expédiée.
* **Rôle** : champ de référence.
* **Contenu typique** : code représentant les unités, par ex. "LBP".

#### packing\_slip\_quantity

* **Signification** : quantité selon le bordereau de livraison.
* **Rôle** : champ quantitatif.
* **Contenu typique** : nombre décimal, souvent null.

#### packing\_slip\_quantity\_unit\_code

* **Signification** : code d'unité de la quantité du bordereau de livraison.
* **Rôle** : champ de référence.
* **Contenu typique** : code représentant les unités, souvent null.

#### received\_quantity

* **Signification** : quantité d'articles effectivement reçue.
* **Rôle** : champ quantitatif.
* **Contenu typique** : nombre décimal indiquant la quantité reçue.

#### received\_quantity\_unit\_code

* **Signification** : code d'unité de la quantité reçue.
* **Rôle** : champ de référence.
* **Contenu typique** : code représentant les unités, par ex. "LBP".

#### purchase\_order\_line\_number

* **Signification** : numéro de ligne dans la commande d'achat.
* **Rôle** : champ de référence.
* **Contenu typique** : chaîne numérique.

#### status\_effective\_from

* **Signification** : date et heure à partir desquelles le statut est effectif.
* **Rôle** : champ de statut.
* **Contenu typique** : date et heure avec fuseau horaire, souvent null.

#### purchase\_order\_sub\_line\_number

* **Signification** : numéro de sous-ligne dans la commande d'achat.
* **Rôle** : champ de référence.
* **Contenu typique** : chaîne numérique, souvent "000".

#### invoiced\_quantity

* **Signification** : quantité qui a été facturée.
* **Rôle** : champ quantitatif.
* **Contenu typique** : nombre décimal.

#### invoice\_matching\_status

* **Signification** : statut du processus de rapprochement des factures.
* **Rôle** : champ de statut.
* **Contenu typique** : code de statut textuel, par ex. "9.0".

#### open\_quantity

* **Signification** : quantité qui reste ouverte ou pas encore traitée.
* **Rôle** : champ quantitatif.
* **Contenu typique** : nombre décimal.

#### last\_modified\_by

* **Signification** : identifiant de l'utilisateur qui a modifié l'enregistrement en dernier.
* **Rôle** : champ d'audit.
* **Contenu typique** : UUID de l'utilisateur, souvent null.

#### deleted\_by

* **Signification** : identifiant de l'utilisateur qui a marqué l'enregistrement comme supprimé.
* **Rôle** : champ d'audit.
* **Contenu typique** : UUID de l'utilisateur, souvent null.
