# Use the dashboard

### Filters

| Filter                            | What it does                                                                                                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **7D / 30D / 90D**                | The period for the key figures and the queue. The default is 30 days                                                                                                                                                           |
| **Document Type**                 | Filters the Touchless metrics and related analysis to one type, for example INVOICE. Learned rule proposals currently have their own selection; see below                                                                                                                                                                        |
| **Segment field / Segment value** | Only if your organisation runs several processes through one document type (for example direct, indirect and EAM orders in the field `order_type`). Pick a field to see the breakdown, pick a value to narrow everything to it |
| **Document ID**                   | Opens the **Document Trace** for one document                                                                                                                                                                                  |

The **sub-organisation** you selected at the top of DocBits narrows the key figures and the supplier queue. Issue clusters and the AI analysis always cover the whole organisation.

### Top-level document type versus learned rule proposals

The top selector and the document type in **Learned rule proposals** are independent in the currently checked implementation. The section loads its own available types and initially picks the first entry. Selecting **ORDER_CONFIRMATION** above can therefore leave **INVOICE** selected below. Those proposals concern invoices, not the order confirmations chosen for the metrics.

Before applying a rule, check the type shown inside that section. If no matching type is available there, proposals for it have not been established. The section also uses its own data basis, such as corrected documents from the last 60 days, rather than automatically adopting the headline period. This describes the current separate controls; it does not claim synchronisation has been implemented.

### The five key figures

<figure><img src="../../../.gitbook/assets/touchless-kpi-cards.png" alt="The five key figures: Pure touchless, AP touchless, AP assisted, Process exceptions and Diagnosis coverage"><figcaption><p>The five key figures. Here the pure rate is 50.3 % (156 documents), which is 19.7 points under the 70 % target, and diagnosis coverage is 100 %. Example organisation with demo data; supplier names are fictional.</p></figcaption></figure>

| Card                   | Shows                                             | Example (illustrative)                                                      |
| ---------------------- | ------------------------------------------------- | --------------------------------------------------------------------------- |
| **Pure touchless**     | The percentage and the difference to the target   | **63.2 %** · "120 documents" · "−6.8 pp vs 70 % target" (red, below target) |
| **AP touchless**       | Combined percentage: pure plus approval-only; the document count underneath refers to the approval-only outcome | **78.9 %** · "30 documents" (approval only) |
| **AP assisted**        | The number of documents and their share           | **30** · 15.8 %                                                             |
| **Process exceptions** | The number of documents and their share           | **10** · 5.3 %                                                              |
| **Diagnosis coverage** | How many blocked documents have a **known** cause | **80 %** · "10 without a known cause"                                       |

* In the screenshot, 156 pure documents plus 11 approval-only documents give **167 ÷ 310 = 53.9% AP touchless**. Pure alone is **156 ÷ 310 = 50.3%**. The two percentages overlap.
* A card shows a dash (—) instead of **0 %** when there is nothing to measure. A dash means "no data", not "zero".
* **Diagnosis coverage** = documents with a known blocking reason ÷ all blocked documents. Example: 50 blocked documents, 10 with an unknown cause → 40 ÷ 50 = **80 %**. A low value means "we do not yet understand why documents stop". Improve it before you try to fix individual causes.
* **Click a card** to open the document list behind the number in a new tab ("View the documents behind this number"). Cards with 0 documents are not clickable.

### Touchless rate over time

<figure><img src="../../../.gitbook/assets/touchless-trend.png" alt="Line chart of the pure touchless and AP touchless rate per day with the 70 percent target line"><figcaption><p>The rate per day with the target line. Here the rate stays between 40 and 60 % and drops sharply from 10 October. Example organisation with demo data; supplier names are fictional.</p></figcaption></figure>

The screenshot shows separate outcome shares: **Pure touchless** and **AP touchless** (approval only), plus the **target line**. In this captured view the blue line is the approval-only share, not the combined AP headline rate. The combined rate adds the pure and approval-only shares over the same population. Keep outcome shares and the combined KPI distinct when reading charts. Short periods show daily points, long periods weekly points.

**Example.** After you switched on automatic PO matching on 1 October, the pure rate climbs from 55 % to 68 % within two weeks. The chart shows the day the curve turns, so you can investigate the timing. A before/after association does not by itself prove that this setting caused the improvement. Compare document type, supplier mix and other changes.

### Where touchless is lost first

<figure><img src="../../../.gitbook/assets/touchless-blocking-stages.png" alt="Bar chart of the blocked documents per first blocking stage and reason"><figcaption><p>Blocked documents by the stage and reason where they stopped first. Here <strong>Field validation: Required field missing</strong> costs the most documents (58), then <strong>Export mapping failed</strong> (46) and <strong>PO item mismatch</strong> (27). Example organisation with demo data; supplier names are fictional.</p></figcaption></figure>

A bar chart of **Blocked documents** per pipeline stage: the **first** stage that stopped a document.

**Example.** Bars: Supplier Identification 12, Field Validation 41, PO Line Match 7. The biggest bar tells you to look at **Field Validation** first. A missing extracted value is one possible cause; compare the original invoice, field rules and available source data before confirming it.

### Supplier opportunities

