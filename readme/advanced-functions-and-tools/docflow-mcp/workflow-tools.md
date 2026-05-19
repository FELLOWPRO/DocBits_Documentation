# Workflow Tools

DocFlow MCP exposes tools for managing and testing advanced workflows, plus tools for reading workflow logs and managing workflow variables. The Card SDK tools live in their own page — see [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

List all workflows for the current organization.

**Parameters:** None

## get\_workflow

Get details of a specific workflow including its node and edge structure.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workflow_id` | string | Yes | UUID of the workflow |

## create\_advanced\_workflow

Create a new advanced workflow with nodes and edges.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Workflow name (3-126 characters) |
| `description` | string | No | Optional description |
| `nodes` | array | Yes | Array of workflow nodes |
| `edges` | array | Yes | Array of edges connecting nodes |

### Node Structure

Each node requires:

| Field | Type | Description |
|-------|------|-------------|
| `node_id` | string | Unique identifier for the node |
| `node_type` | string | See node types below |
| `position` | object | `{x: number, y: number}` position on canvas |
| `label` | string | Display label |
| `card` | object | Card configuration (required for `when`, `and`, `then` — see below) |

**Node types:**

| Type | Card requirement | Purpose |
|------|------------------|---------|
| `start` | No card | Trigger node — entry point of the workflow |
| `when` | Condition card | Trigger condition (also a valid entry point) |
| `and` | Condition card | Additional condition gate after a `when` |
| `or` | No card | Branch node — proceeds if any incoming branch succeeds |
| `then` | Action card | Action to execute |
| `delay` | No card | Wait node — pauses execution for a configured duration |
| `all` | No card | Merge node — waits for all incoming branches |
| `any` | No card | Merge node — proceeds on the first incoming branch |
| `note` | No card | Sticky note / annotation; not executed |

### Edge Structure

Each edge requires:

| Field | Type | Description |
|-------|------|-------------|
| `edge_id` | string | Unique identifier for the edge |
| `source_node_id` | string | ID of the source node |
| `target_node_id` | string | ID of the target node |
| `source_handle` | string | `success`, `error`, or `failed_condition` (optional) |
| `target_handle` | string | `input` (optional) |

**Source handles:**

- `success` — taken when the source node succeeds (available on every executable node).
- `failed_condition` — taken when a `when` or `and` condition card evaluates to false.
- `error` — taken when an `and` or `then` node raises an error.

### Card Configuration

Cards define what a node does. Use `list_cards` or `sdk_list_cards_picker` to get available cards.

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
You only need to provide `id`, `card_type`, `version`, and `variables` for each card. The server automatically enriches cards with display metadata (svg, text, category) from the database.
{% endhint %}

**Example Request:**

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

Update an existing advanced workflow. You can update any combination of name, description, nodes, and edges.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workflow_id` | string | Yes | UUID of workflow to update |
| `name` | string | No | New name |
| `description` | string | No | New description |
| `nodes` | array | No | New nodes (replaces all existing nodes) |
| `edges` | array | No | New edges (replaces all existing edges) |

## delete\_workflow

Delete a workflow by ID (soft delete).

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workflow_id` | string | Yes | UUID of workflow to delete |

## test\_advanced\_workflow

Test an advanced workflow execution. Optionally provide a document ID to test with a real document.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workflow_id` | string | Yes | UUID of the advanced workflow |
| `doc_id` | string | No | UUID of a document to test with |

## list\_test\_scenarios

List all workflow test scenarios for the organization.

**Parameters:** None

## list\_cards

List all available workflow cards with their conditions and configuration.

**Parameters:** None

{% hint style="info" %}
Cards have role flags: `when_condition` (trigger), `and_condition` (additional condition), and `then_condition` (action). Use these to determine which node types a card can be used in.
{% endhint %}
