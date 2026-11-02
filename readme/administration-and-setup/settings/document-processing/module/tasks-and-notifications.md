# Tasks & Notifications

### Overview

The **Tasks & Notifications** setting turns on DocBits’ built-in task management. When it is enabled, team members can create tasks, assign documents to each other (for example for validation, correction or approval) and receive notifications about them. It also unlocks the **Dashboard Tasks Count** option described below.

This setting is **disabled by default**.

### What Does It Do?

* **Enabled** — The Tasks & Notifications features become available across DocBits. Users can assign tasks, track their status and get notified when something needs their attention.
* **Disabled** — Task assignment and the related notifications are turned off. (Turning this off also automatically turns off **Dashboard Tasks Count**.)

### Dashboard Tasks Count

**Dashboard Tasks Count** is an additional option that appears only when **Tasks & Notifications** is enabled. It controls whether a **task counter** is shown on the Dashboard.

* **Enabled** — The Dashboard shows how many documents are waiting (for example in your queue and ready for validation), so the team sees at a glance how much work is open.
* **Disabled** — The counter is hidden. Tasks still work normally; only the number on the Dashboard is not displayed.

{% hint style="info" %}
**Dashboard Tasks Count** depends on **Tasks & Notifications**. If you switch Tasks & Notifications off, the task counter is switched off as well.
{% endhint %}

### Non-admin task completion

**Non-admin task completion** decides which users who are not organisation admins may close a task, that is, set it to **Done** or **Rejected**. It appears only when **Tasks & Notifications** is enabled. Organisation admins can always close tasks, whatever is selected here.

| Option | Who can close a task |
| --- | --- |
| **Default behaviour** | The setting adds no restriction. Tasks can be closed exactly as before the setting existed. This is what an organisation gets when the option was never changed. |
| **Admins and assigned users** | Admins, and the users the task is assigned to, either directly or through one of their groups. A task that is assigned to someone else, or to nobody, cannot be closed by other users. |
| **Admins only** | Only organisation admins. |

With **Admins and assigned users** or **Admins only**, a user who may not close a task:

* does not see the green **Done** button on the task page, and the status list there offers only **Open** and **In progress**;
* cannot click the status circle of the task in the document's task panel; hovering over it shows "You are not allowed to mark this task as done or rejected.";
* does not see **Mark as done** for that task in the task list, and bulk **Mark as done** is hidden as long as such a task is selected;
* cannot drag the task into the **Done** or **Rejected** column of the task board. The card returns to its column and the same message is shown.

These users can still edit the title, the description and the other fields of the task and save them. They can also move the task between **Open** and **In progress**, and reopen a task that is already done. The setting restricts closing only.

#### Tasks on documents sent back to validation

Because users cannot clear their own tasks under **Admins and assigned users** or **Admins only**, DocBits clears the open tasks of a document itself when a document waiting for approval is sent back to validation:

* **Restart workflow** on the approval screen: every open task of the document is rejected.
* **Reject And Correct**: every open task of the document is rejected.
* **Approve And Correct**: the approver's own tasks are completed in the same way **Approve** completes them (only for document types with **Approval History** enabled), and every remaining open task is rejected.

The open tasks are cleared before the document returns to validation. Workflows that run on the status change can then create new tasks for anything that still needs attention.

With **Default behaviour**, open tasks stay open when a document is sent back, as before.

{% hint style="info" %}
**Non-admin task completion** works next to **Non-admin task deletion**. The completion setting does not change who may delete a task. To stop non-admins from both closing and deleting tasks, set both settings.
{% endhint %}

### Benefits

* **Clear responsibilities**: Documents can be assigned to the right person instead of relying on email.
* **Nothing gets forgotten**: Notifications remind users about documents that need their action.
* **At-a-glance workload**: With Dashboard Tasks Count, the team immediately sees how many documents are still open.

### How to Use

1. Go to **Settings**.
2. Select **Document Processing**.
3. Select **Module**.
4. Open the **Document Type** section.
5. Switch **Tasks & Notifications** on.
6. (Optional) Once it is on, the **Dashboard Tasks Count** toggle appears below it — switch it on to show the task counter on the Dashboard.
7. (Optional) Choose who may close tasks in **Non-admin task completion**.

### When to Use This Feature

* **Teams that share document work**: Enable it when several people validate or approve documents and need to hand work to each other.
* **Workload visibility**: Also enable Dashboard Tasks Count when supervisors want to see open work directly on the Dashboard.
* **Tasks that only admins or an automated process should close**: Set **Non-admin task completion** to **Admins only** or **Admins and assigned users** when users must not mark tasks as done that were not actually done.
* **Single-user or fully automated setups**: You can leave it off if no one needs to assign documents or track tasks.
