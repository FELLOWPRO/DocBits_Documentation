# Política de Prioridade (Priority)

Escolher esta opção permite-lhe definir prioridades para cada regra. Quanto menor o número selecionado, maior a prioridade (ou seja, a prioridade 1 tem a prioridade mais alta). As regras são avaliadas com base na sua ordem de prioridade. A regra correspondente de prioridade mais alta será aplicada.

**Exemplo:**

<table><thead><tr><th width="137">Regra</th><th width="110">Prioridade</th><th width="268">Condição</th><th>Grupo Devolvido</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Se o montante total for **1500**, as regras avaliadas serão:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (corresponde)
* **Regra 3**: Total Amount <= 3000 (corresponde)
* **Regra 4**: Total Amount <= 4000 (corresponde)
* **Regra 5**: Total Amount <= 5000 (corresponde)

Uma vez que a prioridade é aplicada pela ordem **5, 4, 3, 2, 1**, a regra correspondente de prioridade mais alta será a **Regra 5** (**GROUP_5**). A árvore de decisão devolverá **GROUP_5** porque a **Regra 5** tem a prioridade mais alta (prioridade 1).
