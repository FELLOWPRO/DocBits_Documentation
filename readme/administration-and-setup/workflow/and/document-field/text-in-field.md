# Text in Field

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to automate actions based on the presence or absence of specific text within a specified document field. It ensures workflows can adapt dynamically to the content of documents, supporting efficient processing and accurate decision-making.

## **Components of the Card:**

1. **Text**
   * **Description:** Specifies the text string to be checked within the field.
   * **Detail:** This can be a word, phrase, or sequence of characters relevant to the workflow.
2. **Operator**
   * **Description:** Defines the condition for text presence in the field.
   * **Options:**
     * **Is:** Triggers the workflow if the specified text is present in the field.
     * **Is Not:** Triggers the workflow if the specified text is not present in the field.
3. **Field Name**
   * **Description:** Specifies the name of the document field to be evaluated.
   * **Detail:** This must match the exact identifier of the field within the document.

## **Functionality:**

1. **Condition Evaluation:** The system checks whether the specified text exists in the field, based on the selected operator (Is or Is Not).
2. **Action Execution:**
   * **True Condition:**\
     If the text's presence in the field matches the specified condition, the system initiates the associated actions. These could include triggering alerts, progressing workflows, or updating records.
   * **False Condition:**\
     If the text's presence in the field does not match the condition, alternative actions or no actions may be taken, depending on the workflow configuration.

## **Setup and Configuration:**&#x20;

* The user inputs the text to be checked. They then select the field name of the relevant document.

## **Conclusion:**

The "Text Presence in Field" workflow card is a simple yet powerful tool for document content analysis. By automating actions based on text detection, this card supports more intelligent workflows, improves document handling accuracy, and reduces manual effort.
