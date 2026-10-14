# Invoice Automation Testing with DocBits

## Overview

This document outlines the testing plan for invoice automation using DocBits with Infor LN or M3. It includes details of test cases, testing preparation, execution steps, and support processes.

## Testing Cases

| ID | Testing Case                                                               | Description                                                                                                                                                       | Status       |
| -- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| 1  | Cost Invoices                                                              | Invoices with no purchase order are processed successfully in DocBits and exported to LN as “cost invoice”.                                                       | TO BE TESTED |
| 2  | Purchase Order Related Invoice with Perfect Matching                       | Purchase order-related invoices are processed successfully in DocBits with a perfect match from invoice to PO, since item number, quantity, and unit price match. | TO BE TESTED |
| 3  | Purchase Order Related Invoices with Different Quantity                    | Purchase order-related invoices are processed in DocBits but in the PO matching module, we have a mismatch on the quantity.                                       | TO BE TESTED |
| 4  | Purchase Order Related Invoices with Different Unit Price                  | Purchase order-related invoices are processed in DocBits but in the PO matching module, we have a mismatch on the unit price.                                     | TO BE TESTED |
| 5  | Purchase Order Related Invoices with Different or Non-Existing Item Number | Purchase order-related invoices are processed in DocBits but in the PO matching module, we have a mismatch or a non-existing item number.                         | TO BE TESTED |
| 6  | Purchase Order Related Invoices with a Mismatch within Tolerance           | Purchase order-related invoices are processed in DocBits but in the PO matching module, we have a mismatch on quantity or unit price, but it’s within tolerance.  | TO BE TESTED |
| 7  | Credit Notes                                                               | Credit notes are successfully processed in DocBits and exported to LN. Clarify whether amounts should be exported with a positive or negative sign.               | TO BE TESTED |

## Plan for Testing with Customer

### 1. Set Up

* **Initial Meeting**: Schedule a kickoff meeting with the customer to explain the testing process and objectives.
* **Access and Permissions**: Ensure the customer has all necessary access to DocBits and Infor LN or M3 for testing purposes.

### 2. Testing Preparation

* **Training**: Provide comprehensive training to the customer’s team on how to use DocBits for invoice processing.
* **Documentation**: Share detailed documentation on the testing procedures, including expected outcomes for each test case.

### 3. Execution of Test Cases

* **Testing Environment**: Set up a testing environment that replicates the customer's production system as closely as possible.
* **Step-by-Step Testing**: Work with the customer to execute each test case, ensuring they understand each step:
  * Process invoices through DocBits.
  * Verify the output in the PO matching module.
  * Check the export results in LN or M3.

### 4. Issue Resolution

* **Tracking**: Use a tracking system (like Jira or a simple spreadsheet) to log any issues or mismatches that occur during testing.
* **Support**: Provide immediate support to resolve issues and clarify any doubts.

### 5. Verification and Feedback

* **Verification**: After each test case, verify the results with the customer to ensure accuracy.
* **Feedback Loop**: Collect feedback from the customer on the process and any improvements needed.

### 6. Finalization

* **Documentation of Results**: Document the results of each test case and provide a summary report to the customer.
* **Review Meeting**: Conduct a review meeting to discuss the testing outcomes and any further steps required before going live.

### 7. Go Live Preparation

* **Training Refresh**: Offer a refresher training session if necessary.
* **Support Plan**: Develop a support plan for the initial go-live phase to ensure smooth transition.

