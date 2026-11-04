# Document Field Comparison

<figure><img src="../../../../.gitbook/assets/userlmn_7d5c06ce63181faee30b7bc6903e4d7b.png" alt=""><figcaption></figcaption></figure>

**Purpose**

This workflow card is designed to automatically compare the values of two specified fields within a document based on a defined operator. It's used to enforce data integrity and ensure that document data conforms to business rules or conditions.

**Components of the Card**

1. **Field Names**
   * **Description**: Specifies the names of the two fields within the document that will be compared.
   * **Detail**: Users must input the exact names of the fields as they appear in the system. These fields can be any data type that supports comparison, such as numeric, date, or text fields.
2. **Operator**
   * **Description**: The comparison operator used to evaluate the relationship between the values of the two fields.
   * **Options**:
     * **Equal (==)**: Checks if the value of the first field is equal to the value of the second field.
     * **Not Equal (!=)**: Checks if the value of the first field is not equal to the value of the second field.
     * **Greater Than (>)**: Checks if the value of the first field is greater than the value of the second field.
     * **Greater Than or Equal (>=)**: Checks if the value of the first field is greater than or equal to the value of the second field.
     * **Less Than (<)**: Checks if the value of the first field is less than the value of the second field.
     * **Less Than or Equal (<=)**: Checks if the value of the first field is less than or equal to the value of the second field.

**Functionality**

* **Field Selection**: Users input or select the names of the two fields to be compared. This is typically done through a form or a dropdown menu within the card setup.
* **Operator Selection**: Users choose an operator from a list of available options that define how the fields should be compared.
* **Comparison Execution**:
  * The system reads the values from the specified fields and applies the selected operator to evaluate the relationship between them.
  * Based on the result of the comparison (true or false), subsequent actions may be triggered. For example, if a comparison fails, the system might flag the document for review, block further processing, or notify responsible parties.

**User Interactions**

* **Setup and Configuration**: Users configure the comparison by entering field names and selecting an operator. This setup should be straightforward and guided, possibly with help text or examples.
* **Monitoring and Reporting**: The system can provide feedback on the results of comparisons, such as logging all comparisons made, their outcomes, and any actions taken in response to the comparison results.
* **Error Handling and Notifications**: Users receive alerts if the comparison cannot be executed (e.g., if one of the fields is not found in the document or is not in a comparable format).

#### Conclusion

The "Document Field Comparison" workflow card is vital for maintaining data accuracy and consistency across documents in an ERP system. It helps automate checks that would otherwise be manual, error-prone, and time-consuming, enhancing efficiency and reliability in document processing. Documenting this card clearly in your ERP system's manual will assist users in effectively employing this feature, ensuring that data across documents remains consistent and in accordance with business rules.
