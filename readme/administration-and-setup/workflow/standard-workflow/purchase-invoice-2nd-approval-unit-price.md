# Purchase Invoice - 2nd Approval Unit Price

<figure><img src="../../../../.gitbook/assets/docbits_approval_invoice_3.png" alt="DocBits Aprovação Fatura 3"><figcaption></figcaption></figure>

Este título indica que a regra está configurada para gerir a fase de segunda aprovação de uma fatura de compra, com enfoque específico na validação do preço unitário.

#### Configuração da regra:

1. **When…**
   * **Document Type is Invoice**: Esta condição garante que a regra é acionada apenas para documentos identificados como faturas, filtrando outros tipos de documento e mantendo a relevância do fluxo de trabalho.
2. **And…**
   * **Document Status is Pending Second Approval**: Isto especifica que a fatura está na fase em que aguarda uma segunda aprovação. Trata-se normalmente de um passo concebido para garantir uma supervisão adicional antes do processamento final.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Isto restringe ainda mais a aplicação desta regra apenas às faturas classificadas como "Purchase Invoices", distinguindo-as de outros subtipos de fatura.
   * **Logic Unit Price in order confirmation Not Equals purchase order**: Esta verificação lógica é fundamental, pois compara o preço unitário indicado na confirmação da encomenda com o preço unitário da ordem de compra original. A ação é acionada caso estes valores não coincidam, o que pode indicar uma discrepância que necessita de resolução.

#### Ação (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: Se as condições especificadas forem cumpridas (ou seja, se existir uma divergência nos preços unitários), a fatura é automaticamente atribuída a um comprador (o nome indicado no campo 'Buyer Name') para revisão adicional. Se o campo 'Buyer Name' estiver vazio ou não especificado, é atribuído um utilizador predefinido (provavelmente um administrador ou outro colaborador designado) como alternativa para tratar da aprovação.

#### Objetivo desta regra:

* **Ensure Accuracy and Compliance**: Esta regra é fundamental para garantir que o processo de faturação é exato e está em conformidade com os termos acordados. Ao desencadear uma revisão sempre que existe uma discrepância nos preços unitários, o sistema ajuda a prevenir erros financeiros ou possíveis fraudes.
* **Streamline Approvals**: A automatização da atribuição para revisão com base em discrepâncias específicas ajuda a simplificar o processo de aprovação e garante que os problemas são prontamente resolvidos pelo pessoal adequado.
* **Financial Oversight**: A exigência de uma segunda aprovação, especialmente com base na correspondência de preços, reforça os controlos financeiros e a responsabilização dentro da organização.
