# Combined Price of Quantity Difference

<figure><img src="../../../../.gitbook/assets/image (17) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (21) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose**:

This workflow card evaluates the combined price of a quantity difference, comparing it against a specified value. It helps automate actions based on price and quantity discrepancies across related documents, improving procurement and receiving workflows. **Version 4** expands this functionality by allowing comparisons between different entities such as the purchase order, received quantities, and the document itself, adding more flexibility and control to the workflow.

## **Components of the Card**:

1. **Operator**:&#x20;
   * **Description:** The condition for comparing the combined price against a specified value.
   * **Options:**
     * **Equals (=)**: Checks if the combined price matches the specified value.
     * **Not Equals (≠)**: Ensures the combined price is different from the specified value.
     * **Greater Than (>)**: Verifies if the combined price is greater than the specified value.
     * **Greater or Equals (≥)**: Checks if the combined price is greater than or equal to the specified value.
     * **Lesser Than (<)**: Verifies if the combined price is less than the specified value.
     * **Lesser or Equals (≤)**: Checks if the combined price is less than or equal to the specified value
2. **Value**:&#x20;
   * **Description:** Specifies the value against which the combined  price of quantity value will be compared.
   * **Detail:** The value has to be a numeric value.

## **Additional Components in Version 4**:

* **Comparison Type**: Selects the entities to compare. The options include:
  * **Purchase Order to Document**: Compares the quantities and prices between the purchase order and the related document.
  * **Received to Document**: Compares the received quantities to the quantities in the document.
  * **Purchase Order to Received**: Compares the purchase order quantities to the received quantities.

## **Functionality**:

* **Condition Evaluation**: Calculates the combined price by multiplying the quantity difference by the price per unit and compares it against the specified value using the selected operator.\
  **Version 4** adds the option to compare additional entities based on the user’s configuration, such as purchase order to received or purchase order to document.
* **Action Execution**: Based on whether the combined price meets the specified condition, the workflow will continue with true or false conditions to trigger actions or halt the workflow. **Version 4** also allows for more dynamic action execution, where the condition type (e.g., purchase order to received) influences the next step.

## **Setup and Configuration**:

* **Version 3**: Users configure the card by selecting the document fields for the quantity difference and price per unit. The operator is then chosen to define how the combined price will be compared to the specified value. Finally, users set the continue condition (true or false), which dictates the next step in the workflow.
* **Version 4**: In addition to the configuration in **Version 3**, users have an additional option to configure the **Comparison Type**. This defines what entities will be compared, such as **Purchase Order to Document**, **Received to Document**, or **Purchase Order to Received**.

## **Example Scenario**:

* An invoice shows 50 units of a product at $100 each, totaling $5000. The related purchase order authorized a purchase of $4500 for 45 units. The quantity difference is 5 units, and the combined price of the difference is $500. The card compares the purchase order quantity (45 units) to the received quantity (50 units) and checks if the combined price is greater than $400 (the specified value). Using the **Greater Than (>)** operator, the card identifies the discrepancy and flags it for review by the finance team.

## **Conclusion**:

**Version 3** of the "Combined Price of Quantity Difference" workflow card offers a straightforward approach for comparing quantity discrepancies and triggering actions based on price thresholds.\
**Version 4** extends this functionality by allowing comparisons between different entities (purchase order, received, document), providing more flexibility and control over the workflow. Organizations can now automate more complex scenarios and enforce tighter control over their procurement and receiving processes.
