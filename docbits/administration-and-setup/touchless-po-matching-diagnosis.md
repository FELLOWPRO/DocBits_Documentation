# Touchless Intelligence: PO Matching Diagnosis

## Overview

Many invoices stop at the purchase order. The invoice says one thing, the purchase order (PO) says another, and DocBits cannot decide on its own whether they belong together. Every such document needs a person, so it is **not touchless**.

Touchless Intelligence shows you **why** a PO match failed and **how** DocBits tried to match. This page explains the two pipeline stages involved, the reasons you will see, and the **PO matching decision flow**, a diagram that shows the matching steps one after the other.

### Where you see PO matching in Touchless Intelligence

| Where | What you see |
| --- | --- |
| **Where touchless is lost first** (overview tab) | A bar such as *PO line match: PO item mismatch*. It tells you how many documents stopped there |
| **Supplier opportunities** | A supplier with the root cause **PO matching** |
| **Supplier Diagnosis**, section **How this organisation matches** and the **issue cluster** | The decision flow with the rule set of your organisation |
| **Document Trace** | The stage **PO Line Match** with the status **blocked** and the reason |
| **Settings → Document Types → More Settings → Purchase Order** | The matching rules themselves. See [Purchase Order Matching Rules](settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) |

## The two PO stages

| Stage | Question | Stops with |
| --- | --- | --- |
| **9 · PO Lookup** | Is there a purchase order for this invoice? | *Purchase order not found* |
| **10 · PO Line Match** | Does every invoice line match a PO line? | *PO item mismatch*, *PO line identifier mismatch*, *Unit price outside PO tolerance*, *Quantity outside PO tolerance* |

A document that stops at stage 9 or 10 shows up with the first blocker **PO matching** in the supplier queue.

## Reasons a PO match fails

| Reason you see | What it means | Typical cause | What to change |
| --- | --- | --- | --- |
| **Purchase order not found** | DocBits found no purchase order for the PO number on the invoice | The PO number is read wrongly or missing; the PO was not imported yet; the PO belongs to another supplier | Check the PO number extraction for this supplier, the PO master data import and the supplier link |
| **PO item mismatch** | The invoice lines did not match the PO lines | The supplier uses its own item numbers; the description differs; lines were merged or split | Check the item number mapping and the **rule priorities** in the matching rules; add a rule for the supplier's way of identifying lines |
| **PO line identifier mismatch** | The line number or identifier on the invoice does not match the PO | The supplier renumbers lines | Match by item and quantity instead of by line number |
| **Unit price outside PO tolerance** | The price differs more than the allowed tolerance | A real price change, a rounding difference or a different price unit | Check the **Unit price tolerance** in the rule set; correct the PO or ask the supplier |
| **Quantity outside PO tolerance** | The quantity differs more than the allowed tolerance | Partial delivery, over-delivery | Check **Match quantity on** and the **Quantity tolerance** |
| **PO matching service error** | The matching service could not answer | A temporary technical problem | Restart the documents; contact support if it repeats |
| **Automatic PO export disabled** | The setting **Auto export if PO matched 100%** is off, so matched documents are not exported automatically | The setting is off | Switch the setting on if you want automatic export. See [Auto Export if PO Matched 100%](settings/document-processing/module/auto-export-if-po-matched-100.md) |

{% hint style="info" %}
Not every PO matching reason can be fixed in DocBits. If the supplier sends a wrong PO number, the card says **Supplier action only**: the supplier has to correct the document and send it again.
{% endhint %}

## The PO matching decision flow

The decision flow shows how DocBits tries to match an invoice line to a PO line. It has **five stages**, and the first match wins:

1. **Single match validation**: apply the rules in order of priority. This is the normal case, one invoice line and one PO line
2. **Multi match validation**: after a single match, when several lines are involved on one side
3. **Total match validation**: only when nothing matched at all. The PO line total is compared with the sum of its table lines
4. **Single mismatch validation**: the unit price is ignored, so a line can be matched by item and quantity even if the price differs
5. **Fallback logic**: one PO line and one table line are left, so they are paired

Inside the stages DocBits tries, in this order:

* **Exact match for all rules**: every compared value is identical
* **Tolerance-based match**: numeric values may deviate within the tolerance
* **Package criteria**: the last pass, based on the package-related criteria of the rule set

Each step asks **Match found?** The answer **Yes** (green) leads to **Match found** and the document continues. The answer **No match** (red) moves on to the next step, and after the last step the result is **No match found**: the document stops and needs a person.

