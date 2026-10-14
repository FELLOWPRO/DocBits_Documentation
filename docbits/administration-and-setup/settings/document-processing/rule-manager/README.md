# Rule Management

<figure><img src="../../../../.gitbook/assets/rule_management.png" alt="Rule Management"><figcaption><p>Rule Management Page</p></figcaption></figure>

Rule Management allows you to create and manage TOML-based conflict resolution rules used during PO matching and document export. Each rule set defines how DocBits handles discrepancies between invoice data and purchase order data.

## Rule List

The main table shows all rule configurations:

| Column | Description |
|--------|-------------|
| **Name** | The rule set name. Items tagged **default** are system-provided templates. |
| **Description** | A summary of what the rule set handles. |
| **Last Modified By** | The user who last edited this rule set. |
| **Last Modified At** | Timestamp of the last change. |
| **Actions** | Three-dot menu to edit, copy, or delete. |

Click **+ New** to create a new rule set, or click an existing name to open the rule editor.

---

## Rule Structure Reference

This section provides an in-depth explanation of the conflict resolution rules used in the DocBits invoicing system. These rules are designed to automatically handle discrepancies between invoice details and purchase order (PO) data, ensuring accurate financial reconciliation. The system applies these rules to process invoice lines, charges, and taxes, and generates appropriate adjustments or notes when necessary.

## Structure of the Rules

### 1. Metadata

• version: Identifies the version of the mapping file.

• revision: Revision number for tracking changes.

• author: Indicates the creator of the mapping file.

• description: A brief description of the file’s purpose.

• created_at & updated_at: Timestamps for when the file was created and last updated.

### 2. Export Configuration

The export configuration section defines the mapping between the data fields in the system and the corresponding fields in the export files.

• Header: Defines the header fields for the exported invoice data.

• Tax Lines: Specifies the fields for tax line items in the export.

• Order Header Charges: Maps fields related to additional charges at the order header level.

• Receipt Lines: Maps fields for individual line items in a receipt.

• Order Line Charges: Defines the fields for charges related to specific order lines.

• Cost Lines: Specifies fields for cost allocation lines.

• Debit Note & Credit Note: Defines fields for generating debit and credit notes in cases of discrepancies.

### 3. Conflict Resolution Rules

These rules handle discrepancies between invoice data and the corresponding PO data. Each rule is composed of several components:

• Name: The rule’s descriptive name, indicating the type of discrepancy it addresses.

• Section: Indicates which part of the invoice (e.g., receipt_lines, line_charges) the rule applies to.

• Active: Boolean value (true or false) indicating if the rule is currently active.

• Match Criteria: Conditions that trigger the rule based on comparisons between actual invoice data and expected PO data.

• Actions: Defines what the system should do when the rule is triggered, including adjusting values, applying charges, or generating credit/debit notes.

## Common Elements in the Rules

### Comparison Operators

These operators define how the actual invoice values are compared to the expected PO values:

• equal

• greater than

• greater than or equal to

• less than

• less than or equal to

• within tolerance

• outside tolerance


### Approval Status

Indicates whether a discrepancy is approved or not:

• approved

• rejected

• any


### Action Types

Defines specific actions to take when a discrepancy is detected:

• receipt line

• cost line

• header charge

• line charge

• tax line

• debit note receipt line

• debit note cost line

• debit note header charge

• debit note line charge

• credit note receipt line

• credit note cost line

• credit note header charge

• credit note line charge

• credit note tax line


### Rule Examples

#### [Case 1, 2, 3: Quantity and Unit Price Within Tolerance](transactionconfig-pro-template/case-1-2-3-quantity-and-unit-price-within-tolerance.md)

• Purpose: Handles scenarios where both the quantity and unit price on the invoice are within the accepted tolerance limits compared to the PO.

• Action: The system accepts the invoice values and calculates the total amount.



#### [Case 4, 5: Quantity Within Tolerance, Unit Price Outside Tolerance (Approved)](./#case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved)

• Purpose: Applies when the quantity is within tolerance but the unit price is outside tolerance and has been approved.

• Action: The system adjusts the unit price to match the PO and applies any necessary line charges.



#### [Case 6: Quantity Within Tolerance, Unit Price Outside Negative Tolerance (Rejected)](transactionconfig-pro-template/case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

• Purpose: Deals with cases where the unit price is less than expected and outside the tolerance range, leading to rejection.

• Action: The system adjusts the unit price to match the PO, generates a credit note for the difference, and applies header charges as needed.


### Handling Charges and Taxes

### Charge Per Unit Tolerance

• Rules under this category handle discrepancies in charges per unit, with specific actions based on whether the charge is within or outside the tolerance and whether it is approved or rejected.

### Tax Line Adjustments

• These rules manage tax discrepancies by adjusting the tax lines or generating corresponding credit or debit notes based on the differences between invoice and PO tax data.

### Enums and Options

• Enums: Predefined lists of values ensuring consistency across the rules (e.g., comparison operators, approval types).

• Options: Predefined choices for handling quantities or unit prices, offering flexibility in rule definitions.

## Screenshots Explanation

### Screenshot 1: Rule Management Interface

<figure><img src="../../../../.gitbook/assets/rule_management_interface.png" alt="Rule Management Interface"><figcaption></figcaption></figure>

This screenshot shows the Rule Management interface where administrators can view and manage all conflict resolution rules. Key elements include:

• Add Rule Button: Allows adding new rules.

• List of Rules: Displays all active rules with details such as name, section, and active status.

• Section Dropdown: Filters the rules based on the section they apply to (e.g., Receipt Lines, Line Charges).

### Screenshot 2: Detailed Rule Editing

<figure><img src="../../../../.gitbook/assets/rule_detailed_editing.png" alt="Detailed Rule Editing"><figcaption></figcaption></figure>

his screenshot illustrates the detailed view of a specific rule being edited. Key elements include:

• Criteria Section: Defines the conditions under which the rule is triggered. For example, the criteria might specify that if the quantity and unit price differ from the PO but are within tolerance, the rule should be applied.

• Actions Section: Specifies what actions should be taken when the criteria are met. This can include adjusting the invoice lines, generating credit or debit notes, or applying additional charges.

• Document Type and Costing Elements: Allows the administrator to map specific actions to document types and costing elements, providing flexibility in handling different scenarios.