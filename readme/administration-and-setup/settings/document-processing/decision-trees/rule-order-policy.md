# Politique d'ordre des règles (Rule Order)

Cette politique applique les règles dans l'ordre où elles apparaissent dans l'arbre de décision et renvoie le résultat de la règle qui correspond en premier.

**Exemple :**

| Règle | Condition            | Groupe renvoyé |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Étant donné que la valeur d'entrée est **Total Amount = 3500**, l'évaluation des règles serait :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (ne correspond pas)
* **Règle 3** : Total Amount <= 3000 (correspond)
* **Règle 4** : Total Amount <= 4000 (correspond)
* **Règle 5** : Total Amount <= 5000 (correspond)

Sous **Rule Order**, l'arbre traitera les règles dans l'ordre où elles sont répertoriées. Ainsi, les règles correspondantes seront :

* **Règle 3** : GROUP_3
* **Règle 4** : GROUP_4
* **Règle 5** : GROUP_5

**Résultat** : **GROUP_3**, **GROUP_4**, **GROUP_5**