<figure><img src="../.gitbook/assets/touchless-po-matching-flow.png" alt="The PO matching decision flow: rule set header, five numbered matching stages with their passes and the end points Match found and No match found"><figcaption><p>The PO matching decision flow, opened from <strong>How this organisation matches</strong> on the Supplier Diagnosis page. The header shows the rule set (version 7, owned by this organisation) and the tolerances. Below it, the five stages with their passes run from top to bottom. Green leads to <strong>Match found</strong>, red moves on to the next step and ends in <strong>No match found</strong>. Example organisation with demo data.</p></figcaption></figure>

### What the header of the diagram tells you

| Field | Meaning |
| --- | --- |
| **Document type** | The document type the rule set belongs to, for example INVOICE |
| **Rule set version** | The version of the matching rules, for example v3 |
| **Rule set owner** | **This organisation** (your own rules) or **Shipped default rule set** (the standard rules of DocBits) |
| **Published** | When the version was published |
| **Match quantity on** | Which quantity is compared (ordered quantity, open quantity) |
| **Tolerance amount** | Whether the tolerances come from the document type attributes or from the rule set |
| **Unit price tolerance** / **Quantity tolerance** | How much a price or a quantity may deviate |
| **Default tolerance** | The tolerance for all other numeric values |

In the example above, the tolerances show **not configured** and **not in force: attribute decides**. That means: the rule set itself has no own tolerance, and the **Tolerance amount** line says the tolerances come from the **document type attributes**. A tolerance only decides when it is in force. Read this line first when a price or quantity difference blocks documents: it tells you **where** to change the tolerance.

The state of the rule set is shown as a note: **Active version** (these rules decide), **Approved, not active**, **Draft, not yet in force** or **Version state unknown**. Only the active version decides.

If transformation rules changed a document before matching, the diagram says so, for example *2 applied: (names)* or *"(rule)" rebuilt (table): the PO match was lost here*. That is a frequent hidden cause: a rule that reformats a table can break a match that worked before.

## Examples

The numbers in the examples are illustrative.

### Example 1: Price within tolerance

An invoice line has a unit price of **10.40**. The PO line says **10.00**. The unit price tolerance is **5 %**.

* **Exact match** fails (10.40 is not 10.00).
* **Tolerance-based match** succeeds: the difference is **4 %**, which is within 5 %.
* The line is matched. **Match found.**

With a tolerance of **3 %** the tolerance-based match fails too. After all stages the document stops with **Unit price outside PO tolerance**. The diagram shows exactly this path, and the fix is either the tolerance (if 4 % is acceptable for your business) or a correction at the supplier.

### Example 2: The supplier's item numbers differ from yours

A supplier invoices item **"A-4711-X"**, your PO says **"4711"**. No rule compares the two, so no match is found, and Touchless Intelligence groups all invoices of this supplier into one cluster: **PO line match, PO item mismatch**, 27 documents.

* In the cluster you read *27 affected, 27 recoverable*, expected lift for example **+8.7 pp**.
* The fix is on your side: add or reorder a rule that matches on the supplier item number or the description, or maintain the supplier item numbers in the master data.
* After you changed the rule, apply the change with a [change proposal](touchless-change-proposals.md) and read the **Change history** two weeks later: pure rate before and after.

### Example 3: The purchase order is not there yet

Invoices arrive before the PO was imported. They stop at **PO Lookup** with **Purchase order not found**. The cluster shows a short peak. The fix is the order of your processes, or the schedule of the PO import, not the matching rules. Check **Where touchless is lost first**: a bar *PO lookup: Purchase order not found* that grows after each import gap points to this cause.

### Example 4: One rule rebuilt the table

After a transformation rule for the table of a supplier went live, the matching rate of this supplier fell sharply. The diagram of an affected document says *"(rule)" rebuilt (table): the PO match was lost here*. The fix is to adjust or undo the transformation rule, not the matching rules.

## A routine for PO matching problems

1. Open **Where touchless is lost first**. Is a PO matching stage in the top three?
2. Open **Supplier opportunities** and sort by **Expected lift**. Take the supplier with the root cause **PO matching** and the status **RECOVERABLE**.
3. Open the **Supplier Diagnosis** and read the cluster: reason, affected documents, **What to change**, **Missing evidence**.
4. Open **How this organisation matches** and check the rule set: version, owner and tolerances.
5. Open one **sample document** and its [Document Trace](touchless-document-trace.md): which stage, which reason?
6. Change **one** thing (rule order, tolerance, item mapping) with a preview, so the **Change history** can measure it.

## Related pages

* [Touchless Intelligence](touchless-intelligence.md)
* [Supplier Diagnosis and Issue Clusters](touchless-supplier-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Change Proposals and Reports](touchless-change-proposals.md)
* [Purchase Order Matching Rules](settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md)
* [PO Matching Cards: Complete Guide](workflow/cards-overview/po-matching-complete-guide.md)
