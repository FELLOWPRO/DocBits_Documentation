# Promised delivery date for line items in table with promised delivery date

<figure><img src="../../../../../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure>

## Purpose:

This workflow card is designed to validate the **promised delivery date of line items** against the **promised delivery date on the purchase order**, using comparison operators and configurable tolerance rules. It allows workflows to automatically detect compliant, early, or late delivery dates and react accordingly.

## Components of the Card:

1. **Operator**
   * **Description:**\
     Defines how the line item promised delivery date is compared to the purchase order promised delivery date.
   * **Options:**
     * **Equals (=):** The line item date must fall within the tolerance window.
     * **Not Equals (≠):** The line item date must fall outside the tolerance window.
     * **Greater Than (>):** The line item date must be after the tolerance window.
     * **Greater or Equals (≥):** The line item date must be on or after the start of the tolerance window.
     * **Lesser Than (<):** The line item date must be before the tolerance window.
     * **Lesser or Equals (≤):** The line item date must be on or before the end of the tolerance window.<br>
2. **Tolerance Days**
   * **Description:**\
     Specifies the number of days used to calculate the acceptable tolerance window around the purchase order promised delivery date.
   * **Detail:**\
     This value is an integer and defines how many days before and after the purchase order date are considered during validation.<br>
3. **Allowed Tolerance Days**
   * **Description:**\
     Defines which weekdays are counted when calculating tolerance days.
   * **Detail:**\
     Users can select specific weekdays (for example, Monday to Friday). Only the selected days are included when calculating the tolerance window.

### Functionality:

* **Condition Evaluation:** The system calculates a tolerance window around the purchase order promised delivery date based on the configured **Tolerance Days** and **Allowed Tolerance Days**.\
  Each line item’s promised delivery date is then compared to this window using the selected operator.
* Action Execution:
  * **True Condition:** If the delivery date difference is within the tolerance range and matches the condition set by the operator, the workflow proceeds.
  * **False Condition:** If the condition is not met, the workflow will not continue.

### Setup and Configuration:

* Select the appropriate comparison operator.
* Enter the number of tolerance days.
* Choose which weekdays should be counted as tolerance days.

### Conclusion:

The **Compare with Purchase Order – Promised Delivery Date for Line Items** workflow card provides a flexible way to enforce delivery date rules. By combining operators with weekday-aware tolerance handling, it enables precise validation of delivery commitments while reducing manual checks and exceptions.
