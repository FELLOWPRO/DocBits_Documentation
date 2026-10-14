# Première

La première règle correspondante est appliquée et aucune autre règle n'est évaluée.

**Exemple :**

| Règle | Condition            | Groupe renvoyé |
| ----- | -------------------- | -------------- |
| 1     | Total Amount <= 1000 | GROUP\_1       |
| 2     | Total Amount <= 2000 | GROUP\_2       |
| 3     | Total Amount <= 5000 | GROUP\_5       |
| 4     | Total Amount <= 4000 | GROUP\_4       |
| 5     | Total Amount <= 3000 | GROUP\_3       |

Si le montant total est de **1500**, les règles évaluées seront :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (correspond) → L'arbre de décision cesse d'évaluer les règles suivantes et applique **GROUP\_2**.
