# Assign Sequentially to Groups

## **Purpose**

The "**Assign the Document Sequentially to the Groups**" workflow card enables the sequential assignment of documents to one or more selected groups. The priority value determines the order of assignment, with lower numbers representing higher priority.

## **Components of the Card**

1. **Group**
   * **Description**: Specifies the groups that will receive the document assignment.
   * **Detail**: A dropdown menu where one or multiple groups can be selected for document assignment.
2. **Priority (Value)**
   * **Description**: A numeric input field where the priority level for the groups can be set.
   * **Detail**: Lower numbers signify higher priority, ensuring that documents are assigned to groups in ascending order of priority.

## **Functionality**

* **Document Assignment**:\
  The card assigns documents sequentially to the selected groups based on their priority values.\
  If multiple groups share the same priority, documents are assigned in the order the groups were selected.

## **Setup and Configuration**

1. Add the **Assign the Document Sequentially** card to your workflow.
2. Configure the **Group** field:
   * Select one or multiple groups from the dropdown menu.
3. Configure the **Priority (Value)** field:
   * Enter a numeric value to set the assignment priority.
4. Save and activate the workflow to apply the configuration.

## **Conclusion**

The "Assign the Document Sequentially to Groups" workflow card ensures efficient document allocation to one or more groups based on priority. This feature supports flexible and organized document processing across multiple teams or departments.

<!-- workflow-card-practical-example-20261021 -->

## Practical example

**When to use:** Prioritize document assignment to review teams.

**Configuration:** Select the configured demo groups and set the required priority, for example `10`.

**Expected result and counterexample:** The document receives the selected group assignments at that priority. Test a second priority separately when the groups must occupy different stages.

This is an illustrative configuration and expected outcome. Use fields, users and groups configured in your test organization; it is not a claim that this example was executed.
