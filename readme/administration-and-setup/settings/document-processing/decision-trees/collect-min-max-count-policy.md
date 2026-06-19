# Política de Recolha (Collect — mín/máx/contagem)

Esta política recolhe todas as regras correspondentes e seleciona o **mínimo**, o **máximo** ou **conta** as ocorrências. Funciona apenas para **Return Type Value**.

**Exemplo:**

| Regra | Condição             | Valor Devolvido |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Se a opção **Collect (mín)** for selecionada, o resultado devolverá o **mínimo** dos **Return Values** das regras correspondentes.
   * Para o valor de entrada de **Total Amount = 3500**, a avaliação das regras seria:
     * **Regra 1**: Total Amount <= 1000 (não corresponde)
     * **Regra 2**: Total Amount <= 2000 (não corresponde)
     * **Regra 3**: Total Amount <= 3000 (corresponde, Return Value = 3)
     * **Regra 4**: Total Amount <= 4000 (corresponde, Return Value = 4)
     * **Regra 5**: Total Amount <= 5000 (corresponde, Return Value = 5)
   * As **regras correspondentes** são a Regra 3, a Regra 4 e a Regra 5, com **Return Values** de **3, 4 e 5**.
   * Uma vez que a política **Collect (mín)** é aplicada, o resultado será o **valor mínimo**, que é **3**.
   * **Resultado**: **3**
2. Se a opção **Collect (máx)** for selecionada, o resultado devolverá o **máximo** dos **Return Values** das regras correspondentes.
   * Para a mesma avaliação acima, o resultado será:
   * **Resultado**: **5**
3. Se a opção **Collect (contagem)** for selecionada, o resultado contará o **número de regras correspondentes**.
   * Para a mesma avaliação acima, o resultado será:
   * **Resultado**: **3** (uma vez que 3 regras corresponderam).
