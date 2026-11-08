# Document Trace

<!-- touchless-admin-video-v2-20261104:start -->
**Video chapter (review version):** [Compare runs](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/en.html#chapter=08).
<!-- touchless-admin-video-v2-20261104:end -->

Enter a document ID in **Document ID**, or open a sample document from a cluster, to see **what happened to this one document**.

The header shows the file, its status (for example **In progress**), the run you are looking at and its first blocker, and a **Document** button with the document ID.

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-overview-en.png" alt="Dev NOVA: processing path and recorded points from the first test run"><figcaption><p>New capture from Dev NOVA 11.0.3, 4 November 2026. The fictional test invoice stops at field validation. Classification, supplier search, header extraction and table extraction contain real recorded points; the cards show the document and run history. This is the running product UI.</p></figcaption></figure>

The **Pipeline Path** shows 14 stages: Intake, Classification, E-Document Validation, Supplier Identification, Text Recognition, Header Extraction, Table Extraction, Field Validation, PO Lookup, PO Line Match, Approval, Workflow Routing, Export, ERP Acknowledgement. Each stage carries one state:

| State | Meaning |
| --- | --- |
| **Passed** (green) | The stage ran fine |
| **Stopped Here** (orange) | The stage blocked the document |
| **Not reached** | Shown after the first blocker in the path; check the stage log for any additional recorded execution |
| **Nothing Recorded** (dashed) | No data was recorded for this stage |
| **Not applicable** | The stage does not apply to this document |

### Stage Log

The **Stage Log** below the path lists the same stages with what each one recorded. A status dot and the status word sit on the left and right of every row.

* Each value is a **point chip**: a number with its unit, for example **Confidence 100 %**, **Threshold 60 %**, **Failed rules 0**, **8 missing fields** or **0 mapping gaps**. Percentages are shown as `97 %`, never as `0.97`.
* **Details** opens the full list of points a stage recorded, including the alternatives it considered.
* The stage that blocked the document says why, for example **Field validation failed**.
* A point that no stage recorded is shown as **Not recorded**, never as an invented value. Points are numbers and fixed words, never document text.
* **Show Raw Diagnostics** switches the raw data on when support asks for it.

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-stage-log-en.png" alt="Dev NOVA: stage log with confidence, extraction points and blocked field validation"><figcaption><p>Actual first run: 100% classification confidence, 0 supplier candidates, 1 table row and 7 mapping gaps. Passed means a stage ran; it does not prove a supplier match or that every invoice value is correct. Field validation reports a missing required field.</p></figcaption></figure>

### Runs and changes

Use the run selector to choose an attempt. Run History lists its result and first blocker. Recorded differences compare the selected run with its predecessor, not automatically with the current run. A difference badge includes its unit; unchanged points stay unchanged.

The Document card lists the document type, supplier, invoice number, purchase order, pages and recorded analysis method. Here Manual reflects the document type supplied during test import. The 100% classification value is therefore not independent evidence of automatic classification accuracy.

### Read supplier and table details

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-supplier-en.png" alt="Dev NOVA: supplier details separate detected identifiers, master-data searches and matches"><figcaption><p>This run finds the supplier name on the invoice and searches master data, but assigns no supplier. VAT ID, IBAN, email and GLN are absent from this test invoice. A missing master-data match is a different diagnosis from a missing invoice value.</p></figcaption></figure>

Check three separate questions: was an identifier found on the document, was it looked up, and was a supplier matched? A green stage alone does not answer them.

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-table-en.png" alt="Dev NOVA: first-run table details report seven mapping gaps"><figcaption><p>Table details report 7 mapping gaps for 1 table and 1 row. Check column mapping before concluding that extraction failed. The comparison footer is not a valid baseline for the selected initial run, which has no predecessor.</p></figcaption></figure>

### Recognize a real restart

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-runs-en.png" alt="Dev NOVA: comparison of two actual test runs with unchanged stage points"><figcaption><p>The same test invoice after a genuine manual restart, with no invoice fields corrected. A new run proves another attempt, not an improvement. Unchanged points show No change; no difference badges have been invented.</p></figcaption></figure>

A manual restart is a human intervention. Only a later successful completion would classify this case as AP Assisted. While it remains in progress, it is excluded from the completed-document denominator.

Evidence limits. This case demonstrates no business approval, successful export or ERP acknowledgement. The legacy PO matcher provides no recorded decision path here; this is not evidence of an Infor comparison. In NOVA 11.0.3, the stage log can record a passed PO lookup after blocked field validation while the path labels it Not reached. Check both views. The summary also shows the invoice number as Not recorded although the extraction contains it; use the original and extracted fields for a value comparison.

## Distinguish extraction from source-system data

1. Open the **original invoice** and compare its header fields and lines with what DocBits extracted. Use the values before a person's correction when investigating an earlier run. A current corrected value does not establish what was originally extracted.
2. Read the first blocker in the trace. A passed extraction stage means the stage completed; it does not certify that every value matches the invoice.
3. For a PO discrepancy, compare the invoice values with the **order data actually available to DocBits** and the corresponding Infor record. Include units, price units, quantities and the import time.
4. Record the confirmed difference: **invoice vs extraction**, **correct extraction vs imported source data**, or **Infor vs its imported copy**. Leave the cause open if the required evidence is not recorded.
5. Check the run history for a manual correction, approval or restart, and the final outcome. The outcome and the cause answer different questions.

**Example.** The invoice and extracted value both say €10.00, while the imported order says €9.00. This establishes a discrepancy with the order data, not an extraction error. Confirm which price was agreed and whether Infor itself or its imported copy needs correction. If AP manually restarts the invoice and it then finishes successfully, it is AP assisted despite the correct extraction. See the [worked examples and calculation](./#example-100-correct-extraction-80-ap-touchless).

**Repeated missing fields.** Several documents stopping at Field Validation establish a repeated blocker. Possible causes include extraction, a genuinely absent invoice value, a validation rule or a missing configured default. Compare the evidence before choosing a fix; repetition alone does not prove any one cause.

## Prove the original extraction before drawing conclusions

1. Open **Document** from this trace and verify the document ID and selected run. Compare the original PO number, currency, quantities, units, price units, unit prices, line amounts and relevant totals with the validation fields and tables.
2. Distinguish current values from extraction before a correction. For an already edited invoice, use a matching historical field record or extraction evidence for that run. Switching runs does not promise reconstruction of every old field and cell.
3. If the original extracted value is unavailable, record it as **not assessable**, not correct. Define the fields, line coverage, sample selection and sample size before reporting an independent extraction-quality result.
4. Compare imported PO values and import timestamp with current Infor values. This separates incorrect source data from an outdated copy.

Successive blockers are possible: run 1 may stop because a PO has not arrived; after import, run 2 may reveal a price discrepancy. Neither proves that the first run reached the later check. A manual restart persists after success as AP Assisted; a final ERP rejection instead takes precedence as a process exception. **Not recorded** means missing evidence, not a passed check.

See [Touchless with MCP](touchless-mcp.md) for the matching tool calls and classification of human actions.

## Related pages

* [Touchless Intelligence](./)
* [Supplier Diagnosis and Issue Clusters](touchless-supplier-diagnosis.md)
* [PO Matching Diagnosis](touchless-po-matching-diagnosis.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->

<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->

The five new trace screenshots show the localized Dev NOVA 11.0.3 UI and the same owned test invoice. Any separate original-versus-field image remains a limited illustration of that comparison.
