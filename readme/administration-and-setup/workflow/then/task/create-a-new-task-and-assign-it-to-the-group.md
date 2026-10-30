# Create a New Task and assign it to the group

<figure><img src="../../../../.gitbook/assets/image (289).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

The **"Create Group Task or Notification"** workflow card facilitates task or notification creation for specified groups, ensuring efficient communication and task management. Enhanced with decision tree functionality in later versions, it dynamically determines the assigned group or method, streamlining operations.

## **Components of the Card:**

1. **Title**
   * **Description**: Specifies the title of the task or notification.
   * **Detail**: Acts as the identifier for the created task or notification.
2. **Description**
   * **Description**: Describes the context or details of the task or notification.
   * **Detail**: Provides clarity on its purpose.
3. **Priority**
   * **Description**: Sets the importance level of the task.
   * **Options**:
     * **High**: Requires immediate action.
     * **Medium**: Important but less urgent.
     * **Low**: Can be addressed later.
4. **Assigned Group**
   * **Description**: Specifies the group responsible for the task or notification.
   * **Detail**: Selected from a dropdown list of available groups.
5. **Email Notification**
   * **Description**: Enables sending an email to notify the assigned group.
   * **Options**:
     * **True**: Sends an email notification.
     * **False**: No email notification is sent.

## **Additional Components in Version 3 and Version 4**

1. **Decision Tree  (Version 3 Only)**
   * **Description**: Enables the use of a decision tree for dynamic task creation.
   * **Options**:
     * **True**: Activates decision tree processing.
     * **False**: Disables decision tree processing.
2. **Task/Notification Option** **(Version 4 Only)**
   * **Description**: Allows creating either a task or a notification.
   * **Options**:
     * **Task**: Creates a task for the selected group.
     * **Notification**: Sends a notification instead of creating a task.

## **Functionality:**

* **Condition Evaluation**:\
  Executes the card action only when the **"Where"** and **"And Sections"** are true.
* **Task or Notification Creation**:
  * A task is created for the selected group with the specified title, description, and priority.
  * In Version 4, the card can create a notification instead of a task.
* **Dynamic Assignment (Version 3 only)**:\
  If enabled, the decision tree determines the target group dynamically.
* **Email Notification**:\
  Sends an email notification to the group if the email option is set to true.

## **Setup and Configuration:**

1. **Define Task or Notification Details**: Enter the title, description, and priority.
2. **Assign to a Group**: Select a group from the dropdown list for task or notification assignment.
3. **Enable Email Notification**: Indicate whether the group should be notified via email.
4. **Use Decision Tree (Version 3 only)**: Enable the decision tree to dynamically assign the group.
5. **Select Output Type (Version 4 only)**: Choose whether the card creates a task or a notification.

## **Conclusion:**

The **"Create Group Task or Notification"** workflow card simplifies task and notification management by targeting groups directly. Its dynamic assignment feature, enabled by the decision tree, enhances flexibility, while email notifications ensure timely communication. Versions 3 and 4 add advanced functionality, making it a versatile tool for efficient workflow execution.
