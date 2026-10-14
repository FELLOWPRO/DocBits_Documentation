# Eerst

De eerste overeenkomende regel wordt toegepast en er worden geen verdere regels geëvalueerd.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde groep |
| ----- | -------------------- | -------------------- |
| 1     | Total Amount <= 1000 | GROUP\_1             |
| 2     | Total Amount <= 2000 | GROUP\_2             |
| 3     | Total Amount <= 5000 | GROUP\_5             |
| 4     | Total Amount <= 4000 | GROUP\_4             |
| 5     | Total Amount <= 3000 | GROUP\_3             |

Als het totaalbedrag **1500** is, worden de volgende regels geëvalueerd:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt overeen) → De beslissingsboom stopt met het evalueren van verdere regels en past **GROUP\_2** toe.
