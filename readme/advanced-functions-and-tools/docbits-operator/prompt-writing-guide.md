# Prompt Writing Guide

This guide explains how to write effective prompts for the DocBits Operator. Prompts are step-by-step instructions that direct the operator to perform specific tasks, such as navigating web pages, interacting with UI elements, and entering data.

### What is a Prompt?

A prompt is a sequence of instructions written in text that guides the operator to execute a workflow. Prompts can include commands like clicking buttons, filling out forms, waiting for pages or elements to load, and more.

### Prompt Syntax and Structure

* Each instruction should be written as a numbered step.
* Use clear, concise language to describe each action.
* Specify UI elements by name, label, or index number to ensure precision.
* Use consistent formatting to improve readability.

### Using Variables in Prompts

Variables allow you to make prompts dynamic by inserting different values at runtime. Instead of hardcoding values like dates or document numbers, use placeholders inside curly braces—for example: `{invoice_number}`, `{url}`, or `{purchase_order}`.

This makes prompts reusable and adaptable across different workflows or data sets.

#### How to Use Variables

* Write variables inside curly braces within your prompt text:
  * Enter the invoice number: {invoice\_number} in the 'Invoice number HP' field.
* Each variable must have a unique name (e.g., `invoice_number`, `url`, `document_type`).
* Variable names must not include spaces or special characters (underscores are allowed).
* For workflows, variable names must exactly match the document’s field IDs to enable automatic data mapping.

### Prompt Variables Popup

To open the Prompt Variables popup, click the **cogwheel icon** located next to the prompt input field.

<div align="left"><figure><img src="../../.gitbook/assets/prompt_variables_icon_location.png" alt="Prompt Variables Icon Location" width="426"><figcaption></figcaption></figure></div>

### Popup Layout and Controls

<div align="left"><figure><img src="../../.gitbook/assets/image (11).png" alt="Prompt Variables Popup Interface" width="375"><figcaption></figcaption></figure></div>

* **Key Input Field:** Enter the variable name here (without curly braces).
* **Value Input Field:** Enter the value to be used for this variable when the prompt runs.
* **Save as Sensitive (Checkbox):** When checked, this marks the variable value as sensitive. Sensitive values are encrypted and hidden in workflows to protect confidential information from unauthorized users.
* **Add Button (+):** Click to add another key-value pair input row.
* **Delete Icon (Trashcan):** When multiple key-value pairs exist, all pairs except the first show a small trashcan icon to delete that specific pair.
* **Clear Button:** Resets the popup by clearing all key-value pairs and values entered.
* **Save Button :** Saves all the defined variables and their values for the current prompt.
