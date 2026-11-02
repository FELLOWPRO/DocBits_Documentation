# Examples

Complete end-to-end examples showing how to use DocFlow MCP tools together.

## Example 1: Create a Custom Card and Use It in a Workflow

This example walks through the full lifecycle: create a partner card, validate it, test it, approve it, and build a workflow that uses it.

### Step 1: Create the Card

Call `sdk_create_card`:

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

Note the `card_id` from the response — you'll need it in the following steps.

### Step 2: Validate the Card

Call `sdk_validate_card` with the card ID:

```json
{
  "card_id": "returned-card-uuid"
}
```

Review the validation report. All 5 stages should pass.

### Step 3: Test the Card

Call `sdk_test_card` with a mock document context:

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

Verify the response shows `CardStatus.SUCCESS`.

### Step 4: Approve the Card

Call `sdk_approve_card` (requires admin):

```json
{
  "card_id": "returned-card-uuid"
}
```

The card is now active and available for use in workflows.

### Step 5: Build a Workflow with the Card

Open the **DocFlow designer** in the web app, create an advanced workflow and add the approved card as a node, for example a *Document Received* trigger, the *High Value Check* card, and an *Approval* node for the `true` branch. Workflow graphs are created and edited in the designer; the MCP does not create them.

Back in the assistant, confirm the workflow exists and read its structure:

```json
{
  "tool": "get_workflow",
  "workflow_id": "<id from list_workflows>"
}
```

### Step 6: Test the Workflow

Call `test_advanced_workflow`:

```json
{
  "workflow_id": "new-workflow-uuid"
}
```

Review the execution logs to verify each node executed correctly.

---

## Example 2: Build a Workflow with Built-in Cards

This example creates a workflow using only built-in cards (no custom cards needed).

### Step 1: Discover Available Cards

Call `sdk_list_cards_picker` to see all available cards with their role flags:

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

Filter by role:
- `is_when: true` — Use in WHEN nodes (triggers)
- `is_and: true` — Use in AND nodes (additional conditions)
- `is_then: true` — Use in THEN nodes (actions)

### Step 2: Create the Workflow

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

This creates a workflow: **WHEN** document is an invoice **AND** amount > 1000 **THEN** set status to review.

---

## Example 3: Import Cards from GitHub

If your partner cards are in a GitHub repository, you can import them directly:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main"
}
```

For private repositories, include a GitHub token:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main",
  "token": "ghp_your_token_here"
}
```

After import, the cards go through validation automatically. Check their status with `sdk_list_submissions` and approve them with `sdk_approve_card`.
