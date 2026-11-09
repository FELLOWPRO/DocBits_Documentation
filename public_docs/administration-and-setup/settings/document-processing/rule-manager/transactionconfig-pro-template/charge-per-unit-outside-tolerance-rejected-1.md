# Encargo por unidade fora da tolerância (Rejeitado)

> **Nota sobre o exemplo:** O cenário seguinte é um mapeamento configurado a título de exemplo, não um modelo padrão cuja implantação tenha sido verificada. A saída real, os valores, os sinais e os tipos de documento dependem das regras e expressões `conflict_resolution` ativas, do mapeamento de exportação e das decisões de aprovação. Qualquer nota de débito ou de crédito descrita abaixo depende dessa configuração; o exemplo não garante emissão automática nem conformidade legal.

## Cenário:

O encargo por unidade está fora da tolerância e não foi aprovado.

## Ação:

O sistema ajusta o encargo por unidade ao pedido de compra ou aos valores aprovados e gera as notas de débito ou crédito necessárias.

## Exemplo:

* **Purchase Order (PO):**
  * Charge Per Unit: $6.00
  * Quantity: 800 unidades
  * Total Charge Amount: $4,800.00
* **Invoice Received:**
  * Charge Per Unit: $7.00 (variação 16.67%, fora da tolerância de ±5%, rejeitado)
  * Quantity: 800 unidades
  * Total Charge Amount: $5,600.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Como o encargo por unidade ($7.00) excede a tolerância de 5% e não foi aprovado, o sistema irá:

1. **Reject the Invoiced Charge Per Unit:** o sistema não aceita o valor de $7.00 porque o desvio excede o limite de tolerância.
2. **Adjust the Charge Per Unit:** o sistema ajusta o valor ao pedido de compra ou ao encargo por unidade aprovado:
   * Adjusted Charge Per Unit = $6.00 (do pedido de compra)
3. **Recalculate the Total Charge Amount:** o sistema recalcula o total com o encargo por unidade ajustado:
   * **Corrected Total Charge Amount = Quantity × Adjusted Charge Per Unit**
   * **Corrected Total Charge Amount = 800 units × $6.00 = $4,800.00**
4. **Generate a Debit Note:** como o total original da fatura é superior ao total corrigido, o sistema gera uma nota de débito para o valor cobrado em excesso:
   * **Valor da nota de débito = Total original da fatura - Valor total corrigido dos encargos**
   * **Debit Note Amount = $5,600.00 - $4,800.00 = $800.00**
5. **Process the Invoice:** o sistema processa a fatura com o total corrigido dos encargos de $4,800.00 e emite uma nota de débito de $800.00 para refletir o valor cobrado em excesso.

Esta abordagem mantém a transação alinhada com as condições do pedido de compra e rejeita os desvios não aprovados.
