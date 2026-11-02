# Exemplos

Exemplos completos de ponta a ponta mostrando como usar as ferramentas do DocFlow MCP em conjunto.

## Exemplo 1: Criar um Card Personalizado e Usá-lo em um Workflow

Este exemplo percorre o ciclo de vida completo: criar um card de parceiro, validá-lo, testá-lo, aprová-lo e construir um workflow que o utiliza.

### Passo 1: Criar o Card

Chame `sdk_create_card`:

```json
{
  "app_manifest": {
    "id": "com.example.invoice-tools",
    "name": "Invoice Tools",
    "version": "1.0.0",
    "partner": {
      "id": "example-partner",
      "name": "Example Corp"
    }
  },
  "card_manifest": {
    "id": "high-value-check",
    "title": {"en": "High Value Invoice Check"},
    "entry_point": "src/high_value.py",
    "class_name": "HighValueCheck",
    "args": [
      {
        "id": "threshold",
        "title": {"en": "Amount Threshold"},
        "type": "number",
        "required": true
      }
    ]
  },
  "card_type": "condition",
  "source_code": "from api.sdk.base import PartnerCard\nfrom api.sdk.result import CardResult, CardStatus\n\nclass HighValueCheck(PartnerCard):\n    def execute(self, context):\n        threshold = float(self.variables.get('threshold', 1000))\n        total = float(context.document_fields.get('total_amount', 0))\n        if total > threshold:\n            return CardResult(status=CardStatus.SUCCESS, message=f'High value: {total}')\n        return CardResult(status=CardStatus.FAILURE, message=f'Below threshold: {total}')",
  "test_code": "def test_high_value():\n    assert True  # Basic test"
}
```

Anote o `card_id` da resposta - você precisará dele nos passos seguintes.

### Passo 2: Validar o Card

Chame `sdk_validate_card` com o ID do card:

```json
{
  "card_id": "returned-card-uuid"
}
```

Revise o relatório de validação. Todas as 5 etapas devem passar.

### Passo 3: Testar o Card

Chame `sdk_test_card` com um contexto de documento simulado:

```json
{
  "card_id": "returned-card-uuid",
  "variables": {"threshold": "1000"},
  "mock_context": {
    "document_type": "INVOICE",
    "document_fields": {
      "total_amount": "2500.00",
      "currency": "EUR"
    }
  }
}
```

Verifique se a resposta mostra `CardStatus.SUCCESS`.

### Passo 4: Aprovar o Card

Chame `sdk_approve_card` (requer admin):

```json
{
  "card_id": "returned-card-uuid"
}
```

O card agora está ativo e disponível para uso em workflows.

### Passo 5: Construir um Workflow com o Card

Abra o **designer do DocFlow** na aplicação web, crie um workflow avançado e adicione o card aprovado como um nó, por exemplo um gatilho *Document Received*, o card *High Value Check* e um nó *Approval* para o ramo `true`. Os grafos de workflow são criados e editados no designer; o MCP não os cria.

De volta ao assistente, confirme que o workflow existe e leia a sua estrutura:

```json
{
  "tool": "get_workflow",
  "workflow_id": "<id obtido de list_workflows>"
}
```

### Passo 6: Testar o Workflow

Chame `test_advanced_workflow`:

```json
{
  "workflow_id": "new-workflow-uuid"
}
```

Revise os logs de execução para verificar se cada nó foi executado corretamente.

---

## Exemplo 2: Construir um Workflow com Cards Integrados

Este exemplo cria um workflow usando apenas cards integrados (sem necessidade de cards personalizados).

### Passo 1: Descobrir os Cards Disponíveis

Chame `sdk_list_cards_picker` para ver todos os cards disponíveis com suas flags de função:

```json
// Response includes cards like:
{
  "card_id": "doc-type-uuid",
  "card_name": "Document Type Is",
  "is_when": true,
  "is_and": false,
  "is_then": false
}
```

Filtre por função:
- `is_when: true` — Use em nós WHEN (gatilhos)
- `is_and: true` — Use em nós AND (condições adicionais)
- `is_then: true` — Use em nós THEN (ações)

### Passo 2: Criar o Workflow

```json
{
  "name": "Invoice Document Type Router",
  "description": "When document is an invoice, apply validation",
  "nodes": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "position": {"x": 250, "y": 50},
      "label": "Document is Invoice",
      "card": {
        "id": "doc-type-card-uuid",
        "card_type": "document_type_is",
        "version": 1,
        "variables": [
          {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "and-1",
      "node_type": "and",
      "position": {"x": 250, "y": 200},
      "label": "Amount > 1000",
      "card": {
        "id": "amount-card-uuid",
        "card_type": "field_value_check",
        "version": 1,
        "variables": [
          {"id": "field-var", "data": "total_amount", "data_type": "string"},
          {"id": "op-var", "data": ">", "data_type": "string"},
          {"id": "val-var", "data": "1000", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "then-1",
      "node_type": "then",
      "position": {"x": 250, "y": 350},
      "label": "Set Status to Review",
      "card": {
        "id": "status-card-uuid",
        "card_type": "set_document_status",
        "version": 1,
        "variables": [
          {"id": "status-var", "data": "review", "data_type": "string"}
        ]
      }
    }
  ],
  "edges": [
    {
      "edge_id": "e1",
      "source_node_id": "when-1",
      "target_node_id": "and-1",
      "source_handle": "success",
      "target_handle": "input"
    },
    {
      "edge_id": "e2",
      "source_node_id": "and-1",
      "target_node_id": "then-1",
      "source_handle": "success",
      "target_handle": "input"
    }
  ]
}
```

Isso cria um workflow: **WHEN** o documento é uma fatura **AND** o valor > 1000 **THEN** definir status como revisão.

---

## Exemplo 3: Importar Cards do GitHub

Se seus cards de parceiros estão em um repositório GitHub, você pode importá-los diretamente:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main"
}
```

Para repositórios privados, inclua um token do GitHub:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main",
  "token": "ghp_your_token_here"
}
```

Após a importação, os cards passam pela validação automaticamente. Verifique o status com `sdk_list_submissions` e aprove-os com `sdk_approve_card`.
