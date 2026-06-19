# Criterio Priority (priorità)

La scelta di questa opzione consente di impostare le priorità per ciascuna regola. Più basso è il numero selezionato, più alta è la priorità (ad es. la priorità 1 ha la priorità più elevata). Le regole vengono valutate in base al loro ordine di priorità. Verrà applicata la regola corrispondente con la priorità più alta.

**Esempio:**

<table><thead><tr><th width="137">Regola</th><th width="110">Priorità</th><th width="268">Condizione</th><th>Gruppo restituito</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Se l'importo totale è **1500**, le regole valutate saranno:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (corrisponde)
* **Regola 3**: Total Amount <= 3000 (corrisponde)
* **Regola 4**: Total Amount <= 4000 (corrisponde)
* **Regola 5**: Total Amount <= 5000 (corrisponde)

Poiché la priorità viene applicata nell'ordine **5, 4, 3, 2, 1**, la regola corrispondente con priorità più alta sarà la **Regola 5** (**GROUP_5**). L'albero decisionale restituirà **GROUP_5** perché la **Regola 5** ha la priorità più alta (priorità 1).
