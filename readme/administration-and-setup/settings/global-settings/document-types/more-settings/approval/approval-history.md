# Approval History

Approval History helps users inspect decisions in a document's approval workflow. The previous version of this page linked an old **General Settings** path and showed three images from an older interface without explaining the controls. Use the current document-type settings to enable the option, then verify the result with a synthetic approval in your own organisation.

## Enable the option for a document type

1. With an administrator account, open **Settings → Document Types**. Find the document type, such as **Invoice**, and select its **gear icon** to open **More Settings**. The **Layouts** and **Fields** links on the card lead to different editors.

   <figure><img src="../../../../../../.gitbook/assets/dbdc222-document-types-en.png" alt="English DocBits Document Types page with an Invoice card and gear icon for More Settings"><figcaption><p>Open More Settings on the document type whose approval workflow you want to inspect.</p></figcaption></figure>

2. Expand **Approval & Rejection** and locate **Approval History**. This switch is separate from **Approve before export**, **Second Approval** and **Approval Stamp**. The English Sandbox screenshot shows the synthetic **DocBits Documentation Test A** organisation with all four switches **off**. No setting was changed for this guide.

   <figure><img src="../../../../../../.gitbook/assets/dbdc222-approval-history-en.png" alt="English Invoice More Settings page with Approval and Rejection expanded and Approval History switched off"><figcaption><p>Check the Approval History switch for the selected document type.</p></figcaption></figure>

3. Enable Approval History only after confirming the intended approval workflow and who may see its decisions. Record the previous setting so a test can be compared with it.

## Verify with a test document

Use a synthetic document of the configured type that actually enters the approval workflow. Have an authorised test user approve or reject it, then open that document's approval view and inspect the available history. Confirm the decision, user, time and any entered comment against the action you performed. For a workflow with more than one approver, check the sequence after each decision. If no history is visible, check the document type, workflow state, switch and viewing permissions before treating it as a documentation or product error.

The old screenshots' colours and top-left navigation are not presented as current behaviour because no approved or rejected document was available in Test A. The two new images verify the current settings path and switch only; the history view still needs a synthetic document with approval activity.
