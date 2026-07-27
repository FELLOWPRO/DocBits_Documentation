# Collect (min/max/count) Policy

This policy collects all matching rules and either selects the **minimum**, **maximum**, or **counts** the occurrences. It only works for **Return Type Value**.

**Example:**

| Rule | Condition            | Return Value |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. If the **Collect (min)** option is selected, the result will return the **minimum** of the **Return Values** for the matching rules.
   * For the input value of **Total Amount = 2500**, the evaluation of rules would be:
     * **Rule 1**: Total Amount <= 1000 (does not match)
     * **Rule 2**: Total Amount <= 2000 (does not match)
     * **Rule 3**: Total Amount <= 3000 (matches, Return Value = 3)
     * **Rule 4**: Total Amount <= 4000 (matches, Return Value = 4)
     * **Rule 5**: Total Amount <= 5000 (matches, Return Value = 5)
   * The **matching rules** are Rule 3, Rule 4, and Rule 5, with **Return Values** of **3, 4, and 5**.
   * Since the **Collect (min)** policy is applied, the result will be the **minimum value**, which is **3**.
   * **Result**: **3**
2. If the **Collect (max)** option is selected, the result will return the **maximum** of the **Return Values** for the matching rules.
   * For the same evaluation as above, the result will be:
   * **Result**: **5**
3. If the **Collect (count)** option is selected, the result will count the **number of matching rules**.
   * For the same evaluation as above, the result will be:
   * **Result**: **3** (since 3 rules matched).
