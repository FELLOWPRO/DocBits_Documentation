# Touchless Intelligence

## Overview

**Touchless Intelligence** answers two questions about your document processing:

1. **How many documents run through DocBits without anyone touching them?** This is your *touchless rate*.
2. **Why do the others stop, and what should we change so that fewer stop?** This is the *diagnosis*.

It is a tab of the [Analytics Dashboard](analytics-dashboard.md). It does not add any work for your team: DocBits records what happens to every document in the processing pipeline and evaluates the result every 15 minutes.

### What you can do with it

| You want to… | Use | Example |
| --- | --- | --- |
| See how automated you are | The five **key figures** at the top | "63.2 % of our documents ran without a person last month" |
| See the trend | **Touchless rate over time** | "The rate rose from 55 % to 68 % since we fixed supplier master data" |
| Find out where documents get stuck | **Where touchless is lost first** | "Most documents stop at Field Validation" |
| Decide which supplier to fix first | **Supplier opportunities** | "Supplier A would give us +4.0 percentage points" |
| Understand one supplier | **Supplier Diagnosis** page | "Their invoices have no PO number, so PO matching fails" |
| Understand one document | **Document Trace** | "This invoice stopped at stage 8, Field Validation" |
| Compare suppliers | **Compare suppliers** | "Supplier A and B use the same template, but only B fails" |
| Change a setting that helps | **Change proposals** | "Switch on automatic PO match: preview, apply, measure, undo" |

## Who can see it

* The tab is part of the Analytics Dashboard. Your administrator enables it for the organisation. If the tab is missing, ask your administrator.
* **Organisation administrators** always see it.
* Other users see it when an administrator granted their role the **Analytics dashboard** tab (**Settings → Roles**). Without a grant, only administrators have access.
* Some actions are for administrators only: **AI analysis**, **applying and undoing a change**, **learned rule proposals** and the **Consulting report**.

If you are not allowed, the page shows *Action not allowed, please contact the administrator*.

## What "touchless" means

Every document ends in exactly **one** outcome:

| Outcome | Meaning | Counts in the rate |
| --- | --- | --- |
| **Pure touchless** | Processed from import to export with **no human involvement at all** | Yes, as a success |
| **AP touchless** | Ran automatically, and a person only gave the **business approval**. No correction was needed | Yes, as a success |
| **AP assisted** | A person had to **correct a field, restart the document** or otherwise step in | Yes, as a miss. It is not a failure, only automation that did not fully carry the document |
| **Process exception** | Ended in an **error**, was **rejected**, was **refused by the ERP**, or **stalled** in the pipeline | Yes, as a miss |
| **In progress** | Not finished yet | **No**. It has no outcome yet |
| **Not eligible** | Deleted, archived, a test document, or an excluded document type | **No** |

The **touchless rate** is:

```
rate = (Pure touchless + AP touchless)
       ÷ (Pure touchless + AP touchless + AP assisted + Process exception)
```

Documents that are still **in progress** or **not eligible** are never in the calculation. This protects the rate: a document that arrived five minutes ago cannot pull it down.

{% hint style="info" %}
**One touch counts for good.** Once a person has touched a document, it stays counted as touched, even if a later automatic run would have needed nobody. **Restarting a document does not make it touchless again.** The rate reflects the work that happened.
{% endhint %}

### Example calculation (illustrative numbers)

In 30 days, 200 documents arrived:

| Outcome | Documents |
| --- | --- |
| Pure touchless | 120 |
| AP touchless | 30 |
| AP assisted | 30 |
| Process exception | 10 |
| In progress | 8 |
| Not eligible (test documents) | 2 |

* Denominator: 120 + 30 + 30 + 10 = **190**. The 8 in-progress and 2 not-eligible documents are left out.
* **Pure touchless**: 120 ÷ 190 = **63.2 %**
* **AP touchless**: 30 ÷ 190 = **15.8 %**
* **Touchless rate**: (120 + 30) ÷ 190 = **78.9 %**

