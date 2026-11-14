# Modo de anotação

O Modo de anotação permite colocar notas diretamente num documento durante a validação. Pode editar, mover ou eliminar uma nota antes de descarregar um PDF anotado. O administrador tem de ativar primeiro a funcionalidade para a organização. Se um documento tiver anotações, estas são incluídas na **exportação para o IDM**.

## Ativar o modo de anotação

Um administrador abre **Configurações → Módulo → Integração De Documentos → Tipo de documento** e ativa **Modo de anotação**. Se não vir o botão de anotação durante a validação, peça a um administrador para verificar esta definição e o seu acesso.

<figure><img src="../../../../.gitbook/assets/dbdc-1317-annotation-mode-settings-pt-20261114.png" alt="Secção Tipo de documento em português com as opções Construtor de fluxo de trabalho e Modo de anotação ativado"><figcaption><p>A secção Tipo de documento em Configurações → Módulo → Integração De Documentos. Neste exemplo, o Modo de anotação está ativado.</p></figcaption></figure>

{% embed url="https://youtu.be/ay0gGtwlqRE" %}
Tutorial do modo de anotação do DocBits: adicionar notas na validação e descarregar com ou sem anotações
{% endembed %}

## Adicionar uma anotação durante a validação

1. Abra o documento no [ecrã de validação](../../../../end-user-and-partner-section/end-user-section/validation-screen/README.md).
2. Selecione o **balão de fala** na barra de ferramentas à direita. A dica apresenta **Ativar modo de anotação**. Selecione-o novamente para sair do Modo de anotação.
3. Arraste sobre a parte do PDF onde a nota deve aparecer. Surge uma pequena barra de ferramentas junto à área selecionada.
4. Selecione a **caneta** para abrir **Criar/Editar Anotação**. Introduza a nota em **Anotação-Texto**. Pode escolher o tipo de letra e o tamanho, usar **Negrito** ou *Itálico* e definir a **Cor do texto**. **Cancelar** fecha a caixa de diálogo sem aplicar o texto; **Salvar** aplica-o à anotação selecionada.
5. Utilize o botão **disquete** na barra de ferramentas da anotação para guardar a alteração. Utilize o botão **caixote do lixo** para eliminar a anotação, se já não for necessária.

<figure><img src="../../../../.gitbook/assets/dbdc-1317-annotation-mode-toolbar-pt-20261114.png" alt="Botão de balão de fala na barra de ferramentas de validação com a dica Ativar modo de anotação"><figcaption><p>Abra o Modo de anotação a partir da barra de ferramentas de validação.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/dbdc-1317-annotation-mode-edit-toolbar-pt-20261114.png" alt="Barra de ferramentas da anotação com caneta para editar, disquete para guardar e caixote do lixo para eliminar"><figcaption><p>A barra de ferramentas aparece depois de selecionar uma área no PDF.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/dbdc-1317-annotation-mode-dialog-pt-20261114.png" alt="Caixa de diálogo Criar/Editar Anotação com tipo de letra, tamanho, negrito, itálico, cor do texto, campo de texto vazio, Cancelar e Salvar"><figcaption><p>Escreva e formate a nota na caixa de diálogo da anotação. Nesta imagem o campo de texto está vazio.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/dbdc-1317-annotation-mode-dialog-filled-pt-20261114.png" alt="Caixa de diálogo da anotação com o texto de exemplo Verifique este valor. introduzido antes de guardar"><figcaption><p>Reveja a nota antes de selecionar Salvar. O texto «Verifique este valor.» é um exemplo inventado e não dados reais.</p></figcaption></figure>

## Gerir uma anotação existente

Selecione uma nota no Modo de anotação para mostrar a sua barra de ferramentas. Utilize a **caneta** para alterar o texto ou a formatação, arraste a nota selecionada para a mover ou utilize o **caixote do lixo** para a eliminar. Pode criar várias anotações no mesmo documento. As anotações só estão visíveis enquanto o Modo de anotação está ativo e aparecem no PDF depois de guardadas. O botão de balão de fala não mostra se um documento já tem notas; ative o Modo de anotação para as ver.

<figure><img src="../../../../.gitbook/assets/dbdc-1317-annotation-mode-saved-pt-20261114.png" alt="Nota guardada com o texto de exemplo Verifique este valor. numa fatura sintética, com os botões editar, guardar e eliminar por baixo"><figcaption><p>Uma nota guardada continua visível no documento enquanto o Modo de anotação está ativo.</p></figcaption></figure>

As anotações também estão disponíveis durante a [aprovação de documentos](../../global-settings/document-types/more-settings/approval/README.md), onde pode vê-las, adicioná-las e alterá-las. Para a saída através do Infor IDM, consulte [Exportar para o IDM](../../../../infor-integration-and-configuration/exporting-to-infor/exporting-to-idm.md).

## Descarregar o PDF original ou o PDF anotado

No **Painel**, abra o menu de ações de três pontos do documento. Escolha **Download** para o PDF original ou **Baixar PDF anotado** para a versão com as notas guardadas. A opção anotada aparece depois de uma anotação ter sido guardada. O menu oferece também **Validar** (abrir o ecrã de validação), **Atribuir a** (escolher uma pessoa), **Fluxo de documentos** (ver o [fluxo de documentos](../../../../end-user-and-partner-section/end-user-section/dashboard/document-flow.md)), **Reiniciar** (processar o documento novamente), **Registos de documentos** (ver a atividade) e **Excluir** (remover o documento). Utilize estas ações apenas quando pretender alterar ou inspecionar o documento.

<figure><img src="../../../../.gitbook/assets/dbdc-1317-annotation-mode-download-menu-pt-20261114.png" alt="Menu de ações do Painel com Download para o PDF original e Baixar PDF anotado para as notas guardadas"><figcaption><p>Escolha a versão do PDF de que precisa no menu de ações do documento.</p></figcaption></figure>
