# Opções de Auto Match & Export

Três configurações no final do cartão **Ordem de compra** decidem quem vê os atalhos de correspondência de PO e quais documentos podem ser exportados por conta própria após uma correspondência. Elas se aplicam a um tipo de documento por vez.

<figure><img src="../../../../../../.gitbook/assets/doc-type-settings-po-options-pt.png" alt="O cartão Ordem de compra das configurações do tipo de documento com todas as opções de PO"><figcaption><p>O cartão Ordem de compra. As três opções abaixo são as três últimas linhas.</p></figcaption></figure>

## Permitir exportação automática para linhas de PO não correspondentes

A exportação automática após a correspondência de PO normalmente exige um documento **totalmente correspondido**. Quando este interruptor está ativado, os documentos cujo status é **Nenhuma linha de PO correspondente** também podem ser exportados automaticamente. Esse status significa que o pedido de compra não tem linhas às quais a fatura possa ser correspondida.

* **Desligado (padrão):** somente os documentos totalmente correspondidos são exportados automaticamente.
* **Ligado:** os documentos totalmente correspondidos e os documentos sem linhas de PO correspondentes são exportados automaticamente.

O interruptor só tem efeito quando os documentos são exportados automaticamente, por exemplo com [**Exportação automática se o pedido de compra corresponder 100%**](../../../../document-processing/module/auto-export-if-po-matched-100.md) ou um cartão de exportação do DocFlow. Ele não altera a forma como as linhas são correspondidas.

## A correspondência automática e a exportação ficam visíveis para

A tela de correspondência de PO tem uma ação **Auto Match & Export**. Ela corresponde o documento e o exporta logo após a correspondência. Esta configuração controla quem recebe a ação:

| Valor | Quem vê a ação |
| ----- | -------------- |
| **Somente o administrador** (padrão) | Administradores |
| **Todos os usuários** | Todo usuário que pode abrir a tela de correspondência de PO |

Os administradores sempre veem a ação. A configuração não ativa o recurso. O módulo [**Exportação automática se o pedido de compra corresponder 100%**](../../../../document-processing/module/auto-export-if-po-matched-100.md) precisa estar ativo para a organização.

## Use o valor líquido das linhas para o total correspondente visível para

A tela de correspondência de PO pode calcular o **Total correspondido** a partir do **Valor líquido** das linhas de fatura correspondidas, em vez de computá-lo. Esta configuração controla quem pode ativar esse cálculo:

| Valor | Quem vê o interruptor |
| ----- | --------------------- |
| **Somente o administrador** (padrão) | Administradores |
| **Todos os usuários** | Todo usuário que pode abrir a tela de correspondência de PO |

Quando o interruptor está ativado, o Total correspondido usa diretamente os valores do Valor líquido das linhas de fatura correspondidas.
