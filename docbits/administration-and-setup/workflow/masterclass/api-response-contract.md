---
description: "P1: Verify API calls and downstream response use"
---

# P1: Verify API calls and downstream response use

**Call API** version 2 appends its configured path to the DocBits API base and uses the current organization context. **Send HTTPS Request** version 2 uses an external URL and its own headers. A completely external URL is not an interchangeable Call API path. Both cards simulate sending in Advanced tests.

The inspected HTTPS action logs status and response text but exposes no freely named JSON-response store to later cards. Call API converts response text to a boolean. HTTP 200, valid JSON and successful downstream business processing therefore require separate evidence. Do not invent access syntax such as `api.response.cost_center`.

For external `{"cost_center":"4711"}`, agree an explicitly supported write-back or callback into a document field. Verify the stored field and read it in the intended follow-up run. Direct response-data transfer needs a card or extension with a documented output contract. JSON in card configuration also does not automatically prove the JSON bytes actually sent.

Use an owned test destination and inspect method, headers, actual body, status and response schema. Cover 4xx, 5xx, timeout, invalid JSON and duplicate triggering. Retry writes only after checking whether the first request was received. The example URL is reserved placeholder data and was not tested as a reachable service.

## Cards and example parameters

These values describe individual card parameters, not an importable complete workflow. Replace YOUR_* with your own test selections. The designer manages the hidden caller ID. Catalog: Dev, DocFlow 2.10.38, 21 October 2026; check available versions and entitlements in your own organization.

### `call_api` · v2

Identity: `6ca5e621-af72-4f55-aa2e-b3caa288722a`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `params` | `params:str` | `"{}"` |
| `api_endpoint` | `api_endpoint:str` | `"YOUR_RELATIVE_API_PATH"` |
| `data` | `data:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

### `action_https_request` · v2

Identity: `18d06ca4-3aca-4e49-b75c-566ade2fcb10`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `data` | `data` | `"{}"` |
| `params` | `params` | `"{}"` |
| `url` | `url:str` | `"https://training.example.invalid/status"` |
| `headers` | `headers:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

## Business test cases

| Case | Input / setup | Expected outcome |
| --- | --- | --- |
| API-01 | Advanced Test | simulated; no delivery proof |
| API-02 | HTTPS: 4xx / 5xx | error |
| API-03 | timeout | check receipt before retry |
| API-04 | {"cost_center":"4711"} | no automatic api.response.cost_center |
| API-05 | POST × 2 | destination duplicate check |

## Evidence and limits

Parameters and behavior were checked against the Dev catalog and inspected source revision. Business test cases are an acceptance procedure. Personal approvals, real data changes and delivery were not performed for this chapter.

[Continue learning](../workflow-learning-path.md) · [Training kit](../workflow-training-kit.md)
