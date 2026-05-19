# DocFlow MCP

DocFlow exposes a **Model Context Protocol (MCP)** server that lets AI assistants manage workflows and partner cards programmatically. Any MCP-compatible client — Claude Code, Claude Desktop, OpenAI Codex, or custom integrations — can connect and use these tools.

## What Can You Do?

With DocFlow MCP you can:

- **List, create, update, and delete** advanced workflows
- **Test workflows** with real or mock documents
- **Build custom cards** using the Partner Card SDK
- **Validate, test, approve, and manage** partner card submissions
- **Import cards** directly from GitHub repositories

## Tools Overview

DocFlow MCP groups its tools into the following categories. Most workflow- and Card-SDK tools mirror existing REST endpoints — see the API reference for those. The categories below cover the MCP-specific surface and the workflow concepts you need to use it.

### Workflow Management

| Tool | Description |
|------|-------------|
| `list_workflows` | List all workflows for the current organization |
| `get_workflow` | Get details of a specific workflow by ID |
| `create_advanced_workflow` | Create a new advanced workflow with nodes and edges |
| `update_advanced_workflow` | Update an existing advanced workflow |
| `delete_workflow` | Delete a workflow by ID |

### Workflow Testing

| Tool | Description |
|------|-------------|
| `test_advanced_workflow` | Test an advanced workflow execution with optional document |
| `list_test_scenarios` | List all workflow test scenarios |
| `list_cards` | List available workflow cards/actions |

### Card SDK Management

| Tool | Description |
|------|-------------|
| `sdk_list_submissions` | List all partner card submissions |
| `sdk_get_submission_status` | Get validation status for a submission |
| `sdk_approve_card` | Approve a validated partner card (admin) |
| `sdk_reject_card` | Reject a partner card submission (admin) |
| `sdk_delete_submission` | Deactivate or delete a submission (admin) |
| `sdk_list_cards_picker` | List all enabled cards with role flags |

### Card SDK Development

| Tool | Description |
|------|-------------|
| `sdk_create_card` | Create a new partner card from source code |
| `sdk_validate_card` | Run validation pipeline without saving |
| `sdk_test_card` | Execute a card in a sandboxed environment |
| `sdk_import_github` | Import a partner app from GitHub |

## Getting Started

1. [Set up your MCP client](setup-and-configuration.md)
2. Learn about [Workflow Tools](workflow-tools.md)
3. Explore the [Card SDK Tools](card-sdk-tools.md)
4. Follow end-to-end [Examples](examples.md)

{% hint style="info" %}
DocFlow MCP uses **Streamable HTTP** transport. The server endpoint is `/v3/mcp/` on the DocFlow host (e.g. `https://docflow.docbits.com/v3/mcp/`). See [Setup & Configuration](setup-and-configuration.md) for the full URL list.
{% endhint %}
