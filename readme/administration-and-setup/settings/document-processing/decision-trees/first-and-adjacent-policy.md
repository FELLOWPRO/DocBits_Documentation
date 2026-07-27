# Première et adjacente

Choisit le résultat de la règle adjacente à la première règle qui est vraie.

**Exemple :**

| Règle | Condition            | Groupe renvoyé |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Si le montant total est de **1500**, les règles évaluées seront :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (correspond)

Étant donné que la **Règle 2** est la première règle qui correspond, **Première et adjacente** appliquerait le résultat de la **Règle 3** : **GROUP_3**.
