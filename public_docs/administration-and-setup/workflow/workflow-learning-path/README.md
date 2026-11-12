---
description: Learning path from beginner to expert
---

# Learning path from beginner to expert

Seven levels take you from your first look at the workflow designer to owning a change in a running workflow. Each level names a goal, three steps you carry out in your own test organization, and a result you can check. Do them in order, and build along the way: reading the page on its own will not get you there.

1. [Orientation and execution model](./#level-1)
2. [Your first rule](./#level-2)
3. [Fields, types and boundaries](./#level-3)
4. [Business rules and approvals](./#level-4)
5. [Advanced control flow and child workflows](./#level-5)
6. [Calculation, integration and export](./#level-6)
7. [Change management and expert operation](./#level-7)

## Before you start

* A test organization you own, with a synthetic invoice in it. Never practise on customer documents.
* Your role, the workflow license and the Advanced entitlement, checked before level 1.
* Exercises you import stay disabled until you have tested them.
* Complete JSON fixtures belong in **Advanced Test → Custom Data**.
* Real approvals and integrations need their own test users and destinations; a designer test does not stand in for them.

## 1. Orientation and execution model <a href="#level-1" id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v2/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v2/en.html).

**Goal:** Know what starts a workflow, and what a test result can and cannot tell you.

1. Check the organization, your access, the workflow module and the Advanced entitlement.
2. Say When–And–Then in your own words, then explain where a linear rule stops and how an Advanced graph follows its connected outputs instead.
3. Keep four things apart that look alike in the designer: the document-type filter, the execution event, saving, and activation.

**Done when:** you can say when a rule is considered at all, and which piece of evidence separates a simulation from a run on a real document.

**Detail:** [When does my workflow run?](workflow-execution-model.md) · [Change status without restarting your workflow](status-and-reentry.md)

## 2. Your first rule <a href="#level-2" id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/en.html).

**Goal:** Get one rule from the designer to a checked result without touching a document.

1. Build When Invoice → And invoice\_id = WF-TRAINING-001 → And total\_amount > 1000 → Then wf\_training\_route = REVIEW. Save it and leave it disabled; a linear rule this size needs no control node.
2. Run Advanced Test with complete data for 999, 1000 and 1000.01.
3. Write down field type, operator and selected output for each case, then add a case where the amount is missing altogether.

**Done when:** REVIEW is reached for 1000.01 only, and a missing amount comes out as an error rather than as an ordinary below-the-limit result.

**Detail:** [Advanced case study: invoice routing](advanced-workflow-case-study.md) · [Workflow training kit](workflow-training-kit.md)

## 3. Fields, types and boundaries <a href="#level-3" id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/en.html).

**Goal:** Know what a condition actually compares before you trust what it returns.

1. Test the empty-state check against a missing field, `null`, empty text, whitespace, `false`, `0`, `"0"` and `"false"`, and note which of them count as empty.
2. Calculate the same 2 percent tolerance twice: once with the PO as the reference (PO 100, document 102.02) and once with the document as the reference.
3. Switch between Any and All, and count how many lines were actually compared.

**Done when:** you can explain true, false and error from value, type, reference and available data. When no line could be compared, the outcome is a data error, not a successful approval.

**Detail:** [Choose Field is, Docfield is or Compare two Fields](field-conditions.md) · [Make tolerance and PO reference direction explicit](tolerances-and-po.md)

## 4. Business rules and approvals <a href="#level-4" id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/en.html).

**Goal:** Send an invoice to the right person through a decision table, and see who has actually decided what.

1. Create a decision table with two rules that cannot both match: reviewer A up to 1000, reviewer B above 1000.
2. Store the returned user and assign the document from that stored return; use real users from your test organization.
3. Plan the sequence with A at order 10 and B at order 20, then add a rejection by A and a fallback for the case where no user comes back.

**Done when:** you can tell responsibility, task, notification and an actual approval apart, and you accept the handover to B only after A has decided.

**Detail:** [Trace a decision table through to assignment](decision-table-routing.md) · [Distinguish assignment, tasks and sequential approval](assignment-task-sequential.md)

## 5. Advanced control flow and child workflows <a href="#level-5" id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/en.html).

**Goal:** Join parallel paths correctly, and hand work to another workflow.

1. Compare ALL, ANY and OR on two checks that are actually reached: ALL needs a matching output from every source, ANY and OR need one.
2. Look at a branch the run did not take. A test still evaluates it, while the normal run skips the waiting merge once a predecessor never arrives.
3. Run the seven cases of the v2 case study (above, below, boundary, just-above, missing, invalid-number, other-invoice), then call one of your own inactive workflows with Run Workflow and open the target's own path.

**Done when:** you can explain the test-and-run difference from step 2, how sources are counted (green and orange from one source still make one source), and where an error travels. A green Run Workflow call still needs the target inspected. V2 here means the second version of the case-study graph: each route's status card connects straight to the shared completion card, with no waiting OR node.

**Detail:** [Connect Wait ALL, Wait ANY and OR correctly](control-nodes.md) · [Understand Run Workflow, target conditions and errors](run-workflow.md) · [Advanced case study: invoice routing](advanced-workflow-case-study.md)

## 6. Calculation, integration and export <a href="#level-6" id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/en.html).

**Goal:** Calculate values, get a result back from an external system, and export only after a real approval.

1. Calculate a column and compare the whole table before and after, including a row where the regex does not match and a division by zero.
2. Write down the write-back contract with the external system: which document field takes the result, which card or extension writes it there, and how you check the stored value afterwards. HTTP 200 on its own is not a result.
3. Plan the export after approval with your own export configuration, and note what you will inspect at the recipient.

**Done when:** field values downstream, the recipient's receipt and ERP processing each have their own evidence. A simulation or a queued export is not a delivery.

**Detail:** [Calculate table columns and check regex dependencies](table-calculations.md) · [Verify API calls and downstream response use](api-response-contract.md) · [Choose export variants, pending-task checks and final status](export-lifecycle.md)

## 7. Change management and expert operation <a href="#level-7" id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/en.html).

**Goal:** Change a workflow you did not build, and be able to undo it.

1. Export the workflow and note the card versions before you touch anything.
2. After the change, repeat the positive, negative, error and boundary cases, plus a second run of the same case.
3. Trace the first failure back to one input and one configuration, and keep the saved export as the way back.

**Done when:** you can accept the change, restore the saved configuration, and compare a new document run with evidence. Write down cause, correction and the limits that remain.

**Detail:** [Diagnose workflow problems systematically](workflow-troubleshooting.md) · [Understand and configure workflow cards](card-reference-standard.md)

## Check your understanding

| Question                                                      | Answer                                                                                   |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Is false empty for Field is v2?                               | Yes. Number 0 and text "false" are not empty.                                            |
| Does a green OR test guarantee the document run?              | No. Unreached predecessors are handled differently in tests and the inspected scheduler. |
| Can Run Workflow call an inactive target?                     | Yes, for the inspected explicit call. Still inspect target conditions and outcome.       |
| Does HTTP 200 automatically expose api.response.cost\_center? | No. The inspected actions do not provide that automatic JSON-output contract.            |
| Does a green test prove export receipt?                       | No. Document execution, recipient receipt and ERP processing need separate evidence.     |

## Record what you accepted

Download `workflow-training-kit-v2.zip` from the [workflow training kit](workflow-training-kit.md), extract it and open `acceptance-record-template.json`. It is a blank record, not something you import; the same ZIP also holds the fixtures, the expectations and the saved test responses the levels refer to.

Fill in what you tested and how you know: the scenario, the configuration (workflow export hash, card versions), what you expected, what you observed, and which kind of evidence you have. Keep a test in Advanced Test, an isolated source check, a real document run, a recipient receipt and ERP processing apart, and leave steps you have not tested marked as open.
