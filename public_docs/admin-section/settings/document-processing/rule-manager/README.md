# Gestionnaire de Règles

\


Ce document fournit une explication approfondie des règles de résolution des conflits utilisées dans le système de facturation DocBits. Ces règles sont conçues pour gérer automatiquement les divergences entre les détails de la facture et les données de commande d'achat (PO), garantissant une réconciliation financière précise. Le système applique ces règles pour traiter les lignes de factures, les charges et les taxes, et génère des ajustements ou des notes appropriées lorsque cela est nécessaire.

## Structure des Règles

### &#x20;1. Métadonnées

• version : Identifie la version du fichier de mappage.

• révision : Numéro de révision pour le suivi des modifications.

• auteur : Indique le créateur du fichier de mappage.

• description : Une brève description de l'objectif du fichier.

• created\_at & updated\_at : Horodatages pour indiquer quand le fichier a été créé et mis à jour pour la dernière fois.

### &#x20;2. Configuration d'Exportation

La section de configuration d'exportation définit le mappage entre les champs de données dans le système et les champs correspondants dans les fichiers d'exportation.

• En-tête : Définit les champs d'en-tête pour les données de facturation exportées.

• Lignes de Taxe : Spécifie les champs pour les éléments de ligne de taxe dans l'exportation.

• Charges d'En-tête de Commande : Mappe les champs liés aux charges supplémentaires au niveau de l'en-tête de commande.

• Lignes de Reçu : Mappe les champs pour les éléments de ligne individuels dans un reçu.

• Charges de Ligne de Commande : Définit les champs pour les charges liées à des lignes de commande spécifiques.

• Lignes de Coût : Spécifie les champs pour les lignes d'allocation de coût.

• Note de Débit & Note de Crédit : Définit les champs pour générer des notes de débit et de crédit en cas de divergences.

### 3. Règles de Résolution des Conflits

Ces règles gèrent les divergences entre les données de facturation et les données de PO correspondantes. Chaque règle est composée de plusieurs composants :

• Nom : Le nom descriptif de la règle, indiquant le type de divergence qu'elle traite.

• Section : Indique quelle partie de la facture (par exemple, receipt\_lines, line\_charges) la règle s'applique.

• Actif : Valeur booléenne (vrai ou faux) indiquant si la règle est actuellement active.

• Critères de Correspondance : Conditions qui déclenchent la règle en fonction des comparaisons entre les données de facturation réelles et les données de PO attendues.

• Actions : Définit ce que le système doit faire lorsque la règle est déclenchée, y compris ajuster les valeurs, appliquer des charges ou générer des notes de crédit/débit.

## Éléments Communs dans les Règles

### Opérateurs de Comparaison

Ces opérateurs définissent comment les valeurs de facturation réelles sont comparées aux valeurs de PO attendues :

• égal

• supérieur à

• supérieur ou égal à

• inférieur à

• inférieur ou égal à

• dans la tolérance

• hors tolérance

\


### Statut d'Approbation

Indique si une divergence est approuvée ou non :

• approuvé

• rejeté

• tout

\


### Types d'Actions

Définit des actions spécifiques à entreprendre lorsqu'une divergence est détectée :

\
• ligne de reçu

• ligne de coût

• charge d'en-tête

• charge de ligne

• ligne de taxe

• ligne de reçu de note de débit

• ligne de coût de note de débit

• charge d'en-tête de note de débit

• charge de ligne de note de débit

• ligne de reçu de note de crédit

• ligne de coût de note de crédit

• charge d'en-tête de note de crédit

• charge de ligne de note de crédit

• ligne de taxe de note de crédit

\


### Exemples de Règles

#### [Cas 1, 2, 3 : Quantité et Prix Unitaire Dans la Tolérance](transactionconfig-pro-template/case-1-2-3-quantity-and-unit-price-within-tolerance.md)

\
• Objectif : Gère les scénarios où à la fois la quantité et le prix unitaire sur la facture sont dans les limites de tolérance acceptées par rapport à la PO.

• Action : Le système accepte les valeurs de la facture et calcule le montant total.



#### [Cas 4, 5 : Quantité Dans la Tolérance, Prix Unitaire Hors Tolérance (Approuvé)](./#case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved)

• Objectif : S'applique lorsque la quantité est dans la tolérance mais que le prix unitaire est hors tolérance et a été approuvé.

• Action : Le système ajuste le prix unitaire pour correspondre à la PO et applique toutes les charges de ligne nécessaires.

\


#### [Cas 6 : Quantité Dans la Tolérance, Prix Unitaire Hors Tolérance Négative (Rejeté)](transactionconfig-pro-template/case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)&#x20;

• Objectif : Traite les cas où le prix unitaire est inférieur à ce qui était attendu et hors de la plage de tolérance, entraînant un rejet.

• Action : Le système ajuste le prix unitaire pour correspondre à la PO, génère une note de crédit pour la différence et applique les charges d'en-tête si nécessaire.



### Gestion des Charges et Taxes

### Charge Par Unité de Tolérance

• Les règles sous cette catégorie gèrent les divergences dans les charges par unité, avec des actions spécifiques en fonction de si la charge est dans ou hors de la tolérance et si elle est approuvée ou rejetée.

### Ajustements de Lignes de Taxe

• Ces règles gèrent les divergences fiscales en ajustant les lignes de taxe ou en générant des notes de crédit ou de débit correspondantes en fonction des différences entre les données fiscales de la facture et de la PO.

### Énumérations et Options

• Énumérations : Listes de valeurs prédéfinies garantissant la cohérence à travers les règles (par exemple, opérateurs de comparaison, types d'approbation).

• Options : Choix prédéfinis pour gérer les quantités ou les prix unitaires, offrant une flexibilité dans les définitions de règles.

## Explication des Captures d'Écran

### Capture d'Écran 1 : Interface de Gestion des Règles

<figure><img src="../../../../.gitbook/assets/docbits_rule_manager_interface.png" alt="Docbits Rule Manager Interface"><figcaption></figcaption></figure>

Cette capture d'écran montre l'interface de Gestion des Règles où les administrateurs peuvent voir et gérer toutes les règles de résolution des conflits. Les éléments clés incluent :

• Bouton Ajouter une Règle : Permet d'ajouter de nouvelles règles.

• Liste des Règles : Affiche toutes les règles actives avec des détails tels que le nom, la section et le statut actif.

• Menu Déroulant de Section : Filtre les règles en fonction de la section à laquelle elles s'appliquent (par exemple, Lignes de Reçu, Charges de Ligne).

### Capture d'Écran 2 : Édition Détailée de Règle

<figure><img src="../../../../.gitbook/assets/docbits_rule_editing_detail.png" alt="Docbits Rule Editing Detail"><figcaption></figcaption></figure>

Cette capture d'écran illustre la vue détaillée d'une règle spécifique en cours d'édition. Les éléments clés incluent :

• Section Critères : Définit les conditions sous lesquelles la règle est déclenchée. Par exemple, les critères peuvent spécifier que si la quantité et le prix unitaire diffèrent de la PO mais sont dans la tolérance, la règle doit être appliquée.

• Section Actions : Spécifie quelles actions doivent être prises lorsque les critères sont remplis. Cela peut inclure l'ajustement des lignes de factures, la génération de notes de crédit ou de débit, ou l'application de charges supplémentaires.

• Type de Document et Éléments de Coût : Permet à l'administrateur de mapper des actions spécifiques aux types de documents et aux éléments de coût, offrant une flexibilité dans la gestion de différents scénarios.