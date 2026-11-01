# For Developers

This page is for developers and CI owners who write templates as JSON or start tests from code.

## Template JSON at a glance

A template is a JSON document (schema version 1). Export any template with the download icon to see a complete example.

```json
{
  "schemaVersion": 1,
  "id": "my-testing-page-check",
  "name": "Testing page check",
  "category": "smoke",
  "version": "1.0.0",
  "timeoutMs": 60000,
  "allowWrites": false,
  "params": {
    "document_id": { "type": "string", "required": true, "description": "Document to open" }
  },
  "steps": [
    { "id": "open", "action": "navigate", "route": "/settings/testing" },
    { "id": "badge", "action": "waitFor", "target": "testing.environment-badge", "state": "visible" }
  ]
}
```

* `id` and `version` identify a template; a saved version never changes, save changes under a new `version`.
* `params` declares the values an input supplies; steps refer to them as `{{params.<name>}}`.
* `allowWrites: true` is required for templates that upload, export, delete or approve.
* Steps address elements by stable test IDs (`target`), never by visible text, so a template works in every UI language.
* Validate before saving: **Import JSON → Validate**, or `POST /live-tests/validate`.

## Start an input via REST or Playwright

Prerequisites: an organisation admin token, the organisation ID, the input ID, and the `session_id` of a browser tab
with **Allow starts from outside** switched on.

```http
POST https://eu.api.docbits.com/testing/start
Authorization: Bearer <token>
X-ORG-ID: <organisation id>
Content-Type: application/json

{ "input_id": "<input id>", "session_id": "<session id>", "source": "playwright" }
```

The answer is `202` with `log_id`, `run_id` and `status`. Poll `GET /testing/logs/<log_id>` until the result is final.
Add `"confirm_writes": true` only for a template that writes data, and only when that is intended.

```ts
// Playwright test (API request context)
const res = await request.post(`${API}/testing/start`, {
  headers: { Authorization: `Bearer ${token}`, 'X-ORG-ID': orgId },
  data: { input_id: inputId, session_id: sessionId, source: 'playwright' },
});
expect(res.status()).toBe(202);
const { log_id } = await res.json();
// poll `${API}/testing/logs/${log_id}` until the result is PASS, FAIL or BLOCKED
```

Use your region's API host (see [DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp) for the host list).
CSV of the logs: `GET /testing/logs/export.csv` (same filters as the list) and `GET /testing/logs/<log_id>/export.csv`.

## Start via MCP

The DocBits MCP server offers the Testing tools `testing_list_templates`, `testing_list_inputs`, `testing_start`,
`testing_get_log` and `testing_list_logs`, and `list_test_sessions` for the registered tabs. `testing_start` needs an
explicit `session_id`; `confirm_writes` is set only after the user agreed. Sensitive values are passed for the run
only and never stored.

## Limits of the in-browser runner

* Tests run as the person who registered the tab: no login, no role switch.
* A full page reload ends the run.
* Native browser dialogs (file chooser, print, alerts) cannot be driven; file uploads use organisation or server test files.
* Screenshot steps are skipped (the run becomes **Blocked**).
For anything beyond this, use Playwright directly.
