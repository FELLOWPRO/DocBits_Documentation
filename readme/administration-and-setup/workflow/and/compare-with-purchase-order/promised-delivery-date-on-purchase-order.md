# Promised Delivery Date on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose**

This DocBits card is designed to facilitate the precise comparison of promised delivery dates on purchase orders with delivery dates specified for line items in a table. By integrating a tolerance value, the card ensures flexibility in monitoring delivery timelines, helping maintain inventory planning accuracy and customer satisfaction.

## **Components of the Card**

1. **Operator**
   * **Description:** Defines the condition applied to compare delivery dates.
   * **Options:**
     * **Equals (=):** Checks if the promised delivery date on the line item matches the purchase order’s delivery date.
     * **Not Equal (≠):** Ensures the promised delivery date on the line item does not match the date on the purchase order.
     * **Greater Than (>):** Verifies if the line item’s promised delivery date is later than the purchase order’s delivery date.
     * **Greater or Equals (≥):** Checks if the line item’s promised delivery date equals or is later than the purchase order’s delivery date.
     * **Less Than (<):** Confirms if the line item’s promised delivery date is earlier than the purchase order’s delivery date.
     * **Less or Equals (≤):** Validates if the line item’s promised delivery date equals or is earlier than the purchase order’s delivery date.
2. **Value**
   * **Description:** Specifies an allowable margin of error in the delivery date comparison.
   * **Detail:** Users define the number of days by which the line item delivery date can differ from the promised delivery date.

## **Functionality**

* **Condition Evaluation:**\
  The card calculates the difference between the purchase order's promised delivery date and the delivery dates for line items in the table. The selected operator is then applied to determine if the condition is met.
* **Action Execution:**
  * **True Condition:** If the delivery date difference is within the tolerance range and matches the condition set by the operator, the workflow proceeds.
  * **False Condition:** If the condition is not met, the workflow will not continue.

## **Setup and Configuration**

* The operator is selected to define the desired comparison condition, such as equal to, greater than or less than. Finally, users specify a tolerance value in days, which allows for small variations in the comparison without triggering alerts.

## **Example Scenario**

* A purchase order specifies a promised delivery date of December 1st. A line item in the table has a promised delivery date of December 3rd. With a tolerance value set to 2 days and the **Equals (≥)** operator selected, the card considers the delivery date within the acceptable range. No alert is triggered, ensuring minor variances are tolerated without disrupting operations.

## **Conclusion**

The "Promised Delivery Date Comparison" card helps streamline supply chain operations by enabling precise monitoring of delivery timelines. With its ability to incorporate tolerances and flexible comparison operators, it ensures adherence to delivery expectations while avoiding unnecessary alerts for minor deviations. This enhances vendor management and overall workflow efficiency.
