# Set to

<figure><img src="../../../../.gitbook/assets/image (278).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to automatically set a specified field in the document to a predefined text value based on the conditions defined in the **"Where"** and **"And Sections."** It allows users to streamline data entry by ensuring fields are populated with consistent values when certain criteria are met.

## **Components of the Card:**

1. **Field Name**
   * **Description**: Specifies the field that will be updated with the text value.&#x20;
   * **Detail**: The field selected will be updated with the specified text value if the conditions in the **"Where"** and **"And Sections"** are met.
2. **Text**
   * **Description**: Defines the text value that will be set in the target field when the conditions evaluate as true.
   * **Detail**: This can be a custom message, status, or predefined value that the user wishes to write into the field. The text should align with the field's expected input format (e.g., alphanumeric, date, or other types of textual information).

## **Functionality:**

* **Condition Evaluation**: The system evaluates the conditions in the **"Where"** and **"And Sections"**:
  * If **both conditions are true**, the actions defined in the **"Then Section"** will be executed. Specifically, the target field (Field Name) will be populated with the specified text.
  * If **either the "Where" or the "And" section is false**, no action is taken, and the field remains unchanged. The **Then Section** actions are skipped entirely if either condition is false.
* **Action Execution**: If both conditions in the **"Where"** and **"And Sections"** are met, the system automatically populates the specified field with the chosen text value. If the conditions are not met, no changes are made to the field.

## **Setup and Configuration:**

To set up this card:

1. **Select the field** (Field Name) that will be updated with the text value. The available fields in the document are listed for selection.
2. **Specify the text value** that will be written into the target field when the conditions are true.
3. The action will only execute if both the **"Where"** and **"And Sections"** conditions evaluate to true.

## **Conclusion:**

The **"Set Field to Text"** workflow card offers a straightforward way to automate the population of text values into specific document fields based on predefined conditions. This reduces manual data entry and ensures consistency in document processing, making it a useful tool for automating workflows and enhancing efficiency.
