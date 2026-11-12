---
description: "Préciser la référence des tolérances et des comparaisons PO"
---

# P1 : préciser la référence des tolérances et comparaisons PO

Une tolérance de 2 pour cent n’est pas un montant fixe. C’est 2 pour cent du côté avec lequel vous comparez, donc la même ligne de facture peut échouer dans un sens et passer dans l’autre. Cette page le montre sur une paire de valeurs, vous donne trois exercices pour le reproduire, puis liste les six directions de comparaison et les paramètres de carte que vous pouvez reprendre dans votre propre test.

Faites les exercices dans Advanced Test, dans votre propre organisation de test, avec un document synthétique et une commande rapprochée.

## Le côté de référence est la base

Dans la carte PO version 5 examinée, `document_po` compare la valeur du document à celle de la commande ; la commande est donc la base d’une tolérance en pourcentage. `po_document` inverse à la fois la comparaison et la base. Les six directions autorisées incluent aussi le côté réceptionné. Définissez direction, opérateur et Any/All explicitement au lieu de faire confiance à ce qu’une carte enregistrée contient encore.

## Exercice 1 : mêmes valeurs, deux directions

**Objectif :** voir deux résultats différents sortir des mêmes chiffres.

1. Préparez une commande rapprochée de `100` et un prix unitaire de document de `102.02`.
2. Comparez avec l’opérateur `eq` et une tolérance de `2` pour cent, d’abord avec `document_po`. Attendez-vous à `false` : 2 pour cent de 100 font 2, l’intervalle fermé va donc de 98 à 102, et 102.02 se situe 0.02 au-dessus.
3. Répétez le même cas avec `po_document`. Attendez-vous à `true` : 2 pour cent de 102.02 font 2.0404, l’intervalle va de 99.9796 à 104.0604, et la valeur de commande 100 s’y trouve.

**Terminé quand :** les deux résultats et les deux intervalles sont notés, et vous pouvez dire à partir de quelle valeur le pourcentage a été calculé dans chaque direction.

Une tolérance absolue de `2` se comporte autrement : elle utilise l’unité de la valeur comparée et ne se déplace pas avec la référence.

## Exercice 2 : trouver la limite exacte

**Objectif :** savoir si le bord de l’intervalle compte.

1. Gardez `document_po`, `eq` et la tolérance de 2 pour cent, et passez la valeur du document à `102`.
2. Lancez le cas, puis relancez-le avec `102.01`.

**Terminé quand :** `102` renvoie `true` et `102.01` renvoie `false`. La borne est incluse : 102 se trouve exactement sur la limite supérieure de l’intervalle 98 à 102.

## Exercice 3 : Any, All et les lignes comparées

**Objectif :** savoir ce que la carte fait de plusieurs lignes et ce qui se passe quand il n’y a rien à comparer.

1. Construisez un document avec deux lignes sur la même commande rapprochée : une dans la tolérance, une en dehors.
2. Lancez la carte avec `match_any`, puis avec `match_all`.
3. Lancez un document qui n’a aucune ligne comparable.

**Terminé quand :** `match_any` passe sur la seule ligne correspondante, `match_all` échoue dès qu’une comparaison échoue, et le document sans ligne comparable renvoie une erreur de données. En version 5, c’est une erreur et non un All satisfait automatiquement.

## Quel côté est la base ?

| Option enregistrée | Côté comparé | Côté de référence (base du pourcentage) |
| --- | --- | --- |
| `po_document` | Commande | Document |
| `received_document` | Données réceptionnées | Document |
| `po_received` | Commande | Données réceptionnées |
| `document_po` | Document | Commande |
| `document_received` | Document | Données réceptionnées |
| `received_po` | Données réceptionnées | Commande |

## Vérifiez avant de faire confiance à un workflow existant

La carte normalise les prix par unité tarifaire et utilise les données de commande ou de réception selon la direction : contrôlez donc d’abord le rapprochement, les quantités et les unités. Any a besoin d’une comparaison correspondante ; All, de toutes les comparaisons réellement effectuées. Les lignes non rapprochées se relèvent séparément.

Sur un workflow existant, relisez la version enregistrée, la direction et l’opérateur : des migrations ont modifié les réglages de comparaison, les libellés historiques ne suffisent donc pas comme preuve de recette. Notez les valeurs et la référence, la limite exacte, le plus petit dépassement, la précision d’arrondi, la commande absente et la ligne non rapprochée. Ce calcul ne remplace pas une recette avec vos propres données de base PO.

## Cartes et paramètres d’exemple

Ces valeurs décrivent des paramètres de cartes individuellement, pas un workflow complet importable. Remplacez YOUR\_\* par vos propres choix de test. L’ID masqué de l’appelant est géré par le concepteur. Catalogue : Dev, DocFlow 2.10.38, 21 octobre 2026 ; vérifiez les versions disponibles et les droits dans votre propre organisation.

### `condition_docfield_operator_docfield_tolerances` · v2

Identité : `d0472648-d1a2-499d-83e3-b47306ae130a`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |

### `condition_doc_to_po_unit_price` · v5

Identité : `ed2cd0fe-ac87-4bae-9a86-0b0576159b28`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `operator_any_all` | `match_any / match_all` | `"match_all"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |
| `comparison_data` | `po_document / received_document / po_received / document_po / document_received / received_po` | `"document_po"` |

## Cas de test métier

| Cas | Entrée / configuration | Résultat attendu |
| --- | --- | --- |
| PO-01 | document\_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document\_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po\_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared\_rows=0 | erreur de données |
| PO-05 | unmatched\_rows>0 | contrôler la couverture séparément |

## Preuves et limites

Les paramètres et le comportement ont été vérifiés contre le catalogue Dev et la révision de code examinée. Les cas de test métier sont une procédure de recette. Aucune approbation personnelle, aucune modification de données réelles et aucune remise n’ont été effectuées pour ce chapitre.

[Poursuivre l’apprentissage](../workflow-learning-path.md) · [Kit de formation](../workflow-training-kit.md)
