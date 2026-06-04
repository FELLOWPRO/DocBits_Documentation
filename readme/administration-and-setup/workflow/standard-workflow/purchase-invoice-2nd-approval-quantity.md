# Purchase Invoice - 2nd Approval Quantity

<figure><img src="../../../../.gitbook/assets/docbits_approval_invoice_4.png" alt="DocBits Aprovação Fatura 4"><figcaption></figcaption></figure>

Este título indica que a regra se refere especificamente ao tratamento de faturas de compra durante uma fase de aprovação secundária, com enfoque na verificação da exatidão das quantidades indicadas.

#### Configuração da regra:

1. **When…**
   * **Document Type is Invoice**: Esta condição garante que a regra é ativada apenas para documentos classificados como faturas. Isto é essencial para manter a especificidade e a relevância no fluxo de trabalho.
2. **And…**
   * **Document Status is Pending Second Approval**: Isto especifica que a fatura está atualmente pendente de uma segunda aprovação. Esta fase destina-se normalmente a proporcionar uma supervisão adicional antes de finalizar a fatura.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Esta condição refina ainda mais a regra para se aplicar exclusivamente a faturas identificadas como "Purchase Invoices". Esta categorização ajuda a diferenciá-las de outros tipos de fatura.
   * **Logic Quantity in order confirmation Not Equals purchase order**: Esta condição crítica verifica se a quantidade indicada na confirmação da encomenda corresponde à quantidade da ordem de compra original. A ação é acionada caso exista uma discrepância, indicando um possível erro ou problema que necessita de resolução.

#### Ação (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: Se as condições da regra forem cumpridas (ou seja, se existir uma discrepância nas quantidades), a fatura é automaticamente atribuída à pessoa indicada no campo 'Buyer Name' para revisão adicional. Se este campo estiver vazio ou se a pessoa especificada não estiver disponível, um utilizador predefinido (provavelmente um administrador ou outro colaborador designado) assume a tarefa para garantir uma revisão e resolução atempadas.

#### Objetivo desta regra:

* **Accuracy and Compliance**: A regra é vital para garantir que o processo de faturação é exato e está em conformidade com os termos acordados na ordem de compra. Ajuda a prevenir discrepâncias financeiras e potenciais erros de inventário.
* **Streamlined Approvals**: A automatização do processo de revisão para discrepâncias específicas ajuda a simplificar as aprovações e garante que quaisquer problemas são rapidamente resolvidos pelo pessoal adequado.
* **Enhanced Financial Oversight**: A exigência de uma aprovação secundária para a verificação das quantidades reforça os controlos financeiros e a responsabilização dentro da organização.

Esta configuração exemplifica como a automação de fluxos de trabalho pode ser utilizada para melhorar a eficiência operacional e garantir a integridade financeira, em particular na gestão de processos de compra complexos dentro de uma empresa.
