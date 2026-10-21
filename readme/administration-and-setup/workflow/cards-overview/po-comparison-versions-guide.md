# Comparaison avec la commande : sens, tolérance et versions des cartes

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-72e8f3204ac8-fr.png" alt="Cartes disponibles dans la catégorie sélectionnée. Renseignez les champs avant utilisation."><figcaption><p>Cartes disponibles dans la catégorie sélectionnée. Renseignez les champs avant utilisation.</p></figcaption></figure>

Les cartes de comparaison PO comparent une valeur choisie à une valeur de référence. La référence détermine la base d'un pourcentage de tolérance. Effectuez d’abord le rapprochement des bons de commande, puis sélectionnez la comparaison, l’opérateur, Any/All et la tolérance demandée par la carte spécifique.

## Sens de comparaison

| Option stockée | Côté comparé | Côté référence |
| --- | --- | --- |
| `po_document` | Bon de commande | Document |
| `received_document` | Données reçues | Document |
| `po_received` | Bon de commande | Données reçues |
| `document_po` | Document | Bon de commande |
| `document_received` | Document | Données reçues |
| `received_po` | Données reçues | Bon de commande |

Le côté reçu est dérivé des données de bon de commande correspondantes. Une comparaison reçue sur la carte de prix unitaire peut utiliser des quantités pour dériver un montant comparable ; il ne s’agit pas d’une comparaison directe d’une quantité avec un prix en devise. Utilisez les valeurs enregistrées par cette carte dans le journal lors de la vérification du calcul.

## Pourquoi la direction est importante

Pour une référence de `100` et une valeur comparée de `110`, un pourcentage de tolérance de `5` correspond à `5` autour de la référence. Si le document est la référence et que sa valeur est modifiable, la modification du document modifie également cette base de tolérance. Choisissez délibérément la référence, notamment pour une approbation automatique.

Inverser les côtés inverse les opérateurs d'ordre : `>` devient `<`, `>=` devient `<=`, et vice versa. L'égalité et l'inégalité conservent leur sens. Ne renversez pas un opérateur sans inspecter également les côtés choisis.

Les versions contenant la migration de comparaison ont affecté les cartes enregistrées de `po_document` à `document_po` et de `received_document` à `document_received`, tout en inversant l'opérateur de tri. Les versions concernées sont la tolérance de quantité v4, la confirmation de commande au bon de commande v4 et le prix unitaire v4/v5. La différence combinée de prix et de quantité est exclue de cette migration de carte enregistrée. Inspecter la configuration enregistrée et tester ses résultats commerciaux après une version ; ne l'inversez pas manuellement une seconde fois.

## Versions de cartes à prix unitaire

| Version | Configuration |
| --- | --- |
| v3 | Utilise le comportement de comparaison précédent. Ne présumez pas qu’il expose les nouveaux champs de direction et de tolérance. |
| v4 | Ajoute la sélection côté comparaison. |
| v5 | Inclut Any/All, l'opérateur, le montant de tolérance, le type de tolérance et la sélection côté comparaison. |

Choisissez une tolérance absolue pour un montant fixe et une tolérance en pourcentage pour un écart par rapport à la référence sélectionnée. Utiliser l'opérateur proposé par la carte ; l’égalité exacte et le fait de se situer dans une tolérance sont des décisions différentes. Il n’existe pas de tolérance commerciale universelle adaptée à chaque fournisseur ou type de document.

## Exemple de vérification

1. Utilisez une référence de bon de commande correspondante de `100` et une valeur de document `110`.
2. Sélectionnez Document à bon de commande, une comparaison dans les limites de tolérance lorsqu'elle est proposée et le pourcentage `5`. Attendez-vous à une comparaison hors bande.
3. Testez la limite de tolérance exacte, les valeurs de chaque côté et un bon de commande manquant.
4. Avec plusieurs lignes, vérifiez Any versus All en utilisant une ligne de réussite et une ligne d'échec.
5. Inspectez les valeurs comparées du journal, les côtés sélectionnés, l'opérateur et la tolérance, puis vérifiez la branche de flux de travail résultante.

Un bon de commande sans correspondance, une valeur non numérique et une fausse condition commerciale sont des résultats différents. Ne considérez pas les données manquantes comme une correspondance réussie. Pour les frais, utilisez [Any / All Charges](../and/compare-with-purchase-order/any-all-charges.md), qui explique séparément le comportement des frais manquants et v2/v3.

Continuez avec le [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md) et la référence de carte individuelle pour ses champs restants.
