# Regel Bestellung

Diese Policy wendet die Regeln in der Reihenfolge an, in der sie im Entscheidungsbaum erscheinen, und gibt das Ergebnis der zuerst zutreffenden Regel zurück.

**Beispiel:**

| Regel | Bedingung            | Rückgabegruppe |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Bei dem Eingabewert **Total Amount = 2500** würde die Auswertung der Regeln wie folgt aussehen:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft nicht zu)
* **Regel 3**: Total Amount <= 3000 (trifft zu)
* **Regel 4**: Total Amount <= 4000 (trifft zu)
* **Regel 5**: Total Amount <= 5000 (trifft zu)

Bei **Regel Bestellung** verarbeitet der Baum die Regeln in der Reihenfolge, in der sie aufgeführt sind. Die zutreffenden Regeln sind also:

* **Regel 3**: GROUP_3
* **Regel 4**: GROUP_4
* **Regel 5**: GROUP_5

**Ergebnis**: **GROUP_3**, **GROUP_4**, **GROUP_5**
