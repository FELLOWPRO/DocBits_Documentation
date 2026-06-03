# Single Assigned User Condition

<figure><img src="../../../../.gitbook/assets/image (16) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Purpose:**\
This workflow card executes operations based on whether a task or document is assigned to a particular group. It uses a straightforward condition to trigger or prevent actions based on group assignment.

**Components of the Card:**

1. **Operator**
   * **Description:** Defines the logical condition to apply to the group assignment.
   * **Options:**
     * **IS:** Triggers the operation if the assigned group of the document or task matches the specified group.
     * **IS NOT:** Triggers the operation if the assigned group of the document or task does not match the specified group.
2. **Group**
   * **Description:** Specifies the group to compare against the assigned group.
   * **Detail:** This field allows you to select a single group to compare the assignment.

**Functionality:**

* **Group Assignment Identification:** Automatically identifies the group assigned to a particular task or document.
* **Condition Evaluation:**
  * Using the **IS** operator, the card checks if the assigned group matches the specified group.
  * Using the **IS NOT** operator, the card ensures the assigned group does not match the specified group.
* **Action Execution:**
  * **True Condition:** If the group assignment meets the condition (either **IS** or **IS NOT**), relevant actions are triggered, such as notifications, task initiations, approvals, or other workflow steps.
  * **False Condition:** If the condition is not met, the document or task may pass through different routing, or alternative actions may be specified.

**User Interactions:**

* **Setup and Configuration:**\
  Users configure the card by selecting an operator and specifying the relevant group. The setup should be simple and intuitive.
* **Monitoring and Reporting:**\
  The system should provide functionality to monitor and report on operations triggered by this card, offering insights into assignment accuracy and process efficiency.
* **Error Handling and Notifications:**\
  Users should have options to receive alerts or notifications if there are issues with the assignments, such as unassigned tasks or errors in group selection.

**Conclusion:**\
The "Assigned Group Condition" workflow card is essential for managing document and task workflows based on group assignments. By allowing conditions based on whether a task or document is assigned to a specific group, it ensures that workflows are only triggered by the appropriate group interactions, enhancing task management and workflow efficiency.
