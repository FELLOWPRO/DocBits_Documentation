---
description: "Distinguish workflow events, conditions, execution order, tests and activation."
---

# When does my workflow run?

A workflow needs an execution event and matching conditions. **Document type is Invoice** selects documents; it does not mean every change to an invoice automatically starts another run.

## From event to action

1. Check the organization, permissions and Workflow module, plus the Advanced entitlement where required.
2. Identify the event: document processing, an explicit manual invocation or a supported event trigger. Use only triggers actually available in your version's card catalog.
3. In a Standard Workflow, When and every And condition must match. A false condition stops that linear card sequence.
4. In an Advanced Workflow, the entry and connected result handles determine the route. A false And condition can continue through orange; red handles an evaluation error.
5. Check the result in the appropriate place: test response, persisted execution, document or connected destination.

**Start** is a manual entry. The training kit uses a When entry for Invoice and an exact training invoice number, meeting the current interface's requirements. Import it disabled and test manually. A successful manual test does not establish automatic document-event triggering.

## Save, test and activate

| State | Meaning |
| --- | --- |
| Local draft | A browser copy does not replace saving to the server. |
| Saved | The configuration exists. Check activation separately; saving a new rule can already enable it. |
| Advanced test | Evaluates the current graph, including unsaved changes. Document actions are simulated in test mode. |
| Enabled | The rule can be considered for its matching execution event. Test that event separately. |

Test Manager and the Advanced test dialog are different execution surfaces. A status comparison alone does not confirm assignment, a notification or export delivery. Check the side effects of the selected test surface before running against real documents.

## Multiple workflows and repeated execution

Lower **execution order** values run first. For example, workflow 100 prepares a field and workflow 200 checks it. Use distinct values and confirm the data actually read in a new run. An Advanced card's canvas position does not determine execution order.

**Change Status to → Trigger Workflows** can initiate another execution. **Run Workflow** invokes a selected workflow. Both require deliberate conditions; neither guarantees execution only once. Restrict tasks and exports using business processing state, and explicitly test a second run. A completed flag alone is not a general defense against concurrent duplicate processing.

Continue with the [Advanced case study](advanced-workflow-case-study.md), [training kit](workflow-training-kit.md) and [troubleshooting guide](workflow-troubleshooting.md).

## WF-01: Exercise and acceptance

Record execution event, filter, enabled state and card version. Inspect two successive runs and order 100/200 using a downstream field actually read. Separate an expected follow-up request from an observed execution.

[Learning path](workflow-learning-path.md)
