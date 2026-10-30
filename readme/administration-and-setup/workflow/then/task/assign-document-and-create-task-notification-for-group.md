# Assign Document and Create Task/Notification for Group

<figure><img src="../../../../.gitbook/assets/image (12) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose**

The "**Assign Document and Create Task/Notification for Group**" workflow card assigns a document to a specified group, creates a task or notification with customizable details, and optionally sends an email notification to the group. This card also supports assigning a numeric priority value to determine the order of execution.

## **Components of the Card**

1. **Group Name**
   * **Description:** Specifies the group that will receive the task or notification.
   * **Detail:** A dropdown to choose the name of the group to which the document and task/notification will be assigned.
2. **Task/Notification**
   * **Description:** Specifies the type of action to create for the group.
   * **Detail:** A dropdown to select either "Task" or "Notification" based on the desired action.
3. **Title**
   * **Description:** Provides the title of the task or notification.
   * **Detail:** A field to add a concise, descriptive title for the task or notification.
4. **Description**
   * **Description:** Further describes the task or notification.
   * **Detail:** A field to provide additional details about the task’s purpose or the notification’s content.
5. **Priority**
   * **Description:** Defines the urgency level of the task or notification.
   * **Options:**
     * **High:** Requires immediate attention.
     * **Medium:** Important but not urgent.
     * **Low:** Can be addressed later.
6. **Send Mail**
   * **Description:** Configures whether an email notification is sent to the group.
   * **Options:**
     * **True:** Sends an email notification.
     * **False:** Does not send an email.
7. **Value**
   * **Description:** Sets the numeric priority for the document assignment.
   * **Detail:** A field to input a numeric value, where a lower number indicates a higher priority.

## **Functionality**

* **Condition Evaluation:**\
  The card executes its actions only if the configured workflow conditions are satisfied.
* **Document Assignment and Task/Notification Creation:**\
  The document is assigned to the group specified in the "Group Name" field. A task or notification is created with the configured title, description, and priority level.
* **Email Notification:**\
  If "Send Mail" is set to True, an email notification is sent to the group to inform them about the task or notification.

## **Setup and Configuration**

1. **Define Group Name:**
   * Input the name of the group in the Group Name field.
2. **Select Task/Notification:**
   * Choose "Task" or "Notification" from the Task/Notification dropdown.
3. **Set Task/Notification Details:**
   * Enter the Title and Description for the task or notification.
   * Select the Priority from the dropdown (High, Medium, or Low).
4. **Enable Email Notification:**
   * Configure the Send Mail option to True or False, depending on whether an email notification should be sent.
5. **Assign Numeric Priority:**
   * Input a numeric value in the Value field to determine the assignment’s priority, where lower values take precedence.
6. Save the card configuration and activate the workflow.

## **Conclusion**

The "Assign Document and Create Task/Notification for Group" workflow card ensures documents are assigned to the appropriate group while creating tasks or notifications with customizable priority and email notification options. This streamlines document management and enhances workflow efficiency.
