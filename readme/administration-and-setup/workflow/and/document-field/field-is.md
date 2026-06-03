# Field is

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to automate actions based on the presence or state of a specified field within a document. By evaluating whether the field is empty, missing, or populated, it enables workflows to handle documents with precision and accuracy.

## **Components of the Card:**

1. **Field Name**
   * **Description:** Specifies the name of the field to be evaluated.
   * **Detail:** This must match the exact identifier used in the document to ensure accurate field detection.
2. **Operators**
   * **Description**: Defines the condition that triggers the workflow, based on the presence or state of the field.
   * **Options**:
     * **Empty/Not in Document:** The workflow triggers if the field is either missing from the document or is present but empty.
     * **In Document/Not Empty:** The workflow triggers if the field exists in the document and contains a value.

## **Functionality:**

* **State Detection:** The card monitors the specified field to evaluate its presence and state.
* **Condition Evaluation:**
  * The system evaluates whether the specified field is in the state (Empty/Not in Document or In Document/Not Empty) defined by the selected operator.
*

    **Action Execution:**

    * **Empty/Not in Document Condition:** If the field's state matches this condition (i.e., the field is either absent from the document or present but empty), the system initiates the associated actions. These may include generating alerts, flagging the document for review, or halting the workflow.
    * **In Document/Not Empty Condition:** If the field's state matches this condition (i.e., the field exists in the document and contains a value), the system triggers the associated actions. These could involve enabling subsequent workflow steps, updating records, or triggering notifications.

## **Setup and Configuration:**&#x20;

* Users select the field from a list of available document fields. The operator is chosen via a dropdown menu, offering clear options for "Empty/Not in Document" or "In Document/Not Empty."

## **Conclusion:**

The "Field Presence and State Validation" workflow card is a critical tool for document processing workflows, ensuring accurate handling of missing or populated fields. By automating actions based on field states, this card enhances data integrity, reduces errors, and ensures workflows operate smoothly and efficiently.
