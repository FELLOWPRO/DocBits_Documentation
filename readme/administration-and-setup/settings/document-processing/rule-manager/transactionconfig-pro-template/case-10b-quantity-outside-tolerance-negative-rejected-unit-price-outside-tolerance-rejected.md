# Caso 10b: Quantidade abaixo da tolerância e preço unitário fora da tolerância — rejeitados

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade e o preço unitário estão fora da tolerância e nenhum dos desvios foi aprovado.

## Ação:

O sistema rejeita os dados da fatura, ajusta os valores ao pedido de compra e gera as notas de débito ou crédito necessárias.

## Exemplo:

* **Pedido de compra (PO):**
  * Quantidade: 150 unidades
  * Preço unitário: $30.00 por unidade
  * Valor total: $4,500.00
* **Fatura recebida:**
  * Quantidade: 140 unidades (fora da tolerância de -6.67%, rejeitado)
  * Preço unitário: $33.00 por unidade (fora da tolerância de 10%, rejeitado)
  * Valor total: $4,620.00
* **Níveis de tolerância:**
  * Tolerância da quantidade: ±5%
  * Tolerância do preço unitário: ±2%

Como a quantidade (140 unidades) e o preço unitário ($33.00) estão fora dos limites de tolerância e nenhum dos desvios foi aprovado, o sistema irá:

1. **Rejeitar os dados da fatura:** o sistema não aceita a quantidade nem o preço unitário faturados devido ao desvio dos limites de tolerância.
2. **Ajustar a quantidade:** o sistema repõe a quantidade do pedido de compra original.
   * Quantidade ajustada = 150 unidades (do pedido de compra)
3. **Ajustar o preço unitário:** o sistema repõe o preço unitário do pedido de compra original.
   * Preço unitário ajustado = $30.00 por unidade (do pedido de compra)
4. **Recalcular o valor total:** o sistema recalcula o total com a quantidade e o preço unitário ajustados:
   * **Valor total corrigido = Quantidade ajustada × Preço unitário ajustado**
   * **Valor total corrigido = 150 unidades × $30.00 por unidade = $4,500.00**
5. **Gerar uma nota de débito:** como o total original da fatura é superior ao total corrigido, o sistema gera uma nota de débito para o valor cobrado em excesso.
   * **Valor da nota de débito = Total original da fatura - Valor total corrigido**
   * **Valor da nota de débito = $4,620.00 - $4,500.00 = $120.00**
6. **Processar a fatura:** o sistema processa a fatura com o total corrigido de $4,500.00 e emite uma nota de débito de $120.00 para compensar o valor cobrado em excesso.

Esta abordagem corrige a transação de acordo com as condições do pedido de compra, mantendo os registos financeiros.
