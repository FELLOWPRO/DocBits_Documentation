# Unit Price Combined with Fields

<figure><img src="../../../../.gitbook/assets/image (26) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to evaluate whether the unit price, when combined with a specified field value (such as quantity, discount, or additional charges), meets a defined condition. The card compares the unit price and field value to a specified threshold to help ensure that pricing aligns with expectations. This comparison can trigger actions based on specific conditions, such as flagging discrepancies or automating approval processes in procurement or receiving workflows.

## **Components of the Card:**

1. **Field Name**
   * **Description:** Specifies the document field that contains the value to be combined with the unit price.
   * **Detail:** This must match the exact identifier of the first field within the document.
2. **Operator**
   * **Description:** Defines the condition that will be applied to the comparison between the combined value and the specified value.
   * **Options:**
     * **Equals (=):** Checks if the combined value of the unit price and field matches the specified value.
     * **Not Equals (≠):** Ensures the combined value of the unit price and field is different from the specified value.
     * **Greater Than (>):** Verifies if the combined value is greater than the specified value.
     * **Greater or Equals (≥):** Checks if the combined value is greater than or equal to the specified value.
     * **Lesser Than (<):** Verifies if the combined value is less than the specified value.
     * **Lesser or Equals (≤):** Checks if the combined value is less than or equal to the specified value.
3. **Value**
   * **Description:** Specifies the value against which the combined unit price and field value will be compared.
   * **Detail:** The value has to be a numeric value.

## **Functionality:**

* **Condition Evaluation:** The system evaluates the combined unit price and field value based on the selected operator and compares it to the specified value. The result of this evaluation determines whether the condition is true or false.
* **Action Execution:**
  * **True Condition:** If the comparison results in true (e.g., the combined value exceeds the specified value), the workflow proceeds with the true condition. This might trigger actions such as approval, document routing, or applying processing rules.
  * **False Condition:** If the comparison results in false (e.g., the combined value does not meet the condition), the workflow proceeds with the false condition. This could trigger a notification, send the document for manual review, or stop the workflow.

## **Setup and Configuration:**

* Users begin by selecting the document field(s) that contains the value(s) to be combined with the unit price. After selecting the field, they then choose the appropriate operator to define how the combined value will be compared to the specified value. Then they can set the value.

## **Example Scenario:**

* An invoice lists 50 units of a product at $20 each, totaling $1000. The related document has a quantity field with a value of 10. Using the "Greater Than" operator, the card compares the combined value of the unit price ($20) and the quantity (10), which equals $200. The card checks if the combined value is greater than $150 (the specified value). Since the combined value of $200 is greater than the threshold of $150, the workflow proceeds to trigger an approval for the document.

## **Conclusion:**

The "Unit Price Combined with Fields" workflow card ensures that pricing conditions are met by evaluating the combined value of the unit price and a specified field. By automating this comparison, organizations can ensure consistency and flag discrepancies in pricing or quantities before proceeding with approval, helping to streamline procurement and financial processes.
