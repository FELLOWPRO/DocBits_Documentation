# Caso 8b, 9b: Quantidade fora da tolerância (Aprovado), Preço unitário fora da tolerância (Aprovado)

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade e o preço unitário estão fora da tolerância, mas ambos foram aprovados.

## Ação:

O sistema processa a transação com a quantidade e o preço unitário da fatura, aplicando os ajustes ou encargos de linha necessários.

## Exemplo:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $25.00 per unit
  * Total Amount: $5,000.00
* **Invoice Received:**
  * Quantity: 220 units — 10% above the PO value, outside the configured ±5% tolerance; approved.
  * Unit Price: $27.00 per unit — 8% above the PO value, outside the configured ±2% tolerance; approved.
  * Total Amount: $5,940.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Como a quantidade (220 unidades) e o preço unitário ($27.00) estão fora da tolerância, mas foram aprovados, o sistema irá:

1. **Aceitar a quantidade aprovada:** o sistema aceita as 220 unidades faturadas, apesar de estarem fora da tolerância, porque foram aprovadas.
2. **Aceitar o preço unitário aprovado:** o sistema aceita o preço faturado de $27.00 por unidade, apesar de estar fora da tolerância, porque foi aprovado.
3. **Calcular o valor total:** o sistema calcula o total com os valores aprovados da fatura:
   * **Total Amount = Quantity × Unit Price**
   * **Total Amount = 220 units × $27.00 per unit = $5,940.00**
4. **Aplicar os ajustes ou encargos de linha necessários:** quando aplicável, o sistema pode acrescentar encargos ou ajustes de acordo com as políticas da organização para os desvios aprovados.
5. **Processar a fatura:** o sistema processa a fatura com a quantidade e o preço unitário aprovados e finaliza a transação no total de $5,940.00.

Esta abordagem processa a transação de acordo com os desvios aprovados, mantendo os registos financeiros.
