# Eerste & aangrenzend beleid (First & Adjacent Policy)

Kiest het resultaat van de regel die aangrenzend is aan de eerste regel die waar is.

**Voorbeeld:**

| Regel | Voorwaarde           | Geretourneerde groep |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Als het totaalbedrag **1500** is, worden de volgende regels geëvalueerd:

* **Regel 1**: Total Amount <= 1000 (komt niet overeen)
* **Regel 2**: Total Amount <= 2000 (komt overeen)

Omdat **Regel 2** de eerste regel is die overeenkomt, zou **First & Adjacent** het resultaat van **Regel 3** toepassen: **GROUP_3**.
