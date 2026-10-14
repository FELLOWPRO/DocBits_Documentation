# Above Max Amount

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.51.42.png" alt=""><figcaption></figcaption></figure>

This title indicates that the rule is designed to manage cases where the invoice total is greater than the maximum amount an approver is authorized to handle.

#### Rule Configuration:

1. **When…**
   * **Document Type is Invoice**: This condition ensures that the rule applies only to invoices, which is essential for directing the workflow correctly.
2. **And…**
   * **Document Status is Pending Approval**: The invoice must be in a "Pending Approval" status. This status is crucial to ensure that the rule is applied to invoices that are still being processed and have not yet been finalized.
   * **Compare two fields: Total Amount Greater Than Approver Max Amount**: This condition checks if the invoice's total amount exceeds the maximum amount an approver is allowed to handle. This comparison might also include a tolerance setting, allowing for minor variations based on predefined criteria.

#### Action (Then…):

* **Assign user from field Next Level Approver, use user User as fallback**: If the invoice exceeds the specified maximum amount, it is automatically assigned to a higher-level approver, indicated by the 'Next Level Approver' field. If this field is not filled or the specified user is unavailable, a default user (likely an admin or another designated staff member) is used as a fallback to ensure the invoice is reviewed without delay.

#### Interface Elements:

* **Add Card**: This option allows additional conditions or actions to be added to the rule, providing flexibility to address complex scenarios.
* **Save**: This button saves the rule configuration to the system.

#### Purpose of This Rule:

The purpose of this rule is to ensure that invoices which exceed certain financial thresholds are reviewed by approvers with the appropriate authorization levels. This helps in maintaining financial control and oversight, ensuring that expenditures are reviewed by personnel with the requisite approval limits, thereby safeguarding the organization against unauthorized or inappropriate expenditures.

This rule, like the previous one, helps automate the workflow, reducing manual effort and enhancing compliance with the organization's financial policies. It is an example of how workflow automation can be effectively used to manage complex financial processes within a company.
