# And : choisir une carte de condition

Utilisez une carte **And** (« Et ») pour décider si un workflow doit se poursuivre après son déclencheur **When** (« Quand »). Ajoutez les contrôles nécessaires avant l'action **Then** (« Alors »). Chaque carte affiche des champs à remplir, comme **Opérateur**, **Nom du champ** ou **Valeur** ; les captures d'écran montrent les modèles de cartes disponibles, et non des règles complétées.

Dans le **Constructeur De Flux De Travail**, sélectionnez **Ajouter une carte** sous **Et....**. Choisissez une catégorie à gauche, ou saisissez le nom d'une carte dans **Carte de recherche**. Sélectionnez l'aperçu d'une carte pour l'ajouter au workflow. Vous pouvez faire défiler la liste des aperçus pour voir davantage de cartes. Utilisez **×** pour fermer le sélecteur sans choisir une autre carte. Après avoir configuré les cartes, enregistrez le workflow avec **Enregistrer le flux de travail**. Voir [Workflow](../README.md) pour les étapes environnantes **Quand**, **Et** et **Alors**.

## Comparaison des bons de commande

Utilisez ces cartes pour comparer les données d'une commande ou d'une facture avec un bon de commande, comme le prix unitaire, la date de livraison promise, les frais ou la quantité. Choisissez les champs, l'opérateur et toute tolérance demandés par la carte sélectionnée. Voir [Comparaison des bons de commande](compare-with-purchase-order/README.md) pour les différentes cartes.

<figure><img src="../../../.gitbook/assets/and-category-po-comparison-fr-20261008.png" alt="Sélecteur de cartes And en français avec la catégorie Comparaison des bons de commande ouverte ; les aperçus visibles comparent le prix unitaire, la date de livraison, les frais et la quantité."><figcaption><p>La catégorie Comparaison des bons de commande dans la Sandbox en français.</p></figcaption></figure>

## Champ du document

Choisissez cette catégorie pour vérifier une case à cocher ou le statut d'un champ, comparer un champ avec une valeur ou comparer deux champs. Remplissez les espaces réservés **Nom du champ** et **Opérateur** sur la carte choisie. Certaines comparaisons demandent aussi une tolérance. Voir [Champ du document](document-field/README.md).

<figure><img src="../../../.gitbook/assets/and-category-document-field-fr-20261008.png" alt="Sélecteur de cartes And en français avec la catégorie Champ du document ouverte ; les aperçus visibles vérifient une case à cocher, le statut d'un champ, les valeurs de champs et la comparaison de deux champs."><figcaption><p>Les contrôles Champ du document utilisent les valeurs du document en cours.</p></figcaption></figure>

## Date & Heure

Utilisez **Date & Heure** pour comparer une date ou une heure avec une plage, ou pour comparer **Aujourd'hui** avec une date choisie. Sélectionnez l'**Opérateur** et les valeurs de date dans la carte. Voir [Date & Heure](date-and-time/README.md).

<figure><img src="../../../.gitbook/assets/and-category-date-time-fr-20261008.png" alt="Sélecteur de cartes And en français avec la catégorie Date &amp; Heure ouverte ; deux aperçus comparent une date ou une heure avec une plage et comparent Aujourd'hui avec une date."><figcaption><p>Date & Heure propose un contrôle de plage et un contrôle par rapport à aujourd'hui.</p></figcaption></figure>

## Document

Utilisez ces cartes lorsqu'un workflow doit dépendre du **type de document** ou de la **sous-organisation**. Choisissez le type ou l'organisation nommé dans la carte. Voir [Document](document/README.md).

<figure><img src="../../../.gitbook/assets/and-category-document-fr-20261008.png" alt="Sélecteur de cartes And en français avec la catégorie Document ouverte ; les aperçus vérifient le type de document et l'appartenance à une sous-organisation."><figcaption><p>Les conditions Document vérifient le type ou la sous-organisation.</p></figcaption></figure>

## Logique

Cette catégorie regroupe des contrôles utilisant une table de décision, une réponse HTTPS, la disponibilité d'un module, un prix d'article cité, une valeur de chance ou deux valeurs. Ouvrez la carte concernée et remplissez ses espaces réservés nommés ; par exemple, la carte HTTPS demande une URL, une méthode et un code de statut accepté. Voir [Logique](logic/README.md).

<figure><img src="../../../.gitbook/assets/and-category-logic-fr-20261008.png" alt="Sélecteur de cartes And en français avec la catégorie Logique ouverte ; les aperçus incluent une table de décision, une requête HTTPS, un module actif, un prix cité, une chance et une comparaison de valeurs."><figcaption><p>Logique propose plusieurs types de conditions différents ; choisissez celle qui correspond à votre règle.</p></figcaption></figure>

## Statut

Utilisez **Statut** pour vérifier si un document possède un statut choisi ou si son statut fait partie d'un ensemble sélectionné. Choisissez l'**Opérateur** et le **Statut** dans la carte. Voir [Statut](status/README.md).

<figure><img src="../../../.gitbook/assets/and-category-status-fr-20261008.png" alt="Sélecteur de cartes And en français avec la catégorie Statut ouverte ; deux aperçus comparent le statut du document avec un statut ou un ensemble de statuts."><figcaption><p>Les conditions Statut vérifient l'état actuel du document.</p></figcaption></figure>

## Tableau

Ces cartes examinent les lignes de tableau d'un document. Les options visibles incluent des vérifications de date, des motifs de texte, la durée de conservation et des comparaisons entre colonnes. Sélectionnez le **Nom de la table** et le **Nom de la colonne** avant de choisir un opérateur ou un motif. Voir [Tableau](table/README.md).

<figure><img src="../../../.gitbook/assets/and-category-table-fr-20261008.png" alt="Sélecteur de cartes And en français avec la catégorie Tableau ouverte ; les aperçus visibles incluent la date, un motif d'expression rationnelle, la durée de conservation et des comparaisons de colonnes de tableau."><figcaption><p>Les conditions Tableau utilisent les lignes et les colonnes d'un tableau de document.</p></figcaption></figure>

## Comparer avec le prix du devis

Utilisez ces cartes pour comparer un article avec les données d'un prix cité. Les choix visibles couvrent l'ID d'article, le type de fournisseur, l'ID d'article du fournisseur, le prix unitaire et l'unité de mesure. L'**Opérateur** et les espaces réservés de données dépendent de la carte que vous sélectionnez.

<figure><img src="../../../.gitbook/assets/and-category-quote-price-fr-20261008.png" alt="Sélecteur de cartes And en français avec la catégorie Comparer avec le prix du devis ouverte ; cinq aperçus couvrent l'ID d'article, le type de fournisseur, l'ID d'article du fournisseur, le prix unitaire et l'unité de mesure."><figcaption><p>Comparer avec le prix du devis est une catégorie distincte dans le sélecteur de cartes actuel.</p></figcaption></figure>

## Attribué à

Utilisez **Attribué à** lorsque la condition dépend de l'utilisateur ou du groupe attribué. Choisissez de comparer avec un seul utilisateur ou groupe, ou avec un ensemble sélectionné. Voir [Attribué à](assignee/README.md).

<figure><img src="../../../.gitbook/assets/and-category-assignee-fr-20261008.png" alt="Sélecteur de cartes And en français avec la catégorie Attribué à ouverte ; les aperçus comparent l'utilisateur ou le groupe attribué avec un ou plusieurs choix."><figcaption><p>Les conditions Attribué à vérifient l'utilisateur ou le groupe attribué au document.</p></figcaption></figure>
