# Caso 10b: Quantidade abaixo da tolerância e preço unitário fora da tolerância — rejeitados

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade e o preço unitário estão fora da tolerância e nenhum dos desvios foi aprovado.

## Ação:

O sistema rejeita os dados da fatura, ajusta os valores ao pedido de compra e gera as notas de débito ou crédito necessárias.

## Exemplo:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $30.00 per unit
  * Total Amount: $4,500.00
* **Invoice Received:**
  * Quantity: 140 units — 6.67% below the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $33.00 per unit — 10% above the PO value, outside the configured ±2% tolerance; rejected.
  * Total Amount: $4,620.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Como a quantidade (140 unidades) e o preço unitário ($33.00) estão fora dos limites de tolerância e nenhum dos desvios foi aprovado, o sistema irá:

1. **Rejeitar os dados da fatura:** o sistema não aceita a quantidade nem o preço unitário faturados devido ao desvio dos limites de tolerância.
2. **Ajustar a quantidade:** o sistema repõe a quantidade do pedido de compra original.
   * Adjusted Quantity = 150 units (from PO)
3. **Ajustar o preço unitário:** o sistema repõe o preço unitário do pedido de compra original.
   * Adjusted Unit Price = $30.00 per unit (from PO)
4. **Recalcular o valor total:** o sistema recalcula o total com a quantidade e o preço unitário ajustados:
   * **Corrected Total Amount = Adjusted Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 150 units × $30.00 per unit = $4,500.00**
5. **Gerar uma nota de débito:** como o total original da fatura é superior ao total corrigido, o sistema gera uma nota de débito para o valor cobrado em excesso.
   * **Debit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Debit Note Amount = $4,620.00 - $4,500.00 = $120.00**
6. **Processar a fatura:** o sistema processa a fatura com o total corrigido de $4,500.00 e emite uma nota de débito de $120.00 para compensar o valor cobrado em excesso.

Esta abordagem corrige a transação de acordo com as condições do pedido de compra, mantendo os registos financeiros.
