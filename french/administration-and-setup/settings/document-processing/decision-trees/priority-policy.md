# Priorité

Choisir cette option vous permet de définir des priorités pour chaque règle. Plus le numéro sélectionné est bas, plus la priorité est élevée (c'est-à-dire que la priorité 1 a la priorité la plus élevée). Les règles sont évaluées selon leur ordre de priorité. La règle correspondante ayant la priorité la plus élevée sera appliquée.

**Exemple :**

<table><thead><tr><th width="137">Règle</th><th width="110">Priorité</th><th width="268">Condition</th><th>Groupe renvoyé</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Si le montant total est de **1500**, les règles évaluées seront :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (correspond)
* **Règle 3** : Total Amount <= 3000 (correspond)
* **Règle 4** : Total Amount <= 4000 (correspond)
* **Règle 5** : Total Amount <= 5000 (correspond)

Étant donné que la priorité est appliquée dans l'ordre **5, 4, 3, 2, 1**, la règle correspondante ayant la priorité la plus élevée sera la **Règle 5** (**GROUP_5**). L'arbre de décision renverra **GROUP_5**, car la **Règle 5** a la priorité la plus élevée (priorité 1).
