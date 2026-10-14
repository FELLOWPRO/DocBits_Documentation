# Then

## Visão geral dos cartões de ação "Then..."

Um cartão **Then** indica ao fluxo de trabalho o que fazer depois do gatilho **When** e das eventuais condições **And**. No **Workflow Builder**, selecione **Adicionar cartão** sob **Então...**. Escolha uma categoria à esquerda ou digite um nome em **Cartão de Pesquisa**. Selecione uma pré-visualização de cartão para adicioná-lo, preencha os campos mostrados no cartão e guarde o fluxo de trabalho. Desloque-se dentro do seletor para ver mais cartões. Selecione **×** para fechar sem adicionar um cartão. Veja [Fluxo de trabalho](../README.md) para a sequência completa.

As pré-visualizações abaixo mostram as ações disponíveis, não configurações já concluídas. Escolha a ação que corresponde ao resultado que pretende obter.

## Campo de documento

Defina ou inverta uma caixa de seleção, coloque texto num campo ou copie um campo para outro. Escolha os nomes dos campos e o valor solicitados pelo cartão. Veja [Campo de documento](document-field/README.md).

<figure><img src="../../../.gitbook/assets/then-category-document-field-pt.png" alt="Seletor de cartões Then em português com Campo de documento selecionado; as pré-visualizações mostram as ações de caixa de seleção, texto e cópia do campo."><figcaption>Altere um campo ou copie o seu conteúdo.</figcaption></figure>

## Documento

Escolha **Aprovar o Documento** ou **Rejeitar o documento** quando o fluxo de trabalho deve tomar essa decisão. Use primeiro uma condição **And** se a aprovação depender de uma verificação. Veja [Documento](document/README.md).

<figure><img src="../../../.gitbook/assets/then-category-document-pt.png" alt="Seletor de cartões Then em português com Documento selecionado; as pré-visualizações Aprovar o Documento e Rejeitar o documento estão visíveis."><figcaption>Aprove ou rejeite o documento atual.</figcaption></figure>

## Lógica

Use estes cartões para converter valores entre formato numérico, texto e booleano, ou para ler um valor de JSON. Escolha os campos de input e output no cartão selecionado.

<figure><img src="../../../.gitbook/assets/then-category-logic-pt.png" alt="Seletor de cartões Then em português com Lógica selecionado; as pré-visualizações visíveis convertem tipos de dados e leem valores de JSON."><figcaption>Transforme valores para um passo posterior do fluxo de trabalho.</figcaption></figure>

## Status

Escolha **Alterar status para** para levar o documento a um status selecionado. O cartão também pode acionar outro fluxo de trabalho. Veja [Status](status/README.md).

<figure><img src="../../../.gitbook/assets/then-category-status-pt.png" alt="Seletor de cartões Then em português com Status selecionado; a pré-visualização Alterar status para inclui um campo de status e um acionador de fluxo de trabalho opcional."><figcaption>Leve o documento a outro status.</figcaption></figure>

## Prompts e scripts

Escolha esta categoria para executar um script de prompt DocOperator. Selecione o script e as variáveis solicitados pelo cartão. O cartão também oferece definições de execução, como tentativas.

<figure><img src="../../../.gitbook/assets/then-category-prompts-scripts-pt.png" alt="Seletor de cartões Then em português com Prompts e scripts selecionado; uma pré-visualização de script de prompt DocOperator está visível."><figcaption>Execute um script de prompt DocOperator configurado.</figcaption></figure>

## Exportar

Inicie uma exportação, exporte com uma configuração escolhida ou coloque uma exportação final na fila. Escolha a configuração de exportação e a opção de tarefas pendentes mostrada no seu cartão. Veja [Exportar](export/README.md).

<figure><img src="../../../.gitbook/assets/then-category-export-pt.png" alt="Seletor de cartões Then em português com Exportar selecionado; as pré-visualizações mostram exportação inicial, configurada, em fila e alternativa."><figcaption>Escolha quando e como o documento é exportado.</figcaption></figure>

## Tarefa

Crie uma tarefa ou notificação e atribua-a a um utilizador ou grupo. Introduza o título, a descrição, a prioridade e as definições de notificação solicitados pelo cartão. Alguns cartões fazem atribuição sequencial. Veja [Tarefa](task/README.md).

<figure><img src="../../../.gitbook/assets/then-category-task-pt.png" alt="Seletor de cartões Then em português com Tarefa selecionado; as pré-visualizações visíveis criam ou atribuem tarefas e notificações."><figcaption>Crie trabalho de acompanhamento para uma pessoa ou grupo.</figcaption></figure>

## E-mail

Envie um e-mail usando um modelo selecionado, para destinatários ou para grupos. Escolha o modelo e o destino no cartão.

<figure><img src="../../../.gitbook/assets/then-category-email-pt.png" alt="Seletor de cartões Then em português com E-mail selecionado; as pré-visualizações enviam um e-mail com modelo para destinatários ou grupos."><figcaption>Envie um e-mail com modelo.</figcaption></figure>

## Mesa

Altere entradas ou calcule valores numa tabela do documento. Selecione a tabela, as colunas, o operador e a coluna de resultado solicitados pelo cartão. Veja [Mesa](table/README.md).

<figure><img src="../../../.gitbook/assets/then-category-table-pt.png" alt="Seletor de cartões Then em português com Mesa selecionado; as pré-visualizações alteram entradas e calculam colunas de resultado."><figcaption>Atualize ou calcule dados da tabela.</figcaption></figure>

## Cessionário

Atribua o documento a um utilizador, grupo, destinatário ou sub-organização. Alguns cartões usam um campo ou uma tabela de decisão e oferecem um valor de recurso. Escolha o destino correto e o recurso no cartão selecionado. Veja [Cessionário](assignee/README.md).

<figure><img src="../../../.gitbook/assets/then-category-assignee-pt.png" alt="Seletor de cartões Then em português com Cessionário selecionado; as pré-visualizações visíveis atribuem a um utilizador, destinatário, grupo ou contacto do fornecedor."><figcaption>Encaminhe o documento para a próxima pessoa ou grupo responsável.</figcaption></figure>

## Ação

Execute outro fluxo de trabalho, envie uma solicitação HTTPS, faça uma chamada de API ou use o cartão de cálculo de aumento de custos. Estas ações podem afetar outros sistemas; pergunte ao seu administrador qual endpoint e definições usar. Veja [Ação](action/README.md).

<figure><img src="../../../.gitbook/assets/then-category-action-pt.png" alt="Seletor de cartões Then em português com Ação selecionado; as pré-visualizações mostram Executar fluxo de trabalho, solicitação HTTPS, chamada de API e cálculo de aumento de custos."><figcaption>Inicie outro fluxo de trabalho ou ação de integração.</figcaption></figure>
