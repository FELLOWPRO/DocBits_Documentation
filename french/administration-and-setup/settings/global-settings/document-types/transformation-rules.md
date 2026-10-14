# Règles de Transformation

## Vue d'ensemble

Les règles de transformation nettoient ou réécrivent les données extraites **automatiquement** — un champ dans l’en-tête, une colonne dans un tableau, des lignes entières d’un tableau, ou un attribut du document — à chaque fois qu’un document est traité et à chaque fois qu’il est enregistré. Elles remplacent les petits scripts que de nombreuses organisations écrivaient pour « toujours tronquer ce champ », « par défaut cette colonne à 1 », « mapper les codes unités de ce fournisseur » ou « regrouper les lignes de cet fournisseur en une seule ligne totale ».

Une règle est définie par **type de document** et s’exécute sur chaque document de ce type. Les règles s’exécutent **avant** la validation, les scripts et la correspondance des bons de commande, de sorte que tout ce qui suit voit déjà les valeurs transformées.

## Comment y accéder

1. Naviguez vers **Paramètres → Paramètres globaux → Types de documents**.
2. Ouvrez le type de document et choisissez **Règles de transformation**. La liste affiche chaque règle du type avec sa portée, sa cible, sa priorité et si elle est active.
3. Cliquez sur **Nouvelle règle** pour ouvrir le générateur de règles, ou ouvrez une règle existante pour la modifier.

## Anatomie d’une règle

| Partie                      | Ce que c’est                                                                                                                                                                                                                                                                       |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nom / clé**               | Le nom affiché dans les listes, messages et l’historique des correspondances, et une clé technique qui reste stable lorsque vous renommez la règle.                                                                                                                                |
| **Portée**                  | Où la règle écrit : un **champ d’en-tête**, une **colonne de tableau**, un **tableau** (lignes entières) ou un **attribut du document**. Voir ci-dessous.                                                                                                                          |
| **Cible**                   | Le champ, la colonne (avec son tableau) ou le tableau sur lequel la règle écrit.                                                                                                                                                                                                   |
| **Source**                  | Optionnel. D’où la règle lit son entrée au lieu de la cible elle-même : `header.<field>` pour un champ d’en-tête, `doc.<attribute>` pour un attribut du document, `row.<column>` pour une autre colonne de la même ligne (portée colonne uniquement).                              |
| **Quand**                   | **Toujours**, ou **seulement lorsque** une condition est vraie (voir Conditions).                                                                                                                                                                                                  |
| **Actions**                 | La liste des transformations, appliquées dans l’ordre ; la sortie d’une action est l’entrée de la suivante.                                                                                                                                                                        |
| **Priorité**                | Les règles de même portée s’exécutent par priorité croissante (puis par clé). Utilisez-la lorsqu’une règle doit voir le résultat d’une autre.                                                                                                                                      |
| **Exécuter une fois**       | La règle s’applique à un document **au plus une fois**. Nécessaire pour les actions qui changeraient la valeur à chaque enregistrement (sous-chaîne, remplacement regex, extraction regex) et pour les règles de tableau qui ne doivent pas reconstruire les lignes à chaque fois. |
| **Journaliser l’exécution** | Écrit une ligne de journal par application — utile lors de l’ajustement d’une nouvelle règle.                                                                                                                                                                                      |

### Portées

| Portée                   | Écrit sur                                                            | Règle typique                                                                                 |
| ------------------------ | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Champ d’en-tête**      | un champ d’en-tête extrait (numéro de facture, devise, …)            | tronquer et mettre en majuscules le numéro de facture ; mapper « EUR€ » en « EUR »            |
| **Colonne de tableau**   | une colonne dans chaque ligne d’un tableau                           | par défaut `UNIT_PRICE_PER` à 1 ; supprimer le préfixe « Art.-Nr. » du numéro d’article       |
| **Tableau**              | les lignes d’un tableau                                              | vider les lignes et ajouter une ligne totale pour un fournisseur qui est apparié sur le total |
| **Attribut du document** | un attribut du document lui-même (actuellement la sous-organisation) | diriger les documents d’un fournisseur vers une sous-organisation                             |

