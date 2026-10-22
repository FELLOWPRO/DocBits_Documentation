---
description: "P1: Trace a decision table through to assignment"
---

# P1: Trace a decision table through to assignment

A decision table connects input fields to typed returns. The example uses `cost_center=4711` and `total_amount`: reviewer A up to 1000, reviewer B above 1000. Create two non-overlapping rules and use valid users in your test organization. The kit's example describes the setup; it is not a guaranteed editor import.

For **Decision Table has Returns** version 3, enable `store_data=wf_store_data`. Version 2 instead reads the boolean storage option. The assignment card needs returns stored in the same run. Successful table execution alone does not confirm a valid user.

A user return can contain `output_type=user` and `value=101`; 101 is synthetic and must be replaced with an existing test user. Then choose **Assign document based on decision table** with `assignee_type=user`. The inspected version 2 of that action selects the last matching return. Multiple matches do not automatically require approval by all users.

Test one match, no match, multiple matches, wrong return type, invalid user ID and storage disabled. Route no-match and assignment errors to an explicit fallback. Establish ordering and hit policy instead of treating incidental table order as a business rule. Accept the actual assignment on the document.

The decision-table condition actually calls the table service to evaluate the table. Test mode is not a blanket guarantee against side effects; use only owned test data and inspect the actions involved.

## Cards and example parameters

These values describe individual card parameters, not an importable complete workflow. Replace YOUR_* with your own test selections. The designer manages the hidden caller ID. Catalog: Dev, DocFlow 2.10.38, 21 October 2026; check available versions and entitlements in your own organization.

### `condition_decision_tree_data` · v3

Identity: `c40160ce-805f-4312-8726-51b0fd7af8ec`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `decision_table` | `decision_table:str` | `"YOUR_TEST_DECISION_TABLE_ID"` |
| `boolean` | `boolean:bool` | `true` |
| `store_data` | `wf_store_data / wf_do_not_store_data` | `"wf_store_data"` |

### `action_assign_doc_based_on_decision_table` · v2

Identity: `699912a7-2369-47e0-9092-8d027e13752a`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `assignee_type` | `user / group` | `"user"` |

## Business test cases

| Case | Input / setup | Expected outcome |
| --- | --- | --- |
| DT-01 | 4711; 1000; store_data=wf_store_data | USER_A |
| DT-02 | 4711; 1000.01; store_data=wf_store_data | USER_B |
| DT-03 | no result / invalid user / wrong type | FALLBACK |
| DT-04 | returns=[USER_A, USER_B]; assign v2 | USER_B |
| DT-05 | store_data=wf_do_not_store_data | no stored return for assignment |

## Evidence and limits

Parameters and behavior were checked against the Dev catalog and inspected source revision. Business test cases are an acceptance procedure. Personal approvals, real data changes and delivery were not performed for this chapter.

[Continue learning](../workflow-learning-path.md) · [Training kit](../workflow-training-kit.md)
