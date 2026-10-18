---
description: "Cinco capítulos em português sobre workflows avançados e registos, com legendas e transcrições."
---

# Vídeos do Advanced Workflow

Aprenda a criar, testar e diagnosticar um workflow avançado. Os cinco capítulos têm narração em português.

Os três primeiros capítulos mostram a interface real do DocBits. Os dois capítulos de registos utilizam diagramas didáticos identificados como ilustrações. As capturas mostram rascunhos de demonstração não guardados.

Cada vídeo inclui legendas WebVTT e uma transcrição expansível.

1. [Construtor e canvas](#builder-and-canvas) · 1:55
2. [Nós e percursos](#nodes-and-routes) · 2:00
3. [Variáveis, testes e ativação](#variables-tests-and-activation) · 1:56
4. [Encontrar a execução relevante](#find-the-relevant-execution) · 1:58
5. [Seguir nós e diagnosticar](#trace-nodes-and-diagnose) · 1:55

## Construtor e canvas {#builder-and-canvas}

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

## Nós e percursos {#nodes-and-routes}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/pt.mp4" %}

[Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/pt.vtt) · 2:00

<details>
<summary>Transcrição</summary>

**A função de cada nó**

Start inicia manualmente. When define um evento. Nenhum aceita ligações de entrada. And verifica uma condição. Then executa uma ação. Ambos os construtores partilham o catálogo de cartões. As notas explicam o desenho sem serem executadas.

**Três resultados diferentes**

Arraste uma saída para a entrada seguinte. No editor, azul significa sucesso, laranja condição falsa e vermelho erro. And tem três resultados; Then, sucesso e erro. As vistas de execução mostram o sucesso a verde.

**Crie uma alternativa**

Verifique se uma fatura ultrapassa o limiar. Ligue azul à aprovação, laranja ao processamento normal e vermelho à gestão de erros. Uma condição falsa pode continuar pelo percurso ligado; não interrompe todos os ramos.

**Unir com Wait ALL**

Wait ALL reúne ramos. Cada nó de origem deve ter seguido um percurso ligado à junção. Ligue ambas as verificações necessárias e a ação seguinte. Um percurso não selecionado não fornece o resultado obrigatório.

**Alternativas com ANY e OR**

Wait ANY e OR reúnem ramos se pelo menos uma origem seguir um percurso ligado. OR exige dois nós de origem diferentes. Estas junções não criam escolhas exclusivas nem cancelam outras ações. Teste o grafo completo.

**Mantenha o grafo executável**

Os nós devem ser acessíveis a partir de uma entrada. Evite ciclos e ligações de entrada para Start ou When. Inclua uma ação Then e valide os percursos. Nós Delay importados exigem duração positiva; Adicionar não oferece Delay.

</details>

## Variáveis, testes e ativação {#variables-tests-and-activation}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/pt.mp4" %}

[Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/pt.vtt) · 1:56

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

**Examine os resultados**

Examine mensagens e durações: verde, sucesso; laranja, condição falsa; vermelho, erro; cinzento, ignorado. Corrija e repita. Use o gestor de testes para cenários repetíveis: sucesso, alternativas, dados em falta e erros.

**Guarde antes de ativar**

A gravação automática conserva um rascunho local cerca de trinta segundos após alterações. Guarde explicitamente no servidor. Ative após a primeira gravação. Verifique o estado na lista antes de esperar execução automática.

</details>

## Encontrar a execução relevante {#find-the-relevant-execution}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/pt.mp4" %}

[Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/pt.vtt) · 1:58

<details>
<summary>Transcrição</summary>

**Abra os registos**

No painel de documentos, selecione Workflow Logs no menu Ações. O acesso aos workflows deve estar ativo. Estes registos pertencem ao documento escolhido. Os testes do editor e os registos de eventos ou atividade da organização são separados.

**Leia os contadores**

Azul conta execuções nos resultados atuais; vermelho, erros; amarelo, condições falsas; verde, sucessos. Os contadores representam execuções, não definições de workflow ou nós. Os filtros podem alterar estes números.

**Escolha a execução exata**

Cada linha mostra nome, data de criação, duração em segundos e resultado. Um workflow pode executar várias vezes no mesmo documento. Compare os horários. Uma duração curta pode aparecer como zero vírgula zero zero segundos por arredondamento.

**Restrinja os resultados**

Use Pesquisar para encontrar um workflow. O ícone de ajustes abre direção e critério de ordenação, estado e datas inicial e final. Ordene por nome ou criação. Introduza datas como ano, mês, dia e selecione Aplicar.

**Verifique páginas e filtros**

Use a paginação para resultados antigos. Limpar filtros recarrega a lista sem seleções. Limpe a pesquisa separadamente. Sem resultados, verifique documento, datas e estado. Uma lista vazia não demonstra um erro de execução.

**Estados especiais**

Um aviso e um ícone de bloqueio indicam o limite de execuções do documento. Investigue eventos repetidos antes de alterar limites. A transferência de vídeo DocOperator aparece apenas se existir gravação; corresponde àquela execução.

</details>

## Seguir nós e diagnosticar {#trace-nodes-and-diagnose}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/pt.mp4" %}

[Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/pt.vtt) · 1:55

<details>
<summary>Transcrição</summary>

**Expanda uma execução**

Expanda a linha do workflow. Uma execução avançada mostra o grafo à esquerda e mensagens à direita; um workflow padrão mostra cartões em sequência. Os dados descrevem aquela execução e podem diferir do editor atual.

**Selecione um nó**

Desloque ou amplie o grafo e selecione um nó. Card Logs mostra as mensagens. Wait ALL e Wait ANY também podem ter mensagens de nó. Relacione a mensagem com o nó selecionado e o horário da execução.

**Distinga os resultados**

Verde indica sucesso; laranja, condição falsa; vermelho, erro; cinzento, ignorado. Um nó ignorado não executou. Antes de o alterar, verifique se foi escolhido outro ramo ou falta uma entrada na junção.

**Siga o primeiro desvio**

Siga o percurso real desde a entrada. Numa condição de montante falsa, examine laranja; num erro, leia a mensagem e siga vermelho. O tratamento de erros pode funcionar enquanto a execução mantém o erro original.

**Verifique as junções**

Em Wait ALL, verifique cada origem e resultado ligado. Em ANY ou OR, procure uma origem correspondente. Duas saídas do mesmo nó não são aprovações independentes. Uma condição laranja pode ser intencional.

**Corrija e verifique**

Registe workflow, referência do documento, horário, nó e mensagem exata. Corrija configuração ou dados e teste um cenário repetível. Guarde e verifique a ativação. Compare uma execução nova com a anterior; registos antigos conservam o comportamento anterior.

</details>
