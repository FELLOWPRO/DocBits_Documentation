# Règles de transformation : aperçu pratique complet

> Limite connue de l’aperçu (vérifiée le 29 octobre 2026, version 11.15.2) : lors de l’ajout du préfixe `INV-`, l’aperçu transforme à tort `INV-4711` en `INV-INV-4711`. Le test indépendant du serveur conserve `INV-4711`. Vérifiez aussi les exécutions répétées par un test serveur ; un aperçu correct ne prouve pas à lui seul l’exécution complète lors de l’enregistrement.

Date de vérification : 28 octobre 2026. Les exemples ont été vérifiés avec des valeurs de formation synthétiques sur Dev NOVA. Un aperçu ne constitue pas une preuve de modification de document enregistrée, de rapprochement de commande ou d'export ERP.


## Libellés visibles dans l’éditeur

Certains libellés de l’interface actuelle sont traduits de manière imprécise. Le tableau reprend le texte réellement affiché pour retrouver la bonne étape ; les explications fonctionnelles utilisent les termes techniques. Les captures montrent l’interface sans modification.

| Opération | Libellé affiché |
| --- | --- |
| case | Changer la casse |
| trim | Supprimer les espaces |
| pad | Tampon |
| truncate | Tronquer |
| affix | Affixe |
| sanitize | Nettoyer |
| substring | Prenez une tranche |
| regex_extract | Extrait |
| regex_replace | Rechercher et remplacer |
| value_map | Valeurs de la carte |
| date_format | Date de reformatage |
| number_format | numéro de format |
| fix_value | valeur fixe |
| clear | Supprimer |
| clear_rows | Effacer toutes les lignes |
| add_row | Ajouter une ligne |


## Quatre domaines d'application

| Domaine | Entrée et cible | Tâche typique |
| --- | --- | --- |
| Champ d'en-tête | Un champ par document ; la source peut être un autre champ d'en-tête | Nettoyer le numéro de facture, reprendre le numéro de commande |
| Colonne de tableau | La colonne choisie pour chaque ligne du tableau sélectionné | Uniformiser les numéros d'article ou les codes d'unité |
| Lignes de tableau | Tableau entier | Supprimer des lignes ou ajouter des positions définies |
| Routage | Attribut de document `sub_org_id` | Attribuer une sous-organisation existante |

Les domaines s'exécutent dans l'ordre **Champ d'en-tête → Routage → Lignes de tableau → Colonne de tableau**. Au sein d'un domaine, la priorité et la clé de règle déterminent l'ordre. Les étapes d'une règle s'exécutent de haut en bas. Une règle ultérieure peut donc lire des valeurs déjà modifiées. L'ordre des domaines n'est pas inversé par la priorité d'une seule règle.

## Toutes les étapes de l'éditeur

L'éditeur vérifié propose 14 étapes de valeur pour l'en-tête/la colonne, deux étapes pour les tableaux entiers et une attribution fixe dans le routage. `fix_value` et l'attribution de routage fixe utilisent côté serveur toutes deux `set_value`. De plus, l'interface connaît `default` ; cette étape n'est pas proposée dans le menu d'étapes normales vérifié.

