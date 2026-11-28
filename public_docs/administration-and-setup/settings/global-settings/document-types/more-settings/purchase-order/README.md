# Ordem de compra

O cartão **Purchase Order** nas **More Settings** de um tipo de documento controla como documentos desse tipo são correspondidos com ordens de compra. As configurações valem para um tipo de documento por vez, então abra primeiro o tipo de documento que deseja alterar em **Settings → Document Types**.

Para encontrar as configurações de uma fatura:

1. Abra **Settings → Document Types**.
2. Localize o cartão **Invoice** e selecione o ícone de engrenagem (**More Settings**).
3. Abra a seção **Purchase Order** para revisar as opções de correspondência e validação.

<figure><img src="../../../../../../.gitbook/assets/dbdc226228-invoice-card-en-20261030.png" alt="English Invoice document type card with the More Settings gear at the upper right"><figcaption><p>O cartão Invoice no ambiente de teste Dev em inglês atual. Use o ícone de engrenagem para abrir as More Settings; os demais controles se aplicam ao tipo de documento.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/dbdc226-po-section-en-20261030.png" alt="Closed Purchase Order section labelled PO Matching and Validation"><figcaption><p>A seção Purchase Order nas More Settings, mostrada fechada. Expanda o cabeçalho para ver as opções; nenhuma configuração foi alterada para esta captura.</p></figcaption></figure>

Comece pelas regras de correspondência e pelas tolerâncias e depois ajuste o comportamento em torno da correspondência e da exportação:

* [Regras de Correspondência de Pedido de Compra](purchase-order-matching-rules.md) e [Configurações de tolerância de pedido de compra / Tolerância adicional de pedido de compra](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) definem como as linhas de fatura e de pedido são comparadas.
* [Opções de Auto Match & Export](auto-match-and-export-options.md), [Exportar linhas de PO não correspondidas](export-not-matched-po-lines.md) e [Exportação Alternativa](alternate-export.md) cobrem o que acontece depois de uma correspondência.
* [Quantidade exportada na unidade de medida base](export-quantity-in-base-unit-of-measure.md) converte a quantidade e o preço unitário exportados para a unidade de medida base, para a exportação para o Infor LN.
* [Tabela de PO no Construtor de Layout](po-table-in-layout-builder.md), [Status da linha de PO consumida](consumed-po-line-status.md) e [Calcular preço unitário do PO](calculate-po-unit-price.md) alteram o que os usuários veem na vista de correspondência.
* [Verificação automática de atualizações de PO](auto-check-for-po-updates.md), [Estados de desativação de pedidos de compra](purchase-order-disable-statuses.md) e [Atualizar Status do Pedido de Compra do Documento](update-document-purchase-order-status.md) controlam como os dados e os status da ordem de compra permanecem atualizados.
* [Mapa de Números de Itens do Fornecedor - Documentação do Administrador](supplier-item-number-map-admin-documentation.md) e a página geral [Ordem de compra](purchase-order.md) trazem mais contexto.

As configurações podem afetar documentos em produção. Verifique as alterações com um documento de teste antes de salvá-las em produção.

Esta visão geral mostra onde encontrar as configurações. Ela não verifica uma correspondência de PO nem uma exportação concluídas.
