# Assign a Task with Title

<figure><img src="../../../../.gitbook/assets/image (291).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

The "Assign Task / Notification from Decision Table" workflow card is designed to dynamically assign tasks or notifications based on the results of a decision table. This card ensures tasks or notifications are assigned to the correct user or group according to the logic defined in the decision table, with an optional email notification sent to the recipient.

## **Components of the Card:**

1. **Title**
   * **Description**: Specifies the title of the task or notification being created.
   * **Detail**: The title should provide context and describe the purpose of the task or notification.
2. **Description**
   * **Description**: Defines the content or purpose of the task or notification.
   * **Detail**: Provides additional information about the task or notification, explaining the context or action required.
3. **Priority**
   * **Description**: Defines the urgency level of the task or notification.
   * **Options**:
     * **High**: Tasks or notifications requiring immediate attention.
     * **Medium**: Important tasks that should be addressed promptly.
     * **Low**: Tasks that can be attended to at a later time.
4. **Assignee Type**
   * **Description**: Specifies the user or group assigned to the task or notification based on the decision table’s output.
   * **Detail**: The decision table dynamically evaluates conditions and returns the appropriate user or group for assignment.
5. **Email Notification**
   * **Description**: Configures whether an email notification will be sent to the assigned user or group.
   * **Options**:
     * **True**: Sends an email notification to the recipient.
     * **False**: No email notification is sent.

#### **Additional Components in Version 3**

1. **Notification Type**
   * **Description**: Specifies whether the card creates a task or a notification.
   * **Options**:
     * **Task**: Creates a task assigned to the user or group from the decision table.
     * **Notification**: Sends a notification to the user or group from the decision table.

## **Functionality:**

* **Condition Evaluation:**\
  The card only executes its action if both the **"Where"** and **"And Sections"** evaluate as true.
* **Task / Notification Assignment**\
  The card assigns the task or notification to the user or group identified by the decision table. The decision table dynamically evaluates predefined conditions and returns the corresponding recipient.
* **Email Notification**\
  If configured to do so, an email notification is sent to the assigned user or group.
* **Version 3 Functionality**\
  In Version 3, the card allows the creation of either a Task or a Notification, providing more flexibility for task management and communication.

## **Setup and Configuration:**

1. **Define Task or Notification Details**:\
   Enter the title, description, and priority for the task or notification.
2. **Configure Decision Table**:\
   Set up the decision table to dynamically determine which user or group should be assigned the task or notification.
3. **Enable Email Notification**:\
   Specify whether an email notification should be sent to the assigned user or group.
4. **Specify Notification Type (Version 3)**:\
   Choose whether the card will create a task or send a notification.

## **Conclusion:**

The **"Assign Task / Notification from Decision Table"** workflow card automates the assignment of tasks or notifications based on dynamic conditions defined in a decision table. Version 3 enhances its functionality by allowing users to choose between creating a task or notification, and ensures the correct recipient is always assigned. The email notification feature keeps users informed, streamlining communication and task management.
