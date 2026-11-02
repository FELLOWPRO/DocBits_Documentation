# Encargo por unidade dentro da tolerância

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

O encargo de cabeçalho por unidade está dentro da tolerância aceite em relação ao pedido de compra.

## Ação:

O sistema processa o encargo de cabeçalho faturado sem ajustes.

## Exemplo:

* **Pedido de compra (PO):**
  * Encargo de cabeçalho por unidade: $3.50
  * Quantidade: 1,200 unidades
  * Valor total do encargo de cabeçalho: $4,200.00
* **Fatura recebida:**
  * Encargo de cabeçalho por unidade: $3.55 (dentro da tolerância de 1.43%)
  * Quantidade: 1,200 unidades
  * Valor total do encargo de cabeçalho: $4,260.00
* **Níveis de tolerância:**
  * Tolerância do encargo de cabeçalho por unidade: ±2%

Como o encargo de cabeçalho por unidade ($3.55) está dentro da tolerância de 2% em relação ao pedido de compra, o sistema irá:

1. **Aceitar o encargo de cabeçalho por unidade:** o sistema aceita o valor faturado de $3.55 por estar dentro do limite definido.
2. **Processar o encargo de cabeçalho:** o sistema processa a fatura com o total calculado a partir do encargo faturado por unidade e da quantidade:
   * **Valor total do encargo de cabeçalho = Quantidade × Encargo de cabeçalho por unidade**
   * **Valor total do encargo de cabeçalho = 1,200 unidades × $3.55 = $4,260.00**
3. **Finalizar a fatura:** o sistema processa a transação sem ajustes e aceita a fatura tal como foi apresentada.

Esta abordagem permite processar os encargos de cabeçalho dentro da tolerância aceite sem rejeições ou atrasos desnecessários.
