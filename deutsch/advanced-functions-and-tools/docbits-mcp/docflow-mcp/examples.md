# Beispiele

Vollstaendige End-to-End-Beispiele, die zeigen, wie DocFlow MCP Tools zusammen verwendet werden.

## Beispiel 1: Eine benutzerdefinierte Karte erstellen und in einem Workflow verwenden

Dieses Beispiel fuehrt durch den vollstaendigen Lebenszyklus: Eine Partner-Karte erstellen, validieren, testen, genehmigen und einen Workflow damit erstellen.

### Schritt 1: Die Karte erstellen

Rufen Sie `sdk_create_card` auf:

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

Notieren Sie sich die `card_id` aus der Antwort -- Sie benoetigen sie in den folgenden Schritten.

### Schritt 2: Die Karte validieren

Rufen Sie `sdk_validate_card` mit der Karten-ID auf:

```json
{
  "card_id": "returned-card-uuid"
}
```

Ueberpruefen Sie den Validierungsbericht. Alle 5 Stufen sollten bestanden sein.

### Schritt 3: Die Karte testen

Rufen Sie `sdk_test_card` mit einem Mock-Dokumentkontext auf:

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

Ueberpruefen Sie, ob die Antwort `CardStatus.SUCCESS` anzeigt.

### Schritt 4: Die Karte genehmigen

Rufen Sie `sdk_approve_card` auf (erfordert Admin):

```json
{
  "card_id": "returned-card-uuid"
}
```

Die Karte ist nun aktiv und kann in Workflows verwendet werden.

### Schritt 5: Einen Workflow mit der Karte erstellen

Öffnen Sie den **DocFlow-Designer** in der Web-App, erstellen Sie einen erweiterten Workflow und fügen Sie die genehmigte Karte als Knoten hinzu, zum Beispiel einen Auslöser *Document Received*, die Karte *High Value Check* und einen *Approval*-Knoten für den `true`-Zweig. Workflow-Graphen werden im Designer erstellt und bearbeitet; das MCP erstellt sie nicht.

Zurück im Assistenten bestätigen Sie, dass der Workflow existiert, und lesen seine Struktur:

```json
{
  "tool": "get_workflow",
  "workflow_id": "<id aus list_workflows>"
}
```

### Schritt 6: Den Workflow testen

Rufen Sie `test_advanced_workflow` auf:

```json
{
  "workflow_id": "new-workflow-uuid"
}
```

Ueberpruefen Sie die Ausfuehrungsprotokolle, um sicherzustellen, dass jeder Knoten korrekt ausgefuehrt wurde.

---

## Beispiel 2: Einen Workflow mit integrierten Karten erstellen

Dieses Beispiel erstellt einen Workflow, der nur integrierte Karten verwendet (keine benutzerdefinierten Karten erforderlich).

### Schritt 1: Verfuegbare Karten ermitteln

Rufen Sie `sdk_list_cards_picker` auf, um alle verfuegbaren Karten mit ihren Rollen-Flags anzuzeigen:

```json
// Antwort enthaelt Karten wie:
{
  "card_id": "doc-type-uuid",
  "card_name": "Document Type Is",
  "is_when": true,
  "is_and": false,
  "is_then": false
}
```

Filtern Sie nach Rolle:
- `is_when: true` -- Verwendung in WHEN-Knoten (Ausloeser)
- `is_and: true` -- Verwendung in AND-Knoten (zusaetzliche Bedingungen)
- `is_then: true` -- Verwendung in THEN-Knoten (Aktionen)

### Schritt 2: Den Workflow erstellen

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

Dies erstellt einen Workflow: **WHEN** das Dokument eine Rechnung ist **AND** der Betrag > 1000 **THEN** Status auf "Review" setzen.

---

## Beispiel 3: Karten von GitHub importieren

Wenn sich Ihre Partner-Karten in einem GitHub-Repository befinden, koennen Sie diese direkt importieren:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main"
}
```

Fuer private Repositories fuegen Sie ein GitHub-Token hinzu:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main",
  "token": "ghp_your_token_here"
}
```

Nach dem Import durchlaufen die Karten automatisch die Validierung. Ueberpruefen Sie deren Status mit `sdk_list_submissions` und genehmigen Sie sie mit `sdk_approve_card`.
