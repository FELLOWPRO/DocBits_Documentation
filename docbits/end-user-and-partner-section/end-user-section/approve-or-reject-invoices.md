# Approve or reject an invoice

## What follows a business approval decision

<figure><img src="../../.gitbook/assets/process-approval-en-20261028.png" alt="Approve or reject invoice: Distinguish between examination, decision and subsequent handover."><figcaption><p>Distinguish between examination, decision and subsequent handover. The diagram is schematic; the active settings of your organization determine the actual behavior.</p></figcaption></figure>

Technical validation checks document data; approval records the business decision of an authorized reviewer. Even a technically valid invoice may still require one or more approvals.

1. **Check responsibility:** Open the assigned invoice and check which approval level you are allowed to decide on.
2. **Review the invoice:** Compare header values, line items and tax with the original document and your company requirements.
3. **Document decision:** Approve a correct invoice or reject it with a specific reason. Wait for the response and then check the approval history.
4. **Identify the next step:** If additional approval stages are configured, the invoice awaits their decisions. After rejection, clarification, correction and any resubmission follow your configured process. The separate export process determines whether data has reached the target system.

### Three statements that don't mean the same thing

| statement | What it does not automatically prove |
| --- | --- |
| **The data is validated.** | That an authorized business reviewer has approved it. |
| **A reviewer approved.** | That all required approval stages have been completed. |
| **Approvals have been completed.** | That the invoice has already been exported or posted in ERP. |

Use [Document tasks](tasks.md) to process assigned work and [Document status](dashboard/document-status.md) to classify current status.

Follow an ordinary reviewer checking an invoice, recording a decision and verifying the saved result.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/invoice-approval-customer/v1/en.mp4" %}
Approve or reject an invoice
{% endembed %}

[Watch with subtitles](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/invoice-approval-customer/v1/en.html)

The recording shows the real application. Option wording may vary with the deployed version.

Use approval to record your business decision on an invoice that has already been validated. You need access to the document and permission for its current approval stage. The video uses an ordinary reviewer account.

## Review and decide

1. Open the invoice assigned to you and check the current approval stage.
2. Compare the invoice number, supplier, dates and total with the original. Review the line items and tax as well. Technical validation does not replace your business review.
3. Record a clear review note. Approve a correct invoice, or reject it with a specific reason when it needs clarification. Wait for the operation to complete.
4. Reopen the document and inspect its approval history. Check the reviewer, time, decision and full note against what you intended.

<figure><img src="../../.gitbook/assets/customer-check-en-a48081418929.png" alt="Populated invoice values compared with the original before approval."><figcaption><p>Populated invoice values compared with the original before approval.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/customer-rejected-en-a48081418929.png" alt="Saved rejection and its recorded reason after reopening the invoice."><figcaption><p>Saved rejection and its recorded reason after reopening the invoice.</p></figcaption></figure>

## Check the next stage

When a second approval is configured, your first approval leaves the invoice waiting for another authorized reviewer. It is not yet fully approved. A rejection needs business clarification; correction and resubmission follow your configured process.

An approval-history entry does not prove that data reached an ERP system. In this isolated example, the retrieval channel has no external ERP target. The technical status `pending_data_fetch`, when displayed, means that the document is waiting for data retrieval.

## Related pages

- [Validation screen](validation-screen/README.md)
- [Document tasks](tasks.md)
