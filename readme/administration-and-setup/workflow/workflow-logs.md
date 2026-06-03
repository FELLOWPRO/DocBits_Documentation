# Workflow Logs

## **Overview**

The **Workflow Logs** allow users to analyze which workflows were executed for a document, understand the execution results, and drill into condition-level details for debugging or validation.

## **Accessing Workflow Logs**

To access workflow logs:

1. Navigate to the **Dashboard**.
2. Click the **Actions menu** (three-dot icon) next to the desired document.
3. Select **Workflow Logs** from the menu.
   * <mark style="color:red;">**Note**</mark>: The Workflow feature must be enabled to access this option.
4.  A **side panel** opens showing a summary of executed workflows.\\

    <div align="left"><figure><img src="../../.gitbook/assets/image (8).png" alt="" width="563"><figcaption></figcaption></figure></div>

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

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="" width="563"><figcaption></figcaption></figure></div>

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