The tab shows a **target** (70 % unless your organisation uses a different one). In this example the rate is above the target.

Click **How touchless is calculated** at the top right to open this explanation inside DocBits, with the numbers of your own period (documents in period, still in progress, excluded, measured).

### How current are the numbers

Outcomes are **recalculated every 15 minutes**. A document's outcome can still change after it first appears: the ERP may confirm an export hours later. The line **Data as of …** at the bottom of the tab shows when the numbers were last computed.

## The overview tab

### Filters

| Filter | What it does |
| --- | --- |
| **7D / 30D / 90D** | The period for the key figures and the queue. The default is 30 days |
| **Document Type** | Restricts every number to one type, for example INVOICE |
| **Segment field / Segment value** | Only if your organisation runs several processes through one document type (for example direct, indirect and EAM orders in the field `order_type`). Pick a field to see the breakdown, pick a value to narrow everything to it |
| **Document ID** | Opens the **Document Trace** for one document |

The **sub-organisation** you selected at the top of DocBits narrows the key figures and the supplier queue. Issue clusters and the AI analysis always cover the whole organisation.

### The five key figures

| Card | Shows | Example (illustrative) |
| --- | --- | --- |
| **Pure touchless** | The percentage and the difference to the target | **63.2 %** · "120 documents" · "−6.8 pp vs 70 % target" (red, below target) |
| **AP touchless** | The percentage | **15.8 %** · "30 documents" |
| **AP assisted** | The number of documents and their share | **30** · 15.8 % |
| **Process exceptions** | The number of documents and their share | **10** · 5.3 % |
| **Diagnosis coverage** | How many blocked documents have a **known** cause | **80 %** · "10 without a known cause" |

* A card shows a dash (—) instead of **0 %** when there is nothing to measure. A dash means "no data", not "zero".
* **Diagnosis coverage** = documents with a known blocking reason ÷ all blocked documents. Example: 50 blocked documents, 10 with an unknown cause → 40 ÷ 50 = **80 %**. A low value means "we do not yet understand why documents stop". Improve it before you try to fix individual causes.
* **Click a card** to open the document list behind the number in a new tab ("View the documents behind this number"). Cards with 0 documents are not clickable.

### Touchless rate over time

A chart with one line for **Pure touchless**, one for **AP touchless** and the **target line**. Short periods show daily points, long periods weekly points.

**Example.** After you switched on automatic PO matching on 1 October, the pure rate climbs from 55 % to 68 % within two weeks. The chart shows the day the curve turns, so you can match it to your change.

### Where touchless is lost first

A bar chart of **Blocked documents** per pipeline stage: the **first** stage that stopped a document.

**Example.** Bars: Supplier Identification 12, Field Validation 41, PO Line Match 7. The biggest bar tells you to look at **Field Validation** first, usually because a required field is not extracted.

### Supplier opportunities

The queue answers **"Which supplier should we fix first?"** It is sorted by **Recoverable** documents, highest first, 25 rows per page.

| Column | Meaning |
| --- | --- |
| **Supplier Number / Supplier** | The supplier. Documents without a recognised supplier appear as **No supplier identified (n documents)** |
| **Volume** | Eligible documents of the supplier in the period |
| **Pure Rate** | Share of pure touchless documents. Green if at or above the target, red if below |
| **Lost Documents** | Documents that ended as AP assisted or as a process exception. Not always a person: an ERP rejection or a document that stalled for seven days counts too |
| **Root Cause** | Who owns the fix: Configuration, ERP integration, Export, Extraction, Master data, Measurement, PO matching, User process, Validation or Unknown |
| **Recoverable** | Lost documents whose cause DocBits can fix: configuration, master data or supplier template |
| **Expected Lift** | How many **percentage points** your organisation's rate would gain if every recoverable document of this supplier ran touchless (**+x pp**) |
| **Confidence** | **High**, **Medium** or **Low**: how sure the diagnosis is |
| **Status** | New, Open, Investigating, In progress, Confirmed, Resolved, Dismissed. A supplier with too few documents shows **NEEDS_DIAGNOSIS** |

