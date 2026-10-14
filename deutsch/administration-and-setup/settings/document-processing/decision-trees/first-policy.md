# Erste

Die erste zutreffende Regel wird angewendet, und es werden keine weiteren Regeln ausgewertet.

**Beispiel:**

| Regel | Bedingung            | Rückgabegruppe |
| ----- | -------------------- | -------------- |
| 1     | Total Amount <= 1000 | GROUP\_1       |
| 2     | Total Amount <= 2000 | GROUP\_2       |
| 3     | Total Amount <= 5000 | GROUP\_5       |
| 4     | Total Amount <= 4000 | GROUP\_4       |
| 5     | Total Amount <= 3000 | GROUP\_3       |

Wenn der Gesamtbetrag **1500** ist, werden die Regeln wie folgt ausgewertet:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft zu) → Der Entscheidungsbaum beendet die Auswertung weiterer Regeln und wendet **GROUP\_2** an.
