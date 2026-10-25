# AI Assistant in the Script Editor

The script editor has a built-in **AI Assistant** that writes and explains DocBits scripts for you. You describe what the script should do in plain language, and the assistant answers with Python code you can copy into the editor.

{% hint style="info" %}
The AI Assistant is part of **DocNet**. Your organization needs an active DocNet subscription to use it. See [Subscription Plan](../../subscription-plan.md) and [Modules](../../../document-processing/module/README.md).
{% endhint %}

## Open the assistant

1. Go to **Settings → Document Types**, open the document type and click **Scripts**.
2. Click **New**, or open an existing script version as a draft.
3. Click the robot icon next to the script name. The **AI Assistant** panel opens on the right side of the editor.

## What the assistant knows

With every question, DocBits sends the assistant:

* the **scripting reference** (the functions described in [Scripting in DocBits](scripting-in-docbits/README.md)),
* the **document type** of the script,
* the **current script** from the editor,
* the **field names and table columns** your organization uses for this document type.

Because of the field names, the assistant uses your real fields, for example `invoice_date` or `purchase_order`, in `get_field_value()` and `set_field_value()`.

## Write a script with the assistant

1. Type your request into the box at the bottom of the panel, for example: *Set the currency to EUR if it is empty.*
2. Press **Enter** or click the send icon. The answer streams in.
3. Click the copy icon (tooltip **Copy to Editor**) next to a code block to put the code into the script editor.
4. Review the code, give the script a name and save it as a draft.

Follow-up questions work in the same panel. Paste an error message or ask *Why does this script not set the due date?* and the assistant looks at the current script in the editor.

## Always check the result

{% hint style="warning" %}
The assistant can make mistakes. Read the generated code, check that the field names match your document type and test the script with a test document before you activate it. See [Testing Scripts](testing-scripts.md).
{% endhint %}

Scripts only run with the approved script functions. If a script calls a function that does not exist, DocBits rejects it with the message *Unknown function*.

## Usage and limits

* Each answer shows the number of tokens it used (input, output and total) below the reply.
* The usage is recorded as DocNet usage of your organization.
* DocBits rejects the request when the DocNet subscription is missing (*DocNet subscription required*), expired (*DocNet subscription expired*) or the quota is used up (*DocNet quota exhausted*).

## Related pages

* [Creating and Editing Scripts](creating-and-editing-scripts.md)
* [Field Functions](scripting-in-docbits/field-functions.md)
* [Sample Scripts](scripting-in-docbits/sample-scripts/README.md)
* [Script Activation and Management](script-activation-and-management.md)
