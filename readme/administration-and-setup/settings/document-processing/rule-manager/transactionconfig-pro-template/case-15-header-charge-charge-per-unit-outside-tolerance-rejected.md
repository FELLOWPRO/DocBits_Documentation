# Caso 15: Encargo de cabeçalho - Encargo por unidade fora da tolerância (Rejeitado)

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

O encargo de cabeçalho por unidade está fora da tolerância e não foi aprovado.

## Ação:

O sistema ajusta o encargo de cabeçalho ao pedido de compra, processa a transação e gera as notas necessárias.

## Exemplo:

* **Pedido de compra (PO):**
  * Encargo de cabeçalho por unidade: $4.00
  * Quantidade: 1,500 unidades
  * Valor total do encargo de cabeçalho: $6,000.00
* **Fatura recebida:**
  * Encargo de cabeçalho por unidade: $5.00 (fora da tolerância de 25%, rejeitado)
  * Quantidade: 1,500 unidades
  * Valor total do encargo de cabeçalho: $7,500.00
* **Níveis de tolerância:**
  * Tolerância do encargo de cabeçalho por unidade: ±5%

Como o encargo de cabeçalho por unidade ($5.00) excede a tolerância de 5% e não foi aprovado, o sistema irá:

1. **Rejeitar o encargo de cabeçalho faturado por unidade:** o sistema não aceita o valor de $5.00 porque o desvio excede o limite de tolerância.
2. **Ajustar o encargo de cabeçalho por unidade:** o sistema ajusta o valor ao pedido de compra original ou ao encargo por unidade aprovado:
   * Encargo de cabeçalho ajustado por unidade = $4.00 (do pedido de compra)
3. **Recalcular o total do encargo de cabeçalho:** o sistema recalcula o total com o encargo por unidade ajustado:
   * **Valor total corrigido do encargo de cabeçalho = Quantidade × Encargo de cabeçalho ajustado por unidade**
   * **Valor total corrigido do encargo de cabeçalho = 1,500 unidades × $4.00 = $6,000.00**
4. **Gerar uma nota de crédito:** como o total original da fatura é superior ao total corrigido, o sistema gera uma nota de crédito para o valor cobrado em excesso:
   * **Valor da nota de crédito = Total original da fatura - Valor total corrigido do encargo de cabeçalho**
   * **Valor da nota de crédito = $7,500.00 - $6,000.00 = $1,500.00**
5. **Processar a fatura:** o sistema processa a fatura com o total corrigido de $6,000.00 e emite uma nota de crédito de $1,500.00 para refletir o valor cobrado em excesso.

Esta abordagem alinha a transação com as condições originais do pedido de compra, corrigindo os valores cobrados em excesso nos registos financeiros.
