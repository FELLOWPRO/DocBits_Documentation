# Ferramentas de Workflow

O DocFlow MCP fornece ferramentas para gerir e testar workflows avançados, bem como ferramentas para ler os registos de workflows e gerir variáveis de workflow.

{% hint style="info" %}
**Nomes das ferramentas através do gateway DocBits MCP.** Quando se liga através do DocBits MCP unificado (`api.docbits.com/v3/mcp`), todas as ferramentas do DocFlow têm o prefixo `docflow_`: `list_workflows` chama-se `docflow_list_workflows`, `run_workflow_with_assertions` é `docflow_run_workflow_with_assertions`. Os parâmetros são idênticos. Os nomes abaixo são os nomes simples do DocFlow.

Os workflows são **criados e editados no designer do DocFlow** na aplicação web. O MCP lê, testa, executa e elimina workflows; não cria nem modifica grafos de workflow.
{% endhint %} As ferramentas do SDK de Cards têm a sua própria página, ver [Ferramentas do SDK de Cards](card-sdk-tools.md).

## list\_workflows

Lista todos os workflows da organização atual.

**Parâmetros:** Nenhum

**Exemplo de Resposta:**

```json
[
  {
    "id": "a1b2c3d4-...",
    "name": "Invoice Approval",
    "version": 3,
    "enabled": true,
    "doc_types": ["INVOICE"],
    "workflow_type": "advanced",
    "created_on": "2025-01-15 10:30:00",
    "last_modified_on": "2025-03-20 14:22:00"
  }
]
```

## get\_workflow

Obtém detalhes de um workflow específico, incluindo sua estrutura de nós e arestas.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sim | UUID do workflow |

**Exemplo de Resposta:**

```json
{
  "id": "a1b2c3d4-...",
  "name": "Invoice Approval",
  "version": 3,
  "enabled": true,
  "doc_types": ["INVOICE"],
  "workflow_type": "advanced",
  "description": "Routes invoices based on amount",
  "advanced_config": {
    "nodes": [
      {"node_id": "when-1", "node_type": "when", "label": "Amount > 1000"},
      {"node_id": "then-1", "node_type": "then", "label": "Send for Approval"}
    ],
    "edges": [
      {"source_node_id": "when-1", "target_node_id": "then-1"}
    ]
  }
}
```

## delete\_workflow

Exclui um workflow por ID (exclusão lógica).

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sim | UUID do workflow a ser excluído |

**Exemplo de Resposta:**

```json
{
  "success": true,
  "workflow_id": "a1b2c3d4-..."
}
```

## test\_advanced\_workflow

Testa a execução de um workflow avançado. Opcionalmente, forneça um ID de documento para testar com um documento real.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sim | UUID do workflow avançado |
| `doc_id` | string | Não | UUID de um documento para teste |

**Exemplo de Resposta:**

```json
{
  "success": true,
  "workflow_id": "a1b2c3d4-...",
  "execution_time": 0.234,
  "workflow_result": "completed",
  "node_results": {
    "when-1": {"status": "success", "output": true},
    "then-1": {"status": "success"}
  },
  "logs": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "status": "success",
      "error": null,
      "duration_ms": 12
    }
  ]
}
```

## list\_test\_scenarios

Lista todos os cenários de teste de workflow da organização.

**Parâmetros:** Nenhum

**Exemplo de Resposta:**

```json
[
  {
    "id": "scenario-uuid",
    "name": "Invoice over 1000 EUR",
    "workflow_id": "a1b2c3d4-...",
    "enabled": true,
    "status": "passed",
    "last_run": "2025-03-20 14:00:00"
  }
]
```

## list\_cards

Lista todos os cards de workflow disponíveis com suas condições e configuração.

**Parâmetros:** Nenhum

**Exemplo de Resposta:**

```json
[
  {
    "id": "card-uuid",
    "text": "Document Type Is",
    "card_type": "document_type_is",
    "card_version": 1,
    "category": "Document",
    "when_condition": true,
    "and_condition": false,
    "then_condition": false
  },
  {
    "id": "card-uuid-2",
    "text": "Send Email Notification",
    "card_type": "send_email",
    "card_version": 1,
    "category": "Communication",
    "when_condition": false,
    "and_condition": false,
    "then_condition": true
  }
]
```

{% hint style="info" %}
Os cards possuem flags de função: `when_condition` (gatilho), `and_condition` (condição adicional) e `then_condition` (ação). Use-as para determinar em quais tipos de nó um card pode ser utilizado.
{% endhint %}

## list\_workflow\_variables

Lista todas as variáveis de workflow da organização com nome, tipo e valor atual.

**Parâmetros:** Nenhum

## set\_workflow\_variable

Cria uma variável de workflow ou atualiza o seu valor. As variáveis do tipo documento não têm valor próprio; são definidas pelo workflow em tempo de execução.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `name` | string | Sim | Nome da variável |
| `value` | string | Não | Novo valor |
| `var_type` | string | Não | Tipo da variável ao criar (por exemplo `string`, `number`, `document`) |

## search\_workflow\_logs

Pesquisa os registos de execução de workflows para descobrir porque é que as execuções falharam, tiveram sucesso ou encontraram uma condição não satisfeita.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Não | Limitar a um workflow |
| `doc_id` | string | Não | Limitar às execuções de um documento |
| `status` | string | Não | Estado da execução pelo qual filtrar |
| `keyword` | string | Não | Filtro de texto livre sobre o registo |
| `include_workflow_data` | boolean | Não | Incluir o snapshot da definição do workflow por execução |
| `limit` / `offset` | integer | Não | Paginação |

## get\_workflow\_log\_detail

Detalhe completo de uma execução: os registos brutos de execução dos cards e a definição do workflow tal como estava em tempo de execução.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `log_id` | string | Sim | ID da entrada de registo obtido de `search_workflow_logs` |

## run\_workflow\_with\_assertions

Inicializa variáveis de workflow, executa um workflow avançado com o executor real e verifica o resultado na base de dados. As variáveis são escritas reais, não mocks; use-a para testar a integração de um workflow a partir de um assistente.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sim | UUID do workflow a executar |
| `doc_id` | string | Não | Documento contra o qual executar o workflow |
| `seed_variables` | array | Não | Variáveis a criar ou atualizar antes da execução; as variáveis do tipo documento podem apontar para um `doc_id` através de `value` |
