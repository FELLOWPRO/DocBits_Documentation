# Regelvolgorde

Dit beleid past regels toe in de volgorde waarin ze in de beslissingsboom verschijnen en retourneert het resultaat van de regel die als eerste overeenkomt.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde groep |
| ----- | -------------------- | -------------------- |
| 1     | Total Amount <= 1000 | GROUP\_1             |
| 2     | Total Amount <= 2000 | GROUP\_2             |
| 3     | Total Amount <= 3000 | GROUP\_3             |
| 4     | Total Amount <= 4000 | GROUP\_4             |
| 5     | Total Amount <= 5000 | GROUP\_5             |

Gegeven dat de invoerwaarde **Total Amount = 2500** is, zou de evaluatie van de regels als volgt zijn:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt niet overeen)
* **Regel 3**: Total Amount <= 3000 (komt overeen)
* **Regel 4**: Total Amount <= 4000 (komt overeen)
* **Regel 5**: Total Amount <= 5000 (komt overeen)

Onder **Regelvolgorde** verwerkt de boom de regels in de volgorde waarin ze worden vermeld. De overeenkomende regels zijn dus:

* **Regel 3**: GROUP\_3
* **Regel 4**: GROUP\_4
* **Regel 5**: GROUP\_5

**Resultaat**: **GROUP\_3**, **GROUP\_4**, **GROUP\_5**
