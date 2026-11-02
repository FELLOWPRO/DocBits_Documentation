# Linhas de imposto

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

Trata as divergências nos valores dos impostos entre a fatura e o pedido de compra.

## Ação:

O sistema ajusta as linhas de imposto às taxas e aos valores aprovados, de acordo com as regras fiscais aplicáveis.

## Exemplo:

* **Pedido de compra (PO):**
  * Subtotal: $10,000.00
  * Taxa de imposto: 8%
  * Valor esperado do imposto: $800.00
  * Valor total com impostos: $10,800.00
* **Fatura recebida:**
  * Subtotal: $10,000.00
  * Taxa de imposto: 10% (divergência)
  * Valor do imposto faturado: $1,000.00
  * Valor total com impostos: $11,000.00

Como a taxa de imposto da fatura (10%) difere da taxa esperada (8%) e não foi aprovada, o sistema irá:

1. **Rejeitar a taxa de imposto faturada:** o sistema não aceita a taxa de 10% por não corresponder à taxa aprovada no pedido de compra.
2. **Ajustar a taxa de imposto:** o sistema ajusta a taxa à que foi aprovada no pedido de compra.
   * Taxa de imposto ajustada = 8% (do pedido de compra)
3. **Recalcular o valor do imposto:** o sistema recalcula o imposto com a taxa ajustada:
   * **Valor corrigido do imposto = Subtotal × Taxa de imposto ajustada**
   * **Valor corrigido do imposto = $10,000.00 × 8% = $800.00**
4. **Recalcular o valor total:** o sistema recalcula o total com impostos:
   * **Valor total corrigido com impostos = Subtotal + Valor corrigido do imposto**
   * **Valor total corrigido com impostos = $10,000.00 + $800.00 = $10,800.00**
5. **Gerar uma nota de crédito:** o sistema gera uma nota de crédito para corrigir o imposto cobrado em excesso:
   * **Valor da nota de crédito = Valor original do imposto da fatura - Valor corrigido do imposto**
   * **Valor da nota de crédito = $1,000.00 - $800.00 = $200.00**
6. **Processar a fatura:** o sistema processa a fatura com o imposto corrigido de $800.00 e o total de $10,800.00, emitindo uma nota de crédito para a diferença de $200.00.

Esta abordagem alinha o imposto da fatura com o pedido de compra e as regras fiscais aplicáveis, evitando pagamentos em excesso e mantendo os registos financeiros.
