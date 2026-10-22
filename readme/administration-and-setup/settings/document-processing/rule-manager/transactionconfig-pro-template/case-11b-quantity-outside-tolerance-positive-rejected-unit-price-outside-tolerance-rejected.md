# Caso 11b: Quantidade acima da tolerância e preço unitário fora da tolerância — rejeitados

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade excede o limite superior e foi rejeitada; o preço unitário também está fora da tolerância e foi rejeitado.

## Ação:

O sistema ajusta a quantidade e o preço unitário aos valores aprovados do pedido de compra, rejeita os excessos e processa a transação.

## Exemplo:

* **Pedido de compra (PO):**
  * Quantidade: 200 unidades
  * Preço unitário: $50.00 por unidade
  * Valor total: $10,000.00
* **Fatura recebida:**
  * Quantidade: 220 unidades (fora da tolerância de 10%, rejeitado)
  * Preço unitário: $55.00 por unidade (fora da tolerância de 10%, rejeitado)
  * Valor total: $12,100.00
* **Níveis de tolerância:**
  * Tolerância da quantidade: ±5%
  * Tolerância do preço unitário: ±2%

Como a quantidade (220 unidades) e o preço unitário ($55.00) excedem os limites de tolerância e nenhum dos desvios foi aprovado, o sistema irá:

1. **Rejeitar a quantidade excedente:** o sistema não aceita as 220 unidades faturadas e ajusta a quantidade ao pedido de compra original.
   * Quantidade ajustada = 200 unidades (do pedido de compra)
2. **Rejeitar o preço unitário da fatura:** o sistema não aceita o preço faturado de $55.00 e ajusta-o ao pedido de compra original.
   * Preço unitário ajustado = $50.00 por unidade (do pedido de compra)
3. **Recalcular o valor total:** o sistema calcula o total com a quantidade e o preço unitário ajustados:
   * **Valor total corrigido = Quantidade ajustada × Preço unitário ajustado**
   * **Valor total corrigido = 200 unidades × $50.00 por unidade = $10,000.00**
4. **Processar a fatura:** o sistema processa a fatura com o total corrigido de $10,000.00, rejeitando a quantidade excedente e o preço unitário superior.

Esta abordagem alinha a transação com as condições originais do pedido de compra, mantendo os controlos de preço e quantidade e rejeitando os desvios não aprovados.
