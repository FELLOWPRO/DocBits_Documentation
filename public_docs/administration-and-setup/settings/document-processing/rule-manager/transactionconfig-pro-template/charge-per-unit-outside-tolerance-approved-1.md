# Caso 14: Linha de encargo - Encargo por unidade fora da tolerância (Aprovado)

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

O encargo por unidade está fora da tolerância, mas foi aprovado.

## Ação:

O sistema aceita o encargo por unidade aprovado e processa a transação.

## Exemplo:

* **Purchase Order (PO):**
  * Charge Per Unit: $4.50
  * Quantity: 1,000 units
  * Total Charge Amount: $4,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.00 — 11.11% above the PO value, outside the configured ±5% tolerance; approved.
  * Quantity: 1,000 units
  * Total Charge Amount: $5,000.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Como o encargo por unidade ($5.00) está fora da tolerância de 5%, mas foi aprovado, o sistema irá:

1. **Aceitar o encargo aprovado por unidade:** o sistema aceita o valor faturado de $5.00, apesar de exceder a tolerância, porque foi aprovado.
2. **Processar a transação:** o sistema processa a fatura com o encargo por unidade aprovado e a quantidade:
   * **Total Charge Amount = Quantity × Approved Charge Per Unit**
   * **Total Charge Amount = 1,000 units × $5.00 = $5,000.00**
3. **Finalizar a fatura:** o sistema processa a transação com os encargos aprovados, refletindo o total de $5,000.00.

Esta abordagem permite processar os desvios aprovados dos encargos, mantendo os registos financeiros.
