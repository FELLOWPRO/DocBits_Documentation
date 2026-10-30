# All Value of

<figure><img src="../../../../.gitbook/assets/image (45).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This DocBits card is used to validate whether **all values** in a specific column of a table match a provided regex pattern. For the workflow to continue, every entry in the column must meet the condition, making this card ideal for ensuring consistency and data integrity across all entries.

## **Functionality:**

* **Regex Pattern Validation:** This card checks that **all values** in a specified column of a table match the provided regular expression pattern. The workflow will only proceed if every entry in the column meets the condition.
* **Operator:** Users define the column and specify the regex pattern. The available condition includes:
  * **Matches Regex Pattern:** Verifies that every value in the specified column matches the regex pattern.
* **Table and Column Selection:** Users specify the table and column they wish to check for complete regex pattern matches.

## **Usage:**

This card is ideal for cases where data uniformity is required, such as ensuring all phone numbers, product IDs, or other field entries adhere to a specific format. It ensures that workflows only proceed when every relevant entry is consistent with the pattern.

## **Example Scenario:**

* A user sets the card to check the "Phone Number" column in the "Contacts" table, using a regex pattern to validate phone number formats. If every phone number entry in the column matches the pattern, the card will trigger the next step in the workflow, confirming uniform data formatting.

By using the "All Values Regex Pattern Matching" card, organizations can enforce strict data standards and enhance workflow accuracy, ensuring that every entry in a specified column meets the required format before proceeding.
