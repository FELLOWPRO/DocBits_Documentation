# Tasks & Notifications

### Overview

The **Tasks & Notifications** setting turns on DocBits’ built-in task management. When it is enabled, team members can create tasks, assign documents to each other (for example for validation, correction or approval) and receive notifications about them.

This setting is **disabled by default**. When it is enabled, four more options appear below it:

* **Dashboard Tasks Count**: shows on the Dashboard which documents have open tasks.
* **Allow "All" filter for non-admins**: lets users who are not admins see every task.
* **Non-admin task deletion**: decides which tasks users who are not admins may delete.
* **Non-admin task completion**: decides which tasks users who are not admins may close.

Organisation admins are never restricted by these options.

### What Does It Do?

* **Enabled**: The Tasks & Notifications features become available across DocBits. Users can assign tasks, track their status and get notified when something needs their attention.
* **Disabled**: Task assignment and the related notifications are turned off. Turning this off also turns off **Dashboard Tasks Count**.

### Dashboard Tasks Count

**Dashboard Tasks Count** controls whether the Dashboard shows which documents have open tasks.

* **Enabled**: A document that has tasks in the status **Open** or **In progress** shows a task icon in the Dashboard list. Hovering over the icon shows how many open tasks the document has, for example "2 Open Task(s)". Tasks that are done, rejected or deleted are not counted.
* **Disabled**: The icon is hidden. Tasks still work normally.

{% hint style="info" %}
**Dashboard Tasks Count** depends on **Tasks & Notifications**. If you switch Tasks & Notifications off, the task count is switched off as well.
{% endhint %}

### Allow "All" filter for non-admins

The task overview has an **Assigned To** filter with the options **All** and **Assigned to me**. Admins always get both options.

* **Enabled**: Users who are not admins can also choose **All** and see every task of the organisation.
* **Disabled** (default): Users who are not admins get only **Assigned to me**, so the overview shows the tasks assigned to them.

### Non-admin task deletion

**Non-admin task deletion** decides which tasks and notifications users who are not admins may delete. Admins can always delete every task.

| Option | Users who are not admins may delete |
| --- | --- |
| **None** | No tasks. |
| **Created tasks only** | Tasks they created. |
| **Created and assigned tasks** | Tasks they created, and tasks assigned to them or to one of their groups. This applies when the option was never changed. |
| **All tasks** | Every task. |

Users can always delete the tasks they created, except with **None**. A task that is assigned to nobody can therefore be deleted only by the user who created it, by admins, or with **All tasks**. A task without a recorded creator, for example one created by the system, can be deleted only by the users it is assigned to (with **Created and assigned tasks**), by admins, or with **All tasks**.

{% hint style="warning" %}
Deleting a task removes it from the task list without a decision. If tasks must be closed only by a decision, set **Non-admin task deletion** to **None** together with **Non-admin task completion** (see below) to **Admins only**.
{% endhint %}

### Non-admin task completion

**Non-admin task completion** decides which users who are not admins may close a task, that is, set it to **Done** or **Rejected**. Admins can always close tasks, whatever is selected here.

| Option | Who can close a task |
| --- | --- |
| **Default behaviour** | The setting adds no restriction. Users can close the tasks that are assigned to them or to one of their groups, as before the setting existed. This applies when the option was never changed. |
| **Admins and assigned users** | Admins, and the users the task is assigned to, either directly or through one of their groups. A task that is assigned to someone else, or to nobody, cannot be closed by other users. DocBits also checks this when a task is changed through the API. |
| **Admins only** | Only admins. |

With **Admins and assigned users** or **Admins only**, a user who may not close a task:

* does not see the green **Done** button on the task page, and the status list there offers only **Open** and **In progress**;
* cannot click the status circle of the task in the document's task panel. Hovering over it shows "You are not allowed to mark this task as done or rejected.";
* does not see **Mark as done** for that task in the task list, and **Mark as done** for a selection is hidden as long as such a task is selected;
* cannot drag the task into the **Done** or **Rejected** column of the task board. The card returns to its column and the same message is shown.

The setting restricts closing only. Users keep every other right they had before: users a task is assigned to can still edit it, save it, move it between **Open** and **In progress**, and reopen it after it was done. Users a task is not assigned to could not change its status before, and still cannot.

For document types with **Approval History** enabled, **Approve** still completes open tasks of the document, whatever is selected here: the tasks assigned to the approver or to one of their groups, and the tasks assigned to nobody. If the approver is an admin, all open tasks of the document are completed.

#### Tasks on documents sent back to validation

Because users cannot clear their own tasks under **Admins and assigned users** or **Admins only**, DocBits clears the open tasks of a document itself when a document waiting for approval is sent back to validation:

* **Restart workflow** on the approval screen: every open task of the document is rejected.
* **Reject And Correct**: every open task of the document is rejected.
* **Approve And Correct**: the tasks that **Approve** would complete (see above) are completed, only for document types with **Approval History** enabled. Every remaining open task is rejected.

The open tasks are cleared before the document returns to validation. Workflows that run on the status change can then create new tasks for anything that still needs attention.

With **Default behaviour**, open tasks stay open when a document is sent back, as before.

### Benefits

* **Clear responsibilities**: Documents can be assigned to the right person instead of relying on email.
* **Nothing gets forgotten**: Notifications remind users about documents that need their action.
* **Open work at a glance**: With Dashboard Tasks Count, the Dashboard shows which documents still have open tasks.
* **Decisions stay traceable**: With the deletion and completion options, tasks leave the queue only through a decision or an admin.

### How to Use

1. Go to **Settings**.
2. Select **Document Processing**.
3. Select **Module**.
4. Open the **Document Type** section.
5. Switch **Tasks & Notifications** on.
6. (Optional) Switch **Dashboard Tasks Count** on to show the task icon on the Dashboard.
7. (Optional) Switch **Allow "All" filter for non-admins** on if all users should see every task.
8. (Optional) Choose which tasks users may delete in **Non-admin task deletion**.
9. (Optional) Choose who may close tasks in **Non-admin task completion**.

The deletion and completion options are saved as soon as you choose a value.

### When to Use This Feature

* **Teams that share document work**: Enable it when several people validate or approve documents and need to hand work to each other.
* **Workload visibility**: Also enable Dashboard Tasks Count when the team should see on the Dashboard which documents still have open tasks.
* **Tasks that only admins or a decision should close**: Set **Non-admin task completion** to **Admins only** or **Admins and assigned users**, and **Non-admin task deletion** to **None**, when users must not remove tasks that were not actually done.
* **Single-user or fully automated setups**: You can leave it off if no one needs to assign documents or track tasks.
