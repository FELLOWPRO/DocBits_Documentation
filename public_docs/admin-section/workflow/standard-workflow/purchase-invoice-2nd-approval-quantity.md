# Fatura de Compra - 2ª Aprovação de Quantidade

<figure><img src="../../../.gitbook/assets/docbits_approval_invoice_4.png" alt="DocBits Aprovação Fatura 4"><figcaption></figcaption></figure>

Este título indica que a regra se refere especificamente ao tratamento de faturas de compra durante uma fase de aprovação secundária, com foco na verificação da precisão das quantidades listadas.

#### Configuração da Regra:

1. **Quando…**
* **Tipo de Documento é Fatura**: Esta condição garante que a regra seja ativada apenas para documentos classificados como faturas. Isso é essencial para manter a especificidade e relevância no fluxo de trabalho.
2. **E…**
* **Status do Documento é Pendente de Segunda Aprovação**: Isso especifica que a fatura está atualmente aguardando uma segunda aprovação. Esta etapa é geralmente destinada a fornecer supervisão adicional antes de finalizar a fatura.
* **Campo do Documento Subtipo de Fatura é Igual a Fatura de Compra**: Esta condição refina ainda mais a regra para se aplicar exclusivamente a faturas identificadas como "Faturas de Compra". Essa categorização ajuda a diferenciá-las de outros tipos de faturas.
* **Lógica Quantidade na confirmação do pedido Não é Igual ao pedido de compra**: Esta condição crítica verifica se a quantidade declarada na confirmação do pedido corresponde à quantidade no pedido de compra original. A ação é acionada se houver uma discrepância, indicando um possível erro ou problema que precisa ser resolvido.

#### Ação (Então…):

* **Atribuir usuário do campo Nome do Comprador, usar usuário Usuário como alternativa**: Se as condições da regra forem atendidas (ou seja, houver uma discrepância nas quantidades), a fatura é automaticamente atribuída à pessoa listada no campo 'Nome do Comprador' para uma revisão adicional. Se este campo estiver vazio ou a pessoa especificada não estiver disponível, um usuário padrão (provavelmente um administrador ou outro membro designado da equipe) assume para garantir uma revisão e resolução oportuna.

#### Propósito Dessa Regra:

* **Precisão e Conformidade**: A regra é vital para garantir que o processo de faturamento seja preciso e esteja alinhado com os termos acordados no pedido de compra. Isso ajuda a evitar discrepâncias financeiras e possíveis erros de inventário.
* **Aprovações Simplificadas**: Automatizar o processo de revisão para discrepâncias específicas ajuda a simplificar as aprovações e garante que quaisquer problemas sejam rapidamente tratados pela equipe apropriada.
* **Supervisão Financeira Aprimorada**: Exigir uma segunda aprovação para verificações de quantidade fortalece os controles financeiros e a responsabilidade dentro da organização.

Esta configuração exemplifica como a automação de fluxo de trabalho pode ser utilizada para aprimorar a eficiência operacional e garantir a integridade financeira, especialmente na gestão de processos de compra complexos dentro de uma empresa.
