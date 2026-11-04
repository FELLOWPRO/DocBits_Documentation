# Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513.png" alt=""><figcaption></figcaption></figure>

**Purpose**

This workflow card manages the execution of operations based on whether a task or document is assigned to a particular user or set of users. It employs conditional logic to either trigger or prevent specific actions, making it ideal for workflows that require user-specific handling.

**Components of the Card**

1. **Operator**
   * **Description**: Defines the logical condition to apply to the user assignment.
   * **Options**:
     * **IS**: Triggers the operation if the assigned user of the document or task matches any user in the specified list.
     * **IS NOT**: Triggers the operation if the assigned user of the document or task does not match any user in the specified list.
2. **User List**
   * **Description**: A list or selection of users to compare against the assigned user.
   * **Detail**: This list can include one or multiple users, allowing the card to handle both singular and multiple user conditions effectively. The selection can be made through checkboxes, a multi-select dropdown, or similar UI elements.

**Functionality**

* **User Assignment Identification**: Automatically identifies the user or users assigned to a particular task or document within the ERP system.
* **Condition Evaluation**:
  * Using the **IS** operator, the card checks if the assigned user is among those listed in the User List.
  * Using the **IS NOT** operator, the card ensures the assigned user is not among those listed.
* **Action Execution**:
  * **True Condition**: If the user assignment meets the condition (either IS or IS NOT), relevant actions are triggered, such as notifications, task initiations, approvals, or other workflow steps.
  * **False Condition**: If the condition is not met, the document or task may pass through different routing, or alternative actions may be specified.

**User Interactions**

* **Setup and Configuration**: Users configure the card by selecting an operator and specifying the relevant users from the User List. Setup should be user-friendly and intuitive to accommodate selections from potentially large user bases.
* **Monitoring and Reporting**: The ERP system should provide functionality to monitor and report on the operations triggered by this card, offering insights into assignment accuracy and process efficiency.
* **Error Handling and Notifications**: Users should have options to receive alerts or notifications if there are issues with the assignments, such as unassigned tasks or errors in user selection.

#### Conclusion

The "Assigned User Condition" workflow card is a critical tool for managing document and task workflows that depend on user assignments. By allowing conditions based on whether a task or document is assigned to specific users, it ensures that workflows are only triggered by appropriate user interactions, enhancing both accountability and task alignment within teams. Clearly documenting this card will help users understand its significance and integrate it effectively into their workflows, ensuring smooth and efficient operations tailored to user roles and responsibilities.

