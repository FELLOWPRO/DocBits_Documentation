# Validação e Testes

## Vídeo: Variáveis, testes e ativação

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/pt.mp4" %}

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/pt.mp4) · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/pt.vtt) · 1:57

<details>
<summary>Transcrição</summary>

**Escolha o tipo**

Abra Variáveis pelas chavetas. Escolha texto, número, sim ou não, ou documento. Pesquise nomes. Document guarda uma referência definida por uma ação específica; o formulário não aceita valores de documento.

**Variáveis da organização**

Escolha nome único, tipo e valor inicial. Criar, editar ou eliminar guarda imediatamente na organização. Outros workflows partilham estes valores. Guardar ou descartar o canvas não anula alterações às variáveis.

**Valide a estrutura**

Clique em Validar. Examine erros e avisos acima do canvas. Uma mensagem foca o nó. Verifique ações, entradas, saídas, ciclos e junções. Uma estrutura válida não garante dados corretos.

**Escolha o contexto**

Reproduzir na barra abre a escolha do documento. Escolha documento, dados personalizados ou teste sem documento para cartões independentes. Start executa diretamente. Os testes incluem alterações não guardadas e simulam ações destrutivas.

**Preparar e rever cenários de teste**

Prepara testes separados acima, abaixo e exatamente em mil, além de dados em falta. Após a execução, verifica mensagens e durações: verde indica sucesso, laranja falso, vermelho erro e cinzento ignorado. Volta a testar as correções. Usa o gestor de testes para cenários repetíveis.

**Guarde antes de ativar**

A gravação automática conserva um rascunho local cerca de trinta segundos após alterações. Guarde explicitamente no servidor. Ative após a primeira gravação. Verifique o estado na lista antes de esperar execução automática.

</details>

[Ver os cinco capítulos](../advanced-workflow-videos.md)

Enquanto constrói um Advanced Workflow, dois controlos na barra de ferramentas permitem-lhe verificá-lo sem sair do construtor. Estes destinam-se a *verificações rápidas durante a construção* — para testes guardados e repetíveis, use o [Test Manager](../test-manager.md).

## Validate

Clique no controlo **Validate** (o ícone de círculo de verificação, ou prima <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). A validação verifica o grafo em busca de problemas — nós não ligados, configuração em falta e ligações inválidas — e assinala-os para que os possa corrigir antes de o fluxo de trabalho ser executado em documentos reais.

## Test

Clique no controlo **Test** (o ícone de reprodução, ou prima <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) para executar o fluxo atual contra uma amostra e observar o seu comportamento, sem afetar documentos em produção. Esta é a forma mais rápida de verificar uma alteração que acabou de fazer na tela.

## Quando usar qual

- **Validate / Test no construtor** (esta página) — feedback instantâneo enquanto desenha o fluxo.
- **[Test Manager](../test-manager.md)** — guarde o cenário para o poder voltar a executar mais tarde (e em conjunto com todos os seus outros cenários) para detetar regressões após alterações futuras.

## Próximos passos

- Reveja os tipos de nós e ligações em [Nós](nodes.md).
- Veja todos os controlos da barra de ferramentas e da tela em [Barra de ferramentas e Tela](toolbar-and-canvas.md).
