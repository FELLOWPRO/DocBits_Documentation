# Plan du Site

Le Plan du Site est l'index complet et consultable de tout ce que DocBits propose — chaque page, boîte de dialogue, entrée de barre latérale, action et fonctionnalité dans la page, regroupés par catégorie. C'est le complément long de la [Recherche Rapide Globale](global-quick-search.md).

## Comment y accéder

Ouvrez le Plan du Site depuis la barre latérale (entrée proche du bas) ou appuyez sur <kbd>Cmd</kbd>/<kbd>Ctrl</kbd> + <kbd>K</kbd> et choisissez **Voir tous les résultats**. L'URL directe est `/sitemap`.

<figure><img src="../../.gitbook/assets/sitemap-overview.png" alt="Aperçu du Plan du Site"><figcaption><p>Plan du Site avec aperçu des catégories et en-tête de recherche.</p></figcaption></figure>

## Parcourir le catalogue

Le Plan du Site est regroupé en catégories qui reflètent la structure de l'application — Paramètres, Traitement de document, Workflow, Validation, etc. Chaque catégorie liste d'abord ses pages puis ses fonctionnalités intra-page regroupées par sous-catégorie.

Les entrées sont colorées par type :

* **Page** — un itinéraire navigable complet.
* **Boîte de dialogue** — un modal ouvert depuis un autre endroit de l'application.
* **Barre latérale / Panneau / Menu** — une surface de navigation ou de contexte.
* **Action** — un bouton ou raccourci qui effectue une opération sans naviguer.

Cliquez sur n'importe quelle entrée pour y aller directement. Les entrées qui nécessitent un paramètre (un type ou un identifiant de document) incluent un sélecteur intégré — choisissez la valeur avant de cliquer.

## Recherche et filtres

L'en-tête fixe en haut de la page abrite la zone de recherche et les filtres en forme de pastilles. Tapez quelques caractères pour filtrer la liste en direct par nom et description. Utilisez les pastilles de type pour restreindre à un seul type d'entrée — par exemple uniquement **Boîte de dialogue**.

La recherche et le filtre courants sont ajoutés à l'URL, de sorte qu'une vue filtrée peut être ajoutée aux favoris ou partagée.

<mark>Le Plan du Site respecte les mêmes autorisations que le reste de DocBits. Les pages auxquelles vous n'avez pas accès n'apparaissent pas.</mark>

## Mode développeur

Un bouton **Utilisateur / Dev** dans l'en-tête active des informations supplémentaires destinées aux développeurs partenaires :

* L'itinéraire interne de chaque entrée.
* Les marqueurs de paramètres (`:docType`, `:docId`, clés de lien profond).

Le mode développeur est mémorisé dans votre navigateur. Repassez en mode Utilisateur pour la vue de lecture habituelle.

## Retour en haut

Le Plan du Site est long. Dès que vous dépassez le premier écran, un bouton Retour en haut apparaît en bas à droite.
