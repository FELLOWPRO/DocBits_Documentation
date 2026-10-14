# Fellow kv table column rule

## Table `public.fellow_kv_table_column_rule`

### Colonnes

* `id` : interne
* `docType` : interne
* `tableName` : interne
* `dlfName` : interne
* `multi_line` : boolean
* `filterID1` : interne
* `filterID2` : interne
* `filterID3` : interne
* `tfidf_doc_id` : interne
* `tfidf_id` : interne
* `valuePattern` : interne
* `coordsY0` : integer
* `coordsY1` : integer
* `coordsX0` : integer
* `coordsX1` : integer
* `normalizedY0` : numeric
* `normalizedY1` : numeric
* `normalizedX0` : numeric
* `normalizedX1` : numeric
* `width` : integer
* `height` : integer
* `patternLeft` : interne
* `patternRight` : interne
* `patternAbove` : interne
* `patternBelow` : interne
* `wordLeft` : interne
* `wordAbove` : interne
* `ruleWeight` : integer
* `user_id` : integer
* `org_id` : ID de l'organisation
* `created_on` : timestamp with time zone
* `last_modified_on` : timestamp with time zone
* `is_deleted` : boolean
* `is_new` : boolean

### Analyse et description

## Documentation technique de `public.fellow_kv_table_column_rule`

### Introduction

La table `public.fellow_kv_table_column_rule` semble conçue pour stocker des règles et des motifs destinés au traitement ou à l'extraction de données à partir de documents. On le déduit de la présence de champs tels que `docType`, `tableName`, `dlfName` ainsi que de divers champs de motifs et de coordonnées. La table semble faciliter l'application de règles à différents types de documents, permettant la reconnaissance de motifs et l'extraction de données à partir de documents structurés comme les factures ou les contrats.

### Description des colonnes

#### id

* **Signification** : identifiant unique de chaque règle.
* **Rôle** : clé primaire.
* **Contenu typique** : chaînes UUID.
* **Remarque** : indispensable pour identifier chaque ligne de manière unique.

#### docType

* **Signification** : type de document auquel s'applique la règle.
* **Rôle** : champ descriptif.
* **Contenu typique** : types de documents comme 'INVOICE', 'CONTRACT'.
* **Remarque** : aide à catégoriser les règles par type de document.

#### tableName

* **Signification** : nom du tableau dans lequel la règle est appliquée.
* **Rôle** : champ descriptif.
* **Contenu typique** : noms de tableaux comme 'INVOICE\_TABLE'.
* **Remarque** : indique le contexte dans lequel la règle est appliquée.

#### dlfName

* **Signification** : nom du champ ou de la colonne concerné dans le document.
* **Rôle** : champ descriptif.
* **Contenu typique** : noms de champs tels que 'COUNTRY\_ORIGIN'.
* **Remarque** : précise le champ cible de l'extraction de données.

#### multi\_line

* **Signification** : indique si la règle s'applique à un texte sur plusieurs lignes.
* **Rôle** : indicateur booléen.
* **Contenu typique** : `True` ou `False`.
* **Remarque** : utile pour traiter les champs de texte multilignes.

#### filterID1, filterID2, filterID3

* **Signification** : filtres ou conditions d'application de la règle.
* **Rôle** : champs descriptifs ou conditionnels.
* **Contenu typique** : éventuellement des chaînes représentant des conditions de filtre.
* **Remarque** : servent à affiner l'application de la règle selon certaines conditions.

#### tfidf\_doc\_id, tfidf\_id

* **Signification** : identifiants liés au traitement TF-IDF.
* **Rôle** : rôles ou identifiants de type clé étrangère.
* **Contenu typique** : chaînes UUID.
* **Remarque** : probablement liés à l'analyse de texte et à l'extraction de caractéristiques.

#### valuePattern

* **Signification** : motif regex pour l'extraction de valeurs.
* **Rôle** : champ de motif.
* **Contenu typique** : expressions régulières.
* **Remarque** : définit le motif utilisé pour identifier et extraire les valeurs.

#### coordsY0, coordsY1, coordsX0, coordsX1

* **Signification** : coordonnées définissant le cadre englobant pour l'extraction.
* **Rôle** : champs de coordonnées.
* **Contenu typique** : entiers représentant des positions en pixels.
* **Remarque** : définissent la zone d'intérêt dans un document pour l'extraction de données.

#### normalizedY0, normalizedY1, normalizedX0, normalizedX1

* **Signification** : coordonnées normalisées pour l'extraction.
* **Rôle** : champs de coordonnées.
* **Contenu typique** : valeurs numériques représentant des positions proportionnelles.
* **Remarque** : servent à définir des zones indépendamment de la résolution.

#### width, height

* **Signification** : dimensions de la zone définie par les coordonnées.
* **Rôle** : champs de dimensions.
* **Contenu typique** : valeurs entières.
* **Remarque** : aident à définir la taille de la zone d'extraction.

#### patternLeft, patternRight, patternAbove, patternBelow

* **Signification** : motifs contextuels entourant les données cibles.
* **Rôle** : champs de motifs.
* **Contenu typique** : expressions régulières.
* **Remarque** : fournissent un contexte sur l'emplacement des données par rapport aux autres textes.

#### wordLeft, wordAbove

* **Signification** : mots spécifiques situés à proximité des données cibles.
* **Rôle** : champs contextuels.
* **Contenu typique** : mots ou expressions spécifiques.
* **Remarque** : aident à affiner la recherche des données cibles à partir des mots voisins.

#### ruleWeight

* **Signification** : importance ou priorité de la règle.
* **Rôle** : champ de poids ou de priorité.
* **Contenu typique** : valeurs entières.
* **Remarque** : des valeurs plus élevées peuvent indiquer une priorité ou une importance supérieure.

#### user\_id

* **Signification** : identifiant de l'utilisateur qui a créé ou modifié la règle.
* **Rôle** : clé étrangère.
* **Contenu typique** : valeurs entières.
* **Remarque** : relie la règle à un utilisateur précis.

#### org\_id

* **Signification** : identifiant de l'organisation associée à la règle.
* **Rôle** : clé étrangère.
* **Contenu typique** : chaînes UUID.
* **Remarque** : associe la règle à une organisation.

#### created\_on

* **Signification** : horodatage de la création de la règle.
* **Rôle** : champ technique.
* **Contenu typique** : horodatage avec fuseau horaire.
* **Remarque** : utile pour suivre l'historique de création de la règle.

#### last\_modified\_on

* **Signification** : horodatage de la dernière modification de la règle.
* **Rôle** : champ technique.
* **Contenu typique** : horodatage avec fuseau horaire ou `None`.
* **Remarque** : permet de suivre les modifications de la règle dans le temps.

#### is\_deleted

* **Signification** : indique si la règle est marquée comme supprimée.
* **Rôle** : indicateur booléen.
* **Contenu typique** : `True` ou `False`.
* **Remarque** : sert à la suppression logique des règles.

#### is\_new

* **Signification** : indique si la règle vient d'être créée.
* **Rôle** : indicateur booléen.
* **Contenu typique** : `True` ou `False`.
* **Remarque** : aide à repérer les règles ajoutées récemment.
