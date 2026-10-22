# Caso 6: Quantidade dentro da tolerância, Preço unitário abaixo da tolerância inferior (Rejeitado)

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade está dentro da tolerância, mas o preço unitário está abaixo do limite inferior e o desvio não foi aprovado.

## Ação:

Neste exemplo de mapeamento, o preço unitário é rejeitado e ajustado ao pedido de compra. O tratamento do desvio e de eventuais encargos de cabeçalho depende das ações configuradas.

## Exemplo:

* **Pedido de compra (PO):**
  * Quantidade: 100 unidades
  * Preço unitário: $10.00 por unidade
  * Valor total: $1,000.00
* **Fatura recebida:**
  * Quantidade: 100 unidades (desvio de 0%; dentro da tolerância de ±2%)
  * Preço unitário: $9.00 por unidade (desvio de −10%; fora da tolerância de ±1%)
  * Valor total: $900.00
* **Níveis de tolerância:**
  * Tolerância da quantidade: ±2%
  * Tolerância do preço unitário: ±1%

Como a quantidade (100 unidades) está dentro da tolerância, mas o preço unitário ($9.00) está abaixo do limite inferior e não foi aprovado, o sistema irá:

1. **Rejeitar o preço unitário:** o sistema não aceita o preço faturado de $9.00.
2. **Ajustar o preço unitário:** o sistema repõe o preço unitário do pedido de compra original.
   * Preço unitário ajustado = $10.00 (do pedido de compra)
3. **Calcular o total corrigido:** o sistema recalcula o total com o preço unitário ajustado.
   * **Valor total corrigido = Quantidade × Preço unitário ajustado**
   * **Valor total corrigido = 100 unidades × $10.00 por unidade = $1,000.00**
4. **Calcular o desvio com sinal:** o mapeamento compara o total original da fatura com o total corrigido. O tipo de saída depende das ações de débito ou crédito configuradas; o sinal do desvio não determina, por si só, um documento fiscal.
   * **Desvio com sinal = Total original da fatura - Valor total corrigido**
   * **Desvio com sinal = $900.00 - $1,000.00 = -$100.00**
   * O resultado de -$100.00 é a diferença com sinal entre 900 e 1,000. Não demonstra, por si só, que uma nota de crédito corrige o valor cobrado a menos.
5. **Processar o resultado configurado:** neste exemplo, o total ajustado é $1,000.00 e o valor absoluto do desvio é $100.00. Verifique no mapeamento ativo e no ERP se existe uma saída adicional, qual o seu sinal e qual o tipo de documento aplicado.

Esta abordagem alinha o preço com as condições do pedido de compra, mesmo quando é faturado um preço inferior incorreto.
