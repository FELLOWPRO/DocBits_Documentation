# Politique de collecte (min/max/count) (Collect (min/max/count))

Cette politique collecte toutes les règles correspondantes et sélectionne soit le **minimum**, soit le **maximum**, soit **compte** les occurrences. Elle ne fonctionne qu'avec un **Return Type Value**.

**Exemple :**

| Règle | Condition            | Valeur renvoyée |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Si l'option **Collect (min)** est sélectionnée, le résultat renverra le **minimum** des **Return Values** des règles correspondantes.
   * Pour la valeur d'entrée **Total Amount = 3500**, l'évaluation des règles serait :
     * **Règle 1** : Total Amount <= 1000 (ne correspond pas)
     * **Règle 2** : Total Amount <= 2000 (ne correspond pas)
     * **Règle 3** : Total Amount <= 3000 (correspond, Return Value = 3)
     * **Règle 4** : Total Amount <= 4000 (correspond, Return Value = 4)
     * **Règle 5** : Total Amount <= 5000 (correspond, Return Value = 5)
   * Les **règles correspondantes** sont la Règle 3, la Règle 4 et la Règle 5, avec des **Return Values** de **3, 4 et 5**.
   * Étant donné que la politique **Collect (min)** est appliquée, le résultat sera la **valeur minimale**, soit **3**.
   * **Résultat** : **3**
2. Si l'option **Collect (max)** est sélectionnée, le résultat renverra le **maximum** des **Return Values** des règles correspondantes.
   * Pour la même évaluation que ci-dessus, le résultat sera :
   * **Résultat** : **5**
3. Si l'option **Collect (count)** est sélectionnée, le résultat comptera le **nombre de règles correspondantes**.
   * Pour la même évaluation que ci-dessus, le résultat sera :
   * **Résultat** : **3** (puisque 3 règles correspondent).
