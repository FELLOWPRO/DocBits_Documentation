# Fatura de Compra - Exportação de Quantidade de 2ª Aprovação

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_6.png" alt="DocBits Compra Pedido Exportar 6"><figcaption></figcaption></figure>

Este título indica que a regra está configurada para gerenciar a segunda fase de aprovação para faturas de compra com ênfase nos detalhes de quantidade, garantindo que as quantidades na fatura correspondam às do pedido de compra original.

#### Configuração da Regra:

1. **Quando…**
* **Tipo de Documento é Fatura**: Esta condição garante que a regra seja ativada apenas para documentos identificados como faturas, o que é crucial para direcionar o fluxo de trabalho com precisão.
2. **E…**
* **Status do Documento é Pendente de Segunda Aprovação**: Isso especifica que a fatura está atualmente aguardando uma segunda aprovação. Esta etapa frequentemente fornece supervisão adicional para garantir precisão antes que a transação seja finalizada.
* **Campo do Documento Subtipo de Fatura é Igual a Fatura de Compra**: Esta condição especifica ainda mais que a regra se aplica apenas a faturas categorizadas especificamente como "Faturas de Compra", diferenciando-as de outros tipos de faturas.
* **Lógica Quantidade na confirmação do pedido é Igual ao pedido de compra**: Esta condição verifica se a quantidade listada na confirmação do pedido corresponde à quantidade no pedido de compra. Isso garante que o processamento da fatura avance apenas se as quantidades forem consistentes, o que é crítico para a gestão de inventário e a precisão financeira.

#### Ação (Então…):

* **Iniciar Exportação**: Uma vez que a fatura atende às condições especificadas (ou seja, as quantidades correspondem entre a confirmação do pedido e o pedido de compra), a ação de "Iniciar Exportação" é acionada. Isso provavelmente envolve exportar os dados da fatura para processamento adicional, possivelmente para outro sistema financeiro ou para fins de relatório.

#### Objetivo Dessa Regra:

* **Garantir Precisão e Consistência**: Ao verificar que as quantidades correspondem entre a confirmação do pedido e o pedido de compra, o sistema ajuda a manter a precisão do inventário e evita discrepâncias que poderiam afetar relatórios financeiros ou gestão de estoque.
* **Otimizar o Processamento Financeiro**: Automatizar a exportação de dados uma vez que as quantidades são confirmadas reduz o manuseio manual e acelera o ciclo de processamento financeiro.
* **Aprimorar a Conformidade e Supervisão**: Exigir uma segunda aprovação para verificação de quantidade adiciona uma camada extra de supervisão, crucial para a conformidade com políticas e controles financeiros.

Esta regra é um exemplo claro de como a automação de fluxo de trabalho pode ser usada de forma eficaz para garantir o manuseio preciso e eficiente de documentos financeiros dentro de uma organização, especialmente no contexto de processos de compra que envolvem grandes volumes de transações que requerem validação meticulosa.
