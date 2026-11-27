# Caso 11a: Quantidade acima da tolerância rejeitada; preço unitário dentro da tolerância

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade da fatura excede o limite superior e foi rejeitada, mas o preço unitário está dentro da tolerância.

## Ação:

O sistema ajusta a quantidade ao valor aprovado, mantém o preço unitário e processa a transação. A quantidade excedente é rejeitada e não é faturada.

## Exemplo:

* **Purchase Order (PO):**
  * Quantity: 100 units
  * Unit Price: $8.00 per unit
  * Total Amount: $800.00
* **Invoice Received:**
  * Quantity: 110 units — 10% above the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $8.00 per unit (within tolerance)
  * Total Amount: $880.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Como a quantidade (110 unidades) excede o limite superior de tolerância, com um desvio de 10% não aprovado, mas o preço unitário ($8.00) está dentro da tolerância, o sistema irá:

1. **Reject the Excess Quantity:** o sistema rejeita a quantidade que excede a tolerância aprovada.
2. **Adjust the Quantity:** o sistema ajusta a quantidade ao valor aprovado no pedido de compra.
   * Approved Quantity = 100 units (from PO)
3. **Maintain the Unit Price:** o preço de $8.00 por unidade está dentro da tolerância e mantém-se.
4. **Recalculate the Total Amount:** o sistema calcula o total com a quantidade aprovada e o preço unitário aceite:
   * **Total Amount = Approved Quantity × Unit Price**
   * **Total Amount = 100 units × $8.00 per unit = $800.00**
5. **Process the Invoice:** o sistema processa a fatura com o total ajustado de $800.00, refletindo apenas a quantidade e o preço aprovados. As 10 unidades excedentes são rejeitadas e não são faturadas.

Esta abordagem alinha o valor faturado com as condições do pedido de compra, mesmo quando o fornecedor tenta faturar uma quantidade superior.
