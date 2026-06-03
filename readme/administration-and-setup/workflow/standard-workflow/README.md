# Standard Workflow

<figure><img src="../../../.gitbook/assets/DocBits-APWorkflow-Gronbach.drawio (1) (1).svg" alt=""><figcaption></figcaption></figure>

#### Overview of Workflow Components:

* **AP Invoice Email**: The process likely begins with an invoice received via email.
* **DocBits**: This tool might be used for initial document management tasks such as capturing and digitizing invoices.
* **Finance Review**: Invoices undergo a finance review where decisions are made regarding their validity and accuracy.

#### Steps in the Workflow:

1. **Initial Review**:
   * Invoices are received and initially processed using DocBits.
   * They are then reviewed by the finance team to ensure they are removed from the workflow if they are complete, or pushed forward for further processing.
2. **PO vs Non-PO Invoices**:
   * The workflow distinguishes between PO-related and non-PO invoices.
   * Non-PO invoices are routed for further approval or rejection based on predefined criteria like supplier ID, quantity, unit price, and item number.
3. **Matching and Mismatching**:
   * Invoices are checked against goods receipts to ensure that details match (like supplier ID and quantity).
   * If mismatches occur, the invoice is subject to further review and possibly rejection.
4. **Finance and Buyer Review**:
   * For PO-related invoices, a detailed matching process is conducted involving a buyer review.
   * Adjustments to purchase orders or goods receipts might be required.
5. **Final Decisions**:
   * Invoices that pass all checks are approved and integrated into financial systems for record-keeping.
   * Rejected invoices trigger notifications, and a new invoice may be requested by the buyer.
6. **Integration with Infor IDM & LN+M3**:
   * Approved invoices are likely sent to Infor's IDM for document management and LN for ledger noting.
   * This integration ensures that all financial records are up-to-date and that the workflow seamlessly feeds into the broader ERP system.

#### Decision Points:

* Throughout the workflow, there are various decision points where an invoice might be approved, rejected, or sent back for additional information. Notifications are sent out after delays, ensuring timely processing.

These Workflows will be included in the Standard Workflow
