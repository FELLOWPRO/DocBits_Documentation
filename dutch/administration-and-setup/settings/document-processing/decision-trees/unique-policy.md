# Uniek

Zorgt ervoor dat slechts één enkele regel wordt gematcht. Als er meerdere regels worden gematcht, retourneert de beslissingsboom false.

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
* **Regel 2**: Total Amount <= 2000 (komt overeen)
* **Regel 3**: Total Amount <= 5000 (komt overeen)
* **Regel 4**: Total Amount <= 4000 (komt overeen)
* **Regel 5**: Total Amount <= 3000 (komt overeen)

Omdat er meerdere regels overeenkomen (**Regel 2**, **Regel 3**, **Regel 4**, **Regel 5**), retourneert de beslissingsboom **false**, omdat het **Unieke** beleid ervoor zorgt dat slechts één regel kan overeenkomen.
