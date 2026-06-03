# Create a New Task and assign it to the Recipient

<figure><img src="../../../../.gitbook/assets/image (288).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

The **"Create Task with Fallback"** workflow card ensures efficient task delegation by assigning tasks to specific roles—dispatcher or purchaser—while incorporating a fallback mechanism to prevent task assignment failures. This card improves workflow reliability and adaptability in dynamic scenarios.

## **Components of the Card:**

1. **Title**
   * **Description**: Specifies the title of the task being created.
   * **Detail**: Provides a concise identifier for the task.
2. **Description**
   * **Description**: Describes the purpose or context of the task.
   * **Detail**: Clarifies the details of the task.
3. **Priority**
   * **Description**: Sets the urgency level for the task.
   * **Options**:
     * **High**: Requires immediate attention.
     * **Medium**: Important but not urgent.
     * **Low**: Can be addressed later.
4. **Assigned Role**
   * **Description**: Specifies the primary role to which the task is assigned.
   * **Options**:
     * **Disponent**: Assigns the task to the disponent.
     * **Purchaser**: Assigns the task to the purchaser.
5. **Email Notification**
   * **Description**: Enables notifying the assigned user via email.
   * **Options**:
     * **True**: Sends an email notification to the user.
     * **False**: No email notification is sent.
6. **Fallback User**
   * **Description**: Provides a fallback option for task assignment if the recipient role is not found.
   * **Detail**: Allows selecting a user from a dropdown list to ensure task delegation.

## **Functionality:**

* **Condition Evaluation**:\
  The card executes only if the conditions in the **"Where"** and **"And Sections"** are met.
* **Task Assignment**:
  * The task is assigned to the selected role (dispatcher or purchaser).
  * If the specified role is not found, the task is assigned to a user from the fallback dropdown list.
* **Email Notification**:\
  Sends an email to the assigned user if email notification is enabled.

## **Setup and Configuration:**

1. **Specify Task Details**: Enter the title, description, and priority of the task.
2. **Select Primary Role**: Choose the role to which the task will be assigned (dispatcher or purchaser).
3. **Configure Fallback User**: Select a fallback user from the dropdown list to ensure task assignment if the primary role is not found.
4. **Enable Email Notification**: Indicate whether the assigned user should receive an email notification.

## **Conclusion:**

The **"Create Task with Fallback"** workflow card ensures seamless task delegation by integrating a fallback mechanism. By assigning tasks based on roles and providing an alternate user option, it enhances reliability and flexibility in task management processes.
