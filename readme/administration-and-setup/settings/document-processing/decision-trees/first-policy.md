# Criterio First (prima)

Viene applicata la prima regola corrispondente e nessuna regola successiva viene valutata.

**Esempio:**

| Regola | Condizione           | Gruppo restituito |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Se l'importo totale è **1500**, le regole valutate saranno:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (corrisponde) → L'albero decisionale interrompe la valutazione delle ulteriori regole e applica **GROUP_2**.
