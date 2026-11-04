# Single Document Status Condition

<figure><img src="../../../../.gitbook/assets/userlmn_928e514bc0e2aa775894e4ec5f992bd9.png" alt=""><figcaption></figcaption></figure>

**Purpose**

This workflow card is tailored to manage operations on documents based on a single, specified document status. By simplifying the condition to one status, the card is focused on very specific workflow triggers, making it ideal for targeted document processing activities within an ERP system.

**Components of the Card**

1. **Operator**
   * **Description**: Specifies the method for evaluating the document’s status against the selected condition.
   * **Options**:
     * **is**: Triggers the operation if the document's current status matches the selected status.
     * **is not**: Triggers the operation if the document's current status does not match the selected status.
2. **Status**
   * **Description**: Allows the selection of a single document status to set the condition.
   * **Examples of Statuses**: "Error", "Export Error", "Ready in Validation", "Ready in Review", "Pending Approval", "Pending Second Approval".
   * **Detail**: Users choose one status from a dropdown or a set of radio buttons. This status then serves as the criterion for the card’s operation.

**Functionality**

* **Document Status Identification**: Identifies the current status of a document as it is processed through the ERP system.
* **Condition Evaluation**:
  * Based on the operator selected (`is` or `is not`), the card checks whether the document's current status aligns with the chosen status criterion.
* **Action Execution**:
  * **True Condition**: If the status matches (or does not match, based on the operator), the corresponding action is initiated. This could be routing for further processing, notification generation, or other predefined workflows.
  * **False Condition**: If the condition is not met, no action is taken, or an alternate pathway is triggered.
* **Integration with Other Workflows**: Even though it's designed for single-status evaluation, this card can be effectively integrated into broader workflow sequences to ensure precise document handling.

**User Interactions**

* **Setup and Configuration**: Users set up the card by selecting an operator and then choosing one status from the available options. This selection process is straightforward and designed to prevent confusion.
* **Monitoring and Reporting**: Enables monitoring through system-generated reports or dashboards that track the processing of documents based on their status, helping to oversee the effectiveness of the implemented workflows.
* **Error Handling and Notifications**: Configurable to alert users to any processing anomalies or to flag documents that do not meet the set conditions, ensuring prompt attention and resolution.

#### Conclusion

The "Single Document Status Condition" workflow card simplifies document management by focusing on individual status conditions. This specification helps in cases where precise control over document flows is necessary, especially in environments with stringent processing criteria. Documenting this version of the card clearly will ensure that users fully understand its application and can effectively integrate it within their daily operations, enhancing both compliance and efficiency in document processing.
