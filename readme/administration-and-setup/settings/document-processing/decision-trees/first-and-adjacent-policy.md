# First-&-Adjacent-Policy

Wählt das Ergebnis der Regel, die der ersten zutreffenden Regel benachbart ist.

**Beispiel:**

| Regel | Bedingung            | Rückgabegruppe |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Wenn der Gesamtbetrag **1500** ist, werden die Regeln wie folgt ausgewertet:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft zu)

Da **Regel 2** die erste zutreffende Regel ist, würde **First & Adjacent** das Ergebnis von **Regel 3** anwenden: **GROUP_3**.
