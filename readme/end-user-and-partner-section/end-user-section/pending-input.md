# Pending Input

**Pending Input** pauses a document while you wait for an answer from a colleague. Instead of leaving a comment nobody notices, you ask the question in the document's Activity Stream and tag the people who should answer. The document leaves the active queue until they reply, and the people you tagged can open it read-only through a link in their e-mail.

The status appears on the [dashboard](dashboard/README.md) as **Pending Input**, and you can filter the worklist by it.

## Ask for input

1. Open the document and open the **Activity Stream** (the chat icon in the toolbar of the document screen).
2. Write your question and type **@** followed by the name of the person you want to ask. Pick the person from the list that appears. Tagging is what grants access: somebody who is not tagged cannot open the document.
3. Once a person is tagged, a box appears under the editor with two choices:

* **Comment only** – the question is posted in the Activity Stream, the status stays as it is. Use this when you only need an answer and do not want to hold the document.
* **Send & set to Pending Input** – the question is posted and the document is set to waiting. It leaves the active queue and stays paused until the tagged person answers.

The tagged people receive an e-mail with a link to the document. **Enter** or the send icon still posts an ordinary comment without granting access; **Shift+Enter** starts a new line. On a document that is already paused, or on one that cannot be paused yet, the box offers the ask without the pause option.

## Answer a request

You are asked for input when a colleague tags you in the Activity Stream.

* Open the link in the e-mail. The **Pending Input** page shows the pages of the document on the left and the Activity Stream on the right, with a **Pending Input** badge.
* Your access is read-only: you can read the document and reply in the Activity Stream, but you cannot change fields or export.
* Write your answer in the Activity Stream and send it. The questioner is notified, and the conversation stays in the document's history.
* The header of the page shows how long your access lasts, for example **Read-only access until 09.11.2026**. Access also ends as soon as the document moves on.

If you open the link after the request was answered or after your access ended, the page tells you that the request has been resolved or has expired and that no action is needed.

## Resolve the request

The document stays paused until the assignee picks up the answer.

1. Open the document from the dashboard. A paused document opens directly on its **Pending Input** page.
2. Read the answer in the Activity Stream.
3. Select **Resolve & Proceed**. The document resumes in the status that follows in its workflow, so you land on the screen where you continue working.

Only the assignee of the document, or a member of the group it is assigned to, can resolve it. Administrators and approvers can open a paused document read-only to see why it is waiting.

## Set the access period

The feature is available in every organisation. What you can configure is how long a person you asked for input keeps access to the document:

1. Open **Settings → Dashboard**.
2. Expand **Action**.
3. In **Pending Input access (days)** enter a whole number of days. The default is **14**, and at least one day is required.
4. Save your changes.

The period starts when the request is sent. It ends earlier when the document is resolved or moves to another status.

<figure><img src="../../.gitbook/assets/pending-input-access-setting.png" alt="The Action section of the Dashboard settings with the Pending Input access field set to 14 days"><figcaption><p>Pending Input access (days) in the Action section of the Dashboard settings.</p></figcaption></figure>
