# Supplier Diagnosis and Issue Clusters

<!-- touchless-admin-video-v2-20261104:start -->
**Video chapter (review version):** [Investigate recurring issues](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/en.html#chapter=06).
<!-- touchless-admin-video-v2-20261104:end -->

Click a supplier in the queue to open its diagnosis page.

<figure><img src="../../../.gitbook/assets/touchless-supplier-detail.png" alt="The Supplier Diagnosis page with outcome tiles, trend and two issue clusters"><figcaption><p>The Supplier Diagnosis page: outcome tiles, trend with period selector and two issue clusters ordered by expected lift. Example organisation with demo data; supplier names are fictional.</p></figcaption></figure>

The page shows:

The outcome tiles and chart segments count separate document outcomes. Here AP touchless means approval-only documents; the combined AP headline rate on the overview also includes pure documents.

* **Four final-outcome tiles** (Pure touchless, AP touchless, AP assisted, Process exception), each linked to the documents.
* **The trend** with its own period selector: 30 days, 90 days, 6 months, 1 year or a custom range (up to two years). This changes the chart only.
* **Issue clusters** (see below).
* **Change history**: the changes you applied for this supplier and what they did.
* **Recent examples**: sample documents, in two tabs: **Needed attention** and **Went touchless**.
* **Diagnose supplier with AI**: analyses all clusters of the supplier (administrators).

A short note explains an empty page, for example: _5 documents from this supplier are still being processed and have no analysis result yet._ or _All 40 completed documents from this supplier ran touchless: there is nothing to diagnose._

### Issue clusters

A **cluster** groups the documents of one supplier that stopped for the **same first reason**. Instead of 40 single problems you see "3 problems".

<figure><img src="../../../.gitbook/assets/touchless-issue-cluster.png" alt="An opened issue cluster card with first blocker, what to change and the change proposal"><figcaption><p>An opened cluster card: the first blocker, <strong>What to change</strong>, and a <strong>Change proposal</strong> with risk, scope and open questions. Here the cluster covers 58 documents and is worth +18.7 pp. Example organisation with demo data; supplier names are fictional.</p></figcaption></figure>

**Example cluster (illustrative).**

* **Headline**: _Required field missing_ at stage _Field Validation_
* **Affected**: 28 documents. **Recoverable**: 28 documents. **Expected lift**: +2.8 pp
* **Suspected cause**: the supplier prints the PO number below the table, where the extraction does not look
* **What to check next**: compare the printed PO number with the extracted value and inspect this supplier's extraction configuration before proposing a change
* **Owner**: Consultant. **Confidence**: Medium. **Source**: Hypothesis

What a cluster card shows:

| Part                                       | Meaning                                                                                                                                                                                                                                                |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **First blocker** and **stage**            | The reason and the pipeline stage where the documents stop. There are more than 30 reasons, for example _Supplier not identified_, _Purchase order not found_, _Unit price outside PO tolerance_, _Rejected by the ERP_, _E-invoice validation failed_ |
| **Affected / Recoverable / Expected lift** | How many documents, how many can be won back, how many percentage points it would give                                                                                                                                                                 |
| **Suspected cause / Confirmed cause**      | What DocBits thinks (or a person confirmed) is the reason                                                                                                                                                                                              |
| **Evidence** and **Missing evidence**      | What the finding is based on, and what DocBits could **not** establish. Read **Missing evidence** before you trust the rest                                                                                                                            |
| **What to change**                         | Concrete steps with **Open** links to the settings. A chip tells the type: _Configuration change_, _Master data change_, _Supplier template change_, _Process change_, _Supplier action needed_, _Not fixable_                                         |
| **Owner**                                  | DocBits, Customer, Consultant, Supplier or Unassigned. The chip names the owner of the change proposal; only when the proposals of the card disagree does it fall back to the owner of the whole cluster                                                                                  |
| **Sample documents**                       | Real documents of the cluster to look at                                                                                                                                                                                                               |

**Fixable in DocBits** and **Supplier action only** are shown in two groups. For _Supplier action only_ nothing in DocBits changes the result: the supplier has to correct the document and send it again.

### Where does a recommendation come from

Every cause shows its **source**, so you can tell a derived finding from a guess:

| Source                             | Meaning                                                                                                |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Deterministic** / **Rule-based** | A rule derived it from the recorded pipeline evidence. No language model was involved                  |
| **Hypothesis**                     | A language model proposed it from the cluster evidence. Treat it as a lead and check it before you act |
| **Confirmed**                      | A person reviewed the evidence and confirmed the cause                                                 |

AI texts are written in your organisation's language. If a cluster was analysed in another language, use **Analyse in this language**.

## Who needs to fix a source-data discrepancy?

Do not equate **AP assisted** with an extraction failure. For each sample document, separate the processing outcome from the confirmed cause:

| Evidence | Investigate or fix |
| --- | --- |
| The invoice contains a value that DocBits extracted differently | Extraction configuration or supplier template |
| Extraction matches the invoice, but the Infor order has a confirmed incorrect price, quantity or unit | Source-system data; AP coordinates with purchasing or the master-data owner |
| Infor is correct, but DocBits has an old or incomplete copy | Import or ERP integration |
| Invoice and source values differ, but the agreed value is not established | Business clarification; keep the root cause unconfirmed |

A small AP intervention can finish the invoice while leaving a recurring source-data issue unresolved. Record both the immediate action and the lasting fix. The cluster alone does not prove the historical contents of Infor. See the [worked Infor example](touchless-po-matching-diagnosis.md#worked-example-correct-extraction-different-infor-data).

## PO matching clusters

If the first blocker of a cluster is a PO matching reason (for example _PO item mismatch_ or _Purchase order not found_), the cluster card shows how DocBits tries to match the invoice to the purchase order. See [PO Matching Diagnosis](touchless-po-matching-diagnosis.md).

See [Touchless with MCP](touchless-mcp.md) for the matching tool calls and classification of human actions.

## Related pages

* [Touchless Intelligence](./)
* [PO Matching Diagnosis](touchless-po-matching-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Change Proposals and Reports](touchless-change-proposals.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->

<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
