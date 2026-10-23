---
description: "Learning path from beginner to expert"
---

# Learning path from beginner to expert

Work through the levels in order. Reading alone is insufficient: finish each level with your own configuration, a checkable expectation and evidence. P0 prevents basic execution mistakes; P1 develops data handling, business decisions and integrations.

1. [Orientation and execution model](#level-1)
2. [Your first rule](#level-2)
3. [Fields, types and boundaries](#level-3)
4. [Business rules and approvals](#level-4)
5. [Advanced control flow and child workflows](#level-5)
6. [Calculation, integration and export](#level-6)
7. [Change management and expert operation](#level-7)

## Prerequisites

Use an owned test organization and a synthetic document. Check organization, role, workflow license and Advanced entitlement. Keep imported exercises disabled. Complete JSON fixtures are for Advanced Test → Custom Data. Real approval and integration acceptance needs separate test users and destinations.

## 1. Orientation and execution model <a id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v2/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v2/en.html).

**Exercise:** Explain organization, access, When–And–Then and the difference between a linear rule and an Advanced graph. Distinguish a document-type filter, execution event, saving and activation.

**Completion criterion:** Before building, you can explain when the rule is considered and which evidence distinguishes simulation from a document run.

Read and build: [When does my workflow run?](workflow-execution-model.md) · [P0: Change status and control re-entry](masterclass/status-and-reentry.md).

## 2. Your first rule <a id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/en.html).

**Exercise:** Build When Invoice → And invoice_id = WF-TRAINING-001 → And total_amount > 1000 → Then wf_training_route = REVIEW. Keep it disabled. Test complete data for 999, 1000 and 1000.01; this linear rule needs no control node yet.

**Completion criterion:** REVIEW is reached only above 1000. Record field type, operator and selected output. Handle absent input separately.

Read and build: [Advanced case study: invoice routing](advanced-workflow-case-study.md) · [Workflow training kit](workflow-training-kit.md).

## 3. Fields, types and boundaries <a id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/en.html).

**Exercise:** Check missing, null, empty text, whitespace, false, 0 and numbers as text. Calculate tolerance once using PO reference and once using document reference. Compare one versus all actually matched lines.

**Completion criterion:** Explain true, false and error using value, type, reference and available data; no comparable line must not count as successful approval.

Read and build: [P1: Choose Field is, Docfield is or Compare two Fields](masterclass/field-conditions.md) · [P1: Make tolerance and PO reference direction explicit](masterclass/tolerances-and-po.md).

## 4. Business rules and approvals <a id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/en.html).

**Exercise:** Configure a decision table with two non-overlapping amount rules. Follow its stored user return through to assignment. Plan A at order 10 and B at 20, including rejection and fallback.

**Completion criterion:** Distinguish responsibility, task, notification and actual approval. Accept real handoff to B only after a processed decision by A.

Read and build: [P1: Trace a decision table through to assignment](masterclass/decision-table-routing.md) · [P1: Distinguish assignment, tasks and sequential approval](masterclass/assignment-task-sequential.md).

## 5. Advanced control flow and child workflows <a id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/en.html).

**Exercise:** Compare ALL, ANY and OR with two checks actually reached. Also inspect an unselected branch. Run all seven v2 routing cases and test Run Workflow with an owned inactive target.

**Completion criterion:** Explain test/scheduler divergence, source counting and error propagation. V2 reaches common completion without a stalled OR; inspect a green child call at its target.

Read and build: [P0: Connect Wait ALL, Wait ANY and OR correctly](masterclass/control-nodes.md) · [P0: Understand Run Workflow, target conditions and errors](masterclass/run-workflow.md) · [Advanced case study: invoice routing](advanced-workflow-case-study.md).

## 6. Calculation, integration and export <a id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/en.html).

**Exercise:** Compare the complete table before/after calculation, including regex nonmatch and division by zero. Define the actual integration write-back contract. Plan export after approval using an owned test configuration.

**Completion criterion:** Prove downstream field values, recipient receipt and ERP processing separately. Do not record simulation or an export request as delivery.

Read and build: [P1: Calculate table columns and check regex dependencies](masterclass/table-calculations.md) · [P1: Verify API calls and downstream response use](masterclass/api-response-contract.md) · [P1: Choose export variants, pending-task checks and final status](masterclass/export-lifecycle.md).

## 7. Change management and expert operation <a id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/en.html).

**Exercise:** Save a workflow export and record card versions before changing anything. Repeat positive, negative, error and boundary cases plus a second execution. Attribute the first failure to specific input and configuration.

**Completion criterion:** You can accept a change, restore the saved configuration and compare a new document run with effect evidence. Record cause, correction and remaining limits.

Read and build: [Diagnose workflow problems systematically](workflow-troubleshooting.md) · [Understand and configure workflow cards](card-reference-standard.md).

## Check your understanding

| Question | Answer |
| --- | --- |
| Is false empty for Field is v2? | Yes. Number 0 and text "false" are not empty. |
| Does a green OR test guarantee the document run? | No. Unreached predecessors are handled differently in tests and the inspected scheduler. |
| Can Run Workflow call an inactive target? | Yes, for the inspected explicit call. Still inspect target conditions and outcome. |
| Does HTTP 200 automatically expose api.response.cost_center? | No. The inspected actions do not provide that automatic JSON-output contract. |
| Does a green test prove export receipt? | No. Document execution, recipient receipt and ERP processing need separate evidence. |

## The five companion guides

Use these throughout the exercises: execution model → reproducible case study → training kit → diagnosis → card reference. They support the levels; they are not five additional unverified tasks.

1. [When does my workflow run?](workflow-execution-model.md)
2. [Advanced case study: invoice routing](advanced-workflow-case-study.md)
3. [Workflow training kit](workflow-training-kit.md)
4. [Diagnose workflow problems systematically](workflow-troubleshooting.md)
5. [Understand and configure workflow cards](card-reference-standard.md)

## Completion record

Use acceptance-record-template.json from the kit. Record scenario, configuration revision, expectation, observation and evidence kind. Distinguish Dev test, isolated source check, actual document execution, receipt and ERP processing. Explicitly leave untested steps open.
