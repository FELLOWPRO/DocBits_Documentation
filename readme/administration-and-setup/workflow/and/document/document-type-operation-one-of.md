# Document Type Operation one of

<figure><img src="../../../../.gitbook/assets/userlmn_14ab8ac5e693d9bbe68d178795d12a9f.png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This card is designed to manage actions on documents contingent upon their type, employing simple conditional logic (is/is not) to either trigger or prevent specific workflows. This enables precise control over how different types of documents are processed within the ERP system.

## **Components of the Card:**

1. **Operator**
   * **Description**: Determines the conditional logic applied to the document types.
   * **Options**:
     * **is**: The operation will trigger if the document's type matches one of the specified types in the list.
     * **is not**: The operation will trigger if the document's type does not match any of the types listed.
2. **Document Types List**
   * **Description**: Specifies a list of document types to which the condition will apply.
   * **Detail**: This includes a variety of document types such as "Invoice", "Purchase Order", etc., based on which the condition (is/is not) will be evaluated.

## Functionality:

* **Condition Evaluation:** The system checks if the document type matches the operator condition (is or is not) against the specified list of document types.
* **Action Execution:**
  * **True Condition:**\
    If the document type satisfies the specified condition (either is or is not in the list), the workflow continues. This could trigger processes like document approvals, specific validations, or routing actions.
  * **False Condition:**\
    If the document type does not meet the condition, alternative actions are executed, such as rejecting the document or halting the workflow.

## Setup and Configuration:

* Users configure the card by selecting the document type field and defining the operator (is or is not). They then specify the list of document types to check against. The setup is straightforward, involving dropdown menus for field and operator selection and a field for entering the list of document types.

## Conclusion:

The "Document Type Condition" workflow card plays a crucial role in managing document-based operations with precision and flexibility. By using simple conditional logic, it helps ensure that documents are processed appropriately, enhancing efficiency and compliance. Documenting this card clearly will help users understand how to implement and utilize it effectively, making it a valuable part of your ERP system's documentation.
