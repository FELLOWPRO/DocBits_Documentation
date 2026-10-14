# Purchase Invoice - 2nd Approval Quantity Export

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_export_6.png" alt="DocBits Compra Pedido Exportar 6"><figcaption></figcaption></figure>

Este título indica que a regra está configurada para gerir a fase de segunda aprovação de faturas de compra, com ênfase nos detalhes das quantidades, garantindo que as quantidades na fatura correspondem às da ordem de compra original.

#### Configuração da regra:

1. **When…**
   * **Document Type is Invoice**: Esta condição garante que a regra é ativada apenas para documentos identificados como faturas, o que é fundamental para encaminhar o fluxo de trabalho com precisão.
2. **And…**
   * **Document Status is Pending Second Approval**: Isto especifica que a fatura está atualmente pendente de uma segunda aprovação. Esta fase proporciona frequentemente uma supervisão adicional para garantir a exatidão antes de a transação ser finalizada.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Esta condição especifica ainda que a regra se aplica apenas a faturas categorizadas especificamente como "Purchase Invoices", diferenciando-as de outros tipos de faturas.
   * **Logic Quantity in order confirmation Equals purchase order**: Esta condição verifica se a quantidade indicada na confirmação da encomenda corresponde à quantidade da ordem de compra. Garante que o processamento da fatura só avança se as quantidades forem coincidentes, o que é fundamental para a gestão de inventário e a exatidão financeira.

#### Ação (Then…):

* **Start Export**: Assim que a fatura cumpre as condições especificadas (ou seja, as quantidades coincidem entre a confirmação da encomenda e a ordem de compra), é acionada a ação "Start Export". Isto envolve provavelmente a exportação dos dados da fatura para processamento adicional, possivelmente para outro sistema financeiro ou para fins de relatório.

#### Objetivo desta regra:

* **Ensure Accuracy and Consistency**: Ao verificar que as quantidades coincidem entre a confirmação da encomenda e a ordem de compra, o sistema ajuda a manter a exatidão do inventário e previne discrepâncias que possam afetar os relatórios financeiros ou a gestão de stock.
* **Streamline Financial Processing**: A automatização da exportação dos dados assim que as quantidades são confirmadas reduz o tratamento manual e acelera o ciclo de processamento financeiro.
* **Enhance Compliance and Oversight**: A exigência de uma segunda aprovação para a verificação das quantidades acrescenta uma camada extra de supervisão, fundamental para a conformidade com as políticas e os controlos financeiros.

Esta regra é um exemplo claro de como a automação de fluxos de trabalho pode ser utilizada eficazmente para garantir um tratamento preciso e eficiente dos documentos financeiros dentro de uma organização, em particular no contexto de processos de compra que envolvem grandes volumes de transações que exigem uma validação minuciosa.
