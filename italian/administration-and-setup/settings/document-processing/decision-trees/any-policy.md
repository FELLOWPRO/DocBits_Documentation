# Qualsiasi

Più regole possono essere vere, ma il risultato di tali regole deve essere lo stesso.

**Esempio:**

| Regola | Condizione           | Gruppo restituito |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Se l'importo totale è **2500**, le regole valutate saranno:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (non corrisponde)
* **Regola 3**: Total Amount <= 3000 (corrisponde)
* **Regola 4**: Total Amount <= 4000 (corrisponde)
* **Regola 5**: Total Amount <= 5000 (corrisponde)

Affinché **Qualsiasi** si applichi, tutte le regole corrispondenti devono restituire lo stesso **Return Group**. Poiché i gruppi non corrispondono tra le diverse regole, il risultato sarebbe **false**.
