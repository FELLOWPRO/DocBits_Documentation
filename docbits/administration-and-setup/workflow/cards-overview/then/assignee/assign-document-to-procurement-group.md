# Assign document to procurement group

<figure><img src="../../../../../.gitbook/assets/workflow_card_action_assign_doc_to_procurement_group_v2.png" alt="Workflow card Assignee: Assign document to procurement group Group Name, version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

## **Purpose:**

The **"Assign to Procurement Group"** workflow card is used to assign a document to a specified procurement group within the system. This helps streamline document management by ensuring that the appropriate team handles the document based on its assigned procurement group.

## **Components of the Card:**

1. **Procurement Group**
   * **Description:** Specifies the procurement group to which the document will be assigned.
   * **Detail:** The selected procurement group will be responsible for processing and managing the document.

## **Functionality:**

* **Condition Evaluation:**\
  The card only executes its action if both the **"When"** and **"And"** evaluate as true.
* **Action Execution:**\
  If both conditions are true, the document is assigned to the specified procurement group. If either condition is false, no actions are taken, and the document remains unassigned.

## **Setup and Configuration:**

* **Select Procurement Group:** Choose the procurement group to assign the document to from the dropdown list.

## **Conclusion:**

The **"Assign to Procurement Group"** workflow card provides a simple yet effective way to ensure that documents are automatically assigned to the correct procurement team for further processing.

<!-- workflow-card-practical-example-20261021 -->

## Practical example

**When to use:** Send a purchasing exception to its procurement group.

**Configuration:** Select the configured group `Demo Procurement`.

**Expected result and counterexample:** The document is assigned to that procurement group. A similarly named ordinary group must not be assumed to be the same configured target.

This is an illustrative configuration and expected outcome. Use fields, users and groups configured in your test organization; it is not a claim that this example was executed.
