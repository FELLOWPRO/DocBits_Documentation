# Encargo por unidade dentro da tolerância

> **Nota sobre o exemplo:** O cenário seguinte é um mapeamento configurado a título de exemplo, não um modelo padrão cuja implantação tenha sido verificada. A saída real, os valores, os sinais e os tipos de documento dependem das regras e expressões `conflict_resolution` ativas, do mapeamento de exportação e das decisões de aprovação. Qualquer nota de débito ou de crédito descrita abaixo depende dessa configuração; o exemplo não garante emissão automática nem conformidade legal.

## Cenário:

O encargo por unidade da fatura está dentro da tolerância aceite em relação ao pedido de compra.

## Ação:

O sistema aceita o encargo por unidade faturado e processa a transação sem ajustes.

## Exemplo:

* **Pedido de compra (PO):**
  * Encargo por unidade: $5.00
  * Quantidade: 500 unidades
  * Valor total dos encargos: $2,500.00
* **Fatura recebida:**
  * Encargo por unidade: $5.10 (variação 2%, dentro da tolerância de ±3%)
  * Quantidade: 500 unidades
  * Valor total dos encargos: $2,550.00
* **Níveis de tolerância:**
  * Tolerância do encargo por unidade: ±3%

Como o encargo por unidade ($5.10) está dentro da tolerância de 3% em relação ao pedido de compra, o sistema irá:

1. **Aceitar o encargo por unidade:** o sistema aceita o valor faturado de $5.10 por estar dentro do limite de tolerância definido.
2. **Processar a transação:** o sistema processa a fatura com o total dos encargos calculado a partir do encargo por unidade faturado e da quantidade:
   * **Valor total dos encargos = Quantidade × Encargo por unidade**
   * **Valor total dos encargos = 500 unidades × $5.10 = $2,550.00**
3. **Finalizar a fatura:** o sistema processa a transação sem ajustes e aceita a fatura tal como foi apresentada.

Esta abordagem permite aceitar pequenas diferenças nos encargos dentro da tolerância, sem rejeições ou atrasos desnecessários.
