# Elk

Meerdere regels kunnen waar zijn, maar het resultaat van die regels moet hetzelfde zijn.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde groep |
| ----- | -------------------- | -------------------- |
| 1     | Total Amount <= 1000 | GROUP\_1             |
| 2     | Total Amount <= 2000 | GROUP\_2             |
| 3     | Total Amount <= 3000 | GROUP\_3             |
| 4     | Total Amount <= 4000 | GROUP\_4             |
| 5     | Total Amount <= 5000 | GROUP\_5             |

Als het totaalbedrag **2500** is, worden de volgende regels geëvalueerd:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt niet overeen)
* **Regel 3**: Total Amount <= 3000 (komt overeen)
* **Regel 4**: Total Amount <= 4000 (komt overeen)
* **Regel 5**: Total Amount <= 5000 (komt overeen)

Om **Elk** toe te passen, moeten alle overeenkomende regels dezelfde **Return Group** retourneren. Omdat de groepen niet overeenkomen tussen de verschillende regels, is het resultaat **false**.
