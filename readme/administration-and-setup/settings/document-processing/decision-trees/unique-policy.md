# Unique Policy

Ensures that only a single rule is matched. If multiple rules are matched, the decision tree will return false.

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
* **Rule 2**: Total Amount <= 2000 (matches)
* **Rule 3**: Total Amount <= 5000 (matches)
* **Rule 4**: Total Amount <= 4000 (matches)
* **Rule 5**: Total Amount <= 3000 (matches)

Since multiple rules are matched (**Rule 2**, **Rule 3**, **Rule 4**, **Rule 5**), the decision tree will return **false** because the **Unique** policy ensures only one rule can match.
