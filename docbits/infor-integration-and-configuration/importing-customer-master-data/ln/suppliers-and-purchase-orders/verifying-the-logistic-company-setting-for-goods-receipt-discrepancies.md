# Verifying the Logistic Company Setting for Goods Receipt Discrepancies

When working with large-scale procurement processes, it’s not uncommon to encounter situations where certain data points don’t align as expected. For example, you might see an error message like:

**“Delivery Note L1234, Order Type: Purchase, Order 100000211, Position 10, Subsequent Number 1, Logistic Company&#x20;**<mark style="color:red;">**XXXX**</mark>**, Goods Receipt WE0000293 and Entry Position 10 not found in direct debit.”**

This type of message often indicates that there’s a mismatch or missing information related to your logistic company configuration. The logistic company is a critical element in enterprise resource planning (ERP) systems, especially in complex supply chains spanning multiple legal or logistic entities.

**Why Does This Happen?**

In multi-entity environments, each transaction—purchasing, receiving goods, or initiating payments—must be correctly assigned to the right logistic company. The “logistic company” is more than just an identifier; it determines which warehouse, distribution center, or supply network node is responsible for the order and fulfillment tasks. If the company number doesn’t match the expected entity, downstream processes like goods receipt verification or direct debit settlements can fail.

## **Key Checks to Perform:**

### 1. Verify the Assigned Logistic Company:

Check the master data records to ensure the referenced logistic company (in this case, <mark style="color:red;">XXXX</mark>) is the correct entity for the given order. Is <mark style="color:red;">XXXX</mark> the right company code for handling purchases from this supplier or for this particular product line?

### 2. Review Purchase Order (PO) Setup:

Confirm that the purchase order’s logistic company aligns with your intended receiving location. Sometimes an order is created under one logistic company, but the goods are received under another if the setup isn’t consistent.

### 3. Cross-Reference Goods Receipt and Warehouse Records:

Look at the goods receipt (WE0000293) and ensure it was booked in the correct company’s warehouse. If the warehouse belongs to a different logistic company, you may need to correct the configuration or process a transfer to the right entity.

### 4. Check Integration and Master Data Consistency:

Integration points between different modules (Purchasing, Warehousing, Finance) rely on consistent codes. Ensure that the logistic company is uniformly defined across all relevant modules.

### 5. Consult Documentation and Support:

If internal checks fail to resolve the issue, consult your system documentation or reach out to your ERP support team. They can help verify if the logistic company code is set up correctly or if additional configuration steps are needed.

