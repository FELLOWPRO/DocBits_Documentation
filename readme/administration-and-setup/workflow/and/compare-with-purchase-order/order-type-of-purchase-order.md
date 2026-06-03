# Order Type of Purchase Order

<figure><img src="../../../../.gitbook/assets/image (277).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to compare the order type of a purchase order against a specified value. The card checks whether the order type of the purchase order meets the specified condition (e.g., whether it equals, does not equal, is greater than, or meets another condition) to ensure that the purchase order is classified correctly. This comparison can trigger actions based on specific conditions, such as routing the order for further review or approval if discrepancies are found.

## **Components of the Card:**

1. **Any/All:**
   * **Description**: Defines whether the condition applies to any or all purchase orders being evaluated in the workflow.
   * **Options**:
     * **Any**: The condition is met if any one of the purchase orders matches the specified condition.
     * **All**: The condition is met only if all of the purchase orders meet the specified condition.
2. **Operator:**
   * **Description**: Defines the condition that will be applied to compare the order type against a specified value.
   * **Options**:
     * **Equals (=)**: Checks if the order type matches the specified value.
     * **Not Equals (≠)**: Ensures the order type is different from the specified value.
3. **Order Type:**
   * **Description**: Specifies the value to which the order type of the purchase order will be compared.
   * **Detail**: The value must match the order type or classification in the system.

## **Functionality:**

* **Condition Evaluation:** The system evaluates the order type of the purchase order against the specified condition using the selected operator. If the order type matches (or does not match) the specified value, the workflow proceeds accordingly.
* **Action Execution:**
  * **True Condition**: If the condition evaluates to true (e.g., the order type matches the specified value), the workflow will continue, possibly triggering additional actions or processing steps.
  * **False Condition**: If the condition evaluates to false (e.g., the order type does not match the specified value), the workflow will not continue.

## **Setup and Configuration:**

* Users configure the card by selecting the order type field of the purchase order and choosing the operator that defines how the order type will be compared. Then, they set the specified value and decide whether to apply the condition to any or all of the purchase order lines.

## **Example Scenario:**

* A purchase order has the order type "Standard." The workflow is configured to check if the order type is "Urgent." Using the "Equals" operator, the card compares the order type and finds that it does not match the specified value, triggering the workflow to send the order for review due to the mismatch.

## **Conclusion:**

The "Order Type of Purchase Order" workflow card ensures that purchase orders are classified correctly according to their specified order type. By automating the comparison of order types, organizations can ensure that purchase orders are processed according to their expected classifications, helping to enforce compliance and streamline procurement workflows.
