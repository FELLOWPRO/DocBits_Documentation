# Recherche plein texte

La recherche plein texte permet aux utilisateurs de rechercher dans le contenu réel des documents et dans chaque champ extrait, et non plus seulement dans les noms de fichiers et les ID.

<figure><img src="../../../../.gitbook/assets/fulltext-search-required-dialog.png" alt="Boîte de dialogue „Fulltext Module Required“ affichée lorsque le module est désactivé"><figcaption><p>La boîte de dialogue « Fulltext Module Required » apparaît sur les pages qui dépendent du module.</p></figcaption></figure>

## Sans le module

Lorsque la recherche plein texte n'est pas activée, la barre de recherche du tableau de bord ne peut interroger qu'un petit ensemble de champs structurés. Le texte libre saisi est uniquement comparé à :

* `filename`
* `ID` du document
* `invoice_id`
* `purchase_order`

Tout ce qui sort de ces champs est ignoré. Aucune recherche sur le contenu, aucun support des plages, opérateurs ou filtres intelligents.

## Avec le module activé

L'activation de la recherche plein texte ouvre la recherche à tous les champs extraits d'un document et remplace la barre de recherche du tableau de bord par un langage de requête enrichi. Une requête peut combiner des filtres par champ, des comparaisons de plage, des opérateurs logiques, des dates relatives et des filtres intelligents.

<figure><img src="../../../../.gitbook/assets/fulltext-search-dashboard-query.png" alt="Barre de recherche du tableau de bord avec une requête de plage et la liste de documents filtrée"><figcaption><p>La barre de recherche du tableau de bord accepte le langage de requête étendu. Saisissez une requête puis appuyez sur <kbd>Entrée</kbd> pour filtrer la liste.</p></figcaption></figure>

### Requêtes ciblées sur un champ

Préfixez le nom du champ extrait suivi de deux points pour le cibler. Les noms de champs suivent la convention de l'API (minuscules, snake\_case) et s'appliquent à tout champ capturé par vos types de documents — fournisseur, métadonnées de facture, lignes, champs personnalisés.

```
supplier_name: Acme
invoice_id: INV-1234
status: ready_for_validation
```

### Requêtes par plage

Les opérateurs de comparaison fonctionnent sur les champs numériques et les dates. Les comparaisons ouvertes et les plages bornées sont prises en charge.

```
total_amount > 5000
total_amount <= 10000
invoice_due_date between 2026-01-01 and 2026-04-30
```

### Opérateurs logiques

Combinez les clauses avec `AND`, `OR` et `NOT`, et utilisez les parenthèses pour fixer la priorité. Les listes `IN` testent un champ contre un ensemble de valeurs possibles.

```
supplier_name: Acme AND total_amount > 1000
(status: ready_for_validation OR status: validated) AND invoice_date: this_month
NOT status: archived
status IN (ready_for_validation, exported)
```

### Dates relatives

Expressions temporelles évaluées au moment de la requête. Elles peuvent être utilisées partout où une date est attendue.

```
imported_on: today()
invoice_date: last_week
imported_on: this_quarter
```

### Filtres intelligents

Raccourcis à un seul jeton pour les requêtes courantes. Ils fonctionnent seuls ou comme partie d'une expression plus large.

```
overdue
@User
#INV-1234
$5k+
```

* `overdue` — documents dont la date d'échéance est dépassée.
* `@User` — filtre par personne assignée ; remplacez `User` par le nom de l'utilisateur.
* `#INV-1234` — recherche rapide par identifiant de document.
* `$5k+` — montants supérieurs à 5 000 dans la devise du document.

## Fonctionnalités dérivées

Deux modes de recherche spécialisés reposent sur le module de recherche plein texte. Les deux exigent que le module soit activé et ne peuvent pas être utilisés indépendamment.

### Recherche vectorielle

La recherche vectorielle trouve des documents sémantiquement proches de la requête, plutôt que des correspondances purement lexicales. Le tableau de bord traite toute requête commençant par `vector:` comme une recherche vectorielle, l'évalue contre les embeddings des documents et classe les résultats par similarité.

```
vector: frozen food invoices
```

L'indexation vectorielle se gère séparément de l'index de texte sur la page **Paramètres de recherche plein texte**. La désactiver arrête la génération d'embeddings pour les nouveaux documents, mais conserve l'index de texte.

### Recherche IA

La recherche IA accepte des requêtes en langage naturel et utilise un LLM pour en extraire des filtres structurés, qui sont ensuite exécutés contre l'index plein texte. Préfixez la requête par `ai:`.

```
ai: invoices from Ruiz over 1000 last quarter
```

La recherche IA et la recherche vectorielle ne sont pas interchangeables : la vectorielle trouve du contenu similaire, la recherche IA traduit le langage naturel en filtres. La recherche IA n'a pas d'interrupteur dédié — elle s'appuie sur les index plein texte et vectoriel existants.

<figure><img src="../../../../.gitbook/assets/fulltext-search-settings-page.png" alt="Page „Paramètres de recherche plein texte“ avec les sous-index Documents, Vector Index et Fulltext (Text)"><figcaption><p>Paramètres de recherche plein texte. L'index vectoriel possède son propre interrupteur ; l'index de texte fonctionne tant que le module est activé.</p></figcaption></figure>

## Prérequis

* L'infrastructure OpenSearch tourne en arrière-plan pour alimenter l'index.
* Lors de la première activation, tous les documents existants sont réindexés. La durée dépend du volume de documents de l'organisation.
* Seuls les administrateurs d'organisation peuvent activer ou désactiver les modules.

## Activation du module

1. Allez dans **Paramètres → Traitement de document → Module**.
2. Dans le groupe **Dashboards**, activez **Full text search**.
3. Confirmez la boîte de dialogue d'abonnement si elle s'affiche.
4. Attendez la fin de la première réindexation avant d'utiliser les requêtes plein texte.

<figure><img src="../../../../.gitbook/assets/fulltext-search-module-toggle.png" alt="Page „Modules“ avec l'interrupteur „Full text search“ sous le groupe Dashboards"><figcaption><p>L'interrupteur <strong>Full text search</strong> se trouve dans <strong>Module → Dashboards &#x26; Analytics</strong>.</p></figcaption></figure>

{% hint style="info" %}
La tarification du module de recherche plein texte est gérée par votre interlocuteur commercial DocBits. La confirmation d'abonnement apparaît lors de la première activation du module.
{% endhint %}

## Voir aussi

* [Paramètres de recherche plein texte](../../log-settings/fulltext-search-settings.md) — gestion de l'index et interrupteur de l'index vectoriel.
* [Fonctions Fulltext & Vector Search](../../global-settings/document-types/script/scripting-in-docbits/fulltext-search-functions.md) — API de scripting pour `fulltext_search()` et `vector_search()`.
* [Vue d'ensemble des modules](README.md) — liste complète des modules optionnels de DocBits.
