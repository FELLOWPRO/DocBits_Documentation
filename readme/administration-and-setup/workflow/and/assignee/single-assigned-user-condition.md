# Single Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50 (1).png" alt="" width="552"><figcaption></figcaption></figure>

**Purpose**

This workflow card facilitates operations based on the assignment of a task or document to a single, specific user. Using a direct conditional logic approach, it manages workflows that require targeted user engagement, ensuring precision in user-based task handling.

**Components of the Card**

1. **Operator**
   * **Description**: Specifies the logic to apply to the user assignment.
   * **Options**:
     * **IS**: Triggers the operation if the assigned user of the document or task matches the specified user.
     * **IS NOT**: Triggers the operation if the assigned user does not match the specified user.
2. **User**
   * **Description**: Allows selection of a single user against whom the assigned user will be compared.
   * **Detail**: This involves a simple dropdown or autocomplete field where one user can be selected at a time.

**Functionality**

* **User Assignment Identification**: Identifies the user currently assigned to a specific task or document.
* **Condition Evaluation**:
  * For the **IS** operator, the card checks if the assigned user is the same as the user selected.
  * For the **IS NOT** operator, it verifies that the assigned user is different from the selected user.
* **Action Execution**:
  * **True Condition**: If the assignment meets the set condition (IS or IS NOT), it triggers predefined actions, which could include moving forward with approvals, initiating further tasks, sending notifications, or other related workflows.
  * **False Condition**: If the condition is not met, the workflow will not continue.

**User Interactions**

* **Setup and Configuration**: Users set up the card by choosing an operator and selecting a user from the user field. This setup should be straightforward, ensuring easy user selection and configuration.
* **Monitoring and Reporting**: Offers tools for monitoring the card’s performance, such as tracking which tasks are triggered by specific user assignments and the outcomes of these triggers.
* **Error Handling and Notifications**: Provides mechanisms to alert users if tasks are incorrectly assigned or if operational errors occur due to assignment issues.

#### Conclusion

The "Single Assigned User Condition" workflow card is essential for precise, user-specific document and task management within an ERP system. It simplifies workflows by focusing on individual user assignments, thus ensuring that actions are only executed when appropriate, based on the user's role and responsibilities. Documenting this card clearly will assist users in understanding its application, allowing them to implement and manage it effectively within their daily operations. This documentation ensures that all potential users can easily grasp the card's purpose and integrate it seamlessly into their workflows.
