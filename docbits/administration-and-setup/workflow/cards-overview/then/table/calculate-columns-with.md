# Calculate Columns with

<figure><img src="../../../../../.gitbook/assets/image (370).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

The **"Calculate Columns in Table"** workflow card is used to perform calculations between columns in a selected table. It allows users to select columns, apply a mathematical operation, and store the result in a specified result column.

## **Components of the Card:**

1. **Table Name**
   * **Description:** Specifies the **table** in which the columns will be calculated.
   * **Detail:** A dropdown list of all available **tables** is provided for selection.
2. **Column Name (1st Column)**
   * **Description:** Specifies the **first column** to be involved in the calculation.
   * **Detail:** A list of all available **columns** is provided for selection.
3. **Operation**
   * **Description:** Defines the mathematical operation to be applied between the selected columns.
   * **Options:**
     * **Add (+):** Adds the value of the second column to the value of the first column.
     * **Subtract (-):** Subtracts the value of the second column from the value of the first column.
     * **Multiply (\*):** Multiplies the value in the first column by the value in the second column.
     * **Divide (/):** Divides the value in the first column by the value in the second column.
4. **Column Name (2nd Column)**
   * **Description:** Specifies the **second column** to be involved in the calculation.
   * **Detail:** A list of available **columns** is provided for selection.
5. **Result Column**
   * **Description:** Specifies the **column** where the result of the calculation will be stored.
   * **Detail:** A list of available **columns** is provided where the calculated value will be saved.

## **Functionality:**

* **Condition Evaluation:**\
  The card only executes its action if both the **"When"** and **"And"** evaluate as true.
* **Column Calculation:**\
  The card performs the selected mathematical operation between the two chosen columns.
* **Result Storage:**\
  The result of the calculation is stored in the selected **result column**.

## **Setup and Configuration:**

* **Select Table:**\
  Choose the **table** where the columns will be calculated.
* **Choose Columns:**\
  Select the **first column** and **second column** that will be used in the calculation.
* **Select Operation:**\
  Choose the mathematical operation (**Add (+)**, **Subtract (-)**, **Multiply (\*)**, **Divide (/)**) to be applied between the columns.
* **Select Result Column:**\
  Choose the **result column** where the calculation will be stored.

## **Conclusion:**

The **"Calculate Columns in Table"** workflow card enables users to perform dynamic calculations between columns in a table, and store the results in a designated column. The card offers flexibility to apply different mathematical operations and ensures the result is stored in the specified column.

<!-- workflow-card-practical-example-20261021 -->

## Practical example

**When to use:** Calculate line totals from quantity and unit price.

**Configuration:** Select table `lines`, columns `quantity` and `unit_price`, multiplication and result column `line_total`.

**Expected result and counterexample:** A row containing `2` and `10` produces `20`. Test another row independently and diagnose missing or nonnumeric input rather than treating it as a valid total.

This is an illustrative configuration and expected outcome. Use fields, users and groups configured in your test organization; it is not a claim that this example was executed.
