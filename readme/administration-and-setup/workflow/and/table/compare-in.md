# Compare In

<figure><img src="../../../../.gitbook/assets/image (43).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This DocBits card performs a comparison between two columns in a specified table, allowing users to set conditions based on values in each column. Additionally, this card includes a dependency feature, where the comparison will only take place if the value in a third column matches a specified Python regex pattern. This setup is useful for conditional checks that depend on multiple data points within a dataset.

## **Functionality:**

* **Column Comparison with Dependency:** This card compares values in two specified columns based on a set condition, which is only applied if the value in a third "dependency" column matches a defined Python regex pattern.
* **Operators:** Users can choose the following operators for the column comparison:
  * **Equals (=):** Checks if values in the two columns are exactly equal.
  * **Not Equals (≠):** Ensures values in the two columns are not equal.
  * **Greater Than (>):** Confirms that values in the first column are greater than those in the second column.
  * **Greater or Equals (≥):** Ensures values in the first column are greater than or equal to those in the second column.
  * **Lesser Than (<):** Checks if values in the first column are less than those in the second column.
  * **Less or Equals (≤):** Ensures values in the first column are less than or equal to those in the second column.
* **Regex Dependency:** This card includes a dependency feature that allows users to define a regex pattern for a third column. The comparison condition is only applied if at least one value in the dependency column matches the regex pattern.

## **Usage:**

This card is particularly useful in scenarios where complex conditional logic is required, such as quality checks that depend on relationships between data points, with additional conditions based on data formatting or specific patterns.

***

## **Example Scenario:**

* A user configures the card to compare the "Quantity" and "Threshold" columns in a "Stock" table with the condition **Quantity ≥ Threshold**. This comparison only takes place if the "Item Code" column matches the regex pattern for specific code formats, such as **^A\d{3}$** (indicating an item code starting with "A" followed by three digits).

By using the "Conditional Column Comparison" card, organizations can create advanced, pattern-dependent comparisons within datasets, enabling fine-tuned data processing and enhanced accuracy in conditional workflows.
