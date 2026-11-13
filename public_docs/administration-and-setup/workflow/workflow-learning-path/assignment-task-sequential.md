---
description: 'P1: Distinguish assignment, tasks and sequential approval'
---

# P1: Distinguish assignment, tasks and sequential approval

A **document assignment** sets current responsibility. A **task** is a separate work item. A **notification** informs someone. None of these is already a person's approval. Assigning a group also does not prove consent from every group member.

Sequential cards collect recipients and order for the approval process. The example uses reviewer A at order 10 and reviewer B at 20. The inspected finalization starts with the smaller value. Moving to B follows the processed user decision in the approval process; a Wait node continuing in the designer does not itself perform that handoff.

Avoid direct assignment in the same run when expecting the first sequential recipient: inspected finalization can skip that first assignment after a document was directly assigned. For tasks, configure `task_type`, priority, recipient and `send_email` independently. Keep email disabled for training exercises.

Business acceptance needs A→approve→B→approve, rejection by A, a missing recipient and a repeated trigger. Rejection must prevent final export; failed recipient resolution must not appear as completed approval. Inspect document responsibility and task inventory separately. Designer simulations do not prove a real user handoff.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/en.mp4" %}

**Video:** Two-step approval with decision tables · 3:03 · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/en.vtt)

<details>

<summary>Transcript</summary>

**Two steps, two decision tables** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/en.mp4#t=0.25)

A two-step approval: first the approvers a decision table returns, then a final group that always comes last. Two decision tables, one returns users, the other a group.

**One chain: table, assign, table, assign** · [0:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/en.mp4#t=13.35)

Put each assign card right after its own decision table, in one chain: decision table, assign, decision table, assign. Both decision tables store their returned data.

**Each assign card right after its table** · [0:26](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/en.mp4#t=26.75)

A workflow keeps only the last decision table result. Each assign card reads it when it runs, so it must run before the next decision table replaces it.

**Priorities set the order** · [0:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/en.mp4#t=38.783)

The order of the approvals comes from the priorities, not from the order of the cards: the lowest number gets the document first. Give the final group the highest number.

**Test: approvers, then the group** · [0:52](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/en.mp4#t=52.116)

The test shows every card succeeding. The first assign card queues the two approvers, the second one the final group. At the end of the run, one final assignment gives the document to the first of them.

**Side by side: does not work** · [1:20](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/en.mp4#t=80.216)

This layout does not work. Two paths side by side look the same, but the workflow runs them step by step: both decision tables first, then both assign cards.

**The approvers are lost - no error** · [1:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/en.mp4#t=94.65)

The test runs both decision tables first, then both assign cards. Both read the result of the second table: the group is queued twice, and the approvers are lost. Every card still shows success, so nothing warns you. Use the chain.

**A fixed last approver: priority 99** · [2:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/en.mp4#t=124.05)

In a Standard workflow, a fixed approver can always come last: assign the decision table's users, then add a card that assigns one user with a high priority, for example 99.

**Keep the table's priorities lower** · [2:19](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/en.mp4#t=139.05)

The decision table's priorities must stay below that number. If the table finds nobody, the workflow stops at the decision table card, and nobody is assigned. A user returned by both is asked twice.

**Check it in a test** · [2:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/en.mp4#t=154.616)

A Standard workflow tests one card at a time, so test the same cards in an Advanced workflow. The first assign card queues the table's approvers, the second adds the fixed user. Their priorities put the fixed user last.

</details>

## Cards and example parameters

These values describe individual card parameters, not an importable complete workflow. Replace YOUR\_\* with your own test selections. The designer manages the hidden caller ID. Catalog: Dev, DocFlow 2.10.38, 21 October 2026; check available versions and entitlements in your own organization.

### `action_assign_doc_to_user_sequential` · v2

Identity: `859b2ea5-27a9-41e4-b7f1-3cf8812b9343`

| Parameter | Type / choices | Example               |
| --------- | -------------- | --------------------- |
| `user`    | `user:int`     | `"YOUR_TEST_USER_ID"` |
| `value`   | `value:int`    | `10`                  |

### `action_create_task_for_user_sequential` · v2

Identity: `548b3583-6a96-483f-8c66-7871d5b067fa`

| Parameter     | Type / choices        | Example               |
| ------------- | --------------------- | --------------------- |
| `description` | `description:str`     | `"WF-TRAINING-001"`   |
| `task_type`   | `task / notification` | `"task"`              |
| `priority`    | `high / medium / low` | `"medium"`            |
| `send_email`  | `send_email:bool`     | `false`               |
| `value`       | `value:int`           | `20`                  |
| `user`        | `user:int`            | `"YOUR_TEST_USER_ID"` |
| `title`       | `title:str`           | `"WF-TRAINING-001"`   |

## Business test cases

| Case      | Input / setup       | Expected outcome          |
| --------- | ------------------- | ------------------------- |
| ASSIGN-01 | A:10; B:20          | A → APPROVE → B → APPROVE |
| ASSIGN-02 | A → REJECT          | EXPORT=NO                 |
| ASSIGN-03 | recipient=∅         | FALLBACK                  |
| ASSIGN-04 | RUN-1 → RUN-2       | duplicate check           |
| ASSIGN-05 | direct + sequential | inspect first assignee    |

## Evidence and limits

Parameters and behavior were checked against the Dev catalog and inspected source revision. Business test cases are an acceptance procedure. Personal approvals, real data changes and delivery were not performed for this chapter.

[Continue learning](./) · [Training kit](workflow-training-kit.md)
