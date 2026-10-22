# Caso 7: Quantidade dentro da tolerância; preço unitário acima da tolerância rejeitado

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade está dentro da tolerância, mas o preço unitário está acima do limite superior e o desvio não foi aprovado.

## Ação:

O sistema rejeita o preço unitário da fatura, ajusta-o ao pedido de compra e pode gerar uma nota de débito para refletir o valor cobrado em excesso.

## Exemplo:

* **Pedido de compra (PO):**
  * Quantidade: 200 unidades
  * Preço unitário: $15.00 por unidade
  * Valor total: $3,000.00
* **Fatura recebida:**
  * Quantidade: 198 unidades (dentro da tolerância de 1%)
  * Preço unitário: $17.00 por unidade (acima da tolerância superior de 13.33%)
  * Valor total: $3,366.00
* **Níveis de tolerância:**
  * Tolerância da quantidade: ±2%
  * Tolerância do preço unitário: ±1%

Como a quantidade (198 unidades) está dentro da tolerância, mas o preço unitário ($17.00) excede o limite superior e não foi aprovado, o sistema irá:

1. **Rejeitar o preço unitário da fatura:** o sistema não aceita o preço faturado de $17.00.
2. **Ajustar o preço unitário:** o sistema repõe o preço unitário do pedido de compra original.
   * Preço unitário ajustado = $15.00 (do pedido de compra)
3. **Calcular o total corrigido:** o sistema recalcula o total com o preço unitário ajustado.
   * **Valor total corrigido = Quantidade × Preço unitário ajustado**
   * **Valor total corrigido = 198 unidades × $15.00 por unidade = $2,970.00**
4. **Gerar uma nota de débito:** o sistema gera uma nota de débito para a diferença cobrada em excesso.
   * **Valor da nota de débito = Total original da fatura - Valor total corrigido**
   * **Valor da nota de débito = $3,366.00 - $2,970.00 = $396.00**
   * A nota de débito representa o valor cobrado em excesso pelo fornecedor.
5. **Processar a fatura:** o sistema processa a fatura com o total corrigido de $2,970.00 e emite uma nota de débito de $396.00 para compensar o valor cobrado em excesso.

Esta abordagem corrige os valores cobrados em excesso e alinha a transação com as condições do pedido de compra.
