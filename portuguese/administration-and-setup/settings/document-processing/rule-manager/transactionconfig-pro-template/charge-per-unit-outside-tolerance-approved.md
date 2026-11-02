# Caso 14: Encargo de cabeçalho - Encargo por unidade fora da tolerância (Aprovado)

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

O encargo de cabeçalho por unidade está fora da tolerância, mas foi aprovado.

## Ação:

O sistema processa o encargo por unidade aprovado e aplica-o à transação.

## Exemplo:

* **Pedido de compra (PO):**
  * Encargo de cabeçalho por unidade: $2.50
  * Quantidade: 2,000 unidades
  * Valor total do encargo de cabeçalho: $5,000.00
* **Fatura recebida:**
  * Encargo de cabeçalho por unidade: $3.00 (fora da tolerância de 20%, aprovado)
  * Quantidade: 2,000 unidades
  * Valor total do encargo de cabeçalho: $6,000.00
* **Níveis de tolerância:**
  * Tolerância do encargo de cabeçalho por unidade: ±5%

Como o encargo de cabeçalho por unidade ($3.00) excede a tolerância de 5%, mas foi aprovado, o sistema irá:

1. **Aceitar o encargo de cabeçalho aprovado por unidade:** o sistema aceita o valor faturado de $3.00 apesar de exceder o limite de tolerância, porque foi aprovado.
2. **Processar o encargo de cabeçalho:** o sistema processa a fatura com o encargo por unidade aprovado e a quantidade:
   * **Valor total do encargo de cabeçalho = Quantidade × Encargo de cabeçalho aprovado por unidade**
   * **Valor total do encargo de cabeçalho = 2,000 unidades × $3.00 = $6,000.00**
3. **Finalizar a fatura:** o sistema processa a transação com os encargos aprovados, refletindo o total de $6,000.00.

Esta abordagem permite processar os desvios aprovados dos encargos de cabeçalho de acordo com a aprovação, mantendo os registos financeiros.
