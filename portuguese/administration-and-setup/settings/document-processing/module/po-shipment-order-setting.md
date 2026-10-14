# Configuração do Pedido de Envio de PO

## **Visão Geral**

A seção **Pedido de Envio de PO** fornece uma análise do status de entrega e faturamento dos itens do Pedido de Compra correspondentes. Esta seção aparece dentro da tela de **Correspondência de Pedido de Compra** quando o recurso está habilitado.

## **Como Habilitar**

Para ativar este recurso:

1. Vá para **Configurações** → **Processamento de Documentos** → **Módulo**.
2. Selecione **Pedido de Compra**.
3.  Ative a opção **Pedido de Envio de PO**.

    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2ZdK2XuCIjc4Hz3W0s5H%252FPO-Shipment-Order-Setting.jpg%3Falt%3Dmedia%26token%3Dbe657223-f04e-4326-a284-bb29bae148e0&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=97986166&#x26;sv=2" alt="" width="563"></div>

## **Onde Aparece**

Uma vez habilitada, a seção Pedido de Envio de PO se torna visível na interface de Correspondência de Pedido de Compra.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2R9tB3JySdIMk8meRSVZ%252FPO-Shipment-Order-1.jpg%3Falt%3Dmedia%26token%3D70aa50f4-84cd-4a55-b580-037b893d1f5b\&width=768\&dpr=4\&quality=100\&sign=e4619335\&sv=2)

### **Pedido de Envio de PO – Descrições dos Campos**

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
