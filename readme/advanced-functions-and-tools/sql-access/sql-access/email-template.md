# Modèle d’e-mail

## Colonnes

* `id` : interne
* `org_id` : ID de l'organisation
* `name` : interne
* `email_type` : interne
* `value` : texte
* `created_by` : integer
* `created_on` : horodatage avec fuseau horaire
* `last_modified_on` : horodatage avec fuseau horaire
* `is_deleted` : boolean
* `deleted_on` : horodatage avec fuseau horaire
* `subject` : interne
* `last_modified_by` : interne
* `deleted_by` : interne
* `doc_type` : DOC Type

## Analyse et description

```markdown
# Documentation technique de la table `public.email_template`

## Introduction

La table `public.email_template` est conçue pour stocker les modèles d'e-mail utilisés dans le système. Ces modèles sont associés à différentes organisations et servent vraisemblablement à envoyer des communications par e-mail standardisées. La table contient des métadonnées sur les modèles, notamment les détails de création et de modification, et indique également si un modèle a été supprimé.

## Description des colonnes

### id
- **Signification** : identifiant unique de chaque modèle d'e-mail.
- **Rôle** : clé primaire.
- **Contenu typique** : une chaîne UUID telle que `da34c6ed-e659-4392-91ea-3c89f9602198`.
- **Remarque** : sert d'identifiant principal de l'enregistrement du modèle.

### org_id
- **Signification** : identifiant de l'organisation associée au modèle d'e-mail.
- **Rôle** : clé étrangère.
- **Contenu typique** : une chaîne UUID.
- **Remarque** : relie le modèle à une organisation précise.

### name
- **Signification** : nom du modèle d'e-mail.
- **Rôle** : champ descriptif.
- **Contenu typique** : texte descriptif comme `Supplier Magic Link Email`.
- **Remarque** : sert à identifier la finalité du modèle.

### email_type
- **Signification** : type ou catégorie du modèle d'e-mail.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaînes telles que `supplier_invite`.
- **Remarque** : indique le contexte ou l'usage du modèle.

### value
- **Signification** : contenu du modèle d'e-mail, généralement au format HTML.
- **Rôle** : champ de contenu.
- **Contenu typique** : chaîne HTML contenant la mise en page et le contenu de l'e-mail.
- **Remarque** : il s'agit du modèle réellement utilisé dans les e-mails.

### created_by
- **Signification** : identifiant de l'utilisateur qui a créé le modèle.
- **Rôle** : champ de métadonnées.
- **Contenu typique** : un entier représentant un ID utilisateur.
- **Remarque** : permet de savoir qui a créé le modèle.

### created_on
- **Signification** : horodatage de la création du modèle.
- **Rôle** : champ de métadonnées.
- **Contenu typique** : un horodatage comme `2024-07-18 13:29:59 UTC`.
- **Remarque** : enregistre la date et l'heure de création.

### last_modified_on
- **Signification** : horodatage de la dernière modification du modèle.
- **Rôle** : champ de métadonnées.
- **Contenu typique** : un horodatage.
- **Remarque** : permet de suivre la mise à jour la plus récente du modèle.

### is_deleted
- **Signification** : indique si le modèle est marqué comme supprimé.
- **Rôle** : champ technique.
- **Contenu typique** : valeur booléenne, `True` ou `False`.
- **Remarque** : sert à la suppression logique du modèle.

### deleted_on
- **Signification** : horodatage du marquage du modèle comme supprimé.
- **Rôle** : champ de métadonnées.
- **Contenu typique** : un horodatage ou `None` si non supprimé.
- **Remarque** : enregistre le moment de la suppression du modèle.

### subject
- **Signification** : ligne d'objet du modèle d'e-mail.
- **Rôle** : champ de contenu.
- **Contenu typique** : texte comme `Welcome to Testing Ruiz Foods Supplier Portal. Let's help you get set up`.
- **Remarque** : utilisé comme objet de l'e-mail lors de l'envoi du modèle.

### last_modified_by
- **Signification** : identifiant de l'utilisateur qui a modifié le modèle en dernier.
- **Rôle** : champ de métadonnées.
- **Contenu typique** : un identifiant d'utilisateur.
- **Remarque** : permet de savoir qui a modifié le modèle en dernier.

### deleted_by
- **Signification** : identifiant de l'utilisateur qui a marqué le modèle comme supprimé.
- **Rôle** : champ de métadonnées.
- **Contenu typique** : un identifiant d'utilisateur.
- **Remarque** : enregistre qui a supprimé le modèle.

### doc_type
- **Signification** : type ou format du document lié au modèle.
- **Rôle** : champ descriptif.
- **Contenu typique** : chaînes indiquant le type de document.
- **Remarque** : peut se rapporter au format ou à la catégorie du contenu de l'e-mail.
```
