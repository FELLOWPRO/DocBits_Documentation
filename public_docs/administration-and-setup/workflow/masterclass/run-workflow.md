---
description: "P0: Understand Run Workflow, target conditions and errors"
---

# P0: Understand Run Workflow, target conditions and errors

**Run Workflow** calls a workflow by ID and waits for its execution. A name is insufficient. The designer manages the caller's hidden workflow ID; do not change it as a business parameter. The current document is passed to the target, whose entry and conditions are evaluated again.

The inspected explicit call also reaches an **inactive** target. Inactive therefore does not mean unreachable through Run Workflow. Dev tests covered an inactive training target, a self-call and an unknown target ID. Self-calls and unknown IDs took Error. Built-in recursion and chain limits do not replace business rules that bound repeated calls.

Distinguish organization variables and document fields from run-local returns. The call does not automatically forward all parent decision-table or HTTP return data. Agree the required document fields and inspect their actual values in the next card.

A green call does not confirm every target business condition: an Advanced target result without a technical error is treated as a successful call, which can include `failed_condition`. Inspect the target's selected path and actual effect. Handle failure explicitly in the caller; avoid A→B→A and repeated calls to the same target.

## Cards and example parameters

These values describe individual card parameters, not an importable complete workflow. Replace YOUR_* with your own test selections. The designer manages the hidden caller ID. Catalog: Dev, DocFlow 2.10.38, 21 October 2026; check available versions and entitlements in your own organization.

### `run_workflow` · v2

Identity: `bb773bc7-b258-49b9-b0e9-b1c28ac227cb`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `hidden_workflow_id` | `hidden_workflow_id` | `"MANAGED_BY_DESIGNER"` |
| `workflow` | `workflow:str` | `"YOUR_TARGET_WORKFLOW_ID"` |

## Business test cases

| Case | Input / setup | Expected outcome |
| --- | --- | --- |
| CHILD-01 | enabled=false; workflow=VALID_ID | call=success |
| CHILD-02 | caller_id=target_id | error |
| CHILD-03 | workflow=UNKNOWN_ID | error |
| CHILD-04 | Advanced target=failed_condition | call may be success; inspect target |

## Evidence and limits

Selected card and node outcomes were checked with synthetic data in Advanced Test. Responses are in the training kit. Document actions are simulated; these tests do not establish a persisted document run or external delivery.

[Continue learning](../workflow-learning-path.md) · [Training kit](../workflow-training-kit.md)
