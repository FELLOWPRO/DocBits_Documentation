# Criterio Collect (sum) (raccogli somma)

Questo criterio raccoglie tutte le regole corrispondenti e somma i risultati. Funziona solo per **Return Type Value**.

**Esempio:**

| Regola | Condizione           | Valore restituito |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Per il valore di input di **Total Amount = 3500**, la valutazione delle regole sarebbe:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (non corrisponde)
* **Regola 3**: Total Amount <= 3000 (corrisponde, Return Value = 3)
* **Regola 4**: Total Amount <= 4000 (corrisponde, Return Value = 4)
* **Regola 5**: Total Amount <= 5000 (corrisponde, Return Value = 5)

Poiché viene applicato il criterio **Collect (sum)**, sommiamo i **Return Values** delle regole corrispondenti, che sono **3, 4, 5**.

**La somma di questi valori** dà:

* 5 + 4 + 3 = **12**

Pertanto, il risultato restituito dall'albero decisionale sarebbe **12**, ovvero la somma di tutti i valori restituiti corrispondenti.
