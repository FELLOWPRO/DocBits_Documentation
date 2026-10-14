# Ordem das Regras

Esta política aplica as regras pela ordem em que aparecem na árvore de decisão e devolve o resultado da regra que corresponde em primeiro lugar.

**Exemplo:**

| Regra | Condição             | Grupo Devolvido |
| ----- | -------------------- | --------------- |
| 1     | Total Amount <= 1000 | GROUP\_1        |
| 2     | Total Amount <= 2000 | GROUP\_2        |
| 3     | Total Amount <= 3000 | GROUP\_3        |
| 4     | Total Amount <= 4000 | GROUP\_4        |
| 5     | Total Amount <= 5000 | GROUP\_5        |

Dado que o valor de entrada é **Total Amount = 2500**, a avaliação das regras seria:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (não corresponde)
* **Regra 3**: Total Amount <= 3000 (corresponde)
* **Regra 4**: Total Amount <= 4000 (corresponde)
* **Regra 5**: Total Amount <= 5000 (corresponde)

Sob a política **Ordem das Regras**, a árvore processará as regras pela ordem em que estão listadas. Assim, as regras correspondentes serão:

* **Regra 3**: GROUP\_3
* **Regra 4**: GROUP\_4
* **Regra 5**: GROUP\_5

**Resultado**: **GROUP\_3**, **GROUP\_4**, **GROUP\_5**
