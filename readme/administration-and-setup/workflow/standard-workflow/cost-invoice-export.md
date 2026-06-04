# Cost Invoice - Export

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_export_4.png" alt="DocBits Compra Pedido Exportar 4"><figcaption></figcaption></figure>

Este título indica que a regra está especificamente configurada para gerir faturas de custo e envolve uma ação de exportação, possivelmente para relatórios, processamento adicional ou integração com outros sistemas.

#### Configuração da regra:

1. **When…**
   * **Document Type is Invoice**: Esta condição garante que a regra é acionada apenas para documentos categorizados como faturas, mantendo a especificidade do fluxo de trabalho na gestão de faturas.
2. **And…**
   * **Document Field Invoice Sub Type is Equals Cost Invoice**: Isto especifica que a regra se aplica apenas às faturas que estão explicitamente marcadas como "Cost Invoices" num determinado campo do documento. Isto ajuda a distingui-las de outros tipos de faturas.
   * **Document Status is Pending Second Approval**: A fatura tem de estar no estado "Pending Second Approval". Isto indica que a fatura já foi submetida a uma aprovação inicial e aguarda uma segunda revisão, possivelmente final.

#### Ação (Then…):

* **Start Export**: Assim que a fatura cumpre as condições especificadas (ser uma fatura de custo e estar pendente de segunda aprovação), é executada a ação "Start Export". Isto pode envolver o envio dos dados da fatura para outro sistema, para fins de análise financeira, relatórios ou conformidade.

#### Objetivo desta regra:

* **Workflow Efficiency**: Esta regra ajuda a automatizar o tratamento das faturas de custo, garantindo que são processadas através das fases de aprovação necessárias sem intervenção manual, aumentando a rapidez e a exatidão das operações financeiras.
* **Control and Compliance**: Ao exigir uma segunda aprovação, o sistema impõe um mecanismo de controlo que garante que as faturas de custo são minuciosamente revistas, reforçando a supervisão financeira.
* **Integration and Reporting**: A ação de exportação sugere que, assim que as faturas estiverem totalmente aprovadas, podem ser integradas noutros sistemas para processamento ou análise adicional, o que é fundamental para os relatórios financeiros e as auditorias.

Este tipo de regra é vital para as organizações que lidam com vários tipos de faturas e que precisam de garantir que cada tipo é tratado de acordo com protocolos específicos. Reduz o risco de erros e assegura a conformidade com os controlos internos e as regulamentações externas.
