# AI Table

Use AI Table to review extracted line items, correct columns and save suitable instructions for a supplier layout. Choose the guide for your task below. Structured Output has its own configuration guide, with Default/Yes/No, overrides, the preview and a worked example.

* [Settings and overrides](configuration.md)
* [Structured Output for Tables](structured-output.md)
* [Columns and corrections](columns-and-corrections.md)
* [AI instructions](ai-instructions.md)
* [AI Table Tags](ai-table-tags.md)
* [Explain extraction and troubleshoot](explain-extraction.md)
* [Assistant and permissions](assistant-and-permissions.md)
* [Videos](videos.md)

<figure><img src="../../../.gitbook/assets/anatomy-ai-table.svg" alt="Isometric illustration of a table reader: a reader head with an instructions cartridge scans a document table, a patch panel plugs each returned column into a configured column, and the configured columns stand as bins with a three-position Use AI knob each."><figcaption><p>The AI reads the table and returns columns. Each returned column is mapped to a configured table column (a returned column without a mapping stays hidden), each configured column has its own Use AI setting (Default, Yes or No), and the AI instructions and <strong>Save as training</strong> shape how the next documents of the supplier layout are read.</p></figcaption></figure>

## When you get the AI table

* An admin has switched on **AI Table extraction** (Settings → Document Processing → Classification and Extraction, see [Settings for admins](./#settings-for-admins)). If it is off, the table area shows _AI Table will display here. Enable in …_.
* Check readable text or the selected Vision input. Saved classic table rules can still determine the effective table path; check [which extraction path was actually used](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md).
* Individual columns have their own three-state Use AI selection. Check the effective source and supplier rules as well as this selection; enabling Structured Output does not replace every rule-based table.

Which AI tier reads the table (Fast, Full, Nexus) is set per organization and can be overridden per supplier, see [Supplier-Specific AI Model](../validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

## The AI table at a glance

<figure><img src="../../../.gitbook/assets/ai-table-overview-en.png" alt="AI Extracted table with its column headers and four rows"><figcaption><p>The two tabs, the AI Extracted table and its column headers.</p></figcaption></figure>

* **Tabs.** _AI Extracted table_ is what the AI read. _Extracted table_ is the classic table from trained rules. The AI tab opens by default when the document has an AI table.
* **Column header.** Each column shows its name, a small **origin** symbol (hover it: _AI · mapping_, _AI · synonym_ and so on tell you how the AI matched the column), a **three-dots** menu and, for a mapped column, a **name button** you can click to change which column it is.
* **Row buttons.** The **x** at the start of a row removes that row. Right-click a row for _Select as additional cost_ / _Remove as additional cost_.
* **Footer toolbar.** The icons at the bottom of the screen add or hide columns and rows, see [Footer toolbar](./#footer-toolbar).
* **AI instructions card** below the table: prompt, extra columns, **Test change**, **Apply**, **Save as training**, **Delete**, **Export**, see [Give the AI instructions](./#give-the-ai-instructions).

{% hint style="info" %}
The column controls only work when you can edit the document. If they are greyed out, the document is read-only or locked in another session. When the red banner says the document is locked by your own user in another session, **Unlock** takes the lock over.
{% endhint %}


## Settings for admins

Continue here: [Settings and overrides](configuration.md).

### Use AI per column

Continue here: [Structured Output for Tables](structured-output.md).

<a id="pick-the-right-column-remap"></a>
<a id="the-three-dots-menu"></a>
<a id="footer-toolbar"></a>

## Change a column

Continue here: [Columns and corrections](columns-and-corrections.md).

<a id="suggest-with-nexus"></a>
<a id="test-apply-save-what-each-button-does"></a>

## Give the AI instructions

Continue here: [AI instructions](ai-instructions.md).


## See what the AI did

Continue here: [Explain extraction and troubleshoot](explain-extraction.md).


## Practical examples

Continue here: [Explain extraction and troubleshoot](explain-extraction.md).

<a id="suggest-a-rule-to-your-admin"></a>

## The Assistant and the AI table

Continue here: [Assistant and permissions](assistant-and-permissions.md).


## Who can do what

Continue here: [Assistant and permissions](assistant-and-permissions.md).

<a id="1-read-the-ai-table"></a>
<a id="2-fix-a-column-and-teach-docbits"></a>
<a id="3-three-typical-problems"></a>
<a id="4-discount-tax-and-zero-quantity-lines"></a>
<a id="5-what-the-ai-already-reads-correctly"></a>
<a id="6-the-assistant-and-who-can-change-what"></a>

## Video series

Continue here: [Videos](videos.md).


## Administrator video: change a column

Continue here: [Videos](videos.md).

## Related pages

* [AI Table Tags and instructions](ai-table-tags.md)
* [Training Line Fields / Table Training](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/)
* [Supplier-Specific AI Model](../validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md)
* [Which Extraction Path Was Used?](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md)
* [Touchless Intelligence](../../../administration-and-setup/analytics-dashboard/touchless-intelligence/)
