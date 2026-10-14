# Workflow Example: Conditional Export Trigger

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_7.png" alt="DocBits Workflow Aankoop Bestelling 7"><figcaption></figcaption></figure>

This workflow outlines the conditions under which an export process should be initiated. It ensures that only documents meeting all specified criteria are processed for export, enhancing data integrity and alignment with business rules.

### When:

* A document within the system is evaluated for export eligibility.

### Logic:

1. **Document Type Check**
   * The document must be of a certain type (e.g., "Invoice" or "Receipt"). Specify the document type that qualifies for the export process.
2. **Status Verification**
   * The document's current status must meet predefined criteria (e.g., "Approved" or "Ready for Export") indicating it is ready for further processing.
3. **Contextual Conditions**
   * Additional checks are performed to ensure the document's details align with specific requirements. These checks might involve verifying information within order confirmations or purchase orders. Specify the particular conditions that need to be met. For example:
     * All items listed in the order confirmation match those in the purchase order.
     * The total amount in the order confirmation matches the total amount in the purchase order.
     * The delivery dates specified in the order confirmation align with those in the purchase order.

### Then:

#### Action:

* **Initiate Export**
  * If all the above conditions are satisfied, the system automatically starts the export process for the document.
  * This may involve generating an export file, sending data to an external system, or triggering a workflow in another application.

#### Implementation Example:

```yaml
rules:
  - description: "Conditional Export Trigger"
    conditions:
      - type: "DocumentType"
        criteria: "<SpecifyDocumentType>"
      - type: "Status"
        criteria: "<SpecifyStatus>"
      - type: "DetailMatch"
        criteria:
          - "ItemMatch"
          - "AmountMatch"
          - "DateMatch"
    actions:
      - operation: "StartExport"
```
