# Primeiro e Adjacente

Escolhe o resultado da regra que é adjacente à primeira regra que é verdadeira.

**Exemplo:**

| Regra | Condição             | Grupo Devolvido |
| ----- | -------------------- | --------------- |
| 1     | Total Amount <= 1000 | GROUP\_1        |
| 2     | Total Amount <= 2000 | GROUP\_2        |
| 3     | Total Amount <= 3000 | GROUP\_3        |
| 4     | Total Amount <= 4000 | GROUP\_4        |
| 5     | Total Amount <= 5000 | GROUP\_5        |

Se o montante total for **1500**, as regras avaliadas serão:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (corresponde)

Uma vez que a **Regra 2** é a primeira regra que corresponde, a política **Primeiro e Adjacente** aplicaria o resultado da **Regra 3**: **GROUP\_3**.
