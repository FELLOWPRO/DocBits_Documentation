# Assistente de IA no editor de scripts

O editor de scripts tem um **Assistente de IA** integrado que escreve e explica scripts do DocBits por si. Descreva em linguagem simples o que o script deve fazer e o assistente responde com código Python que pode copiar para o editor.

{% hint style="info" %}
O Assistente de IA faz parte do **DocNet**. A sua organização precisa de uma subscrição DocNet ativa para o utilizar. Consulte [Plano de subscrição](../../subscription-plan/README.md) e [Módulos](../../../document-processing/module/README.md).
{% endhint %}

## Abrir o assistente

1. Vá a **Configurações → Tipos de documentos**, abra o tipo de documento e clique em **Roteiros**.
2. Clique em **Novo** ou abra uma versão de script existente como rascunho.
3. Clique no ícone de robô junto ao nome do script. O painel **Assistente de IA** abre-se no lado direito do editor.

## O que o assistente conhece

Com cada pergunta, o DocBits envia ao assistente:

* a **referência de scripting** (as funções descritas em [Scripting no DocBits](scripting-in-docbits/README.md)),
* o **tipo de documento** do script,
* o **script atual** do editor,
* os **nomes dos campos e as colunas de tabela** que a sua organização utiliza para este tipo de documento.

Graças aos nomes dos campos, o assistente utiliza os seus campos reais, por exemplo `invoice_date` ou `purchase_order`, em `get_field_value()` e `set_field_value()`.

## Escrever um script com o assistente

1. Escreva o seu pedido na caixa na parte inferior do painel, por exemplo: *Definir a moeda como EUR se estiver vazia.*
2. Prima **Enter** ou clique no ícone de envio. A resposta aparece em fluxo contínuo.
3. Clique no ícone de cópia (dica **Copiar para o editor**) junto a um bloco de código para colocar o código no editor de scripts.
4. Reveja o código, dê um nome ao script e guarde-o como rascunho.

As perguntas de seguimento funcionam no mesmo painel. Cole uma mensagem de erro ou pergunte *Porque é que este script não define a data de vencimento?* e o assistente analisa o script atual do editor.

## Verifique sempre o resultado

{% hint style="warning" %}
O assistente pode cometer erros. Leia o código gerado, verifique se os nomes dos campos correspondem ao seu tipo de documento e teste o script com um documento de teste antes de o ativar. Consulte [Testando Scripts](testing-scripts.md).
{% endhint %}

Os scripts só são executados com as funções de script aprovadas. Se um script chamar uma função que não existe, o DocBits rejeita-o com a mensagem *Unknown function*.

## Utilização e limites

* Cada resposta mostra, abaixo da resposta, o número de tokens utilizados (entrada, saída e total).
* A utilização é registada como utilização DocNet da sua organização.
* O DocBits rejeita o pedido quando a subscrição DocNet não existe (*DocNet subscription required*), expirou (*DocNet subscription expired*) ou a quota está esgotada (*DocNet quota exhausted*).

## Páginas relacionadas

* [Criando e Editando Scripts](creating-and-editing-scripts.md)
* [Funções de Campo](scripting-in-docbits/field-functions.md)
* [Scripts de Exemplo](scripting-in-docbits/sample-scripts/README.md)
* [Ativar e gerir scripts](script-activation-and-management.md)
