# N'importe quel

Plusieurs règles peuvent être vraies, mais le résultat de ces règles doit être identique.

**Exemple :**

| Règle | Condition            | Groupe renvoyé |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Si le montant total est de **2500**, les règles évaluées seront :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (ne correspond pas)
* **Règle 3** : Total Amount <= 3000 (correspond)
* **Règle 4** : Total Amount <= 4000 (correspond)
* **Règle 5** : Total Amount <= 5000 (correspond)

Pour que la politique **N'importe quel** s'applique, toutes les règles correspondantes doivent renvoyer le même **Return Group**. Étant donné que les groupes ne correspondent pas entre les différentes règles, le résultat serait **false**.
