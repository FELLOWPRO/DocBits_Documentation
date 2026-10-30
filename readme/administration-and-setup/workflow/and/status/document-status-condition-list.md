# Document Status Condition List

<figure><img src="../../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605.png" alt="" width="521"><figcaption></figcaption></figure>

**Purpose**

This card is designed to control workflow actions based on the current status of a document, using conditional logic to either trigger or restrict certain processes. It ensures that documents only proceed through workflows when they meet predefined status criteria.

**Components of the Card**

1. **Operator**
   * **Description**: Determines how the document status will be evaluated against a specified condition.
   * **Options**:
     * **is**: Triggers the associated actions if the document’s current status matches one of the specified statuses.
     * **is not**: Triggers the actions if the document’s status does not match any of the specified statuses.
2. **Status ( List )**
   * **Description**: Lists the specific statuses against which the document’s current status will be compared.
   * **Examples**: "Error", "Export Error", "Ready in Validation", "Ready in Review", "Pending Approval", "Pending Second Approval". These represent different stages or conditions a document might be in within a workflow process.

**Functionality**

* **Status Identification**: Automatically identifies the current status of a document as it moves through the ERP system’s workflow.
* **Condition Evaluation**: Applies the chosen operator (is or is not) to the document’s status in comparison to the listed statuses:
  * If **is**, it checks whether the document’s status matches any status in the list.
  * If **is not**, it checks whether the document’s status does not appear in the list.
* **Action Execution**: Depending on the outcome of the condition evaluation:
  * **True**: Executes predefined actions or workflows if the condition is met.
  * **False**: Skips or triggers alternative workflows if the condition is not met.
* **Workflow Integration**: Integrates seamlessly with other workflow components, ensuring that document handling is coordinated across the system.

**User Interactions**

* **Setup and Configuration**: Users configure the card by selecting the operator and specifying the relevant statuses. This setup may involve simple dropdown menus or checkboxes for selecting statuses and operators.
* **Monitoring and Management**: Users can track the card’s activity via a dashboard, which provides insights into the status conditions being monitored and the actions being taken based on those conditions.
* **Error Handling and Alerts**: Supports setting up alerts for process failures or mismatches in expected document statuses, enabling quick responses to operational issues.

#### Conclusion

The "Document Status Condition" workflow card is vital for ensuring that documents are processed correctly according to their current status, enhancing control and efficiency within the ERP system. Clearly documenting this card in the system's manual will help users effectively implement and manage it, leveraging its functionality to maintain smooth and compliant document workflows. This card is particularly useful in managing document lifecycles and ensuring that only documents meeting specific criteria advance to subsequent stages of business processes.
