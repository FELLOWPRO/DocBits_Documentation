# Tela de Correspondência de Ordem de Compra

Use a **Correspondência de PO** para comparar as linhas da ordem de compra carregadas para um documento com as linhas da fatura extraídas dele. Os dados da ordem de compra podem vir de uma integração com ERP ou de outra importação configurada. A tela mostra o documento ao lado das duas tabelas para que você confira números, quantidades, preços e diferenças antes de salvar ou exportar.

## Conferir as linhas da fatura com a encomenda

O percurso começa com um número de encomenda reconhecido e três linhas da fatura conciliadas. Depois mostra a pesquisa manual como exceção, uma ligação incorreta intencional, uma correspondência parcial, a correspondência automática e a gravação. Verifique o resultado após recarregar: guardar a correspondência não aprova nem exporta, por si só, a fatura.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-customer/v4/pt.mp4" %}

[Ver o vídeo com legendas](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-customer/v4/pt.html)

{% hint style="info" %}
A gravação utiliza dados de teste sintéticos com três linhas de fatura extraídas e a respetiva encomenda. O papel, as caixas de arquivo e a entrega totalizam 118 EUR líquidos. A correspondência completa mostra 118 EUR conciliados e nenhum valor em aberto.
{% endhint %}

<figure><img src="../../../.gitbook/assets/po-tutorial-v4-full-pt.png" alt="Correspondência completa: as três linhas estão ligadas, com 118 EUR conciliados e 0 EUR em aberto."><figcaption><p>Correspondência completa: as três linhas estão ligadas, com 118 EUR conciliados e 0 EUR em aberto.</p></figcaption></figure>

## Encontrar e inspecionar uma ordem de compra

1. Abra a fatura na **Correspondência de PO**. Quando o número da encomenda é reconhecido, o DocBits carrega a encomenda correspondente. Use a pesquisa manual se faltar o número ou para consultar outra encomenda.
2. Selecione o ícone de filtro ao lado da caixa de pesquisa para **Palavra-chave**, **Fornecedor**, **Status**, **Status do pedido**, datas, faixa de valor, ordenação e o número de registros exibidos. Selecione **Mais** para critérios adicionais. Selecione **Aplicar** para pesquisar ou **Claro** para redefinir os filtros.
3. Selecione um número de ordem de compra acima da tabela para inspecionar suas linhas. O ícone de atualização ao lado do número recarrega os dados dessa ordem. Uma recarga pode depender da integração configurada.
4. Compare cada linha da encomenda com a fatura e a tabela extraída. O **+** abre os detalhes de correspondência existentes; não liga, por si só, a linha à fatura.

<figure><img src="../../../.gitbook/assets/po-tutorial-v4-search-pt.png" alt="A pesquisa manual mostra as três linhas da encomenda de teste. Use os filtros quando necessário; um número de encomenda reconhecido não exige uma segunda pesquisa."><figcaption><p>A pesquisa manual mostra as três linhas da encomenda de teste. Use os filtros quando necessário; um número de encomenda reconhecido não exige uma segunda pesquisa.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/po-tutorial-v4-partial-pt.png" alt="Correspondência parcial: estão conciliados 50 EUR de papel e ficam 68 EUR em aberto. Não significa um limite fixo de cinquenta por cento."><figcaption><p>Correspondência parcial: estão conciliados 50 EUR de papel e ficam 68 EUR em aberto. Não significa um limite fixo de cinquenta por cento.</p></figcaption></figure>

## Corresponder linhas e revisar o resultado

Quando as duas tabelas contiverem linhas, conecte uma linha da fatura à linha correspondente da ordem de compra arrastando-a, ou use as ações de correspondência no menu de contexto da linha. **Correspondência Automática** tenta conectar as linhas elegíveis usando as regras da sua organização. Verifique o resultado antes de salvar: um número de item correspondente sozinho não prova que quantidade, preço ou condições de entrega concordam. Veja [Ferramentas de Correspondência de Ordem de Compra](purchase-order-matching-tools.md) para a barra de ferramentas, os controles de colunas e as ações manuais, e [Atalhos de Teclado](keyboard-shortcuts.md) para as ações por teclado.

Se um documento não for correspondido, leia o motivo exibido acima da área da ordem de compra. Ele pode dizer que o número da PO está ausente, que a ordem não foi encontrada, que suas linhas não estão disponíveis ou que a fatura não tem linhas extraídas. Corrija o documento ou a configuração indicada por esse motivo. Um administrador pode inspecionar as [regras de correspondência](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) e a [extração de tabelas](../../../administration-and-setup/settings/document-processing/classification-and-extraction/README.md) quando nenhuma linha de fatura aparecer.

