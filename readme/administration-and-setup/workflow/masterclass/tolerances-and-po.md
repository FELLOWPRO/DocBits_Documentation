---
description: "P1 : préciser la référence des tolérances et comparaisons PO"
---

# P1 : préciser la référence des tolérances et comparaisons PO

La tolérance en pourcentage dépend du **côté de référence**. Dans la carte PO v5 examinée, `document_po` compare le document à la commande ; la commande est la base du pourcentage. `po_document` inverse comparaison et base. Les six directions autorisées comprennent aussi la valeur réceptionnée. Définissez direction, opérateur et Any/All explicitement.

Exemple : commande 100, document 102.02, égalité à 2 %. Avec la commande comme référence, l’intervalle est 98–102 : hors tolérance. Avec le document, il est 99.9796–104.0604 : la commande 100 est dedans. Le document 102 atteint exactement la limite supérieure incluse de la première direction. Une tolérance absolue de 2 utilise l’unité de la valeur comparée.

La carte normalise les prix par unité tarifaire et utilise les données de commande ou réception selon la direction. Vérifiez rapprochement, quantités et unités. Any exige une comparaison correspondante ; All toutes les comparaisons effectuées. **Aucune ligne comparable** est une erreur de données en v5, pas un All satisfait automatiquement. Comptez séparément les lignes non rapprochées.

Pour les workflows existants, relisez version, direction et opérateur enregistrés : des migrations ont modifié ces réglages. Les anciennes étiquettes ne suffisent pas pour la recette. Notez valeurs, référence, limite, plus petit dépassement, précision, commande absente et ligne non rapprochée. Ce calcul ne remplace pas la recette avec vos référentiels PO.

## Cartes et paramètres d’exemple

Ces valeurs décrivent des paramètres de cartes, pas un workflow complet importable. Remplacez YOUR_* par vos choix de test. Le concepteur gère l’ID caché de l’appelant. Catalogue : Dev, DocFlow 2.10.38, 21 octobre 2026 ; contrôlez versions et droits de votre organisation.

### `condition_docfield_operator_docfield_tolerances` · v2

Identité: `d0472648-d1a2-499d-83e3-b47306ae130a`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |

### `condition_doc_to_po_unit_price` · v5

Identité: `ed2cd0fe-ac87-4bae-9a86-0b0576159b28`

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
| PO-01 | document_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared_rows=0 | erreur de données |
| PO-05 | unmatched_rows>0 | vérifier la couverture séparément |

## Preuves et limites

Paramètres et comportement ont été confrontés au catalogue Dev et au code examiné. Les cas métier constituent une procédure de recette. Aucune approbation personnelle, modification réelle ou livraison n’a été réalisée pour ce chapitre.

[Poursuivre l’apprentissage](../workflow-learning-path.md) · [Kit de formation](../workflow-training-kit.md)
