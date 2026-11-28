# Registos do Fluxo de Trabalho

Para explicações narradas da vista avançada de registos, veja [Encontrar a execução relevante](advanced-workflow-builder/videos.md#find-the-relevant-execution) e [Seguir nós e diagnosticar](advanced-workflow-builder/videos.md#trace-nodes-and-diagnose). Ambos os capítulos estão disponíveis em inglês e alemão, com ficheiros de legendas e transcrições.

## **Visão Geral**

Os **Registos do Fluxo de Trabalho** permitem aos utilizadores analisar quais Workflows foram executados para um documento, compreender os resultados da execução e aprofundar os detalhes ao nível das condições para depuração ou validação.

## **Aceder aos Registos do Fluxo de Trabalho**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4" %}

**Vídeo:** Ler os registos do Workflow · 1:34 · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.vtt)

<details>

<summary>Transcrição</summary>

**Abrir os registos do Workflow** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=0.25)

Cada documento guarda os registos dos Workflows que nele foram executados. No Dashboard do documento, abra as ações de um documento e escolha Workflow Logs.

**Execuções e os seus resultados** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=12.15)

No topo vê quantas execuções houve e quantas terminaram com um erro, uma condição falhada ou sucesso. Abaixo, cada execução é listada com o seu Workflow, hora, duração e resultado.

**O percurso de uma execução** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=25.716)

Arraste o divisor para a esquerda para dar mais espaço aos registos. Depois clique numa execução para ver o percurso que seguiu. Cada cartão mostra o seu resultado: verde para sucesso, laranja para uma condição falhada, vermelho para um erro. Aqui o cartão And terminou com uma condição falhada, pelo que o cartão Then seguinte não foi executado.

**Porque um cartão terminou assim** · [0:45](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=45.35)

Selecione um cartão para ler o seu registo. Ele indica o que o cartão comparou e porque terminou assim. Aqui, o documento está pronto para validação, mas o cartão espera uma segunda aprovação pendente.

**Um erro e o seu motivo** · [0:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=58.283)

Uma execução que termina com um erro mostra o cartão que falhou a vermelho. Aqui o cartão And não conseguiu ler a morada de entrega do documento. Dados em falta são sempre um erro, pelo que o cartão Then seguinte não foi executado.

**Encontrar execuções** · [1:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=73.216)

Com muitas execuções, use a pesquisa para encontrar um Workflow pelo nome e o botão de filtro para restringir a lista por estado ou data.

**Nota sobre o limite de execuções** · [1:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=83.116)

Aparece uma nota no topo quando um Workflow atingiu o seu limite de execuções neste documento. O vídeo sobre limites de execução explica-o.

</details>

Para aceder aos registos do Workflow:

1. Navegue até ao **Dashboard**.
2. Clique no **Actions menu** (ícone de três pontos) junto do documento pretendido.
3. Selecione **Workflow Logs** no menu.
   * <mark style="color:red;">**Note**</mark>: O recurso Workflow tem de estar ativado para aceder a esta opção.
4.  Um **side panel** abre-se a mostrar um resumo dos Workflows executados.\\

    <div align="left"><figure><img src="../../.gitbook/assets/image (5).png" alt="Dashboard with the workflow logs side panel showing summary counters and a table of executed workflows with result icons" width="563"><figcaption></figcaption></figure></div>

## **Abrir um registo como página própria**

O side panel tapa a lista de documentos. Para um documento cujo Workflow inspeciona durante algum tempo, abra o mesmo registo como página completa: selecione o ícone de nova janela no cabeçalho do painel. A página tem o endereço `/workflows/logs/<document id>`, pelo que a pode manter aberta numa segunda janela do navegador ou enviar o endereço a um colega que tenha acesso ao documento.

A página mostra os mesmos contadores de resumo, a mesma tabela de Workflows executados e a mesma vista de detalhe que o painel.

## **Mudar para outro documento**

Na página completa, um campo de pesquisa acima da lista encontra um documento pelo nome ou pelo seu ID. Os resultados mostram a data de carregamento, o responsável e o estado de cada documento, para poder distinguir documentos com nomes semelhantes. Selecionar um resultado carrega o respetivo registo de Workflow e coloca o documento no endereço. A pesquisa abrange os documentos da sua organização que as suas permissões lhe permitem ver; quando nada corresponde, o DocBits indica-o abaixo do campo em vez de mostrar uma lista vazia.

## **Componentes do Painel de Registos do Fluxo de Trabalho**

#### **1. Contadores de Resumo do Workflow**

Localizados no topo do painel de registos:

* **Azul**: Número total de Workflows executados.
* **Vermelho**: Workflows que terminaram em **erros**.
* **Amarelo**: Workflows que **não foram concluídos** devido a condições não cumpridas.
* **Verde**: Workflows **executados** com sucesso.

#### **2. Tabela de Execução de Workflows**

Cada linha da tabela representa uma execução de Workflow e inclui:

* **Workflow Name**
* **Timestamp** (Created On)
* **Runtime** (em segundos)
* **Result Icon**:
  * Marca de verificação verde: Workflow executado com sucesso.
  * Cruz vermelha: Workflow executado com um erro.
  * Traço laranja: A execução foi interrompida porque uma condição não foi cumprida

Clicar na **seta** à esquerda de cada linha expande a **vista de detalhe do Workflow**.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Expanded workflow log row showing When and And condition cards with green checks and a grayed card that was not met, plus card logs" width="563"><figcaption></figcaption></figure></div>

### **Vista de Detalhe do Workflow**

Clicar numa linha de Workflow específica abre o respetivo **registo de execução detalhado**, mostrando:

#### **Avaliação de Condições**

* Bloco **When...**: Condição inicial.
* Bloco(s) **And...**: Condições adicionais.
* Bloco(s) **Then...**: Ações executadas quando todas as condições são cumpridas.

Cada linha de condição mostra:

* **Marca de verificação verde**: Condição cumprida.
* **Traço laranja**: Condição não cumprida.
* **Cruz vermelha**: Condição falhou **devido a um erro**

### **Nota Importante sobre o Comportamento**

Se uma condição num Workflow **não for cumprida**, o sistema **deixa de avaliar quaisquer cartões de Workflow seguintes** nesse Workflow. Este comportamento evita processamento desnecessário\
Como indicador visual, o cartão que **não cumpriu a sua condição** é mostrado em **cinza**, e todos os **cartões seguintes** no mesmo Workflow também aparecem em **cinza**, indicando que **não foram executados**.
