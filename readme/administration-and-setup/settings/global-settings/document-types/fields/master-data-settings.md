# Paramètres des données de référence

## Tutoriel vidéo : données de base et listes de valeurs

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/master-data-lists-admin/v1/fr.mp4" %}
Sources de données de base, listes de valeurs et paramètres des données de base dans DocBits
{% endembed %}

La vidéo présente les sources de données de base, les listes de valeurs et les paramètres des données de base d'un type de document.

Les **Paramètres des données de référence** relient les champs de validation d'un document aux données stockées sous [Recherche de données de référence](../../../document-processing/master-data-lookup.md). Utilisez **Consultation des données de base** pour trouver un enregistrement correspondant et le reprendre. Utilisez **Données de base LOV** pour proposer une liste de valeurs issue d'un jeu de données.

Les images des formulaires montrent leurs valeurs initiales avant toute saisie. Les valeurs des associations existantes sont masquées dans l'image du tableau.

## Ouvrir les paramètres

1. Dans **Paramètres**, ouvrez **Traitement des documents → Types de documents**.
2. Ouvrez le type de document que vous souhaitez configurer, par exemple **Facture**, puis sélectionnez **Champs**.
3. Sélectionnez **Paramètres des données maîtres**. La page contient les deux sections **Consultation des données de base** et **Données de base LOV**. Sélectionnez le titre d'une section pour la déplier.

<figure><img src="../../../../../.gitbook/assets/dbdc-35-overview-fr-20261101.png" alt="Sections Consultation des données de base et Données de base LOV repliées dans les paramètres des données maîtres de Facture"><figcaption><p>Sélectionnez le titre d'une section pour déplier les paramètres de recherche ou de listes de valeurs.</p></figcaption></figure>

## Associer un enregistrement avec la consultation des données de base

Les configurations de la section **Consultation des données de base** parcourent un jeu de données et associent un enregistrement correspondant aux champs du document. La liste affiche le nom de chaque configuration et indique si elle est active. Un badge **Par défaut** identifie une configuration fournie par DocBits ; vous pouvez la désactiver, mais pas la modifier ni la supprimer.

### Créer une configuration de recherche

1. Sélectionnez **Créer une configuration de recherche**.
2. Saisissez un **Nom de recherche** et choisissez le **Nom du jeu de données de recherche** qui contient les enregistrements à parcourir.
3. Choisissez un **Gestionnaire de conflits** pour le cas où plusieurs enregistrements correspondent :
   * **Best Score** choisit la correspondance la plus forte.
   * **Return None** laisse le résultat vide, à une personne de décider.
   * **Return First** utilise le premier résultat.
4. Choisissez **HEADER** pour les champs du document ou **LINE** pour les champs d'un tableau du document. Pour **LINE**, choisissez également le **Détail du contexte**, c'est-à-dire le tableau auquel la recherche s'applique.
5. Activez **Tout faire correspondre** si chaque champ de recherche configuré doit correspondre à un enregistrement. Laissez-le désactivé si un seul champ correspondant suffit. Sélectionnez **Créer**.

<figure><img src="../../../../../.gitbook/assets/dbdc-35-lookup-config-fr-20261101.png" alt="Formulaire vide Créer une configuration de données de base avec type de document, nom de recherche, jeu de données, gestionnaire de conflits, type de contexte, Tout faire correspondre, Annuler et Créer"><figcaption><p>Le formulaire affiche initialement INVOICE, Best Score et HEADER ; renseignez les champs pour la configuration souhaitée.</p></figcaption></figure>

**Tout faire correspondre** et le **Gestionnaire de conflits** agissent ensemble et décident si un fournisseur est reconnu automatiquement. Vous trouverez des exemples dans [Configuration des données floues avec les données maîtres](../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md).

### Mapper les champs d'une configuration

Dépliez une configuration pour voir les champs qui lui sont associés. Les colonnes indiquent le champ du jeu de données, le champ de validation du document, un champ parent facultatif et si l'association est recherchable ou déclenche la recherche automatiquement. Les associations de votre organisation peuvent différer.

<figure><img src="../../../../../.gitbook/assets/dbdc-35-mapped-fields-fr-20261101.png" alt="Tableau des associations déplié avec Champ De Recherche, Champ De Validation, Champ Parent, Recherche Possible, Déclenchement Automatique et Actions ; les valeurs existantes sont masquées"><figcaption><p>Examinez les colonnes avant d'ajouter un champ. Les valeurs existantes sont masquées dans cette image.</p></figcaption></figure>

