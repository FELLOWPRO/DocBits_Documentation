# Collect (sum) Policy

This policy collects all matching rules and sums the results. It only works for **Return Type Value**.

**Example:**

| Rule | Condition            | Return Value |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

For the input value of **Total Amount = 3500**, the evaluation of rules would be:

* **Rule 1**: Total Amount <= 1000 (does not match)
* **Rule 2**: Total Amount <= 2000 (does not match)
* **Rule 3**: Total Amount <= 3000 (matches, Return Value = 3)
* **Rule 4**: Total Amount <= 4000 (matches, Return Value = 4)
* **Rule 5**: Total Amount <= 5000 (matches, Return Value = 5)

Since the **Collect (sum)** policy is applied, we sum the **Return Values** of the matching rules, which are **3, 4, 5**.

**Summing these values** gives:

* 5 + 4 + 3 = **12**

Thus, the result returned by the decision tree would be **12**, which is the sum of all matching return values.
