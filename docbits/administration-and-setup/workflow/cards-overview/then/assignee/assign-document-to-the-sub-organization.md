# Assign document to the sub organization

<figure><img src="../../../../../.gitbook/assets/image (375).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

The **"Assign Document to Sub-Organization"** workflow card assigns a document to a specific sub-organization within the system, ensuring that it is routed to the appropriate organizational unit for processing.

## **Components of the Card:**

1. **Sub-Organization**
   * **Description:** Specifies the sub-organization to which the document will be assigned.
   * **Detail:** A dropdown list of available sub-organizations is provided for selecting the target sub-organization.

## **Functionality:**

* **Condition Evaluation:**\
  The card only executes its action if both the **"When"** and **"And"** evaluate as true.
* **Document Assignment:**\
  The card assigns the document to the sub-organization selected from the dropdown list.

## **Setup and Configuration:**

* **Select Sub-Organization:**\
  Choose the appropriate sub-organization from the dropdown list to which the document should be assigned.

## **Conclusion:**

The **"Assign Document to Sub-Organization"** workflow card ensures that documents are routed to the correct sub-organization, streamlining the document management process by assigning responsibility based on organizational structure.

<!-- workflow-card-practical-example-20261021 -->

## Practical example

**When to use:** Route a document to a known business unit.

**Configuration:** Select configured suborganization `Demo North`.

**Expected result and counterexample:** The document belongs to the selected suborganization after the action. Confirm the target before enabling the workflow because suborganization access rules may differ.

This is an illustrative configuration and expected outcome. Use fields, users and groups configured in your test organization; it is not a claim that this example was executed.
