# Cartes de comparaison de devis

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-4a7af1d99c73-fr.png" alt="Cartes disponibles dans la catégorie sélectionnée. Renseignez les champs avant utilisation. Certains libellés de cette version de la carte ont encore une traduction incomplète ou incorrecte dans l’interface. Les explications de cette page emploient les termes corrects."><figcaption><p>Cartes disponibles dans la catégorie sélectionnée. Renseignez les champs avant utilisation. Certains libellés de cette version de la carte ont encore une traduction incomplète ou incorrecte dans l’interface. Les explications de cette page emploient les termes corrects.</p></figcaption></figure>

Ces conditions Et utilisent les données du devis ou de l'article fournisseur disponibles sur le document. Configurez-les et testez-les après le chargement des données de devis requises. Un identifiant d'article correspondant ne prouve pas en soi que son prix ou son unité de mesure est correct.

## Sélectionnez le chèque

| Type de carte | Vérification et configuration |
| --- | --- |
| `CONDITION_QUOTES_ITEM_NUMBER_COMPARISON` | Vérifie l'identifiant de l'article par rapport aux données de prix de l'article. Sélectionnez les champs Comparaison et Tout/Tout proposés par la carte. |
| `CONDITION_SPECIFY_SUPPLIER_TYPE` | Compare le type de fournisseur à partir des données du devis avec `supplier_type`. Il s'agit d'une vérification de classification des fournisseurs et non d'une comparaison de prix. |
| `CONDITION_QUOTE_SUPPLIER_ITEM_NUMBER_EXISTS` | Vérifie si l'ID d'article du fournisseur est présent ou non dans les données de prix de l'article ; choisissez l'opérateur et Any/All. Les données manquantes sur les devis ou les articles doivent être examinées dans le journal. |
| `CONDITION_QUOTE_PRICE_MATCH` | Compare un prix unitaire avec le prix fournisseur sélectionné : `ManagedPrice` ou `LastPrice`. Choisissez Any/All et l’opérateur de comparaison numérique. Les lignes sans numéro comparable de chaque côté sont ignorées et enregistrées ; si aucune ligne n'est comparable, la carte signale des données de document manquantes. |
| `CONDIITON_UNIT_OF_MEASURE_EQUAL` | Vérifie l'unité de mesure par rapport aux données associées. Le type technique contient une faute d'orthographe retenue ; ne le modifiez pas dans le workflow stocké JSON. Un prix exprimé par différentes unités nécessite une attention particulière. |
| `CONDITION_ITEM_QUOTES_TO_CONTRACTED_PRICE` | Compare les prix proposés et contractuels. La version 3 ajoute Any/All ; voir ci-dessous. |

Les étiquettes visibles peuvent différer selon la version et la langue de l'interface utilisateur. Sélectionnez par la vérification réelle, pas seulement par le nom de la catégorie. Par exemple, le prix de l'article indiqué peut apparaître sous Logique tandis que les autres vérifications du devis apparaissent dans Comparer avec le prix du devis.

## Prix de l'article proposé : version 3

Choisissez l'opérateur d'égalité ou d'inégalité et si une ligne comparée ou chaque ligne comparée doit le satisfaire :

- `match_any` : une ligne comparable réussie suffit.
- `match_all` : chaque ligne comparée doit satisfaire l'opérateur sélectionné.

La version 2 conserve le comportement Tous. Un paramètre Any/All non défini sur la version 3 revient à All et est enregistré. Une carte sans lignes comparables signale des données manquantes ; l’absence de prix n’est pas une preuve d’égalité ou d’inégalité. Inspectez les lignes sautées et leur côté manquant dans le journal.

Par exemple, deux lignes comparables produisent des résultats vrai et faux pour l'égalité. Tous les laissez-passer ; Tout échoue. En cas d'inégalité, le résultat de la comparaison pour chaque ligne change en premier, et Any/All combine ensuite ces résultats. Il n’inverse pas le résultat final All pour implémenter Any.

## Cas de tests

Utilisez les identifiants exacts des articles et des fournisseurs, la source de prix prévue et les unités correspondantes. Testez la correspondance de toutes les lignes, un résultat mitigé, des prix non comparables, des données de devis manquantes et un identifiant de fournisseur erroné. Vérifiez à la fois le résultat de la comparaison et quelles lignes ont été ignorées. Conservez l’approbation ou l’exportation derrière les contrôles commerciaux réellement requis ; une vérification d’identifiant réussie ne constitue pas une validation complète de l’approvisionnement.

Voir [PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md) pour les comparaisons de bons de commande et [Workflow Logs](../workflow-logs.md) pour le dépannage.
