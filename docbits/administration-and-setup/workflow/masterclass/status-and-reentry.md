---
description: "P0: Change status and control re-entry"
---

# P0: Change status and control re-entry

**Change Status to** updates the document status. In version 3, `trigger_docflow` controls whether further workflow processing is requested. Set it explicitly. A missing parameter defaults to `true` in the code; versions 1/2 do not read this switch in the same execution path. Check the saved card version.

Start with `validated_pending_approval` and `trigger_docflow=false`. The status is a technical option: an invented `pending_approval` is not a substitute. An Advanced test simulates the update. It proves neither a persisted status change nor processing of a requested follow-up execution.

A bounded business process checks the initial status and a processing marker, performs its action and moves to the next state. A repeated event must no longer satisfy the original condition. Two concurrent runs may both read the old marker, however: task and export destinations need additional duplicate handling.

For acceptance, compare the first and second actual runs: document status, requested follow-up execution and number of tasks or destination records. Do not alternate between two statuses merely to experiment. A status update does not grant an approval whose business condition remains unmet.

## Cards and example parameters

These values describe individual card parameters, not an importable complete workflow. Replace YOUR_* with your own test selections. The designer manages the hidden caller ID. Catalog: Dev, DocFlow 2.10.38, 21 October 2026; check available versions and entitlements in your own organization.

### `staus_change` · v3

Identity: `4e0d38a2-a0af-4c1c-b0c2-2f380d70d910`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `trigger_docflow` | `trigger_docflow:bool` | `false` |
| `status` | `error / rejected / ready_for_validation / validated_pending_approval / approved_pending_second_approval / archived / finished / exported` | `"validated_pending_approval"` |

## Business test cases

| Case | Input / setup | Expected outcome |
| --- | --- | --- |
| STATUS-01 | v3; trigger_docflow=false | validated_pending_approval; trigger=false |
| STATUS-02 | v3; trigger_docflow=true | follow-up request ≠ completed follow-up |
| STATUS-03 | v3; trigger_docflow: — | default=true |
| STATUS-04 | RUN-1 → RUN-2 | tasks=1; destination_records=1 |

## Evidence and limits

Selected card and node outcomes were checked with synthetic data in Advanced Test. Responses are in the training kit. Document actions are simulated; these tests do not establish a persisted document run or external delivery.

[Continue learning](../workflow-learning-path.md) · [Training kit](../workflow-training-kit.md)
