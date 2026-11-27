# Caso 8a, 9a: Quantidade fora da tolerância (Aprovado), Preço unitário dentro da tolerância

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade da fatura está fora da tolerância aceite, mas foi aprovada; o preço unitário permanece dentro da tolerância.

## Ação:

O sistema aceita a quantidade aprovada e o preço unitário da fatura e processa a transação.

## Exemplo:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $12.00 per unit
  * Total Amount: $1,800.00
* **Invoice Received:**
  * Quantity: 160 units — 6.67% above the PO value, outside the configured ±5% tolerance; approved.
  * Unit Price: $12.00 per unit (within tolerance)
  * Total Amount: $1,920.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Como a quantidade (160 unidades) excede o limite de tolerância, mas foi aprovada, e o preço unitário ($12.00) está dentro do intervalo aceite, o sistema irá:

1. **Accept the Approved Quantity:** o sistema reconhece a aprovação da quantidade apesar de estar fora da tolerância normal.
2. **Accept the Unit Price:** o preço de $12.00 por unidade está dentro da tolerância e é aceite tal como foi faturado.
3. **Process the Transaction:** o sistema calcula o total com a quantidade aprovada e o preço unitário:
   * **Total Amount = Quantity × Unit Price**
   * **Total Amount = 160 units × $12.00 per unit = $1,920.00**
4. **Finalize the Invoice:** o sistema processa a fatura com o total de $1,920.00, refletindo a quantidade aprovada e o preço unitário aceite.

Esta abordagem permite aceitar desvios aprovados na quantidade, mantendo o preço unitário dentro do intervalo esperado.
