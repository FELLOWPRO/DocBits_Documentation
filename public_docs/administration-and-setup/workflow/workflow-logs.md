# Workflow Logs

For narrated explanations of the advanced log view, watch [Find the relevant execution](advanced-workflow-builder/videos.md#find-the-relevant-execution) and [Trace nodes and diagnose](advanced-workflow-builder/videos.md#trace-nodes-and-diagnose). Both chapters are available in English and German, with caption files and transcripts.

## **Overview**

The **Workflow Logs** allow users to analyze which workflows were executed for a document, understand the execution results, and drill into condition-level details for debugging or validation.

## **Accessing Workflow Logs**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4" %}

**Video:** Reading the workflow logs · 1:34 · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.vtt)

<details>

<summary>Transcript</summary>

**Open the workflow logs** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=0.25)

Every document keeps the logs of the workflows that ran on it. In the document dashboard, open the actions of a document and choose Workflow logs.

**Runs and their results** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=12.15)

At the top you see how many runs there were, and how many ended with an error, a failed condition or success. Below, each run is listed with its workflow, time, duration and result.

**The path of one run** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=25.716)

Drag the divider to the left to give the logs more room. Then click a run to see the path it took. Each card shows its result: green for success, orange for a failed condition, red for an error. Here the And card ended with a failed condition, so the Then card after it did not run.

**Why a card ended this way** · [0:45](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=45.35)

Select a card to read its log. It says what the card compared and why it ended this way. Here, the document is ready for validation, but the card expects pending second approval.

**An error and its reason** · [0:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=58.283)

A run that ends with an error shows the failing card in red. Here the And card could not read the delivery address from the document. Missing data is always an error, so the Then card after it did not run.

**Find runs** · [1:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=73.216)

With many runs, use the search to find a workflow by name, and the filter button to narrow the list by status or date.

**Execution limit note** · [1:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=83.116)

A note at the top appears when a workflow has reached its execution limit on this document. The video about execution limits explains it.

</details>

To access workflow logs:

1. Navigate to the **Dashboard**.
2. Click the **Actions menu** (three-dot icon) next to the desired document.
3. Select **Workflow Logs** from the menu.
   * <mark style="color:red;">**Note**</mark>: The Workflow feature must be enabled to access this option.
4.  A **side panel** opens showing a summary of executed workflows.\\

    <div align="left"><figure><img src="../../.gitbook/assets/image (5).png" alt="Dashboard with the workflow logs side panel showing summary counters and a table of executed workflows with result icons" width="563"><figcaption></figcaption></figure></div>

## **Open a log as its own page**

The side panel covers the document list. For a document whose workflow you inspect for a while, open the same log as a full page: select the new-window icon in the header of the panel. The page has the address `/workflows/logs/<document id>`, so you can keep it open in a second browser window or send the address to a colleague who has access to the document.

The page shows the same summary counters, the same table of executed workflows and the same detail view as the panel.

## **Switch to another document**

On the full page, a search field above the list finds a document by name or by its ID. The results show the upload date, the assignee and the status of each document, so you can tell documents with similar names apart. Selecting a result loads its workflow log and puts the document into the address. The search covers the documents of your organisation that your permissions allow you to see; when nothing matches, DocBits says so below the field instead of showing an empty list.

## **Components of the Workflow Logs Panel**

#### **1. Workflow Summary Counters**

Located at the top of the logs panel:

* **Blue**: Total number of workflows executed.
* **Red**: Workflows that ended in **errors**.
* **Yellow**: Workflows that were **not finished** due to condition mismatches.
* **Green**: Successfully **executed** workflows.

#### **2. Workflow Execution Table**

Each row in the table represents one workflow execution and includes:

* **Workflow Name**
* **Timestamp** (Created On)
* **Runtime** (in seconds)
* **Result Icon**:
  * Green checkmark: Workflow executed successfully.
  * Red cross: Workflow executed with an error.
  * Orange dash: Execution was stopped due to a conditions was not met

Clicking the **arrow** on the left of each row expands the **workflow detail view**.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Expanded workflow log row showing When and And condition cards with green checks and a grayed card that was not met, plus card logs" width="563"><figcaption></figcaption></figure></div>

### **Workflow Detail View**

Clicking a specific workflow row opens its **detailed execution log**, showing:

#### **Condition Evaluation**

* **When...** block: Initial condition.
* **And...** block(s): Additional conditions.
* **Then...** block(s): Actions performed when all conditions are met.

Each condition line shows:

* **Green check**: Condition was met.
* **Orange dash**: Condition was not met.
* **Red cross**: Condition failed **due to an error**

### **Important Behavior Note**

If a condition in a workflow is **not met**, the system **stops evaluating any further workflow cards** within that workflow. This behavior prevents unnecessary processing\
As a visual indicator, the card that **did not meet its condition** is shown in **gray**, and all **subsequent cards** in the same workflow will also appear **gray**, indicating that they were **not executed**.
