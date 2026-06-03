# Compare Total Charges

<figure><img src="../../../../.gitbook/assets/image (271).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card compares the total charges in a document field with the corresponding charges in a purchase order. The card helps ensure that the charges in the document align with those in the purchase order, considering specified tolerance levels. The comparison can trigger actions if discrepancies are found, such as flagging discrepancies for review or adjusting charges accordingly.

## **Components of the Card:**

1. **Field Name:**
   * **Description**: Specifies the document field that contains the total charge values to be compared with the charges in the purchase order.
   * **Detail**: The value in this field represents the total charges applied in the document (e.g., invoice) and will be compared with the purchase order charge.
2. **Operator:**
   * **Description**: Defines the condition that will be applied to the comparison between the total charge in the document and the charge in the purchase order.
   * **Options**:
     * **Equals (=)**: Verifies if the total charge in the document matches the charge in the purchase order.
     * **Not Equals (≠)**: Ensures the total charge in the document is different from the charge in the purchase order.
     * **Greater Than (>)**: Verifies if the total charge in the document is greater than the charge in the purchase order.
     * **Greater or Equals (≥)**: Verifies if the total charge in the document is greater than or equal to the charge in the purchase order.
     * **Lesser Than (<)**: Verifies if the total charge in the document is less than the charge in the purchase order.
     * **Lesser or Equals (≤)**: Verifies if the total charge in the document is less than or equal to the charge in the purchase order.
3. **Tolerance Amount**
   * **Description**: Specifies the tolerance threshold for comparing the total charges.
   * **Detail**: This numeric value represents the allowed variance in charges between the document and the purchase order.
4. **Tolerance Type:**
   * **Description**: Specifies the type of tolerance that will be applied.
   * **Options**:
     * **Percentage**: Tolerance is applied as a percentage of the purchase order charge.
     * **Value**: Tolerance is applied as a fixed numeric amount.
5. **Separator:**
   * **Description**: Specifies the separator used to distinguish the Charge ID at the end of the field name.
   * **Detail**: The separator separates the charge field from the unique Charge ID that will be used to link the document charge to the corresponding charge in the purchase order.

## **Functionality:**

* **Condition Evaluation:** The system compares the total charge in the document field with the corresponding charge in the purchase order based on the operator and tolerance. The tolerance is applied to determine whether the difference between the two charges is within an acceptable range.
* **Action Execution:**
  * **True Condition**: If the charges match (considering tolerance) and the condition is true, the workflow will continue with the defined action, such as document approval or further processing.
  * **False Condition**: If the condition is false (i.e., the charges do not match within the tolerance), the workflow will not continue.

## **Setup and Configuration:**

* Users begin by selecting the document field that contains the total charge value. Next, they select the operator to define how the charge will be compared to the purchase order charge. Then, users set the tolerance amount and tolerance type (percentage or absolute). Finally, they specify the separator and Charge ID that will be used for comparison.

## **Example Scenario:**

An invoice lists a charge of $500 in the "total charges" field. The corresponding purchase order charge is $480, and the tolerance is set to $20 (absolute tolerance). The card compares the document charge against the purchase order charge:

* The total charge in the document is within the $20 tolerance of the purchase order, and the workflow continues without issue.
* If the charge exceeds the tolerance, the workflow flags the discrepancy for review.

## **Conclusion:**

The "Compare Total Charges" workflow card ensures that the charges in documents align with those in purchase orders, considering specified tolerance levels. This helps organizations automate the verification process, identify discrepancies early, and maintain better control over charge-related processes.
