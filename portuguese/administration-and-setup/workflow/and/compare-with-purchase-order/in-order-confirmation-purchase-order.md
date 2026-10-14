---
hidden: true
---

# Compare uma confirmação de pedido com um pedido de compra

Use **Compare with Purchase Order** no Workflow Builder quando uma confirmação de pedido precisar ser verificada em relação ao respectivo pedido de compra. Adicione o cartão em **And...** e escolha os dados do pedido, um operador e o que deve acontecer com o resultado. As capturas de tela abaixo mostram duas versões de cartão disponíveis na interface em inglês. Os campos ainda são marcadores; defina-os para o seu workflow antes de salvar.

## Gravar o resultado em um campo

<figure><img src="../../../../.gitbook/assets/dbdc-133-workflow-card-write-text.png" alt="Cartão Compare with Purchase Order no Workflow Builder com os campos Order Data, Operator, Text, Field Name e Result of condition." width="563"><figcaption>Versão 2: grava um texto em um campo com base no resultado da condição.</figcaption></figure>

Escolha os **Order Data** da confirmação de pedido e um **Operator** para a comparação com o pedido de compra. Informe o **Text** a gravar, selecione o **Field Name** e escolha o **Result of condition** que deve acionar a gravação.

## Comparar os dados

<figure><img src="../../../../.gitbook/assets/dbdc-133-workflow-card-compare-as.png" alt="Cartão Compare with Purchase Order no Workflow Builder com os campos Any/All, Order Data, Operator e Comparison Data." width="563"><figcaption>Versão 4: compara dados selecionados da confirmação de pedido com dados do pedido de compra.</figcaption></figure>

Escolha **Any/All** para definir se uma ou todas as condições selecionadas devem corresponder. Em seguida, selecione os **Order Data**, o **Operator** e os **Comparison Data** para a comparação com o pedido de compra.

Para as etapas relacionadas, consulte [Workflow](../../README.md) e [Compare with Purchase Order](README.md).
