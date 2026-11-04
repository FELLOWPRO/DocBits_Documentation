---
description: "Diagnose workflow problems using execution events, input data, selected paths and actual outcomes."
---

# Diagnose workflow problems systematically

Start with one affected execution. Record the organization and environment, workflow name and saved revision, document reference, timestamp and timezone, and exact node message. In test responses, also use `execution_id`. Keep access keys and unprotected customer data out of shared evidence.

## From symptom to verification

| Symptom | Find evidence | Correct and retest |
| --- | --- | --- |
| No execution | License, module, enabled state, time filters and matching event | Correct the entry and filters; repeat the actual event. Manual Start does not prove that event. |
| Action remains gray | Predecessor's result and connected handle | Follow the path actually taken. A skipped node did not itself fail. |
| Orange condition | Field key, type, value and operator actually read | Distinguish a negative result from an evaluation error. Retest below, at and above the boundary. |
| Red condition or action | First error message and required input | Correct data or configuration; repeat the error and success cases. |
| Nothing follows Wait ALL | Every source and its connected result handle | Do not require mutually exclusive routes together. Show a satisfiable path for each required source. |
| Duplicate tasks or exports | Repeated runs, events, status changes and Run Workflow calls | Restrict trigger conditions and state transitions; test the same case twice. Consider suitable protection against concurrent processing in the destination process. |
| Variable affects other workflows | Shared organization variable | Check dependencies. Changes persist independently of the canvas; retest affected workflows. |
| Test passes but effect is absent | What was compared or simulated? | Verify assignment on the document, the task in Tasks, and receipt at the destination. Status alone is insufficient. |
| Export starts but receiver has nothing | Export history, response and receiver's data | Diagnose before retrying; check whether the receiver already processed the first request. |

## Interpret messages

In the [Advanced example](advanced-workflow-case-study.md), a missing amount takes red to data correction. The handler and OR merge can then succeed while the overall execution remains erroneous. A normally false amount comparison instead takes orange and can finish successfully on the standard route.

Two connections from one source are not two independent approvals. A merge evaluates the connected outcomes of its sources. Check the complete flow: a partial test from a middle node can omit necessary predecessors.

## Prove the correction

1. Preserve the original evidence and business expectation.
2. Change data or configuration deliberately. Change expectations only when the requirement changes.
3. Repeat the failed case, positive case and affected boundaries with the [training kit](workflow-training-kit.md).
4. Save the corrected rule and check its enabled state separately.
5. Compare a new real execution with the old one. Old logs continue to describe their original revision.

Record the cause, correction, demonstrated outcome and remaining limitations. Separate queueing time from execution time; a long total duration alone does not identify a slow node.

## WF-04: Exercise and acceptance

Start with invalid-number. Save the first amount error and overall error result. Repeat with above and compare the new evidence. Preserve the old error record; successful error handling alone is insufficient.

[Learning path](workflow-learning-path.md)

## Repeat isolated card tests with an explicit scope

In the inspected Dev designer, repeating a test after testing from a selected node switched to the whole graph. Open the intended card’s context-menu test again and check the nodes actually visited. A six-node result does not establish an isolated emptiness-card test. A failed-action counter may also include an unmet condition: read the selected output, log message and overall result as well.
