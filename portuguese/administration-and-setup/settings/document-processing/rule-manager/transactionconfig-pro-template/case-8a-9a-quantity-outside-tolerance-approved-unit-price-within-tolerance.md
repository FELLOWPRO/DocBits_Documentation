# Caso 8a, 9a: Quantidade fora da tolerância (Aprovado), Preço unitário dentro da tolerância

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade da fatura está fora da tolerância aceite, mas foi aprovada; o preço unitário permanece dentro da tolerância.

## Ação:

O sistema aceita a quantidade aprovada e o preço unitário da fatura e processa a transação.

## Exemplo:

* **Pedido de compra (PO):**
  * Quantidade: 150 unidades
  * Preço unitário: $12.00 por unidade
  * Valor total: $1,800.00
* **Fatura recebida:**
  * Quantidade: 160 unidades (fora da tolerância de 6.67% mas aprovado)
  * Preço unitário: $12.00 por unidade (dentro da tolerância)
  * Valor total: $1,920.00
* **Níveis de tolerância:**
  * Tolerância da quantidade: ±5%
  * Tolerância do preço unitário: ±2%

Como a quantidade (160 unidades) excede o limite de tolerância, mas foi aprovada, e o preço unitário ($12.00) está dentro do intervalo aceite, o sistema irá:

1. **Aceitar a quantidade aprovada:** o sistema reconhece a aprovação da quantidade apesar de estar fora da tolerância normal.
2. **Aceitar o preço unitário:** o preço de $12.00 por unidade está dentro da tolerância e é aceite tal como foi faturado.
3. **Processar a transação:** o sistema calcula o total com a quantidade aprovada e o preço unitário:
   * **Valor total = Quantidade × Preço unitário**
   * **Valor total = 160 unidades × $12.00 por unidade = $1,920.00**
4. **Finalizar a fatura:** o sistema processa a fatura com o total de $1,920.00, refletindo a quantidade aprovada e o preço unitário aceite.

Esta abordagem permite aceitar desvios aprovados na quantidade, mantendo o preço unitário dentro do intervalo esperado.
