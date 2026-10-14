# Erste & Angrenzende

Wählt das Ergebnis der Regel, die der ersten zutreffenden Regel benachbart ist.

**Beispiel:**

| Regel | Bedingung            | Rückgabegruppe |
| ----- | -------------------- | -------------- |
| 1     | Total Amount <= 1000 | GROUP\_1       |
| 2     | Total Amount <= 2000 | GROUP\_2       |
| 3     | Total Amount <= 3000 | GROUP\_3       |
| 4     | Total Amount <= 4000 | GROUP\_4       |
| 5     | Total Amount <= 5000 | GROUP\_5       |

Wenn der Gesamtbetrag **1500** ist, werden die Regeln wie folgt ausgewertet:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft zu)

Da **Regel 2** die erste zutreffende Regel ist, würde **Erste & Angrenzende** das Ergebnis von **Regel 3** anwenden: **GROUP\_3**.