| Étape | Variantes et paramètres | Exemple | Limite et contre-épreuve |
| --- | --- | --- | --- |
| Modifier la casse (`case`) | upper, lower, title, capitalize | `inv-4711` → `INV-4711` | Title : `acme gmbh` → `Acme Gmbh` ; capitalize : `aCME GMBH` → `Acme gmbh`. Les noms propres/abréviations peuvent changer de manière indésirable sur le plan métier. Pour `capitalize`, l'aperçu navigateur vérifié laisse le reste inchangé, tandis que le serveur le met en minuscules ; vérifier la valeur serveur séparément. |
| Trimmer (`trim`) | les deux / gauche / droite ; caractères vides = espaces | `  4711  ` → `4711` | `47 11` est conservé. Caractères à gauche `0` : `004711` → `4711`, mais `000` → vide. Les caractères constituent un ensemble, pas un texte de préfixe complet. |
| Remplir (`pad`) | longueur minimale, un caractère de remplissage, gauche/droite | Longueur 10, gauche `0` : `4711` → `0000004711` | Déjà 11 caractères restent 11 caractères. Droite `_`, longueur 6 : `ABC` → `ABC___`. |
| Tronquer (`truncate`) | longueur maximale | Longueur 10 : `ABCDEFGHIJKL` → `ABCDEFGHIJ` | `ABC` reste `ABC`. La troncature perd des informations et peut faire fusionner des numéros. |
| Affixe (`affix`) | ajouter/supprimer préfixe/suffixe | `INV-` + `4711` → `INV-4711` | Un affixe exact existant n'est pas ajouté en double. La suppression n'agit que sur le bord approprié et respecte la casse. |
| Nettoyer les caractères (`sanitize`) | conserver alphanumérique / lettres / chiffres / alphanumérique + espaces ; alternativement supprimer une classe de caractères | `DE 123.456.789` → `DE123456789` | Les signes peuvent être porteurs de sens. Lors de la suppression, l'entrée est une classe de caractères d'expression régulière ; protéger correctement le tiret, par exemple `.\-/`. |
| Sous-chaîne (`substring`) | début + longueur **ou** début + fin ; indices négatifs possibles | Début 3, fin 7 : `DE-4711-X` → `4711` | Le début compte à partir de 0, la fin est exclusive. Début −4 : quatre derniers caractères. Une source originale séparée est requise. |
| Extraire (`regex_extract`) | expression régulière, groupe de capture | `PO[- ]?(\d+)`, groupe 1 : `Order PO-45001234` → `45001234` | Premier résultat ; groupe 0 = résultat complet. Sans résultat : vide. Une source séparée est requise. |
| Rechercher et remplacer (`regex_replace`) | motif, remplacement, nombre | `\s+` → espace : `ACME    GmbH` → `ACME GmbH` | Nombre 0 = tous, 1 = premier résultat. Une source séparée est requise. Vérifier séparément l'expression régulière navigateur/serveur pour les motifs complexes. |
| Mapper les valeurs (`value_map`) | paires complètes de→vers ; ignorer la casse ; remplacement sans résultat | `stk` → `PCE` avec `STK→PCE` et casse ignorée | Un remplacement vide signifie **conserver l'entrée**. `BOX` reste `BOX` ; un remplacement fixe `C62` écraserait `BOX`. Le trimmage n'est pas automatique. |
| Formater la date (`date_format`) | modèle de sortie, par exemple `%d.%m.%Y`, `%m/%d/%Y`, `%Y-%m-%d`, `%d %b %Y` | `2026-10-28` → `28.10.2026` dans la cible texte | Pour les champs d'en-tête DATE, la valeur enregistrée peut rester ISO et seule l'affichage change. Un texte illisible reste inchangé ; le test serveur indique la raison. |
| Formater le nombre (`number_format`) | de_DE / en_US / en_GB / fr_FR ; décimales min./max. | `1234.5` → `1234,50` ou `1234.50` dans le résultat serveur vérifié | Pas de séparateur de milliers dans le résultat serveur vérifié. Pas de conversion de devise ou de quantité. Vérifier séparément l'arrondi et le retraitement. |
| Valeur fixe (`fix_value` dans l'éditeur, `set_value` dans l'API) | une valeur fixe | `USD` → `EUR` | Écrase également les valeurs existantes. À ne pas confondre avec une valeur par défaut. |
| Vider (`clear`) | aucun paramètre | `Altwert` → `""` | Vide la valeur ; ne supprime ni la définition de champ ni le document. |
| Supprimer toutes les lignes (`clear_rows`) | lignes de tableau uniquement | 2 positions → 0 | Peut invalider les références de lignes et le rapprochement de commande existant. |
| Ajouter une ligne (`add_row`) | début/fin ; par colonne valeur fixe ou source d'en-tête | Quantité `1`, montant net à partir de `header.total_net_amount` | Sans suppression préalable, uniquement avec une exécution unique appropriée. Pas d'agrégation automatique des positions existantes. |
| Sous-organisation fixe (`set_value`, routage) | cible existante parmi le choix des sous-organisations | Fournisseur A → Sous-organisation Nord | Pas d'attribut de statut/utilisateur/droit arbitraire. Alternativement attribution via `value_map` et source. |

