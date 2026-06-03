# Compare Order Confirmation with Purchase order

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (267).png" alt="" width="563"><figcaption></figcaption></figure>

## Purpose:

This DocBits card is designed to compare a specific order data field—such as quantity, discount, or unit price—between an order confirmation and a purchase order. By allowing a focused comparison of one field at a time, it ensures precision in validating key data points, maintaining order accuracy. **Version 4** expands this functionality by allowing comparisons between different entities such as the purchase order, received quantities, and the document itself, adding more flexibility and control to the workflow.

## Components of the Card:

1. **Any/All**&#x20;
   * **Description:** Determines whether the condition applies to any or all lines in the order confirmation.\
     **Options:**
     * **Any**: The comparison will trigger if the selected field value in any line of the order confirmation matches the corresponding value in the purchase order.
     * **All**: The comparison will trigger only if the selected field value in all lines of the order confirmation matches the corresponding value in the purchase order.
2. **Order Data Field**
   * **Description**: Specifies the data field to be compared between the order confirmation and the purchase order.
   * **Detail**: Users can select one of the following fields for comparison:
     * **Quantity**: Compares the quantity ordered with the confirmed quantity.
     * **Discount**: Validates that the discount in the confirmation matches the purchase order.
     * **Unit Price**: Ensures that the unit price in the confirmation aligns with the purchase order.
3. **Operator**
   * **Description**: Defines the condition applied to the comparison of the selected data field.
   * **Options**:
     * **Equals (=)**: Confirms that the value matches the purchase order.
     * **Not Equals (≠)**: Ensures the value is different from the purchase order.
     * **Greater Than (>)**: Verifies that the value exceeds the purchase order’s value.
     * **Greater or Equals (≥)**: Confirms that the value equals or exceeds the purchase order’s value.
     * **Less Than (<)**: Checks that the value is below the purchase order’s value.
     * **Less or Equals (≤)**: Confirms that the value is below or equals the purchase order’s value.

## **Additional Components in Version 4**:

* **Comparison Type**: Selects the entities to compare. The options include:
  * **Purchase Order to Document**: Compares the purchase order data with the related document.
  * **Received to Document**: Compares the received data (e.g., quantities received) with the document.
  * **Purchase Order to Received**: Compares the purchase order data with the received quantities.

## Functionality:

* **Field Comparison**: The system compares the selected order data field (Unit Price, Discount, or Quantity) from the order confirmation to the corresponding value in the purchase order.
* **Action Execution**: Based on the comparison result and operator condition, the card can trigger follow-up actions, such as notifications or alerts.

## Example Scenario:

* An order confirmation specifies a **unit price** of $50, while the purchase order states $45. Using the "Greater Than" operator, the card flags the discrepancy, enabling the procurement team to address it before processing.

## Conclusion:

This card simplifies the validation of individual order data fields, ensuring compliance with purchase order terms. By isolating one field at a time for comparison, it supports targeted reviews and error prevention in order processing.
