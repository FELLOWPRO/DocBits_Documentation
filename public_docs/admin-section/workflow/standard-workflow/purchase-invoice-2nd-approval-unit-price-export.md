# Fatura de Compra - Exportação de Preço Unitário de 2ª Aprovação

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_5.png" alt="DocBits Compra Pedido Exportar 5"><figcaption></figcaption></figure>

Este título indica que a regra está configurada para gerenciar a segunda fase de aprovação de faturas de compra com foco no preço unitário, garantindo que corresponda aos termos acordados.

#### Configuração da Regra:

1. **Quando…**
* **Tipo de Documento é Fatura**: Esta condição garante que a regra seja ativada apenas para documentos identificados como faturas, o que é crucial para direcionar o fluxo de trabalho com precisão.
2. **E…**
* **Status do Documento é Pendente de Segunda Aprovação**: Isso especifica que a fatura está aguardando uma segunda aprovação. Essa etapa frequentemente fornece supervisão adicional para garantir precisão antes de finalizar a transação.
* **Campo do Documento Subtipo de Fatura é Igual a Fatura de Compra**: Esta condição especifica ainda mais que a regra se aplica apenas a faturas categorizadas especificamente como "Faturas de Compra", diferenciando-as de outros tipos de faturas.
* **Lógica Preço Unitário na confirmação do pedido é Igual ao pedido de compra**: Esta condição verifica se o preço unitário listado na confirmação do pedido corresponde ao preço unitário no pedido de compra. Garante que o processamento da fatura avance apenas se houver consistência nos preços, o que é crucial para o orçamento e relatórios financeiros.

#### Ação (Então…):

* **Iniciar Exportação**: Uma vez que a fatura atende às condições especificadas (ou seja, os preços unitários correspondem entre a confirmação do pedido e o pedido de compra), a ação de "Iniciar Exportação" é acionada. Isso provavelmente envolve exportar os dados da fatura para processamento adicional, possivelmente para outro sistema financeiro ou para fins de relatório.

#### Propósito Dessa Regra:

* **Garantir Precisão e Consistência**: Ao verificar que os preços unitários correspondem entre a confirmação do pedido e o pedido de compra, o sistema ajuda a manter a precisão financeira e evita cobranças excessivas ou insuficientes.
* **Otimizar o Processamento Financeiro**: Automatizar a exportação de dados uma vez que os preços são confirmados reduz o manuseio manual e acelera o ciclo de processamento financeiro.
* **Aprimorar a Conformidade e Supervisão**: Exigir uma segunda aprovação para verificação de preços adiciona uma camada extra de supervisão, o que é crucial para a conformidade com políticas e controles financeiros.

Esta regra é um exemplo de como a automação de fluxo de trabalho pode ser utilizada de forma eficaz para garantir o manuseio preciso e eficiente de documentos financeiros dentro de uma organização, especialmente no contexto de grandes volumes de transações que requerem validação meticulosa.
