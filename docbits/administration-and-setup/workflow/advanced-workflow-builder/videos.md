---
description: "Watch five narrated chapters on Advanced Workflows and Workflow Logs in English, with caption files and transcripts."
---

# Video guide

Learn how to build, test and diagnose an Advanced Workflow. Each chapter has English narration and takes less than two minutes.

The first chapter shows a configured workflow in the real DocBits interface. The other four chapters use labelled teaching diagrams. For complete control descriptions, use the [Advanced Workflows guide](README.md), [Toolbar & Canvas](toolbar-and-canvas.md), [Nodes](nodes.md), [Variables](variables.md) and [Validation & Testing](validation-and-testing.md).

Caption files are available in WebVTT format below each video. Open the expandable transcript to read the explanation without playing the video.

| Chapter | Duration |
| --- | --- |
| [1. Builder and canvas](#builder-and-canvas) | 1:38 |
| [2. Nodes and routes](#nodes-and-routes) | 1:42 |
| [3. Variables, tests and activation](#variables-tests-and-activation) | 1:54 |
| [4. Find the relevant execution](#find-the-relevant-execution) | 1:52 |
| [5. Trace nodes and diagnose](#trace-nodes-and-diagnose) | 1:43 |

## Builder and canvas

Build an invoice amount check with two connected actions. The example shows an unsaved demonstration draft in the actual DocBits interface, including card settings and the test dialog.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/en.mp4" %}

[Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/en.vtt) · 1:38

<details>
<summary>Transcript</summary>

**An invoice with two routes**

Here is a real Advanced Workflow in DocBits. An invoice amount check leads to two actions. The connections define which action runs. This example uses an unsaved draft and demonstration fields.

**Configure the amount check**

Open Add, choose And, and select a Document Field condition. Set the amount field, choose Greater Than, and enter one thousand. Use the exact field key from your document configuration.

**Configure the actions**

Add two Then cards. Each card sets the demonstration field approval route. One writes Approval; the other writes Standard. These values label the route. Configure your business actions for a production workflow.

**Connect the result outputs**

Connect Start to the condition input. Connect blue Success to Approval, and orange Failed Condition to Standard. The red Error output handles evaluation errors separately. Card position alone does not create a route.

**Prepare the test cases**

Open Test in the toolbar. Choose a test document, or enter complete document data as JSON. Check amounts above, below, and exactly at one thousand. Also check missing values. Inspect the node results after execution.

**Validate, save and activate**

Validate the connections and card settings. Save explicitly to write the workflow to the server, then check activation separately. Automatic browser drafts do not replace Save. Execution and log access require the appropriate module and subscription.

</details>

## Nodes and routes

Understand node roles, connect success, false-condition and error outputs, build alternatives, use Wait ALL, Wait ANY and OR, and avoid invalid connections.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v1/en.mp4" %}

[Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v1/en.vtt) · 1:42

<details>
<summary>Transcript (English)</summary>

Start is the manual entry. When defines an event trigger. Neither accepts incoming connections. And checks a condition. Then performs an action. Both builders share the card catalog. Notes explain the design without executing.

Drag an output to the next input. Designer blue means success, orange means false condition, and red means error. And has three outcomes. Then has success and error. Execution views show success in green.

Check whether an invoice exceeds a threshold. Connect blue to approval, orange to normal processing, and red to error handling. A false condition can continue through its connected route. It does not stop every branch.

Wait ALL joins branches. Every source must have taken a route connected to the gate. Connect both required checks and the next action. An unselected route cannot provide a required result.

Wait ANY and OR join branches when at least one source took a connected route. OR requires two different source nodes. These gates neither create exclusive choices nor cancel other actions. Test the complete graph.

Keep processing nodes reachable from an entry. Avoid cycles and incoming connections to entry nodes. Include a Then action. Validate changed routes. Imported Delay nodes need a positive duration. The current Add menu does not offer Delay.

</details>

## Variables, tests and activation

Choose variable types and understand organization scope, validate the graph, select the test context, inspect results, save and check activation.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v1/en.mp4" %}

[Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v1/en.vtt) · 1:54

<details>
<summary>Transcript (English)</summary>

Open Variables with the braces icon. Choose Text, Number, Yes or No, or Document. Search finds variable names. A Document variable stores a reference set by a dedicated workflow action. This form does not accept document values.

Choose a unique name, type and initial value. Creating, editing and deleting variables persist immediately for the organization. Other workflows can share these values. Saving or discarding the canvas cannot undo variable changes.

Select Validate. Review errors and warnings above the canvas. Click a message to focus its node. Check actions, entry connections, handles, cycles and merges. Structural validation does not prove that runtime data is correct.

Toolbar play opens Select Test Document. Choose a document, Custom Data, or Test Without Document for independent cards. Start play runs directly. Tests use the current canvas, including unsaved edits, and simulate destructive actions.

Inspect node messages and durations. Green means success, orange false condition, red error, and gray skipped. Retest corrections. Use Test Manager for repeatable scenarios. Cover the successful route, alternatives, missing data and errors.

Auto-save keeps a local browser draft about every thirty seconds after changes. Save explicitly to the server. The activation toggle is unavailable before the first save. Check the enabled state in Workflow List before expecting automatic execution.

</details>

## Find the relevant execution

Open logs for a document, read counters and execution rows, filter results, check dates and pagination, and understand empty or special log states.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v1/en.mp4" %}

[Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v1/en.vtt) · 1:52

<details>
<summary>Transcript (English)</summary>

Open the document Dashboard. Select Workflow Logs in the document Actions menu. Workflow access must be enabled. These logs describe the selected document's executions. Designer tests and organization event or activity logs are separate.

Blue counts executions in the current results. Red counts errors, yellow failed conditions, and green successes. The counters describe executions, not unique workflow definitions or graph nodes. Filters can change these counts.

Each row shows workflow name, creation time, runtime in seconds and result. One workflow can run repeatedly for one document. Compare timestamps. Rounded runtime can display zero point zero zero seconds for a short execution.

Use Search to find a workflow. The tune icon opens Sort Direction, Sort By, Status, Start Date and End Date. Sort by name or creation time. Enter dates as year, month, day. Select Apply.

Use pagination for older results. Clear Filters reloads the list without filter selections. Clear Search separately. For empty results, check document, dates and status. An empty list does not prove execution failed.

A banner and blocked icon identify the document's execution limit. Investigate repeated triggers before changing limits. A DocOperator video download appears only when a recording exists. It is an execution recording, separate from tutorial videos.

</details>

## Trace nodes and diagnose

Expand an advanced execution, select nodes, distinguish false conditions, errors and skipped nodes, inspect merge results, then correct, test and verify the workflow.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/en.mp4" %}

[Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/en.vtt) · 1:43

<details>
<summary>Transcript (English)</summary>

Expand the workflow row. An advanced execution shows its graph on the left and messages on the right. Standard workflows show a card sequence. Available execution data describes that run, which can differ from today's designer.

Pan or zoom, then click a node. Card Logs shows its messages. Control nodes, including Wait ALL and Wait ANY, can show node-level messages. Read the message with the selected node and execution timestamp.

Green means success, orange false condition, red error, and gray skipped. A skipped node was not executed. Check whether another branch was selected or a required merge input was missing before changing that node.

Follow the actual route from the entry. For a false amount check, inspect orange. For an error, read the message and inspect red. An error handler can succeed while the overall execution still reports the original error.

For Wait ALL, check every source and connected outcome. For ANY or OR, find a matching source. Two handles from one source are not independent approvals. An orange condition result can be intentional.

Record workflow name, document reference, timestamp, node and exact message. Correct configuration or data, then test a repeatable scenario. Save and check activation. Compare a new execution with the old run. Earlier logs still describe earlier behavior.

</details>

Continue with the [Advanced Workflows guide](README.md) or [Workflow Logs](../workflow-logs.md).
