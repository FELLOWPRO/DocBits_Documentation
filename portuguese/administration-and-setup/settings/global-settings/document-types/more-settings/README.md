# Mais Configurações

## Visão Geral

Na seção "Mais Configurações", você pode encontrar várias opções relacionadas a tipos de documentos individuais. Uma vez que uma configuração é ativada, ela se aplicará apenas a esse tipo específico de documento. Esta página fornece uma breve visão geral do que cada configuração faz.

## Como Acessar

1.  Navegue até **Configurações** → **Configurações globais** → **Tipos de documentos**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Selecione o tipo de documento desejado e clique em **Mais Configurações**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>

## Extração de Tabelas

* **Ignorar validação de tabela**: Permite ignorar o processo de validação padrão para dados de tabela. Esta opção é útil em cenários onde é necessário um manuseio de dados flexível ou quando certos passos de validação podem ser pulados para melhorar o desempenho durante o processamento de dados.

## Detecção de Duplicados

* [**Detecção de Documentos Duplicados**](duplicate-document-handling.md): Isso permite que você detecte e gerencie documentos duplicados.

## Em Revisão

* **Design em forma de revisão**: Configure o layout dos formulários de revisão usando o **Construtor de layout**. Este layout determina como o conteúdo é apresentado durante o processo de revisão do documento. Para instruções detalhadas sobre como usar o **Construtor de layout**, clique [aqui](../../../../setup/document-types/layout-builder.md).

## Rejeitar

* **Formulário de rejeição de design**: Configure o layout usando o **Construtor de layout** para o formulário de rejeição exibido durante o processo de revisão do documento. Para instruções detalhadas sobre como usar o **Construtor de layout**, clique [aqui](../../../../setup/document-types/layout-builder.md).

## Exportar Formato PDF

* **Formato de Arquivo de Exportação**: Permite que você especifique o formato PDF a ser usado ao exportar documentos.

## Aprovação

* **Aprovar antes de exportar**: Garante que os documentos devem ser aprovados antes de serem exportados do sistema. Você também pode configurar o layout da tela de aprovação usando o **Construtor de layout**. Para instruções detalhadas sobre como usar o **Construtor de layout**, clique [aqui](../../../../setup/document-types/layout-builder.md).
* **Aprovar antes da exportação V2**: Ativa a Aprovação V2, que suporta o uso de campos dinâmicos em vez de estáticos. Você também pode personalizar o layout da tela de aprovação usando o **Construtor de layout**. Para instruções detalhadas sobre como usar o **Construtor de layout**, clique [aqui](../../../../setup/document-types/layout-builder.md).
* **Segunda Aprovação**: Adiciona uma camada adicional de aprovação para validação aprimorada e maior controle sobre o processamento de documentos. Você também pode personalizar o layout da tela de aprovação usando o **Construtor de layout**. Para instruções detalhadas sobre como usar o **Construtor de layout**, clique [aqui](../../../../setup/document-types/layout-builder.md).
* [**Selo de Aprovação**](approval/approval-stamp.md): Adiciona um selo ao documento quando ele é aprovado.
* [**Histórico de Aprovação**](approval/approval-history.md): Permite a exibição do histórico de aprovação tanto na tela de aprovação quanto na validação de campos.

## Ordem de Compra

* [**Tabela de OC no construtor de layout**](purchase-order/po-table-in-layout-builder.md): Permite a inclusão de tabelas de ordem de compra no construtor de layout para layouts de documentos personalizados.
* [**Verificação automática de atualizações de OC**](purchase-order/auto-check-for-po-updates.md): Quando ativado, o sistema exibe um indicador visual na tela de Correspondência de Ordem de Compra para mostrar quando uma ordem de compra foi atualizada, solicitando aos usuários que atualizem para as informações mais recentes.
* **Atualizar dados da OC automaticamente**: Ativar isso atualizará automaticamente os dados da OC quando novos dados estiverem disponíveis.
* [**Status da linha da OC consumida**](purchase-order/estado-da-linha-de-po-consumida.md): Esta configuração melhora a tela de Correspondência de Ordem de Compra aplicando codificação de cores às linhas da ordem de compra.
* [**Calcular preço unitário do pedido de compra**](purchase-order/calculate-po-unit-price.md): Isso permite que você calcule o preço unitário da OC usando o valor líquido e a quantidade, em vez de extraí-lo.
* [**Ordem de Compra**](purchase-order/purchase-order.md): Alterna se o documento deve ser processado na tela de Correspondência de Ordem de Compra. Você também pode especificar qual termo de quantidade o processo de correspondência deve ser baseado.
* [**Exportar linhas de OC não correspondidas**](purchase-order/export-not-matched-po-lines.md): Este recurso controla a exportação de linhas de ordem de compra. Quando desativado, apenas linhas correspondidas são exportadas. Quando ativado, todas as linhas de ordem de compra são exportadas, mesmo que não estejam correspondidas a uma linha de confirmação de pedido.
* [**Configuração de Tolerância da OC**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md): Este recurso permite que você defina níveis de tolerância para quantidade e preço unitário, acomodando pequenas discrepâncias sem marcá-las como incompatibilidades.
* [**Configuração Adicional de Tolerância da OC**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md#configuracao-para-configurar-configuracoes-adicionais-de-tolerancia-de-pedido-de-compra): Este recurso permite que você defina níveis de tolerância adicionais para frete, encargos e impostos, acomodando pequenas discrepâncias sem marcá-las como incompatibilidades.
* [**Exportação Alternativa**](purchase-order/alternate-export.md): Isso permite que você configure uma exportação alternativa para status específicos.
* [**Desativar status da OC**](purchase-order/purchase-order-disable-statuses.md): Permite que você desative status específicos de serem considerados no processo de correspondência.
* **Ignorar Linhas Já Correspondidas**: Ativar isso pulará linhas que já foram correspondidas durante um novo processo de correspondência.
* [**Atualizar status do pedido de compra do documento**](purchase-order/update-document-purchase-order-status.md): Quando ativado, a coluna **Status do PO** no painel é atualizada automaticamente sempre que o status do pedido de compra é alterado.
* [**Mapa de Números de Item do Fornecedor**](purchase-order/supplier-item-number-map-admin-documentation.md): Uma configuração utilitária que mapeia números de itens do fornecedor para números de itens internos, garantindo precisão na gestão de inventário e ordens de compra.
