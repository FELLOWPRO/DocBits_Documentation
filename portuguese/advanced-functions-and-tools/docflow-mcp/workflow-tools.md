# Ferramentas de workflow

O DocFlow MCP expõe ferramentas para gerenciar e testar workflows avançados, além de ferramentas para ler os logs de workflow e gerenciar as variáveis de workflow.

{% hint style="info" %}
**Nomes das ferramentas pelo gateway MCP do DocBits.** Ao se conectar pelo MCP unificado do DocBits (`api.docbits.com/v3/mcp`), toda ferramenta do DocFlow recebe o prefixo `docflow_`: `list_workflows` passa a se chamar `docflow_list_workflows` e `run_workflow_with_assertions` passa a ser `docflow_run_workflow_with_assertions`. Os parâmetros são idênticos. Os nomes abaixo são os nomes simples do DocFlow.

Os workflows são **criados e editados no designer do DocFlow** no aplicativo web. O MCP lê, testa, executa e exclui workflows; ele não cria nem modifica grafos de workflow.
{% endhint %}

As ferramentas do Card SDK ficam em uma página própria, consulte [Ferramentas do Card SDK](card-sdk-tools.md).

## list\_workflows

Lista todos os workflows da organização atual.

**Parâmetros:** nenhum

## get\_workflow

Obtém os detalhes de um workflow específico, incluindo a estrutura de nós e arestas.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sim | UUID do workflow |

## delete\_workflow

Exclui um workflow pelo ID (exclusão lógica).

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sim | UUID do workflow a excluir |

## test\_advanced\_workflow

Testa a execução de um workflow avançado. Opcionalmente, informe o ID de um documento para testar com um documento real.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sim | UUID do workflow avançado |
| `doc_id` | string | Não | UUID de um documento para testar |

## list\_test\_scenarios

Lista todos os cenários de teste de workflow da organização.

**Parâmetros:** nenhum

## list\_cards

Lista todos os cartões de workflow disponíveis com suas condições e configuração.

**Parâmetros:** nenhum

{% hint style="info" %}
Os cartões têm indicadores de função: `when_condition` (gatilho), `and_condition` (condição adicional) e `then_condition` (ação). Use-os para determinar em quais tipos de nó um cartão pode ser usado.
{% endhint %}

## list\_workflow\_variables

Lista todas as variáveis de workflow da organização com nome, tipo e valor atual.

**Parâmetros:** nenhum

## set\_workflow\_variable

Cria uma variável de workflow ou atualiza o valor dela. As variáveis do tipo documento não têm valor próprio; elas são definidas pelo workflow em tempo de execução.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `name` | string | Sim | Nome da variável |
| `value` | string | Não | Novo valor |
| `var_type` | string | Não | Tipo da variável ao criar (por exemplo `string`, `number`, `document`) |

## search\_workflow\_logs

Pesquisa os logs de execução de workflows para descobrir por que as execuções falharam, tiveram sucesso ou encontraram uma condição não atendida.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Não | Limita a um workflow |
| `doc_id` | string | Não | Limita às execuções de um documento |
| `status` | string | Não | Status da execução para filtrar |
| `keyword` | string | Não | Filtro de texto livre no log |
| `include_workflow_data` | boolean | Não | Inclui o snapshot da definição do workflow por execução |
| `limit` / `offset` | integer | Não | Paginação |

## get\_workflow\_log\_detail

Detalhes completos de uma execução: os logs brutos de execução dos cartões e a definição do workflow como estava no momento da execução.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `log_id` | string | Sim | ID da entrada de log obtido em `search_workflow_logs` |

## run\_workflow\_with\_assertions

Preenche variáveis de workflow, executa um workflow avançado com o executor real e verifica o resultado no banco de dados. As variáveis são gravações reais, não simulações; use-o para fazer testes de integração de um workflow a partir de um assistente.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sim | UUID do workflow a executar |
| `doc_id` | string | Não | Documento no qual o workflow será executado |
| `seed_variables` | array | Não | Variáveis a criar ou atualizar antes da execução; variáveis do tipo documento podem apontar para um `doc_id` por meio de `value` |
