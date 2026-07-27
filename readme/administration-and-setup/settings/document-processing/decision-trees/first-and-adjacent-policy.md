# Primo e adiacente

Sceglie il risultato della regola adiacente alla prima regola che è vera.

**Esempio:**

| Regola | Condizione           | Gruppo restituito |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Se l'importo totale è **1500**, le regole valutate saranno:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (corrisponde)

Poiché la **Regola 2** è la prima regola che corrisponde, **Primo e adiacente** applicherebbe il risultato della **Regola 3**: **GROUP_3**.
