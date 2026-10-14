# TransactionConfig Pro Template

## Comprehensive Configuration Tool for Financial Document Processing

_TransactionConfig Pro Template_ is a powerful configuration tool designed for enterprise environments to manage the processing of financial documents, such as invoices, debit notes, and credit notes. The tool provides detailed mapping and field definitions that allow businesses to automate and customize their financial workflows with precision. Integrating seamlessly with existing Infor ERP systems, _TransactionConfig Pro Template_ ensures accurate handling of complex transactions while maintaining compliance with global financial standards.

### Key Features

• Detailed Mapping: Allows for precise mapping of fields across various transaction types, ensuring data consistency and accuracy.

• Customization: Supports customization of financial document workflows to meet specific business needs.

• Automation: Automates the handling of financial transactions, reducing manual errors and increasing efficiency.

• Integration: Easily integrates with existing Infor M3/LN ERP systems, enhancing the overall financial processing capabilities of the organization.

• Compliance: Ensures compliance with international financial standards and regulations, helping businesses manage global transactions effectively.



## Detailed Explanation of Conflict Resolution Cases

_TransactionConfig Pro Template_ includes a series of predefined rules to handle common discrepancies between invoice data and purchase order (PO) data. These rules are designed to automate decision-making when variances occur, ensuring consistency and accuracy in financial processing.

### [Case 1, 2, 3: Quantity and Unit Price Within Tolerance](case-1-2-3-quantity-and-unit-price-within-tolerance.md)

**Scenario:** Both the quantity and unit price on the invoice are within an acceptable tolerance range compared to the purchase order.

• **Action:** The system accepts the invoice values and calculates the total amount based on the provided quantity and unit price.

### [Case 4, 5: Quantity Within Tolerance, Unit Price Outside Tolerance (Approved)](case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md)

**Scenario:** The quantity on the invoice is within tolerance, but the unit price is outside tolerance, and this variance has been approved.

• **Action:** The system adjusts the unit price to match the purchase order and applies any necessary line charges to account for the difference.

### [Case 6: Quantity Within Tolerance, Unit Price Outside Negative Tolerance (Rejected)](case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

**Scenario:** The quantity is within tolerance, but the unit price is below the acceptable range (negative tolerance) and is not approved.

• **Action:** The system rejects the unit price, adjusts it to match the purchase order, and generates a credit note for the difference. Additional header charges may be applied as necessary.

### [Case 7: Quantity Within Tolerance, Unit Price Outside Tolerance (Positive Rejected)](case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md)

**Scenario:** The quantity is within tolerance, but the unit price exceeds the acceptable range (positive tolerance) and is not approved.

• **Action:** The system rejects the invoice unit price, adjusts it to match the purchase order, and may generate a debit note to account for the overcharged amount.

### [Case 8a, 9a: Quantity Outside Tolerance (Approved), Unit Price Within Tolerance](case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md)

**Scenario:** The quantity on the invoice is outside the acceptable tolerance but has been approved, while the unit price remains within tolerance.

• **Action:** The system accepts the approved quantity and the unit price as per the invoice and processes the transaction accordingly.

### [Case 11a: Quantity Outside Tolerance (Positive Rejected), Unit Price Within Tolerance](case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md)

**Scenario:** The quantity on the invoice exceeds the acceptable range (positive) and is rejected, but the unit price is within tolerance.

• **Action:** The system adjusts the quantity to the approved level, maintaining the unit price, and processes the transaction. Any excess quantity is rejected and not invoiced.

### [Case 10a: Quantity Outside Tolerance (Negative Rejected), Unit Price Within Tolerance](case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md)

**Scenario:** The quantity is below the acceptable range (negative tolerance) and is not approved, though the unit price is within tolerance.

• **Action:** The system adjusts the quantity to match the approved level, keeping the unit price consistent. The transaction is processed accordingly.

### [Case 8b, 9b: Quantity Outside Tolerance (Approved), Unit Price Outside Tolerance (Approved)](case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md)

**Scenario:** Both the quantity and unit price are outside the tolerance range but have been approved.

• **Action:** The system processes the transaction using the invoice values for both quantity and unit price, applying any necessary adjustments or line charges.

### [Case 10b: Quantity Outside Tolerance (Negative Rejected), Unit Price Outside Tolerance (Rejected)](case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md)

**Scenario:** Both the quantity and unit price are outside tolerance, and neither has been approved.

• **Action:** The system rejects the invoice data, adjusts the values to match the purchase order, and generates necessary debit or credit notes.

### [Case 11b: Quantity Outside Tolerance (Positive Rejected), Unit Price Outside Tolerance (Rejected)](case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md)

**Scenario:** The quantity exceeds the acceptable range (positive) and is rejected, and the unit price is also outside tolerance and rejected.

• **Action:** The system adjusts the quantity and unit price to match the approved levels from the purchase order, rejecting any excesses, and processes the transaction.

### [Case 12, 13: Charge Line - Charge Per Unit Within Tolerance](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**Scenario:** The charge per unit on the invoice is within the acceptable tolerance range compared to the purchase order.

• **Action:** The system accepts the charge per unit as invoiced and processes the transaction without adjustments.

### [Case 14: Charge Line - Charge Per Unit Outside Tolerance (Approved)](charge-per-unit-outside-tolerance-approved-1.md)

**Scenario:** The charge per unit is outside tolerance but has been approved.

• **Action:** The system accepts the charge per unit and applies the approved charges, processing the transaction accordingly.

### [Case 15: Charge Line - Charge Per Unit Outside Tolerance (Rejected)](charge-per-unit-outside-tolerance-rejected.md)

**Scenario:** The charge per unit is outside tolerance and has not been approved.

• **Action:** The system adjusts the charge per unit to match the purchase order or approved levels, generating any necessary debit or credit notes.

### [Case 12, 13: Header Charge - Charge Per Unit Within Tolerance](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**Scenario:** The header charge per unit is within the acceptable tolerance range compared to the purchase order.

• **Action:** The system processes the header charge as invoiced, applying it without adjustments.

### [Case 14: Header Charge - Charge Per Unit Outside Tolerance (Approved)](charge-per-unit-outside-tolerance-approved.md)

**Scenario:** The header charge per unit is outside tolerance but has been approved.

• **Action:** The system processes the approved charge per unit, applying it to the transaction.

### [Case 15: Header Charge - Charge Per Unit Outside Tolerance (Rejected)](case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md)

**Scenario:** The header charge per unit is outside tolerance and has not been approved.

• **Action:** The system adjusts the header charge to match the purchase order, processing the transaction accordingly, and generating any necessary notes.

### [tax-lines.md](tax-lines.md "mention")

**Scenario:** Handles discrepancies in tax amounts between the invoice and purchase order.

• **Action:** The system adjusts the tax lines according to the approved tax rates and amounts, ensuring compliance with applicable tax regulations.
