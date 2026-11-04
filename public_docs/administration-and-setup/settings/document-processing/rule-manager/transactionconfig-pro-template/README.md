# TransactionConfig Pro Template

> **Nota sobre o exemplo:** Este cenário ilustra um mapeamento de exportação configurado. A saída real, os montantes, o sinal e o tipo de documento dependem do mapeamento ativo, das expressões das regras e das decisões de aprovação. A geração de dados para uma nota de débito ou de crédito não significa, por si só, a emissão de um documento fiscal válido. Verifique a configuração e o resultado no ERP; este exemplo não garante conformidade legal.

## Ferramenta de configuração para o processamento de documentos financeiros

O _TransactionConfig Pro Template_ é uma ferramenta de configuração para ambientes empresariais que gere o processamento de documentos financeiros, como faturas e notas de débito e crédito. Disponibiliza mapeamentos e definições de campos detalhados para automatizar e personalizar os fluxos financeiros. A integração utiliza os mapeamentos configurados para os sistemas ERP Infor existentes.

### Principais funcionalidades

• Mapeamento detalhado: permite mapear campos de vários tipos de transação com precisão, mantendo a consistência e a exatidão dos dados.

• Personalização: adapta os fluxos de documentos financeiros às necessidades específicas da empresa.

• Automatização: automatiza o tratamento das transações financeiras, reduzindo erros manuais e aumentando a eficiência.

• Integração: integra-se com os sistemas ERP Infor M3/LN existentes, alargando as capacidades de processamento financeiro da organização.

• Âmbito: estas regras configuram o tratamento técnico dos dados. Os requisitos fiscais e a validade de notas de débito ou de crédito devem ser verificados separadamente.



## Explicação detalhada dos casos de resolução de conflitos

O _TransactionConfig Pro Template_ inclui regras predefinidas para tratar divergências comuns entre os dados da fatura e do pedido de compra (PO). Estas regras automatizam as decisões quando existem diferenças, promovendo a consistência e a exatidão do processamento financeiro.

### [Caso 1, 2, 3: Quantidade e preço unitário dentro da tolerância](case-1-2-3-quantity-and-unit-price-within-tolerance.md)

**Cenário:** a quantidade e o preço unitário da fatura estão dentro da tolerância aceite em relação ao pedido de compra.

• **Ação:** o sistema aceita os valores da fatura e calcula o total a partir da quantidade e do preço unitário indicados.

### [Caso 4, 5: Quantidade dentro da tolerância, Preço unitário fora da tolerância (Aprovado)](case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md)

**Cenário:** a quantidade da fatura está dentro da tolerância, mas o preço unitário está fora; esse desvio foi aprovado.

• **Ação:** o sistema ajusta o preço unitário ao pedido de compra e aplica os encargos de linha necessários para refletir a diferença.

### [Caso 6: Quantidade dentro da tolerância, Preço unitário abaixo da tolerância inferior (Rejeitado)](case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

**Cenário:** a quantidade está dentro da tolerância, mas o preço unitário está abaixo do limite inferior e o desvio não foi aprovado.

• **Ação:** o sistema rejeita o preço unitário, ajusta-o ao pedido de compra e gera uma nota de crédito para a diferença. Podem ser aplicados encargos adicionais de cabeçalho, se necessário.

### [Caso 7: Quantidade dentro da tolerância, Preço unitário fora da tolerância (Desvio positivo rejeitado)](case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md)

**Cenário:** a quantidade está dentro da tolerância, mas o preço unitário está acima do limite superior e o desvio não foi aprovado.

• **Ação:** o sistema rejeita o preço unitário da fatura, ajusta-o ao pedido de compra e pode gerar uma nota de débito para refletir o valor cobrado em excesso.

### [Caso 8a, 9a: Quantidade fora da tolerância (Aprovado), Preço unitário dentro da tolerância](case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md)

**Cenário:** a quantidade da fatura está fora da tolerância aceite, mas foi aprovada; o preço unitário permanece dentro da tolerância.

• **Ação:** o sistema aceita a quantidade aprovada e o preço unitário da fatura e processa a transação com esses valores.

### [Caso 11a: Quantidade fora da tolerância (Desvio positivo rejeitado), Preço unitário dentro da tolerância](case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md)

