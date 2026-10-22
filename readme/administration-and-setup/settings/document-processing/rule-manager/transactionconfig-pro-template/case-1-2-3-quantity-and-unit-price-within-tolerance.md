# Caso 1, 2, 3: Quantidade e preço unitário dentro da tolerância

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade e o preço unitário da fatura estão dentro da tolerância aceite em relação ao pedido de compra.

## Ação:

O sistema aceita os valores da fatura e calcula o total a partir da quantidade e do preço unitário indicados.

## Exemplo:

**Pedido de compra (PO):**

Quantidade: 100 unidades

Preço unitário: $10.00 por unidade

Valor total: $1,000.00

**Fatura recebida:**

Quantidade: 101 unidades (dentro da tolerância de 1%)

Preço unitário: $10.05 por unidade (dentro da tolerância de 0.5%)

Valor total: $1,015.05

**Níveis de tolerância:**

Tolerância da quantidade: ±2%

Tolerância do preço unitário: ±1%\


Como a quantidade (101 unidades) e o preço unitário ($10.05) estão dentro da tolerância aceite em relação ao pedido de compra, o sistema irá:\


1\. **Aceitar os valores da fatura:** a quantidade e o preço unitário são aceites por estarem dentro dos limites de tolerância definidos.

2\. **Calcular o valor total:** o total é calculado com os valores aceites:

• Valor total = Quantidade × Preço unitário

• Valor total = 101 unidades × $10.05 por unidade = $1,015.05

3\. **Processar a fatura:** a fatura é processada com o total de $1,015.05 e os registos financeiros são atualizados.

Esta abordagem evita rejeições ou atrasos no pagamento causados por pequenas divergências dentro da tolerância aceite.
