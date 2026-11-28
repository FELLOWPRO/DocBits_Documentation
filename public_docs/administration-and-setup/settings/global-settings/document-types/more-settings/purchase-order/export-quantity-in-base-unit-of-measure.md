# Quantidade exportada na unidade de medida base

O seletor **Export quantity in base unit of measure** fica na seção **Purchase Order** das **More Settings** de um tipo de documento. Ele altera a quantidade e o preço unitário que a exportação para o Infor LN grava nas linhas de pedido correspondidas.

Abra-o em **Settings → Document Types**, selecione o ícone de engrenagem (**More Settings**) no tipo de documento e expanda **Purchase Order**.

## O que o seletor faz

* **Off:** o DocBits exporta a quantidade e o preço unitário na unidade da fatura.
* **On:** o DocBits converte a quantidade e o preço unitário de cada linha de pedido correspondida para a unidade de medida base dessa linha, usando o fator de conversão dela, e grava o código da unidade base em vez do código da unidade faturada.

Uma linha sem fator de conversão é exportada sem alteração, portanto um fator ausente não bloqueia a exportação.

{% hint style="info" %}
A conversão se aplica apenas à exportação para o Infor LN. Os demais destinos de exportação mantêm a unidade faturada.
{% endhint %}

## Quando usar

Ative o seletor quando a instância do Infor LN espera quantidades de pedido na unidade de medida base. A conversão usa o fator armazenado na linha de pedido, não um fator que o DocBits calcule a partir do cadastro de itens.

As configurações podem afetar documentos em uso. Verifique o resultado com um documento de teste antes de salvar a alteração em produção. O seletor altera os valores exportados; ele não altera como as linhas de fatura e de pedido são correspondidas.

## Páginas relacionadas

* [Ordem de compra](README.md)
* [Exportar linhas de PO não correspondidas](export-not-matched-po-lines.md)
* [Exportação Alternativa](alternate-export.md)

<!-- Documentation review 2026-11-27: switch label, help text and behaviour checked against DocBits_Web src/pages/Settings/Components/DocTypes/PO.vue on origin/sandbox-nova (DOP-53, commit feb262ab89, contained in the deployed NOVA build 11.24.8). -->