Mensagens comuns e próximos passos:

| O que você vê | O que verificar |
| --- | --- |
| Nenhum número de ordem de compra | Digite ou corrija o número da PO no documento e salve. |
| Nenhuma ordem de compra foi encontrada | Verifique o número e se a ordem foi importada para esta organização. |
| A ordem foi encontrada, mas não está conectada | Tente a **Correspondência Automática** ou conecte as linhas manualmente depois de conferir as duas tabelas. |
| Nenhuma linha da ordem corresponde | Compare os valores da fatura com os da ordem e verifique o histórico de correspondência. |
| Nenhum item de linha da fatura | Verifique a [extração de tabelas](../../../administration-and-setup/settings/document-processing/classification-and-extraction/README.md) antes de tentar corresponder. |
| Nenhuma linha de ordem aberta | Verifique os [status de linha consumida](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/consumed-po-line-status.md) e os status excluídos. |

{% hint style="warning" %}
Salvar pode acionar a correspondência novamente após um número de PO alterado ou recém-detectado. Verifique o resultado exibido após salvar. Se uma correspondência não puder ser salva, leia o erro exibido na tela e peça a um administrador para verificar a [transformação](../../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) e as [regras de correspondência](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md).
{% endhint %}

Use o **Histórico de correspondência** (ícone de relógio, onde suas permissões permitirem) para inspecionar como uma correspondência anterior foi decidida. É uma visão somente leitura. Você pode revisar quais regras foram executadas e por que um candidato não correspondeu; abrir o histórico não exporta o documento.

### Mais de uma linha por correspondência

Uma única linha da fatura pode corresponder a várias linhas da ordem, ou o contrário, quando suas regras de correspondência permitirem. Abra os detalhes do **+** em uma linha para inspecionar qualquer correspondência múltipla existente. Verifique a quantidade e o preço combinados, não apenas uma linha. Um painel de detalhes vazio significa que não há correspondência múltipla para inspecionar. Veja [Ferramentas de Correspondência de Ordem de Compra](purchase-order-matching-tools.md) para alterar conexões.

### Quantidades, diferenças e descontos

Dependendo da configuração, a correspondência pode comparar a quantidade de entrega pedida, recebida ou restante, além do preço unitário, número do item e outros campos mapeados. Uma diferença pode ser aceita se o tipo de documento tiver uma tolerância configurada. Verifique a divergência exibida antes de aceitá-la. As [configurações de tolerância](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) e o [guia de descontos](discounts.md) explicam esses casos.

A área de totais, quando disponível, ajuda a conciliar o valor líquido da fatura com as linhas correspondidas e os encargos. Se permanecer um **Valor não liquidado**, inspecione os valores individuais das linhas e qualquer [elemento de custo](../../../administration-and-setup/settings/document-processing/classification-and-extraction/table-extraction-for-costing-element.md) antes de exportar.

## Conferir os totais e salvar

Revise a pré-visualização da fatura à direita e compare os totais das linhas e quaisquer encargos. Para uma explicação completa das ações na barra de ferramentas superior, veja [Ferramentas de Correspondência de Ordem de Compra](purchase-order-matching-tools.md). Selecione **Salvar** após alterar correspondências. Selecione **Exportar** somente depois de conferir o documento e o resultado da correspondência; a seta ao lado de Exportar mostra opções de exportação adicionais configuradas. Sua organização pode ter ações de exportação diferentes.

A barra de ferramentas da pré-visualização permite navegar entre as páginas do documento, aplicar zoom, baixar o original e abrir uma visão ampliada. Use-a para verificar se o número da ordem de compra e os valores das linhas realmente aparecem na fatura. Se você sair com alterações de correspondência não salvas, elas poderão ser perdidas.

As comparações disponíveis e os valores de tolerância dependem das configurações do seu tipo de documento. Leia [Regras de Correspondência de PO](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md), [Configurações de Tolerância](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md), [Status Desativados](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-disable-statuses.md) e [Status de Linha de PO Consumida](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/consumed-po-line-status.md) para as configurações de administrador. Para linhas de muitos para um, veja [Descontos](discounts.md) e as [Ferramentas de Correspondência](purchase-order-matching-tools.md).
