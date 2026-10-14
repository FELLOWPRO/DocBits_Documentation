# Esempi

Esempi completi end-to-end che mostrano come utilizzare insieme gli strumenti DocFlow MCP.

## Esempio 1: Creare una Card Personalizzata e Usarla in un Workflow

Questo esempio illustra il ciclo di vita completo: creare una card partner, validarla, testarla, approvarla e costruire un workflow che la utilizza.

### Passo 1: Creare la Card

Chiama `sdk_create_card`:

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

Prendi nota del `card_id` dalla risposta -- ti servira' nei passaggi successivi.

### Passo 2: Validare la Card

Chiama `sdk_validate_card` con l'ID della card:

```json
{
  "card_id": "returned-card-uuid"
}
```

Esamina il report di validazione. Tutte e 5 le fasi dovrebbero essere superate.

### Passo 3: Testare la Card

Chiama `sdk_test_card` con un contesto documento simulato:

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

Verifica che la risposta mostri `CardStatus.SUCCESS`.

### Passo 4: Approvare la Card

Chiama `sdk_approve_card` (richiesto admin):

```json
{
  "card_id": "returned-card-uuid"
}
```

La card e' ora attiva e disponibile per l'utilizzo nei workflow.

### Passo 5: Costruire un Workflow con la Card

Apri il **designer DocFlow** nell'app web, crea un workflow avanzato e aggiungi la card approvata come nodo, ad esempio un trigger *Documento ricevuto*, la card *High Value Check* e un nodo *Approvazione* per il ramo `true`. I grafi dei workflow vengono creati e modificati nel designer; l'MCP non li crea.

Di nuovo nell'assistente, verifica che il workflow esista e leggine la struttura:

```json
{
  "tool": "get_workflow",
  "workflow_id": "<id da list_workflows>"
}
```

### Passo 6: Testare il Workflow

Chiama `test_advanced_workflow`:

```json
{
  "workflow_id": "new-workflow-uuid"
}
```

Esamina i log di esecuzione per verificare che ogni nodo sia stato eseguito correttamente.

---

## Esempio 2: Costruire un Workflow con Card Integrate

Questo esempio crea un workflow utilizzando solo card integrate (nessuna card personalizzata necessaria).

### Passo 1: Scoprire le Card Disponibili

Chiama `sdk_list_cards_picker` per visualizzare tutte le card disponibili con i relativi flag di ruolo:

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

Filtra per ruolo:
- `is_when: true` -- Usa nei nodi WHEN (trigger)
- `is_and: true` -- Usa nei nodi AND (condizioni aggiuntive)
- `is_then: true` -- Usa nei nodi THEN (azioni)

### Passo 2: Creare il Workflow

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

Questo crea un workflow: **WHEN** il documento e' una fattura **AND** l'importo > 1000 **THEN** imposta lo stato su revisione.

---

## Esempio 3: Importare Card da GitHub

Se le tue card partner si trovano in un repository GitHub, puoi importarle direttamente:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main"
}
```

Per repository privati, includi un token GitHub:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main",
  "token": "ghp_your_token_here"
}
```

Dopo l'importazione, le card vengono validate automaticamente. Controlla il loro stato con `sdk_list_submissions` e approvale con `sdk_approve_card`.
