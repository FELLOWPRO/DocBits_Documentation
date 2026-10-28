# Start Export

<figure><img src="../../../../.gitbook/assets/workflow_card_export_v1.png" alt="Workflow card Export: Start Export, version 1" width="634"><figcaption><p>Version 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_export_v2.png" alt="Workflow card Export: Start Export, version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_export_v3.png" alt="Workflow card Export: Start Export, with Validation set to Boolean, version 3" width="634"><figcaption><p>Version 3</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_export_v4.png" alt="Workflow card Export: Start Export, with Validation set to Boolean, status after export, version 4" width="634"><figcaption><p>Version 4</p></figcaption></figure>

## **Purpose:**

The **"Start Export"** workflow card is designed to initiate the export process for a document. This card functions as a trigger within the workflow to seamlessly start the export operation once the conditions in the preceding sections are satisfied.

## **Components of the Card:**

1. **Action**
   1. **Description**: Initiates the export process for the document.
   2. **Detail**: The card uses the configured export settings in the system to process and export the document.

## **Functionality:**

* **Condition Evaluation**: The system evaluates the conditions set in the **"Where"** and **"And Sections"** of the workflow. If all conditions are true, the export process begins.
* **Document Export**: The document is processed and exported using the default or previously defined export configuration.

## **Setup and Configuration:**

This card does not require specific configuration as it uses the export settings already defined in the system. Users need to ensure that:

1. The **"Where"** and **"And Sections"** conditions are correctly configured, as the card only executes if these conditions evaluate to true.
2. A valid export configuration is associated with the document in the system.

## **Conclusion:**

The **"Start Export"** workflow card provides a streamlined and automated way to trigger the export process. By relying on pre-configured settings and conditional evaluations, it ensures efficient and accurate document processing.
