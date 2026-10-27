# Assign document to recipient

<figure><img src="../../../../../.gitbook/assets/image (374).png" alt="Assignee card Assign document to a recipient with a user as fallback" width="563"><figcaption></figcaption></figure>

## **Purpose:**

The **"Assign Document to Disponent / Purchaser"** workflow card assigns a document to either a **Disponent** or **Purchaser**. If no valid user is found, a fallback user is selected to ensure the document is always assigned to someone.

## **Components of the Card:**

1. **Disponent / Purchaser**
   * **Description:** Specifies whether the document will be assigned to a Disponent or Purchaser.
   * **Options:**
     * **Disponent:** Assign the document to the Disponent.
     * **Purchaser:** Assign the document to the Purchaser.
2. **Fallback User**
   * **Description:** Specifies a fallback user in case the document cannot be assigned to the selected Disponent or Purchaser.
   * **Detail:** The dropdown list of available users lets you choose a fallback user to ensure the document is assigned even if the primary user cannot be determined.

## **Functionality:**

* **Condition Evaluation:**\
  The card only executes its action if both the **"When"** and **"And"** evaluate as true.
* **Document Assignment:**\
  The card assigns the document to either the **Disponent** or **Purchaser** as selected. If the selected person is unavailable or not valid, the document is assigned to the fallback user.

## **Setup and Configuration:**

* **Select Disponent / Purchaser:**\
  Choose whether to assign the document to the **Disponent** or **Purchaser**.
* **Select Fallback User:**\
  Choose a fallback user from the dropdown list who will receive the document if the primary assignment is not possible.

## **Conclusion:**

The **"Assign Document to Disponent / Purchaser"** workflow card ensures the document is always assigned, either to the selected Disponent/Purchaser or, if needed, to the fallback user. This minimizes workflow disruptions and ensures document processing continues smoothly.

<!-- workflow-card-practical-example-20261021 -->

## Practical example

**When to use:** Assign a document to its resolved recipient, with a safe fallback.

**Configuration:** Select the recipient source and fallback user `Demo Reviewer A`.

**Expected result and counterexample:** A resolvable recipient receives the assignment. If the recipient cannot be resolved, the configured fallback is used. Verify both paths.

This is an illustrative configuration and expected outcome. Use fields, users and groups configured in your test organization; it is not a claim that this example was executed.
