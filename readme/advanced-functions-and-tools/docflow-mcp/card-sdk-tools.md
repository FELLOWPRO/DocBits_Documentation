# Card SDK Tools

The Card SDK tools let you create, validate, test, and manage custom partner cards through MCP. Partner cards extend DocFlow with custom business logic written in Python.

## Card Lifecycle

A partner card moves through these submission states (`partner_status`):

| State | Meaning | Workflow visibility |
|-------|---------|---------------------|
| `validating` | Submission accepted; validation pipeline is running. | Submitting org only |
| `validated` | All validation stages passed. Awaiting admin approval. | Submitting org only |
| `rejected` | Validation failed, or an admin rejected the card. Source is kept for inspection. | Submitting org only |
| `approved` | Admin approved the card; `enabled = true`. | **All orgs** |
| `disabled` | Previously approved card that an admin deactivated. | Submitting org only |
| `deleted` | Soft-deleted; not returned by submission listings. | Hidden |

{% hint style="warning" %}
**Org visibility:** A partner card is only available to workflow nodes in `list_cards` once it has been **approved**. Approved partner cards are visible to every organization on the platform — approval is a global activation, not a per-org one. Non-approved cards (validating, validated, rejected, disabled) are visible only to the organization that submitted them.
{% endhint %}

Typical flow:

1. **Create** a card with `sdk_create_card` or `sdk_import_github` — runs the validation pipeline and stores the card with `partner_status = validated` (or `rejected` on failure).
2. **Validate** with `sdk_validate_card` to re-check an existing card or dry-run new source code without persisting.
3. **Test** with `sdk_test_card` to execute the card in the sandbox against a mock context.
4. **Approve** with `sdk_approve_card` (organization admin only) — re-runs AST and behavioral validation, then sets `partner_status = approved` and `enabled = true`.
5. Once approved, the card appears in `list_cards` for every org and can be referenced from workflow nodes.

## Development Tools

### sdk\_create\_card

