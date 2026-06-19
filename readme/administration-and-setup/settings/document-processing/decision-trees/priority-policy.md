# Priority-Policy

Mit dieser Option können Sie für jede Regel Prioritäten festlegen. Je niedriger die gewählte Zahl, desto höher die Priorität (d. h. Priorität 1 hat die höchste Priorität). Die Regeln werden anhand ihrer Prioritätsreihenfolge ausgewertet. Die zutreffende Regel mit der höchsten Priorität wird angewendet.

**Beispiel:**

<table><thead><tr><th width="137">Regel</th><th width="110">Priorität</th><th width="268">Bedingung</th><th>Rückgabegruppe</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Wenn der Gesamtbetrag **1500** ist, werden die Regeln wie folgt ausgewertet:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft zu)
* **Regel 3**: Total Amount <= 3000 (trifft zu)
* **Regel 4**: Total Amount <= 4000 (trifft zu)
* **Regel 5**: Total Amount <= 5000 (trifft zu)

Da die Priorität in der Reihenfolge **5, 4, 3, 2, 1** angewendet wird, ist die zutreffende Regel mit der höchsten Priorität **Regel 5** (**GROUP_5**). Der Entscheidungsbaum gibt **GROUP_5** zurück, weil **Regel 5** die höchste Priorität hat (Priorität 1).
