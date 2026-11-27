# Caso 11b: Quantidade acima da tolerância e preço unitário fora da tolerância — rejeitados

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade excede o limite superior e foi rejeitada; o preço unitário também está fora da tolerância e foi rejeitado.

## Ação:

O sistema ajusta a quantidade e o preço unitário aos valores aprovados do pedido de compra, rejeita os excessos e processa a transação.

## Exemplo:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $50.00 per unit
  * Total Amount: $10,000.00
* **Invoice Received:**
  * Quantity: 220 units — 10% above the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $55.00 per unit — 10% above the PO value, outside the configured ±2% tolerance; rejected.
  * Total Amount: $12,100.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Como a quantidade (220 unidades) e o preço unitário ($55.00) excedem os limites de tolerância e nenhum dos desvios foi aprovado, o sistema irá:

1. **Rejeitar a quantidade excedente:** o sistema não aceita as 220 unidades faturadas e ajusta a quantidade ao pedido de compra original.
   * Adjusted Quantity = 200 units (from PO)
2. **Rejeitar o preço unitário da fatura:** o sistema não aceita o preço faturado de $55.00 e ajusta-o ao pedido de compra original.
   * Adjusted Unit Price = $50.00 per unit (from PO)
3. **Recalcular o valor total:** o sistema calcula o total com a quantidade e o preço unitário ajustados:
   * **Corrected Total Amount = Adjusted Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 200 units × $50.00 per unit = $10,000.00**
4. **Processar a fatura:** o sistema processa a fatura com o total corrigido de $10,000.00, rejeitando a quantidade excedente e o preço unitário superior.

Esta abordagem alinha a transação com as condições originais do pedido de compra, mantendo os controlos de preço e quantidade e rejeitando os desvios não aprovados.
