# Ordine della regola

Questo criterio applica le regole nell'ordine in cui appaiono nell'albero decisionale e restituisce il risultato della prima regola che corrisponde.

**Esempio:**

| Regola | Condizione           | Gruppo restituito |
| ------ | -------------------- | ----------------- |
| 1      | Total Amount <= 1000 | GROUP\_1          |
| 2      | Total Amount <= 2000 | GROUP\_2          |
| 3      | Total Amount <= 3000 | GROUP\_3          |
| 4      | Total Amount <= 4000 | GROUP\_4          |
| 5      | Total Amount <= 5000 | GROUP\_5          |

Dato che il valore di input è **Total Amount = 2500**, la valutazione delle regole sarebbe:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (non corrisponde)
* **Regola 3**: Total Amount <= 3000 (corrisponde)
* **Regola 4**: Total Amount <= 4000 (corrisponde)
* **Regola 5**: Total Amount <= 5000 (corrisponde)

Con **Ordine della regola**, l'albero elaborerà le regole nell'ordine in cui sono elencate. Quindi, le regole corrispondenti saranno:

* **Regola 3**: GROUP\_3
* **Regola 4**: GROUP\_4
* **Regola 5**: GROUP\_5

**Risultato**: **GROUP\_3**, **GROUP\_4**, **GROUP\_5**