**Example.** Your organisation has 1,000 eligible documents in the period. Supplier A has 40 recoverable documents, Supplier B has 90 lost documents but only 10 recoverable (their problem is on their side).

* Supplier A: 40 ÷ 1,000 = **+4.0 pp expected lift**
* Supplier B: 10 ÷ 1,000 = **+1.0 pp**, although B has more lost documents

The queue ranks A above B because **expected lift** is measured against your whole organisation, not against the supplier. A supplier with four bad documents cannot outrank one with four hundred.

Use the search box ("Search supplier number or name") to find a supplier. Click a row to open the **Supplier Diagnosis**.

### Compare suppliers

Click **Compare suppliers**, tick **two to five** suppliers (each is listed with its number of blocked documents) and click **Compare**.

The comparison shows the suppliers side by side: **Pure rate**, **Lost documents**, **Recoverable**, **Root cause**, **Expected lift**, a bar chart of the outcomes, and a link to each **Supplier Diagnosis**.

**Example.** Supplier A and B send the same invoice layout. B has a pure rate of 80 %, A only 35 %. Both have the root cause "Master data". The comparison shows that the layout is fine and that A's supplier record is incomplete. Fix A's master data instead of changing the template.

### Analyse with AI

The button **Analyse n clusters with AI** analyses the issue clusters with the highest touchless potential (at least a minimum number of documents each). It takes about 13 seconds per cluster and covers the **whole organisation**. Only administrators can start it.

While it runs you see **Queued**, **Running**, **Done**, **Already analysed** or **Error** for each cluster, with a link **Open cluster**. If AI is switched off or not configured in the environment, the button is disabled with the reason, and **everything else on the page keeps working**.

## Supplier Diagnosis

Click a supplier in the queue to open its diagnosis page.

The page shows:

* **Six outcome tiles** (Pure touchless, AP touchless, AP assisted, Process exception, In progress, Not eligible), each linked to the documents.
* **The trend** with its own period selector: 30 days, 90 days, 6 months, 1 year or a custom range (up to two years). This changes the chart only.
* **Issue clusters** (see below).
* **Change history**: the changes you applied for this supplier and what they did.
* **Recent examples**: sample documents, in two tabs: **Needed attention** and **Went touchless**.
* **Diagnose supplier with AI**: analyses all clusters of the supplier (administrators).

A short note explains an empty page, for example: *5 documents from this supplier are still being processed and have no analysis result yet.* or *All 40 completed documents from this supplier ran touchless: there is nothing to diagnose.*

### Issue clusters

A **cluster** groups the documents of one supplier that stopped for the **same first reason**. Instead of 40 single problems you see "3 problems".

**Example cluster (illustrative).**

* **Headline**: *Required field missing* at stage *Field Validation*
* **Affected**: 28 documents. **Recoverable**: 28 documents. **Expected lift**: +2.8 pp
* **Suspected cause**: the supplier prints the PO number below the table, where the extraction does not look
* **What to change**: *Master data change*: add the layout of this supplier. **Open** takes you to the right settings page
* **Owner**: Consultant. **Confidence**: Medium. **Source**: Hypothesis

What a cluster card shows:

| Part | Meaning |
| --- | --- |
| **First blocker** and **stage** | The reason and the pipeline stage where the documents stop. There are more than 30 reasons, for example *Supplier not identified*, *Purchase order not found*, *Unit price outside PO tolerance*, *Rejected by the ERP*, *E-invoice validation failed* |
| **Affected / Recoverable / Expected lift** | How many documents, how many can be won back, how many percentage points it would give |
| **Suspected cause / Confirmed cause** | What DocBits thinks (or a person confirmed) is the reason |
| **Evidence** and **Missing evidence** | What the finding is based on, and what DocBits could **not** establish. Read **Missing evidence** before you trust the rest |
| **What to change** | Concrete steps with **Open** links to the settings. A chip tells the type: *Configuration change*, *Master data change*, *Supplier template change*, *Process change*, *Supplier action needed*, *Not fixable* |
| **Owner** | DocBits, Customer, Consultant, Supplier or Unassigned |
| **Sample documents** | Real documents of the cluster to look at |

