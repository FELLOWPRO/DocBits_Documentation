# Plus de paramètres

## Aperçu

Dans la section "Plus de paramètres", vous pouvez trouver diverses options liées aux types de documents individuels. Une fois qu'un paramètre est activé, il s'appliquera uniquement à ce type de document spécifique. Cette page fournit un bref aperçu de ce que fait chaque paramètre.

## Comment accéder

1.  Naviguez vers **Paramètres** → **Paramètres globaux** → **Types de documents**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_1_fr.png" alt=""><figcaption></figcaption></figure>
2.  Sélectionnez le type de document souhaité et cliquez sur **Plus de paramètres**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_2_fr.png" alt=""><figcaption></figcaption></figure>

## Extraction de table

* **Ignorer la validation du tableau** : Permet de contourner le processus de validation standard pour les données de tableau. Cette option est utile dans les scénarios où une gestion des données flexible est requise ou lorsque certaines étapes de validation peuvent être ignorées pour améliorer les performances lors du traitement des données.

## Détection des doublons

* [**Détection des documents en double**](duplicate-document-handling.md) : Cela vous permet de détecter et de gérer les documents en double.

## En révision

* **Formulaire de conception en cours d'examen** : Configurez la mise en page des formulaires de révision à l'aide du **Module de création de mise en page**. Cette mise en page détermine comment le contenu est présenté lors du processus de révision du document. Pour des instructions détaillées sur l'utilisation du **Module de création de mise en page**, cliquez [ici](../../../../setup/document-types/layout-builder.md).

## Rejeter

* **Concevoir le formulaire de rejet** : Configurez la mise en page à l'aide du **Module de création de mise en page** pour le formulaire de rejet affiché lors du processus de révision du document. Pour des instructions détaillées sur l'utilisation du **Module de création de mise en page**, cliquez [ici](../../../../setup/document-types/layout-builder.md).

## Exporter le format PDF

* **Format du fichier d'exportation** : Vous permet de spécifier le format PDF à utiliser lors de l'exportation des documents.

## Approbation

* **Approuver avant l'exportation** : Assure que les documents doivent être approuvés avant de pouvoir être exportés du système. Vous pouvez également configurer la mise en page de l'écran d'approbation à l'aide du **Module de création de mise en page**. Pour des instructions détaillées sur l'utilisation du **Module de création de mise en page**, cliquez [ici](../../../../setup/document-types/layout-builder.md).
* **Approuver avant l'exportation V2** : Active l'Approbation V2, qui prend en charge l'utilisation de champs dynamiques à la place de champs statiques. Vous pouvez également personnaliser la mise en page de l'écran d'approbation à l'aide du **Module de création de mise en page**. Pour des instructions détaillées sur l'utilisation du **Module de création de mise en page**, cliquez [ici](../../../../setup/document-types/layout-builder.md).
* **Deuxième approbation** : Ajoute une couche d'approbation supplémentaire pour une validation améliorée et un meilleur contrôle sur le traitement des documents. Vous pouvez également personnaliser la mise en page de l'écran d'approbation à l'aide du **Module de création de mise en page**. Pour des instructions détaillées sur l'utilisation du **Module de création de mise en page**, cliquez [ici](../../../../setup/document-types/layout-builder.md).
* [**Cachet d'approbation**](approval/approval-stamp.md) : Ajoute un cachet au document lorsqu'il est approuvé.
* [**Historique de l'approbation**](approval/approval-history.md) : Permet l'affichage de l'historique des approbations à la fois dans l'écran d'approbation et la validation des champs.

## Bon de commande

* [**Table PO dans le générateur de mise en page**](purchase-order/po-table-in-layout-builder.md) : Permet l'inclusion de tables de bon de commande dans le générateur de mise en page pour des mises en page de documents personnalisées.
* [**Vérification automatique des mises à jour de l'OP**](purchase-order/auto-check-for-po-updates.md) : Lorsqu'elle est activée, le système affiche un indicateur visuel dans l'écran de correspondance des bons de commande pour montrer quand un bon de commande a été mis à jour, incitant les utilisateurs à actualiser pour obtenir les dernières informations.
* **Mise à jour automatique des données de la commande** : L'activation de cette option mettra automatiquement à jour les données de la commande lorsque de nouvelles données sont disponibles.
* [**Statut de la ligne de commande consommée**](purchase-order/consumed-po-line-status.md) : Ce paramètre améliore l'écran de correspondance des Bon de Commande en appliquant un code couleur aux lignes de bon de commande.
* [**Calculer le prix unitaire de la commande**](purchase-order/calculate-po-unit-price.md) : Cela vous permet de calculer le prix unitaire de la commande en utilisant le montant net et la quantité, au lieu de l'extraire.
* [**Bon de commande**](purchase-order/purchase-order.md) : Bascule si le document doit être traité dans l'écran de correspondance des bons de commande. Vous pouvez également spécifier sur quel terme de quantité le processus de correspondance doit être basé.
* [**Exporter les lignes de bon de commande non assorties**](purchase-order/export-not-matched-po-lines.md) : Cette fonctionnalité contrôle l'exportation des lignes de bon de commande. Lorsqu'elle est désactivée, seules les lignes appariées sont exportées. Lorsqu'elle est activée, toutes les lignes de bon de commande sont exportées, même si elles ne sont pas appariées à une ligne de confirmation de commande.
* [**Paramètre de tolérance PO**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) : Cette fonctionnalité vous permet de définir des niveaux de tolérance pour la quantité et le prix unitaire, en tenant compte des petites divergences sans les signaler comme des incohérences.
* [**Paramètre de tolérance PO supplémentaire**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md#parametre-pour-configurer-les-parametres-de-tolerance-de-commande-dachat-supplementaires) : Cette fonctionnalité vous permet de définir des niveaux de tolérance supplémentaires pour le fret, les charges et les taxes, en tenant compte des petites divergences sans les signaler comme des incohérences.
* [**Exportation alternative**](purchase-order/alternate-export.md) : Cela vous permet de configurer une exportation alternative pour des statuts spécifiques.
* [**PO désactiver statuts**](purchase-order/purchase-order-disable-statuses.md) : Vous permet de désactiver des statuts spécifiques pour qu'ils ne soient pas pris en compte dans le processus de correspondance.
* **Ignorer les lignes déjà appariées** : L'activation de cette option ignorera les lignes qui ont déjà été appariées lors d'un nouveau processus de correspondance.
* [**Mettre à jour le statut du bon de commande du document**](purchase-order/update-document-purchase-order-status.md): Lorsqu'activé, la colonne État de la commande sur le tableau de bord est automatiquement mise à jour chaque fois que le statut de la commande d'achat change.
* [**Carte des numéros d'articles des fournisseurs**](purchase-order/supplier-item-number-map-admin-documentation.md) : Un paramètre utilitaire qui associe les numéros d'articles des fournisseurs aux numéros d'articles internes, garantissant l'exactitude dans la gestion des stocks et des bons de commande.
