# Verzamelbeleid (min/max/aantal) (Collect (min/max/count) Policy)

Dit beleid verzamelt alle overeenkomende regels en selecteert ofwel het **minimum**, het **maximum**, of **telt** het aantal voorkomens. Het werkt alleen voor **Return Type Value**.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde waarde |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Als de optie **Collect (min)** is geselecteerd, retourneert het resultaat het **minimum** van de **Return Values** voor de overeenkomende regels.
   * Voor de invoerwaarde **Total Amount = 3500** zou de evaluatie van de regels als volgt zijn:
     * **Regel 1**: Total Amount <= 1000 (komt niet overeen)
     * **Regel 2**: Total Amount <= 2000 (komt niet overeen)
     * **Regel 3**: Total Amount <= 3000 (komt overeen, Return Value = 3)
     * **Regel 4**: Total Amount <= 4000 (komt overeen, Return Value = 4)
     * **Regel 5**: Total Amount <= 5000 (komt overeen, Return Value = 5)
   * De **overeenkomende regels** zijn Regel 3, Regel 4 en Regel 5, met **Return Values** van **3, 4 en 5**.
   * Omdat het **Collect (min)**-beleid wordt toegepast, is het resultaat de **minimale waarde**, namelijk **3**.
   * **Resultaat**: **3**
2. Als de optie **Collect (max)** is geselecteerd, retourneert het resultaat het **maximum** van de **Return Values** voor de overeenkomende regels.
   * Voor dezelfde evaluatie als hierboven is het resultaat:
   * **Resultaat**: **5**
3. Als de optie **Collect (count)** is geselecteerd, telt het resultaat het **aantal overeenkomende regels**.
   * Voor dezelfde evaluatie als hierboven is het resultaat:
   * **Resultaat**: **3** (aangezien 3 regels overeenkwamen).