**Cenário:** a quantidade da fatura está acima do limite superior e foi rejeitada, mas o preço unitário está dentro da tolerância.

• **Ação:** o sistema ajusta a quantidade ao valor aprovado, mantém o preço unitário e processa a transação. A quantidade excedente é rejeitada e não é faturada.

### [Caso 10a: Quantidade fora da tolerância (Desvio negativo rejeitado), Preço unitário dentro da tolerância](case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md)

**Cenário:** a quantidade está abaixo do limite inferior e o desvio não foi aprovado, embora o preço unitário esteja dentro da tolerância.

• **Ação:** o sistema ajusta a quantidade ao valor aprovado, mantém o preço unitário e processa a transação.

### [Caso 8b, 9b: Quantidade fora da tolerância (Aprovado), Preço unitário fora da tolerância (Aprovado)](case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md)

**Cenário:** a quantidade e o preço unitário estão fora da tolerância, mas ambos foram aprovados.

• **Ação:** o sistema processa a transação com a quantidade e o preço unitário da fatura, aplicando os ajustes ou encargos de linha necessários.

### [Caso 10b: Quantidade fora da tolerância (Desvio negativo rejeitado), Preço unitário fora da tolerância (Rejeitado)](case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md)

**Cenário:** a quantidade e o preço unitário estão fora da tolerância e nenhum dos desvios foi aprovado.

• **Ação:** o sistema rejeita os dados da fatura, ajusta os valores ao pedido de compra e gera as notas de débito ou crédito necessárias.

### [Caso 11b: Quantidade fora da tolerância (Desvio positivo rejeitado), Preço unitário fora da tolerância (Rejeitado)](case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md)

**Cenário:** a quantidade está acima do limite superior e foi rejeitada; o preço unitário também está fora da tolerância e foi rejeitado.

• **Ação:** o sistema ajusta a quantidade e o preço unitário aos valores aprovados do pedido de compra, rejeita os excessos e processa a transação.

### [Caso 12, 13: Linha de encargo - Encargo por unidade dentro da tolerância](charge-per-unit-within-tolerance.md)

**Cenário:** o encargo por unidade da fatura está dentro da tolerância aceite em relação ao pedido de compra.

• **Ação:** o sistema aceita o encargo por unidade faturado e processa a transação sem ajustes.

### [Caso 14: Linha de encargo - Encargo por unidade fora da tolerância (Aprovado)](charge-per-unit-outside-tolerance-approved-1.md)

**Cenário:** o encargo por unidade está fora da tolerância, mas foi aprovado.

• **Ação:** o sistema aceita o encargo por unidade e aplica os encargos aprovados ao processar a transação.

### [Caso 15: Linha de encargo - Encargo por unidade fora da tolerância (Rejeitado)](charge-per-unit-outside-tolerance-rejected.md)

**Cenário:** o encargo por unidade está fora da tolerância e não foi aprovado.

• **Ação:** o sistema ajusta o encargo por unidade ao pedido de compra ou aos valores aprovados e gera as notas de débito ou crédito necessárias.

### [Caso 12, 13: Encargo de cabeçalho - Encargo por unidade dentro da tolerância](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**Cenário:** o encargo de cabeçalho por unidade está dentro da tolerância aceite em relação ao pedido de compra.

• **Ação:** o sistema processa o encargo de cabeçalho faturado sem ajustes.

### [Caso 14: Encargo de cabeçalho - Encargo por unidade fora da tolerância (Aprovado)](charge-per-unit-outside-tolerance-approved.md)

**Cenário:** o encargo de cabeçalho por unidade está fora da tolerância, mas foi aprovado.

• **Ação:** o sistema processa o encargo por unidade aprovado e aplica-o à transação.

### [Caso 15: Encargo de cabeçalho - Encargo por unidade fora da tolerância (Rejeitado)](case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md)

**Cenário:** o encargo de cabeçalho por unidade está fora da tolerância e não foi aprovado.

• **Ação:** o sistema ajusta o encargo de cabeçalho ao pedido de compra, processa a transação e gera as notas necessárias.

### [Linhas de imposto](tax-lines.md "mention")

**Cenário:** divergências nos valores dos impostos entre a fatura e o pedido de compra.

• **Ação:** o sistema ajusta as linhas de imposto às taxas e aos valores aprovados, de acordo com as regras fiscais aplicáveis.
