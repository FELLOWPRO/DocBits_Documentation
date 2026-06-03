# Docfield is

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to automate actions by comparing a specified document field's value with a reference value or condition. It ensures dynamic and accurate decision-making in workflows based on document data validation.

## **Components of the Card:**

1. **Field Name**
   * **Description:** Specifies the name of the document field to be evaluated.
   * **Detail:** This must match the exact identifier of the field within the document.
2. **Operators**
   * **Description:** Defines the type of comparison to be performed between the field value and the reference value.
   * **Options:**
     * **Equals (=):** Checks if the field value matches the reference value.
     * **Not Equals (≠):** Ensures the field value differs from the reference value.
     * **Greater Than (>):** Confirms the field value is greater than the reference value.
     * **Greater or Equals (≥):** Validates the field value is equal to or greater than the reference value.
     * **Lesser Than (<):** Checks if the field value is less than the reference value.
     * **Less or Equals (≤):** Ensures the field value is less than or equal to the reference value.

## **Functionality:**

* **Condition Evaluation:** The system checks whether the document field's value, in relation to its associated column, satisfies the comparison condition specified by the operator and reference value.
* **Action Execution:**
  * **True Condition:**\
    If the document field's value meets the specified condition (e.g., equals the reference value), the system triggers the associated actions. These could include updating records, progressing the workflow, or generating notifications.
  * **False Condition:**\
    If the document field's value does not meet the specified condition, alternative actions or no actions are executed, based on the workflow configuration.

## **Setup and Configuration:**

* The user selects the field name of the relevant document and chooses the operator from the drop-down menu. The user then specifies the reference field value to complete the configuration.

## **Conclusion:**

The "DocField Comparison Validation" workflow card is a robust tool for dynamic document processing. By automating actions based on field comparisons, this card streamlines workflows, enhances accuracy, and supports data-driven decision-making.
