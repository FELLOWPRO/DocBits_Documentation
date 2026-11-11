# Paramètres de la Recherche Plein Texte

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Paramètres de la Recherche Plein Texte dans le bac à sable, avec une boîte de dialogue expliquant que le module est requis et les boutons Go to Modules et Enable Now"><figcaption><p>Lorsque la Recherche Plein Texte est désactivée, cette boîte de dialogue explique la marche à suivre.</p></figcaption></figure>

Les Paramètres de la Recherche Plein Texte déterminent ce que DocBits indexe et la manière dont ce contenu devient consultable dans les documents, les données de référence ERP et les modèles. La page de paramètres affiche une boîte de dialogue d'exigence tant que le **Fulltext Search module** n'est pas activé — consultez [Recherche plein texte](../document-processing/module/fulltext-search.md) pour le langage de requête destiné aux utilisateurs.

## Prérequis

Le module Recherche Plein Texte doit être activé dans **Settings → Module → Dashboards & Analytics → Full text search**. Si le module n'est pas activé, la boîte de dialogue propose trois actions :

* **Help (?)** — Ouvrir la documentation de la Recherche Plein Texte dans un nouvel onglet avant de modifier un paramètre.
* **Go to Modules** — Ouvrir les paramètres du module Dashboards & Analytics pour vérifier la configuration.
* **Enable Now** — Ouvrir la boîte de dialogue d'abonnement. Vérifiez et confirmez cette boîte de dialogue avant l'activation du module ; un clic sur ce seul bouton ne l'active pas.

La page de paramètres elle-même devient disponible une fois le module actif.

## Disposition de la page

La page de paramètres est organisée en trois onglets : **Documents**, **ERP** et **Templates**. Chaque onglet couvre un type de contenu différent que la Recherche Plein Texte peut indexer.

### Onglet Documents

L'onglet Documents couvre tout ce qui concerne l'indexation des documents traités :

* **Indexing statistics** — totaux des documents indexés et en attente, actualisés à la demande.
* **Vector preferences** — trois interrupteurs au niveau de l'organisation qui déterminent si l'indexation vectorielle s'exécute parallèlement à l'index texte pour les documents. L'indexation vectorielle alimente le mode de requête `vector:` et la fonction « Find Similar ».
* **Reindex actions** — lancer une réindexation complète ou incrémentale. Pendant le déroulement d'une réindexation, vous voyez la progression en direct (documents par minute, temps restant estimé), l'état actuel du flux et la dernière défaillance (le cas échéant).
* **Sync diagnostics** — diagnostics à la demande pour les cas où l'index semble désynchronisé du magasin de documents sous-jacent.

<mark>La réindexation n'est pas destructive — la recherche existante continue de fonctionner pendant la reconstruction du nouvel index.</mark>

### Onglet ERP

L'onglet ERP contrôle l'indexation des données de référence ERP — fournisseurs, clients, articles et entités similaires. Chaque entité dispose de son propre interrupteur :

* **Indexing** — indexer l'entité dans l'index texte afin qu'elle soit consultable depuis le tableau de bord.
* **Vector** — indexer l'entité dans l'index vectoriel afin qu'elle puisse être mise en correspondance par des requêtes sémantiques.

Utilisez l'action **Toggle all** en haut de la liste pour appliquer le même état activé ou désactivé à toutes les entités en une seule fois. L'indexation démarre en arrière-plan ; un indicateur sur chaque ligne montre qu'elle est en cours.

### Onglet Templates

L'onglet Templates liste les versions de modèles connues de l'index plein texte. Utilisez cette vue pour confirmer, après un redéploiement, que les versions de modèles dont vous dépendez sont présentes dans l'index.

## Ce qui est indexé

Une fois activée et configurée, la Recherche Plein Texte permet aux utilisateurs de :

* Rechercher dans tout le contenu des documents (et pas seulement dans les champs de métadonnées).
* Trouver des documents par le texte contenu dans les fichiers téléversés.
* Utiliser des opérateurs de recherche avancés pour des requêtes précises.
* Accéder aux résultats de recherche directement depuis le tableau de bord.
* Utiliser la recherche sémantique (préfixe `vector:`) lorsque l'indexation vectorielle est active pour ce type de contenu.

Consultez la page du module [Recherche plein texte](../document-processing/module/fulltext-search.md) pour la référence complète du langage de requête, y compris les requêtes par plage, les filtres intelligents et le mode de recherche IA.
