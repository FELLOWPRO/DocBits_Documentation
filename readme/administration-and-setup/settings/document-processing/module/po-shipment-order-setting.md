# Configuração do Pedido de Envio de PO

## **Visão Geral**

A seção **Pedido de Envio de PO** fornece uma análise do status de entrega e faturamento dos itens do Pedido de Compra correspondentes. Esta seção aparece dentro da tela de **Correspondência de Pedido de Compra** quando o recurso está habilitado.

## **Como Habilitar**

Para ativar este recurso:

1. Vá para **Configurações** → **Módulo**.
2. Abra a seção **Ordem de compra** (*Conciliação e Validação de Pedidos de Compra*).
3.  Ative a opção **Ordem de Remessa de PO**.

    <div align="left"><figure><img src="../../../../.gitbook/assets/po-shipment-order-module-setting-pt.png" alt="Seção Ordem de compra em Configurações → Módulo com o interruptor Ordem de Remessa de PO" width="563"><figcaption><p>Configurações → Módulo → Ordem de compra</p></figcaption></figure></div>

A mesma seção contém mais dois interruptores: **Painel de PO** adiciona à navegação um painel de pedidos de compra, e **Painel de Pedidos de Remessa** adiciona um painel de pedidos de remessa que lista as entregas recebidas por item do pedido de compra.

## **Onde Aparece**

Uma vez habilitada, a seção Ordem de Remessa de PO se torna visível na interface de Correspondência de Pedido de Compra.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2R9tB3JySdIMk8meRSVZ%252FPO-Shipment-Order-1.jpg%3Falt%3Dmedia%26token%3D70aa50f4-84cd-4a55-b580-037b893d1f5b\&width=768\&dpr=4\&quality=100\&sign=e4619335\&sv=2)

### **Ordem de Remessa de PO – Descrições dos Campos**

* **ID do Item** Identifica o item específico no pedido de compra.
* **Número de Entrega** Número de referência para o envio ou entrega.
* **Quantidade Enviada** Quantidade que foi entregue ou recebida.
* **Quantidade Faturada** Quantidade que já foi faturada.
* **Quantidade em Aberto para Faturamento** Quantidade ainda em aberto para faturamento (calculada como _Quantidade Enviada - Quantidade Faturada_).
* **Barra de Progresso e Porcentagem**
  * Mostra quanto da quantidade enviada foi correspondida com faturas.
  * Começa em 0% para novos POs.
  * Atualiza cumulativamente em várias faturas.
  * Reflete o progresso total de itens faturados versus enviados.
* **Data de Entrega Prometida** A data de entrega esperada para o item do PO.
*   **Indicador de Atraso**

    Mostra o número de dias de atraso na entrega com base na **Data de Entrega Prometida**.
