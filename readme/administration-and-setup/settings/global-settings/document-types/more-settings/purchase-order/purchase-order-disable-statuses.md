# Estados de desativação de pedidos de compra

## **Visão Geral**

A configuração **Statuses de Desativação de PO** permite que os usuários especifiquem statuses de pedidos de compra (PO) que impedem que faturas sejam correspondidas a esses POs. Se um pedido de compra tiver um status listado nesta configuração, ele **não pode** ser usado para correspondência de faturas na tela de correspondência de PO, interrompendo o processamento de faturas relacionadas até que o status do PO mude para um que não esteja desativado.\
\
Ao usar esta configuração, os usuários podem garantir que pedidos de compra com statuses específicos não passem por processamento adicional de faturas, reduzindo erros e prevenindo pagamentos desnecessários.

## **Passos de Ativação**

1.  Vá para **Configurações → Configurações Globais → Tipos de Documentos**

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt="Navegação de configurações do DocBits em espanhol com os grupos Global Settings e Document Processing e as entradas de informações da empresa e permissões de utilizador"><figcaption></figcaption></figure>
2.  Selecione o tipo de documento desejado e clique em **Mais Configurações**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt="Página de Document Types com a lista de Invoice, Credit Note, Delivery Note, Order Confirmation e Contract e os separadores Edit layout, Document Sub Types, Table columns e Fields"><figcaption></figcaption></figure>
3.  Na seção **Pedido de Compra**, navegue até a opção **Statuses de Desativação de PO**.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_3.png" alt="Página More Settings para tipos de documentos com a secção Purchase Order e a opção PO disable statuses destacada"><figcaption></figcaption></figure>

### **Como Identificar um Pedido de Compra Desativado**

Na tela de **Correspondência de PO**, um pedido de compra desativado aparece **riscado**. Isso indica visualmente que o PO está atualmente restrito de ser correspondido devido ao seu status.

<figure><img src="../../../../../../.gitbook/assets/disable_po_status_6.png" alt="Tabela do ecrã de PO Matching com as colunas LINE NUMBER, ITEM ID, STATUS, QUANTITY, UNIT PRICE e MATCHED QUANTITY"><figcaption></figcaption></figure>

### **Como configurá-lo**

1. Na configuração **Statuses de Desativação de PO**, você verá um campo de seleção no lado esquerdo.
2.  Clicar neste campo abre uma lista suspensa de statuses de PO disponíveis.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_4.png" alt="Lista pendente de estados de desativação de PO com Canceled, Deleted, Invoiced, Open, Partially Invoiced, Partially Received, Received, Rejected, Unapproved, Hold e Closed" width="372"><figcaption></figcaption></figure>
3. Selecione um ou mais statuses clicando neles. Clique novamente para desmarcar.
4.  Clique no botão **Aplicar** para salvar suas alterações.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_5.png" alt="Definição dos estados desativados do PO com os valores selecionados Canceled, Deleted e Invoiced, e o botão Apply"><figcaption></figcaption></figure>

**Statuses Disponíveis**

* Cancelado
* Excluído
* Faturado
* Aberto
* Parcialmente Faturado
* Parcialmente Recebido
* Recebido
* Rejeitado
* Não Aprovado
* Hold
* Fechado
