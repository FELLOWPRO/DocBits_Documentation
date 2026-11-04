# Any Policy

Multiple rules can be true, but the result of those rules must be the same.

**Example:**

| Rule | Condition            | Return Group |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

If the total amount is **2500**, the rules evaluated will be:

* **Rule 1**: Total Amount <= 1000 (does not match)
* **Rule 2**: Total Amount <= 2000 (does not match)
* **Rule 3**: Total Amount <= 3000 (matches)
* **Rule 4**: Total Amount <= 4000 (matches)
* **Rule 5**: Total Amount <= 5000 (matches)

For **Any** to apply, all matching rules must return the same **Return Group**. Since the groups do not match across the different rules, the result would be **false**.
