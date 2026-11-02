---
description: "P1 : choisir Field is, Docfield is ou Compare two Fields"
---

# P1 : choisir Field is, Docfield is ou Compare two Fields

Utilisez **Field is** pour l’état vide, **Docfield is** pour comparer à une valeur configurée et **Compare two Fields** pour deux valeurs du document courant. Un contrôle de vide ne prouve ni l’existence du champ dans la mise en page ni sa validité métier.

Pour Field is v2, champ absent, `null`, texte vide, espaces seuls et booléen `false` sont vides. Le nombre `0`, le texte `"0"` et le texte `"false"` ne le sont pas. Ces huit cas ont été testés en Dev avec des données documentaires complètes. Employez une condition de case à cocher explicite pour une décision vrai/faux.

`"1000.01"` dans un champ AMOUNT diffère des mêmes caractères dans un champ texte. Le kit v2 utilise AMOUNT et des points décimaux en JSON. Vérifiez ensemble clé technique, mise en page et type. Une étiquette traduite n’est pas une clé technique ; un symbole monétaire n’est pas une valeur numérique.

Pour Compare two Fields, définissez champ gauche, opérateur et champ droit. Vérifiez types compatibles et deux entrées ; une valeur absente ou incomparable est une erreur de données, pas une inégalité démontrée. Répétez cas positif, négatif, entrée absente et limite exacte. Notez valeur, type et sortie choisie.

## Cartes et paramètres d’exemple

Ces valeurs décrivent des paramètres de cartes, pas un workflow complet importable. Remplacez YOUR_* par vos choix de test. Le concepteur gère l’ID caché de l’appelant. Catalogue : Dev, DocFlow 2.10.38, 21 octobre 2026 ; contrôlez versions et droits de votre organisation.

### `condition_docfield_status` · v2

Identité: `6f346541-faa0-42bd-b1a5-b23282157da1`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_status` | `field_empty / field_not_empty` | `"field_empty"` |

### `condition_docfield_operator_value` · v2

Identité: `1c35a5a0-1592-446c-9a61-6abb14d27450`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `operator` | `eq / neq / gt / ge / lt / le` | `"gt"` |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_value` | `field_value:str` | `"1000"` |

### `condition_compare_two_docfield_values` · v2

Identité: `3b3cdc55-6afe-4797-ae8b-9480ec3a8a30`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |

## Cas de test métier

| Cas | Entrée / configuration | Résultat attendu |
| --- | --- | --- |
| FIELD-01 | missing / null / "" / "   " / false | field_empty=success |
| FIELD-02 | 0 / "0" / "false" | field_empty=failed_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Preuves et limites

Des résultats sélectionnés de cartes et de nœuds ont été vérifiés avec des données synthétiques dans Advanced Test. Les réponses sont dans le kit. Les actions documentaires sont simulées ; elles ne prouvent ni exécution persistante ni livraison externe.

[Poursuivre l’apprentissage](../workflow-learning-path.md) · [Kit de formation](../workflow-training-kit.md)
