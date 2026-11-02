# Caso 4, 5: Quantidade dentro da tolerância, Preço unitário fora da tolerância (Aprovado)

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Cenário:

A quantidade da fatura está dentro da tolerância, mas o preço unitário está fora do intervalo aceite. No entanto, o desvio de preço foi revisto e aprovado pelos responsáveis.

## Ação:

O sistema ajusta o preço unitário ao pedido de compra e aplica os encargos de linha necessários para refletir a diferença.

## Exemplo:

**Pedido de compra (PO):**

Quantidade: <mark style="color:green;">100</mark> unidades

Preço unitário: $10.00 por unidade

Valor total: <mark style="color:purple;">$1,000.00</mark>

**Fatura recebida:**

Quantidade: <mark style="color:green;">100</mark> unidades (dentro da tolerância)

Preço unitário: <mark style="color:red;">$11.00</mark> por unidade (fora da tolerância de ±5%)

Valor total: <mark style="color:red;">$1,100.00</mark>

**Níveis de tolerância:**

Tolerância da quantidade: ±2%

Tolerância do preço unitário: ±5% (intervalo esperado: $9.50 a $10.50)

**Aprovação:**

• O preço unitário de $11.00 está fora da tolerância, mas foi aprovado manualmente pelo departamento responsável.

Como a quantidade está dentro da tolerância e o desvio do preço unitário foi aprovado, o sistema irá:

1\. **Ajustar o preço unitário**: o sistema repõe o preço unitário do pedido de compra, uma vez que o desvio foi aprovado:

• **Preço unitário ajustado = $10.00 por unidade**

• **Valor total ajustado = 100 unidades × $10.00 por unidade = $1,000.00**

2\. **Aplicar um encargo de linha para a diferença**: como o preço aprovado de $11.00 é superior ao preço de $10.00 do pedido de compra, o sistema aplica um encargo de linha para refletir a diferença:

• **Valor do encargo da linha = (Preço unitário aprovado da fatura - Preço unitário do pedido de compra) × Quantidade**

• **Valor do encargo da linha = ($11.00 - $10.00) × 100 unidades = $100.00**

3\. **Processar a fatura**: o sistema processa a fatura com:

• **Valor base:** $1,000.00

• **Encargo da linha:** $100.00

• **Valor total processado:** $1,100.00

Os valores base do pedido de compra são mantidos, enquanto o desvio aprovado do preço unitário é refletido num encargo adicional de linha, preservando os registos financeiros da transação.
