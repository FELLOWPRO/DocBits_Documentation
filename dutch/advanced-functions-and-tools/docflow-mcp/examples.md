# Voorbeelden

Volledige end-to-end voorbeelden die laten zien hoe u DocFlow MCP-tools samen kunt gebruiken.

## Voorbeeld 1: Een aangepaste kaart aanmaken en gebruiken in een workflow

Dit voorbeeld doorloopt de volledige levenscyclus: een partnerkaart aanmaken, valideren, testen, goedkeuren en een workflow bouwen die deze gebruikt.

### Stap 1: De kaart aanmaken

Roep `sdk_create_card` aan:

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

Noteer het `card_id` uit de respons — u heeft dit nodig in de volgende stappen.

### Stap 2: De kaart valideren

Roep `sdk_validate_card` aan met het kaart-ID:

```json
{
  "card_id": "returned-card-uuid"
}
```

Bekijk het validatierapport. Alle 5 fasen moeten slagen.

### Stap 3: De kaart testen

Roep `sdk_test_card` aan met een gesimuleerde documentcontext:

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

Controleer of de respons `CardStatus.SUCCESS` toont.

### Stap 4: De kaart goedkeuren

Roep `sdk_approve_card` aan (vereist admin):

```json
{
  "card_id": "returned-card-uuid"
}
```

De kaart is nu actief en beschikbaar voor gebruik in workflows.

### Stap 5: Een workflow bouwen met de kaart

Open de **DocFlow-designer** in de webapp, maak een geavanceerde workflow en voeg de goedgekeurde kaart toe als node, bijvoorbeeld een trigger *Document Received*, de kaart *High Value Check* en een node *Approval* voor de `true`-tak. Workflowgrafen worden in de designer aangemaakt en bewerkt; de MCP maakt ze niet aan.

Terug in de assistent controleert u of de workflow bestaat en leest u de structuur ervan:

```json
{
  "tool": "get_workflow",
  "workflow_id": "<id uit list_workflows>"
}
```

### Stap 6: De workflow testen

Roep `test_advanced_workflow` aan:

```json
{
  "workflow_id": "new-workflow-uuid"
}
```

Bekijk de uitvoeringslogboeken om te verifiëren dat elke node correct is uitgevoerd.

---

## Voorbeeld 2: Een workflow bouwen met ingebouwde kaarten

Dit voorbeeld maakt een workflow aan met alleen ingebouwde kaarten (geen aangepaste kaarten nodig).

### Stap 1: Beschikbare kaarten ontdekken

Roep `sdk_list_cards_picker` aan om alle beschikbare kaarten met hun rolvlaggen te bekijken:

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

Filter op rol:
- `is_when: true` — Gebruik in WHEN-nodes (triggers)
- `is_and: true` — Gebruik in AND-nodes (aanvullende voorwaarden)
- `is_then: true` — Gebruik in THEN-nodes (acties)

### Stap 2: De workflow aanmaken

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

Dit maakt een workflow aan: **WHEN** document is een factuur **AND** bedrag > 1000 **THEN** status instellen op beoordeling.

---

## Voorbeeld 3: Kaarten importeren vanuit GitHub

Als uw partnerkaarten zich in een GitHub-repository bevinden, kunt u ze rechtstreeks importeren:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main"
}
```

Voor privérepositories voegt u een GitHub-token toe:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main",
  "token": "ghp_your_token_here"
}
```

Na het importeren doorlopen de kaarten automatisch de validatie. Controleer hun status met `sdk_list_submissions` en keur ze goed met `sdk_approve_card`.