**Fixable in DocBits** and **Supplier action only** are shown in two groups. For *Supplier action only* nothing in DocBits changes the result: the supplier has to correct the document and send it again.

### Where does a recommendation come from

Every cause shows its **source**, so you can tell a derived finding from a guess:

| Source | Meaning |
| --- | --- |
| **Deterministic** / **Rule-based** | A rule derived it from the recorded pipeline evidence. No language model was involved |
| **Hypothesis** | A language model proposed it from the cluster evidence. Treat it as a lead and check it before you act |
| **Confirmed** | A person reviewed the evidence and confirmed the cause |

AI texts are written in your organisation's language. If a cluster was analysed in another language, use **Analyse in this language**.

### PO matching decision flow

For clusters about **PO matching**, the card shows how DocBits tries to match an invoice line to a purchase order line, as a diagram:

1. **Single match validation**: apply the rules in order of priority
2. **Multi match validation**: after a single match, when several lines are involved
3. **Total match validation**: only when nothing matched at all (PO line total against the sum of the table lines)
4. **Single mismatch validation**: the unit price is ignored
5. **Fallback logic**: one PO line and one table line are left, so they are paired

Inside the stages DocBits tries **Exact match for all rules**, then **Tolerance-based match**, then **Package criteria**. Each step asks *Match found?* **Yes** leads to **Match found**, **No match** moves on to the next step and, at the end, to **No match found**. The header lists the **rule set version**, who owns it and the **tolerances** (**Unit price tolerance**, **Quantity tolerance**).

**Example.** An invoice line has a unit price of 10.40, the PO line says 10.00, the price tolerance is 5 %. The exact match fails, the tolerance match succeeds (4 % difference), the line is matched. With a tolerance of 3 % it fails, and the document stops with *Unit price outside PO tolerance*. The diagram shows exactly this path.

## Change proposals: preview, apply, measure, undo

A recommendation can come with a **change proposal**, a single setting change that should help. Administrators work with it in four steps:

1. **Preview**: shows the change (current → proposed value) and what DocBits expects. Nothing is saved. **Apply** is only possible after you looked at a preview.
2. **Apply**: saves exactly the previewed change. It is logged.
3. **Measure**: DocBits compares the touchless rate of the same document type **before and after**, over equally long periods. At least **20 documents** are needed in each period, otherwise it says *not measurable*.
4. **Undo**: takes the change back.

{% hint style="warning" %}
A before/after difference is an **observation**, not proof of cause. Other things can change at the same time (a new supplier, a seasonal peak).
{% endhint %}

**Example.** You apply *Switch on automatic PO match and export* for invoices. Two weeks later the **Change history** says: pure rate before 52 % (210 documents), after 61 % (198 documents). That is +9 pp, enough documents to be measurable.

## Document Trace

Enter a document ID in **Document ID**, or open a sample document from a cluster, to see **what happened to this one document**.

<figure><img src="../.gitbook/assets/touchless-document-trace.png" alt="The Document Trace page with the 14-stage pipeline path and the stopped stage Field Validation"><figcaption><p>The Document Trace: the pipeline path with the stage where the document stopped, what that stage had in its hands, and the run history below.</p></figcaption></figure>

The top shows the **pipeline path** with 14 stages: Intake, Classification, E-Document Validation, Supplier Identification, Text Recognition, Header Extraction, Table Extraction, Field Validation, PO Lookup, PO Line Match, Approval, Workflow Routing, Export, ERP Acknowledgement. Each box has a state:

| State | Meaning |
| --- | --- |
| **passed** (green) | The stage ran fine |
| **stopped here** (red) | The stage blocked the document |
| **skipped or not applicable** | The stage does not apply to this document |
| **not reached** | The document never got this far |
| **unknown** (dashed) | Nothing was recorded for this stage |

