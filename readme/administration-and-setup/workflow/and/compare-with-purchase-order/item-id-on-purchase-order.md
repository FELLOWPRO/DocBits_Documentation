# Item Id on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to compare item IDs between a purchase order and a related document to ensure that the correct items are included. The card evaluates whether the item ID in the purchase order matches the item ID in the document. This comparison can trigger actions if discrepancies are found, ensuring that the items in the document align with the purchase order.

## **Components of the Card:**

1. **Any / All:**
   * **Description**: Defines whether the condition applies to any or all instances of item ID comparisons.
   * **Options**:
     * **Any**: The condition is met if any item ID in the purchase order matches the item ID in the document.
     * **All**: The condition is met only if all item IDs in the purchase order match the item IDs in the document.
2. **Operator:**
   * **Description**: Defines the condition for comparing the item ID on the purchase order to the item ID on the document.
   * **Options**:
     * **Equals (=)**: Verifies if the item ID in the purchase order exactly matches the item ID in the document.
     * **Not Equals (≠)**: Ensures that the item ID in the purchase order does not match the item ID in the document.

## **Functionality:**

* **Condition Evaluation:** The system compares the item ID in the purchase order to the item ID in the document based on the selected operator. If the comparison condition is true (e.g., item IDs match or do not match), the workflow will proceed accordingly.
* **Action Execution:**
  * **True Condition**: If the condition evaluates to true (e.g., the item ID in the purchase order equals the item ID in the document), the workflow will proceed with the true action (e.g., approval or further processing).
  * **False Condition**: If the condition evaluates to false (e.g., the item ID in the purchase order does not match the item ID in the document), the workflow will not proceed.

## **Setup and Configuration:**

* Users configure the card by selecting the item ID in both the purchase order and the document. They then choose the appropriate operator (Equals or Not Equals) to define how the item IDs will be compared. Lastly, users select whether the condition applies to any or all of the item IDs in the comparison.

## **Example Scenario:**

* An invoice lists an item with ID "ABC123" and the related purchase order also includes an item with ID "ABC123". Using the "Equals" operator, the card compares the item ID in the document with the item ID in the purchase order. Since the item IDs match, the workflow continues without issue

## **Conclusion:**

The "Item ID Comparison" workflow card ensures that the item IDs in documents align with those in purchase orders. This helps prevent discrepancies in item listings and ensures that the correct items are processed according to the purchase order. The ability to compare based on any or all instances provides flexibility in different use cases, improving the accuracy and efficiency of procurement workflows.
