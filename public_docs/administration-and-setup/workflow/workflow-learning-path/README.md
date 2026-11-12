---
description: Learning path from beginner to expert
---

# Learning path from beginner to expert

Seven levels take you from your first look at the workflow designer to owning a change in a running workflow. Each level names a goal, the steps you carry out in your own test organization, and a result you can check. Work through them in order and build each exercise yourself: every level builds on the configuration you made in the one before.

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

1. Build it in the Advanced Builder: When Invoice → And invoice\_id = WF-TRAINING-001 → And total\_amount > 1000 → Then wf\_training\_route = REVIEW. A linear rule this size needs no control node.
2. Save it, then open the rule list and check that it is still disabled, because saving a new rule can already enable it. Advanced Test is a separate execution surface: it evaluates the graph in the builder, not the enabled rule.
3. Run Advanced Test with complete data for 999, 1000 and 1000.01. Write down field type, operator and selected output for each case, then add a case where the amount is missing altogether.

**Done when:** REVIEW is reached for 1000.01 only, a missing amount comes out as an error rather than as an ordinary below-the-limit result, and the rule is switched off again when you finish.

**Detail:** [Advanced case study: invoice routing](advanced-workflow-case-study.md) · [Workflow training kit](workflow-training-kit.md)

## 3. Fields, types and boundaries <a href="#level-3" id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/en.html).

**Goal:** Know what a condition actually compares before you trust what it returns.

1. Test the empty-state check against a missing field, `null`, empty text, whitespace, `false`, `0`, `"0"` and `"false"`, and note which of them count as empty.
2. Calculate the same 2 percent tolerance twice: once with the PO as the reference (PO 100, document 102.02) and once with the document as the reference.
3. Switch between Any and All on the PO card, and count how many lines were actually compared.

**Done when:** you can explain true, false and error from value, type, reference and available data. In the PO card version 5, a document that has no comparable line is a data error, not a successful approval.

**Detail:** [Choose Field is, Docfield is or Compare two Fields](field-conditions.md) · [Make tolerance and PO reference direction explicit](tolerances-and-po.md)

## 4. Business rules and approvals <a href="#level-4" id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/en.html).

**Goal:** Send an invoice to the right person through a decision table, then run an approval chain that waits for the first reviewer.

**Exercise 1: decision table with direct assignment**

1. Create a decision table with two rules that cannot both match: reviewer A up to 1000, reviewer B above 1000, using `cost_center=4711` and `total_amount`.
2. In **Decision Table has Returns** version 3, set `store_data=wf_store_data`. Assign the document with **Assign document based on decision table** and `assignee_type=user`, using real users from your test organization.
3. Test one match, no match, multiple matches and an invalid user ID, and route the no-match and assignment errors to an explicit fallback. Accept the assignment on the document itself.

**Exercise 2: sequential approval without direct assignment**

1. Create a second, separate rule with the sequential cards: the sequential assignment card at order 10 for reviewer A, then the sequential task card at order 20 for reviewer B. Keep direct assignment out of this run, because the inspected finalization can skip the first sequential recipient when a document was already directly assigned in the same run.
2. Approve as A, then check that B receives the document only after A's processed decision, and approve as B.
3. Reject as A in a fresh run and confirm that the export does not happen, then test what happens when no recipient can be resolved.

**Done when:** you can tell responsibility, task, notification and an actual approval apart; A→approve→B→approve happened in that order; a rejection by A prevented the export; and a missing recipient did not count as a completed approval.

**Detail:** [Trace a decision table through to assignment](decision-table-routing.md) · [Distinguish assignment, tasks and sequential approval](assignment-task-sequential.md)

## 5. Advanced control flow and child workflows <a href="#level-5" id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/en.mp4" %}

[Open the video with English captions and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/en.html).

**Goal:** Join parallel paths correctly, and hand work to another workflow.

1. Compare ALL, ANY and OR on two checks that are actually reached: ALL needs a matching output from every source, ANY and OR need one, and green plus orange from one source still count as one source.
2. Look at a branch the run did not take, as in case MERGE-04: Advanced Test still evaluates the waiting merge, while the normal run skips it once a predecessor never arrives.
3. Run the seven cases of the v2 case study (above, below, boundary, just-above, missing, invalid-number, other-invoice), then call one of your own inactive workflows with Run Workflow and open the target's own path.

**Done when:** you can explain the MERGE-04 difference between test and run from step 2, how sources are counted, and where an error travels. A green Run Workflow call still needs the target inspected. V2 here means the second version of the case-study graph: each route's status card connects straight to the shared completion card, with no waiting OR node.

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

| Question                                                      | Answer                                                                                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Is false empty for Field is v2?                               | Yes. Number 0 and text "false" are not empty.                                                                            |
| Does a green OR test guarantee the document run?              | No. In the checked case MERGE-04, a test evaluates the merge that a document run skips when a predecessor never arrives. |
| Can Run Workflow call an inactive target?                     | Yes, for the inspected explicit call. Still inspect target conditions and outcome.                                       |
| Does HTTP 200 automatically expose api.response.cost\_center? | No. The inspected actions do not provide that automatic JSON-output contract.                                            |
| Does a green test prove export receipt?                       | No. Document execution, recipient receipt and ERP processing need separate evidence.                                     |

## Record what you accepted

Download `workflow-training-kit-v2.zip` from the [workflow training kit](workflow-training-kit.md), extract it and open `acceptance-record-template.json`. It is a blank record, not something you import; the same ZIP also holds the fixtures, the expectations and the saved test responses the levels refer to.

Fill in what you tested and how you know: the scenario, the configuration (workflow export hash, card versions), what you expected, what you observed, and which kind of evidence you have. Keep a test in Advanced Test, an isolated source check, a real document run, a recipient receipt and ERP processing apart, and leave steps you have not tested marked as open.
