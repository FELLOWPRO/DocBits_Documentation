# Change Entries with

<figure><img src="../../../../../.gitbook/assets/image (369).png" alt="Workflow Then card that changes entries in a table column using a rule" width="563"><figcaption></figcaption></figure>

## **Purpose:**

The **"Change Entries in Table"** workflow card is used to update entries in a specified database table. It allows you to select a **table** and **column**, then perform mathematical operations (addition, subtraction, multiplication, or division) on the values in that column, using a specified value.

## **Components of the Card:**

1. **Table Name**
   * **Description:** Specifies the **table** in which entries will be updated.
   * **Detail:** A dropdown list of available **tables** is provided, allowing you to select the target table for updating entries.
2. **Column Name**
   * **Description:** Specifies the **column** within the selected table to be updated.
   * **Detail:** A list of all available **columns** will be provided for selection.
3. **Operation**
   * **Description:** Defines the mathematical operation to be performed on the **column** values.
   * **Options:**
     * **Add (+):** Adds a specified **value** to the current value in the selected column.
     * **Subtract (-):** Subtracts a specified **value** from the current value in the selected column.
     * **Multiply (\*):** Multiplies the current value in the selected column by a specified **value**.
     * **Divide (/):** Divides the current value in the selected column by a specified **value**.
4. **Value**
   * **Description:** Specifies the **value** to be used in the selected operation.
   * **Detail:** This is the number that will be added, subtracted, multiplied, or divided with the entries in the selected column.

## **Functionality:**

* **Condition Evaluation:**\
  The card only executes its action if both the **"When"** and **"And"** evaluate as true.
* **Table Entry Update:**\
  The card performs the selected operation (**+**, **-**, **\***, or **/**) on the values in the chosen **column** of the selected **table, u**sing the specified **value**.

## **Setup and Configuration:**

* **Select Table:**\
  Choose the **table** where the changes will be applied.
* **Choose Column:**\
  Select the **column** within the table that you want to update.
* **Select Operation:**\
  Choose the mathematical operation (**+**, **-**, **\***, **/**) to be applied to the selected column's values.
* **Enter Value:**\
  Provide the **value** to be used in the selected operation.

## **Conclusion:**

The **"Change Entries in Table"** workflow card enables automated updates to database entries by selecting a **table**, **column**, and desired **mathematical operation**. This card is essential for performing bulk data modifications or calculations within your database.

<!-- workflow-card-practical-example-20261021 -->

## Practical example

**When to use:** Apply a numeric adjustment to an existing table column.

**Configuration:** Select demo table `lines`, numeric column `quantity`, addition and value `1`.

**Expected result and counterexample:** An existing quantity of `2` becomes `3`. Repeating this action produces `4`, so use it only when repeated addition is intended.

This is an illustrative configuration and expected outcome. Use fields, users and groups configured in your test organization; it is not a claim that this example was executed.
