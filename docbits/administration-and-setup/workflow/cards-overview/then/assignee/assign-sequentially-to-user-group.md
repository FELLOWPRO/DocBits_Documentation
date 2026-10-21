# Assign Sequentially to User/Group

<figure><img src="../../../../../.gitbook/assets/image (144).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose**

The "**Assign the Document Sequentially to User/Group Based on Decision Table**" workflow card dynamically assigns documents to either a user or a group, depending on the decision table's evaluation. This ensures that documents are routed appropriately based on predefined rules.

## **Components of the Card**

1. **Priority (Value)**
   * **Description**: Specifies the priority level for assignments, where lower numbers represent higher priority.
   * **Detail**: A numeric input field where the priority value can be set to control the sequence of assignment.

## **Functionality**

* **Decision Table Evaluation**:\
  The decision table evaluates predefined conditions to decide whether the document is assigned to a user or a group.
* **Document Assignment**:
  * If the decision table returns a user, the document is assigned directly to that user.
  * If the decision table returns a group, the document is assigned to the group sequentially, respecting the specified priority value.

## **Setup and Configuration**

1. Add the **Assign the Document Sequentially** card to your workflow.
2. Configure the **Priority (Value)** field:
   * Enter a numeric value to set the assignment priority.
3. Save and activate the workflow to apply the configuration.

## **Conclusion**

The "**Assign the Document Sequentially to User/Group Based on Decision Table**" workflow card ensures efficient and dynamic document routing. By leveraging decision table logic and priority values, the card facilitates accurate assignment to either a user or a group, streamlining document workflows.

<!-- workflow-card-practical-example-20261021 -->

## Practical example

**When to use:** Use a decision table to select a prioritized document assignee.

**Configuration:** Configure a matching demo decision-table rule returning the intended user or group, then select that table on the card.

**Expected result and counterexample:** The returned assignee is used for sequential document assignment. With no matching return, do not assume a default assignee; inspect the result and configured fallback behavior of this version.

This is an illustrative configuration and expected outcome. Use fields, users and groups configured in your test organization; it is not a claim that this example was executed.
