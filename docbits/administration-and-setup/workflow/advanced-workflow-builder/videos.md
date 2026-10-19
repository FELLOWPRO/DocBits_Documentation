---
description: "Watch five narrated chapters on Advanced Workflows and Workflow Logs in English, with caption files and transcripts."
---

# Video guide

Learn how to build, test and diagnose an Advanced Workflow. Every chapter has English narration; durations are listed below.

The first chapter opens with a fictional, AI-generated administrator, then shows his actions in the real DocBits designer. The next two chapters also use genuine DocBits demonstration drafts. The execution-search preview shows genuine document processing and log controls with empty results. The diagnosis chapter still uses labelled teaching diagrams. For complete control descriptions, use the [Advanced Workflows guide](README.md), [Toolbar & Canvas](toolbar-and-canvas.md), [Nodes](nodes.md), [Variables](variables.md) and [Validation & Testing](validation-and-testing.md).

Caption files are available in WebVTT format below each video. Open the expandable transcript to read the explanation without playing the video.

| Chapter | Duration |
| --- | --- |
| [1. Builder and canvas](#builder-and-canvas) | 5:00 |
| [2. Nodes and routes](#nodes-and-routes) | 1:42 |
| [3. Variables, tests and activation](#variables-tests-and-activation) | 1:53 |
| [4. Find the relevant execution](#find-the-relevant-execution) | 1:50 |
| [5. Trace nodes and diagnose](#trace-nodes-and-diagnose) | 1:43 |

## Builder and canvas

Meet Mike, a fictional, AI-generated administrator, then follow his explanation directly in the real English DocBits interface. Follow Workflow Dashboard, Workflow List and License before he opens an unsaved designer preview. Watch him name a draft, configure an invoice amount check and two actions, arrange the cards, connect both routes and inspect the document and Custom Data test options. The demo account blocks validation because it has no Advanced Workflow subscription; the workflow stays unsaved and inactive.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.mp4" %}

[Open video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.mp4) · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.vtt) · [Transcript (text)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.txt) · 5:00

| In this film | Start |
| --- | --- |
| Meet the administrator | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.mp4#t=0) |
| Check workflow access | [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.mp4#t=14) |
| Name the workflow | [0:47](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.mp4#t=47) |
| Configure the amount check | [1:03](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.mp4#t=63) |
| Add the Approval action | [1:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.mp4#t=98) |
| Add the Standard action | [2:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.mp4#t=125) |
| Arrange the canvas | [2:32](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.mp4#t=152) |
| Connect the routes | [3:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.mp4#t=184) |
| Prepare test cases | [3:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.mp4#t=230) |
| Validate, save and activate | [4:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v1/en.mp4#t=263) |

<details>
<summary>Transcript</summary>

**Meet the administrator**

I look after DocBits here. Let me show you how I build an invoice check and connect its two routes.

**Check workflow access**

I start on Workflow Dashboard and open Workflow List. Then I check License. Workflow and Advanced Workflow both need active access. With those enabled, New Workflow offers Advanced Workflow. This documentation account has no active workflow subscription, so this video continues with an unsaved designer preview.

**Name the workflow**

I'm working in the real DocBits designer. First, I give this draft a clear name. We'll check an invoice amount, then use two simple actions to show the possible routes. This demonstration stays unsaved.

**Configure the amount check**

I open Add and choose And. Under Document Field, I select the Docfield condition. I set the field to total amount. Then I choose Greater Than. And enter one thousand. Use your own document field key. Exactly one thousand does not pass this comparison.

**Add the Approval action**

Now I add a Then card from Document Field. The action sets a document field. I use the demonstration key approval route, and enter Approval. This labels the route. A real approval process needs its own business actions.

**Add the Standard action**

I add a second Then card using the same action. This time, the demonstration field gets the value Standard. Both cards are configured. They still need connections to define which action runs.

**Arrange the canvas**

I drag the cards into a readable layout. The two actions go on the right. The condition sits in the middle, with Start on the left. Moving cards changes their position. It does not create a connection.

**Connect the routes**

I drag from Start's output to the condition's input. The Success route goes to Approval, with a blue connection. The orange Failed Condition route goes to Standard. Red Error is a separate output for evaluation failures. Here it remains unconnected. In a production workflow, decide how you will handle those failures.

**Prepare test cases**

The toolbar Test button opens Select Test Document. I can select a demonstration document, or prepare complete Custom Data. Test amounts above, below, and exactly at one thousand. Check a missing amount too. This account has no Advanced Workflow subscription. I'm showing test preparation, not an executed result.

**Validate, save and activate**

I locate Validate to check connections and card settings. This account blocks validation because the subscription is unavailable. In an enabled account, I would save explicitly to the server. Then check activation separately. The switch is disabled before the first save. The automatic draft indicator refers to a local browser copy. It does not mean this workflow is saved or enabled.

</details>

## Nodes and routes

Follow a connected demonstration draft in the real DocBits designer. See success, false-condition and error routes, then connect two source nodes to Wait ALL, Wait ANY and OR. The example actions write demonstration values to identify the routes.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/en.mp4" %}

[Open video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/en.mp4) · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/en.vtt) · 1:42

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

Follow the connected invoice workflow in the real DocBits designer. Open Variables, compare the types and document-reference form, locate Validate, prepare document or Custom Data tests, and identify Save and activation. The test scenes show example input configuration; they do not show an executed result.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/en.mp4" %}

[Open video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/en.mp4) · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/en.vtt) · 1:53

<details>
<summary>Transcript (English)</summary>

Open Variables with the braces icon. Choose Text, Number, Yes or No, or Document. Search finds variable names. A Document variable stores a reference set by a dedicated workflow action. This form does not accept document values.

Choose a unique name, type and initial value. Creating, editing and deleting variables persist immediately for the organization. Other workflows can share these values. Saving or discarding the canvas cannot undo variable changes.

Select Validate. Review errors and warnings above the canvas. Click a message to focus its node. Check actions, entry connections, handles, cycles and merges. Structural validation does not prove that runtime data is correct.

Toolbar play opens Select Test Document. Choose a document, Custom Data, or Test Without Document for independent cards. Start play runs directly. Tests use the current canvas, including unsaved edits, and simulate destructive actions.

Prepare separate tests above, below and exactly at one thousand, plus missing data. After running, inspect node messages and durations: green success, orange false, red error, gray skipped. Retest fixes; use Test Manager for repeatable scenarios.

Auto-save keeps a local browser draft about every thirty seconds after changes. Save explicitly to the server. The activation toggle is unavailable before the first save. Check the enabled state in Workflow List before expecting automatic execution.

</details>

## Find the relevant execution

{% hint style="info" %}
Preview for testing: genuine DocBits document actions, Document Flow, step timing, empty Workflow Logs and status/date filters. The demonstration document has no saved Advanced Workflow execution. Execution rows, pagination and node diagnosis are not included in this preview.
{% endhint %}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/en.mp4" %}

[Open video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/en.mp4) · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/en.vtt) · 1:50

<details>
<summary>Transcript (English)</summary>

**Start with the document**

In the document Dashboard, open the Actions menu and choose Document flow. The real processing history shows import and OCR. Open a step to inspect waiting and processing time. These processing steps are separate from Advanced Workflow nodes.

**Read the real log counters**

Here are Workflow Logs for the same document. Blue is the total, red errors, yellow failed conditions, and green successes. This demonstration document has no recorded workflow executions. All four counters therefore show zero.

**Check the execution columns**

The table has columns for workflow name, creation time, runtime and result. Use the timestamp to distinguish repeated runs. This preview has no execution row to open. An empty list alone does not prove an execution error.

**Open the status filters**

The tune icon opens the actual filter menu. Choose sorting by name or creation time and select ascending or descending order. Status offers success, failed condition and error. The interface shown here is the real DocBits screen.

**Choose dates and reset filters**

Use the start and end fields or the calendar to choose a period. Dates use year, month and day. Apply requests the results. Clear filters resets the selections. Clear the search separately. The calendar retains English month names in this version.

**Preview: a saved execution is still missing**

This preview lets you check document navigation, processing details and log controls. A saved Advanced Workflow execution is still needed to demonstrate actual rows, pagination, routes and node messages. Those results are not simulated in this video.

</details>

## Trace nodes and diagnose

Expand an advanced execution, select nodes, distinguish false conditions, errors and skipped nodes, inspect merge results, then correct, test and verify the workflow.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/en.mp4" %}

[Open video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/en.mp4) · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/en.vtt) · 1:43

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
