# Assign Document and Create Task/Notification for User

<figure><img src="../../../../.gitbook/assets/image (13) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose**

The "**Assign Document and Create Task/Notification for User**" workflow card assigns a document to a specified user, creates a task or notification with configurable details, and optionally sends an email notification to the user. This card also enables setting a numeric priority value to determine the order of execution.

## **Components of the Card**

1. **User**
   * **Description:** Specifies the user who will receive the task or notification.
   * **Detail:** A dropdown menu to select the user to whom the document and task/notification will be assigned.
2. **Task/Notification**
   * **Description:** Specifies the type of action to create for the user.
   * **Detail:** A dropdown to choose either "Task" or "Notification" based on the intended action.
3. **Title**
   * **Description:** The title of the task or notification.
   * **Detail:** A field to provide a concise, descriptive title for the task or notification.
4. **Description**
   * **Description:** Additional details about the task or notification.
   * **Detail:** A field to describe the task’s purpose or provide context for the notification.
5. **Priority**
   * **Description:** Defines the urgency level of the task or notification.
   * **Options:**
     * **High:** Requires immediate attention.
     * **Medium:** Important but not urgent.
     * **Low:** Can be addressed later.
6. **Send Mail**
   * **Description:** Configures whether an email notification is sent to the user.
   * **Options:**
     * **True:** Sends an email notification to the user.
     * **False:** No email notification is sent.
7. **Value**
   * **Description:** Sets the numeric priority for the document assignment.
   * **Detail:** A field to input a numeric value, where lower numbers indicate higher priority.

## **Functionality**

* **Condition Evaluation:**\
  The card executes its actions only if the configured workflow conditions are met.
* **Document Assignment and Task/Notification Creation:**\
  The document is assigned to the user specified in the "User" field. A task or notification is created with the provided title, description, and priority level.
* **Email Notification:**\
  If "Send Mail" is set to True, an email is sent to the user notifying them about the task or notification.

## **Setup and Configuration**

1. **Select User:**
   * Choose the user from the User dropdown menu.
2. **Configure Task/Notification Details:**
   * Select "Task" or "Notification" from the Task/Notification dropdown.
   * Enter the Title and Description for the task or notification.
   * Set the Priority by selecting High, Medium, or Low from the dropdown.
3. **Enable Email Notification:**
   * Configure the Send Mail option to True or False, depending on whether an email notification should be sent.
4. **Set Numeric Priority:**
   * Input a numeric value in the Value field to determine the assignment’s priority, where lower values are processed first.
5. Save the card configuration and activate the workflow.

## **Conclusion**

The "Assign Document and Create Task/Notification for User" workflow card ensures documents are assigned to the appropriate user while creating tasks or notifications with defined priorities and optional email notifications. This card helps streamline task delegation and enhances workflow efficiency.
