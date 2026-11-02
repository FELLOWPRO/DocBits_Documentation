---
description: "P1 : calculer les colonnes et contrôler les dépendances regex"
---

# P1 : calculer les colonnes et contrôler les dépendances regex

**Calculate Columns** calcule deux colonnes d’une ligne et écrit le résultat. **Calculate in / CALC_COLUMNS_REGEX** ajoute une condition regex sur une troisième colonne. La regex décide ici de calculer ; elle n’extrait ni ne remplace du texte. L’ancienne explication de substitution ne décrit pas cette carte.

Exemple : `QTY=2`, `PRICE=10`, opération `*`, résultat `TOTAL=20.0`. Pour la variante regex, utilisez `TYPE` et `^A$`. Une ligne A est calculée. Pour une ligne B sans correspondance, le code écrit un résultat vide ; un TOTAL existant n’est pas préservé automatiquement.

L’aide arithmétique arrondit à quatre décimales. Un opérande vide peut devenir 0 ; deux textes vides donnent vide. `+` peut concaténer du texte non numérique. Dans la fonction examinée, `10/0` provoque une erreur. Validez nombres et cellules obligatoires avant le calcul et définissez un chemin d’erreur.

Conservez un tableau avant/après complet : deux lignes correspondantes, une sans correspondance, entrée vide, texte invalide et division par zéro. Pour des calculs dépendants A→B, reliez explicitement les cartes et contrôlez la valeur actualisée lue par B. Comparez chaque ligne et les autres colonnes existantes, pas seulement le statut du document.

## Cartes et paramètres d’exemple

Ces valeurs décrivent des paramètres de cartes, pas un workflow complet importable. Remplacez YOUR_* par vos choix de test. Le concepteur gère l’ID caché de l’appelant. Catalogue : Dev, DocFlow 2.10.38, 21 octobre 2026 ; contrôlez versions et droits de votre organisation.

### `calc_columns` · v2

Identité: `92d7a634-736a-4e1f-80b3-2b521efcd81c`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |

### `calc_columns_regex` · v2

Identité: `dbf035c8-927b-444a-9e5a-18555f5deacf`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `regex_pattern` | `regex_pattern:str` | `"^A$"` |
| `column_name_dependency` | `column_name_dependency:str` | `"TYPE"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |

## Cas de test métier

| Cas | Entrée / configuration | Résultat attendu |
| --- | --- | --- |
| CALC-01 | QTY=2; PRICE=10; TYPE=A; ^A$ | TOTAL=20.0 |
| CALC-02 | QTY=2; PRICE=10; TYPE=B; ^A$; TOTAL=99 | TOTAL="" |
| CALC-03 | 10 / 3 | 3.3333 |
| CALC-04 | 10 / 0 | error |
| CALC-05 | "" + 2 | 2.0 |
| CALC-06 | x + y | "x y" |

## Preuves et limites

Paramètres et comportement ont été confrontés au catalogue Dev et au code examiné. Les cas métier constituent une procédure de recette. Aucune approbation personnelle, modification réelle ou livraison n’a été réalisée pour ce chapitre.

[Poursuivre l’apprentissage](../workflow-learning-path.md) · [Kit de formation](../workflow-training-kit.md)
