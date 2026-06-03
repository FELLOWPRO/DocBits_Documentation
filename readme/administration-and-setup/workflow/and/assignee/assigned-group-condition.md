# Assigned Group Condition

<figure><img src="../../../../.gitbook/assets/image (15) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Purpose:**

This workflow card executes operations based on whether a task or document is assigned to a particular group or set of groups. It utilizes conditional logic to either trigger or prevent specific actions depending on the group assignment, making it ideal for workflows that require group-specific handling.

**Components of the Card:**

1. **Operator**
   * **Description:** Defines the logical condition to apply to the group assignment.
   * **Options:**
     * **IS:** Triggers the operation if the assigned group of the document or task matches one of the groups in the specified list.
     * **IS NOT:** Triggers the operation if the assigned group of the document or task does not match any of the groups in the specified list.
2. **Groups List**
   * **Description:** A list or selection of groups to compare against the assigned group.
   * **Detail:** This list can include one or multiple groups, allowing the card to handle both singular and multiple group conditions effectively.

**Functionality:**

* **Group Assignment Identification:** Automatically identifies the group or groups assigned to a particular task or document within the system.
* **Condition Evaluation:**
  * Using the **IS** operator, the card checks if the assigned group is one of the groups listed in the Groups List.
  * Using the **IS NOT** operator, the card ensures the assigned group is not part of the groups listed.
* **Action Execution:**
  * **True Condition:** If the group assignment meets the condition (either **IS** or **IS NOT**), relevant actions are triggered, such as notifications, task initiations, approvals, or other workflow steps.
  * **False Condition:**  If the condition is not met, the workflow will not continue.

**User Interactions:**

* **Setup and Configuration:**&#x55;sers configure the card by selecting an operator and specifying the relevant groups from the Groups List. Setup should be user-friendly and intuitive to accommodate selections from potentially large group bases.
* **Monitoring and Reporting:**\
  The system should provide functionality to monitor and report on the operations triggered by this card, offering insights into assignment accuracy and process efficiency.
* **Error Handling and Notifications:**\
  Users should have options to receive alerts or notifications if there are issues with the assignments, such as unassigned tasks or errors in group selection.

**Conclusion:**\
The "Assigned Group Condition" workflow card is essential for managing document and task workflows that depend on group assignments. By allowing conditions based on whether a task or document is assigned to specific groups, it ensures that workflows are only triggered by appropriate group interactions, improving accountability and task management across teams.
