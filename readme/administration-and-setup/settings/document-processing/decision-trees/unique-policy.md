# Unico

Garantisce che venga soddisfatta una sola regola. Se vengono soddisfatte più regole, l'albero decisionale restituirà false.

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
* **Regola 2**: Total Amount <= 2000 (corrisponde)
* **Regola 3**: Total Amount <= 5000 (corrisponde)
* **Regola 4**: Total Amount <= 4000 (corrisponde)
* **Regola 5**: Total Amount <= 3000 (corrisponde)

Poiché vengono soddisfatte più regole (**Regola 2**, **Regola 3**, **Regola 4**, **Regola 5**), l'albero decisionale restituirà **false** perché il criterio **Unico** garantisce che possa corrispondere una sola regola.
