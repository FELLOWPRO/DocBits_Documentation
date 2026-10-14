# Qualquer

Várias regras podem ser verdadeiras, mas o resultado dessas regras tem de ser o mesmo.

**Exemplo:**

| Regra | Condição             | Grupo Devolvido |
| ----- | -------------------- | --------------- |
| 1     | Total Amount <= 1000 | GROUP\_1        |
| 2     | Total Amount <= 2000 | GROUP\_2        |
| 3     | Total Amount <= 3000 | GROUP\_3        |
| 4     | Total Amount <= 4000 | GROUP\_4        |
| 5     | Total Amount <= 5000 | GROUP\_5        |

Se o montante total for **2500**, as regras avaliadas serão:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (não corresponde)
* **Regra 3**: Total Amount <= 3000 (corresponde)
* **Regra 4**: Total Amount <= 4000 (corresponde)
* **Regra 5**: Total Amount <= 5000 (corresponde)

Para que a política **Qualquer** se aplique, todas as regras correspondentes têm de devolver o mesmo **Return Group**. Uma vez que os grupos não coincidem entre as diferentes regras, o resultado seria **falso**.