Les règles s’exécutent portée par portée dans cet ordre : en-tête → document → tableau → colonne. Une règle de colonne voit donc déjà les lignes qu’une règle de tableau a ajoutées.

### Conditions (« seulement lorsque »)

Une condition compare une valeur du document avec une constante. La valeur provient d’un champ d’en-tête (`header.<field>`), d’un attribut du document (`doc.<attribute>`) ou, pour les règles de colonne, d’une colonne de la ligne courante (`row.<column>`).

| Opérateur                                   | Signification            |
| ------------------------------------------- | ------------------------ |
| est / n’est pas                             | comparaison exacte       |
| est l’un de / n’est pas l’un de             | valeur dans une liste    |
| contient, commence par, finit par           | comparaison de texte     |
| est vide / n’est pas vide                   | aucune valeur nécessaire |
| supérieur à, inférieur à, au moins, au plus | comparaison numérique    |
| correspond                                  | expression régulière     |

Les conditions peuvent être regroupées avec **toutes** (et) et **n’importe laquelle** (ou) et niées avec **pas**. Exemple : _seulement lorsque `header.supplier_id` est `20723`_ — la règle s’exécute pour un seul fournisseur.

### Actions

Actions pour les champs d’en-tête et les colonnes de tableau (elles forment un pipeline ; la valeur entre en haut et sort en bas) :

| Action          | Effet                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `trim`          | supprimer les espaces (ou caractères donnés) à gauche, à droite ou des deux côtés                                                        |
| `case`          | majuscule, minuscule, titre ou capitaliser                                                                                               |
| `pad`           | compléter jusqu’à une longueur avec un caractère, à gauche ou à droite                                                                   |
| `truncate`      | couper à une longueur maximale                                                                                                           |
| `affix`         | ajouter un préfixe ou suffixe, ou en supprimer un                                                                                        |
| `sanitize`      | ne garder qu’une classe de caractères (alphanumérique, alpha, numérique, alphanumérique + espace) ou supprimer un ensemble de caractères |
| `substring`     | prendre une partie de la valeur par début et longueur ou fin                                                                             |
| `regex_replace` | remplacer ce qu’une expression régulière correspond                                                                                      |
| `regex_extract` | garder ce qu’une expression régulière capture                                                                                            |
| `value_map`     | mapper des valeurs vers d’autres valeurs (optionnellement insensible à la casse, avec une valeur par défaut)                             |
| `date_format`   | reformater une date (l’entrée doit être la date ISO que DocBits stocke dans `value`)                                                     |
| `number_format` | reformater un nombre                                                                                                                     |
| `default`       | définir une valeur uniquement lorsque le champ est vide                                                                                  |
| `set_value`     | définir une valeur fixe, quel que soit le contenu du champ                                                                               |
| `clear`         | vider le champ                                                                                                                           |

Actions pour la portée **tableau** (elles agissent sur les lignes, pas sur les valeurs, et ne peuvent pas être mélangées avec les actions ci-dessus) :

| Action       | Effet                                                                                                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `clear_rows` | supprimer toutes les lignes du tableau                                                                                                                                         |
| `add_row`    | ajouter une ligne à la fin ou au début ; chaque colonne reçoit soit une valeur fixe soit une valeur lue depuis l’en-tête (`header.<field>`) ou le document (`doc.<attribute>`) |

{% hint style="info" %}
`substring`, `regex_replace` et `regex_extract` modifient une valeur à nouveau lorsqu’elles s’exécutent sur une valeur déjà transformée. Combinez-les avec **Exécuter une fois**, ou écrivez l’expression régulière de façon qu’une deuxième exécution n’ait plus rien à changer.
{% endhint %}

## Quand les règles s’exécutent

