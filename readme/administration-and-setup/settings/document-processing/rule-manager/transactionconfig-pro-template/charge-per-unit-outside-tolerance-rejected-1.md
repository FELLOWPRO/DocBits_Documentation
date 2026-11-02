# Encargo por unidade fora da tolerância (Rejeitado)

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

O encargo por unidade está fora da tolerância e não foi aprovado.

## Ação:

O sistema ajusta o encargo por unidade ao pedido de compra ou aos valores aprovados e gera as notas de débito ou crédito necessárias.

## Exemplo:

* **Pedido de compra (PO):**
  * Encargo por unidade: $6.00
  * Quantidade: 800 unidades
  * Valor total dos encargos: $4,800.00
* **Fatura recebida:**
  * Encargo por unidade: $7.00 (fora da tolerância de 16.67%, rejeitado)
  * Quantidade: 800 unidades
  * Valor total dos encargos: $5,600.00
* **Níveis de tolerância:**
  * Tolerância do encargo por unidade: ±5%

Como o encargo por unidade ($7.00) excede a tolerância de 5% e não foi aprovado, o sistema irá:

1. **Rejeitar o encargo faturado por unidade:** o sistema não aceita o valor de $7.00 porque o desvio excede o limite de tolerância.
2. **Ajustar o encargo por unidade:** o sistema ajusta o valor ao pedido de compra ou ao encargo por unidade aprovado:
   * Encargo ajustado por unidade = $6.00 (do pedido de compra)
3. **Recalcular o total dos encargos:** o sistema recalcula o total com o encargo por unidade ajustado:
   * **Valor total corrigido dos encargos = Quantidade × Encargo ajustado por unidade**
   * **Valor total corrigido dos encargos = 800 unidades × $6.00 = $4,800.00**
4. **Gerar uma nota de débito:** como o total original da fatura é superior ao total corrigido, o sistema gera uma nota de débito para o valor cobrado em excesso:
   * **Valor da nota de débito = Total original da fatura - Valor total corrigido dos encargos**
   * **Valor da nota de débito = $5,600.00 - $4,800.00 = $800.00**
5. **Processar a fatura:** o sistema processa a fatura com o total corrigido dos encargos de $4,800.00 e emite uma nota de débito de $800.00 para refletir o valor cobrado em excesso.

Esta abordagem mantém a transação alinhada com as condições do pedido de compra e rejeita os desvios não aprovados.
