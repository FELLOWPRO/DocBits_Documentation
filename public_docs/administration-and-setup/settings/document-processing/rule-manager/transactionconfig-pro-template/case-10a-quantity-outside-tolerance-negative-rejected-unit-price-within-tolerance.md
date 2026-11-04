# Caso 10a: Quantidade abaixo da tolerância rejeitada; preço unitário dentro da tolerância

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade está abaixo do limite inferior e o desvio não foi aprovado, embora o preço unitário esteja dentro da tolerância.

## Ação:

O sistema ajusta a quantidade ao valor aprovado, mantém o preço unitário e processa a transação.

## Exemplo:

* **Pedido de compra (PO):**
  * Quantidade: 150 unidades
  * Preço unitário: $20.00 por unidade
  * Valor total: $3,000.00
* **Fatura recebida:**
  * Quantidade: 140 unidades (fora da tolerância de -6.67%, rejeitado)
  * Preço unitário: $20.00 por unidade (dentro da tolerância)
  * Valor total: $2,800.00
* **Níveis de tolerância:**
  * Tolerância da quantidade: ±5%
  * Tolerância do preço unitário: ±2%

Como a quantidade (140 unidades) está abaixo do limite inferior, com um desvio de -6.67% não aprovado, mas o preço unitário ($20.00) está dentro da tolerância, o sistema irá:

1. **Rejeitar a quantidade inferior:** o sistema não aceita a quantidade inferior por estar fora da tolerância aprovada.
2. **Ajustar a quantidade:** o sistema ajusta a quantidade ao valor aprovado no pedido de compra.
   * Quantidade aprovada = 150 unidades (do pedido de compra)
3. **Manter o preço unitário:** o preço de $20.00 por unidade está dentro da tolerância e mantém-se.
4. **Recalcular o valor total:** o sistema calcula o total com a quantidade aprovada e o preço unitário aceite:
   * **Valor total = Quantidade aprovada × Preço unitário**
   * **Valor total = 150 unidades × $20.00 por unidade = $3,000.00**
5. **Processar a fatura:** o sistema processa a fatura com o total ajustado de $3,000.00, refletindo a quantidade e o preço unitário aprovados. Espera-se que o fornecedor fature a quantidade aprovada na totalidade.

Esta abordagem alinha a transação com as condições do pedido de compra e evita a faturação de uma quantidade inferior, mantendo os registos financeiros.
