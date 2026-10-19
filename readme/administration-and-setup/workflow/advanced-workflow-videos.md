---
description: "Cinco capítulos em português sobre workflows avançados e registos, com legendas e transcrições."
---

# Vídeos do Advanced Workflow

Aprenda a criar, testar e diagnosticar um workflow avançado. Os cinco capítulos têm narração em português.

Os três primeiros capítulos mostram o verdadeiro designer do DocBits com rascunhos de demonstração. A pré-visualização da pesquisa mostra o processamento real de documentos e os controlos dos registos com resultados vazios. O capítulo de diagnóstico mantém os diagramas didáticos identificados como ilustrações.

Cada vídeo inclui legendas WebVTT e uma transcrição expansível.

1. [Construtor e canvas](#builder-and-canvas) · 1:55
2. [Nós e percursos](#nodes-and-routes) · 2:00
3. [Variáveis, testes e ativação](#variables-tests-and-activation) · 1:56
4. [Encontrar a execução relevante](#find-the-relevant-execution) · 1:58
5. [Seguir nós e diagnosticar](#trace-nodes-and-diagnose) · 1:55

## Construtor e canvas {#builder-and-canvas}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/pt.mp4" %}

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/pt.mp4) · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/pt.vtt) · 1:55

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

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/pt.mp4) · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/pt.vtt) · 2:00

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

Acompanha o workflow de faturas ligado no verdadeiro designer DocBits. Abre Variáveis, compara os tipos e a referência de documento, localiza Validar, prepara testes com documentos ou dados personalizados e identifica Guardar e ativação. As cenas de teste mostram a configuração de dados de exemplo; não mostram um resultado executado.

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

## Encontrar a execução relevante {#find-the-relevant-execution}

{% hint style="info" %}
Pré-visualização para teste: ecrãs reais do DocBits com ações do documento, fluxo de documentos, tempos dos passos, registos vazios e filtros de estado e data. O documento não tem uma execução Advanced Workflow guardada. Esta pré-visualização ainda não inclui linhas de execução, paginação ou diagnóstico dos nós.
{% endhint %}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/pt.mp4" %}

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/pt.mp4) · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/pt.vtt) · 1:52

<details>
<summary>Transcrição</summary>

**Começar pelo documento**

No painel de documentos, abra o menu de ações e escolha Fluxo de documentos. O histórico real mostra a importação e o OCR. Abra um passo para verificar os tempos de espera e processamento. Estes passos são distintos dos nós de Advanced Workflow.

**Ler os contadores reais**

Aqui estão os registos de workflow do mesmo documento. Azul indica o total, vermelho os erros, amarelo as condições não cumpridas e verde os sucessos. Este documento de demonstração não tem execuções registadas. Por isso, os quatro contadores mostram zero.

**Verificar as colunas de execução**

As colunas mostram o nome do workflow, a data de criação, a duração e o resultado. Distinga execuções repetidas pela data e hora. Este documento não tem uma linha para abrir.

**Abrir os filtros de estado**

O ícone de filtros abre o menu real. Ordene por nome ou data de criação, de forma ascendente ou descendente. O estado oferece sucesso, condição não cumprida e erro.

**Escolher datas e limpar filtros**

Escolha um período com as datas de início e fim ou o calendário. O formato é ano, mês e dia. Aplicar pede os resultados. Limpar filtros repõe a seleção. Limpe a pesquisa separadamente.

**Pré-visualização: falta uma execução guardada**

Esta pré-visualização permite verificar o acesso ao documento, os detalhes do processamento e os controlos dos registos. Falta uma execução Advanced Workflow guardada para mostrar linhas reais, paginação, percursos e mensagens dos nós. Estes resultados não são simulados no vídeo.

</details>

## Seguir nós e diagnosticar {#trace-nodes-and-diagnose}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/pt.mp4" %}

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/pt.mp4) · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/pt.vtt) · 1:55

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