### Valeur par défaut via l'interface

`default` complète sa valeur uniquement en cas d'entrée manquante/vide. Avec la valeur par défaut `1`, `null` et `""` donnent la valeur `1` ; `0` reste `0`, `100` reste `100`. C'est vérifié côté serveur. L'éditeur normal n'a pas d'étape propre à cet effet dans l'état vérifié. Le cas simple correspondant sur le plan métier peut souvent être représenté par **Cible est vide → Valeur fixe**. C'est une condition de règle avec attribution, pas un élément de menu masqué.

## Neuf séquences pratiques détaillées

- [01 · Fondamentaux, domaines d'application et tests sûrs](01-foundations.md)
- [02 · Nettoyage de texte : casse, trimmage et caractères](02-text-cleaning.md)
- [03 · Façonnage de numéros : remplissage, troncature, préfixe et suffixe](03-numbers-and-affixes.md)
- [04 · Sous-chaînes et motifs : découpage, extraction, remplacement](04-substrings-and-patterns.md)
- [05 · Mappages de valeurs et règles par ligne de tableau](05-value-mapping.md)
- [06 · Formater correctement les dates et les nombres](06-dates-and-numbers.md)
- [07 · Reprise de champs, valeurs fixes, vidage et valeurs par défaut](07-field-copy-and-defaults.md)
- [08 · Reconstruction des lignes de tableau](08-table-rows.md)
- [09 · Routage, ordre, données de base et répétitions](09-routing-and-execution.md)

| Séquence | Contenu | Point de vérification concret |
| --- | --- | --- |
| 01 Fondamentaux | Cible, source, quatre domaines, pipeline, conditions, aperçu, enregistrement | Cas approprié, cas contraire, règle enregistrée rouverte |
| 02 Nettoyage de texte | Les quatre casses, trimmage, tous les modes de nettoyage | Espaces internes, suite de zéros pure, caractères porteurs de sens |
| 03 Nombres | Remplissage, troncature, les quatre variantes d'affixe | Numéro trop long, préfixe déjà présent, préfixes doubles |
| 04 Motifs | Sous-chaîne, indices négatifs, extraction/groupes, remplacement/nombre | Source séparée, aucun résultat, plusieurs résultats |
| 05 Mappage | Paires, casse, remplacement, application par ligne | `STK→PCE`, `BOX` inconnu, réapplication sur `PCE` |
| 06 Formats | Date, DATE vs. texte, date illisible, formats de nombres | Valeur serveur réelle plutôt qu'affichage navigateur supposé |
| 07 Reprise de champ | Autre source, cible vide, valeur fixe, vidage, valeur par défaut API | Protéger le numéro de commande correct existant ; zéro reste zéro |
| 08 Tableaux | Suppression, ajout, valeurs de colonnes statiques et dynamiques | Ordre, répétition, nombre de lignes et références de commande |
| 09 Interaction | Routage, phases, recherche, exécution unique, journaux | Source d'en-tête nettoyée, condition sautée, deuxième enregistrement |

## Conditions et sources

Avec « Toujours », la règle s'applique sans restriction métier pour le type de document. « Seulement si… » la limite par des conditions. Les valeurs d'en-tête sont disponibles dans le contexte `header.*`, les caractéristiques de document dans `doc.*` ; `row.*` n'est disponible que dans le contexte de ligne d'une règle de colonne. Les groupes imbriqués Et/Ou permettent des critères combinés. Pour les opérateurs individuels, s'applique la documentation séparée des conditions de règle.

**Exemple de reprise de champ :** Cible `purchase_order`, source `header.invoice_id`, condition `header.purchase_order` est vide, étapes Trimmer → Mise en majuscules. `  po-4711  ` donne `PO-4711`. Un numéro de commande déjà correctement renseigné doit rester inchangé. Ne pas vider la fausse source : copier avec traitement ne déplace pas la source.

**Exemple de numéro d'article :** Tableau `INVOICE_TABLE`, colonne `ITEM_NUMBER`, supprimer le préfixe `Art.-Nr. ` → conserver alphanumérique → Mise en majuscules. `Art.-Nr. ab-12/3` donne `AB123`. Uniquement approprié si le système cible attend exactement cette forme.

**Exemple de ligne totale :** Pour un fournisseur clairement délimité, d'abord `clear_rows`, puis `add_row` ; `POSITION=001`, `QUANTITY=1`, `NET_AMOUNT` à partir du montant net de l'en-tête. La question de savoir si un rapprochement de commande sur le total est métier correct est décidée par la configuration PO supplémentaire et un test de rapprochement séparé.

## Répétition et exécution unique

Les règles peuvent s'exécuter à nouveau dans plusieurs passages de traitement et lors de l'enregistrement. Vérifiez toujours **l'ensemble du pipeline**, pas seulement la stabilité d'une seule étape.

* `substring`, `regex_extract` et `regex_replace` ne peuvent pas lire leur propre valeur cible dans le contrat serveur vérifié. Une source séparée est requise ; `run_once` ne lève pas cette prescription.
* L'ajout d'un affixe exact déjà présent est stable. La suppression d'un préfixe présent plusieurs fois peut, en revanche, continuer à supprimer à chaque passage.
* `A→B` et `B→C` dans le même mappage de valeurs peuvent, en deux passages, transformer `A` en `C`. Testez les sorties à nouveau comme entrées.
* `clear_rows → add_row` reconstruit un tableau de manière limitée. `add_row` sans suppression préalable nécessite une exécution unique appropriée, sinon le tableau croît à chaque enregistrement.
* « Une seule fois par document » marque une règle effectivement appliquée. Les conditions non remplies ne consomment pas l'application. Sans preuve de document/application lisible de manière fiable, l'exécution d'une règle à exécution unique est différée.

## Après la recherche de données de base et avant le rapprochement de commande

« Exécuter également après la recherche de données de base » ajoute une phase après le remplissage par recherche et avant le rapprochement de commande. Seules les règles ainsi marquées s'exécutent dans cette phase supplémentaire. Les autres passages restent en place. Combiné avec l'exécution unique, la règle attend lors du premier passage d'extraction la phase ultérieure ; si la phase de recherche n'a pas lieu, un passage régulier ultérieur est envisageable. L'affichage des phases de l'éditeur actuel montre ces différences.

## Un test de réception fiable

1. Définir l'objectif métier, le format du système cible et le domaine d'application.
2. Préparer une valeur brute appropriée, un cas contraire, une valeur vide et un résultat déjà traité.
3. Vérifier les conditions et toutes les valeurs intermédiaires dans l'aperçu.
4. Exécuter le test côté serveur avec le même exemple ; comparer particulièrement les motifs complexes et les formats de nombres/dates.
5. Enregistrer la règle et la rouvrir. N'utiliser une règle active que dans la portée de test prévue.
6. Pour un document isolé, enregistrer, recharger et vérifier la valeur et l'affichage ; pour les tableaux, vérifier également le nombre de lignes et les valeurs de colonnes.
7. Enregistrer une nouvelle fois. Le résultat ne doit pas être modifié ou multiplié de manière involontaire.
8. Si métier nécessaire, vérifier également le rapprochement de commande et la réception réelle dans le système cible. Un journal de transformation seul ne prouve pas ces résultats.

## Ce qu'une transformation n'accomplit pas automatiquement

Pas de nouvelle reconnaissance OCR, pas de conversion mathématique d'unité ou de devise, pas d'agrégation arbitraire de tableaux et pas d'écriture ERP complète. Le routage est limité à l'attribut de document proposé. La disponibilité et l'affichage exact dépendent de la version déployée, du type de document et de la configuration de l'organisation.

## Document d'exercice cohérent

{% file src="../../../../../.gitbook/assets/transformation-training-invoice-fr-20261028.pdf" %}
Télécharger la facture de formation
{% endfile %}

Le document fictif contient deux positions, des écritures différentes de l'unité et une référence de commande dans le texte libre. Pour des tests de règles reproductibles, les valeurs de départ sont préparées de manière ciblée ; ceci ne constitue pas une preuve d'extraction OCR automatique sans erreur.
