# Workflow Tools

DocFlow MCP exposes tools for managing and testing advanced workflows, plus tools for reading workflow logs and managing workflow variables.

{% hint style="info" %}
**Tool names through the DocBits MCP gateway.** When you connect through the unified DocBits MCP (`api.docbits.com/v3/mcp`), every DocFlow tool carries the prefix `docflow_`: `list_workflows` is called `docflow_list_workflows`, `run_workflow_with_assertions` is `docflow_run_workflow_with_assertions`. The parameters are identical. The names below are the bare DocFlow names.

Workflows are **created and edited in the DocFlow designer** in the web app. The MCP reads, tests, runs and deletes them; it does not create or modify workflow graphs.
{% endhint %} The Card SDK tools live in their own page, see [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

List all workflows for the current organization.

**Parameters:** None

## get\_workflow

Get details of a specific workflow including its node and edge structure.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workflow_id` | string | Yes | UUID of the workflow |

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

## list\_workflow\_variables

List all workflow variables of the organization with name, type and current value.

**Parameters:** None

## set\_workflow\_variable

Create a workflow variable or update its value. Document-type variables have no value of their own; they are set by the workflow at run time.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Variable name |
| `value` | string | No | New value |
| `var_type` | string | No | Variable type when creating (for example `string`, `number`, `document`) |

## search\_workflow\_logs

Search workflow execution logs to find out why runs failed, succeeded or hit a condition mismatch.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workflow_id` | string | No | Limit to one workflow |
| `doc_id` | string | No | Limit to runs for one document |
| `status` | string | No | Run status to filter by |
| `keyword` | string | No | Free-text filter on the log |
| `include_workflow_data` | boolean | No | Include the workflow definition snapshot per run |
| `limit` / `offset` | integer | No | Paging |

## get\_workflow\_log\_detail

Full detail of one run: the raw card execution logs and the workflow definition as it was at run time.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `log_id` | string | Yes | Log entry id from `search_workflow_logs` |

## run\_workflow\_with\_assertions

Seed workflow variables, run an advanced workflow with the real executor and check the outcome against the database. Variables are real writes, not mocks, use it to integration-test a workflow from an assistant.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workflow_id` | string | Yes | UUID of the workflow to run |
| `doc_id` | string | No | Document to run the workflow against |
| `seed_variables` | array | No | Variables to create or update before the run; document-type variables can point at a `doc_id` via `value` |

