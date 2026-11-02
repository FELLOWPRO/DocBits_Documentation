# Then

A **Then** card tells a workflow what to do after its **When** trigger and any **And** conditions. In the **Workflow Builder**, select **Add Card** under **Then...**. Choose a category on the left or type a name in **Search Card**. Select a card preview to add it, fill in the fields shown on the card, and save the workflow. Scroll within the picker to see more cards. Select **×** to close it without adding a card. See [Workflow](../../) for the complete sequence.

The previews below show available actions, not completed settings. Pick the action that matches the outcome you want.

## Document Field

Set or invert a checkbox, put text into a field, or copy one field into another. Choose the field names and value requested by the card. See [Document Field](document-field/).

<figure><img src="../../../../.gitbook/assets/then-category-document-field-en.png" alt="English Then card picker with Document Field selected; previews show checkbox, text, and copy field actions."><figcaption><p>Change a field or copy its contents.</p></figcaption></figure>

## Document

Choose **Approve the Document** or **Reject the Document** when the workflow should make that decision. Use an **And** condition first if approval should depend on a check. See [Document](document/).

<figure><img src="../../../../.gitbook/assets/then-category-document-en.png" alt="English Then card picker with Document selected; Approve the Document and Reject the Document previews are visible."><figcaption><p>Approve or reject the current document.</p></figcaption></figure>

## Logic

Use these cards to convert values between number, text, and boolean formats, or read a value from JSON. Choose the input and output fields on the selected card.

<figure><img src="../../../../.gitbook/assets/then-category-logic-en.png" alt="English Then card picker with Logic selected; visible previews convert data types and read values from JSON."><figcaption><p>Transform values for a later workflow step.</p></figcaption></figure>

## Status

Choose **Change Status** to move the document to a selected status. The card can also trigger another workflow. See [Status](status/).

<figure><img src="../../../../.gitbook/assets/then-category-status-en.png" alt="English Then card picker with Status selected; the Change Status preview includes a status field and optional workflow trigger."><figcaption><p>Move the document to another status.</p></figcaption></figure>

## Prompts and Scripts

Choose this category to run a DocOperator prompt script. Select the script and the variables requested by the card. The card also offers execution settings such as retries.

<figure><img src="../../../../.gitbook/assets/then-category-prompts-scripts-en.png" alt="English Then card picker with Prompts and Scripts selected; one DocOperator prompt script preview is visible."><figcaption><p>Run a configured DocOperator prompt script.</p></figcaption></figure>

## Export

Start an export, export with a chosen configuration, or queue a final export. Choose the export configuration and pending-task option shown on your card. See [Export](export/).

<figure><img src="../../../../.gitbook/assets/then-category-export-en.png" alt="English Then card picker with Export selected; previews show start, configured, queued, and alternate exports."><figcaption><p>Select when and how the document is exported.</p></figcaption></figure>

## Task

Create a task or notification and assign it to a user or group. Enter the title, description, priority, and notification settings requested by the card. Some cards assign sequentially. See [Task](task/).

<figure><img src="../../../../.gitbook/assets/then-category-task-en.png" alt="English Then card picker with Task selected; visible previews create or assign tasks and notifications."><figcaption><p>Create follow-up work for a person or group.</p></figcaption></figure>

## Email

Send an email using a selected template, either to recipients or to groups. Choose the template and destination on the card.

<figure><img src="../../../../.gitbook/assets/then-category-email-en.png" alt="English Then card picker with Email selected; previews send a templated email to recipients or groups."><figcaption><p>Send a templated email.</p></figcaption></figure>

## Table

Change entries or calculate values in a document table. Select the table, columns, operator, and result column requested by the card. See [Table](table/).

<figure><img src="../../../../.gitbook/assets/then-category-table-en.png" alt="English Then card picker with Table selected; previews change entries and calculate result columns."><figcaption><p>Update or calculate table data.</p></figcaption></figure>

## Assignee

Assign the document to a user, group, recipient, or sub-organization. Some cards use a field or decision table and offer a fallback. Choose the right destination and fallback on the selected card. See [Assignee](assignee/).

<figure><img src="../../../../.gitbook/assets/then-category-assignee-en.png" alt="English Then card picker with Assignee selected; visible previews assign a user, recipient, group, or supplier contact."><figcaption><p>Route the document to the next responsible person or group.</p></figcaption></figure>

## Action

Run another workflow, send an HTTPS request, call an API, or use the cost-increase calculation card. These actions can affect other systems; ask your administrator which endpoint and settings to use. See [Action](action/).

<figure><img src="../../../../.gitbook/assets/then-category-action-en.png" alt="English Then card picker with Action selected; previews show Run workflow, HTTPS request, API call, and cost increase calculation."><figcaption><p>Start another workflow or integration action.</p></figcaption></figure>

[Detailed logic-card fields, JSON paths, triggers and tests](../logic-cards-guide.md).