Sélectionnez **Créer** dans la configuration dépliée pour ajouter une association :

* **Champ de recherche** est la colonne du jeu de données à parcourir.
* **Champ de validation** est le champ du document qui reçoit le résultat.
* **Champ parent** vérifie éventuellement le résultat par rapport à un champ associé.
* **Opérateur de recherche** détermine la manière dont le texte est comparé. **Smart** ignore les espaces et la ponctuation ; les autres choix incluent Contient, Commence par, Se termine par et Exact.
* **Déclenchement automatique** lance une recherche dès que ce champ est renseigné. **Recherche possible** laisse le champ participer aux recherches et permet une recherche manuelle pendant la validation.

Sélectionnez **Créer** pour ajouter l'association. Utilisez le menu à trois points **Actions** d'une ligne pour modifier ou supprimer une association modifiable. Les associations par défaut peuvent uniquement être consultées.

<figure><img src="../../../../../.gitbook/assets/dbdc-35-create-field-fr-20261101.png" alt="Formulaire vide Créer des champs de données maîtres avec Champ de recherche, Champ de validation, Champ parent, Opérateur de recherche, Déclenchement automatique, Recherche possible, Annuler et Créer"><figcaption><p>Choisissez la manière dont une colonne du jeu de données est associée à un champ du document.</p></figcaption></figure>

Utilisez le menu à trois points d'une configuration pour l'activer ou la désactiver, la dupliquer ou la modifier. Une configuration par défaut peut uniquement être consultée et ne peut pas être supprimée. Supprimer une configuration ou un champ personnalisé supprime son association ; vérifiez d'abord quels champs du document en dépendent.

## Proposer une liste avec les données de base LOV

**Données de base LOV** crée des listes déroulantes à partir d'un jeu de données de référence. Vous pouvez également ajouter des champs de filtre pour qu'une sélection précédente restreigne les choix affichés ensuite.

Dépliez **Données de base LOV**, puis sélectionnez **Créer une configuration de recherche Lov**. Si aucune configuration n'existe, la section n'affiche que ce bouton.

<figure><img src="../../../../../.gitbook/assets/dbdc-35-lov-overview-fr-20261101.png" alt="Section Données de base LOV dépliée avec le bouton Créer une configuration de recherche Lov"><figcaption><p>Ouvrez le formulaire de liste de valeurs avec Créer une configuration de recherche Lov.</p></figcaption></figure>

Dans le formulaire, saisissez **Consulter le nom de Lov**, choisissez **Nom de l'ensemble de données Lov** et réglez **Type de contexte** sur **HEADER** ou **LINE**. Pour **LINE**, sélectionnez **Détail du contexte** afin d'identifier le tableau du document. Choisissez ensuite :

* **Champ d'étiquette de consultation** : la valeur que les personnes voient dans la liste déroulante.
* **Champ de valeur de recherche** : la valeur stockée pour la sélection et utilisée pour le filtrage.
* **Hors champ** : le champ du document renseigné par l'étiquette sélectionnée.

Sélectionnez **Créer** pour enregistrer la configuration. Dépliez-la pour examiner ses champs, ou utilisez son menu à trois points pour l'activer, la dupliquer, la modifier ou la supprimer.

<figure><img src="../../../../../.gitbook/assets/dbdc-35-lov-config-fr-20261101.png" alt="Formulaire LOV vide Créer une configuration de données de base avec jeu de données, type de contexte, champ d'étiquette de consultation, champ de valeur de recherche, Hors champ, Annuler et Créer"><figcaption><p>Reliez la valeur d'un jeu de données et son étiquette visible à un champ du document.</p></figcaption></figure>

Pour créer des listes déroulantes dépendantes, sélectionnez **Créer** dans une configuration LOV dépliée et choisissez un **Champ de recherche** et un **Champ du filtre**. La valeur du champ de filtre restreint les choix renvoyés par la recherche. Vous pouvez également définir une **Valeur du filtre** fixe et marquer un champ comme **Requis**. Utilisez le menu à trois points de la ligne pour modifier ou supprimer un champ de filtre personnalisé.
