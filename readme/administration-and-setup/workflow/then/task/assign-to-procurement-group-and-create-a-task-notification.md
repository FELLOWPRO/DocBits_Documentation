# Assign to Procurement Group and Create a Task/Notification

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose**

The "**Assign Document to Procurement Group and Create Task/Notification**" workflow card assigns a document to a specified procurement group, creates a task or notification with defined details, and optionally notifies the group via email. It prioritizes task execution based on a configurable numeric priority value.

## **Components of the Card**

1. **Group Name**
   * **Description:** Specifies the procurement group responsible for handling the document.
   * **Detail:** A field where the user can manually enter the name of the procurement group.
2. **Task/Notification**
   * **Description:** Defines whether a task or notification is created for the group.
   * **Detail:** A field where the user can choose between creating a task or a notificatio
3. **Title**
   * **Description:** The title of the task or notification created for the group.
   * **Detail:** A field to provide a concise and identifiable title for the task or notification.
4. **Description**
   * **Description:** Further details about the task or notification.
   * **Detail:** A field to describe the task’s purpose and provide context or instructions.
5. **Priority**
   * **Description:** Defines the urgency level of the task or notification.
   * **Options:**
     * **High:** Task requires immediate attention.
     * **Medium:** Task is important but not urgent.
     * **Low:** Task can be handled at a later time.
6. **Send Mail**
   * **Description:** Configures whether an email notification should be sent to the group.
   * **Options:**
     * **True:** Sends an email notification to the procurement group.
     * **False:** No email notification is sent.
7. **Value**
   * **Description:** Sets the numeric priority for task execution.
   * **Detail:** A field to input a numeric value, where a lower number represents a higher priority.

## **Functionality**

* **Condition Evaluation:**\
  The card performs its actions only if the defined workflow conditions are met.
* **Group Assignment and Task/Notification Creation:**\
  The document is assigned to the specified procurement group. A task or notification is created with the provided title, description, and priority.
* **Email Notification:**\
  If "Send Mail" is set to True, the group receives an email about the task or notification.

## **Setup and Configuration**

1. **Define Group Name:**
   * Enter the name of the procurement group in the Group Name field.
2. **Configure Task/Notification Details:**
   * Specify the Title and Description for the task or notification.
   * Select the Priority from the dropdown menu (High, Medium, or Low).
3. **Enable Email Notification:**
   * Set "Send Mail" to True or False based on whether the group should receive an email.
4. **Set Numeric Priority:**
   * Input a numeric value in the Value field to determine the task's priority, where lower values are processed first.
5. Save the card configuration and activate the workflow.

## **Conclusion**

The "Assign Document to Procurement Group and Create Task/Notification" workflow card ensures documents are directed to the appropriate group with clear task instructions and priority levels. By enabling optional email notifications, this card improves task visibility and ensures smooth workflow execution.
