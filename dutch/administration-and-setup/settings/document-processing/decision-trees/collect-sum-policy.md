# Verzamelen (Sommen)

Dit beleid verzamelt alle overeenkomende regels en telt de resultaten op. Het werkt alleen voor **Return Type Value**.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde waarde |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Voor de invoerwaarde **Total Amount = 2500** zou de evaluatie van de regels als volgt zijn:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt niet overeen)
* **Regel 3**: Total Amount <= 3000 (komt overeen, Return Value = 3)
* **Regel 4**: Total Amount <= 4000 (komt overeen, Return Value = 4)
* **Regel 5**: Total Amount <= 5000 (komt overeen, Return Value = 5)

Omdat het **Verzamel (som)**-beleid wordt toegepast, tellen we de **Return Values** van de overeenkomende regels op, namelijk **3, 4, 5**.

**Het optellen van deze waarden** geeft:

* 5 + 4 + 3 = **12**

Het resultaat dat door de beslissingsboom wordt geretourneerd is dus **12**, wat de som is van alle overeenkomende retourwaarden.
