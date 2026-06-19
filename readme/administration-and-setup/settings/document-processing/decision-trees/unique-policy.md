# Politique d'unicité (Unique)

Garantit qu'une seule règle est satisfaite. Si plusieurs règles sont satisfaites, l'arbre de décision renverra « false ».

**Exemple :**

| Règle | Condition            | Groupe renvoyé |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Si le montant total est de **1500**, les règles évaluées seront :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (correspond)
* **Règle 3** : Total Amount <= 5000 (correspond)
* **Règle 4** : Total Amount <= 4000 (correspond)
* **Règle 5** : Total Amount <= 3000 (correspond)

Étant donné que plusieurs règles correspondent (**Règle 2**, **Règle 3**, **Règle 4**, **Règle 5**), l'arbre de décision renverra **false**, car la politique **Unique** garantit qu'une seule règle peut correspondre.
