# Document Type

<figure><img src="../../../../.gitbook/assets/image (16) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## Purpose:

This workflow card is designed to evaluate whether a document matches a specific type. By checking if the document corresponds to the given type, workflows can continue or take alternative actions based on this condition. This helps to automate processes where the document type dictates the next steps in the workflow.

## Components of the Card:

1. **Operator**
   * **Description**: Defines whether the document should be of the specified type or not.
   * **Options**:
     * **Is**: The document must match the specified type for the condition to be true.
     * **Is Not**: The document must not match the specified type for the condition to be true.
2. **Type**
   * **Description**: Specifies the document type to compare against.
   * **Detail**: This includes a variety of document types such as "Invoice", "Purchase Order", etc., based on which the condition (is/is not) will be evaluated.

## Functionality:

* **Condition Evaluation**: The system evaluates whether the document type in the specified field matches the condition defined by the operator. It compares the field value with the provided document type.
* **Action Execution**:
  * **True Condition**: If the document type matches the specified type (or does not, based on the operator), the workflow proceeds with the true condition. This can trigger actions such as further processing of the document, sending it for approval, or applying specific rules based on the document type.
  * **False Condition**: If the document type does not match the specified type, the workflow proceeds with the false condition. This can trigger alternative actions, such as routing the document to a different process or stopping further actions.

## Setup and Configuration:

* Users configure the card by selecting the document field that contains the document type from a list of available fields. Then, the operator is selected to define whether the document must be the specified type or not. Finally, users set the continue condition (true or false), which determines the next action based on the document type.

## Conclusion:

The "Document Type Comparison" workflow card is essential for ensuring that workflows proceed based on the type of document being processed. By comparing the document type, it helps organizations automate document routing and processing tasks, ensuring that documents are handled appropriately based on their type.
