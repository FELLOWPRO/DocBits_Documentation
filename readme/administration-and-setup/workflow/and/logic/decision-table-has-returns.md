# Decision Table has Returns

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This DocBits card checks whether a specified decision table has return values for a given document and determines if the returned data should be used in subsequent workflow steps. It ensures that workflows can dynamically adapt based on decision table outcomes.

## **Functionality:**

* **Decision Table Validation:** This card verifies if the selected decision table provides return values for the document being processed.
* **Decision Table Selection:** Users specify the name of the decision table to be checked.
* **Use Return Data:** Users can specify whether to use the return data in later cards with a **Boolean** setting:
  * **True:** The return data is available and will be used in subsequent workflow steps.
  * **False:** The return data will not be used, and the workflow proceeds without it.

## **Usage:**

This card is ideal for workflows involving conditional logic or decision-making based on predefined rules in a decision table. It ensures seamless integration of decision table outputs into workflow processes.

## **Example Scenario:**

* A user configures the card to check the **"Invoice Processing Rules"** decision table for return values. The **Boolean** is set to **True**, indicating that the return data (e.g. approval requirements) will be utilized in later cards to guide workflow decisions.

By using the "Decision Table Check" card, organizations can enhance workflow flexibility, streamline rule-based processing, and ensure consistency in decision-making across automated workflows.
