# Política de Recolha (Collect — soma)

Esta política recolhe todas as regras correspondentes e soma os resultados. Funciona apenas para **Return Type Value**.

**Exemplo:**

| Regra | Condição             | Valor Devolvido |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Para o valor de entrada de **Total Amount = 2500**, a avaliação das regras seria:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (não corresponde)
* **Regra 3**: Total Amount <= 3000 (corresponde, Return Value = 3)
* **Regra 4**: Total Amount <= 4000 (corresponde, Return Value = 4)
* **Regra 5**: Total Amount <= 5000 (corresponde, Return Value = 5)

Uma vez que a política **Collect (soma)** é aplicada, somamos os **Return Values** das regras correspondentes, que são **3, 4, 5**.

**Somando estes valores** obtém-se:

* 5 + 4 + 3 = **12**

Assim, o resultado devolvido pela árvore de decisão seria **12**, que é a soma de todos os valores devolvidos correspondentes.
