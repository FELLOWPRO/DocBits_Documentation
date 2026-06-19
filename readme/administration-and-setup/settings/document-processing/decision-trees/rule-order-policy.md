# Criterio Rule Order (ordine delle regole)

Questo criterio applica le regole nell'ordine in cui appaiono nell'albero decisionale e restituisce il risultato della prima regola che corrisponde.

**Esempio:**

| Regola | Condizione           | Gruppo restituito |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Dato che il valore di input è **Total Amount = 3500**, la valutazione delle regole sarebbe:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (non corrisponde)
* **Regola 3**: Total Amount <= 3000 (corrisponde)
* **Regola 4**: Total Amount <= 4000 (corrisponde)
* **Regola 5**: Total Amount <= 5000 (corrisponde)

Con **Rule Order**, l'albero elaborerà le regole nell'ordine in cui sono elencate. Quindi, le regole corrispondenti saranno:

* **Regola 3**: GROUP_3
* **Regola 4**: GROUP_4
* **Regola 5**: GROUP_5

**Risultato**: **GROUP_3**, **GROUP_4**, **GROUP_5**
