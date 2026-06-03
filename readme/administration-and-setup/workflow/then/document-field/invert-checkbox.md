# Invert Checkbox

<figure><img src="../../../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to invert the current state of a checkbox field. If the checkbox is checked (true), it will be unchecked (false), and vice versa. The inversion occurs based on the conditions set in the **"Where"** and **"And Sections."** This card helps automate workflows where a condition requires toggling a checkbox based on specific criteria.

## **Components of the Card:**

1. **Field Name**
   * **Description**: Specifies the checkbox field to be inverted.&#x20;
   * **Detail**: The selected checkbox field will have its state toggled from true to false or from false to true based on its current state.

## **Functionality:**

* **Condition Evaluation**: The system evaluates the conditions defined in the **"Where"** and **"And Sections"**:
  * If **both conditions are true**, the **"Then Section"** action will execute, which in this case means the checkbox field will be toggled.
  * If **either condition is false**, the card will not execute and no change will be made to the checkbox field.
* **Action Execution**: If the conditions in the **"Where"** and **"And Sections"** evaluate to true, the checkbox field's state will be inverted:
  * If the checkbox is checked (true), it will be unchecked (false).
  * If the checkbox is unchecked (false), it will be checked (true).

## **Setup and Configuration:**

To configure this card, users need to:

1. **Select the checkbox field** (Field Name) that will be inverted. The available checkbox fields in the document are listed for selection.
2. The checkbox field will only be inverted if the conditions in both the **"Where"** and **"And Sections"** are true.

## **Conclusion:**

The **"Invert checkbox \[Field Name]"** workflow card offers a simple yet powerful automation tool to toggle checkbox values based on specific conditions. By reducing the need for manual checkbox adjustments, this card enhances efficiency in document processing and ensures consistency across workflows.
