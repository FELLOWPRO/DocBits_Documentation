# Purchase Invoice - 2nd Approval Unit Price

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.55.09.png" alt=""><figcaption></figcaption></figure>

This title indicates that the rule is set up to manage the second approval phase of a purchase invoice, with a specific focus on validating the unit price.

#### Rule Configuration:

1. **When…**
   * **Document Type is Invoice**: This condition ensures that the rule is triggered only for documents that are identified as invoices, filtering out other document types and maintaining the relevance of the workflow.
2. **And…**
   * **Document Status is Pending Second Approval**: This specifies that the invoice is in the phase where it is awaiting a second approval. This is usually a step designed to ensure additional oversight before final processing.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: This further narrows down the application of this rule to only those invoices that are classified as "Purchase Invoices", distinguishing them from other invoice subtypes.
   * **Logic Unit Price in order confirmation Not Equals purchase order**: This logical check is crucial as it compares the unit price listed in the order confirmation against the unit price in the original purchase order. The action is triggered if these values do not match, which could indicate a discrepancy that needs resolution.

#### Action (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: If the conditions specified are met (i.e., there's a mismatch in unit prices), the invoice is automatically assigned to a buyer (the name specified in the 'Buyer Name' field) for further review. If the 'Buyer Name' field is empty or unspecified, a default user (likely an administrator or another designated staff member) is assigned as a fallback to handle the approval.

#### Purpose of This Rule:

* **Ensure Accuracy and Compliance**: This rule is critical in ensuring that the invoicing process is accurate and complies with agreed terms. By triggering a review when there is a discrepancy in unit prices, the system helps prevent financial errors or potential fraud.
* **Streamline Approvals**: Automating the assignment for review based on specific discrepancies helps streamline the approval process and ensures that issues are promptly addressed by the appropriate personnel.
* **Financial Oversight**: Requiring a second approval, especially based on price matching, reinforces financial controls and accountability within the organization.
