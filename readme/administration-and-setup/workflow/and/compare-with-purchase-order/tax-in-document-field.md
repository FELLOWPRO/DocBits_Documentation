# Tax in document field

<figure><img src="../../../../.gitbook/assets/image (268).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to evaluate whether the tax value in a document field matches the tax value in a purchase order, considering tolerances based on charge ID. The card compares these two tax values (one from the document field and one from the purchase order) and checks if they meet a specified condition (e.g., equals, greater than, lesser than, etc.). This helps ensure tax values are consistent and flag discrepancies for further review or approval in procurement workflows.

## **Components of the Card:**

1. **Field Name**
   * **Description**: Specifies the document field that contains the tax value to be compared with the tax value in the purchase order.
   * **Detail**: This field must match the exact identifier for the tax value in the document.
2. **Operator**
   * **Description**: Defines the condition to be applied to the comparison between the document's tax value and the purchase order's tax value.
   * **Options**:
     * **Equals (=)**: Checks if the tax in the document field matches the tax in the purchase order.
     * **Not Equals (≠)**: Ensures the tax in the document field does not match the tax in the purchase order.
     * **Greater Than (>)**: Verifies if the tax in the document field is greater than the tax in the purchase order.
     * **Greater or Equals (≥)**: Checks if the tax in the document field is greater than or equal to the tax in the purchase order.
     * **Lesser Than (<)**: Verifies if the tax in the document field is less than the tax in the purchase order.
     * **Lesser or Equals (≤)**: Checks if the tax in the document field is less than or equal to the tax in the purchase order.
3. **Master Data Table**
   * **Description**: The table that contains the purchase order details, including the charge ID and tax values.
   * **Detail**: This table must have a reference to the charge ID associated with the purchase order tax value.
4. **Tolerance Amount**
   * **Description**: The threshold amount within which the tax values can vary. This is used to account for minor discrepancies in tax calculations.
   * **Detail**: The tolerance amount should be a numeric value, defining the maximum allowed difference between the tax values.
5. **Tolerance Type**
   * **Description**: Specifies the type of tolerance being applied, either absolute or percentage-based.
   * **Options**:
     * **Value**: The tolerance is a fixed numeric value.
     * **Percentage**: The tolerance is calculated as a percentage of the tax value.

## **Functionality:**

* **Condition Evaluation:** The system evaluates whether the tax value in the document field meets the condition specified when compared to the tax value in the purchase order (with the charge ID reference from the master data table). The tolerance amount and type are considered in this evaluation to allow for minor differences in tax calculations.
* **Action Execution:**
  * **True Condition**: If the tax in the document field meets the condition when compared to the purchase order's tax (within the tolerance amount and type), the workflow continues.
  * **False Condition**: If the tax in the document field does not meet the condition (either not within the tolerance range or the comparison fails), the workflow will stop.

## **Setup and Configuration:**

* Users must select the document field that contains the tax value to be compared. They will then choose the operator for how the comparison should be made (e.g., equals, greater than). Following this, users need to specify the master data table reference and set the tolerance amount and type to account for minor tax discrepancies.

## **Example Scenario:**

* An invoice lists a tax amount of $100. The corresponding purchase order, found in the master data table, specifies a tax value of $95. Using the "Greater Than" operator, the system compares the document’s tax value ($100) to the purchase order tax value ($95) with a tolerance of $10 (absolute tolerance type). Since the difference of $5 is within the tolerance range, the workflow proceeds without triggering any alerts.

## **Conclusion:**

The "Tax in Document Field Comparison" workflow card ensures that tax values in documents align with purchase order details, allowing for minor discrepancies based on specified tolerances. By automating this check, organizations can minimize errors in tax calculations and streamline procurement processes, reducing the need for manual intervention or approvals.
