# Irgendeine

Mehrere Regeln können wahr sein, aber das Ergebnis dieser Regeln muss identisch sein.

**Beispiel:**

| Regel | Bedingung            | Rückgabegruppe |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Wenn der Gesamtbetrag **2500** ist, werden die Regeln wie folgt ausgewertet:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft nicht zu)
* **Regel 3**: Total Amount <= 3000 (trifft zu)
* **Regel 4**: Total Amount <= 4000 (trifft zu)
* **Regel 5**: Total Amount <= 5000 (trifft zu)

Damit **Irgendeine** angewendet wird, müssen alle zutreffenden Regeln dieselbe **Group** zurückgeben. Da die Gruppen über die verschiedenen Regeln hinweg nicht übereinstimmen, wäre das Ergebnis **false**.
