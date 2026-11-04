# Fatura de Compra - 2ª Aprovação Preço Unitário

<figure><img src="../../../.gitbook/assets/docbits_approval_invoice_3.png" alt="DocBits Aprovação Fatura 3"><figcaption></figcaption></figure>

Este título indica que a regra está configurada para gerenciar a segunda fase de aprovação de uma fatura de compra, com foco específico na validação do preço unitário.

#### Configuração da Regra:

1. **Quando…**
* **Tipo de Documento é Fatura**: Esta condição garante que a regra seja acionada apenas para documentos identificados como faturas, filtrando outros tipos de documentos e mantendo a relevância do fluxo de trabalho.
2. **E…**
* **Status do Documento é Pendente de Segunda Aprovação**: Isso especifica que a fatura está na fase em que aguarda uma segunda aprovação. Geralmente, este é um passo projetado para garantir uma supervisão adicional antes do processamento final.
* **Subtipo de Fatura é Igual a Fatura de Compra**: Isso restringe ainda mais a aplicação desta regra apenas para faturas classificadas como "Faturas de Compra", distinguindo-as de outros subtipos de faturas.
* **Lógica Preço Unitário na confirmação do pedido Não é Igual ao pedido de compra**: Esta verificação lógica é crucial, pois compara o preço unitário listado na confirmação do pedido com o preço unitário no pedido de compra original. A ação é acionada se esses valores não corresponderem, o que poderia indicar uma discrepância que precisa ser resolvida.

#### Ação (Então…):

* **Atribuir usuário do campo Nome do Comprador, usar usuário Usuário como alternativa**: Se as condições especificadas forem atendidas (ou seja, houver uma diferença nos preços unitários), a fatura é automaticamente atribuída a um comprador (o nome especificado no campo 'Nome do Comprador') para uma revisão adicional. Se o campo 'Nome do Comprador' estiver vazio ou não especificado, um usuário padrão (provavelmente um administrador ou outro membro designado da equipe) é atribuído como alternativa para lidar com a aprovação.

#### Propósito Dessa Regra:

* **Garantir Precisão e Conformidade**: Esta regra é crucial para garantir que o processo de faturamento seja preciso e esteja em conformidade com os termos acordados. Ao acionar uma revisão quando há uma discrepância nos preços unitários, o sistema ajuda a evitar erros financeiros ou possíveis fraudes.
* **Agilizar Aprovações**: Automatizar a atribuição para revisão com base em discrepâncias específicas ajuda a agilizar o processo de aprovação e garante que os problemas sejam prontamente tratados pelo pessoal apropriado.
* **Supervisão Financeira**: Exigir uma segunda aprovação, especialmente com base na correspondência de preços, reforça os controles financeiros e a responsabilidade dentro da organização.
