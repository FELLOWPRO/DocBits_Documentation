# Politique de collecte (somme) (Collect (sum))

Cette politique collecte toutes les règles correspondantes et additionne les résultats. Elle ne fonctionne qu'avec un **Return Type Value**.

**Exemple :**

| Règle | Condition            | Valeur renvoyée |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Pour la valeur d'entrée **Total Amount = 2500**, l'évaluation des règles serait :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (ne correspond pas)
* **Règle 3** : Total Amount <= 3000 (correspond, Return Value = 3)
* **Règle 4** : Total Amount <= 4000 (correspond, Return Value = 4)
* **Règle 5** : Total Amount <= 5000 (correspond, Return Value = 5)

Étant donné que la politique **Collect (sum)** est appliquée, on additionne les **Return Values** des règles correspondantes, à savoir **3, 4, 5**.

**L'addition de ces valeurs** donne :

* 5 + 4 + 3 = **12**

Ainsi, le résultat renvoyé par l'arbre de décision serait **12**, qui est la somme de toutes les valeurs de retour correspondantes.