<figure><img src="../../../.gitbook/assets/touchless-supplier-queue.png" alt="The Supplier opportunities table with volume, pure rate, lost documents, root cause, recoverable documents, expected lift, confidence and status"><figcaption><p>The supplier queue (shortened to the first four rows). The first supplier has 106 documents, a pure rate of 38.7 % and 65 recoverable documents, so fixing it is worth <strong>+21 pp</strong>. Example organisation with demo data; supplier names are fictional.</p></figcaption></figure>

The queue answers **"Which supplier should we fix first?"** It is sorted by **Recoverable** documents, highest first, 25 rows per page.

| Column                         | Meaning                                                                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Supplier Number / Supplier** | The supplier. Documents without a recognised supplier appear as **No supplier identified (n documents)**                                                  |
| **Volume**                     | Eligible documents of the supplier in the period                                                                                                          |
| **Pure Rate**                  | Share of pure touchless documents. Green if at or above the target, red if below                                                                          |
| **Lost Documents**             | Documents that ended as AP assisted or as a process exception. Not always a person: an ERP rejection or a document that stalled for seven days counts too |
| **Root Cause**                 | Who owns the fix: Configuration, ERP integration, Export, Extraction, Master data, Measurement, PO matching, User process, Validation or Unknown          |
| **Recoverable**                | Lost documents whose cause DocBits can fix: configuration, master data or supplier template                                                               |
| **Expected Lift**              | How many **percentage points** your organisation's rate would gain if every recoverable document of this supplier ran touchless (**+x pp**)               |
| **Confidence**                 | **High**, **Medium** or **Low**: how sure the diagnosis is                                                                                                |
| **Status**                     | New, Open, Investigating, In progress, Confirmed, Resolved, Dismissed. A supplier with too few documents shows **NEEDS\_DIAGNOSIS**                       |

**Example.** Your organisation has 1,000 eligible documents in the period. Supplier A has 40 recoverable documents, Supplier B has 90 lost documents but only 10 recoverable (their problem is on their side).

* Supplier A: 40 ÷ 1,000 = **+4.0 pp expected lift**
* Supplier B: 10 ÷ 1,000 = **+1.0 pp**, although B has more lost documents

The queue ranks A above B because **expected lift** is measured against your whole organisation, not against the supplier. A supplier with four bad documents cannot outrank one with four hundred.

Use the search box ("Search supplier number or name") to find a supplier. Click a row to open the **Supplier Diagnosis**.

### Compare suppliers

<figure><img src="../../../.gitbook/assets/touchless-compare-suppliers.png" alt="The Compare suppliers page with three suppliers side by side and a bar chart of their outcomes"><figcaption><p>Three suppliers side by side: pure rate, lost and recoverable documents, root cause, expected lift and a bar chart of the outcomes. Each <strong>Open</strong> leads to the Supplier Diagnosis. Example organisation with demo data; supplier names are fictional.</p></figcaption></figure>

Click **Compare suppliers**, tick **two to five** suppliers (each is listed with its number of blocked documents) and click **Compare**.

The comparison shows the suppliers side by side: **Pure rate**, **Lost documents**, **Recoverable**, **Root cause**, **Expected lift**, a bar chart of the outcomes, and a link to each **Supplier Diagnosis**.

**Example.** Supplier A and B send the same invoice layout. B has a pure rate of 80 %, A only 35 %. A's diagnosis suggests "Master data". Compare original invoices, extracted values and imported supplier records before confirming that cause. The rate difference alone does not prove that the layout is correct or that A's master data is incomplete.

### Analyse with AI

The button **Analyse n clusters with AI** analyses the issue clusters with the highest touchless potential (at least a minimum number of documents each). It takes about 13 seconds per cluster and covers the **whole organisation**. Only administrators can start it.

While it runs you see **Queued**, **Running**, **Done**, **Already analysed** or **Error** for each cluster, with a link **Open cluster**. If AI is switched off or not configured in the environment, the button is disabled with the reason, and **everything else on the page keeps working**.

## Work with Touchless Intelligence: a routine

1. **Weekly**: open the tab and check the **rate** and the **trend** against the target.
2. Look at **Diagnosis coverage**. Below about 80 %, first find out why documents stop.
3. Read **Where touchless is lost first** and pick the biggest stage.
4. Open **Supplier opportunities**. Sort by **Expected lift** and take the top supplier with the status **RECOVERABLE**.
5. Read the **issue clusters**, check **Missing evidence**, then follow **What to change**.
6. Fix one confirmed cause. For a supported DocBits proposal use preview and change history. For an Infor correction, document the source and import separately; it does not automatically create a DocBits setting-change entry.
7. After two weeks check the **before/after** result.

## Who can see it

* The tab is part of the Analytics Dashboard. Your administrator enables it for the organisation. If the tab is missing, ask your administrator.
* **Organisation administrators** always see it.
* Other users see it when an administrator granted their role the **Analytics dashboard** tab (**Settings → Roles**). Without a grant, only administrators have access.
* Some actions are for administrators only: **AI analysis**, **applying and undoing a change**, **learned rule proposals** and the **Consulting report**.

If you are not allowed, the page shows _Action not allowed, please contact the administrator_.

## Related pages

* [Touchless Intelligence](./)
* [Metrics and calculation](touchless-metrics.md)
* [Worked examples: price and quantity](touchless-examples.md)
* [Supplier Diagnosis and Issue Clusters](touchless-supplier-diagnosis.md)
* [PO Matching Diagnosis](touchless-po-matching-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Change Proposals and Reports](touchless-change-proposals.md)
* [Explain and improve Touchless with MCP](touchless-mcp.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
