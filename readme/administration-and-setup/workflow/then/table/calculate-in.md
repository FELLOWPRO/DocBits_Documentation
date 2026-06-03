# Calculate in



<figure><img src="../../../../.gitbook/assets/image (295).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

The **"Calculate with Regex Dependency"** workflow card allows users to perform calculations between columns in a selected table, with an added condition based on a regular expression (regex) pattern applied to a dependency column. If the pattern matches, the calculation is performed, and the result is stored in the specified result column.

## **Components of the Card:**

1. **Table Name**
   * **Description:** Specifies the **table** in which the columns will be calculated.
   * **Detail:** A dropdown list of all available **tables** is provided for selection.
2. **Column Name (1st Column)**
   * **Description:** Specifies the **first column** involved in the calculation.
   * **Detail:** A list of all available **columns** is provided for selection.
3. **Operation**
   * **Description:** Defines the mathematical operation to be applied between the selected columns.
   * **Options:**
     * **Add (+):** Adds the value of the second column to the value of the first column.
     * **Subtract (-):** Subtracts the value of the second column from the first column.
     * **Multiply (\*):** Multiplies the value of the first column by the value in the second column.
     * **Divide (/):** Divides the value of the first column by the second column.
4. **Column Name (2nd Column)**
   * **Description:** Specifies the **second column** involved in the calculation.
   * **Detail:** A list of all available **columns** is provided for selection.
5. **Column Name (Dependency)**
   * **Description:** Specifies the **dependency column** to which the regex pattern will be applied.
   * **Detail:** A list of all available **columns** is provided for pattern matching.
6. **Regex Pattern**
   * **Description:** Defines the **regex pattern** that will be used to match against the dependency column.
   * **Detail:** If the value in the dependency column matches the regex pattern, the calculation will be performed.
7. **Result Column**
   * **Description:** Specifies the **result column** where the calculation result will be stored.
   * **Detail:** This can be a new or existing column where the calculated value will be stored.

## **Functionality:**

* **Condition Evaluation:**
  * The card only executes its action if both the **"Where"** and **"And Sections"** evaluate as true.
  * The card only executes its action if the value in the dependency column matches the provided **regex pattern**.
* **Column Calculation:**\
  If the regex pattern matches, the card performs the selected mathematical operation between the two chosen columns.
* **Result Storage:**\
  The result of the calculation is stored in the selected **result column**.

## **Setup and Configuration:**

* **Select Table:**\
  Choose the **table** where the columns will be calculated.
* **Choose Columns:**\
  Select the **first column** and **second column** that will be used in the calculation.
* **Select Operation:**\
  Choose the mathematical operation (**Add (+)**, **Subtract (-)**, **Multiply (\*)**, **Divide (/)**) to be applied between the columns.
* **Select Dependency Column:**\
  Choose the **dependency column** where the regex pattern will be applied.
* **Define Regex Pattern:**\
  Enter the **regex pattern** that the dependency column should match.
* **Select Result Column:**\
  Choose the **result column** where the calculated value will be stored.

## **Conclusion:**

The **"Calculate with Regex Dependency"** workflow card provides a powerful way to perform calculations with conditional logic based on a regex pattern. This ensures that only rows where the dependency column matches the specified pattern will undergo the specified calculation, and the result is stored in the chosen result column.
