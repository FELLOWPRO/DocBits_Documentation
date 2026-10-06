# Status da linha de PO consumida

**Status da linha de PO consumida** colore as linhas do pedido de compra (PO) na tela de correspondência de acordo com a quantidade de cada linha que já foi correspondida. Ative essa opção para o tipo de documento usado nas suas faturas se a sua equipe precisa identificar rapidamente as linhas de PO não usadas, parcialmente usadas e totalmente usadas. A cor é apenas uma ajuda visual; verifique a **Quantidade correspondida** e a coluna de quantidade de PO selecionada antes de decidir se uma linha pode ser correspondida novamente.

## Ativar a configuração

1. Abra **Configurações → Tipos de documentos**. Encontre o tipo de documento usado para as suas faturas e selecione a engrenagem no seu cartão para abrir **Mais configurações**. A captura de tela mostra o cartão **Fatura**. Deixe as chaves **Ativar** e **Extraction** como estão.

   <figure><img src="../../../../../../.gitbook/assets/1-consumed-po-line-document-types-pt.png" alt="Página Tipos de documentos com o cartão Fatura e sua engrenagem de Mais configurações"><figcaption><p>Abra Mais configurações a partir do cartão Fatura.</p></figcaption></figure>

2. Expanda **Ordem de compra** se estiver recolhida. Encontre **Status da linha de PO consumida** e ative a sua chave. Essa é uma configuração separada de **Atualizar status do pedido de compra do documento**, mais abaixo na mesma seção.

   <figure><img src="../../../../../../.gitbook/assets/2-consumed-po-line-settings-pt.png" alt="Seção Ordem de compra de Mais configurações com a chave Status da linha de PO consumida visível"><figcaption><p>Escolha a chave Status da linha de PO consumida.</p></figcaption></figure>

   <figure><img src="../../../../../../.gitbook/assets/3-consumed-po-line-toggle-pt.png" alt="Vista aproximada do rótulo Status da linha de PO consumida e da sua chave"><figcaption><p>Neste exemplo a chave está desligada; ligue-a para mostrar as cores de correspondência.</p></figcaption></figure>

3. Abra uma fatura com correspondência de pedido de compra e inspecione as suas linhas de PO. Os exemplos abaixo mostram como as cores das linhas se relacionam com o estado de correspondência. Para as etapas de correspondência, veja [Correspondência de Pedidos de Compra](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md).

## Ler as cores das linhas de PO

| Aparência | Significado | O que verificar |
| --- | --- | --- |
| Sem cor ou branca | Nenhuma quantidade nesta linha de PO foi correspondida ainda. | Verifique a quantidade da PO e a linha da fatura antes de correspondê-la. |
| Tom azul | Você selecionou a linha na tela de correspondência atual. | A seleção é temporária; não significa que a linha esteja totalmente correspondida. |
| Laranja claro | Parte da quantidade foi correspondida, mas a quantidade correspondida é inferior à quantidade de PO selecionada. | Verifique quanta quantidade ainda resta. |
| Violeta claro | A quantidade correspondida é pelo menos a quantidade de PO selecionada. | Não presuma que há mais quantidade disponível. |

<figure><img src="../../../../../../.gitbook/assets/image (470).png" alt="Linha de PO com quantidade correspondida zero e sem cor de status"><figcaption><p>Nenhuma quantidade foi correspondida ainda.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (472).png" alt="Linha de PO com tom azul de seleção na tela de correspondência"><figcaption><p>A linha está selecionada para a correspondência atual.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/consumed_po_line_status.png" alt="Linha de PO com fundo laranja claro e quantidade correspondida inferior à quantidade da PO"><figcaption><p>A linha está parcialmente usada.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (473).png" alt="Linha de PO com fundo violeta claro e quantidade correspondida igual à quantidade da PO"><figcaption><p>A linha está totalmente usada.</p></figcaption></figure>

Uma linha riscada tem um significado diferente: o status da PO dela pode estar excluído por [Status de desativação de PO](purchase-order-disable-statuses.md). Verifique essa configuração se uma linha não puder ser selecionada.
