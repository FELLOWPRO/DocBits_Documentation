# Purchase Invoice - 2nd Approval Quantity Export

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 15.00.53.png" alt=""><figcaption></figcaption></figure>

This title indicates that the rule is set up to manage the second approval phase for purchase invoices with an emphasis on the quantity details, ensuring that the quantities on the invoice match those on the original purchase order.

#### Rule Configuration:

1. **When…**
   * **Document Type is Invoice**: This condition ensures that the rule is activated only for documents identified as invoices, which is crucial for directing the workflow accurately.
2. **And…**
   * **Document Status is Pending Second Approval**: This specifies that the invoice is currently pending a second approval. This stage often provides additional oversight to ensure accuracy before the transaction is finalized.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: This condition further specifies that the rule applies only to invoices categorized specifically as "Purchase Invoices," differentiating them from other types of invoices.
   * **Logic Quantity in order confirmation Equals purchase order**: This condition checks if the quantity listed in the order confirmation matches the quantity in the purchase order. It ensures that the invoice processing only moves forward if the quantities are consistent, which is critical for inventory management and financial accuracy.

#### Action (Then…):

* **Start Export**: Once the invoice meets the specified conditions (i.e., the quantities match between the order confirmation and the purchase order), the action to "Start Export" is triggered. This likely involves exporting the invoice data for further processing, possibly to another financial system or for reporting purposes.

#### Purpose of This Rule:

* **Ensure Accuracy and Consistency**: By verifying that the quantities match between the order confirmation and the purchase order, the system helps maintain inventory accuracy and prevents discrepancies that could affect financial reporting or stock management.
* **Streamline Financial Processing**: Automating the export of data once the quantities are confirmed reduces manual handling and speeds up the financial processing cycle.
* **Enhance Compliance and Oversight**: Requiring a second approval for quantity verification adds an extra layer of oversight, crucial for compliance with financial policies and controls.

This rule is a clear example of how workflow automation can be effectively used to ensure precise and efficient handling of financial documents within an organization, particularly in the context of purchase processes that involve large volumes of transactions requiring meticulous validation.
