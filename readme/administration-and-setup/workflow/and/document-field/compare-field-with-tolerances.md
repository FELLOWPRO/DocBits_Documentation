# Compare Field with tolerances

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to compare a field's value with a specified reference value while allowing for tolerances. It enables precise conditional processing in workflows where small deviations are acceptable, making it ideal for scenarios like quality assurance, financial analysis, or threshold-based actions.

## **Components of the Card:**

1. **Field Name**
   * **Description:** The field to be evaluated in the comparison.
   * **Detail:** This must match the exact identifier of the first field within the document.
2. **Comparison Operator**
   * **Description:** Specifies how the selected field value will be compared to the reference value.
   * **Options:**
     * **Equals (=):** Verifies if the field value matches the reference value exactly.
     * **Not Equals (≠):** Verifies if the field value does not match the reference value.
     * **Greater Than (>):** Checks if the field value is greater than the reference value.
     * **Greater or Equals (≥):** Checks if the field value is greater than or equal to the reference value.
     * **Lesser Than (<):** Checks if the field value is less than the reference value.
     * **Lesser or Equals (≤):** Checks if the field value is less than or equal to the reference value.
3. **Reference Value**
   * **Description:** The value against which the field is compared.
   * **Detail:** This value can be numeric, text, or date-based, depending on the context of the comparison.
4. **Tolerance Amount**
   * **Description:** Defines the acceptable margin of error for the comparison.
   * **Detail:** The tolerance amount is a numeric value that indicates the maximum allowable difference between the two field values for the comparison to be considered true.
5. **Tolerance Type**
   * **Description:** Specifies the unit of measurement for the tolerance amount.
   * **Options:**
     * **Value:** The tolerance is an absolute value, meaning the two fields can differ by the specified tolerance amount.
     * **Percent:** The tolerance is calculated as a percentage of the second field value, allowing for a relative margin of error.

## **Functionality:**

* **Condition Evaluation:** The system evaluates the field's value against the reference value using the selected comparison operator. If a tolerance is configured, the system considers the comparison successful if the field value falls within the defined tolerance range.
* **Action Execution:**
  * **Within Tolerance:** If the field value satisfies the condition within the specified tolerance, the workflow continues, triggering the associated actions.
  * **Outside Tolerance:** If the field value does not meet the condition or falls outside the tolerance range, alternative actions may be executed, such as logging, sending alerts, or halting the workflow.

## **Setup and Configuration:**

* Users configure the card by selecting the field to be evaluated from a list of available fields and choosing the comparison operator (e.g., equals, greater than) from a dropdown list. They then specify the reference value to compare against and define the tolerance amount, then they select the tolerance type (e.g.  percent or value).&#x20;

## **Conclusion:**

The "Field Comparison with Tolerances" card is a versatile tool for workflows requiring flexible evaluations. By enabling comparisons with tolerances, it ensures workflows remain efficient and adaptable, accommodating real-world variations without compromising on accuracy.
