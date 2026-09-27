# Purchase Invoice - 2nd Approval Unit Price Export

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.59.02.png" alt=""><figcaption></figcaption></figure>

This title indicates that the rule is set up to manage the second approval phase of purchase invoices with a focus on the unit price, ensuring it matches the agreed terms.

#### Rule Configuration:

1. **When…**
   * **Document Type is Invoice**: This condition ensures that the rule is activated only for documents identified as invoices, which is crucial for directing the workflow accurately.
2. **And…**
   * **Document Status is Pending Second Approval**: This specifies that the invoice is awaiting a second approval. This stage often provides additional oversight to ensure accuracy before finalizing the transaction.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: This condition further specifies that the rule applies only to invoices categorized specifically as "Purchase Invoices," differentiating them from other types of invoices.
   * **Logic Unit Price in order confirmation Equals purchase order**: This condition checks if the unit price listed in the order confirmation matches the unit price in the purchase order. It ensures that the invoice processing only moves forward if there is consistency in pricing, which is critical for budgeting and financial reporting.

#### Action (Then…):

* **Start Export**: Once the invoice meets the specified conditions (i.e., the unit prices match between the order confirmation and the purchase order), the action to "Start Export" is triggered. This likely involves exporting the invoice data for further processing, possibly to another financial system or for reporting purposes.

#### Purpose of This Rule:

* **Ensure Accuracy and Consistency**: By verifying that the unit prices match between the order confirmation and the purchase order, the system helps maintain financial accuracy and prevents overcharging or undercharging.
* **Streamline Financial Processing**: Automating the export of data once the prices are confirmed reduces manual handling and speeds up the financial processing cycle.
* **Enhance Compliance and Oversight**: Requiring a second approval for price verification adds an extra layer of oversight, which is crucial for compliance with financial policies and controls.

This rule is an example of how workflow automation can be effectively utilized to ensure precise and efficient handling of financial documents within an organization, particularly in the context of large volumes of transactions that require meticulous validation.
