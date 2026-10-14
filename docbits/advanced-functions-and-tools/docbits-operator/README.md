# DocBits Operator

## Overview

The **DocBits Operator** is an AI-powered automation assistant designed to simplify repetitive tasks in your workflows. Users create _prompts_—step-by-step instructions enhanced with variables—that guide the AI to navigate, input data, and click through interfaces automatically. This reduces manual effort and speeds up routine operations.

## Enabling the DocBits Operator

To enable the DocBits Operator, follow these steps:

1. **Navigate to Settings**:
   * From the Dashboard, go to **Settings**.
   *   Select **Document Processing** and then choose **Module**.

       <figure><img src="../../.gitbook/assets/docbits_operator_module_selection.png" alt="DocBits Operator Module Selection"><figcaption></figcaption></figure>
2. **Enable the Feature**:
   * Scroll down to locate the **DocBits Operator** option.
   *   Toggle the slider to enable the **DocBits Operator**.

       <div align="left"><figure><img src="../../.gitbook/assets/docbits_operator_enable_toggle.png" alt="DocBits Operator Enable Toggle" width="563"><figcaption></figcaption></figure></div>

## Accessing the Interface

* Once the feature is enabled, open the **DocBits Operator** from the main navigation menu.

### **1. Prompt Input**

At the bottom of the screen, there is an input field labeled _“Enter your prompt here…”_. This is where users write instructions for the operator to follow.

Next to the input field are several control buttons:

* **Prompt Variables** – Opens a popup where you can enter key-value pairs used in the prompt. Variables are written using curly braces, like `{invoice_number}` or `{url}`. These values apply only to the current prompt in the input field.
* **Save Prompt** – Saves the current prompt. Choose to save it as either:
  * **Organization Prompt** – Editable within your organization; includes both the prompt and defined variable values.
  * **Global Prompt** – Shared across all tenants; includes only the prompt and variable placeholders (no values are saved).
* **Clear Chat** – Clears the current conversation with the operator, but leaves the prompt in the input field unchanged. Useful when reusing or refining a prompt.

For detailed guidance on how to write effective prompts—including syntax, variables and examples—please see the [**Prompt Writing Guide**](prompt-writing-guide.md).

### **2. Sidebar Navigation**

Use the top-left icon to open or close the sidebar. The sidebar shows saved prompts, organized in two categories:

* **Organization Prompts**: Editable and reusable within your organization.
* **Global Prompts**: Shared across all tenants. These cannot store variables and cannot be edited or deleted.
  * A global prompt is still editable and deletable by the **organization that created it**, where it appears under Organization Prompts.
* **Search Functionality:** a search bar at the top of the sidebar allows users to quickly find saved prompts by name or keyword.
* **Icon Reference:** Each saved prompt has a set of action icons
  * **Arrow** – Start the prompt
  * **Pen** – Edit the prompt (available only for your own organization’s prompts)
  * **Trashcan** – Delete the prompt (available only for your own organization’s prompts)

### 3. Save Prompt

Clicking the **Save Prompt** button opens a popup where you can save the current prompt for future use.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Save Prompt Popup"><figcaption></figcaption></figure></div>

#### **Save Prompt Popup Fields**

* **Prompt Name:** Enter a name to identify the prompt.
* **Save Prompt Publicly (Checkbox):** When checked, the prompt will be saved as a **Global Prompt**. Global Prompts are shared across all tenants and cannot store variable **values** (only variable **names**).
* **Edit Variables:** Opens the [**Prompt Variables Popup**](prompt-writing-guide.md#prompt-variables-popup) to review or adjust variable definitions before saving.

**Actions**

* **Cancel:** Closes the popup without saving.
* **Save:** Saves the prompt using the specified name and visibility setting.

### 4. Prompt Execution Controls

When a prompt is running, users have several control options to manage or intervene in the execution process:

* **Pause Prompt:** Temporarily halts the current execution. Useful if you want to observe the current state or prepare the system for the next steps.
* **Resume Prompt:** Continues execution from the point where it was paused. ![](<../../.gitbook/assets/image (4).png>)
* **Cancel Prompt:** Stops the execution entirely and resets the session. This is helpful if the prompt needs to be aborted or restarted due to incorrect behavior or changes in input.
* **Take Control:** Allows the user to manually intervene by interacting directly with the system. This is useful if the operator gets stuck or misinterprets a step. Taking control **automatically pauses** the prompt and switches to manual mode until you choose to resume or cancel.

### 5. Operator Detail View

Once a prompt is started, an additional button becomes available that allows users to switch to a **detailed execution view**. ![](<../../.gitbook/assets/Detailed view .jpg>)

* **Open Detail View:** This button takes you to a dedicated view that shows, step-by-step, what the operator is doing in real time.

In the detail view, users can:

* Monitor each action being performed (e.g., clicks, inputs, waits).
* See which step is currently active.
* Identify where issues occur if the prompt encounters problems.
* Use the same **Pause**, **Resume**, **Cancel**, and **Take Control** actions.

<div align="left"><figure><img src="../../.gitbook/assets/detailed view 2 .jpg" alt="" width="563"><figcaption></figcaption></figure></div>
