# Caso 11a: Quantidade acima da tolerância rejeitada; preço unitário dentro da tolerância

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade da fatura excede o limite superior e foi rejeitada, mas o preço unitário está dentro da tolerância.

## Ação:

O sistema ajusta a quantidade ao valor aprovado, mantém o preço unitário e processa a transação. A quantidade excedente é rejeitada e não é faturada.

## Exemplo:

* **Pedido de compra (PO):**
  * Quantidade: 100 unidades
  * Preço unitário: $8.00 por unidade
  * Valor total: $800.00
* **Fatura recebida:**
  * Quantidade: 110 unidades (fora da tolerância de 10%, rejeitado)
  * Preço unitário: $8.00 por unidade (dentro da tolerância)
  * Valor total: $880.00
* **Níveis de tolerância:**
  * Tolerância da quantidade: ±5%
  * Tolerância do preço unitário: ±2%

Como a quantidade (110 unidades) excede o limite superior de tolerância, com um desvio de 10% não aprovado, mas o preço unitário ($8.00) está dentro da tolerância, o sistema irá:

1. **Rejeitar a quantidade excedente:** o sistema rejeita a quantidade que excede a tolerância aprovada.
2. **Ajustar a quantidade:** o sistema ajusta a quantidade ao valor aprovado no pedido de compra.
   * Quantidade aprovada = 100 unidades (do pedido de compra)
3. **Manter o preço unitário:** o preço de $8.00 por unidade está dentro da tolerância e mantém-se.
4. **Recalcular o valor total:** o sistema calcula o total com a quantidade aprovada e o preço unitário aceite:
   * **Valor total = Quantidade aprovada × Preço unitário**
   * **Valor total = 100 unidades × $8.00 por unidade = $800.00**
5. **Processar a fatura:** o sistema processa a fatura com o total ajustado de $800.00, refletindo apenas a quantidade e o preço aprovados. As 10 unidades excedentes são rejeitadas e não são faturadas.

Esta abordagem alinha o valor faturado com as condições do pedido de compra, mesmo quando o fornecedor tenta faturar uma quantidade superior.
