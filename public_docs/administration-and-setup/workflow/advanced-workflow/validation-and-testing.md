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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/pt.mp4" %}

**Vídeo:** Validar um Workflow · 0:48 · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/pt.vtt)

<details>

<summary>Transcrição</summary>

**Validar verifica a montagem** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/pt.mp4#t=0.25)

Antes de salvar, clique em Validar na barra de ferramentas. Ele verifica como o Workflow foi montado: se um cartão Quando o inicia, se todo cartão está conectado e se os caminhos fazem sentido. Os problemas aparecem acima da tela.

**Clique na mensagem para achar o cartão** · [0:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/pt.mp4#t=16.616)

Clique em uma mensagem para ir até o cartão de que ela trata. Aqui o cartão de atribuição não está conectado, então nunca seria executado. Conecte-o.

**Sem mensagens: o Workflow é válido** · [0:26](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/pt.mp4#t=26.883)

Valide de novo. Quando não sobra nada, o Workflow é válido e você pode salvá-lo.

**Primeiro validar, depois testar** · [0:32](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/pt.mp4#t=32.616)

Salvar faz as mesmas verificações, mas salva o Workflow mesmo com problemas, então valide primeiro. Validar não verifica seus dados nem as configurações dentro dos cartões. Para ver o que um Workflow faz com um documento real, teste-o.

</details>

Clique no controlo **Validate** (o ícone de círculo de verificação, ou prima <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). A validação verifica o grafo em busca de problemas — nós não ligados, configuração em falta e ligações inválidas — e assinala-os para que os possa corrigir antes de o fluxo de trabalho ser executado em documentos reais.

## Teste

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pt.mp4" %}

**Vídeo:** Testar um Workflow · 1:36 · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pt.vtt)

<details>

<summary>Transcrição</summary>

**Testar antes de ativar** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pt.mp4#t=0.25)

Teste um Workflow antes de ativá-lo. Um teste executa o que está na tela agora, inclusive mudanças ainda não salvas. Ações como atribuir ou exportar são só simuladas, então o documento fica como está.

**Testar o Workflow inteiro** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pt.mp4#t=12.55)

Aqui está um Workflow que ainda não foi salvo. Para testar o Workflow inteiro, clique em Testar fluxo de trabalho na barra de ferramentas.

**Escolher um documento de teste** · [0:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pt.mp4#t=21.783)

Escolha o documento para o teste. Workflows que não precisam de documento também podem ser testados sem um. Pesquise o documento pelo nome, selecione-o e clique em Teste.

**Ler o resultado na tela** · [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pt.mp4#t=33.616)

O teste segue o caminho do documento. Esta fatura não está com aprovação pendente, então o cartão E termina com uma condição não atendida, e o caminho laranja segue até o cartão de atribuição. Os caminhos não seguidos ficam em cinza, e o banner no topo mostra o resultado e quanto tempo o teste levou.

**Detalhes de cada cartão** · [0:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pt.mp4#t=51.35)

Clique em Detalhes para ver cada cartão com seu resultado e mensagem. Reteste executa o teste de novo depois de uma mudança.

**Testar um único cartão** · [0:59](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pt.mp4#t=59.383)

Para testar um único cartão, passe o mouse sobre ele e clique no botão de reproduzir. Você também pode clicar com o botão direito no cartão e escolher Teste a partir deste nó. O teste começa neste cartão, com a mesma escolha de documento.

**O selo mostra os detalhes** · [1:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pt.mp4#t=74.316)

Só este cartão e os seguintes são executados. Passe o mouse sobre o selo para ver o resultado do cartão. Mude o cartão e teste de novo até ele fazer o que você espera.

**O que as cores significam** · [1:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pt.mp4#t=85.083)

Resumindo: verde é sucesso, laranja uma condição não atendida e vermelho um erro. Cartões que não foram executados ficam esmaecidos e ganham um selo cinza.

</details>

Clique no controlo **Test** (o ícone de reprodução, ou prima <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) para executar o fluxo atual contra uma amostra e observar o seu comportamento, sem afetar documentos em produção. Esta é a forma mais rápida de verificar uma alteração que acabou de fazer na tela.

## Quando usar qual

- **Validate / Test no construtor** (esta página) — feedback instantâneo enquanto desenha o fluxo.
- **[Test Manager](../test-manager.md)** — guarde o cenário para o poder voltar a executar mais tarde (e em conjunto com todos os seus outros cenários) para detetar regressões após alterações futuras.

## Próximos passos

- Reveja os tipos de nós e ligações em [Nós](nodes.md).
- Veja todos os controlos da barra de ferramentas e da tela em [Barra de ferramentas e Tela](toolbar-and-canvas.md).
