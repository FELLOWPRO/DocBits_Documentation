---
description: "Cinco capítulos em português sobre workflows avançados e registos, com legendas e transcrições."
---

# Vídeos do Advanced Workflow

Os cinco capítulos têm narração em português, um ficheiro de legendas e uma transcrição. O primeiro mostra a criação do workflow de exemplo passo a passo; os restantes aprofundam cada tema.

Os três primeiros capítulos mostram o verdadeiro designer do DocBits com rascunhos de demonstração. A pré-visualização da pesquisa mostra o processamento real de documentos e os controlos dos registos com resultados vazios. O capítulo de diagnóstico mantém os diagramas didáticos identificados como ilustrações.

Cada vídeo inclui legendas WebVTT e uma transcrição expansível.

1. [Construtor e canvas](#builder-and-canvas) · 3:15
2. [Nós e percursos](#nodes-and-routes) · 2:00
3. [Variáveis, testes e ativação](#variables-tests-and-activation) · 1:56
4. [Encontrar a execução relevante](#find-the-relevant-execution) · 1:58
5. [Seguir nós e diagnosticar](#trace-nodes-and-diagnose) · 1:55

## Construtor e canvas {#builder-and-canvas}

Conheça o João e acompanhe a sua explicação na interface real do DocBits em português. Verifica o painel, a lista de workflows e a licença antes de abrir um rascunho não guardado no designer. Passo a passo, dá um nome ao workflow, configura a verificação do montante e duas ações, organiza os cartões e liga os dois percursos. Depois mostra como preparar testes com um documento ou dados personalizados. A conta de demonstração não tem uma subscrição Advanced Workflow e bloqueia a validação; o rascunho permanece não guardado e inativo.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.mp4" %}

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.mp4) · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.vtt) · [Transcrição (texto)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.txt) · 3:15

| Neste vídeo | Início |
| --- | --- |
| Conheça o administrador | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.mp4#t=0) |
| Verificar o acesso | [0:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.mp4#t=4) |
| Dar um nome ao workflow | [0:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.mp4#t=27) |
| Configurar a condição de montante | [0:41](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.mp4#t=41) |
| Adicionar a ação Approval | [1:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.mp4#t=65) |
| Adicionar a ação Standard | [1:24](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.mp4#t=84) |
| Organizar os cartões | [1:44](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.mp4#t=104) |
| Ligar os percursos | [1:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.mp4#t=118) |
| Preparar os testes | [2:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.mp4#t=143) |
| Validar, guardar e ativar | [2:47](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-paced-e/pt.mp4#t=167) |

<details>
<summary>Transcrição</summary>

**Conheça o administrador**

Administro o DocBits. Criamos uma verificação de faturas.

**Verificar o acesso**

Começo no painel de workflows e abro a lista. Depois verifico a licença. Workflow e Advanced Workflow precisam ambos de acesso ativo. Com os dois acessos ativos, Novo workflow apresenta Advanced Workflow. Esta conta de documentação não tem uma licença de workflow ativa. Por isso, continuo com uma pré-visualização não guardada no editor.

**Dar um nome ao workflow**

Estou no verdadeiro editor do DocBits. Primeiro, dou um nome claro ao rascunho. Vamos verificar o montante de uma fatura e usar duas ações simples para mostrar os percursos possíveis. Esta demonstração fica por guardar.

**Configurar a condição de montante**

Abro o menu para adicionar e escolho um cartão de condição. Na categoria Campo do documento, seleciono a condição Docfield. Introduzo o campo total_amount. Depois escolho a comparação maior que. E introduzo mil. Utilize a chave do seu próprio campo de documento. Um montante exatamente igual a mil não satisfaz esta comparação.

**Adicionar a ação Approval**

Agora adiciono um cartão de ação da categoria Campo do documento. A ação define um campo do documento. Uso a chave de demonstração approval_route. E introduzo o valor Approval. Isto identifica o percurso. Um processo de aprovação real precisa das suas próprias ações de negócio.

**Adicionar a ação Standard**

Adiciono um segundo cartão com a mesma ação. A ação define um campo do documento. Uso a chave de demonstração approval_route. Desta vez, o campo de demonstração recebe o valor Standard. Os dois cartões estão configurados. Ainda precisam de ligações para determinar qual a ação executada.

**Organizar os cartões**

Arrasto os cartões para uma disposição legível. As duas ações ficam à direita. A condição fica ao centro e Start à esquerda. Mover um cartão altera a posição. Não cria uma ligação.

**Ligar os percursos**

Arrasto da saída de Start para a entrada da condição. O percurso de sucesso segue uma ligação azul até Approval. O percurso laranja de condição não satisfeita segue para Standard. A saída vermelha de erro é distinta e destina-se a erros de avaliação. Aqui fica sem ligação. Num workflow de produção, defina como tratar estes erros.

**Preparar os testes**

O botão de teste na barra de ferramentas abre a seleção do documento de teste. Posso escolher um documento de demonstração ou preparar dados personalizados completos. Teste montantes superiores, inferiores e iguais a mil. Verifique também um montante em falta. Esta conta não tem licença Advanced Workflow. Mostro a preparação do teste, não um resultado executado.

**Validar, guardar e ativar**

A validação verifica ligações e configurações dos cartões. Nesta conta, a falta de licença impede a validação. Com uma conta autorizada, guardaria explicitamente no servidor. Depois verificaria a ativação em separado. Antes de guardar pela primeira vez, o interruptor está desativado. O indicador de rascunho automático refere-se a uma cópia local no navegador. Não significa que o workflow esteja guardado ou ativado.

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
