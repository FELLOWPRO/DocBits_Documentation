# Regelvolgordebeleid (Rule Order Policy)

Dit beleid past regels toe in de volgorde waarin ze in de beslissingsboom verschijnen en retourneert het resultaat van de regel die als eerste overeenkomt.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde groep |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Gegeven dat de invoerwaarde **Total Amount = 3500** is, zou de evaluatie van de regels als volgt zijn:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt niet overeen)
* **Regel 3**: Total Amount <= 3000 (komt overeen)
* **Regel 4**: Total Amount <= 4000 (komt overeen)
* **Regel 5**: Total Amount <= 5000 (komt overeen)

Onder **Regelvolgorde** verwerkt de boom de regels in de volgorde waarin ze worden vermeld. De overeenkomende regels zijn dus:

* **Regel 3**: GROUP_3
* **Regel 4**: GROUP_4
* **Regel 5**: GROUP_5

**Resultaat**: **GROUP_3**, **GROUP_4**, **GROUP_5**
