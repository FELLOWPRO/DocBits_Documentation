# Barra de ferramentas e Tela

## Vídeo: Construtor e canvas

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/pt.mp4" %}

[Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/pt.vtt) · 1:55

<details>
<summary>Transcrição</summary>

**Uma fatura com dois percursos**

Este é um workflow avançado real no DocBits. Uma verificação do montante da fatura conduz a duas ações. As ligações determinam qual a ação executada. O exemplo utiliza um rascunho não guardado e campos de demonstração.

**Configurar a verificação**

Abra Adicionar, escolha And e selecione uma condição de campo do documento. Indique o campo do montante, escolha Maior que e introduza mil. Utilize a chave exata do campo definida na configuração do documento.

**Configurar as ações**

Adicione dois cartões Then. Ambos definem o campo de demonstração approval route. Um escreve Approval e o outro Standard. Estes valores identificam o percurso. Configure as ações do seu processo para um workflow de produção.

**Ligar as saídas**

Ligue Start à entrada da condição. Ligue a saída azul de sucesso a Approval e a saída laranja de condição falsa a Standard. A saída vermelha trata os erros de avaliação separadamente. A posição dos cartões não cria um percurso.

**Preparar os casos de teste**

Abra Testar na barra de ferramentas. Escolha um documento de teste ou introduza os seus dados completos em JSON. Verifique montantes superiores, inferiores e iguais a mil, bem como valores em falta. Consulte os resultados dos nós após a execução.

**Validar, guardar e ativar**

Valide as ligações e as definições dos cartões. Guarde explicitamente no servidor e verifique a ativação em separado. Os rascunhos automáticos do navegador não substituem a gravação. A execução e os registos exigem o módulo e a subscrição adequados.

</details>

[Ver os cinco capítulos](../advanced-workflow-videos.md)

A barra de ferramentas do Advanced Workflow percorre a parte inferior da tela e dá-lhe tudo o que precisa para construir, navegar e gerir o fluxo.

## Controlos da barra de ferramentas

- **+ Add** — abre o menu de nós para adicionar um nó (consulte [Nós](nodes.md)).
- **Undo / Redo** — recue ou avance pelas suas alterações.
- **Zoom in / Zoom out** — altere o nível de zoom da tela.
- **Workflow name** — nomeie o fluxo de trabalho diretamente.
- **Edit description** — adicione uma descrição para o fluxo de trabalho.
- **Variables** — abra o painel [Variables](variables.md).
- **Help** — abra os atalhos de teclado e a caixa de diálogo de ajuda.
- **Validate / Test** — verifique e execute o fluxo (consulte [Validação e Testes](validation-and-testing.md)).
- **Snap to grid** — ative/desative o alinhamento dos nós à grelha para esquemas organizados.
- **Mini-map** — ative/desative um pequeno mapa de visão geral para navegar em grafos grandes.
- **Save** — guarde o fluxo de trabalho. Um indicador de **auto-save** mostra quando o fluxo foi guardado automaticamente pela última vez.

## Atalhos de teclado

Prima <kbd>?</kbd> na tela para abrir a caixa de diálogo de atalhos e ajuda a qualquer momento.

<figure><img src="../../../.gitbook/assets/workflow_advanced_shortcuts.png" alt="Caixa de diálogo de atalhos de teclado e ajuda"><figcaption><p>A caixa de diálogo de atalhos de teclado e ajuda — atalhos, realce do caminho de execução e cores das ligações.</p></figcaption></figure>

| Atalho | Ação |
|---|---|
| <kbd>Cmd/Ctrl</kbd> + <kbd>S</kbd> | Guardar fluxo de trabalho |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> | Validar fluxo de trabalho |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd> | Testar fluxo de trabalho |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Z</kbd> / <kbd>Shift</kbd> + <kbd>Z</kbd> | Anular / Refazer |
| <kbd>Cmd/Ctrl</kbd> + <kbd>C</kbd> / <kbd>V</kbd> / <kbd>D</kbd> | Copiar / Colar / Duplicar nós selecionados |
| <kbd>Cmd/Ctrl</kbd> + <kbd>A</kbd> | Selecionar todos os nós |
| <kbd>Shift</kbd> + Arrastar | Selecionar nós (arrastando) |
| <kbd>Cmd/Ctrl</kbd> + Clique esquerdo | Adicionar/remover nó da seleção |
| Clique direito | Menu de adição de nós |
| <kbd>Del</kbd> | Eliminar nó selecionado |
| <kbd>?</kbd> | Mostrar esta ajuda |

## Próximos passos

- Construa o fluxo com [Nós](nodes.md) e [Variáveis](variables.md).
