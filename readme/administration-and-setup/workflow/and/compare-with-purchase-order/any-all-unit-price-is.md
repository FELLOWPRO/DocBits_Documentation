# Any / All Unit Price is

<figure><img src="../../../../.gitbook/assets/image (274).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (273).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is used to compare the unit price in a document against the unit price in a purchase order, ensuring that prices align within defined tolerance levels. The comparison can trigger actions if the unit price does not meet expectations. **Version 4** adds more flexibility by allowing users to choose different entities for comparison, providing a deeper level of control over pricing and procurement processes.

## **Components of the Card:**

1. **Any / All:**
   * **Description**: Defines whether the condition applies to any or all instances where the unit price is compared.
   * **Options**:
     * **Any**: The condition is met if any unit price meets the specified comparison condition.
     * **All**: The condition is met only if all unit prices meet the specified comparison condition.
2. **Operator:**
   * **Description**: Defines the condition for comparing the unit price against the specified value.
   * **Options**:
     * **Equals (=)**: Verifies if the unit price matches the specified value.
     * **Not Equals (≠)**: Ensures the unit price is different from the specified value.
     * **Greater Than (>)**: Verifies if the unit price is greater than the specified value.
     * **Greater or Equals (≥)**: Verifies if the unit price is greater than or equal to the specified value.
     * **Lesser Than (<)**: Verifies if the unit price is less than the specified value.
     * **Lesser or Equals (≤)**: Verifies if the unit price is less than or equal to the specified value.

## **Additional Components in Version 4:**

**Comparison Type:**

* **Description**: Allows users to choose what entities will be compared in addition to the unit price.
* **Options**:
  * **Purchase Order to Document**: Compares the unit price in the purchase order with the unit price in the document.
  * **Received to Document**: Compares the received quantity to the unit price in the document.
  * **Purchase Order to Received**: Compares the unit price in the purchase order with the received quantity.

## **Functionality:**

* **Condition Evaluation:** The system compares the unit price in the document to the unit price in the purchase order (or other selected entity, in Version 4) based on the selected operator. If the comparison is true, the workflow proceeds according to the next steps, either triggering approval or stopping the process.
* **Action Execution:**
  * **True Condition**: If the condition evaluates to true (e.g., unit price in the document is greater than the specified value), the workflow will proceed with the true action (e.g., approval, document processing).
  * **False Condition**: If the condition evaluates to false (e.g., unit price in the document does not meet the comparison), the workflow will not  proceed.

## **Setup and Configuration:**

* **Version 3 Setup:** Users configure the card by selecting the unit price in the document, choosing the appropriate operator to define how the unit price will be compared to the specified value, and setting the value to compare against. Additionally, users select whether the condition applies to any or all instances of the unit price comparison.
* **Version 4 Setup:** In Version 4, users have the additional option to select the Comparison Type. This allows them to define the entities to compare, such as Purchase Order to Document, Received to Document, or Purchase Order to Received. This enhances the flexibility of the card to compare unit prices in more complex scenarios.

## **Example Scenario:**

*   **Version 3 Example:**&#x20;

    An invoice shows a unit price of $50. The related purchase order has a unit price of $45. The card compares the two unit prices using the "Greater Than" operator. Since the unit price in the document ($50) is greater than the unit price in the purchase order ($45), the workflow will trigger the true condition (e.g., send the document for review).
* **Version 4 Example:**\
  An invoice shows a unit price of $50, and the related purchase order authorized a unit price of $45. Additionally, the received quantity is 60 units. The card compares the received quantity to the document's unit price using the "Greater Than" operator. Since the received quantity (60) is greater than the unit price ($50), the workflow triggers the true condition, and the document is flagged for further review.

## **Conclusion:**

Version 3 of the "Unit Price Comparison" workflow card is designed to ensure that unit prices in documents align with those in purchase orders, triggering actions based on defined conditions. Version 4 extends this functionality by introducing more complex comparison options, such as comparing purchase orders to documents, received quantities to documents, and purchase orders to received quantities. This added flexibility allows organizations to handle more sophisticated pricing and procurement scenarios, improving control and accuracy in their workflows.
