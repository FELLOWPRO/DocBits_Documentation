# Out of Tolerance Unit Price

<figure><img src="../../../../.gitbook/assets/image (272).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to evaluate whether the combined value of unit prices and a specified field exceeds or falls short of a defined threshold. It helps identify any discrepancies where the unit prices, when combined with other fields, are out of tolerance, ensuring that pricing conditions meet expectations and flagging any issues for review or further action.

## **Components of the Card:**

1. **Field Name:**
   * **Description**: Specifies the document field that contains the value to be combined with the unit price.
   * **Detail**: The value in this field will be combined with the unit price to create the total combined value for comparison.
2. **Operator:**
   * **Description**: Defines the condition for comparing the combined value of the unit price and the field value against the specified value.
   * **Options**:
     * **Equals (=)**: Verifies if the combined value of the unit price and the field matches the specified value.
     * **Not Equals (≠)**: Ensures the combined value of the unit price and the field is different from the specified value.
     * **Greater Than (>)**: Verifies if the combined value of the unit price and the field exceeds the specified value.
     * **Greater or Equals (≥)**: Verifies if the combined value of the unit price and the field is greater than or equal to the specified value.
     * **Lesser Than (<)**: Verifies if the combined value of the unit price and the field is less than the specified value.
     * **Lesser or Equals (≤)**: Verifies if the combined value of the unit price and the field is less than or equal to the specified value.
3. **Value:**
   * **Description**: Specifies the value against which the combined unit price and field value will be compared.
   * **Detail**: This numeric value represents the threshold for comparison. If the combined value of the unit price and field exceeds or falls short of this value (based on the selected operator), the condition will trigger the specified actions.

## **Functionality:**

* &#x20;**Condition Evaluation:** The system calculates the combined value by multiplying or adding the unit price with the field value, depending on the configuration. The result is then compared to the specified value using the selected operator. If the condition is met (i.e., the combined value is out of tolerance), the workflow proceeds with the next step, whether that’s approval, rejection, or further review.
* **Action Execution:**
  * **True Condition**: If the comparison results in true (i.e., the combined value meets the condition), the workflow triggers the action associated with the true condition (e.g., approval or notification).
  * **False Condition**: If the comparison results in false (i.e., the combined value does not meet the condition), the workflow will not proceed.

## **Setup and Configuration:**

* Users select the field that contains the value to be combined with the unit price. Next, they choose the appropriate operator to determine how the combined value will be compared to the specified value. Finally, the user sets the value that the combined price will be compared to.

## **Example Scenario:**

* An invoice lists 50 units of a product at $30 each, totaling $1500. The related document has a quantity field with a value of 10. The combined price is calculated by multiplying the unit price ($30) and the quantity (10), resulting in $300. The card then compares this combined value to a threshold of $250. Using the “Greater Than” operator, the card identifies that $300 is greater than $250, triggering an approval process for the document.

## **Conclusion:**

The "Out of Tolerance Unit Prices Combined with Fields" workflow card helps ensure that pricing and field values are in alignment with business rules. By automating this check, organizations can identify discrepancies early in the process, ensuring that any out-of-tolerance unit prices are flagged for review or necessary action.
