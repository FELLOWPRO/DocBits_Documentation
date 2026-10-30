# Create a New Task and assign it to the User

<figure><img src="../../../../.gitbook/assets/image (287).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose**

The **"Create Task or Notification"** workflow card streamlines task management and notifications within workflows. Depending on the version, the card can create tasks, send notifications, and leverage additional functionality such as decision trees for dynamic processing.

## **Components of the Card**

1. **Title**
   * **Description**: Defines the title of the task or notification being created.
   * **Detail**: The title provides a clear and concise identifier for the task or notification.
2. **Description**
   * **Description**: Provides details about the task or notification.
   * **Detail**: Helps clarify the purpose or context of the task or notification for the assigned user.
3. **Priority**
   * **Description**: Sets the urgency level for the task.
   * **Options**:
     * **High**: Requires immediate attention.
     * **Medium**: Important but not urgent.
     * **Low**: Can be addressed later.
4. **Assigned User**
   1. **Description**: Specifies the user to whom the task is assigned.
   2. **Detail**: Users are selected from a dropdown list of available personnel.
5. **Email Notification**
   * **Description**: Determines whether the assigned user receives an email notification.
   * **Options**:
     * **True**: Sends an email notification to the user.
     * **False**: No email notification is sent.

## Additional Components **in Version 3 and Version 4**

1. **Decision Tree (Version 3 Only)**
   * **Description**: Enables the use of a decision tree for dynamic task creation.
   * **Options**:
     * **True**: Activates decision tree processing.
     * **False**: Disables decision tree processing.
2. **Task or Notification (Version 4 Only)**
   * **Description**: Allows selection between creating a task or a notification.
   * **Options**:
     * **Task**: Creates a task.
     * **Notification**: Creates a notification instead of a task.

## **Functionality:**

* **Condition Evaluation**:\
  This card is triggered only if conditions in the **"Where"** and **"And Sections"** are met.
* **Task or Notification Creation**:
  * Versions 2 and 3: A task is created with the specified title, description, priority, and assigned user.
  * Version 4: Allows creating either a task or a notification.
* **Dynamic Assignment**:
  * In Version 3, the decision tree dynamically determines the user to be assigned the task based on workflow parameters.
* **Email Notification**:\
  Sends an email to the assigned user if the notification option is enabled.

## **Setup and Configuration:**

1. **Select Version**: Choose the version of the card based on the functionality required:
   * Version 2: Basic task creation with manual user assignment and email notifications.
   * Version 3: Includes decision tree functionality for dynamic user assignment.
   * Version 4: Adds the ability to create a notification instead of a task.
2. **Enter Task Details**: Specify the title, description, and priority of the task or notification.
3. **Assign User**:
   * For Versions 2 and 4, manually select a user from the dropdown list.
   * For Version 3, enable the decision tree to determine the assigned user dynamically.
4. **Enable Email Notification**: Specify whether the assigned user should receive an email notification.
5. (For Version 4) **Choose Task or Notification**: Indicate whether to create a task or notification.

## **Conclusion:**

The **"Create Task or Notification"** workflow card is a versatile tool for managing tasks and notifications. By supporting dynamic user assignment through decision trees and providing options for task or notification creation, it enhances workflow adaptability and collaboration efficiency.
