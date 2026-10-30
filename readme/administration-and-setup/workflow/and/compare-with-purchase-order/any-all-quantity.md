# Any / All Quantity

<figure><img src="../../../../.gitbook/assets/image (269).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (270).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to compare the quantity in a document against the tolerance defined in the purchase order. It allows users to evaluate if the quantity meets certain conditions, such as equality or exceeding the specified tolerance. In Version 4, the card extends functionality by adding the ability to compare multiple entities, including the purchase order, received quantities, and document quantities, offering greater flexibility in handling different scenarios.

## **Components of the Card:**

1. **Any / All:**
   * **Description**: Specifies how the comparison should be applied across multiple items or conditions.
   * **Options**:
     * **Any**: At least one of the conditions must be true for the action to be triggered.
     * **All**: All conditions must be true for the action to proceed.
2. **Operator:**
   * **Description**: Defines the condition that will be applied to compare the document quantity against the specified tolerance.
   * **Options**:
     * **Equals (=)**: Checks if the quantity matches the specified tolerance value.
     * **Not Equals (≠)**: Ensures the quantity is different from the specified tolerance value.
     * **Greater Than (>)**: Verifies if the quantity is greater than the specified tolerance.
     * **Greater or Equals (≥)**: Checks if the quantity is greater than or equal to the specified tolerance.
     * **Lesser Than (<)**: Verifies if the quantity is less than the specified tolerance.
     * **Lesser or Equals (≤)**: Checks if the quantity is less than or equal to the specified tolerance.
3. **Tolerance Amount:**
   * **Description**: Specifies the tolerance value that the document quantity will be compared against.
   * **Detail**: This value is numeric and represents the threshold of allowed variance in the quantity
4. **Tolerance Type:**
   * **Description**: Defines the type of tolerance that will be applied.
   * **Options**:
     * **Percentage**: Tolerance is calculated as a percentage of the purchase order quantity.
     * **Value**: Tolerance is specified as a fixed numeric value.

## **Additional Components in Version 4:**

* **Comparison Type**: Selects the entities to compare, providing more flexibility in how the quantities are evaluated in Version 4.
  * **Purchase Order to Document**: Compares the quantity in the purchase order to the quantity in the related document.
  * **Received to Document**: Compares the received quantity to the quantity in the document.
  * **Purchase Order to Received**: Compares the purchase order quantity to the received quantity.

## **Functionality:**

* **Condition Evaluation:** The system compares the quantity in the document against the tolerance in the purchase order based on the selected operator and tolerance amount/type. In Version 4, the **Comparison Type** allows for different quantities to be compared, such as purchase order to received, or purchase order to document, providing a more dynamic comparison.
* **Action Execution:**
  * **True Condition**: If the comparison results in true (e.g., the document quantity is within the acceptable tolerance range), the workflow will proceed.
  * **False Condition**: If the comparison results in false (e.g., the quantity does not meet the tolerance), the workflow will not proceed.

## **Setup and Configuration:**

**Version 3:**

* Users configure the card by selecting the document quantity, defining the tolerance amount and tolerance type, and choosing the appropriate operator to compare the quantity against the tolerance. The card evaluates whether the quantity is within the tolerance threshold and proceeds with the "True" or "False" action based on the result.

**Version 4:**

* In addition to the configuration in Version 3, users can select the **Comparison Type**, allowing comparisons between different entities, such as:
  * **Purchase Order to Document**
  * **Received to Document**
  * **Purchase Order to Received**

## **Example Scenario:**

An invoice shows that 100 units were delivered, but the purchase order only authorized 90 units. The tolerance amount is set at 10 units, and the tolerance type is absolute.

* **Version 3**: The card compares the 100 units in the document against the purchase order's tolerance of 90 units. If the quantity exceeds the tolerance, the card flags the discrepancy for further review.
* **Version 4**: The card could compare the **purchase order quantity** (90 units) to the **received quantity** (100 units) or the **document quantity** (100 units). Depending on the selected **Comparison Type**, it checks if the difference between the two entities exceeds the tolerance and triggers the corresponding action.

## **Conclusion:**

* **Version 3**: This workflow card compares the document quantity with the purchase order tolerance, helping to ensure that discrepancies in quantity are flagged and handled appropriately.
* **Version 4**: Extends this functionality by allowing users to compare different entities, such as purchase order to received or purchase order to document, providing greater flexibility in handling more complex scenarios. Version 4 ensures tighter control over procurement and receiving workflows, offering more dynamic comparisons and actions based on the chosen comparison type.
