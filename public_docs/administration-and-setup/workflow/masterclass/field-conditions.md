---
description: "Choisir Field is, Docfield is ou Compare two Fields"
---

# P1 : choisir Field is, Docfield is ou Compare two Fields

Trois cartes de condition se ressemblent dans le concepteur, et leur différence décide de ce qu’une règle peut réellement détecter. Cette page vous aide à choisir la bonne, puis vous propose trois exercices courts qui montrent ce que chaque carte renvoie. À la fin, vous saurez distinguer « vide » de « zéro », « faux » de « absent », et une condition non remplie d’une erreur.

Faites les exercices dans Advanced Test, dans votre propre organisation de test, avec un document synthétique. Rien ici ne touche un document client.

## Quelle carte vous faut-il ?

| Si vous voulez vérifier... | Utilisez | Carte et version |
| --- | --- | --- |
| si un champ porte une valeur, quelle qu’elle soit | **Field is** | `condition_docfield_status` v2 |
| un champ par rapport à une valeur que vous saisissez | **Docfield is** | `condition_docfield_operator_value` v2 |
| deux champs du même document l’un par rapport à l’autre | **Compare two Fields** | `condition_compare_two_docfield_values` v2 |

Les trois sont des conditions : elles renvoient un résultat et ne modifient rien sur le document. Un contrôle d’état vide ne prouve pas qu’un champ existe dans la mise en page ni que son contenu est valide pour l’entreprise. Les pages de chaque carte détaillent tous les réglages : [Field is](../and/document-field/field-is.md), [Docfield is](../and/document-field/docfield-is.md) et [Compare two Fields](../and/document-field/compare-two-fields.md).

## Exercice 1 : découvrir ce que signifie « vide »

**Objectif :** savoir quelles valeurs Field is version 2 traite comme vides.

1. Ajoutez **Field is** version 2 à une règle de votre organisation de test et sélectionnez un champ texte de votre mise en page.
2. Mettez l’état du champ sur `field_empty` (Empty or missing).
3. Lancez huit cas Advanced Test avec des données de document complètes : champ absent, `null`, texte vide `""`, espaces seuls `" "`, booléen `false`, nombre `0`, texte `"0"` et texte `"false"`.

**Terminé quand :** les cinq premiers cas renvoient `field_empty=success` et les trois derniers `field_empty=failed_condition`. Ces huit cas ont été testés dans Dev avec des données de document complètes.

Le nombre `0`, le texte `"0"` et le texte `"false"` sont des valeurs, pas des absences. Si vrai ou faux est votre décision métier, utilisez une condition de case à cocher explicite au lieu de tester le champ sur son absence de contenu.

## Exercice 2 : comparer un champ à une valeur

**Objectif :** voir comment l’opérateur et le type de champ changent la réponse.

1. Choisissez un champ numérique comme `total_amount`, l’opérateur `gt` et la valeur `1000`.
2. Testez `1000`, `1000.01`, un champ absent et une valeur invalide.

**Terminé quand :** `1000` renvoie `failed_condition`, car `gt` signifie strictement supérieur, `1000.01` renvoie `success`, et une saisie absente ou invalide renvoie `error`.

## Exercice 3 : comparer deux champs

**Objectif :** savoir quand deux valeurs sont comparées et quand la carte ne peut pas les comparer du tout.

1. Définissez le champ de gauche, l’opérateur et le champ de droite. Utilisez deux champs dont les types sont compatibles.
2. Testez des valeurs égales, des valeurs différentes et une saisie absente.

**Terminé quand :** des valeurs égales satisfont `eq`, des valeurs différentes renvoient `failed_condition`, et une saisie absente renvoie `error` au lieu d’une inégalité démontrée.

## Ce que signifient les trois résultats

| Résultat | Ce qu’il vous dit |
| --- | --- |
| `success` | La carte a comparé les valeurs et la condition était remplie. |
| `failed_condition` | La carte a comparé les valeurs et la condition n’était pas remplie. `0` et `"0"` finissent ici lors d’un contrôle d’état vide. |
| `error` | La carte n’a pas pu comparer, par exemple parce qu’une valeur manque ou n’est pas valide. Une erreur n’est pas la même réponse que « différent ». |

## Le type fait partie de la comparaison

Une valeur `"1000.01"` dans un champ AMOUNT n’est pas identique aux mêmes caractères dans un champ texte. Le kit d’exercices v2 utilise AMOUNT et des points décimaux dans le JSON. Vérifiez ensemble la clé technique du champ, la mise en page et le type. Un libellé traduit n’est pas une clé technique, et un symbole monétaire n’est pas une valeur numérique.

## Cartes et paramètres d’exemple

Ces valeurs décrivent des paramètres de cartes individuellement, pas un workflow complet importable. Remplacez YOUR\_\* par vos propres choix de test. L’ID masqué de l’appelant est géré par le concepteur. Catalogue : Dev, DocFlow 2.10.38, 21 octobre 2026 ; vérifiez les versions disponibles et les droits dans votre propre organisation.

### `condition_docfield_status` · v2

Identité : `6f346541-faa0-42bd-b1a5-b23282157da1`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_status` | `field_empty / field_not_empty` | `"field_empty"` |

### `condition_docfield_operator_value` · v2

Identité : `1c35a5a0-1592-446c-9a61-6abb14d27450`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `operator` | `eq / neq / gt / ge / lt / le` | `"gt"` |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_value` | `field_value:str` | `"1000"` |

### `condition_compare_two_docfield_values` · v2

Identité : `3b3cdc55-6afe-4797-ae8b-9480ec3a8a30`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |

## Cas de test métier

| Cas | Entrée / configuration | Résultat attendu |
| --- | --- | --- |
| FIELD-01 | missing / null / "" / " " / false | field\_empty=success |
| FIELD-02 | 0 / "0" / "false" | field\_empty=failed\_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed\_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Preuves et limites

Certains résultats de carte et de nœud ont été vérifiés avec des données synthétiques dans Advanced Test. Les réponses figurent dans le kit d’exercices. Les actions sur document sont simulées ; ces tests n’établissent ni une exécution de document enregistrée ni une remise externe.

[Poursuivre l’apprentissage](../workflow-learning-path.md) · [Kit de formation](../workflow-training-kit.md)
