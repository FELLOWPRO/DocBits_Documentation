# Document Flow

O **Document Flow** mostra as etapas de processamento de um documento. Use-o para ver quais etapas foram concluídas, qual está em espera e quanto tempo o processamento levou. O exemplo abaixo usa uma fatura sintética no Sandbox em inglês.

## Abrir pelo dashboard

No **Dashboard**, localize o documento. Na coluna **Actions** dele, selecione os três pontos e depois **Document flow**. A opção abre o fluxo desse documento; ela não altera o documento.

<figure><img src="../../../.gitbook/assets/document-flow-dashboard-menu-en.png" alt="Dashboard em inglês com o menu Actions aberto para uma fatura sintética; Document flow aparece abaixo de Assign to."><figcaption>Escolha Document flow no menu Actions do documento.</figcaption></figure>

## Abrir pela Field Validation

Abra o documento. Na **Field Validation**, selecione os três pontos na barra de ações à direita e depois **Document Flow** em **More options**.

<figure><img src="../../../.gitbook/assets/document-flow-validation-menu-en.png" alt="Tela Field Validation em inglês mostrando o menu More options e o item Document Flow ao lado de uma fatura sintética."><figcaption>O mesmo fluxo está disponível na visualização do documento.</figcaption></figure>

## Ler o fluxo

O **Process Statistics**, à esquerda, resume o número de etapas, as etapas concluídas e em espera, as reinicializações, o tempo total, o status atual e o progresso geral. Cada cartão numerado mostra uma etapa de processamento e o respectivo estado atual. Role para baixo para ver as etapas seguintes.

<figure><img src="../../../.gitbook/assets/document-flow-overview-en.png" alt="Document Flow em inglês mostrando o Process Statistics à esquerda e os primeiros cartões de etapa numerados: Imported, Document Imported e OCR."><figcaption>As primeiras etapas do fluxo de uma fatura sintética.</figcaption></figure>

<figure><img src="../../../.gitbook/assets/document-flow-later-steps-en.png" alt="Document Flow em inglês após rolar para baixo; os cartões seguintes incluem Classification, Field Extraction, Table Extraction, Transformer, Metadata Populator, Lookup Data e Validator."><figcaption>Role para acompanhar a sequência pelas etapas seguintes.</figcaption></figure>

Selecione o cartão de uma etapa para abrir o **Step Details** à esquerda. Ele mostra o módulo e o status dele. Um painel **Task Logs** também pode abrir à direita; os detalhes do log dependem do que está disponível para essa tarefa. Selecione **×** em Step Details para fechar o painel.

<figure><img src="../../../.gitbook/assets/document-flow-step-details-en.png" alt="Document Flow em inglês com o cartão OCR selecionado; o Step Details abaixo do Process Statistics mostra Module OCR e Status Completed."><figcaption>O Step Details explica o status do módulo selecionado.</figcaption></figure>
