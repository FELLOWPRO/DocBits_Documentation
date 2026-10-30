# Module active

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This DocBits card checks whether a specific module in the system is active or inactive. It enables workflows to proceed based on the activation status of a module, ensuring actions are only performed if the necessary module is available.

## **Functionality:**

* **Module Status Validation:** This card verifies the activation status of a specified module and evaluates it against a user-defined condition.
* **Module Selection:** Users specify the name of the module to be checked, ensuring precise validation.
* **Operators:** The following conditions can be applied:
  * **Is:** The workflow continues if the selected module is active.
  * **Is Not:** The workflow continues if the selected module is inactive.

## **Usage:**

This card is particularly useful for administrators or system managers who need to create workflows dependent on the availability or functionality of specific modules. It helps ensure that workflows are only executed when all required modules are appropriately configured.

## **Example Scenario**

* A user configures the card to check if the **"Document Processing"** module **is active.** If the module is active, the workflow proceeds, triggering automated document processing tasks. If the module is inactive, the workflow halts, preventing unnecessary actions.

By using the "Module Active Check" card, organizations can improve workflow reliability, avoid errors due to inactive modules, and ensure processes align with the system configuration.
