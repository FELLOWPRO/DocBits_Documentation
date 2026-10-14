# Primeiro

A primeira regra correspondente é aplicada e não são avaliadas mais regras.

**Exemplo:**

| Regra | Condição             | Grupo Devolvido |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Se o montante total for **1500**, as regras avaliadas serão:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (corresponde) → A árvore de decisão deixa de avaliar mais regras e aplica **GROUP_2**.
