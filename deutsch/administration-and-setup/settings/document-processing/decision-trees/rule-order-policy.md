# Regel Bestellung

Diese Policy wendet die Regeln in der Reihenfolge an, in der sie im Entscheidungsbaum erscheinen, und gibt das Ergebnis der zuerst zutreffenden Regel zurück.

**Beispiel:**

| Regel | Bedingung            | Rückgabegruppe |
| ----- | -------------------- | -------------- |
| 1     | Total Amount <= 1000 | GROUP\_1       |
| 2     | Total Amount <= 2000 | GROUP\_2       |
| 3     | Total Amount <= 3000 | GROUP\_3       |
| 4     | Total Amount <= 4000 | GROUP\_4       |
| 5     | Total Amount <= 5000 | GROUP\_5       |

Bei dem Eingabewert **Total Amount = 2500** würde die Auswertung der Regeln wie folgt aussehen:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft nicht zu)
* **Regel 3**: Total Amount <= 3000 (trifft zu)
* **Regel 4**: Total Amount <= 4000 (trifft zu)
* **Regel 5**: Total Amount <= 5000 (trifft zu)

Bei **Regel Bestellung** verarbeitet der Baum die Regeln in der Reihenfolge, in der sie aufgeführt sind. Die zutreffenden Regeln sind also:

* **Regel 3**: GROUP\_3
* **Regel 4**: GROUP\_4
* **Regel 5**: GROUP\_5

**Ergebnis**: **GROUP\_3**, **GROUP\_4**, **GROUP\_5**
