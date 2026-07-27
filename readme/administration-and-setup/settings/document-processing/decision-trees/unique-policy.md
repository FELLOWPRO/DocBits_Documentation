# Einzigartig

Stellt sicher, dass nur eine einzige Regel zutrifft. Wenn mehrere Regeln zutreffen, gibt der Entscheidungsbaum „false" zurück.

**Beispiel:**

| Regel | Bedingung            | Rückgabegruppe |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Wenn der Gesamtbetrag **1500** ist, werden die Regeln wie folgt ausgewertet:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft zu)
* **Regel 3**: Total Amount <= 5000 (trifft zu)
* **Regel 4**: Total Amount <= 4000 (trifft zu)
* **Regel 5**: Total Amount <= 3000 (trifft zu)

Da mehrere Regeln zutreffen (**Regel 2**, **Regel 3**, **Regel 4**, **Regel 5**), gibt der Entscheidungsbaum **false** zurück, weil die Policy **Einzigartig** sicherstellt, dass nur eine einzige Regel zutreffen darf.
