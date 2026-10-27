# Set Checkbox to

<figure><img src="../../../../../.gitbook/assets/image (355).png" alt="Workflow document field card: set checkbox for a field name to a boolean value" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to set a checkbox field to a specified value (true or false) based on the conditions defined in the **"When"** and **"And"** sections. It provides a simple yet effective way to automate checkbox updates when certain criteria are met, ensuring streamlined document processing.

## **Components of the Card:**

1. **Field Name:**
   * **Description**: Specifies the field where the checkbox will be set.
   * **Detail**: The checkbox field to be updated is identified by the field name.
2. **Boolean**
   * **Description**: Defines the value that the checkbox field will be set to when the conditions in the **Where** and **And Sections** are both true.
   * **Options**:
     * **True**: The checkbox will be set to **true** if the conditions are met.
     * **False**: The checkbox will be set to **false** if the conditions are met.

## **Functionality:**

* **Condition Evaluation**: The system evaluates the conditions in both the **"When"** and **"And"**
* **Action Execution**: If both the **"When"** and **"And"** evaluate to true, the checkbox field will be updated to the specified value (true or false). If either condition is false, no actions are taken, and the checkbox remains as it was.

## **Setup and Configuration:**

To configure this card, users need to:

1. **Specify the target checkbox field** that will be set to true or false when the conditions are met.
2. **Choose the value (true or false)** that the checkbox will be set to upon condition evaluation.
3. The card only executes its action if both conditions in the **"When"** and **"And"** are evaluated as true.

## **Conclusion:**

The **"Set Checkbox"** workflow card is a simple and effective automation tool to update checkbox fields based on specific conditions. By ensuring both **"When"** and **"And"** are met, it allows users to automate processes and reduce manual intervention, ensuring smoother and more efficient document processing.

<!-- workflow-card-practical-example-20261021 -->

## Practical example

**When to use:** Mark a successful validation with an explicit flag.

**Configuration:** Select checkbox field `review_complete` and set it to `true`.

**Expected result and counterexample:** The field becomes checked. Run the action with `false` in a separate test when you need to clear the flag.

This is an illustrative configuration and expected outcome. Use fields, users and groups configured in your test organization; it is not a claim that this example was executed.
