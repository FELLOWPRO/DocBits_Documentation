# Caso 7: Quantidade dentro da tolerância, preço unitário fora da tolerância (positivo rejeitado)

O cenário seguinte é um mapeamento configurado ilustrativo e não um modelo predefinido implementado e verificado. A saída real, os montantes, os sinais e os tipos de documento dependem das regras e expressões `conflict_resolution` ativas, do mapeamento de exportação e das decisões de aprovação. Qualquer nota de débito ou de crédito descrita abaixo depende dessa configuração; o exemplo não garante a emissão automática nem a conformidade legal.

## Cenário:

A quantidade está dentro da tolerância, mas o preço unitário excede o intervalo aceitável (tolerância positiva) e não é aprovado.

## Ação:

O sistema rejeita o preço unitário da fatura, ajusta-o para corresponder ao pedido de compra e pode gerar uma nota de débito para refletir o montante cobrado em excesso.

## Exemplo:

* **Purchase Order (PO):**
  * Quantity: 200 unidades
  * Unit Price: $15.00 por unidade
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 198 unidades — 1% abaixo do valor do PO, dentro da tolerância configurada de ±2%.
  * Unit Price: $17.00 por unidade — 13.33% acima do valor do PO, fora da tolerância configurada de ±1%; rejeitado.
  * Total Amount: $3,366.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Unit Price Tolerance: ±1%

Uma vez que a quantidade (198 unidades) está dentro do intervalo de tolerância aceitável, mas o preço unitário ($17.00) excede a tolerância aceitável e não foi aprovado, o sistema irá:

1. **Rejeitar o preço unitário da fatura:** o sistema não aceita o preço unitário faturado de $17.00.
2. **Ajustar o preço unitário:** o sistema ajusta o preço unitário para corresponder ao preço unitário do pedido de compra original.
   * Preço unitário ajustado = $15.00 (do PO)
3. **Calcular o montante total corrigido:** com o preço unitário ajustado, o sistema recalcula o montante total.
   * **Corrected Total Amount = Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 198 units × $15.00 per unit = $2,970.00**
4. **Gerar uma nota de débito:** o sistema gera uma nota de débito para refletir a diferença resultante do valor cobrado em excesso.
   * **Debit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Debit Note Amount = $3,366.00 - $2,970.00 = $396.00**
   * Esta nota de débito representa o montante cobrado em excesso pelo fornecedor.
5. **Processar a fatura:** o sistema processa a fatura com o montante total corrigido de $2,970.00 e emite uma nota de débito de $396.00 para compensar o valor cobrado em excesso.

Esta abordagem garante que qualquer cobrança em excesso é corrigida, alinhando a transação com as condições do pedido de compra e protegendo os interesses financeiros da empresa.
