# Export with Export Configuration

<figure><img src="../../../../.gitbook/assets/image (284).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

The **"Export Document with Export Configuration"** workflow card is designed to export a document using a specified export configuration. It provides the flexibility to ignore any pending tasks associated with the document, ensuring a smooth export process regardless of its current state.

## **Components of the Card:**

1. **Export Configuration**
   * **Description**: Specifies the export configuration to be used for processing the document.
   * **Detail**: This configuration determines the format, structure, and destination of the exported document.
2. **Ignore Pending Tasks**
   * **Description**: Determines whether pending tasks linked to the document should be disregarded during the export process.
   * **Options**:
     * **True**: Exports the document regardless of pending tasks.
     * **False**: Ensures pending tasks are completed before the export.

## **Functionality:**

* **Condition Evaluation**: The system evaluates the conditions set in the **"Where"** and **"And Sections"** of the workflow. If both conditions are true, the export process is initiated.
* **Document Export**: Using the specified **Export Configuration**, the document is processed and exported in the defined format and destination.
* **Pending Tasks Handling**: If **Ignore Pending Tasks** is set to **True**, the export process bypasses any outstanding tasks linked to the document. If set to **False**, the export is deferred until all tasks are resolved.

## **Setup and Configuration:**

To configure this card, users need to:

1. Select the desired **Export Configuration** to define how the document will be exported.
2. Choose whether to **Ignore Pending Tasks** by setting the value to **True** or **False.**
3. Ensure the conditions in the **"Where"** and **"And Sections"** are correctly set, as the card only executes its action when these conditions are true.

## **Conclusion:**

The **"Export Document with Export Configuration"** workflow card ensures documents are exported efficiently and according to predefined configurations. With the ability to ignore pending tasks, this card offers flexibility in handling documents at various stages, reducing delays and streamlining the export process.
