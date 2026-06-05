---
description: Monitor workflow performance, manage workflows, and access the Card SDK
---

# Painel de Workflows

O Painel de Workflows é o seu hub central para gerenciar e monitorar todos os workflows no DocBits. Acesse-o clicando no ícone **Workflows** na barra lateral esquerda.

<figure><img src="../../.gitbook/assets/workflow_dashboard.png" alt="Painel de Workflows com totais de execuções, taxas de sucesso e falha, o gráfico de execuções e a atividade recente"><figcaption><p>O Painel de Workflows — totais de execuções, taxas de sucesso/falha e atividade recente de todos os workflows.</p></figcaption></figure>

## Aba Painel

A aba Painel fornece uma visão geral rápida do desempenho dos workflows para um período de tempo selecionado.

### Filtros

- **Data de início / Data de término** — Selecione o intervalo de tempo para as estatísticas
- **Nome do Workflow** — Filtre por um workflow específico ou visualize todos
- **Comparar** — Compare dois períodos de tempo lado a lado
- **Limpar** — Redefina todos os filtros

### Cartões de Estatísticas

| Métrica | Descrição |
|---|---|
| **Workflows executados hoje** | Número total de execuções de workflow hoje |
| **Workflows criados (período)** | Novos workflows criados dentro do intervalo de datas selecionado |
| **Total de execuções** | Execuções acumuladas de workflow no período |
| **Execuções bem-sucedidas** | Número de execuções concluídas sem erros |
| **Taxa de sucesso** | Percentual de execuções bem-sucedidas em relação ao total |
| **Taxa de falha** | Percentual de execuções com falha em relação ao total |

{% hint style="warning" %}
Uma alta taxa de falha (exibida como **CRITICAL** em vermelho) indica que os workflows estão encontrando erros. Investigue os workflows com falha usando os logs de execução no [Construtor Avançado de Workflows](advanced-workflow-builder/).
{% endhint %}

### Gráfico de Execuções de Workflow

O gráfico mostra uma distribuição mensal de execuções de workflow **bem-sucedidas** (verde) e **com falha** (vermelho/rosa), ajudando a identificar tendências e picos de erros.

### Atividade Recente

- **Últimos Testes de Workflow** — Mostra execuções de teste recentes com status de aprovação/reprovação
- **Últimos Workflows** — Mostra workflows criados ou modificados recentemente

## Aba Lista de Workflows

A aba Lista de Workflows exibe todos os workflows com funcionalidades de pesquisa, ordenação e gerenciamento.

<!-- screenshot: Workflow List showing Advanced workflows with columns -->

### Colunas

| Coluna | Descrição |
|---|---|
| **Status** | Ícone de alternância — clique para ativar/desativar um workflow |
| **Nome** | Nome do workflow (clique para abrir no Construtor de Workflows) |
| **Tipo** | Badge exibindo `Advanced` para workflows visuais |
| **Quando...** | Resumo da condição de disparo |
| **Atualizado Por** | Usuário que modificou o workflow por último |
| **Criado Em** | Data e hora de criação |
| **Atualizado** | Data e hora da última modificação |
| **Ações** | Menu de contexto (excluir, duplicar, exportar) |

### Ações

- **Pesquisar** — Filtre workflows por nome usando a barra de pesquisa
- **+ ADICIONAR WORKFLOW** — Crie um novo workflow (abre o [Construtor Avançado de Workflows](advanced-workflow-builder/))
- **MODELOS** — Navegue e carregue modelos de workflow salvos
- **IMPORTAR WORKFLOW** — Importe um workflow a partir de um arquivo JSON

## Aba Lista do Gerenciador de Testes

A Lista do Gerenciador de Testes mostra todas as configurações e resultados de testes de workflow. Use-a para configurar cenários de teste automatizados para seus workflows.

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Lista do Gerenciador de Testes de Workflow com cenários de teste e Run All Tests"><figcaption><p>A Lista do Gerenciador de Testes — cada cenário mostra um resultado de aprovação/reprovação; use <strong>Run All Tests</strong> para reexecutar todos.</p></figcaption></figure>

## Aba Licença

A aba Licença exibe o status atual da sua licença DocFlow e os recursos disponíveis.

## Aba Card SDK

A aba Card SDK permite que você construa e gerencie cards de workflow personalizados (cards de parceiros) que estendem as funcionalidades nativas do DocFlow.

<!-- screenshot: Card SDK page with Upload ZIP and Submissions tabs -->

### Upload ZIP

Faça o upload de um aplicativo de parceiro como um arquivo ZIP contendo:
- `app.json` — Metadados e configuração do card
- `.docflowcompose/flow/` — Arquivos de definição do card

Tamanho máximo do arquivo: **10 MB**. Clique em **Upload & Validate** para enviar o card para revisão.

### Importação do GitHub

Importe cards de parceiros diretamente de um repositório do GitHub em vez de fazer upload de um arquivo ZIP.

### Submissões

Visualize e gerencie todos os cards de parceiros submetidos:

<!-- screenshot: Card SDK Submissions list with status badges -->

| Coluna | Descrição |
|---|---|
| **Card Name** | Nome do aplicativo de parceiro e do card |
| **card_type_label** | Tipo do card (`Action_card` ou `Condition_card`) |
| **Version** | Número da versão do card |
| **Submitted** | Data de submissão |
| **Status** | Status atual da revisão |
| **Ações** | Ações disponíveis com base no status |

#### Status dos Cards

| Status | Significado | Ações disponíveis |
|---|---|---|
| **Validated** | O card passou na validação | Download, Aprovar, Rejeitar |
| **Approved** | O card está ativo e disponível nos workflows | Download, Desativar, Revogar |
| **Rejected** | O card não passou na revisão | Excluir |
| **Disabled** | O card foi desativado | Excluir |

### Baixar Modelo do SDK

Clique em **Download SDK Template** para obter um modelo inicial para construir seus próprios cards personalizados. O modelo inclui a estrutura de arquivos necessária e exemplos de configuração.

{% hint style="info" %}
Cards de parceiros também podem ser gerenciados programaticamente por meio das [ferramentas DocFlow MCP](../../../advanced-functions-and-tools/docflow-mcp/). Use as ferramentas MCP do Card SDK para criar, validar, aprovar e testar cards a partir do seu IDE ou scripts de automação.
{% endhint %}
