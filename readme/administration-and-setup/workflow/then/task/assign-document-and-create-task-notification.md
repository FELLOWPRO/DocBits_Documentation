# Assign Document and Create Task/Notification

<figure><img src="../../../../.gitbook/assets/image (14) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose**

The "**Assign Document and Create Task/Notification Based on Decision Table**" workflow card assigns a document and creates a task or notification with configurable details. The assignee is determined by the return of a decision table, and the card allows for setting priorities and sending email notifications.

## **Components of the Card**

1. **Assignee Type**
   * **Description:** Specifies whether the decision table’s return assigns the document and task/notification to a user or group.
   * **Detail:** A field to configure the assignee type as either "User" or "Group" based on the decision table output.
2. **Task/Notification**
   * **Description:** Specifies the type of action to create for the assignee.
   * **Detail:** A dropdown to select either "Task" or "Notification" based on the workflow needs.
3. **Title**
   * **Description:** The title of the task or notification.
   * **Detail:** A field for providing a concise title that identifies the task or notification.
4. **Description**
   * **Description:** Additional details about the task or notification.
   * **Detail:** A field for describing the purpose and context of the task or notification.
5. **Priority**
   * **Description:** Defines the urgency level of the task or notification.
   * **Options:**
     * **High:** Requires immediate attention.
     * **Medium:** Important but not urgent.
     * **Low:** Can be addressed later.
6. **Assignee Type**
   * **Description:** This field determines the type of assignee (User or Group) to whom the document and task/notification are assigned.
   * **Detail:** A dropdown menu to select whether the task/notification is assigned to a user or a group based on the decision table's output.
7. **Send Mail**
   * **Description:** Configures whether an email notification is sent to the assignee.
   * **Options:**
     * **True:** Sends an email notification.
     * **False:** No email notification is sent.
8. **Value**
   * **Description:** Sets the numeric priority for the document assignment.
   * **Detail:** A field to input a numeric value, where lower numbers indicate higher priority.

## **Functionality**

* **Condition Evaluation:**\
  The card executes its actions only if the workflow conditions are satisfied.
* **Decision Table Evaluation:**\
  The decision table determines whether the document and task/notification are assigned to a user or group.
* **Document Assignment and Task/Notification Creation:**\
  The document is assigned to the decision table's result. A task or notification is created with the specified title, description, and priority level.
* **Email Notification:**\
  If "Send Mail" is set to True, an email notification is sent to the assignee.

## **Setup and Configuration**

1. **Define Assignee Type:**
   * Configure the Assignee Type field to either "User" or "Group" based on the decision table's output.
2. **Select Task/Notification:**
   * Choose "Task" or "Notification" from the Task/Notification dropdown.
3. **Set Task/Notification Details:**
   * Enter the Title and Description for the task or notification.
   * Select the Priority (High, Medium, or Low) from the dropdown.
4. **Enable Email Notification:**
   * Set the Send Mail option to True or False, depending on whether an email notification should be sent.
5. **Set Numeric Priority:**
   * Input a numeric value in the Value field to determine the assignment priority, where lower numbers are processed first.
6. Save the card configuration and activate the workflow.

## **Conclusion**

The "Assign Document and Create Task/Notification Based on Decision Table" workflow card ensures tasks or notifications are dynamically assigned to the appropriate user or group based on decision table results. This card facilitates efficient task delegation, customizable priorities, and optional email notifications to enhance workflow responsiveness.
