# Política de Ordem das Regras (Rule Order)

Esta política aplica as regras pela ordem em que aparecem na árvore de decisão e devolve o resultado da regra que corresponde em primeiro lugar.

**Exemplo:**

| Regra | Condição             | Grupo Devolvido |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Dado que o valor de entrada é **Total Amount = 3500**, a avaliação das regras seria:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (não corresponde)
* **Regra 3**: Total Amount <= 3000 (corresponde)
* **Regra 4**: Total Amount <= 4000 (corresponde)
* **Regra 5**: Total Amount <= 5000 (corresponde)

Sob a política **Rule Order**, a árvore processará as regras pela ordem em que estão listadas. Assim, as regras correspondentes serão:

* **Regra 3**: GROUP_3
* **Regra 4**: GROUP_4
* **Regra 5**: GROUP_5

**Resultado**: **GROUP_3**, **GROUP_4**, **GROUP_5**
