# Ferramentas de Workflow

O DocFlow MCP expõe ferramentas para gerenciar e testar workflows avançados, além de ferramentas para ler logs de workflow e gerenciar variáveis de workflow. As ferramentas Card SDK estão em sua própria página — veja [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

Listar todos os workflows da organização atual.

**Parâmetros:** Nenhum

## get\_workflow

Obter detalhes de um workflow específico, incluindo sua estrutura de nós e arestas.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sim | UUID do workflow |

## create\_advanced\_workflow

Criar um novo workflow avançado com nós e arestas.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `name` | string | Sim | Nome do workflow (3-126 caracteres) |
| `description` | string | Não | Descrição opcional |
| `nodes` | array | Sim | Array de nós do workflow |
| `edges` | array | Sim | Array de arestas conectando os nós |

### Estrutura dos Nós

Cada nó requer:

| Campo | Tipo | Descrição |
|-------|------|-------------|
| `node_id` | string | Identificador único do nó |
| `node_type` | string | Veja os tipos de nó abaixo |
| `position` | object | `{x: number, y: number}` posição no canvas |
| `label` | string | Rótulo de exibição |
| `card` | object | Configuração do card (obrigatório para `when`, `and`, `then` — veja abaixo) |

**Tipos de nó:**

| Tipo | Card requerido | Propósito |
|------|------------------|---------|
| `start` | Sem card | Nó de disparo — ponto de entrada do workflow |
| `when` | Card de condição | Condição de disparo (também ponto de entrada válido) |
| `and` | Card de condição | Porta de condição adicional após um `when` |
| `or` | Sem card | Nó de ramificação — prossegue se algum dos ramos de entrada for bem-sucedido |
| `then` | Card de ação | Ação a executar |
| `delay` | Sem card | Nó de espera — pausa a execução por uma duração configurada |
| `all` | Sem card | Nó de junção — aguarda todos os ramos de entrada |
| `any` | Sem card | Nó de junção — prossegue com o primeiro ramo de entrada |
| `note` | Sem card | Anotação adesiva / anotação; não é executada |

### Estrutura das Arestas

Cada aresta requer:

| Campo | Tipo | Descrição |
|-------|------|-------------|
| `edge_id` | string | Identificador único da aresta |
| `source_node_id` | string | ID do nó de origem |
| `target_node_id` | string | ID do nó de destino |
| `source_handle` | string | `success`, `error` ou `failed_condition` (opcional) |
| `target_handle` | string | `input` (opcional) |

**Handles de origem:**

- `success` — tomado quando o nó de origem é bem-sucedido (disponível em todo nó executável).
- `failed_condition` — tomado quando um card de condição `when` ou `and` é avaliado como false.
- `error` — tomado quando um nó `and` ou `then` levanta um erro.

### Configuração do Card

Cards definem o que um nó faz. Use `list_cards` ou `sdk_list_cards_picker` para obter os cards disponíveis.

```json
{
  "id": "card-uuid-here",
  "card_type": "document_type_is",
  "version": 1,
  "variables": [
    {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
  ]
}
```

{% hint style="info" %}
Você só precisa fornecer `id`, `card_type`, `version` e `variables` para cada card. O servidor enriquece os cards automaticamente com metadados de exibição (svg, text, category) do banco de dados.
{% endhint %}

**Exemplo de Requisição:**

```json
{
  "name": "Simple Invoice Router",
  "description": "Routes invoices to approval",
  "nodes": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "position": {"x": 100, "y": 100},
      "label": "Document is Invoice",
      "card": {
        "id": "card-uuid",
        "card_type": "document_type_is",
        "version": 1,
        "variables": [
          {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "then-1",
      "node_type": "then",
      "position": {"x": 100, "y": 300},
      "label": "Send Notification",
      "card": {
        "id": "card-uuid-2",
        "card_type": "send_email",
        "version": 1,
        "variables": []
      }
    }
  ],
  "edges": [
    {
      "edge_id": "e1",
      "source_node_id": "when-1",
      "target_node_id": "then-1",
      "source_handle": "success",
      "target_handle": "input"
    }
  ]
}
```

## update\_advanced\_workflow

Atualizar um workflow avançado existente. Você pode atualizar qualquer combinação de nome, descrição, nós e arestas.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sim | UUID do workflow a atualizar |
| `name` | string | Não | Novo nome |
| `description` | string | Não | Nova descrição |
| `nodes` | array | Não | Novos nós (substitui todos os nós existentes) |
| `edges` | array | Não | Novas arestas (substitui todas as arestas existentes) |

## delete\_workflow

Excluir um workflow por ID (exclusão suave).

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sim | UUID do workflow a excluir |

## test\_advanced\_workflow

Testar a execução de um workflow avançado. Opcionalmente forneça um ID de documento para testar com um documento real.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sim | UUID do workflow avançado |
| `doc_id` | string | Não | UUID de um documento para testar |

## list\_test\_scenarios

Listar todos os cenários de teste de workflows da organização.

**Parâmetros:** Nenhum

## list\_cards

Listar todos os cards de workflow disponíveis com suas condições e configuração.

**Parâmetros:** Nenhum

{% hint style="info" %}
Os cards têm flags de papel: `when_condition` (disparador), `and_condition` (condição adicional) e `then_condition` (ação). Use-as para determinar em quais tipos de nó um card pode ser usado.
{% endhint %}
