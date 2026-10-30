# Item Receiving Method

<figure><img src="../../../../.gitbook/assets/image (47).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This DocBits card checks whether items in a dataset have a specified receiving method. Users can choose to validate **any** item or **all** items in the dataset based on a selected condition, making it suitable for scenarios where workflows depend on item receiving methods, such as in supply chain management or inventory tracking.

## **Functionality:**

* **Receiving Method Validation:** This card verifies the receiving method of items against a specified condition. Users can choose between **any** item or **all** items in the dataset and set the condition as **equals** or **not equals**.
* **Item Selection:** Users can specify:
  * **Any Item:** The card triggers if at least one item meets the specified receiving method condition.
  * **All Items:** The card triggers only if all items meet the specified receiving method condition.
* **Operators:** The following operators are available to define the condition:
  * **Equals (=):** Checks if the receiving method matches the specified value.
  * **Not Equals (≠):** Ensures the receiving method does not match the specified value.

## **Usage:**

This card is ideal for warehouse managers, inventory coordinators, or logistics personnel who need to validate item receiving methods before allowing further actions, such as processing, storage, or shipping.

## **Example Scenario:**

* A user configures the card to check if **all items** have the receiving method **equals "Direct Delivery"**. If every item meets this condition, the workflow proceeds, confirming that all items are intended for direct delivery.

By using the "Receiving Method Validation" card, organizations can ensure compliance with receiving protocols, improve logistics workflows, and maintain accuracy in item handling based on specific receiving methods.
