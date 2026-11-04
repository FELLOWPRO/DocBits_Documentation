# Less than Max Amount

<figure><img src="../../../../.gitbook/assets/docbits_invoice.png" alt="DocBits Factuur"><figcaption></figcaption></figure>

This title suggests that the rule or condition being set up is designed to handle invoices where the total amount is less than or equal to a specified maximum amount.

#### Rule Configuration:

1. **When…**
   * **Document Type is Invoice**: This condition checks if the document being processed is an invoice. This is crucial for ensuring that the rule only applies to invoices and not other types of documents.
2. **And…**
   * **Document Status is Pending Approval**: This specifies that the invoice must be in a "Pending Approval" status. This status check ensures that the rule applies only to invoices awaiting approval.
   * **Compare two fields: Total Amount Less Or Equals Approver Max Amount**: This condition compares the total amount of the invoice to an approver's maximum authorized amount. If the invoice's total amount is less than or equal to this max amount, the rule continues to the next step. This likely includes a tolerance level that allows for minor deviations within specified limits.

#### Action (Then…):

* **Assign user from field Approver Name, use user User as fallback**: If the conditions specified are met, the invoice is automatically assigned to an approver whose name is specified in a field. If this field is empty or unavailable, a default user (likely an admin or another designated staff member) is assigned as a fallback to handle the approval.

#### Interface Elements:

* **Add Card**: This button likely allows users to add more conditions or actions to the rule, enhancing the flexibility and specificity of the workflow.
* **Save**: Saves the configured rule to the system.

#### Purpose of This Rule:

This setup is designed to streamline the approval process for invoices by automatically directing invoices to the appropriate approver based on the amount and ensuring that only those within a certain threshold are handled in this automated way. It helps in managing financial controls and speeds up the workflow by reducing manual checks for each invoice.

\

