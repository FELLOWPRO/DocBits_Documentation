# Run Workflow

<figure><img src="../../../../.gitbook/assets/image (307).png" alt="" width="563"><figcaption></figcaption></figure>

## Purpose:

The **"Run Workflow"** card allows users to dynamically execute a selected workflow from a list of available workflows. This card is useful for automating processes where multiple workflows are interconnected, enabling streamlined operations.

## Components of the Card:

1. **Workflow**
   * **Description:** Specifies the workflow to be executed when the conditions evaluate as true.
   * **Detail:** A dropdown list of all available workflows is provided for selection.

## Functionality:

* **Condition Evaluation:** The card executes the selected workflow only if both the **"Where"** and **"And Sections"** evaluate as true.
  * If either condition is false, no action is taken, and the workflow remains untriggered.
* **Workflow Execution:**
  * When the conditions are met, the specified workflow is triggered automatically.
  * If the conditions are not met, no workflow is executed.

## Setup and Configuration:

1. **Select Workflow:** Choose the workflow to be triggered from the **dropdown list** of available workflows.
2. **Define Conditions:** Configure the **"Where"** and **"And Sections"** to specify the criteria that must be met for the workflow to execute.

## Conclusion:

The **"Run Workflow"** card offers a convenient and efficient way to link workflows, automating multi-step processes with ease. By ensuring the conditions in the **"Where"** and **"And Sections"** are met, users can execute workflows dynamically and reduce manual intervention.
