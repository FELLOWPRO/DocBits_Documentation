# Caso 1, 2, 3: Quantidade e preço unitário dentro da tolerância

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade e o preço unitário da fatura estão dentro da tolerância aceite em relação ao pedido de compra.

## Ação:

O sistema aceita os valores da fatura e calcula o total a partir da quantidade e do preço unitário indicados.

## Exemplo:

**Purchase Order (PO):**

Quantity: 100 units

Unit Price: $10.00 per unit

Total Amount: $1,000.00

**Invoice Received:**

Quantity: 101 units — 1% above the PO value, within the configured ±2% tolerance.

Unit Price: $10.05 per unit — 0.5% above the PO value, within the configured ±1% tolerance.

Total Amount: $1,015.05

**Tolerance Levels:**

Quantity Tolerance: ±2%

Unit Price Tolerance: ±1%


Como a quantidade (101 unidades) e o preço unitário ($10.05) estão dentro da tolerância aceite em relação ao pedido de compra, o sistema irá:


1\. **Aceitar os valores da fatura:** a quantidade e o preço unitário são aceites por estarem dentro dos limites de tolerância definidos.

2\. **Calcular o valor total:** o total é calculado com os valores aceites:

• Total Amount = Quantity × Unit Price

• Total Amount = 101 units × $10.05 per unit = $1,015.05

3\. **Processar a fatura:** a fatura é processada com o total de $1,015.05 e os registos financeiros são atualizados.

Esta abordagem evita rejeições ou atrasos no pagamento causados por pequenas divergências dentro da tolerância aceite.
