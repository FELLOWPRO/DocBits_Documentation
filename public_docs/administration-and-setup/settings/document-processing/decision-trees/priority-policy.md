# Prioriteit

Met deze optie kunt u prioriteiten instellen voor elke regel. Hoe lager het geselecteerde getal, hoe hoger de prioriteit (d.w.z. prioriteit 1 heeft de hoogste prioriteit). Regels worden geëvalueerd op basis van hun prioriteitsvolgorde. De overeenkomende regel met de hoogste prioriteit wordt toegepast.

**Voorbeeld:**

<table><thead><tr><th width="137">Regel</th><th width="110">Prioriteit</th><th width="268">Voorwaarde</th><th>Geretourneerde groep</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Als het totaalbedrag **1500** is, worden de volgende regels geëvalueerd:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt overeen)
* **Regel 3**: Total Amount <= 3000 (komt overeen)
* **Regel 4**: Total Amount <= 4000 (komt overeen)
* **Regel 5**: Total Amount <= 5000 (komt overeen)

Aangezien de prioriteit wordt toegepast in de volgorde **5, 4, 3, 2, 1**, is de overeenkomende regel met de hoogste prioriteit **Regel 5** (**GROUP_5**). De beslissingsboom retourneert **GROUP_5** omdat **Regel 5** de hoogste prioriteit heeft (prioriteit 1).
