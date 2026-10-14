# Calcular preço unitário do PO

## **Visão geral**

Você pode optar por calcular automaticamente o **preço unitário** de cada linha do pedido de compra a partir do **valor** e da **quantidade** da linha, em vez de usar o preço unitário que veio com o pedido de compra. Isso é particularmente útil quando o preço unitário no pedido de compra (no Infor ERP / SAP) difere do preço no documento. Tais discrepâncias podem ocorrer se um desconto for aplicado ao preço unitário no pedido de compra, enquanto o documento aplica o desconto apenas ao valor líquido.

## **Passos para ativação**

1.  Navegue até **Configurações** -> **Configurações Globais** -> **Tipos de Documento**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Selecione o tipo de documento desejado e clique em **Mais Configurações**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  Na seção **Pedido de Compra**, ative a opção **Calcular Preço Unitário do PO**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_3.png" alt=""><figcaption></figcaption></figure>

## Como o preço é calculado

Uma vez que a configuração esteja ativada, o preço unitário de uma linha do pedido de compra é calculado como:

**`Preço Unitário = Valor da Linha ÷ Quantidade × Preço Unitário Por`**

onde o **valor da linha** é escolhido da seguinte forma:

| A linha do pedido de compra contém                                                           | Valor da linha usado                   |
| -------------------------------------------------------------------------------------------- | -------------------------------------- |
| um **valor líquido** (`extended_amount`) que é maior que 0 e não superior ao total da linha  | o valor líquido                        |
| sem valor líquido, ou valor líquido acima do total da linha                                  | o **total** da linha (`total_amount`)  |
| sem valor positivo algum, ou sem quantidade positiva                                         | nada é calculado, o preço do PO permanece |

Por que o valor líquido vem primeiro: os feeds do ERP (Infor BODs) enviam o valor líquido da linha como `extended_amount` e carregam **impostos e encargos adicionais** em `total_amount`. Dividir um total com imposto pela quantidade gera um preço unitário bruto, e toda fatura que é precificada líquida então aparece como _preço unitário subestimado_, embora esteja correto. Exemplo de uma linha real de pedido de compra: quantidade 9, valor líquido 879,84, total 954,63 (8,5% de imposto) — o preço baseado no líquido é 97,76 e corresponde à fatura; o preço baseado no total seria 106,07.

Um valor líquido que é **maior** que o total da linha não pode ser um valor líquido, então o total é usado nesse caso. Um `Preço Unitário Por` de 0 ou vazio conta como 1.

{% hint style="info" %}
O preço calculado é gravado no snapshot do pedido de compra que é armazenado no documento, e é **recalculado toda vez que o documento é conciliado** (Auto PO Match, conciliação manual, conciliação ao salvar). Um documento que foi conciliado antes da alteração da configuração, portanto, adota o novo preço na próxima conciliação — não é necessário recarregar o pedido de compra.
{% endhint %}

## Exemplo:

<figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_4.png" alt="" width="563"><figcaption></figcaption></figure>

Neste caso, o preço unitário (sem o desconto) é extraído do documento, enquanto o pedido de compra no ERP armazena o preço unitário com o desconto aplicado. Isso resulta em uma discrepância no preço unitário. Com a configuração ativada, o preço unitário é obtido a partir do valor da linha e da quantidade, assim ambos os lados concordam.

## Configurações relacionadas

* [Regras de Conciliação de Pedido de Compra](purchase-order-matching-rules.md) — as regras comparam o preço unitário **efetivo**, que é este preço calculado quando a configuração está ativada.
* [Configurações de Tolerância de Pedido de Compra](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) — o quanto o preço da fatura pode divergir do preço calculado.