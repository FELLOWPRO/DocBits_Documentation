# Fatura de Custo - Exportar

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_4.png" alt="DocBits Compra Pedido Exportar 4"><figcaption></figcaption></figure>

Este título indica que a regra é configurada especificamente para gerenciar faturas de custo e envolve uma ação de exportação, possivelmente para relatórios, processamento adicional ou integração com outros sistemas.

#### Configuração da Regra:

1. **Quando…**
* **Tipo de Documento é Fatura**: Esta condição garante que a regra seja acionada apenas para documentos categorizados como faturas, mantendo a especificidade do fluxo de trabalho para o gerenciamento de faturas.
2. **E…**
* **Subtipo de Fatura é Igual a Fatura de Custo**: Isso especifica que a regra se aplica apenas a faturas marcadas explicitamente como "Faturas de Custo" em um campo específico dentro do documento. Isso ajuda a distingui-las de outros tipos de faturas.
* **Status do Documento é Pendente de Segunda Aprovação**: A fatura deve estar em status de "Pendente de Segunda Aprovação". Isso indica que a fatura já passou por uma aprovação inicial e está aguardando uma segunda, possivelmente final, revisão.

#### Ação (Então…):

* **Iniciar Exportação**: Uma vez que a fatura atende às condições especificadas (sendo uma fatura de custo e pendente de segunda aprovação), a ação de "Iniciar Exportação" é executada. Isso pode envolver o envio dos dados da fatura para outro sistema para análise financeira, relatórios ou fins de conformidade.

#### Objetivo Dessa Regra:

* **Eficiência do Fluxo de Trabalho**: Esta regra ajuda a automatizar o tratamento de faturas de custo, garantindo que sejam processadas pelas etapas de aprovação necessárias sem intervenção manual, aumentando a velocidade e precisão das operações financeiras.
* **Controle e Conformidade**: Ao exigir uma segunda aprovação, o sistema aplica um mecanismo de controle que garante que as faturas de custo sejam revisadas minuciosamente, aprimorando a supervisão financeira.
* **Integração e Relatórios**: A ação de exportação sugere que, uma vez que as faturas sejam totalmente aprovadas, elas possam ser integradas a outros sistemas para processamento ou análise adicionais, o que é fundamental para relatórios financeiros e auditorias.

Esse tipo de regra é vital para organizações que lidam com vários tipos de faturas e precisam garantir que cada tipo seja tratado de acordo com protocolos específicos. Isso reduz o risco de erros e garante conformidade com controles internos e regulamentações externas.
