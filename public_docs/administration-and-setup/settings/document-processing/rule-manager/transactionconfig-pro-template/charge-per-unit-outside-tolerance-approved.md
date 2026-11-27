# Caso 14: Encargo de cabeçalho - Encargo por unidade fora da tolerância (Aprovado)

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

O encargo de cabeçalho por unidade está fora da tolerância, mas foi aprovado.

## Ação:

O sistema processa o encargo por unidade aprovado e aplica-o à transação.

## Exemplo:

* **Purchase Order (PO):**
  * Header Charge Per Unit: $2.50
  * Quantity: 2,000 units
  * Total Header Charge Amount: $5,000.00
* **Invoice Received:**
  * Header Charge Per Unit: $3.00 — 20% above the PO value, outside the configured ±5% tolerance; approved.
  * Quantity: 2,000 units
  * Total Header Charge Amount: $6,000.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±5%

Como o encargo de cabeçalho por unidade ($3.00) excede a tolerância de 5%, mas foi aprovado, o sistema irá:

1. **Aceitar o encargo de cabeçalho aprovado por unidade:** o sistema aceita o valor faturado de $3.00 apesar de exceder o limite de tolerância, porque foi aprovado.
2. **Processar o encargo de cabeçalho:** o sistema processa a fatura com o encargo por unidade aprovado e a quantidade:
   * **Total Header Charge Amount = Quantity × Approved Header Charge Per Unit**
   * **Total Header Charge Amount = 2,000 units × $3.00 = $6,000.00**
3. **Finalizar a fatura:** o sistema processa a transação com os encargos aprovados, refletindo o total de $6,000.00.

Esta abordagem permite processar os desvios aprovados dos encargos de cabeçalho de acordo com a aprovação, mantendo os registos financeiros.
