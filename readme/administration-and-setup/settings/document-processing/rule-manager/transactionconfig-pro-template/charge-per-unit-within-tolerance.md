# Encargo por unidade dentro da tolerância

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

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
  * Encargo por unidade: $5.10 (dentro da tolerância de 2%)
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
