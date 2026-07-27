# Collect-(sum)-Policy

Diese Policy sammelt alle zutreffenden Regeln und summiert die Ergebnisse. Sie funktioniert nur für **Return Type Value**.

**Beispiel:**

| Regel | Bedingung            | Rückgabewert |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Für den Eingabewert **Total Amount = 2500** würde die Auswertung der Regeln wie folgt aussehen:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft nicht zu)
* **Regel 3**: Total Amount <= 3000 (trifft zu, Rückgabewert = 3)
* **Regel 4**: Total Amount <= 4000 (trifft zu, Rückgabewert = 4)
* **Regel 5**: Total Amount <= 5000 (trifft zu, Rückgabewert = 5)

Da die **Collect-(sum)**-Policy angewendet wird, summieren wir die **Rückgabewerte** der zutreffenden Regeln, also **3, 4, 5**.

**Die Summe dieser Werte** ergibt:

* 5 + 4 + 3 = **12**

Das vom Entscheidungsbaum zurückgegebene Ergebnis wäre somit **12**, also die Summe aller zutreffenden Rückgabewerte.