Below the path, a sentence names the cause. In the screenshot: *This document stopped at stage 8 "Field Validation", because a required field was not extracted.* The block **What this stage had in its hands** lists the facts: **Invalid field count 5** and the fields (`delivery_date`, `email`, `invoice_sub_type`, `payment_terms`, `supplier_id`), the rule (**REQUIRED**) and the validation codes. The block **Analysis** says whether it is **Rule-based** or AI-written.

The **run history** below lists every run (**Run 1 · Initial run**, then each restart) with every stage and its recorded facts. If the document was corrected and restarted, a note reminds you that it **stays counted as touched**.

**Example.** The documents of one supplier all stop at stage 8. In the trace you see the same five invalid fields every time. That is not an extraction problem of single documents, it is a missing default in your field configuration: fix it once and the whole cluster is recoverable.

## Learned rule proposals and improvement requests

Administrators also see two sections between the key figures and the charts:

* **Improvement requests**: suggestions that users sent from the validation assistant, in two tabs **Open** and **History**.
* **Learned rule proposals**: rules DocBits learned from your team's corrections, for example "for supplier X, replace the value in field Y". Before you create one, check the documents where it would replace a value your team had accepted. The section **After activation** shows the manual corrections of the target field before and after a rule went live.

## Consulting report

Administrators find the **Consulting report** at the bottom of the tab. Click **Create report** to load it. It combines, for your organisation:

* the **changes with the biggest effect**, ranked, each with the domain, the problem, the recommended action, the number of documents and the **estimated** effect per month,
* **the domain of every problem** (extraction, master data, PO matching, auto accounting, settings, process),
* **table configuration checks**, for example *structured table output not used* or *table column type mismatch* per document type and column.

The effect values are **estimates**. If the report answers *forbidden*, your role does not allow it.

## Work with Touchless Intelligence: a routine

1. **Weekly**: open the tab and check the **rate** and the **trend** against the target.
2. Look at **Diagnosis coverage**. Below about 80 %, first find out why documents stop.
3. Read **Where touchless is lost first** and pick the biggest stage.
4. Open **Supplier opportunities**. Sort by **Expected lift** and take the top supplier with the status **RECOVERABLE**.
5. Read the **issue clusters**, check **Missing evidence**, then follow **What to change**.
6. Apply one change at a time with a **preview**, so the **Change history** can measure it.
7. After two weeks check the **before/after** result.

## Ask in plain language: DocBits MCP

All of this is also available to your AI assistant through the [DocBits MCP](../advanced-functions-and-tools/docbits-mcp/README.md). Examples you can ask:

* "What is our touchless rate for the last 30 days?"
* "Which three suppliers cost us the most touchless documents?"
* "Why do documents of this supplier stop for a human?"
* "Why did the PO match fail for this document?"

## FAQ

**The rates show a dash (—).**
No document has reached a final outcome in the period, or fewer documents than the minimum were measured. Documents that are still in progress are not counted.

**The tab is missing.**
Ask your administrator to enable the module and to grant your role the **Analytics dashboard** tab.

**A document is counted as touched, but it ran through without anyone this time.**
It was touched in an earlier run (a correction or a restart). The rate counts the work that happened.

**Why does the number change after a few hours?**
The ERP may confirm an export hours after it was sent. The outcome is recalculated every 15 minutes.

**Does the AI change anything on its own?**
No. AI writes explanations only. A setting changes only after an administrator previews and applies it.

## Related pages

* [Analytics Dashboard](analytics-dashboard.md)
* [Settings Assistant](settings/global-settings/company-information/settings-assistant.md)
* [DocBits MCP](../advanced-functions-and-tools/docbits-mcp/README.md)

<!-- Source notes (not shown): facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.
Screenshots still to add, from an organisation WITH evaluated documents (no empty-state shots): overview with key figures, trend and bottleneck chart, supplier queue, supplier diagnosis with issue clusters, compare dialog, methodology drawer. The document trace screenshot below is real data. -->
