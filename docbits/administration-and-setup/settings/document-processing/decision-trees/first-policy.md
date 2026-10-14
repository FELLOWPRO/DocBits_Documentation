# First Policy

The first matching rule is applied, and no further rules are evaluated.

**Example:**

| Rule | Condition            | Return Group |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

If the total amount is **1500**, the rules evaluated will be:

* **Rule 1**: Total Amount <= 1000 (does not match)
* **Rule 2**: Total Amount <= 2000 (matches) → The decision tree stops evaluating further rules and applies **GROUP_2**.
