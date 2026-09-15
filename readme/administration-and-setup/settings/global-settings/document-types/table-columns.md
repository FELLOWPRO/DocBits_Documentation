# Colonnes de Tableau

Les colonnes de tableau définissent les colonnes du tableau des éléments de ligne d'un type de document : ce que DocBits extrait dans chaque colonne, ce que l'utilisateur voit sur l'écran de validation et ce qui est envoyé à l'ERP lors de l'exportation.

**Où :** Paramètres → Paramètres globaux → Types de documents → Colonnes de tableau

<figure><img src="../../../../.gitbook/assets/table-columns_list.png" alt="Liste des colonnes de tableau avec les indicateurs Obligatoire, Lecture seule, Masquée et Utiliser l'IA par colonne"><figcaption><p>Colonnes de tableau : une ligne par colonne, les indicateurs se modifient directement dans la liste</p></figcaption></figure>

## Ce que vous voyez

Chaque ligne correspond à une colonne d'un tableau. La liste affiche :

| Colonne | Signification |
|---|---|
| **Nom de la colonne** | Nom technique, généré à partir du titre (majuscules, tirets bas). Utilisé dans les scripts, les mappages d'exportation et l'API. Ne peut plus être modifié par la suite. |
| **Titre** | Libellé affiché sur l'écran de validation. Modifiez-le avec l'icône de traduction dans la colonne *Actions* (*Mettre à jour la clé de traduction*). |
| **Type de colonne** | `AMOUNT`, `STRING`, `DATE`, `NUMBER`, `BOOLEAN` ou `CURRENCY`. Détermine la validation et le formatage. |
| **Nom du tableau** | Le tableau auquel appartient la colonne, par exemple `INVOICE_TABLE`. |
| **Obligatoire** | Le document ne peut pas être approuvé tant que cette colonne est vide dans une ligne, quelle qu'elle soit. |
| **Lecture seule** | Les utilisateurs voient la valeur mais ne peuvent pas la modifier. |
| **Masquée** | La colonne n'est ni affichée ni exportée. Sert à désactiver les colonnes par défaut dont vous n'avez pas besoin. |
| **Utiliser l'IA** | L'extraction de tableau par IA remplit cette colonne, même lorsque le fournisseur dispose de règles entraînées. |
| **Actions** | Icône de traduction : renommer le titre. Icône d'information : origine du libellé affiché (votre traduction, la valeur par défaut, la clé). Menu à trois points : *Supprimer*, uniquement pour les colonnes créées par votre organisation ; les colonnes par défaut peuvent seulement être masquées. |

Deux boutons au-dessus de la liste :

* **Créer un nouveau tableau** : un second tableau d'éléments de ligne pour le type de document (par exemple un tableau des frais à côté du tableau des articles).
* **Ajouter une nouvelle colonne de tableau** : ouvre la boîte de dialogue décrite dans la section « Ajouter une nouvelle colonne » ci-dessous.

## Colonnes par défaut et colonnes personnalisées

