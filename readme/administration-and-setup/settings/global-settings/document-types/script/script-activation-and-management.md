# Script Activation and Management

Administrators can use **Scripts** to manage processing rules for a document type. This guide shows where to find scripts, how to switch them on or off, and how to change a published script safely.

## Video guide: manage scripts

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/doc-config-manage-scripts/v4/en.mp4" %}
Manage the scripts of a document type
{% endembed %}

The video shows the script list with filter and sort, switching scripts on and off, copying, the version history and deleting with a confirmation.

## Find a script

1. Open **Settings → Document Types**.
2. On the document type you want to manage, select **Scripts**. The page lists scripts for that document type.
3. Search by name or use **All**, **Active**, and **Inactive** to narrow the list. The list is sorted by execution order by default; the sort control switches between execution order and name (**A-Z** / **Z-A**).

Each card shows the script name, its execution order as a numbered chip, trigger, version, and status. The pencil opens the editor; the copy icon duplicates the script. **New** opens the editor for a new script.

<figure><img src="../../../../../.gitbook/assets/core2170-script-execution-order-list.png" alt="Scripts list sorted by execution order, each card showing a numbered execution-order chip next to the script name"><figcaption><p>The numbered chip on each card is the script's execution order.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc157-scripts-list-inactive-en.png" alt="Scripts list for the Invoice document type with an inactive documentation example and All, Active, Inactive filters"><figcaption><p>Check the status at the right of the script card before changing it.</p></figcaption></figure>

## Set the execution order

Use **Execution order** to control the sequence in which scripts run: lower numbers run first.

1. Open the script in the editor.
2. Enter a whole number in **Execution order**, from 0 upwards. Leave the field empty to keep 0.
3. Save the script. Letters, decimals and negative numbers are rejected with an error on the field, and nothing is saved.

If you change the execution order and then activate a version, DocBits saves the script first and activates the version only when that save succeeds.

<figure><img src="../../../../../.gitbook/assets/core2170-script-execution-order-editor.png" alt="Script editor with the Execution order field next to the document type selector"><figcaption><p>Execution order in the script editor.</p></figcaption></figure>

## Activate or deactivate a script

Use the **Active/Inactive** switch on the script card. The change is saved immediately; the list counts update to show the result. An inactive script remains available to inspect or edit, but it does not run during document processing.

**Check the status after creating a script.** In the current Sandbox interface, saving a new script created an active version and set the card to **Active**. Switch it to **Inactive** if it is only a draft or a test example.

## Change an existing script

1. Select the script card or its pencil icon. A published version is read-only, so you cannot type over it directly.
2. In **Version History**, select the pencil icon on the version you want to change. This creates a **Draft** based on that version.
3. Edit the draft and select the **Save** icon. Review the name, document type, trigger, and code before saving.
4. Test the changed script with representative documents in a test environment. When it is ready, select the check icon for the draft in **Version History** to make that version active.
5. Return to the Scripts list and check the card's **Active/Inactive** switch. The version marked **ACTIVE** in Version History identifies the selected version; the card switch controls whether the script runs.

<figure><img src="../../../../../.gitbook/assets/dbdc157-script-published-version-en.png" alt="Published script version displayed as read-only with a message to clone it as a draft"><figcaption><p>A published version cannot be edited directly. Use the pencil in Version History to create a draft.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc157-script-editable-draft-en.png" alt="Editable draft in Version History next to the currently active script version"><figcaption><p>Save and check the draft before making it the active version.</p></figcaption></figure>

For scripting examples and available functions, see [Scripting in DocBits](scripting-in-docbits/README.md).
