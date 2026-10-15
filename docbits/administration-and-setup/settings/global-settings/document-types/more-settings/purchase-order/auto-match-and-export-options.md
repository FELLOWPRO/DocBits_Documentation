# Auto Match & Export options

Three settings at the end of the **Purchase Order** card decide who sees the PO matching shortcuts and which documents may export on their own after a match. They apply to one document type at a time.

<figure><img src="../../../../../../.gitbook/assets/doc-type-settings-po-options.png" alt="The Purchase Order card of the document type settings with all PO options"><figcaption><p>The Purchase Order card. The three options below are the last three rows.</p></figcaption></figure>

## Allow Auto Export For Non Matchable PO Lines

Automatic export after PO matching normally requires a **fully matched** document. When this switch is on, documents whose status is **No matchable PO lines** may also export automatically. That status means the purchase order has no lines the invoice can be matched to.

* **Off (default):** only fully matched documents export automatically.
* **On:** fully matched documents and documents with no matchable PO lines export automatically.

The switch only matters when documents export automatically, for example with [**Auto Export if PO matched 100%**](../../../../document-processing/module/auto-export-if-po-matched-100.md) or a DocFlow export card. It does not change how lines are matched.

## Auto Match & Export visible to

The PO matching screen has an **Auto Match & Export** action. It matches the document and exports it right after the match. This setting controls who gets the action:

| Value | Who sees the action |
| ----- | ------------------- |
| **Only admin** (default) | Administrators |
| **All users** | Every user who can open the PO matching screen |

Administrators always see the action. The setting does not switch the feature on. The module [**Auto Export if PO matched 100%**](../../../../document-processing/module/auto-export-if-po-matched-100.md) has to be active for the organisation.

## Use Lines Net Amount for Matched Total visible to

The PO matching screen can calculate the **Matched Total** from the **Net Amount** of the matched invoice lines instead of computing it. This setting controls who can switch that calculation on:

| Value | Who sees the switch |
| ----- | ------------------- |
| **Only admin** (default) | Administrators |
| **All users** | Every user who can open the PO matching screen |

When the switch is on, the Matched Total uses the Net Amount values directly from the matched invoice lines.
