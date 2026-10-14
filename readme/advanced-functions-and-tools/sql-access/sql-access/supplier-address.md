# Supplier address

## Colonnes

* `org_id` : ID de l'organisation
* `customer_number` : interne
* `supplier_number` : interne
* `address_id` : interne
* `supplier_name` : nom du fournisseur
* `address_1` : interne
* `address_2` : interne
* `address_3` : interne
* `address_4` : interne
* `zip_code` : interne
* `town_city` : interne
* `country_code` : interne
* `created_by` : integer
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean
* `sub_org_id` : interne
* `id` : interne

## Analyse et description

```markdown
# Documentation technique de la table `public.supplier_address`

## Introduction

La table `public.supplier_address` est conçue pour stocker les informations relatives aux adresses des fournisseurs. Elle contient différents champs qui regroupent notamment les identifiants d'organisation, les numéros de client et de fournisseur, plusieurs lignes d'adresse, des coordonnées, des métadonnées de création et de modification, ainsi que l'état de suppression. Cette table est vraisemblablement utilisée dans un système de gestion des fournisseurs et de leurs adresses respectives, ce qui peut être essentiel pour la logistique, la facturation et la prise de contact.

## Description des colonnes

### org_id
- **Signification** : cette colonne contient l'identifiant unique de l'organisation.
- **Rôle** : clé étrangère, pouvant faire référence à une table d'organisations.
- **Contenu typique** : un UUID représentant une organisation.

### customer_number
- **Signification** : cette colonne peut contenir un numéro unique attribué aux clients.
- **Rôle** : identifiant des clients.
- **Contenu typique** : une chaîne alphanumérique représentant des numéros de client.

### supplier_number
- **Signification** : cette colonne contient un numéro unique attribué aux fournisseurs.
- **Rôle** : identifiant des fournisseurs.
- **Contenu typique** : une chaîne numérique représentant des numéros de fournisseur.

### address_id
- **Signification** : cette colonne contient vraisemblablement le type d'adresse, par exemple « Discrete » ou « Text ».
- **Rôle** : champ descriptif pour la catégorisation des adresses.
- **Contenu typique** : des valeurs telles que « Discrete », « Text ».

### supplier_name
- **Signification** : cette colonne contient le nom du fournisseur.
- **Rôle** : champ descriptif pour l'identification du fournisseur.
- **Contenu typique** : le nom du fournisseur, par ex. « Cake Corp. GmbH Qualitätsstrawberrys ».

### address_1
- **Signification** : cette colonne contient la première ligne de l'adresse du fournisseur.
- **Rôle** : champ descriptif pour les informations d'adresse.
- **Contenu typique** : une adresse postale, par ex. « Irrweg. 42, D-12345 Blastadt ».

### address_2
- **Signification** : cette colonne contient la deuxième ligne de l'adresse du fournisseur, le cas échéant.
- **Rôle** : champ complémentaire pour les informations d'adresse.
- **Contenu typique** : des détails d'adresse supplémentaires, souvent laissés vides.

### address_3
- **Signification** : cette colonne contient la troisième ligne de l'adresse du fournisseur, le cas échéant.
- **Rôle** : champ complémentaire pour les informations d'adresse.
- **Contenu typique** : des détails d'adresse supplémentaires, souvent laissés vides.

### address_4
- **Signification** : cette colonne contient la quatrième ligne de l'adresse du fournisseur, le cas échéant.
- **Rôle** : champ complémentaire pour les informations d'adresse.
- **Contenu typique** : des détails d'adresse supplémentaires, souvent laissés vides.

### zip_code
- **Signification** : cette colonne contient le code postal de l'adresse du fournisseur.
- **Rôle** : champ descriptif pour l'identification géographique.
- **Contenu typique** : un code postal numérique, par ex. « 06449 ».

### town_city
- **Signification** : cette colonne contient le nom de la localité ou de la ville de l'adresse du fournisseur.
- **Rôle** : champ descriptif pour l'identification géographique.
- **Contenu typique** : le nom de la localité ou de la ville, par ex. « Aschersleben ».

### country_code
- **Signification** : cette colonne contient le code pays ISO de l'adresse du fournisseur.
- **Rôle** : champ descriptif pour l'identification du pays.
- **Contenu typique** : un code pays à deux lettres, par ex. « DE ».

### created_by
- **Signification** : cette colonne contient l'identifiant de l'utilisateur ou du système qui a créé l'enregistrement.
- **Rôle** : champ technique pour le suivi de la création des enregistrements.
- **Contenu typique** : un entier représentant un ID d'utilisateur.

### created_on
- **Signification** : cette colonne contient l'horodatage de la création de l'enregistrement.
- **Rôle** : champ technique pour le suivi de l'heure de création.
- **Contenu typique** : un horodatage avec fuseau horaire, par ex. « 2021-11-25 11:24:33 UTC ».

### last_modified_on
- **Signification** : cette colonne contient l'horodatage de la dernière modification de l'enregistrement.
- **Rôle** : champ technique pour le suivi de l'heure de la dernière mise à jour.
- **Contenu typique** : un horodatage avec fuseau horaire, souvent laissé à `None`.

### is_deleted
- **Signification** : cette colonne indique si l'enregistrement est marqué comme supprimé.
- **Rôle** : champ technique pour la fonctionnalité de suppression logique.
- **Contenu typique** : une valeur booléenne, par ex. `False`.

### sub_org_id
- **Signification** : cette colonne contient un identifiant de sous-organisation, le cas échéant.
- **Rôle** : clé étrangère ou identifiant des sous-organisations.
- **Contenu typique** : un UUID, souvent laissé vide.

### id
- **Signification** : cette colonne contient l'identifiant unique de l'enregistrement.
- **Rôle** : clé primaire de la table.
- **Contenu typique** : un UUID représentant l'enregistrement.

```