* Pendant le traitement, après l’extraction et avant la validation, les scripts et la correspondance des bons de commande.
* À **chaque enregistrement** du document dans lequel les données extraites ont changé. Les règles sans **Exécuter une fois** sont appliquées à nouveau à chaque enregistrement ; parce que chaque action sauf les trois ci-dessus est idempotente, une valeur déjà sous la forme cible reste telle quelle.

## Règles de transformation et correspondance des bons de commande

Les règles de tableau et de colonne modifient ce que le moteur de correspondance des BC voit :

* Une règle de tableau qui **reconstruit** les lignes (par exemple vider toutes les lignes et ajouter une ligne totale) conserve une correspondance de bon de commande existante tant qu’elle produit **les mêmes lignes à nouveau** — les valeurs sont comparées par leur sens, donc `1.0` et `1.00` sont la même ligne. Les lignes gardent leur identité et la correspondance survit à chaque enregistrement.
* Si une règle **remplace ou supprime des lignes qui étaient appariées**, la correspondance ne peut pas être conservée. Le document enregistre alors quelle règle l’a supprimée, l’écran de correspondance des bons de commande affiche cela comme raison (« _La correspondance du BC n’a pas pu être enregistrée : la règle de transformation "…" a reconstruit le tableau_ ») et les administrateurs reçoivent un lien vers la règle. L’**historique des correspondances** du document affiche une étape _Règles de transformation_ avant la première étape de correspondance avec les règles qui ont été exécutées.
* Le nombre de lignes après les règles est ce que comptent les [conditions d’activation](https://github.com/Fellow-Consulting-AG/docbits/tree/fr/readme/administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md#activation-conditions) des règles de correspondance. Une règle qui condense une facture en **une** ligne n’a de sens qu’avec une règle de correspondance sur total active pour les documents à une ligne (`[[count(table_lines)]] >= 1`).

## Exemples

**Nettoyer le numéro de facture** — champ d’en-tête `invoice_id`, toujours : `trim` → `case` majuscule.

**Définir par défaut la base de prix** — colonne de tableau `UNIT_PRICE_PER` du tableau des lignes, toujours : `default` `1`.

**Mapper les codes unités d’un fournisseur** — colonne de tableau `UNIT` du tableau des lignes, seulement lorsque `header.supplier_id` est `10040` : `value_map` `{ "STK": "PCE", "KG": "KGM" }`.

**Une ligne totale pour un fournisseur apparié sur le total** — portée tableau sur le tableau des lignes, seulement lorsque `header.supplier_id` est `20723` : `clear_rows`, puis `add_row` avec `POSITION` = `001`, `UNIT_PRICE` = `1.0`, `QUANTITY` = `header.total_net_amount`, `NET_AMOUNT` = `header.total_net_amount`. À associer avec une règle de correspondance sur total dont la condition d’activation accepte un document à une ligne.

**Diriger un fournisseur vers une sous-organisation** — attribut du document `sub_org_id`, seulement lorsque `header.supplier_id` est l’un de `[…]` : `set_value` `<id de la sous-organisation>`.

## Dépannage

| Symptôme                                                                | À vérifier                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| La règle n’a rien changé                                                | Est-elle active ? Le type de document correspond-il ? La condition est-elle vraie pour ce document (comparez la valeur exacte, espaces inclus) ? Une règle avec **Exécuter une fois** a-t-elle déjà été appliquée au document ? |
| La valeur change à nouveau à chaque enregistrement                      | Le pipeline contient `substring`, `regex_replace` ou `regex_extract`. Activez **Exécuter une fois** ou rendez l’expression idempotente.                                                                                         |
| La correspondance du bon de commande est perdue après enregistrement    | Une règle de tableau a remplacé les lignes appariées. La raison sur le document nomme la règle ; faites en sorte que la règle reproduise les mêmes lignes, ou activez **Exécuter une fois**.                                    |
| Une règle de correspondance ne s’exécute jamais après la transformation | La règle a changé le nombre de lignes ; ajustez la condition d’activation de la règle de correspondance.                                                                                                                        |
