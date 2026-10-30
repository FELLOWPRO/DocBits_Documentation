# Supplier on Invoice

<figure><img src="../../../../.gitbook/assets/image (276).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to compare the supplier information on an invoice against the supplier information on the related purchase order. The card ensures that the supplier on the invoice matches the supplier on the purchase order. This comparison helps verify that the correct supplier is invoicing for the order and can trigger actions based on any discrepancies.

## **Components of the Card:**

1. **Operator:**
   * **Description**: Defines the condition for comparing the supplier on the invoice to the supplier on the purchase order.
   * **Options**:
     * **Is**: Checks if the supplier on the invoice matches the supplier on the purchase order.
     * **Is Not**: Ensures that the supplier on the invoice does not match the supplier on the purchase order.

## **Functionality:**

* **Condition Evaluation:** The system compares the supplier on the invoice to the supplier on the purchase order based on the selected operator. If the comparison condition is true (e.g., the supplier is the same or different as required), the workflow will proceed accordingly.
* **Action Execution:**
  * **True Condition**: If the condition evaluates to true (e.g., the supplier on the invoice matches the supplier on the purchase order), the workflow continues without triggering any errors.
  * **False Condition**: If the condition evaluates to false (e.g., the supplier on the invoice does not match the supplier on the purchase order), the workflow will not continue.

## **Setup and Configuration:**

* Users choose the appropriate operator ("Is" or "Is Not") to define how the suppliers will be compared.

## **Example Scenario:**

* An invoice lists a supplier with the ID "SUP123" and the related purchase order also lists "SUP123" as the supplier. Using the "Is" operator, the card compares the suppliers and finds them to be the same, so the workflow proceeds without any issue.

## **Conclusion:**

The "Supplier Comparison" workflow card ensures that the correct supplier is invoicing for the purchase order, helping to prevent discrepancies and errors in the procurement process. By automatically verifying supplier information, organizations can streamline their invoice approval process and reduce the risk of fraud or errors in supplier billing.
