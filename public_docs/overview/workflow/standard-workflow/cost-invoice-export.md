# Cost Invoice - Export

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_export_4.png" alt="DocBits Aankoop Bestelling Exporteren 4"><figcaption></figcaption></figure>

This title indicates that the rule is specifically configured for managing cost invoices and involves an export action, possibly for reporting, further processing, or integration with other systems.

#### Rule Configuration:

1. **When…**
   * **Document Type is Invoice**: This condition ensures that the rule is triggered only for documents categorized as invoices, maintaining the workflow's specificity to invoice management.
2. **And…**
   * **Document Field Invoice Sub Type is Equals Cost Invoice**: This specifies that the rule applies only to those invoices that are explicitly marked as "Cost Invoices" in a particular field within the document. This helps in distinguishing them from other types of invoices.
   * **Document Status is Pending Second Approval**: The invoice must be in a "Pending Second Approval" status. This indicates that the invoice has already undergone an initial approval and is awaiting a second, possibly final, review.

#### Action (Then…):

* **Start Export**: Once the invoice meets the specified conditions (being a cost invoice and pending second approval), the action to "Start Export" is executed. This could involve sending the invoice data to another system for financial analysis, reporting, or compliance purposes.

#### Purpose of This Rule:

* **Workflow Efficiency**: This rule helps automate the handling of cost invoices by ensuring they are processed through the necessary approval stages without manual intervention, increasing the speed and accuracy of financial operations.
* **Control and Compliance**: By requiring a second approval, the system enforces a control mechanism that ensures cost invoices are thoroughly reviewed, enhancing financial oversight.
* **Integration and Reporting**: The export action suggests that once invoices are fully approved, they may be integrated into other systems for further processing or analysis, which is critical for financial reporting and audits.

This kind of rule is vital for organizations that deal with various types of invoices and need to ensure that each type is handled according to specific protocols. It reduces the risk of errors and ensures compliance with internal controls and external regulations.