Chaque type de document est livré avec un ensemble de colonnes par défaut (pour les factures : numéro d'article, description, quantité, prix unitaire, montant total, taxe, etc.). Elles appartiennent à DocBits, pas à votre organisation ; elles ne peuvent donc pas être supprimées, masquez-les à la place. Les colonnes que vous ajoutez vous-même appartiennent à votre organisation et peuvent être supprimées.

{% hint style="info" %}
**Les modifications ne s'appliquent qu'aux nouveaux documents.** Une colonne ajoutée, masquée ou supprimée apparaît sur les documents téléversés ou redémarrés après la modification. Les documents déjà présents sur le tableau de bord conservent leur tableau tel qu'il a été extrait. Redémarrez un document pour qu'il prenne en compte la nouvelle configuration.
{% endhint %}

## Objectif et utilisation

Une colonne de tableau est un champ du tableau des éléments de ligne. Tout ce que DocBits fait avec un tableau (extraction, validation, correspondance de bon de commande, exportation) s'appuie sur les colonnes configurées ici.

### Où une colonne intervient

| Emplacement | Rôle de la colonne à cet endroit |
|---|---|
| **Écran de validation** | Une colonne du tableau des éléments de ligne. Le *Titre* sert d'en-tête, le *Type de colonne* détermine l'éditeur (montant, date, texte, oui/non). Les colonnes masquées ne sont pas affichées. |
| **Entraînement de tableau** | Lorsque vous entraînez le tableau d'un fournisseur, vous associez chaque colonne détectée à l'une des colonnes configurées ici. Seules les colonnes configurées peuvent être mappées. |
| **Extraction de tableau par IA** | L'IA remplit les colonnes configurées. Une colonne marquée *Utiliser l'IA* est remplie par l'IA même pour les fournisseurs disposant de règles entraînées. |
| **Règles de validation** | Les contrôles par ligne, tels que *quantité × prix unitaire = total de ligne*, s'exécutent sur les colonnes par défaut `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **Correspondance de bon de commande** | Nécessite les colonnes par défaut numéro d'article, prix unitaire, quantité et montant total. Sans elles, le document affiche *Line Item Table is missing Mandatory column for PO*. |
| **Exportation** | Chaque colonne non masquée fait partie des données de lignes envoyées à l'ERP. Le mappage d'exportation référence le *Nom de la colonne*. |
| **Scripts** | Les scripts lisent et écrivent les colonnes par *Nom de la colonne*, par exemple `row["TOTAL_AMOUNT"]`. |

### Portée

* Les colonnes de tableau sont configurées **par tableau**, et un tableau appartient à un **type de document**. Les colonnes des factures n'ont aucune incidence sur les bons de livraison.
* La configuration est définie **par organisation**. Les sous-organisations en héritent.
* Les colonnes *remplies* pour un fournisseur donné dépendent de l'entraînement de ce fournisseur ou de l'IA ; la configuration des colonnes indique seulement quelles colonnes existent.

### Raisons courantes de modifier la configuration

* Une valeur propre au client doit être saisie par ligne (centre de coûts, numéro de projet, numéro d'article interne) → ajoutez une colonne.
* Une colonne par défaut n'est jamais utilisée et encombre l'écran de validation → masquez-la.
* Une colonne doit toujours être renseignée avant l'exportation → marquez-la *Obligatoire*.
* Une valeur provient de la recherche dans l'ERP et ne doit pas être modifiée par les utilisateurs → marquez-la *Lecture seule*.
* L'IA capture une colonne mieux que les règles entraînées (par exemple les descriptions en texte libre) → marquez-la *Utiliser l'IA*.

## Ajouter une nouvelle colonne

Ajoutez une colonne lorsqu'une valeur doit être saisie par ligne et que les colonnes par défaut ne la couvrent pas : un centre de coûts, un numéro de projet, un numéro d'article interne.

### Avant de commencer

* Déterminez le **tableau** auquel la colonne appartient. La plupart des types de document n'ont qu'un seul tableau (par exemple `INVOICE_TABLE`). Si la liste est vide, cliquez d'abord sur **Créer un nouveau tableau** ; la boîte de dialogue ne demande qu'un nom de tableau.
* Déterminez le **type** : `AMOUNT` pour les montants, `NUMBER` pour les quantités, `DATE`, `BOOLEAN` pour oui/non, `CURRENCY` pour un code devise ISO, `STRING` pour tout le reste. Le type ne peut plus être modifié après l'enregistrement.
* Vérifiez si une **colonne par défaut** ayant la même signification existe déjà mais est masquée. Les colonnes masquées figurent dans la liste avec l'indicateur *Masquée* activé ; réaffichez-la au lieu de créer un doublon.

### Étapes

1. Ouvrez **Paramètres → Paramètres globaux → Types de documents → Colonnes de tableau**.
2. Cliquez sur **Ajouter une nouvelle colonne de tableau**.

<figure><img src="../../../../.gitbook/assets/table-columns_add-dialog.png" alt="Boîte de dialogue Ajouter une nouvelle colonne de tableau avec Titre, Colonne obligatoire, Type de colonne et Tableau"><figcaption><p>Ajouter une nouvelle colonne de tableau</p></figcaption></figure>

3. Renseignez la boîte de dialogue :

| Champ | Valeur à saisir |
|---|---|
| **Titre** | Libellé que l'utilisateur voit sur l'écran de validation, par exemple `Cost Centre`. Lettres et chiffres uniquement. DocBits en dérive le *Nom de la colonne* technique (`COST_CENTRE`). |
| **La colonne est-elle obligatoire ?** | Cochez la case si le document ne doit pas être approuvé tant que la colonne est vide dans une ligne. |
| **Sélectionner le type de colonne** | Voir la liste des types ci-dessus. |
| **Sélectionner le tableau** | Le tableau qui reçoit la colonne. |

4. Cliquez sur **Continuer**. La colonne apparaît dans la liste avec les indicateurs *Lecture seule*, *Masquée* et *Utiliser l'IA* désactivés. Activez-les dans la liste si nécessaire, voir la section « Modifier et supprimer des colonnes » ci-dessous.

### Après l'ajout

* La colonne est **vide sur les documents existants**. Elle est remplie sur les documents téléversés ou redémarrés après la modification.
* Pour les fournisseurs disposant de **règles entraînées**, ouvrez l'un de leurs documents dans l'entraînement de tableau et mappez la nouvelle colonne, sinon elle restera vide pour ce fournisseur. Voir [Définition des tables et des colonnes](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* Avec l'**extraction de tableau par IA**, l'IA remplit la colonne si la valeur est reconnaissable sur le document. Marquez la colonne *Utiliser l'IA* si le fournisseur a des règles entraînées mais que cette colonne doit tout de même provenir de l'IA.
* Ajoutez la colonne au **mappage d'exportation** si l'ERP doit la recevoir, voir [Exportation](../../document-processing/export.md).

### Messages

| Message | Signification |
|---|---|
| *Column name already exists* | Une colonne portant ce nom technique existe déjà dans le tableau. Choisissez un autre titre. |
| *Column name already exists – Please activate it in Table Column settings* | Une colonne par défaut masquée porte ce nom. Désactivez son indicateur *Masquée* au lieu d'en créer une nouvelle. |
| *No table exists. Please create table before creating columns.* | Le type de document n'a pas encore de tableau : cliquez d'abord sur **Créer un nouveau tableau**. |

## Modifier et supprimer des colonnes

Tout, sauf le titre, se modifie directement dans la liste ; il n'y a pas de boîte de dialogue de modification.

### Activer ou désactiver un indicateur

Cochez ou décochez la case dans la ligne. La modification est enregistrée immédiatement (*Successfully saved*).

| Indicateur | Activé | Désactivé |
|---|---|---|
| **Obligatoire** | L'approbation est bloquée tant que la colonne est vide dans une ligne ; l'écran de validation marque la cellule. | Les cellules vides sont autorisées. |
| **Lecture seule** | La valeur est affichée mais ne peut pas être écrasée. À utiliser pour les valeurs issues d'une recherche ou d'un script. | Les utilisateurs peuvent modifier la cellule. |
| **Masquée** | La colonne disparaît de l'écran de validation et de l'exportation. Ses données sont conservées. | La colonne est affichée et exportée. |
| **Utiliser l'IA** | L'extraction de tableau par IA remplit cette colonne, y compris pour les fournisseurs disposant de règles entraînées. | La colonne est remplie par les règles entraînées, ou par l'IA lorsqu'il n'existe aucune règle. |

{% hint style="info" %}
Les indicateurs prennent effet sur les documents téléversés ou redémarrés **après** la modification. Les documents ouverts conservent leur tableau actuel jusqu'à leur redémarrage.
{% endhint %}

### Renommer le titre

Cliquez sur l'icône de traduction dans la colonne *Actions* (*Mettre à jour la clé de traduction*), saisissez le nouveau libellé et confirmez. L'icône d'information à côté indique le libellé actuellement en vigueur et son origine. Seul le libellé change ; le *Nom de la colonne* technique reste identique, de sorte que les scripts, les mappages d'exportation et les règles entraînées continuent de fonctionner.

### Modifier le type ou le tableau

Impossible. Masquez la colonne (ou supprimez-la s'il s'agit de l'une des vôtres) et ajoutez-en une nouvelle avec le bon type.

### Supprimer une colonne

L'action de suppression n'est proposée que pour les colonnes créées par votre organisation. Les colonnes par défaut ne peuvent pas être supprimées ; masquez-les.

1. Ouvrez le menu à trois points dans la colonne *Actions* et choisissez **Supprimer**. L'entrée est absente pour les colonnes par défaut.
2. Confirmez.

Ce qui se passe :

* La colonne est retirée de la configuration. Les documents traités **à partir de maintenant** ne l'ont plus.
* Les documents déjà extraits conservent la colonne et ses valeurs jusqu'à leur redémarrage.
* Les règles entraînées qui mappaient cette colonne continuent de fonctionner pour les autres colonnes ; le mappage de la colonne supprimée est ignoré.
* Si la colonne est référencée dans un mappage d'exportation ou un script, supprimez cette référence ; sinon l'exportation ou le script échoue avec une erreur de colonne manquante.

### Annuler une suppression

Une colonne supprimée ne peut pas être restaurée depuis la liste. Ajoutez-la de nouveau avec le même titre : le nom technique étant dérivé du titre, une colonne créée avec le même titre reçoit le même *Nom de la colonne* et les mappages existants correspondent à nouveau.

## Bonnes pratiques

### Conservez les colonnes par défaut pour les montants et les quantités

Les contrôles par ligne (*quantité × prix unitaire = total de ligne*) et la correspondance de bon de commande recherchent les colonnes par défaut `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. Si vous créez vos propres colonnes pour ces valeurs à la place, les contrôles ne s'exécutent pas et la correspondance de bon de commande signale des colonnes obligatoires manquantes. Renommez le *titre* si la formulation ne vous convient pas ; conservez la colonne.

### Masquer plutôt que supprimer

Les colonnes par défaut dont vous n'avez pas besoin se masquent, elles ne se suppriment pas ; elles ne peuvent de toute façon pas être supprimées. Pour vos propres colonnes, masquer est aussi le choix le plus sûr tant que vous n'êtes pas certain qu'aucun script ni mappage d'exportation ne référence encore la colonne.

### Ne rendez obligatoire que ce qui bloque l'exportation

Chaque colonne obligatoire doit être renseignée dans chaque ligne avant qu'un utilisateur puisse approuver le document. Réservez cet indicateur aux valeurs que l'ERP rejette lorsqu'elles manquent (par exemple le centre de coûts dans un export comptable), pas aux valeurs simplement utiles.

### Utilisez *Lecture seule* pour les valeurs issues d'une recherche

Les valeurs qu'un script ou une recherche dans les données de base écrit dans le tableau (description d'article issue de la fiche article, code de taxe issu du fournisseur) devraient être en lecture seule, afin que les utilisateurs corrigent la source plutôt que la copie.

### Utilisez l'IA par colonne, pas par fournisseur

Pour un fournisseur disposant de règles entraînées, la plupart des colonnes sont correctement extraites par les règles. Si une colonne n'est pas fiable (descriptions longues qui passent à la ligne, remise qui se trouve parfois à un autre endroit), activez *Utiliser l'IA* sur cette colonne uniquement. Les règles conservent le reste.

### Nommez les colonnes pour l'ERP, pas pour le document

Le *Nom de la colonne* se retrouve dans les mappages d'exportation et les scripts. `COST_CENTRE` est plus facile à mapper que `KST` et ne change pas lorsqu'un fournisseur l'imprime différemment.

### Testez sur un document redémarré

Après une modification, redémarrez un document existant du type de document et ouvrez-le : la nouvelle colonne apparaît, la colonne masquée a disparu, les cellules obligatoires sont marquées. Ce n'est qu'ensuite que vous déployez la modification auprès des utilisateurs.

### Un tableau par structure de lignes

Ne créez un second tableau que lorsqu'un type de document comporte réellement deux tableaux indépendants (par exemple les lignes d'articles et un tableau des frais distinct). Les tableaux vides superflus apparaissent sur chaque document du type.

## Dépannage

### La nouvelle colonne n'apparaît pas sur l'écran de validation

* Le document a été traité avant l'ajout de la colonne. Les modifications s'appliquent aux documents téléversés ou redémarrés ensuite : **redémarrez le document** (Tableau de bord → menu du document → Redémarrer).
* La colonne est **masquée**. Vérifiez l'indicateur dans la liste des colonnes de tableau.
* La colonne a été ajoutée à un **autre tableau** que celui affiché. L'écran de validation affiche les tableaux du type de document ; comparez la colonne *Nom du tableau*.
* Le document n'est pas du type de document que vous avez configuré.

### La colonne est présente mais toujours vide

* Le fournisseur dispose de **règles entraînées** et la nouvelle colonne n'y est pas mappée. Ouvrez l'un des documents du fournisseur dans l'entraînement de tableau et mappez la colonne, ou activez *Utiliser l'IA* sur la colonne.
* Avec l'extraction par IA, la valeur n'est pas reconnaissable sur le document (pas d'en-tête, abréviation, autre langue). Ajoutez une [étiquette de tableau AI](../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) qui nomme la colonne, ou mappez-la dans l'entraînement.

### « Column name already exists »

Une colonne portant le même nom technique existe déjà dans le tableau. Si elle n'apparaît pas dans la liste, il s'agit d'une colonne par défaut masquée : le message indique *Please activate it in Table Column settings*. Désactivez *Masquée* sur cette colonne au lieu d'en créer une nouvelle.

### L'approbation est bloquée par une colonne obligatoire

Le message sur le tableau nomme la colonne. Remplissez la cellule dans chaque ligne, ou (si la valeur n'existe pas sur ce document) décochez *Obligatoire* pour la colonne, redémarrez le document et réessayez. Demandez-vous si la colonne doit vraiment être obligatoire (voir la section « Bonnes pratiques » ci-dessus).

### L'IA remplit une colonne avec la mauvaise valeur

Cas typique : `CHARGES` reçoit le total de ligne, et chaque ligne échoue alors au contrôle du total de ligne avec *Line total does not match quantity x unit price (expected …, got …)*, car les frais font partie de la formule `quantité × prix unitaire + frais`.

* Décochez *Utiliser l'IA* sur la colonne si les règles entraînées la capturent correctement.
* Si le fournisseur n'a pas de règles, entraînez le tableau une fois (entraînement de tableau) afin que la colonne soit liée à la bonne position, ou masquez la colonne si le fournisseur n'imprime jamais cette valeur.
* En dernier recours, *Ignorer la validation du tableau* dans Plus de paramètres du type de document désactive tous les contrôles de tableau pour l'ensemble du type de document ; l'écart n'est alors plus détecté, pas plus que les colonnes obligatoires vides.

### Correspondance de bon de commande : « Line Item Table is missing Mandatory column »

La correspondance de bon de commande nécessite les colonnes par défaut numéro d'article, prix unitaire, quantité et montant total. L'une d'elles est masquée ou a été remplacée par une colonne personnalisée. Réaffichez la colonne par défaut, ou mappez la valeur sur celle-ci dans l'entraînement de tableau.

### Un script ou une exportation échoue après la suppression d'une colonne

Le script ou le mappage d'exportation référence encore le *Nom de la colonne* supprimé. Supprimez la référence, ou ajoutez de nouveau la colonne avec le même titre ; le nom technique est dérivé du titre et correspond à nouveau.

## Pages associées

* [Dépannage de l'extraction de table](../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md) : qualité d'extraction, OCR, E-Text
* [Training Line Fields / Table Training](../../../setup/document-training/training-line-fields-table-training/README.md) : apprendre à DocBits où se trouve le tableau d'un fournisseur
* [Définition des tables et des colonnes](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md)
* [Tableau AI](../../../../end-user-and-partner-section/end-user-section/ai-table/README.md) : ce que l'utilisateur voit sur l'écran de validation