Create a new partner card from source code and manifests. Runs the full validation pipeline (see [Validation Stages](#sdk_validate_card) below) and stores the card in the database. The card lands in `validated` state and requires admin approval before it can be used in workflows.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `app_manifest` | object | Yes | App manifest with id, name, version, partner info |
| `card_manifest` | object | Yes | Card manifest with id, title, entry\_point, class\_name, args |
| `card_type` | string | Yes | `action` or `condition` |
| `source_code` | string | Yes | Python source code (must extend `PartnerCard`) |
| `test_code` | string | Yes | Pytest test code for the card |
| `locales` | object | No | Locale translations, e.g. `{"en": {...}, "de": {...}}` |

**App Manifest Example:**

```json
{
  "id": "com.acme.invoice-tools",
  "name": "Invoice Tools",
  "version": "1.0.0",
  "partner": {
    "id": "acme",
    "name": "Acme Corp"
  }
}
```

**Card Manifest Example:**

```json
{
  "id": "amount-threshold",
  "title": {"en": "Amount Threshold Check"},
  "entry_point": "src/amount_threshold.py",
  "class_name": "AmountThreshold",
  "args": [
    {
      "id": "threshold",
      "title": {"en": "Threshold Amount"},
      "type": "number",
      "required": true
    }
  ]
}
```

**Source Code Example:**

```python
from api.sdk.base import PartnerCard
from api.sdk.context import ExecutionContext
from api.sdk.result import CardResult, CardStatus

class AmountThreshold(PartnerCard):
    def execute(self, context: ExecutionContext) -> CardResult:
        threshold = float(self.variables.get("threshold", 0))
        total = context.document_fields.get("total_amount", 0)
        if float(total) > threshold:
            return CardResult(
                status=CardStatus.SUCCESS,
                message=f"Amount {total} exceeds threshold {threshold}",
            )
        return CardResult(
            status=CardStatus.FAILED,
            message=f"Amount {total} below threshold {threshold}",
        )
```

{% hint style="info" %}
`CardStatus` has three values and they map directly to workflow edges:

| Status | Edge taken | Use it for |
|--------|------------|------------|
| `SUCCESS` | `success` | Card succeeded — applies to both conditions and actions. |
| `FAILED` | `failed_condition` | **Condition cards only.** The condition evaluated to false — the workflow takes the "else" branch. Action cards have no `failed_condition` handle, so returning `FAILED` from an action leaves the run with nowhere to go. |
| `ERROR` | `error` | An unexpected runtime failure (exception). Applies to both conditions and actions. |

In short: actions return `SUCCESS` or `ERROR`; conditions can additionally return `FAILED`.
{% endhint %}

### sdk\_validate\_card

Run the validation pipeline on a partner card without saving. Two modes:

- **Mode A** — Validate an existing card by ID
- **Mode B** — Validate new source code inline

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `card_id` | string | No | UUID of existing card (Mode A) |
| `app_manifest` | object | No | App manifest (Mode B) |
| `card_manifest` | object | No | Card manifest (Mode B) |
| `card_type` | string | No | `action` or `condition` (Mode B) |
| `source_code` | string | No | Python source code (Mode B) |
| `test_code` | string | No | Test code (Mode B) |

{% hint style="info" %}
Provide either `card_id` alone (Mode A) or `app_manifest` + `card_manifest` + `source_code` together (Mode B).
{% endhint %}

**Validation Stages:**

1. **Structure** — Verifies file layout, manifest schema (`app.json`, `.docflowcompose/flow/...`), and that declared entry points exist.
2. **Locales** — Reconciles translation keys used in the card against `locales/<lang>.json` files; fails if a key is missing in a declared language.
3. **AST Analysis** — Walks every `.py` file under `src/` and checks for forbidden imports, dangerous calls, and class-hierarchy / method-signature requirements.
4. **Dependencies** — Validates that all imports resolve to allowed modules from the SDK whitelist.
5. **Tests** — Runs the card's pytest suite under reduced rlimits.
6. **Behavioral** — Executes the card in the production sandbox against a minimal mock context to confirm runtime behaviour.

Stages run in order; the first failing stage short-circuits the rest. Stage 6 (Behavioral) is also re-run at approval time as a defence-in-depth check before the card is activated.

### sdk\_test\_card

Execute a partner card in a sandboxed environment with a mock context. The sandbox enforces restricted builtins, a curated import allow-list, an execution timeout, and reduced process resource limits — the same restrictions a card runs under once approved.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `card_id` | string | No | UUID of existing card (Mode A) |
| `source_code` | string | No | Source code for inline testing (Mode B) |
| `class_name` | string | No | Class name for inline testing (Mode B) |
| `variables` | object | No | Variables to pass to the card constructor |
| `mock_context` | object | No | Mock execution context |

**Mock Context Fields:**

```json
{
  "document_id": "doc-uuid",
  "document_type": "INVOICE",
  "document_fields": {
    "total_amount": "1500.00",
    "currency": "EUR",
    "vendor_name": "Acme Corp"
  },
  "metadata": {
    "custom_key": "custom_value"
  }
}
```

The tool returns `execution_success` (whether the sandbox ran the card to completion — a timeout, import violation, or thrown exception sets it to `false`), `card_status` (the `CardStatus` returned by `execute()` itself), the card's `message` and `data`, the captured `logs`, and `execution_time_ms`.

### sdk\_import\_github

Import a partner app from a GitHub repository. Clones the repo, reads `app.json`, and imports all cards found in the `.docflowcompose` directory.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `github_url` | string | Yes | GitHub HTTPS URL (e.g. `https://github.com/org/repo`) |
| `branch` | string | No | Branch to clone (default: `main`) |
| `token` | string | No | GitHub token for private repos |

**Expected Repository Structure:**

```
repo/
  app.json
  .docflowcompose/
    flow/
      actions/
        my-action.json
      conditions/
        my-condition.json
  src/
    my_action.py
    my_condition.py
  tests/
    test_card.py
```

## Management Tools

### sdk\_list\_submissions

List all partner card submissions for the current organization.

**Parameters:** None

### sdk\_get\_submission\_status

Get the validation status and report for a specific partner card submission.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `card_id` | string | Yes | UUID of the partner card |

### sdk\_approve\_card

Approve a validated partner card and activate it. Approval re-runs AST and behavioural validation as a defence-in-depth check, sets `partner_status = approved` and `enabled = true`, and registers the card in the runtime registry. Once approved, the card appears in `list_cards` for **every organization**, not just the submitting one.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `card_id` | string | Yes | UUID of the partner card |

{% hint style="warning" %}
Requires organization admin permissions. The card must be in `validated` state. Rejected cards must be re-uploaded and re-validated before they can be approved.
{% endhint %}

### sdk\_reject\_card

Reject a partner card submission and deactivate it.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `card_id` | string | Yes | UUID of the partner card |
| `reason` | string | No | Reason for rejection |

{% hint style="warning" %}
Requires organization admin permissions.
{% endhint %}

### sdk\_delete\_submission

Soft-delete a partner card submission, regardless of its current state. Sets `partner_status = deleted`, `enabled = false`, and `deprecated = true`. The row is retained for audit purposes but is hidden from submission listings and `list_cards`.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `card_id` | string | Yes | UUID of the partner card |

{% hint style="warning" %}
Requires organization admin permissions.
{% endhint %}

### sdk\_list\_cards\_picker

List all enabled, non-deprecated cards with role flags. Useful for determining which cards can be used in which node types when building workflows.

**Parameters:** None

## Current Capabilities & Roadmap

The Partner Card SDK is being rolled out incrementally. Here is what your card can rely on today and what is still being wired up:

| Capability | Status |
|------------|--------|
| **Field conditions** — read document fields from `context.document_fields` and branch on their values inside condition cards | ✅ Implemented |
| **Outgoing HTTP requests** — call external services from inside a card | 🚧 Currently being added |
| **Extended document information** — additional document metadata (beyond `document_id`, `document_type`, and `document_fields`) exposed on `ExecutionContext` | 🚧 Currently being added |
| **Database table lookup helpers** — built-in helpers to read from DocBits master-data / lookup tables inside a card | 📅 Planned for 1.1 |
| **Partner card source viewer** — read-only view of the submitted partner card code in the DocBits UI, so admins can inspect what they are approving | 📅 Planned for 1.1 |

{% hint style="info" %}
If your card needs a capability that is still in progress, it will fail validation (forbidden import, missing context attribute, or sandbox restriction) until the corresponding piece lands. This page will be updated as each capability ships.
{% endhint %}

{% hint style="danger" %}
**Partner cards run third-party code — use at your own risk.**

Cards uploaded through the Partner Card SDK are only **partially validated by DocBits**. The validation pipeline checks structure, locales, imports, AST patterns, dependencies, the card's own tests, and a behavioural smoke run in the sandbox — it does **not** constitute a full security audit or a functional guarantee of the card's business logic.

Once an organisation admin approves a partner card, it becomes available to every organisation on the platform and runs inside the production sandbox against real documents. Approving and enabling a partner card is therefore an explicit trust decision on the part of the approving admin. DocBits accepts no liability for data loss, incorrect routing, leaked information, or any other outcome caused by a partner card you choose to install or approve.

If you are not the original author of the card, review the source (and, once 1.1 ships, use the partner card source viewer) before approving it.
{% endhint %}
