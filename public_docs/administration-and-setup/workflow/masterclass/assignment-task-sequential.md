---
description: "P1: Distinguish assignment, tasks and sequential approval"
---

# P1: Distinguish assignment, tasks and sequential approval

A **document assignment** sets current responsibility. A **task** is a separate work item. A **notification** informs someone. None of these is already a person's approval. Assigning a group also does not prove consent from every group member.

Sequential cards collect recipients and order for the approval process. The example uses reviewer A at order 10 and reviewer B at 20. The inspected finalization starts with the smaller value. Moving to B follows the processed user decision in the approval process; a Wait node continuing in the designer does not itself perform that handoff.

Avoid direct assignment in the same run when expecting the first sequential recipient: inspected finalization can skip that first assignment after a document was directly assigned. For tasks, configure `task_type`, priority, recipient and `send_email` independently. Keep email disabled for training exercises.

Business acceptance needs A→approve→B→approve, rejection by A, a missing recipient and a repeated trigger. Rejection must prevent final export; failed recipient resolution must not appear as completed approval. Inspect document responsibility and task inventory separately. Designer simulations do not prove a real user handoff.

## Cards and example parameters

These values describe individual card parameters, not an importable complete workflow. Replace YOUR_* with your own test selections. The designer manages the hidden caller ID. Catalog: Dev, DocFlow 2.10.38, 21 October 2026; check available versions and entitlements in your own organization.

### `action_assign_doc_to_user_sequential` · v2

Identity: `859b2ea5-27a9-41e4-b7f1-3cf8812b9343`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `value` | `value:int` | `10` |

### `action_create_task_for_user_sequential` · v2

Identity: `548b3583-6a96-483f-8c66-7871d5b067fa`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `description` | `description:str` | `"WF-TRAINING-001"` |
| `task_type` | `task / notification` | `"task"` |
| `priority` | `high / medium / low` | `"medium"` |
| `send_email` | `send_email:bool` | `false` |
| `value` | `value:int` | `20` |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `title` | `title:str` | `"WF-TRAINING-001"` |

## Business test cases

| Case | Input / setup | Expected outcome |
| --- | --- | --- |
| ASSIGN-01 | A:10; B:20 | A → APPROVE → B → APPROVE |
| ASSIGN-02 | A → REJECT | EXPORT=NO |
| ASSIGN-03 | recipient=∅ | FALLBACK |
| ASSIGN-04 | RUN-1 → RUN-2 | duplicate check |
| ASSIGN-05 | direct + sequential | inspect first assignee |

## Evidence and limits

Parameters and behavior were checked against the Dev catalog and inspected source revision. Business test cases are an acceptance procedure. Personal approvals, real data changes and delivery were not performed for this chapter.

[Continue learning](../workflow-learning-path.md) · [Training kit](../workflow-training-kit.md)
