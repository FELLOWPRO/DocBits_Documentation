# Política Única (Unique)

Garante que apenas uma única regra é correspondida. Se forem correspondidas várias regras, a árvore de decisão devolverá falso.

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
* **Regra 2**: Total Amount <= 2000 (corresponde)
* **Regra 3**: Total Amount <= 5000 (corresponde)
* **Regra 4**: Total Amount <= 4000 (corresponde)
* **Regra 5**: Total Amount <= 3000 (corresponde)

Uma vez que são correspondidas várias regras (**Regra 2**, **Regra 3**, **Regra 4**, **Regra 5**), a árvore de decisão devolverá **falso**, porque a política **Única** garante que apenas uma regra pode corresponder.
