# Registos do Fluxo de Trabalho

## Vídeo

O vídeo de pesquisa é uma pré-visualização com ecrãs reais do DocBits. O vídeo de diagnóstico mantém os diagramas didáticos identificados como ilustrações.
### Encontrar a execução relevante

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

### Seguir nós e diagnosticar

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

## **Visão Geral**

Os **Registos do Fluxo de Trabalho** permitem aos usuários analisar quais fluxos de trabalho foram executados para um documento, entender os resultados da execução e aprofundar-se nos detalhes do nível de condição para depuração ou validação.

## **Acessando os Registos do Fluxo de Trabalho**

Para acessar os registos do fluxo de trabalho:

1. Navegue até o **Dashboard**.
2. Clique no **menu de Ações** (ícone de três pontos) ao lado do documento desejado.
3. Selecione **Registos do Fluxo de Trabalho** no menu.
   * <mark style="color:red;">**Nota**</mark>**:** O recurso de workflow deve estar ativado para acessar esta opção.
4.  Um **painel lateral** é aberto mostrando um resumo dos fluxos de trabalho executados.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAlgg3jnSVRVyuYxy4tAp%252Fimage.png%3Falt%3Dmedia%26token%3D4e8fcd63-6113-47eb-95a4-95a7821dc9b9\&width=768\&dpr=4\&quality=100\&sign=9e6ba9f5\&sv=2)

## **Componentes do Painel de Registos do Fluxo de Trabalho**

#### **1. Contadores de Resumo do Fluxo de Trabalho**

Localizados no topo do painel de registos:

* **Azul**: Número total de fluxos de trabalho executados.
* **Vermelho**: Fluxos de trabalho que terminaram em **erros**.
* **Amarelo**: Fluxos de trabalho que **não foram concluídos** devido a incompatibilidades de condição.
* **Verde**: Fluxos de trabalho **executados** com sucesso.

#### **2. Tabela de Execução do Fluxo de Trabalho**

Cada linha na tabela representa uma execução de fluxo de trabalho e inclui:

* **Nome do Fluxo de Trabalho**
* **Timestamp** (Criado Em)
* **Tempo de Execução** (em segundos)
* **Ícone de Resultado**:
  * Marca de seleção verde: Fluxo de trabalho executado com sucesso.
  * Cruz vermelha: Fluxo de trabalho executado com um erro.
  * Traço laranja: A execução foi interrompida devido a uma condição não atendida.

Ao clicar na **seta** à esquerda de cada linha, expande-se a **visualização detalhada do fluxo de trabalho**.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="" width="563"><figcaption></figcaption></figure></div>

### **Visualização Detalhada do Fluxo de Trabalho**

Ao clicar em uma linha de fluxo de trabalho específica, abre-se o **registo de execução detalhado**, mostrando:

#### **Avaliação de Condição**

* Bloco **Quando...**: Condição inicial.
* Bloco(s) **E...**: Condições adicionais.
* Bloco(s) **Então...**: Ações realizadas quando todas as condições são atendidas.

Cada linha de condição mostra:

* Marca de seleção **verde**: Condição foi atendida.
* Traço laranja: Condição não foi atendida.
* Cruz vermelha: Condição falhou **devido a um erro**

### **Nota Comportamental Importante**

Se uma condição em um fluxo de trabalho **não for atendida**, o sistema **para de avaliar quaisquer outras cartas de fluxo de trabalho** dentro desse fluxo de trabalho. Esse comportamento evita processamento desnecessário. Como indicador visual, a carta que **não atendeu à sua condição** é mostrada em **cinza**, e todas as **cartas subsequentes** no mesmo fluxo de trabalho também aparecerão **cinza**, indicando que elas **não foram executadas**.
