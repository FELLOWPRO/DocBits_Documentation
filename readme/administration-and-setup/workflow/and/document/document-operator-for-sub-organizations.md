# Document Operator for Sub-Organizations

<figure><img src="../../../../.gitbook/assets/image (42).png" alt="" width="563"><figcaption></figcaption></figure>

## Purpose:

This workflow card evaluates whether a document is part of a specific sub-organization. Based on this evaluation, the workflow can either continue or trigger different actions depending on whether the document is associated with the specified sub-organization or not.

## Components of the Card:

1. **Operator**
   * **Description:** Defines whether the document must be part of the specified sub-organization or not.
   * **Options:**
     * **Is:** The document must be part of the specified sub-organization for the condition to be true.
     * **Is Not:** The document must not be part of the specified sub-organization for the condition to be true.
2. **Sub-org**
   * **Description:** Specifies the sub-organization to which the document should be compared.
   * **Detail:** This should match the sub-organization identifier. The comparison checks if the document belongs to the specified sub-organization.

## Functionality:

* **Condition Evaluation:** The system evaluates whether the document is part of the specified sub-organization. This evaluation checks the document's sub-organization against the one provided by the user.
* **Action Execution:**
  * **True Condition:**\
    If the document is part of the specified sub-organization, the workflow continues with the true condition. This could trigger further actions, such as routing the document to a specific department, applying sub-organization-specific rules, or enabling features tailored to that sub-organization.
  * **False Condition:**\
    If the document is not part of the specified sub-organization, the workflow continues with the false condition. This allows for executing alternative actions, such as sending notifications, halting the workflow, or applying general rules outside of the sub-organization's scope.

## Setup and Configuration:

* Users configure the card by selecting the document field containing the document and specifying the sub-organization to check against. The operator is then chosen from a dropdown list to define whether the document must be part of or not part of the specified sub-organization. Finally, users set the continue condition (true or false), which dictates the next step in the workflow.

## Conclusion:

The "Document in Sub-organization" workflow card is a helpful tool for automating actions based on whether a document belongs to a particular sub-organization. By ensuring documents are processed according to sub-organization-specific rules, this card improves workflow efficiency and ensures that actions are executed within the correct organizational context.
