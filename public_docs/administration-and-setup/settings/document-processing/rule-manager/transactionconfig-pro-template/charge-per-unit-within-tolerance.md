# Encargo por unidade dentro da tolerância

O cenário seguinte é um mapeamento configurado a título de exemplo, não um modelo padrão cuja implantação tenha sido verificada. A saída real, os valores, os sinais e os tipos de documento dependem das regras e expressões `conflict_resolution` ativas, do mapeamento de exportação e das decisões de aprovação. Qualquer nota de débito ou de crédito descrita abaixo depende dessa configuração; o exemplo não garante emissão automática nem conformidade legal.

## Cenário:

O Charge Per Unit da fatura está dentro do intervalo de tolerância aceitável em comparação com o pedido de compra.

## Ação:

O sistema aceita o Charge Per Unit faturado e processa a transação sem ajustes.

## Exemplo:

* **Purchase Order (PO):**
  * Charge Per Unit: $5.00
  * Quantity: 500 units
  * Total Charge Amount: $2,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.10 — 2% above the PO value, within the configured ±3% tolerance.
  * Quantity: 500 units
  * Total Charge Amount: $2,550.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±3%

Como o Charge Per Unit ($5.10) está dentro do intervalo de tolerância aceitável de 3% em comparação com o pedido de compra, o sistema irá:

1. **Accept the Charge Per Unit:** o sistema aceita o Charge Per Unit faturado de $5.10 por estar dentro do limite de tolerância definido.
2. **Process the Transaction:** o sistema processa a fatura com o Total Charge Amount calculado a partir do Charge Per Unit faturado e da Quantity:
   * **Total Charge Amount = Quantity × Charge Per Unit**
   * **Total Charge Amount = 500 units × $5.10 = $2,550.00**
3. **Finalize the Invoice:** o sistema processa a transação sem ajustes e aceita a fatura tal como foi apresentada.

Esta abordagem permite aceitar pequenas diferenças nos encargos dentro da tolerância, sem rejeições ou atrasos desnecessários.
